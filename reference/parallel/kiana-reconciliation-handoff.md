# Kiana changed-history reconciliation

Source released for independent review on 2026-09-26.
This is authored alternate continuation, not a claim that the native game resolves Elan's fate this way.
No quality score is assigned by the author.

## Reproduction

The baseline development Story hash was `D5E26EF079857222B1D306ECDD6E928F3755FCB6DFD829AB9DD03647A9DF9B87`.
Using the actual serialized choice predicates, a state with `kiana.separated`, `kiana.waited` and `seelah.elan_dead` had no selectable answer at eight marital-history selectors.
A state with `kiana.bereaved` and no `seelah.elan_dead` had the same eight failures.
These were `guest_table/history`, `market_weather/past`, `blue_room/box`, `blue_room/supper_later`, `bakery_stairs/history`, `a_place_afterward/history`, `yard_evening/history` and `unborrowed_evening/history`.
The complete C# campaign tests now reach those pages through actual invitation, courtship, separation or widowhood, morning and Seelah scenes before changing the native snapshot.
The native change is test setup, never an authored effect.

## Implementation

`storylines/kiana_reconciliation.py` exports two new optional manual correspondence scenes and `integrate(payload)`.
Append `SCENES` to the payload, then invoke `integrate` after the existing Kiana overlays and further module.
The integration appends two answers and two context-specific pages at each of the eight selectors.
Original node IDs, prose and answer indices stay intact.
No native bindings, engine predicates, new derived state, revival operation or actor spawn are introduced.

The separated/death branch acknowledges bereavement after an existing separation without granting `kiana.bereaved` or taking back the separation.
The formerly bereaved/no-death-evidence branch admits uncertainty instead of declaring Elan alive.
The story continues from each added passage into the same shared activity used by the original branches.
This keeps future promises, the roof supper, writing activities and optional intimacy reachable without rewriting the earlier relationship.

`kiana.former_grief` develops a memory of Elan, the difficulty of being expected to defend a separation after death, and a choice between sending Meral a private memory and asking him about a possible gathering.
Neither choice claims Meral has answered or that the gathering occurred.
`kiana.uncertain_reports` develops a practical request for witness names, dates and locations, a choice of written replies or asking Lenna for help, and a difficult exchange with the Commander about what reliable news could change.
Lenna's agreement is not assumed.
The Commander offers no invented sighting and no resurrection.
The supper invitation remains a future arrangement.

Both letters are manual so existing completed promises and farewell saves can opt in without restarting their route.
They remain unavailable after relationship closure or on the existing inhuman exclusion.
Deferral sets no flags.
Outcome flags occur only on the terminal answer, leaving interruption replay consistent.
There are 31 added pages, including 16 overlay pages, and approximately 3,432 prose words by the local punctuation-aware count.
This is aggregate authored text, not the length of one playthrough.

## Evidence and scope

`reference/canon-review/kiana-authoring-predicates.json` records native `Elan_Dead` as `148423f1d35917946a5ebeeb4f19246c`, at `World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Seelah_Friends/Elan_Dead.jbp`.
The installed expansion consumes that evidence through existing alias `seelah.elan_dead`.
The same evidence file records Kiana's married aftermath cue `81109ea8fb20dbc478cf67116740f4a1`, widow aftermath cue `aebbc1845e827dd4da4e28014e7b4162`, and souls-returned quest `5a5a533c9ce630a48b877f9a194840cb`.
These facts support preserving the already played history rather than retroactively classifying it from the newest snapshot.
The absence of a playing death etude is not proof of a living actor.
No physical returned-Elan encounter is implemented here.
His possible native unit identity `8a863b65171271a44abdeded092a628f` must be independently verified for a later actual-contact extension; this module does not bind or consume it.
The death etude can be historical, so a later witnessed living return while the death etude remains set still needs an explicit supported continuation.
This contribution does not solve that separate case or rewrite native quest consequences.
It also does not repair incompatible external states containing both authored separation and bereavement, or neither outcome, nor a death change during the earlier unfinished marriage-answer sequence.

## Verification

Source comparison proved every original node's non-choice fields unchanged and every original answer array preserved as an identical prefix.
All 16 changed-history selector cases select exactly the corresponding new alternative.
An isolated temporary .NET harness using the actual Story, Snapshot, Rules, Program.Copy and Program.Walk implementations ran `KianaReconciliationTests.Run` successfully: 8,728 checks.
The harness was outside the project and registered only this suite after Story deserialization; its early return emitted the expected unreachable-code warning for unused later test registration.
No production file needed a temporary test hook.
The suite plays waited, affair and widow histories with and without later snapshot changes, checks all new history pages, completes the developed capstone, checks old-farewell manual availability, preserves native and unrelated romance flags, and restarts every visited added correspondence page and overlay page from an interrupted snapshot.
It does not establish Unity delivery, native saves, physical actors, portrait rendering or ToyBox runtime behavior.
Root still needs to register the suite, stage the combined payload, run the complete rule and managed suites, and obtain independent literary and integration review.
