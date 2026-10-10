# fix16b findings

Pinned inputs were read through bundle_path entries. Seven test input hashes matched the manifest. Only tests were edited; source/player text and the inventory were untouched. Existing UTF-8/newline style was preserved.

## Per-test changes and mutations

Full unittest IDs and machine-readable checks are in `fix16b-evidence.json`. Counts below are assertion failures; every control and mutant has zero errors. Retained control failures are owner conflicts, not mutation proof. Each mutant adds one independently attributable assertion failure.

| Test | Pin removed | Behaviour protected | Export mutation | Control → mutant failures |
| --- | --- | --- | --- | --- |
| `tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_frozen_scene_reader_and_shared_producer_contracts` | Node/paragraph hashes and choice wording | Scene and reader gates, ordered node/choice IDs, save identities, transition effects; history predicates found by gates | Remove salt scene’s trickster.ever requirement | 15 → 16 |
| `tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_all_nine_endings_keep_existing_paragraph_indices` | Nine fixed paragraph counts, paragraph offsets, wording and hashes | Declared ending IDs, history predicates, inert terminal exit | Set nidalynn.closed on the salt terminal exit | 7 → 8 |
| `tests.test_nidalynn_partner_claim.NidalynnPartnerClaimTests.test_frozen_prefixes_and_exact_appends` | Frozen prefix/appended wording, hashes, offsets and assembled length | Approved prefix/appended history predicates on their declared pages | Remove the Areelu accounted-history append | 2 → 3 |
| `tests.test_contract_j01.J01Tests.test_reference_manifest_is_exact_and_never_exempts_new_live_action` | 131 contexts and exact text hashes | Reference classification and rejection of added live actions; all manifest addresses execute as independent subtests | Replace a reference with a live action | 2 → 3 |
| `tests.test_contract_j01.J01Tests.test_s08_seal_reply_remains_a_channel_and_is_not_emitted_by_j01` | Whole assembled export forbidden from containing any S08 scenes | J01 installation preserves scene IDs/order; exported S08 contacts remain authenticated letters with no body options; missing receipts/loss flags reject the synthetic channel | Change an exported S08 reply contact to body | 0 → 1 |
| `tests.test_endings_job4.EndingsJob4Tests.test_repeated_pair_summaries_only_follow_selected_terminal` | Exact accepted-terms phrase and undressing phrase counts | With shared terms, visible stance summaries occur at terminal nodes and exist on went; disabled preterminal variants do not render | Append a visible shared-terms summary to start | 0 → 1 |
| `tests.test_iomedae_round2.IomedaeRound2Tests.test_slots_have_one_first_night_and_history_specific_mornings` | Brief’s exact last sentence in slot prose | One first-night slot per selected path; history-specific mornings; quiet path skips sex/morning; no effects on epilogue choices | Redirect the platform slot into night_quiet | 0 → 1 |
| `tests.test_horzalah_polish.HorzalahPolishTests.test_knife_and_missed_chamber_endings_have_no_retroactive_receipts` | Knife paragraph selected by prose, exact cut sentence, lamp/skin phrases | Knife history needs both receipts; alternate knife history excludes a won knife; chamber replay is forbidden after CHAMBER; page exit is inert; cut reaches declared slot without effects | Remove CHAMBER from the together slot’s forbids | 0 → 1 |
| `tests.test_herrax_round2.HerraxRound2Tests.test_all_four_briefs_have_reachable_default_nodes` | Four reserved nodes / brief count, last_line key presence | Each declared brief node or explicit host is graph-reachable from its actual scene entry; commander variants preserved | Disconnect madam.reachable.explicit.1 | 0 → 1 |
| `tests.test_nurah_round2.NurahRoundTwoTests.test_slots_are_reachable_and_legacy_ending_exits_keep_their_effects` | 12 briefs and shirt wording | Each declared slot/host is graph-reachable, reserved slot continues without effects, and legacy exits/quiet transition keep their effects | Disconnect prison.terms.explicit.1 | 0 → 1 |

## Class sweep

71 tests across all seven assigned modules ran against the disposable export: 67 passed; four tests reported 26 assertion failures (24 Nidalynn flag conflicts and two J01 classifier failures). The idempotent repeated-assembly sibling was excluded from this check; an exploratory pre-edit whole-suite run was cancelled while running its expensive rebuilds. Its completion is unproven here. The wrapper’s required changed-tests stage still applies.

Herrax’s late slot is reachable in `herrax.trickster.epilogue.after_hours.invitation`; its global node ID survives that scene move. All seven Herrax and 13 Nurah declared hosts are reachable. Their counts are evidence only, not test expectations. J01’s newer `choice[n]` and `paragraph[n]` addresses now resolve; they no longer produce the 17 parser errors exposed during the initial sweep. S08’s own producer is `storylines/harem_rows/s08.py` (commit `2fd3d3e7c2f1a4850a619993a6b68677cff48e45`); absence from the entire assembled story was an invalid attribution check for J01.

## Escalations

No dependency owner was declared in the bundle (`dependency_owners` is empty). Owners below identify responsible modules/jobs, not named people. No matching baseline runner receipt was supplied, so gate-failure attribution is unknown.

- **Nidalynn structure / struct-nidalynn owner:** commit `e7ecf8c9fb6e3ce3cdc53ee880f9228a601d68e3` changed `kiln.the_chaplain` choice 0: `after_prayer.Set` expected `[]`, actual `[nidalynn.trickster.chaplain_prayed]`; `leave.Set` expected `[]`, actual `[nidalynn.trickster.chaplain_sent_away]`; `end.Set` expected `[nidalynn.trickster.chaplain_prayed]`, actual `[]`. Scene Forbids gained `nidalynn.trickster.chaplain_sent_away`.
- **Same owner, page nodes:** `epilogue.salt`, `late`, `heel`, `unreturned`, `apart`, `claimed`, `lie` expected the chaplain-history predicate `Requires=[nidalynn.trickster.chaplain_prayed], Forbids=[], AnyGroups=[]`; actual `Requires=[], Forbids=[], AnyGroups=[[nidalynn.trickster.chaplain_prayed, nidalynn.trickster.chaplain_sent_away]]`. Same commit. These expectations remain failing.
- **fix15 departure-contract owner:** commit `e62d94c4372ba2257b892c1ff40b2d00bde12895` removed `nidalynn.present_now` from Requires for `epilogue.wolves`, `apart`, `lie`, `given` by reclassifying departure history. Each exact expected/actual list is recorded in the evidence JSON. This changes availability; the task explicitly forbids updating these expectations.
- **J01 classifier owner:** both `herrax.trickster.madam.reachable/cut` and `reachable_restored/cut` return a live Chivarro match for the historical old-cushions reference, where the reference contract expects no live matches. Commit `6f89a00356e82282f87c806153deca5a18bad77c` changed that reference wording. Resolve the classifier/reference contract under its owner; no player prose was edited.

## Gate

The wrapper owns all required profile stages, source/export sealing, staging, commits and pushes. No implementer gate receipts are claimed. Required stages are unrun here (exit null); `gates` remains empty. The mutation command exited 0, sibling command exited 1, and `git diff --check` exited 0; these are finding evidence, not runner acceptance.

## Propose

Resolve the Nidalynn bindings and J01 historical-reference classification with their owners. Migrate remaining unassigned sibling prose selectors through the C7 inventory in separately assigned work.

## Risks

Graph reachability ignores predicates; existing traversal siblings cover the tested histories. Predicate signatures identify conditional history independently of paragraph placement; they cannot judge prose meaning. Four control tests still fail. No acceptance or inherited-failure exemption is claimed.
