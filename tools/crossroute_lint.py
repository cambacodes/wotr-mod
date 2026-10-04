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

CHECKS = (other_woman, commander_alive, location_staging, late_commitment, world_facts, left_trickster)
BASELINE = ROOT / "tools/crossroute_lint_baseline.json"

CALIBRATION = """## Calibration

Hand-checked on the regenerated branch export against `Rules.Available`,
`RouteOpen`, `ParticipantsAvailable`, `ParagraphVisible`, the actual scene
choices, and the blueprint/localization sources cited in the check modules.
No prose or route condition was changed. L1 name-only findings deliberately
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
| L4 | `devarra.trickster.epilogue.woken` | A historical return plus commitment does not establish today's closed/departure eligibility; reported. |
| L4 | `iomedae.trickster.disputation/torches/choice[0]` | Sets commitment with historical `trickster.ever`, without live-path evidence; reported. |
| L4 | `jannah.circle.measure/measure_line/choice[1]` | Romantic response can follow `declined` without `chalk_circle.walked_in`; reported. The repair choice itself remains legitimate. |
| L4 | Nenio `commit.result` clean branch / replication / committed article | Clean incoming branch forbids tampering; replication records the authored repair. All commitment producers and all contamination producers prove the immutable control invariant. Removed the article's initial false positive; unguarded folio romance still reported. |
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
    lines += ["", "Full findings, excerpts and missing conditions: `tools/crossroute_lint_baseline.json`.", "",
              # eng7-l12: preserve q6a's calibration as historical evidence;
              # every remaining debt row has its own route/scene/block referral.
              "## eng7-l12 disposition", "",
              "E-Q7-15: authored venue contracts cover physical Remote/manual reads, travelling hubs, visitors and Threshold callbacks. "
              "L3 cutaways, recollections, origins, similes and explicit wardrobe travel are distinguished from present staging; unrelated staging in the same block still fails.", "",
              "E-Q7-16: native closed-Wound paragraphs and disjoint neutral alternatives preserve earned endings in Crossroads worlds. "
              "Kenabres evidence establishes city rebuilding, not a cathedral. Aeon Irabeth remains unmarried and Anevia dead. "
              "The separately cited Chadali-spoke paragraph and Horzalah inline c6_retry copies are absent in 4a28a03; no obsolete content was reintroduced.", "",
              "E-Q7-05: living continuation contracts cover every sibling, including mourning/allowlisted pages. "
              "Unreturned sacrifice selects bereavement; existing earned Commander returns retain the living alternative. Historical costs remain. "
              "No new device, price, commitment or repair gate was added.", "",
              "L2/L3/L5/L6 are zero. Remaining L1/L4 rows below are route-prose follow-ups, not approved outcomes. "
              "Appended neutral/bereavement alternatives retain applicable L1/L4 debt, so their fingerprints are separately enumerated. "
              "No remaining row is dismissed as a false positive without evidence.", "",
              "## Remaining finding referrals", "",
              "Each row maps one baseline fingerprint to the exact consumer and the guard still needing route-owner review. "
              "Resolve the stated guard or supply history-neutral prose; preserve deliberate kills, closures and existing prices.", "",
              "| Finding fingerprint | Class | Route | Scene / node / block | Follow-up |",
              "| --- | --- | --- | --- | --- |"]
    for f in result["findings"]:
        block = "%s / %s / %s" % (f["scene"], f["node"], f["slot"])
        detail = "%s: %s" % (f["subject"], f["missing_condition"])
        lines.append("| `%s` | %s route-prose follow-up | %s | %s | %s |" %
                     (f["fingerprint"], f["check"], f["route"], block, detail.replace("|", "\\|")))
    lines += ["", "## Historical q6a calibration", "",
              "The following calibration describes the input before eng7-l12 repairs; its reported L3/L5 examples are now resolved. "
              "It remains here as the original evidence and proof-limit record.", "", CALIBRATION.rstrip()]
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
    if args.text:
        args.text.write_text(text_report(result, details=True), encoding="utf-8")
    if args.markdown:
        args.markdown.write_text(markdown_report(result), encoding="utf-8")
    return int(args.strict and bool(result["new_findings"]))


if __name__ == "__main__":
    sys.exit(main())
