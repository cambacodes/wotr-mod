# Arsinoe round 4 local residue

Base reviewed: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
Changes are uncommitted, per the final task instruction. No independent score is claimed.

## CHANGES

| Finding | Status | File and evidence |
| --- | --- | --- |
| arsinoe:D01 | DONE | `storylines/arsinoe_campaign.py`, `arsinoe_the_first_cart/expected`: disputes the accusation using the preceding missed payment, hearing and revised dates. Admits impatience without inventing a stocking surcharge or humiliating Senn. Removes the embedded Commander reassurance. |
| arsinoe:D02 (also S3) | DONE | Same file, `arsinoe_what_she_asks/start`: the callback now identifies the safe passage and stairs. It applies to both full and staged repairs without claiming a repaired room or completed upper landing. |
| arsinoe:D03 | ESCALATE; unresolved | The sole promise remains unchanged. Its only outcome reader is the shared ordinary-payoff alternative. There is no existing route-local discovery/renegotiation design or knowledge producer in the four Arsinoe modules. Shared accountability support is needed; no substitute promise, commitment gate or cross-route exclusion was added. |
| arsinoe:D04 | DONE | `storylines/arsinoe_continuation.py`, `arsinoe_price_of_an_evening/price_objection,terms`: uses the audit's explicit Arsinoe-sponsorship alternative. Two guests pay, Arsinoe covers the other four chairs, including the Commander. `arsinoe_courtyard_company/start` shows Neral pocketing her payment; `arsinoe_another_hour/public` states the same division. No player charge is promised or silently waived. |
| arsinoe:D05 | DONE | Same file and proposal nodes: Arsinoe pays for the entire private evening. The same payment handoff and `arsinoe_another_hour/private` confirm her expenditure and limited ability to repeat it. No new debit, affordability gate or receipt is required because this arrangement assigns no player payment. |
| arsinoe:D06 | OUT OF SCOPE pending S4 | Passage inspection needs the approved physical site, mason actor and inspectable damage point. No S4-approved delivery sheet is present in the supplied plans. No completion flag was substituted for world delivery. |
| arsinoe:D07 | OUT OF SCOPE pending S4 | Negotiation actors and observable loan/staged project variants require the same approved site/runtime contract. Existing dialogue and agreements retained. |
| arsinoe:D08 | OUT OF SCOPE pending S4 | Workbench and persistent carving prop require approved object/placement support. Existing choices and Orvena's authorship retained. |
| arsinoe:D09 | OUT OF SCOPE pending S4 | Completed cart route versus staged pedestrian barriers/traffic require approved world-state delivery. The prose fix to her loan judgment does not claim to fix that runtime omission. |
| arsinoe:D10 (also S3) | DONE | `storylines/arsinoe_continuation.py`, `arsinoe_courtyard_company/quiet`: discussion occurs before the last guest leaves. Final shelving no longer repopulates the gathering; Neral waits to close her courtyard. |
| arsinoe:D11 (also S3) | OUT OF SCOPE shared Last Call; wording supplied | The duplicate is in the Arsinoe entry of `storylines/earned_outcomes.py`, appended after the existing account in `storylines/lastcall_partners.py`. Neither shared host was edited. Replace only the appended paragraph's text with: `{n}Her shop opened late the next morning. Afterward, Arsinoe made a habit of closing on time when she had an evening promised to the Commander.{/n}`. Preserve its acceptance/history guards and index; retain the preceding spring arrival. |

`tests/test_arsinoe_round2.py`: the quick gate exposed an obsolete brief assertion. It now compares each brief's ending against the following node's first beat, using the established slot-brief contract, rather than expecting an old placeholder spoken line. All five endpoints and existing anatomy/narration checks remain asserted. No brief or slot prose changed.

No route-owned Arsinoe section occurs in S1. S3's two local items are fixed; its shared item receives wording above. J01-J10, the Arsinoe/Nurah S35 reconciliation (ruling 20, J03/J08), Kiana's professional Arsinoe/native-history corrections (ruling 41, J01/J10), and other-route/Claude rebuilds were not edited. No refusal was needed.

Voice review entries are in `tools/route_packs/plans/voice-review-pending.json`.
Native anchors verified directly in `/wrath/blueprints.zip` and `/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

| Re-voiced scene | Native enGB anchor | Want / action / cost |
| --- | --- | --- |
| `arsinoe_the_first_cart` | `58ee4b07-0488-4fab-a286-d50f786fe135`, SeelahInDoubt/Cue_0032: "So stop arguing, and let's go." | Wants payment, admiration and supper; defends the hearing actually given, takes the Commander's arm; accepts a delay and contains the anger already shown by her marked palm. |
| `arsinoe_price_of_an_evening` | `d04cb075-766c-4101-a170-d28357918c42`, VendorArsinoe/Cue_0003: serving Abadar "with my deeds and not only with my words." | Wants ordinary company without exploiting the Commander's office; sponsors the promised chairs or private room; spends her own money, within an occasional evening she can afford. |
| `arsinoe_another_hour` | `3ceba8d3-b324-4db6-a56b-e2fa34df5fb7`, VendorArsinoe/Cue_0016: "my aasimar features are rather appealing" | Wants company and the Commander's attention; accounts for her sponsorship and keeps official access out of the gathering; bears the expense and admits that hosting displaced the game she wanted to enjoy. |

These are authored continuations, not assertions about native events. No canon alteration, foresight/echo device, return, sexual slot or heat eligibility changed. None of the changed scenes is voice-locked.

## CLASS SWEEP

- Loan versus staged judgment, praise versus criticism, revised debt dates and subsequent supper invitation. The staged criticism already preserves her judgment; it was left intact.
- Full and staged passage/drain/landing recalls, carved face, and still-sticking window in the commitment and subsequent room scene. No claim of completed upper paving was added to the staged branch.
- Public/private proposals, objection sibling, six-chair arithmetic, gathering payment, and both aftermath accounts. All Commander's-share promises removed from this arrangement; existing cauldron charges are separate and unchanged.
- Earlier/quiet gathering closures, courier departure and unused cup, guest discussion and final tidying. No departed guest is recalled into the closing scene.
- Read the shared spring-arrival/coda siblings and their guards; supplied only the route wording requested by S3.
- Source comparison against HEAD: scene/node order, relationship IDs, choice identities, choices' gates/effects and all other non-text structure are identical. Campaign LF and continuation CRLF preserved byte-for-byte in convention; changed files decode as UTF-8.

## GATE

Explicit generation used `PYTHONHASHSEED=0`, `PYTHONUTF8=1`, `RRT_GAME_DIR=/wrath` and the four parent manifests from `build-expansion.ps1`. C# output/intermediate paths are in system temp through `BaseOutputPath`/`BaseIntermediateOutputPath`.

- `python expansion.py`: PASS, 4,054 scenes from final storyline sources. An earlier generation was deliberately stopped when the sibling payment sweep added the aftermath fixes; the completed final generation contains those fixes.
- `python -m unittest discover -s tests -p "test_arsinoe*.py" -q`: PASS, 8 tests after fixing the obsolete boundary assertion. Seven history tests had already passed; the initial full route selection failed only that old assertion.
- `python -m unittest discover -s tests -p "test_*.py" -q`: invoked twice, including after the assertion fix; both ended with exit 143 and no summary. NOT PASS.
- `python tools/savecompat.py`: PASS, 0 hard failures. Independent comparison against HEAD also proves unchanged scene/node/choice order and non-text gameplay metadata in both modified storyline modules.
- `python -m unittest discover -s tests -p "test_utf8_io.py" -q`: PASS, 1 test. Changed storyline/test files decode as UTF-8 and preserve their original LF/CRLF conventions. `git -c core.whitespace=cr-at-eol diff --check`: PASS (the override recognizes the required CRLF convention).
- `python tools/payoff_lint.py --strict`: PASS, 42 routes, 0 hard failures.
- `python tools/departure_lint.py --strict`: PASS, 43 women, 0 hard failures.
- `python tools/voice_lock_lint.py --strict`: PASS, 576 locked scenes, 0 changed, 0 missing/ambiguous.
- `python tools/slot_brief_lint.py --strict --known-rebuilds`: PASS, 320 briefs, 0 hard failures; existing 315 known-rebuild entries and 168 warnings remain. Isolated `python tools/slot_brief_lint.py --strict --briefs tools/route_packs/explicit_slots/arsinoe`: PASS, 5 briefs, 0 hard, 0 known rebuild, 0 warnings.
- `python tools/rrt_verify.py --strict`: FAIL, exit 1, **13 hard failures**, all in unchanged, voice-locked Jerribeth scenes (locations below); runtime 1,058.4 seconds. No Arsinoe hard findings. Structural validation reports 0 errors; save compatibility, earned presence, native return, intimacy, memory, transaction and draft contracts report 0 hard failures/diagnostics. The overall strict gate is NOT PASS.
- `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json`: invoked twice; both ended with exit 143 without diagnostics. Full rules/progression validation is NOT established; no "Page has no selectable answers" diagnostic was emitted.
- Focused C# `dotnet run ... -- --suites ArsinoeRound3Tests,ArsinoeAssembledTests development/Story.json`: PASS, 3,206 assertions in two suites. Additional selection `ArsinoeOpeningTests,ArsinoeContinuationTests,ArsinoeCampaignTests,ArsinoeTricksterTests` ended with exit 143 without a summary; NOT PASS.

Generated development files were restored to their pre-gate bytes after validation; temporary logs, verifier reports, scripts, caches and dotnet outputs were removed. No temporary artifact remains in the repository.

## ESCALATE

- D03: coordinator must supply the existing-design knowledge/discovery contract and integrate its readers with shared household/payoff consumers. Route-local dialogue alone cannot truthfully claim to enforce that promise. No new policy was invented.
- D06-D09: S4 must approve precise passage/workbench/prop placement, actor and observable project-state delivery, including the runtime/GLOBAL dependency. The supplied setpiece document describes the story but supplies no approved implementation for those world objects. Editing `src/*` is prohibited.
- D11: shared Last Call owner should apply the supplied aftermath text and test that late-only acceptance emits one spring arrival; preserve paragraph identity/guards.
- Required full Python discovery and C# rules/progression runs terminate with exit 143 before any diagnostic summary. The focused route gates pass where completed. The coordinator must obtain complete broad results; no selectable-answer failure was reported, but that absence is not a passing progression result.
- Strict verification reports these 13 hard player-text findings in **voice-locked, unchanged Jerribeth scenes**. They are outside Arsinoe ownership; no source, lock hash, baseline or other-route pending entry was changed to suppress them. Claude/shared lint owners must review:
  - `jerribeth.farewell/traitor_fed`: commander-gender.
  - `jerribeth.farewell/discovery_distant`: speaker-attribution-review.
  - `jerribeth.ending_together/catalogue`, `jerribeth.ending_ascended/catalogue`: commander-gender.
  - `jerribeth.offered_signature/companion_regill`: commander-gender.
  - `jerribeth.counterfeit_guest/maker`, `/square`: commander-gender; `/scout_known`: embedded-commander-speech.
  - `jerribeth.counterfeit_audience/challenge`, `/leverage.reply.1`, `/departure.reply.1`, `/raid_dismissed`: commander-gender.
  - `jerribeth.counterfeit_spoil/object`: commander-gender.

## PROPOSE

None. No new mechanics, costs, gates, reconciliation conditions or route redesigns implemented.

## RISKS

The five completed findings are local fixes; unresolved accountability, world staging and shared coda prevent claiming full route completion or scores >=91. Voice review remains pending. Required broad checks may expose inherited unrelated defects; failures are reported without weakening shared validation. No commit, full build, harness, game launch or installation.
