#!/usr/bin/env python3
"""Deterministic L1-L6 cross-route audit gate (report mode by default).

python tools/crossroute_lint.py [--story development/Story.json] [--strict]
    [--json /tmp/report.json] [--text /tmp/report.txt]
    [--baseline tools/crossroute_lint_baseline.json] [--write-baseline]
    [--markdown tools/crossroute_lint_report.md] [--details]

Report mode exits 0. --strict exits 1 for any finding not in the reviewed
baseline. Baseline writing is explicit and cannot be combined with --strict.
JSON/text/Markdown are alternate reports of the same sorted finding set.
"""
import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.crossroute_checks import (other_woman, commander_alive, location_staging,
                                    late_commitment, world_facts, left_trickster)
from tools.crossroute_checks.common import Proof, blocks, verify
from tools.lastcall_entitlement_lint import errors as entitlement_errors

CHECKS = (other_woman, commander_alive, location_staging, late_commitment, world_facts, left_trickster)
BASELINE = ROOT / "tools/crossroute_lint_baseline.json"

CALIBRATION = """## Calibration

Hand-checked on the regenerated branch export against `Rules.Available`,
`RouteOpen`, `ParticipantsAvailable`, `ParagraphVisible`, the actual scene
choices, and the blueprint/localization sources cited in the check modules.
eng7-l13 adds generator guards to L4 producers/consumers and the mandatory
existing refusal/consequence contracts. Node prose and saved identifiers stay
unchanged. The original L1/L2/L3/L5/L6 calibration below remains applicable.
L1 name-only findings deliberately
retain the task's broad name policy (including letters and recollections);
`:physical` findings additionally assert actual staging.

| Check | Sample | Condition logic / result |
| --- | --- | --- |
| L1 | `chadali.trickster.epilogue.lucky_night`, Eritrice mentions | Chadali's commitment and Council return do not establish Eritrice's separate live route; reported. |
| L1 | `galfrey.trickster.iz.road/irabeth` and `/irabeth2` | Incoming choice forbids Irabeth's losses, but no matching physical contact/presence/participant contract; physical finding retained. |
| L1 | Household named-seat fixture | Naming only one seat does not prove the other woman present or alive; all incoming choice paths and paragraph conditions checked. |
| L2 | `iomedae.trickster.epilogue.lived` and living Last Call pages | Scene sacrifice forbids/earned Commander return establish life; no findings. Paragraph and unreturned-sacrifice negative fixtures reject leaks. |
| L3 | `horzalah.trickster.react.wenduag_morning/start` | Citadel staging, Chapter 5, no area gate; reported. |
| L3 | `horzalah.trickster.visit.chamber/room` | Explicit prior room-fold journey on every incoming path earns an authored location variant; removed the initial false positive. |
| L3 | `shamira.trickster.ch4.read/war` | Drezen is mental imagery in a narrated mind search; removed the initial false positive. Drezen wardrobe starts elsewhere remain findings. |
| L4 | `devarra.trickster.epilogue.woken` | Live RouteOpen now guards the outcome; matching earned returns still lift only their losses. |
| L4 | `iomedae.trickster.disputation/torches/choice[0]` | Generator requires `trickster.now`; mutation removing it reproduces L4. |
| L4 | Jannah `blade`, `the_watch`, `anything_but_wings`, `your_part`, and flirt siblings | Each romantic incoming edge reads NOT declined OR existing chalk-circle repair. The repair producer remains selectable. |
| L4 | Nenio `commit.result` clean branch / replication / committed article | Clean incoming branch forbids tampering; replication records the authored repair. All commitment producers and all contamination producers prove the immutable control invariant. Removed the article's initial false positive; generator guards the folio siblings, and kissing during isolation records the existing tampering consequence. |
| L4 | Konomi `ending_private` and sibling ending pages | Forbidding `dead.unreturned` covers the current retained corpse through the central live lifecycle observer. Current sources imply their history latch; the latch never implies current life. Removed these initial false positives after checking `KonomiRecovery.ObserveLife/ReadLifecycle` and `Main.State`. |
| L5 | `chadali.trickster.epilogue.lucky_night/page/paragraph[15]` | `hoped_aloud` does not imply native `Ending_WoundClosed`; reported. |
| L5 | `kaylessa.trickster.epilogue.declined/page` | Claims closure without the closure etude; Crossroads history remains possible; reported. |
| L5 | Iomedae ending `closed` branch / conditional paragraph fixture | Incoming choice or paragraph requirement establishes the closure flag; accepted. Unrelated OR arms cannot prove it. |
| L6 | All return producers and native variants | Existing T1–T7 diagnostics are reused; no branch findings. Synthetic historical-only return, native edit and variant fixtures produce L6; live-path versions pass. Specific already-earned native settlements retain T6's historical-consequence exception. |

False-positive class fixes applied to the lint: attach actions to their named
subject inside narration, distinguish voice/sending from physical staging,
resolve group-seat guards separately, honour built-in `inhuman` exclusions,
derive central ChapterFlag inputs from the scene's actual window,
retain choice guards on every incoming path, invalidate affected entry guards after
flag mutations, distinguish memory and explicit travel from initial location,
prove already-earned control repairs without treating history as live power,
and recognise the central retained-body live observer without accepting its
historical confirmation as a live witness.

## Proof limits

Text recognition uses documented finite place/fact/reward vocabulary; newly
worded facts and indirect pronoun-only staging still need editorial review.
Ambiguous bare titles (queen, lady, dragon) cannot identify a woman; specific
titles and attested short names are included. Generic camp/room/window names
do not determine a unique geography. Authored flags, nonpersistent latches,
cycles and Counts are opaque unless an existing central predicate establishes
the guard. Missing central lifecycle registrations need route-owner review.
The baseline records debt, not permission to grant an unearned outcome.
Fingerprints include full text, effective conditions, required predicates and
location/participant metadata; changed baselined gates require a new review.
"""


def check(story):
    model = verify.Model(story)
    items = list(blocks(model))
    proof = Proof(model)
    results = [finding for module in CHECKS for finding in module.check(model, items, proof)]
    # Multiple sentences may assert the same fact; retain distinct excerpts.
    unique = {f["fingerprint"]: f for f in results}
    return sorted(unique.values(), key=lambda f: (f["route"], f["check"], f["scene"], f["node"], f["slot"], f["subject"], f["fingerprint"]))


def report(findings, baseline=(), all_routes=()):
    known = set(baseline)
    counts = collections.Counter(f["check"] for f in findings)
    routes = collections.defaultdict(collections.Counter)
    for route in all_routes:
        routes[route]  # zero-finding routes belong in the per-route audit too
    for f in findings:
        routes[f["route"]][f["check"]] += 1
    return dict(schema=1, counts={"L%d" % n: counts["L%d" % n] for n in range(1, 7)},
                routes={r: dict(sorted(v.items())) for r, v in sorted(routes.items())}, findings=findings,
                new_findings=[f for f in findings if f["fingerprint"] not in known],
                stale_baseline=sorted(known - {f["fingerprint"] for f in findings}))


def text_report(result, details=False):
    lines = ["cross-route lint: %d findings, %d new; %s" % (len(result["findings"]), len(result["new_findings"]),
             ", ".join("%s=%d" % pair for pair in result["counts"].items()))]
    if details:
        for f in result["findings"]:
            lines.append("%s %s %s/%s/%s [%s]: %s | %s" %
                         (f["check"], f["route"], f["scene"], f["node"], f["slot"], f["subject"], f["missing_condition"], f["excerpt"]))
    else:
        for route, counts in result["routes"].items():
            lines.append("  %s: %s" % (route, ", ".join("%s=%d" % pair for pair in counts.items()) or "0 findings"))
    return "\n".join(lines) + "\n"


def markdown_report(result):
    lines = ["# Cross-route lint baseline", "", "Generated by `python tools/crossroute_lint.py --markdown tools/crossroute_lint_report.md`.",
             "Counts are findings, not unique scenes. Baseline records existing debt; it does not approve route conditions.", "",
             "| Route | L1 | L2 | L3 | L4 | L5 | L6 | Total |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for route, counts in result["routes"].items():
        values = [counts.get("L%d" % n, 0) for n in range(1, 7)]
        lines.append("| %s | %s | %d |" % (route, " | ".join(map(str, values)), sum(values)))
    lines.append("| **Total** | %s | %d |" % (" | ".join(str(result["counts"]["L%d" % n]) for n in range(1, 7)), len(result["findings"])))
    lines += ["", "Full findings, excerpts and missing conditions: `tools/crossroute_lint_baseline.json`.", "", CALIBRATION.rstrip()]
    # eng7-l13: every residual has an explicit route/scene disposition. These
    # are retained review debt outside the L4 lane, not silently waived facts.
    lines += ["", "## eng7-l13 residual dispositions", "",
              "L4 is fully burned down. Explicit historical/negative exemptions and the existing mandatory consumer contracts are in `tools/earned_outcome_inventory_contracts.json`. Aeon's rewritten history retains its existing exception. Exact non-romance framework milestone flags (Shyka's paid page receipt, the Long Con talk, Ledger and table milestones) are documented separately; the exemption never hides another romantic producer on the same answer. Shyka's paid page retains its mandatory no-abort completion. Solo Minagho/Chivarro outcomes read the named woman's losses plus common route blockers, using SeatWomen; the absent partner is not required. Chivarro's own walk-out still reads the existing WON_BACK repair; Minagho's solo road ignores that other woman's walk-out. Late-road keys are checked as producers in their own right, including existing refusal forbids on pages that read raw terms. Existing ForbidOverrides remain repair roads, including Chadali's authored hall_sealed fallback. They retain their preparation inputs and read current route/refusal/control eligibility; new Trickster acts at their consumers additionally read trickster.now. Historical paid consequences retain trickster.ever.", "",
              "Every row below is a **route-prose follow-up**, retained for its route owner. L1 needs a review of the quoted mention/staging and its participant contract; memories/letters may need a documented false-positive exemption, while current bodies need earned presence. L3 needs location/travel staging checked against the quoted scene. L5 needs the stated world fact checked against a native witness or fact-neutral prose. This lane supplies no new return, cost, gate or prose for those classes. The baseline retains each individual fingerprint and full missing predicate.", "",
              "| Check | Route | Scene / node / slot | Subject | Missing evidence / follow-up | Quoted evidence |", "| --- | --- | --- | --- | --- | --- |"]
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    for f in result["findings"]:
        where = "/".join((f["scene"], f["node"], f["slot"]))
        lines.append("| %s |" % " | ".join(map(cell, (f["check"], f["route"], where, f["subject"], f["missing_condition"], f["excerpt"]))))
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--story", type=Path, default=ROOT / "development/Story.json")
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write-baseline", action="store_true")
    parser.add_argument("--json", type=Path)
    parser.add_argument("--text", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--details", action="store_true")
    args = parser.parse_args(argv)
    if args.strict and args.write_baseline:
        parser.error("--strict cannot write its own baseline")
    story = json.loads(args.story.read_text(encoding="utf-8-sig"))
    findings = check(story)
    # eng7-l13: serialized call/coda/Book/journal parity is also mandatory.
    entitlement_failures = entitlement_errors(story)
    baseline = json.loads(args.baseline.read_text(encoding="utf-8-sig")) if args.baseline.exists() else {"findings": []}
    if baseline.get("schema", 1) != 1 or not isinstance(baseline.get("findings"), list):
        parser.error("invalid baseline schema")
    known = [f["fingerprint"] for f in baseline["findings"]]
    if args.write_baseline:
        args.baseline.write_text(json.dumps(dict(schema=1, findings=findings), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        known = [f["fingerprint"] for f in findings]
    result = report(findings, known, story.get("Relationships") or {})
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    output = text_report(result, args.details)
    print(output, end="")
    for failure in entitlement_failures:
        print("L4 entitlement contract: " + failure)
    if args.text:
        args.text.write_text(text_report(result, details=True), encoding="utf-8")
    if args.markdown:
        args.markdown.write_text(markdown_report(result), encoding="utf-8")
    return int(args.strict and bool(result["new_findings"] or entitlement_failures))


if __name__ == "__main__":
    sys.exit(main())
