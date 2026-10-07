"""Classify live harness evidence without promoting supplied state to earned history.

Requirements are reviewed metadata, not switches that force gameplay gates open.
"""
import argparse
import json
from pathlib import Path
import sys

try:
    from .gate_receipts import sha256
except ImportError:
    from gate_receipts import sha256

KINDS = {'synthetic fixture', 'managed construction', 'real save', 'rendered', 'earned campaign'}


def evaluate(report, requirements):
    """Return execution coverage and acceptance against independently supplied requirements."""
    records = []
    init = report.get('Init', {})
    plan = report.get('Plan', {})
    fixtures = bool(plan.get('Force') or any(plan.get(k) for k in
        ('SetFlags', 'StartEtudes', 'SetPresenceFailures', 'HoldEtudes', 'SeenCues', 'RemoveCompanions')))
    for save in report.get('Saves', []):
        state = save.get('State') or {}
        for group, id_field in [('Runs', 'Scene'), ('Systems', 'Scenario'), ('NativeSlides', 'Case')]:
            for run in save.get(group, []):
                supplied = fixtures or run.get('Forced', False)
                complete = report.get('Status') == 'complete' and run.get('Result') == 'completed'
                kinds = ['synthetic fixture' if supplied else 'real save']
                if run.get('Screenshots') and complete:
                    kinds.append('rendered')
                records.append(dict(case=run.get(id_field), save=save.get('ResolvedPath') or save.get('Save'),
                    chapter=state.get('Chapter'), area=state.get('Area'), contacts=state.get('AvailableContacts', []),
                    host=(run.get('Inline') or {}).get('Dialog'), path=(run.get('Inline') or {}).get('NavPath'),
                    placement=state.get('Area'),
                    mod_version=init.get('RrtVersion'), evidence_kinds=kinds,
                    complete=complete, passed=complete and run.get('Passed') is True,
                    result=run.get('Result'), group=group))
    decisions = []
    for requirement in requirements:
        if requirement.get('kind') not in KINDS or not requirement.get('case'):
            raise ValueError('Requirement needs a case and a recognized evidence kind')
        # A supplied snapshot cannot prove campaign earning. Earned campaigns need
        # separately reviewed history evidence, not a live driver's success bit.
        reasons = []
        needed = ('save', 'area', 'chapter', 'mod_version', 'host', 'path', 'placement', 'owner')
        missing = [key for key in needed if not requirement.get(key)]
        if missing:
            reasons.append('missing reviewed context: ' + ', '.join(missing))
        candidates = [r for r in records if r['case'] == requirement['case']]
        matched = []
        for record in candidates:
            gaps = []
            for key in ('save', 'area', 'chapter', 'mod_version', 'host', 'path', 'placement'):
                if not record.get(key) or record[key] != requirement.get(key):
                    gaps.append(key + ' mismatch or missing')
            if not set(requirement.get('contacts', [])).issubset(record['contacts']):
                gaps.append('missing contact')
            if requirement['kind'] not in record['evidence_kinds']:
                gaps.append('evidence kind unproved: ' + requirement['kind'])
            if not record['passed']:
                gaps.append('case skipped, failed or incomplete')
            if not gaps:
                matched.append(record)
            else:
                reasons.extend(gaps)
        if not candidates:
            reasons.append('case absent from inventory')
        passed = bool(matched) and not missing
        decisions.append(dict(requirement=requirement, passed=passed,
                              remaining=[] if passed else sorted(set(reasons))))
    inventory_complete = report.get('Status') == 'complete' and bool(records) and all(r['passed'] for r in records)
    inventory_complete &= not bool(report.get('Summary', {}).get('Skipped'))
    inventory_complete &= all(not s.get('InventoryTruncated') for s in report.get('Saves', []))
    inventory_complete &= bool(report.get('Init', {}).get('RrtVersion'))
    inventory_complete &= all(s.get('LoadOk') and s.get('State') and not s.get('NotIdle') for s in report.get('Saves', []))
    return dict(evidence=records, requirements=decisions, complete=inventory_complete,
                execution_passed=report.get('Summary', {}).get('Passed', False),
                acceptance_passed=inventory_complete and report.get('Summary', {}).get('Passed') is True
                    and bool(decisions) and all(d['passed'] for d in decisions))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--requirements', type=Path)
    parser.add_argument('--source-hash')
    parser.add_argument('--export-hash')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    if args.out.resolve().is_relative_to(root):
        parser.error('--out must be outside the repository')
    report = json.loads(args.report.read_text(encoding='utf-8-sig'))
    requirements = json.loads(args.requirements.read_text(encoding='utf-8-sig')) if args.requirements else []
    result = evaluate(report, requirements)
    result.update(schema=1, report_hash=sha256(args.report),
                  policy_hash=sha256(args.requirements) if args.requirements else None,
                  command=sys.argv if argv is None else argv, seconds=report.get('ElapsedSeconds'),
                  scene_count=report.get('Init', {}).get('SceneCount'),
                  source_hash=args.source_hash or report.get('SourceHash'),
                  export_hash=args.export_hash or report.get('ExportHash'))
    if not result['source_hash'] or not result['export_hash']:
        result['acceptance_passed'] = False
        result['identity_incomplete'] = True
    code = 0 if result['acceptance_passed'] else 2
    result['exit'] = code
    args.out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return code


if __name__ == '__main__':
    sys.exit(main())
