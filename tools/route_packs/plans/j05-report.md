# CHANGES

J05 is **partially implemented**, not release-accepted. Branch `claude/J05`,
base `c3005840`. No commit, following the final user instruction. No scores
are claimed.

- `storylines/harem_rows/z_j05_restitution.py`: append-only registration on
  the three existing S18X/S26 hosts. No emitted scene, clock, retry, currency
  debit, attraction gate or reconciliation condition is added.
  One unlocked old player answer and its Ledger clause now say no remedy
  was *inspected*: actual delivery followed by declined inspection must not
  falsely report that no supplies arrived.
- `tests/test_harem_row_j05.py`: physical action chains, negative histories,
  reload resumption, old identities/destinations/text, safe answers, absence
  of blocked producers and unchanged voice locks.
- `tools/route_packs/plans/prose-pending.json`: three appended rows:
  Horzalah's `j05_instructions_destroyed` in `account` and `account_table`
  (05), and Jerribeth's `j05_cache_offer` in the S26 account (07).
- `tools/route_packs/plans/j05-material-contracts.json`: separate six-child
  canon/plausibility reviews, distinct stock portions, required action
  witnesses, costs, negative histories and exact implementation blockers.
  The manifest is evidence/disposition, never a runtime producer.

| Ruling | Result and evidence |
| --- | --- |
| 05 / S18X | **Consumer implemented; surrender blocked.** Reserved root index 0 retains `remedy`. It now requires actual readiness, carried instructions and surrendered trap knowledge. The appended destruction terminal publishes `captivity_remedy_delivered` and Horzalah's inspection/destruction costs, keeps the accusation, and shares the original account exhaustion. None of its three prerequisites has an emitted producer. The required surrender host, `hepzamirah.trickster.body.terms`, is locked. |
| 07 / S26 | **Implemented, with Jerribeth prose pending.** Current tenant disclosure, selected living recipients, physical retrieval, actual unloading and Gesmerha's inspection have separate witnesses. Only unloading produces `remedy.authorized`; verification needs all action/cost witnesses. The Ledger distinguishes delivered relief from the original no-remedy account. Failed/abandoned retrieval and refusal remain owed. Reload resumes surrendered/retrieved goods without another surrender. Destroyed-clan success stays unavailable because this base establishes no displaced/refugee recipient adapter. |
| 10 / K1-S | **Blocked.** N9/N10 support duty and a research-preserving bargain. Burial preservatives/crates, recovered remains, actual use and Seelah's inspection are authored and still unproduced; no named native casualty invented. |
| 11 / K1-E | **Blocked.** N11 supports living charges. Separate storage timber/tools, current Pulura survivors, actual repairs and Eliandra's inspection remain unproduced. Ch3 OR Ch5 acquaintance remains the prescribed boundary, not an added met-Ch5 requirement. |
| 12 / K1-TG | **Blocked.** N12 establishes alteration, not retained matter. Only the approved inert preparation sample may be destroyed; no soul/cure/barrier change. Pickup, destruction and Targona's inspection remain unproduced. |
| 13 / K1-G | **Blocked.** N13 selects only the actual Irabeth-death history. The ordinary secret approach and escort need actual wounded arrival and current Galfrey/Kitrane inspection, not a map-only flag. Neither royal authority for Kitrane nor a returned Iz unit is created. |
| 14 / K1-TD | **Blocked.** N14 is Areelu's temporary-relief account. A separate mundane instrument set requires pickup, delivery, actual triage by current returned Terendelev and inspection. No return flag becomes equipment/use or a Wound cure. |
| 15 / K1-N | **Blocked; no incident/docket emitted.** N15 admiration cannot establish an experiment. The chosen physical destruction, current Nenio witness, distinct replacement residue, repeated control and inspection are still missing. No recreated Nenio inherits an original woman's memory. |
| 16 / packets | **K1/K3 blocked; K2 remains retired.** K1 cannot complete six missing children. This base's S18F emits nothing and S23 only emits turf/history; J03 concessions are not integrated. S48 alone cannot produce K3. Existing `approved:false` reservations and singleton obligations are retained; no packet-wide yes, pardon, retry or invented saving. |

All cited N4/N6/N8–N15 assets and localized boundaries were reopened in
`/wrath/blueprints.zip` and enGB.json. N8's actual answer list and projector
destruction were checked. New notes/cache and all proposed material portions
are explicitly authored; no native cue is relabelled as restitution.

# CLASS SWEEP

Checked both S18X wrappers, all reserved index-0 destinations and shared
exhaustion; S26 truth/illusion/Marhevok/clan-destroyed branches, tenant/host
forms and current-loss adapter; every new pre-action Later/refusal/failure,
resume choice and verification terminal; all six distinct Areelu child
requirements; K1/K2/K3 reservations and missing sibling producers. Checked
all 576 voice locks. Existing node order, choice indices, text and destinations
are retained apart from that one corrected unlocked player label. Ordinary
nodes have no conditional paragraphs. No new echo,
foresight knowledge, departed body, cure, affection or pardon is supplied.
Existing edited JSON retains LF line endings; no generated repository file
was edited.

# GATE

All export/tests used `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, the four
build parent-binding manifests, and `/wrath`. Export and logs were kept in
system temp. The final wording correction received supplemental checks
as described below.

| Command | Result |
| --- | --- |
| `python expansion.py` with `RRT_STORY_OUTPUT` in system temp | PASS, 4,054 scenes. Runs: 196.798s, 179.050s after action-order/terminal changes, and final 236.271s after two history-wording corrections. |
| `python tools/savecompat.py --story <temp>/Story.json` | PASS, 0 hard failures. |
| `python -m unittest tests.test_utf8_io -q` | PASS. |
| `python tools/payoff_lint.py --strict --story <temp>/Story.json` | PASS, 42 routes, 0 hard failures. |
| `python tools/departure_lint.py --strict --story <temp>/Story.json` | PASS, 43 women, 0 hard failures. |
| `python tools/voice_lock_lint.py --strict --story <temp>/Story.json` | PASS, 576 locked, 0 changed, 0 missing/ambiguous. |
| `python tools/slot_brief_lint.py --strict --story <temp>/Story.json` | FAIL: 320 briefs, 315 hard findings, 168 warnings. Read-only comparison against untouched `development/Story.json` gives **identical findings**, including all 315 hard findings. No J05 explicit slot exists or was added. |
| `python -m unittest tests.test_harem_row_j05 tests.test_harem_row_s18x tests.test_harem_row_s26 tests.test_utf8_io -q` | PASS, 31 tests in 210.042s. First run exposed two new-test fixture/assertion errors; both corrected. After the last wording correction, J05 + UTF-8 rerun: 16 tests passed in 8.709s. |
| `python tools/rrt_verify.py --strict --story <temp>/Story.json --game /wrath` with reports in temp | FAIL, one invocation, runtime 826.8s, 13 hard failures. All are unchanged locked Jerribeth player-text findings: 11 commander-gender, 1 embedded-commander-speech, 1 speaker-attribution-review. Read-only baseline/final comparison using the verifier's exact `player_text_lint` + `player_text_baseline.new_findings` pipeline gives identical 13 hard findings. Shipped structural errors and draft contract diagnostics: 0. |
| `tools/managed_tests_linux.sh /wrath/ <temp>/Story.json` | PASS, exit 0: epilogue 0/1/wrong-type, load, missing `irabeth_dead` and missing `trickster` fixtures. Both managed builds succeeded. Headless Unity/Mono warnings and one existing nullable compiler warning remain. |
| `git diff --check`, UTF-8/line-ending/scope/artifact checks | PASS. No src/tests/managed-tests obj/bin directories. All new files decode as UTF-8 and use LF, matching the touched row/JSON style. |
| Final-export supplemental checks after the two wording corrections | PASS: `rrt_verify.validate(Model(final))`, savecompat, all voice locks, payoff and departure: 0 failures; final J05/UTF-8 tests as above. |

No unittest discovery, full RulesTests, build-expansion.ps1, harness, game,
installation or commit was run.

The single whole strict verifier invocation and the managed script were
started before the last two unlocked wording corrections. The final export
received the supplemental checks above. Those two changes alter no gates,
flags, graph structure, voice locks, native hooks or slot boundaries.

# ESCALATE

1. **Locked-host append conflicts with required zero changed.** Approved rule
   1 requires new pending nodes/choices in the Hepzamirah and Areelu hosts.
   `voice_lock_lint.text_sha` hashes *all* ordered node/choice text, including
   additions. A read-only probe appending one pending node to the wager host
   produced exactly one changed lock. No append-only exception is present.
   Resolve that policy with the voice/tooling owners. Locks/lint were not
   rewritten to hide changes. A separate native pickup/escort scene also
   requires explicit J07 schedule/allowance approval under the proposal's
   scheduling boundary; it cannot bypass the conflict for free.
2. Integrate J03's S18F/S23 actual concession producers, then assemble K3;
   activate K1 only after all six physical children and inspections exist.
   J07 owns the exact ledger and singleton fallback proof.
3. Slot-brief owners/J10 must fix the 315 unchanged base hard findings. They
   concern other routes' brief schemas, boundaries and narration, beyond
   the entries J05 names. No unrelated brief or route prose was edited.
4. Jerribeth voice/lint owners must resolve the 13 unchanged strict hard
   findings in `jerribeth.farewell`, `jerribeth.ending_together`,
   `jerribeth.ending_ascended`, `jerribeth.offered_signature`,
   `jerribeth.counterfeit_guest`, `jerribeth.counterfeit_audience` and
   `jerribeth.counterfeit_spoil`. All seven scenes are voice-locked and none
   is a J05 named entry. No text or lint exception was changed there.
5. Claude must fill the three emitted pending prose rows before narrative
   acceptance. S18X surrender still needs its separately authorized locked
   host attachment and corresponding pending rows.

# PROPOSE

None beyond the approved rulings. No additional mechanics, gates, prices,
reconciliation policies, returns, thresholds or scenes are proposed.

# RISKS

Full J05 acceptance is blocked. The page is only an opportunity gate;
positive outcomes still require actual actions. The S26 destroyed-clan
negative is intentional until real recipients exist. S18X delivery remains
inert; K1 children and K1/K3 remain unimplemented. Pending villain prose
cannot be treated as finished voice work. Managed checks establish headless
construction, not game play or independent rubric scores. Final coordinator
progression/audit coverage and inherited slot-brief fixes remain outstanding.
The strict zero-hard-failure requirement is also unmet by the inherited
Jerribeth findings; this report does not claim a passed release gate.
