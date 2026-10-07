# Horzalah round 4 local residue

Base inspected: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
No commit. Only the commissioned Horzalah entries, route regression tests and
route review/report metadata are changed.

## CHANGES

| Finding | Status | File / evidence |
| --- | --- | --- |
| horzalah:D01; horzalah:K01 | done | `storylines/horzalah_guild.py`, `beat.spit/hers`: explicitly remembers the Commander's killing of Hepzamirah in Colyphyr and takes malicious pleasure in it. A later return does not erase that history. |
| horzalah:D02 | done; Claude voice review pending | `storylines/horzalah_trickster.py`, `unmet.knife/beaten`: restores native profanity, wounded pride and the angry blow against the floor. The subsequent bargain interrupts her fury. |
| horzalah:D03 | done; Claude voice review pending | `storylines/horzalah_guild.py`, `beat.spit/hers,hers2`: she disarms, kneels and humiliates the crusader, then forfeits the tongue she wanted to avoid a fight with the watch. Protection stays on the Commander's intervention road; she supplies no compassionate coaching or ethical lesson. |
| horzalah:D04 | done | `storylines/engine_f6c.py`, **only** the commissioned Horzalah `guild` entry: removes emancipation from Baphomet's claim. The earned Trickster-dependent slide credits the ear con with preserving her chair against her own masters. No new freedom device or native mechanics. |
| horzalah:D05 | out of scope: S6/shared contract owner | Ally still lacks paid-employment history. No retainer or employment gate invented. |
| horzalah:D06 | out of scope: S6/shared contract owner | The same Ally ending's final settlement is unearned; untouched. |
| horzalah:D07 | out of scope: S6/shared contract owner | Mourned Ally's payment/refund still lacks settlement history; untouched. |
| horzalah:D08; horzalah:K02 | out of scope: S6/shared contract owner | Optional invoice and paid ending consumers remain disconnected; no new payment channel or completion receipt. |
| horzalah:D09 | done | `storylines/horzalah_trickster.py`, `unmet.knife/demise`: both original answer indices now test the Commander's own Mobility/Athletics, DC30. Success retains `fight` and the bargain. New appended `outmatched` failure shows her knife at the Commander's throat and the watch interrupting her attack; the existing `guard_called`/`closed` outcome supplies failure consequences, without ear, primed or return rewards. |
| horzalah:D10 | partial; debit relocation escalated | `storylines/horzalah_trickster.py`, `late.at_night/take,no_priest`: explains and names the existing 100-Favors political price before the cut, offers postponement, and labels the actual settlement answer with its debit. Both chapter roads retain the irreversible ear checkpoint/resumable payment. Moving the debit before injury requires changing the shared transaction contract/lint; the final implementation preserves its required charge point. |

`tests/test_horzalah_round4.py` checks the assembled encounter success/failure,
unchanged absence of rewards on failure, price disclosure/resumption in both
chapter roads, sister-killing history and the limited current-Trickster Guild slide.
`tools/route_packs/plans/voice-review-pending.json` lists every changed scene for
the Claude voice pass. None is in the 576-scene voice-lock inventory; no locked
text, explicit slot or brief was changed.

These are authored local encounter/continuity repairs, not new canon facts.
The tactical failure is a watch-interrupted bedchamber attack using existing RRT
skill checks and closure flags. The chair claim remains the existing authored
Trickster-only dependent native rewrite. No new echo, foresight shortcut, fee,
attraction, commitment, reconciliation or return requirement is introduced.

### Native voice anchors / want, act, cost

Verified directly in `/wrath/blueprints.zip` and
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

| Revoiced scene | Native enGB key | Want / on-page act / cost |
| --- | --- | --- |
| `horzalah.trickster.unmet.knife` | `6401f275-7b00-4bed-93fb-986be92b6204`, Mercy `Cue_0001`, asset `366ef842393dcef4d8889f03282529ae` | Wants the Commander's head and Father's favor; attacks, lashes out at defeat or cuts the Commander before escaping the watch; successful resistance costs her pride and endangers her Guild chair, while failure prevents the bargain. |
| `horzalah.trickster.beat.spit` | `aaa2721e-aa43-4a69-a351-519d8d36d647`, YozzDying `Cue_0050`, asset `331941e1396d60b45b887eb8eb7d1375`; also `12efa74c-f969-47ec-a4e7-ff924bf815a1` | Wants the soldier's tongue and public submission; forces him down, draws blood and wipes his spit over his mouth; gives up the mutilation to avoid the watch and continue her own business in Drezen. Native sister-hatred and triumph over crusaders anchor her response. |
| `horzalah.trickster.late.at_night` | `96cafbf4-931b-459e-9d62-90d30d23727d`, YozzDying `Cue_0051`, asset `fc5119d8d4a54e047b07338764beb346` | Wants the trophy that will silence her masters; takes the Commander's hair and claims the left ear; admits needing her defeated target's help, while the Commander owes the existing ear and political price. Her quoted speech is preserved; added price explanation is narration. |
| `horzalah.native.eng7_f6c.guild` | `8ccf1c23-ae95-4b2e-84cc-37b647aabebd`, native Guild epilogue cue `62f20840e6aa33844b641c5c8e10f814` | Wants to retain command; keeps the chair despite Guild rivals and Greybor's competing contracts; depends on the existing earned ear con rather than an invented release from Father. This is narrator prose, not new Horzalah dialogue. |

## CLASS SWEEP

- Street backed/independent/intervention roads: sister hatred is historical;
  only the independent handling had the false family denial and compassionate
  coaching. Restraint now has her own concrete motive and lost appetite.
- Defeat siblings: native Mercy `Cue_0001` and both authored attack answers;
  all saved victory/bargain/kill/go targets remain. Failure cannot award a trophy.
- Guild claim siblings: `guild.kept`, both folded entrance reports and pivots,
  native `guild`/`trio` entries. The false emancipation claim existed only in the
  commissioned native `guild` entry; all other entries are untouched.
- Late injury/price: offer, pre-cut action, irreversible checkpoint, priest
  refusal, both chapter-specific settlement answers and folded Guild onward
  delivery. Exact original 100-Favors spend and terminal receipts are retained.
- Payment class: invoice and Ally/mourned consumers reproduced and mapped to
  their shared owner; no paid-service fix is claimed.
- Original scene/node/relationship identities, answer indices and old targets
  preserved. New node/choice are additive. Existing route files remain CRLF;
  `engine_f6c.py` remains LF. UTF-8 decoding and diff whitespace checks passed.

## GATE

`$TMP` denotes the system temporary directory used for the generated story,
.NET outputs and audit logs. `development/Story.json` is never edited. Commands
use `PYTHONHASHSEED=0`, UTF-8 and the parent bindings from `build-expansion.ps1`.
The temporary gate directory and editing scripts were deleted after verification;
final scope/artifact checks found no repository build/cache/scratch outputs.

| Command | Final result |
| --- | --- |
| `python expansion.py` with `RRT_STORY_OUTPUT=$TMP/Story.json` | Passed; 4,054 scenes. Final regeneration follows the shared-contract correction. |
| `python -m unittest tests.test_horzalah_polish tests.test_horzalah_round2 tests.test_horzalah_round3 tests.test_horzalah_round4 -q` | Passed; 24 tests on the final export. |
| `python tools/savecompat.py --story $TMP/Story.json` | Passed; 0 hard failures. |
| `python tools/payoff_lint.py --strict --story $TMP/Story.json` | Passed; 42 routes, 0 hard failures; existing review notices retained. |
| `python tools/departure_lint.py --strict --story $TMP/Story.json` | Passed; 43 women, 0 hard failures; existing Mielarah review retained. |
| `python tools/voice_lock_lint.py --strict --story $TMP/Story.json` | Passed; 576 locked scenes, 0 changed, 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --known-rebuilds --story $TMP/Story.json` | Passed; 320 briefs, 0 hard, 315 known rebuild findings, 168 warnings. Horzalah's four briefs/hosts were unchanged. |
| `python tools/rrt_verify.py --strict --game /wrath --story $TMP/Story.json --json $TMP/verify.json --text $TMP/verify.txt` | Failed, exit 1: 13 hard player-text findings, all untouched locked Jerribeth text; 0 Horzalah hard findings, 0 shipped structural errors, 0 draft-contract diagnostics, 0 transaction hard failures. One invocation, 772.8 seconds. Exact findings below. |
| `python -m unittest discover -s tests -p "test_*.py" -q` | Attempted; host test guard terminated it, exit 143. No acceptance pass claimed. |
| `dotnet run --project tests/RulesTests.csproj -c Release -- $TMP/Story.json` | Attempted; host test guard terminated it, exit 143. No full progression pass claimed. |
| `dotnet run --project tests/RulesTests.csproj -c Release --no-build -- $TMP/Story.json --suites=HorzalahTricksterTests,TransactionInventory2Tests` | Passed; 5,334 assertions in 2 selected suites, including production affordability, interrupted injury settlement, exit/re-entry and 18 rejected mutations. |
| `dotnet build tests/RulesTests.csproj -c Release` with `RRT_TEST_BUILD_ROOT=$TMP/rules-build` | Passed; 0 errors, 8 existing unused-field warnings. |
| Strict UTF-8 decoding; original CRLF/LF verification; `git -c core.whitespace=cr-at-eol diff --check` | Passed. |

## ESCALATE

1. D10: `tools/transaction_inventory2_contracts.json` freezes the Horzalah entry
   as `irreversible-settlement`, payment at `no_priest[0]` after `cut`.
   `tools/transaction_exit_lint.py` requires that original **terminal** debit,
   and `tests/TransactionInventory2Tests.cs` tests post-injury unpaid settlement.
   A genuine pre-cut debit needs a shared prepayment contract/lint/test repair.
   No generic lint weakening, inventory-kind bypass or second charge was added.
2. D05–D08/K02: section 4.3 explicitly holds these consumers for S6/shared
   contract ownership. Paid employment, final settlement and refund still need
   actual receipts; the invoice's letter budget must be respected.
3. S3 `hepzamirah:D13` is Claude prose-pending/coordinator structure work on
   the locked Hepzamirah route, despite discussing Horzalah's returned state.
   It is not a Horzalah-owned S3 item and was not edited. J03 sister truce,
   J05 captivity remedy, shared current-presence integration and Claude's locked
   Nocticula court reactions are also outside this local assignment.
4. The host `/work/testguard.sh` terminated the two requested unfiltered suites
   with exit 143. Its policy excludes full discovery/RulesTests from this route
   job. No guard bypass or allowlist change was attempted; the coordinator must
   run the uninterrupted full gate. Filtered route/transaction results above do
   not substitute for that full progression proof.
5. The whole-export strict verifier is blocked by these 13 unchanged,
   Claude-locked Jerribeth text findings. All targets remain at their manifest
   text hashes (the strict lock gate reports 0 changed). Their prose and the
   shared text-lint interpretation belong to the existing Claude/shared owner;
   neither was altered or exempted in this route job.

   | Scene / node | Strict code |
   | --- | --- |
   | `jerribeth.farewell/traitor_fed` | `commander-gender` |
   | `jerribeth.farewell/discovery_distant` | `speaker-attribution-review` |
   | `jerribeth.ending_together/catalogue` | `commander-gender` |
   | `jerribeth.ending_ascended/catalogue` | `commander-gender` |
   | `jerribeth.offered_signature/companion_regill` | `commander-gender` |
   | `jerribeth.counterfeit_guest/maker` | `commander-gender` |
   | `jerribeth.counterfeit_guest/square` | `commander-gender` |
   | `jerribeth.counterfeit_guest/scout_known` | `embedded-commander-speech` |
   | `jerribeth.counterfeit_audience/challenge` | `commander-gender` |
   | `jerribeth.counterfeit_audience/leverage.reply.1` | `commander-gender` |
   | `jerribeth.counterfeit_audience/departure.reply.1` | `commander-gender` |
   | `jerribeth.counterfeit_audience/raid_dismissed` | `commander-gender` |
   | `jerribeth.counterfeit_spoil/object` | `commander-gender` |

## PROPOSE

None. The existing-cost relocation above is required by D10, not a proposed
new price or route redesign.

## RISKS

- D10 remains mechanically partial until the shared contract permits prepayment;
  D05–D08/K02 remain unresolved under their assigned owner.
- Claude voice review is queued. No independent score or all-dimensions-91 claim.
- No installed-game, harness or live combat proof was run; the encounter uses
  the audited allowed tactical-check alternative.
- Unfiltered Python/C# acceptance remains blocked by the host guard.
- The requested whole-export zero-hard strict gate remains blocked by the 13
  locked Jerribeth findings above. No strict pass is claimed.
