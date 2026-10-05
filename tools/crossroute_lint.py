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

eng7-l14 refines L1 and wires live cross-route guards at generation time.
Names alone do not assert life. Explicit recollection, mourning, reputation,
religious titles/invocations and surviving objects may remain ungated. Staging,
speaking, current reactions and plans require the woman's current route state,
including the existing registered earned returns. Past tense in an epilogue
describes future life and is not itself a history exemption. Each occurrence
is checked separately; a memory mention cannot exempt a second live mention.
The classifier is `tools/crossroute_checks/mention_context.py`; its conservative
default is a live claim, with regression fixtures for both classes.
Relative clauses and coordinated predicates about today's actor take
precedence over history, relic, comparison and reputation exemptions:
"remember Seelah, who now waits" and "Seelah is brave and stands" still need
life. Conditional meeting plans also need life. A first-year visit in an
epilogue describes postwar life, not an earlier campaign recollection.
Actions by another actor reacting to her name or relic (a knight of her company)
do not establish the named woman's presence. These cases are checked alongside
unreturned-loss exclusion and satisfiable earned-return regression worlds.
The paid receipt for the silver dragon's festival-square promise records the
prologue morning and remains readable without resurrecting Terendelev. A new
live visit in the same clause still requires her existing earned return.
The caves' witnesses likewise recall the first encounter and Terendelev's
earlier healing; their own current speaking cues remain presence-guarded.
The two Soana death receipts explicitly date Camellia's killing to the crusade,
so the remembered perpetrator need not survive to the ending. A coordinated
future visit or separate live cameo remains subject to current availability.

| Check | Sample | Condition logic / result |
| --- | --- | --- |
| L1 | `chadali.trickster.epilogue.lucky_night`, Eritrice mentions | Live Eritrice cameos now read her own current availability; Chadali's commitment never proves it. |
| L1 | `galfrey.trickster.iz.road/irabeth` and `/irabeth2` | Live guest narration now carries the explicit authored participant contract and current route losses, without requiring a household commitment or a visitor clone. |
| L1 | Household named-seat fixture | Naming only one seat does not prove the other woman present or alive; all incoming choice paths and paragraph conditions checked. |
| L2 | `iomedae.trickster.epilogue.lived` and living Last Call pages | Scene sacrifice forbids/earned Commander return establish life; no findings. Paragraph and unreturned-sacrifice negative fixtures reject leaks. |
| L3 | `horzalah.trickster.react.wenduag_morning/start` | Citadel staging, Chapter 5, no area gate; reported. |
| L3 | `horzalah.trickster.visit.chamber/room` | Explicit prior room-fold journey on every incoming path earns an authored location variant; removed the initial false positive. |
| L3 | `shamira.trickster.ch4.read/war` | Drezen is mental imagery in a narrated mind search; removed the initial false positive. Drezen wardrobe starts elsewhere remain findings. |
| L4 | `devarra.trickster.epilogue.woken` | Live RouteOpen now guards the outcome; matching earned returns still lift only their losses. |
| L4 | `iomedae.trickster.disputation/torches/choice[0]` | Integrated scene entry requires `trickster.now`; mutation removing its effective entry/answer guard reproduces L4. |
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

## eng7-l14 scope and rule

`storylines/crossroute_presence.py` runs after all route generators. Ordinary
scene guards exclude a live inverse of the existing availability contract. It
reads native losses and registered earned overrides without adding timed
Requires inputs or restarting the scene's original DelayHours. Optional live
branches instead guard incoming answers where a neutral alternative is proved
selectable, so a refused guest does not suppress the owner's scene. Native
present/departure inputs do not establish life: if such an optional branch's
input survives a later loss, appended answers retain its existing no-guest
targets and costs. No original answer is retargeted. Mixed fetched-return
receipts retain the historical sentence and append a guarded future visit.
Fixed departure hosts and forbidden relationship-state reads use the equivalent
guarded composite. Guest losses, closure and body exclusions stay inside this
live composite across ordinary routes, preserving reader contracts in Long Con, Last
Call, Nenio, Elyanka and siblings. The explicitly scoped Long Con native-host
adapter retains its original direct overrides; registered returns and neutral
histories stay intact.
Native reactions without foreign relationship-state losses read direct native
losses and registered return overrides, including an earned return added after
a snapshot was built. Other reactions use the equivalent inverse exclusion.
Optional ending cameos
append guarded paragraphs; original paragraph indices are retained. The mixed
Irabeth negotiation appends one neutral page and four answers after the original
indices; the original live page and answer targets remain. Four remembered
spousal remarks receive authored past attribution, and Irabeth's road refusal
refers to Anevia's departure without asserting a present meeting. Existing
memory/dream forms assert a remembered/imagined actor, not current life.
No commitment, attraction, new payment, new return or native actor substitution
is introduced. Pair seats inspect only the named woman's losses.
Incoming paths may express the same guard through different native/derived
conditions. L1 proves every edge, applies its flag changes, and inherits an
earlier invariant only when the edge cannot change its inputs; a shared
spelling is not required. Unproved cycles remain failures. Native flags are
read directly on an edge already proving every registered earned override,
so a previously computed absence cannot veto a newly recorded return.
Only a genuinely neutral target is eligible as a no-guest fallback. Shared
Swarm/true-Lich body exclusions remain at ordinary scene entry when neither
owner nor guest has an earned override; changed epilogues remain reachable.

An empty relationship loss list is not proof that a canon-dead body exists.
Hepzamirah, Delamere and Terendelev read their existing
`<woman>.trickster.returned` and `trickster.ever` producers; no return is
produced here. Terendelev's existing parent-lich binding veto and Nidalynn's
`left_with_it` veto are read from their registered presence contracts.
Shyka's paid reading repeats an earlier morning in the Commander's voice;
only that quotation, before the narrated loss of the memory, is historical.
Later live cameos remain guarded. The page's existing payment choices and
foresight/echo producers are unchanged.

The existing `irabeth.trickster.second_ask/price` conditional courier offer and
`second_ask/morning`, `nevi_reply/morning` letter clauses read distant life,
including death exclusions. The pen/discharge price, decline prerequisites and
three-day reply remain in the original route. These clauses do not make Anevia
return to Drezen. Other staged/meeting clauses still exclude unreturned
`anevia_gone`. Removing the existing correspondence prerequisites removes this
narrow exception; no generic remote/departed exemption is allowed.

The Long Con's original Irabeth host contract separately declares
`irabeth_gone -> irabeth.trickster.returned` in ForbidOverrides. Its native
contact is the registered `irabeth.presence` unit; its summons uses the same
existing paid adapter. L1 preserves this explicit contract only for Long Con
Irabeth native-contact or letter pages carrying that original override. Gone
without the registered return remains excluded. Other routes, unrelated
contacts and later departure vetoes do not inherit it. Matching existing
contacts prove staging through this host contract, without requiring an
unrelated generic availability key or a visitor clone.

Native Cue_0310 (`ccd140dbf2603734aa323261c2445bec`, enGB
`cc716238-3702-4913-977d-6189665672b7`) establishes that the living Tirabades
leave Mendev together after Irabeth's humiliation. The existing paid wardrobe
reaches Anevia's south-road lodging; its `beth_left` page and the subsequent
native south-road clauses read that earned access plus Irabeth's current life.
They do not return Irabeth to Drezen or reopen her closed romance. Her death
still needs her registered return. If a subsequent loss prevents the living
wardrobe cameo, appended answers lead to its existing reproach/killer pages;
the Commander’s deliberate killing remains acknowledged. Removing the existing
paid/returned-host prerequisites removes this native-contact exception.

An authored participant key is not proof by its spelling: L1 independently
proves the route's current losses as well as the key. The Tirabades' independent
romance refusals do not remove a living native wife or officer from ordinary
cross-route dialogue. Native companions may also remain when their native
losses are all clear; their custom returns still require the romance route
open, so a hard post-return departure is retained. Other routes retain their existing closure guard,
including deliberate departures. Own romance and household closure gates
remain unchanged. Native bound
speakers and verified native audiences do not need a recreated visitor
clone. A fixed native inline audience retains its original Requires/Forbids
lists and conjoins the identical live predicate as a singleton
RequiresAnyGroups entry; existing alternatives cannot bypass it.
The Minagho citadel and Nocticula Summit witnesses are cited beside
`NATIVE_AUDIENCES` and verified against `/wrath/blueprints.zip` and `enGB.json`.
MeetCamelia's Cue_0007 likewise stages Seelah in the caves before its Prologue
list. Chapter 0 has no ChapterFlag or paid return opportunity; its native
companion audience reads current loss exclusions directly, keeping the
path-neutral introduction available without a Chapters 1–6/Trickster reader.

E-Q7-29 is owned by l11 (`eng7-l11-task.md` and its implementation report);
this lane does not duplicate its attachment mechanism or timing decision.

The retained L4 row for
`anevia.trickster.epilogue.nailed_wardrobe_lover/end/paragraph[18]` is the
appended visit half of the existing fetched-return receipt. Splitting that
receipt exposes its existing missing owner-RouteOpen condition in two slots;
the new Irabeth guard narrows the visit and grants no new outcome. That
owner-route follow-up remains outside this lane.
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
              "L2/L3/L4/L5/L6 are zero. Remaining L1 rows below are route-prose follow-ups, not approved outcomes. "
              "Appended neutral/bereavement alternatives retain applicable L1 debt, so their fingerprints are separately enumerated. "
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
    # eng7-l13: every residual has an explicit route/scene disposition. These
    # are retained review debt outside the L4 lane, not silently waived facts.
    lines += ["", "## eng7-l13 residual dispositions", "",
              "L4 is fully burned down. Explicit historical/negative exemptions and the existing mandatory consumer contracts are in `tools/earned_outcome_inventory_contracts.json`. Aeon's rewritten history retains its existing exception. Exact non-romance framework milestone flags (Shyka's paid page receipt, the Long Con talk, Ledger and table milestones) are documented separately; the exemption never hides another romantic producer on the same answer. Shyka's paid page retains its mandatory no-abort completion. Solo Minagho/Chivarro outcomes read the named woman's losses plus common route blockers, using SeatWomen; the absent partner is not required. Chivarro's own walk-out still reads the existing WON_BACK repair; Minagho's solo road ignores that other woman's walk-out. Late-road keys are checked as producers in their own right, including existing refusal forbids on pages that read raw terms. Existing ForbidOverrides remain repair roads, including Chadali's authored hall_sealed fallback. They retain their preparation inputs and read current route/refusal/control eligibility; new Trickster acts at their consumers additionally read trickster.now. Historical paid consequences retain trickster.ever.", "",
              "The exact remaining route-prose referrals appear in the eng7-l12 table above.", "",
              "## eng7-integ4 baseline review", "",
              "All 76 changed L1 fingerprints match the prior integrated baseline by check, route, scene, node, slot, subject, excerpt, missing condition and required predicate. Their guard contexts changed when l13 added live eligibility; no prose, location or participant contract changed. The combined baseline retains 1,681 existing L1 referrals (previously 1,685). Added live outcome proof resolves four prior rows: anevia.ending_changed_power/end/paragraph[8] (Irabeth), irabeth.ending_ascent/end/text (Iomedae), and irabeth.ending_changed/end/paragraph[6] and paragraph[14] (Anevia). No new finding class or prose was waived. L2/L3/L4/L5/L6 are zero."]
    # eng7-l14: every retained fingerprint gets a concrete owner/location and
    # evidence. Baseline debt in other checks stays visible rather than being
    # mistaken for a completed L1 repair or silently removed.
    lines += ["", "## Remaining findings: route follow-ups", "",
              "Every row below is retained debt outside the L1 presence lane. The missing condition and excerpt are the evidence for the route owner; no row grants permission to bypass that condition.", "",
              "| Check | Route | Scene / node / slot | Subject | Required follow-up and evidence |",
              "| --- | --- | --- | --- | --- |"]
    for f in result["findings"]:
        clean = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        lines.append("| %s | %s | `%s/%s/%s` | %s | %s — %s |" % tuple(clean(v) for v in (
            f["check"], f["route"], f["scene"], f["node"], f["slot"], f["subject"],
            f["missing_condition"], f["excerpt"])))
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
