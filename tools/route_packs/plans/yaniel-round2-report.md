# Yaniel — polish round 2 implementation

## CHANGES

All additions are authored Trickster content. Native evidence was checked in `/wrath/blueprints.zip` and enGB: TrueYaniel cues 0001, 0021, 0023, 0035, 0044 and 0030, plus Joran's cue 0010/shared localization. The final atlas reservation remains `act_before_confession`, at Drezen's flooded east-gate watch-room and the existing martyr-statue niche. No echo, Shyka-affection device, partner stance or live Joran was added.

| File | Situation / finding and result |
|---|---|
| `storylines/yaniel_trickster.py` | S1: the Fane exchange now gets her physical counter-move and voluntary return, rather than surprise or an iron hostage compelling agreement. Sword removal, DC20, oath/refusal branches and native exits stay intact. |
| same | S4 / atlas-0001, 0003, 0012 / F38: she kisses before naming desire; an appended branch recalls the raid kiss only when earned. Other reciprocal histories keep their existing access. Soldiers' song reports and accepted personal testimony have separate continuations; neither claims eyewitness knowledge or a Threshold journey. Material gifts stay unequal; the iron becomes her gift. Trade/vigil commitment effects are unchanged. |
| same | S5 / F26–28, F42–43: one appended explicit-slot node with the brief's heated cut. Worn iron remains on the wrist; a declined-then-vigil re-gift uses the carried-cuff aftermath. Morning dressing leads to custody/party/pending-oath variants of her Radiance argument. Seelah discovers the couple after the act, refills the lamp, and earns `yaniel.trickster.morning.seelah_witness` only at her actual terminal. A later return cannot earn that memory. Sexton remains a separate, non-eyewitness outcome. Delayed dialogue uses event-relative time. |
| same | S6 / deferred tree debt / F44: append the tree answer only to together/late-commit living endings, after the existing Joran memorial paragraph. She initiates the spring kiss and returns to Drezen. Keep the broken oath's scar after vigil; replace the annual injury ritual and abstract couple-ending claims with returns, supper and watch duty. Mourned now excludes departure and closure. All nine ending identities and effect-free legacy exits remain. |
| `storylines/yaniel_walls.py` | S2 / YAN-01–02: the existing unveiling now includes the chaplain misusing her name. She can appear and counter him, or stay hooded and answer without being exhibited; the wounded man's blanket is returned. She demands a meal rather than another speech. No hearing quest, fee, attendance receipt or compulsory guest was added. Scar invitation no longer praises the torturers' work; veteran flirt replaces maiden-in-chapel staging. |
| same | S3 / P14, P22–25, F39, F61: append yield, Mobility DC25 and Bluff DC25 methods with distinct success/failure nodes; describe a bounded blunt-blade bout without inventing teachers. All methods finish at the existing bout receipt and never earn trust. Append plain-Radiance raid tactics; holy-light tactics require the party-held +4/+6 forms, including the plain-party/holy-stash case. Replace stock combat imagery with her braced feet and pulling scar. |
| same | S6 / F4, P13: Areelu correspondence must be useful against the Wound; Yaniel objects to further prisoners and retains her anger. Present Minagho and the Chivarro inquiry read independently earned current presence, with neutral inquiry knowledge when Minagho has not returned. Shared guard injection still prevents this separation in the integrated export (ESCALATE). Wrist, linen and ordinary-pouch aftermaths keep their different handling, deepen chosen contact and supper in her room. |
| `tests/test_yaniel_round2.py` | Eight quick history tests: five sword forms/stash; all sparring methods; optional prior kiss; report/belief/pending trade branches; slot/cuff re-gift; actual witness; departed sacrifice; spring append order and unchanged ending effects. |
| `tests/YanielTricksterTests.cs` | Existing reaction fixtures now provide the actual morning witness receipt; an earned return without witnessing must not open the memory. No unrelated suite changed. |
| `tools/route_packs/plans/yaniel-{setpieces,tp}.md` | Copy both required plans from their named remote branches, retaining the planning evidence and appending implementation status. Older proposed device wording is explicitly superseded by the atlas reservation. |
| `tools/route_packs/turning_points.json` | Record only Yaniel's exact atlas entry, including its fixed class, setting, payoff and canon hooks. |
| `tools/route_packs/explicit_slots/yaniel/yaniel.trickster.visit.niche.explicit.1.json` | Copy the required brief and update implementation status. One slot added; no explicit prose generated. |

Audit items already corrected in the integration baseline were verified and retained: F1–3, F5–7, F10–19, F23–25, F29–37, F40–41, F59–60 and F62. In particular: Tower of Estrod provenance; unsettled Ch3 escort/final Ch5 shipment; half-elf/mortal identity and faith; Fane/wall/empty-handed chronology; packed/pouch fallback and two-iron owner precedence; historical Fane intervention; real skill labels; supper in her quarters. F38 and cuff/witness/departure findings received the additional route-local repairs above. P1–13, P15–20 and F8–9, F20–22, F45–58, F63 have the shared residuals below; no claim is made that route-local prose removed injected guards.

## CLASS SWEEP

Checked all three Yaniel modules, all nine local endings and Yaniel's integrated Last Call/ledger entries. Compared Fane versus wall entry; carries/judges and pre/post-Iz custody; holy/plain/party/stash/song/report/belief/pending/lost states; wearing/packing/skipping/pocketing/declining/re-gifting and two cuffs; each reciprocal/trial alternative; truth/secret; trade/vigil/refusal/departure; both actual dawn witnesses and subsequent Seelah return; sacrifice with and without the existing Commander return. Grief, nightmares and refugee privacy remain nonsexual; Joran remains memory. The raid remains the sole trust repair. No new cost, attraction requirement, reconciliation condition or fate mechanism was added.

Source files retain CRLF byte-for-byte as their newline convention. Old IDs, node order, choice indices and paragraph order remain; new choices/nodes append. The spring paragraph specifically follows the previously appended memorial. No conditional paragraphs were introduced outside epilogue pages.

## GATE

All commands used `PYTHONHASHSEED=0` and ran in a disposable system-temp checkout containing the current sources. Exports, verifier reports, .NET outputs and test scratch data stayed outside this worktree; the checkout and its outputs were deleted before finishing. The worktree's generated `development/Story.json` was not changed.

| Command | Result |
|---|---|
| `python expansion.py` | PASS — 3,755 scenes in the final export. |
| `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_yaniel_round2 -q` | PASS — 20 tests. After the final prose-only correction, UTF-8 and the eight route tests were also rerun: 9 tests passed. |
| `python tools/payoff_lint.py --strict` | PASS — 42 contracts, 0 hard failures; Yaniel's shared Last Call narrative REVIEW remains. |
| `python tools/departure_lint.py --strict` | PASS — 43 women, 0 hard failures. |
| `python tools/rrt_verify.py --strict --gate-only --game /wrath --json <temp>/verify-final.json --text <temp>/verify-final.txt` | PASS — 0 hard failures; 0 shipped structural errors. `--gate-only` runs all strict checks and omits report-only world/budget analyses. The preceding completed run found one commander-gender false match on a pronoun referring to the chaplain; the sentence was rewritten, regenerated and verified again as required by the final fix-the-gate instruction. An earlier stale verifier was stopped during skill-key correction. |
| `dotnet tests/bin/Release/net8.0/RulesTests.dll --suites=YanielTricksterTests,YanielRadianceTests development/Story.json` | PASS — 2,597 assertions in the two route suites, including global `Rules.Validate`. |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | INCOMPLETE — attempted twice under the final user instruction; each process terminated with exit 143 and no diagnostics. No pass claimed. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | INCOMPLETE — attempted twice; each process terminated with exit 143 and no diagnostics. The build produced the runner, which was then used for the passing filtered route suites. Full progression validation is not certified. |
| `git -c core.whitespace=cr-at-eol diff --check` / newline inspection | PASS — no whitespace defects; CRLF preserved in both edited route modules and the existing C# test file. |

The C# validator initially caught `CheckMobility`; it was corrected to the runtime enum `SkillMobility` before the final export and passing C#/strict results. No build-expansion script, harness, game or git commit was run. Full-suite termination had no stated reason, so it is recorded as a validation limitation, not attributed to automatic approval review.

## ESCALATE

1. **Shared historical/current presence classification** (`storylines/crossroute_presence.py` and its classifiers): exported Fane swaps, late wall, Areelu memory, Sosiel's impostor memory, raid and prayer still receive availability guards for remembered captors or Seelah. Found rescue reports, wall courtship, night memory and Church dialogue have the same class of answer guards. The Minagho/Chivarro inquiry receives scene-wide guards for both women despite route-local branch selectors, defeating independently earned Chivarro arrival. Historical death/departure/closure cases must be tested through the derived guard dependencies, not just direct flag names. Maps P1–13, F45–58 and F63; includes the Iomedae closure attached to the dirty tactic. Neither shared module nor another route was edited.
2. **Shared Last Call and ledger** (`storylines/lastcall_partners.py` / shared assembly): origin-neutral call and `owed.yaniel` base; separate initial oath, accepted open relationship, declined and vigil receipts; pre-Iz holy-custody plus verdict for her song, excluding post-Iz handover; a late holy watch paragraph without song; accepted Iz oath recap rather than certified Threshold carriage, with pending/unproven end-possession uncertainty. Maps P15–20, F8–9 and F20–22, plus the engine-round-3 residual. These were inspected but not changed because the shared file is excluded. Strict payoff metadata still reports this narrative REVIEW.
3. **Shared memorial hearing / household propagation**: coordinator owns a single Yaniel–Terendelev hearing and any shared guest/reaction staging. The route-local unveiling and meal are implemented; Terendelev is not made a compulsory participant. Household state and shared fate/return mechanics stay intact.

## PROPOSE

None beyond the required coordinator repairs above. No darker Commander manipulation, live-partner stance, new Joran story, compulsory raid, extra sexual episode or new return device was implemented.

## RISKS

The shared guards and unearned Last Call recaps remain real narrative/integration defects; passing mechanical lints cannot certify their writing. Independent rubric scores were not obtained or self-certified. The explicit slot remains its heated-cut default pending the coordinator's generation and continuity review. Full Python discovery and unfiltered .NET validation remain incomplete after exit-143 interruptions; the final strict gate and route suites passed. The coordinator must complete those full suites at the integration milestone. Changes are intentionally uncommitted under the final user instruction.
