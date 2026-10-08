# noct-reconcile: locked scenes changed (coordinator approval needed)

Scope is text, plus two append-only explicit-slot hosts (cloud finish pass). No existing scene, node or choice ID, choice position, gate, flag or check was changed; the only additions are the appended slot choice and its `.explicit.1`/`.aftermath.1` nodes in noct.last_buyer and noct.empty_chair (see `storylines/nocticula_n3.cloud_slots`).
The diff was measured on integrated text hashes (`tools/voice_lock_lint.text_sha`) of the route payload
before this job (da6ee44, with N3's early-withdraw anchor bypassed) and after it.

## Live scenes
| Scene | Change |
|---|---|
| noct.last_buyer | Full re-voice ("The tour": Ossin in her cells, the lamp room, four outcomes). Cloud finish pass: the start check rolls `CheckBluff` DC 33 (set by nocticula_n1; the field is unchanged), so its label now says Bluff ("Tell him his partners already sold him to her, and watch his hands"), and `guarantor`/`false_lead` open with that bluff instead of a ring reading. Appended optional explicit slot on `named`: choice "[Make her collect for it here, under the lamps.]" -> `noct.last_buyer.explicit.1` (heated cut) -> `noct.last_buyer.aftermath.1` (authored), which re-offers the host exit unchanged. |
| noct.hearing | Check label now names its rolled skill. The check rolls `CheckIntimidate` DC 32 (set by nocticula_n1); the previous pass wrongly labelled it Knowledge: World, so it now says Intimidate. Moved a misplaced narration beat in `incomplete`. |
| noct.her_own_face | Orphan quote in `start` got a narration beat. |
| noct.demonstration | `witness` path no longer says "whole" after the `instrument` path crushes one hand ("Spare her hands"). |
| noct.empty_chair | The returned passengers are no longer said to be "downstairs" (that contradicted the sold/released/harem outcomes). Cloud finish pass: appended optional explicit slot on `vow_guard`: choice "[Keep the mask on.]" -> `noct.empty_chair.explicit.1` (heated cut) -> `noct.empty_chair.aftermath.1` (authored) -> "[Plan the entrance.]" unchanged. |
| noct.unborrowed_evening | The escaping guest is "the one I let out of the hedges", so the line also holds after the guest massacre. |
| noct.no_applause | `run.caught`: she no longer relents ("Fine."); crying raises the price. |
| noct.what_she_keeps | `return_condition` agrees with the hearing, where Ilvara admitted it. The `rival` line is re-voiced (it was soft). |
| noct.uninvited_guest | "Three days ago" became "An hour ago" (it is the same night). |
| noct.ending_death / sacrifice / changed / aeon | Rewritten. They came from an older draft (bollard, lens, a sea, "the account"). Titles changed too. |
| noct.bell_without_master | `keep`: Istrava's season opens "tomorrow night" (was "at the end of the month"), so no_applause/kept_account ("Last night.", two nights after the lodge) holds. Cloud finish pass. |
| noct.ending_limit | Its opener is now "When the harbor and the lodge were done". |
| all scenes with the legacy exit (sixth_passenger, captains_reply, her_own_face, demonstration, return_count, another_place, hearing, last_buyer, empty_chair, uninvited_guest, unborrowed_evening, bell_without_master, no_applause, what_she_keeps, second_door) | The N2 and N3 `withdraw_undertaking` texts are reconciled into one EARLY_WITHDRAW and one LATE_WITHDRAW in `nocticula_continuation.s()`, and N3 now asserts them. The exit choice text is arc-neutral ("running your errands" / "Your business is settled"). |

## Retired scenes (choice text only, via the shared exit choice)
noct.after_the_lamps, noct.closed_gallery, noct.cost_of_return, noct.counterseal, noct.lamp_measure,
noct.mask_and_bell, noct.voices_in_glass, noct.white_shoes.
