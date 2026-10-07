# R4-konomi local residue

Frozen base: `5dd587bd3277fa985e4293601290f59ad8dfcd6e`.
Changes are uncommitted, as requested. No new mechanics, gates, costs, choices,
flags, scene IDs or node IDs. These are authored dialogue/staging corrections;
they do not rewrite native events or add a fate/echo device.

## CHANGES

| Finding | Status | File / evidence |
| --- | --- | --- |
| konomi:D01–D02; K01–K02 | Out of scope | Galfrey's current-location witness: J01/J10, ruling 41. No cameo/presence predicates edited. |
| konomi:D03–D05; K03 | Out of scope | Political settlement versus romantic acceptance and truthful consumers: J08/J10, ruling 42. No eligibility predicates or producers edited. |
| konomi:D06 | Done | `storylines/konomi.py`, `disagreement/mercy` and sibling `respect`: she covers the appeal with her recommendation, insists on figures, and puts the capital's scrutiny behind her advice. She wants Drezen's reserve protected; presses the Commander on page; risks a dispute bearing both their names rather than apologizing for her superiority. |
| konomi:D07 | Done | `storylines/konomi_ordinary_expansion.py`, `the_upper_passage/start` and `miss`: arithmetic barb remains; the plank's crack interrupts her and directs her attention to the demonstration. The wheel joke has no apology. She wants her wagon proposal to survive; investigates the noise; must accept the already-established repair and curtailed trial. |
| konomi:D08 | Done | Same file, `the_trial_day/walk`, `evening_cost`: she writes Oselda's name beside hers and enjoys obtaining an ally with access she lacks. Oselda insists on her own recommendation and the unflattering cask count. Konomi gains influence while surrendering sole control of the account; attraction rewards being understood, without a moral improvement confession. |
| konomi:D09 | Done | Same file, `a_name_beside_hers/start`, `joint`: she enjoys the introduction and political camouflage, sends the existing joint offer, and relishes making the readers admit Oselda. Her cost remains shared access/authorship and existing work time. No confession that ambition is dishonest. |
| konomi:D10 | Done | Same file, `the_evening_she_kept/circular_reply`: she brings out the inadequate letter and savors forcing the correspondent to approach Oselda. She wants broader influence and the pleasure of frustrating him; circulates the existing work; explicitly retains the already-chosen loss of regular income. No deadline for managing her vanity. |
| konomi:D11–D12 | Done: no change needed | Inherited `storylines/lastcall_partners.py` correction already makes official reports exact and sharp, with private evenings separately protected and crusade failures exposed. Shared source left untouched; assembled-page verification recorded below. |
| konomi:D13 (also S3 residual) | Done | `storylines/konomi_round2.py`, `trickster.never_arrived.second_supper/morning` and its retained `never_arrived.rooms/morning` copy: her reach is to the Commander's bare neck; the coat remains on her chair throughout. Existing continuation/receipt unchanged. |

Native voice evidence was checked directly against `/wrath/blueprints.zip` and
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`:

| Scene | Native enGB key / cue |
| --- | --- |
| `konomi.disagreement` | `34a2cf94-7248-4faa-98a8-6bb611a335b4`, Diplomacy_2/Cue_0097: professional superiority; also `326f0657-fe99-4873-b9a9-c8a034b652c9`, Cue_0102: reporting defiance to the capital. |
| `konomi.the_upper_passage` | `34a2cf94-7248-4faa-98a8-6bb611a335b4`, Diplomacy_2/Cue_0097: scorn for disregarding common sense. |
| `konomi.the_trial_day` | `3b7dcfab-68de-4f49-b392-1c10b6b4d17d`, Diplomacy_Officer/Cue_0040: politics as an invigorating hunt. |
| `konomi.a_name_beside_hers` | `b48679a2-ce8e-4d27-ac89-c83bc21632cb`, Diplomacy_Officer/Cue_0016: double and triple agendas, long-term strategizing. |
| `konomi.the_evening_she_kept` | `3b7dcfab-68de-4f49-b392-1c10b6b4d17d`, Diplomacy_Officer/Cue_0040: pleasure in pursuing political prey. |
| `konomi.lastcall.page` (inherited correction) | `571c1850-ed85-491b-84fa-405d9a900007`, Diplomacy_Officer/Cue_0014: service to Queen Galfrey. |

All five re-voiced scenes are queued in
`tools/route_packs/plans/voice-review-pending.json` with their finding IDs.
No refusals; no Konomi voice locks or prose-pending entries required.

`tests/test_konomi_round3.py`: the required route gate exposed a pre-existing
assertion for an obsolete register sentence. The baseline export reproduced
the failure. The test now checks the actual signed correction, dovecote,
two dates, witnessed arrival and earned accreditation/return requirements,
instead of requiring the old sentence. No story rewrite was made for this test.

## CLASS SWEEP

Checked all choices and sibling nodes in the five affected scenes, including
both trial outcomes, both report offers and both supper replies. Removed the
same automatic self-rebuke from `disagreement/respect`, the wheel joke and the
evening trial's report discussion. Oselda retains her independent demand for
credit, access and pay. Checked the retained rooms encounter, second supper,
their explicit-slot approaches/continuations, and other coat references for
prop continuity. Existing price, dispatch, privacy and commitment contracts
were preserved. Checked Last Call reporting against the crown-first report
discussion in `a_name_beside_hers/time` and the separate private-sheet dispatch
in `trickster.dismissed.private/morning_favour`.

## GATE

Generation and all temporary
exports/logs/build outputs use the system temporary directory, because edits
to `development/Story.json` are prohibited. Commands receive that fresh export
through `--story`, `RRT_TEST_STORY` and the rules-runner argument. Hash seed is 0;
.NET artifacts use `RRT_TEST_BUILD_ROOT`. No build script, harness or game run.

- `PYTHONHASHSEED=0 RRT_STORY_OUTPUT=<temp>/Story.json python expansion.py`:
  success, 4,054 scenes. Baseline and revised exports compared: every non-`Text`
  field is identical, across the entire export.
- `python tools/savecompat.py --story <temp>/Story.json`: 0 hard failures.
- `python -m unittest tests.test_utf8_io tests.test_konomi_round2 tests.test_konomi_round3 -q`:
  15 tests pass after the stale assertion correction above.
- `python tools/payoff_lint.py --strict --story <temp>/Story.json`:
  42 routes, 0 hard failures.
- `python tools/departure_lint.py --strict --story <temp>/Story.json`:
  43 women, 0 hard failures.
- `python tools/voice_lock_lint.py --strict --story <temp>/Story.json`:
  576 locks, 0 changed, 0 missing/ambiguous.
- `python tools/slot_brief_lint.py --strict --known-rebuilds --story <temp>/Story.json`:
  320 briefs, 0 hard, 315 known rebuild findings, 168 warnings; no briefs changed.
- `python -m unittest discover -s tests -p "test_*.py" -q`:
  attempted as explicitly requested; terminated by SIGTERM (exit -15), with
  no test output. Not a passing receipt. Focused route tests passed separately.
- `git -c core.whitespace=cr-at-eol diff --check`: pass. LF files retain LF;
  the ordinary-expansion file retains CRLF throughout.
- Assembled `konomi.lastcall.page/page` confirms the D11–D12 inherited correction:
  official reports expose crusade failures; private evenings stay private.

- `python tools/rrt_verify.py --strict --quiet --story <temp>/Story.json`:
  **13 hard failures**, all player-text diagnostics in seven locked Jerribeth
  scenes listed under ESCALATE. Every failing scene is byte-for-byte identical
  in the baseline and revised exports. No Konomi hard findings. This is not a
  zero-hard gate receipt; no shared lint exemptions were added.
- `RRT_TEST_BUILD_ROOT=<temp>/rules-build dotnet build tests/RulesTests.csproj -c Release`:
  success, 0 errors, 8 existing CS0649 warnings.
- `dotnet run --project tests/RulesTests.csproj -c Release -- <temp>/Story.json`:
  attempted as requested; terminated with exit 143 and no output. Not a passing
  rules/progression receipt.
- Filtered Konomi C# run: six suites completed before
  `KonomiOrdinaryExpansionTests` stopped at its pre-final-page outcome assertion.
  All mechanic fields are identical to the baseline. Remaining suites were
  checked separately; no route outcomes were redesigned to satisfy this fixture.
- Second filtered run: `KonomiPolishTests`, `KonomiPoliticalConsequenceTests`,
  `KonomiPoliticalTests` and `KonomiPrivateAbsenceTests` completed.
  `KonomiPrivateConsequenceTests` then failed its final-page-only assertion at
  `konomi.private_last_visit.explicit.1`, an unchanged scene outside this pass.
- Final filtered run: `KonomiPrivateHearingTests`, `KonomiRetainedReturnTests`,
  `KonomiReturnInvitationTests`, `KonomiTests`, `KonomiTricksterTests`:
  **PASS, 171,746 assertions in five suites**. In total, 15 Konomi suites
  completed successfully; two stopped on the inherited invariants above.
- Final workspace inspection: only scoped source/test/plan files changed.
  No `tests/obj`, `tests/bin` or temporary directories. Temporary exports,
  verification reports, test logs and .NET outputs deleted after receipts
  were transcribed here. No commit.

## ESCALATE

Shared J01/J10: D01–D02/K01–K02 current Galfrey location (ruling 41).
Shared J08/J10: D03–D05/K03 earned current commitment and downstream eligibility
(ruling 42). S1's route-local exception does not authorize duplicating these
shared fixes; no uncovered local producer repair was commissioned here.
No Claude rebuild overlaps the edited Konomi scenes.

The strict verifier's 13 inherited player-text hard diagnostics need the Claude
owner of these locked, out-of-route scenes:

| Scene / node | Diagnostic |
| --- | --- |
| `jerribeth.farewell/traitor_fed` | commander-gender |
| `jerribeth.farewell/discovery_distant` | speaker-attribution-review |
| `jerribeth.ending_together/catalogue` | commander-gender |
| `jerribeth.ending_ascended/catalogue` | commander-gender |
| `jerribeth.offered_signature/companion_regill` | commander-gender |
| `jerribeth.counterfeit_guest/maker` | commander-gender |
| `jerribeth.counterfeit_guest/square` | commander-gender |
| `jerribeth.counterfeit_guest/scout_known` | embedded-commander-speech |
| `jerribeth.counterfeit_audience/challenge` | commander-gender |
| `jerribeth.counterfeit_audience/leverage.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/departure.reply.1` | commander-gender |
| `jerribeth.counterfeit_audience/raid_dismissed` | commander-gender |
| `jerribeth.counterfeit_spoil/object` | commander-gender |

Coordinator: reconcile `tests/KonomiOrdinaryExpansionTests.cs:79` with existing
authored intermediate outcome flags. Its final-page-only invariant fails
despite unchanged mechanics. This acceptance debt is outside D06–D13; neither
the fixture nor outcome timing was weakened or redesigned here. The interrupted
full Python and C# checks also require coordinator receipts.
The same reconciliation is needed for
`tests/KonomiPrivateConsequenceTests.cs:33`, which rejects persisted decisions
before completion of the existing `konomi.private_last_visit.explicit.1` slot.

## PROPOSE

None. No additional mechanics or design changes implemented.

## RISKS

The local pass cannot close the shared caps above or certify rubric scores.
The five voice changes require the coordinator's Claude voice review.
Strict verification is blocked by inherited locked-route findings; full-suite
validation did not complete, and the ordinary-expansion C# fixture fails.
The private-consequence C# fixture also fails its intermediate-page invariant.
