# Targona continuation development record

Research and manuscript increment, 2026-09-27; independent review is pending.

The latest source hash is `517AAA3B923EC23F2E54ABED31064778A1528CAD1309865297A71C9EA25E8DBD`.

Independent review `reference/story-review/targona-two-scene-independent-review.md` examined source hash `F164017735B9007BB8D237154533C1C37A37067910129A68476BD97D817B5462`.

Rereview `reference/story-review/targona-revision-rereview.md` examined source hash `13F96B696B12A159A7AA190350CDFC2955037C46D233D247EE4B28FF077E209D` and found three remaining continuity issues addressed in this revision.

## Source-backed foundation

The existing parent route is already Targona's initial rescue, wing treatment, check-up, mythic-power choices, chapter-four intervention, romance decision, chapter-five finale, and epilogue.

`reference/canon-review/targona-route-evidence.md` records the installed script, localization, and native blueprint findings used for this increment.

The native character is a female lawful-good celestial warrior with an adult service history, a dead brother Lariel, and an altered wing whose spiritual consequences she distinguishes from its appearance.

Native dialogue supports mixed joy and distress after freedom, her continued fear about corruption, her wish to choose what happens to the wing, and her protective role during captivity.

The parent route already gives the Trickster and Aeon histories Anograt, who has her own voice, temporary separation limits, and an existing shared intimate ending with Targona and the Commander.

The parent quest is complete only after its finale, and the extension still requires the actual completed treatment quest plus a seen terminal cue.

The native Drezen actor evidence is Angel-specific, so no source inspected here proves Targona can physically appear in Drezen for a Trickster meeting.

These are source facts from the existing research record, not independently re-decompiled or re-extracted during this increment.

## New manuscript work

`storylines/targona_opening.py` now has eight authored scenes and 58 pages.

The two new scenes now add 2,757 distinct normalized text-and-choice words by the local whole-segment counting method.

`the_open_threshold` stages a Trickster opportunity only after the player has chosen either the prior impossible paper-door trick or the ordinary-writing alternative.

The paper-door history supplies the impossible fold as a provisional pattern for joining two named places.

The ordinary-writing history instead uses a known courier, Targona's wayhouse address, and a small fate-bent dispatch coincidence.

These are two distinct authored explanations for how this Trickster reaches her invitation, rather than a single portal awarded by the Trickster label.

The Arcana check at DC 30 is an optional test and stabilization attempt for the impossible paper passage, not a consent check.

If the test fails, the Commander closes the opening before sending Targona the key or asking her to cross.

The no-roll alternative is explicitly the safe same-plane courier road, with Targona deciding whether to walk it.

Both failure and explicit decline preserve the active parent romance and continue the correspondence.

The non-Trickster branch stays in correspondence and preserves the active parent romance.

The visit's conversation grows from Targona's established warrior and Protectress identity, while letting her reject being treated as a symbol, a patient, or proof that the Commander is powerful.

Its romantic option makes her desire explicit and sensual, then gives her control over whether the evening remains tender, becomes more intimate, or pauses.

The two new scenes require the existing RanRomance romance etude, so they extend her established romance instead of silently starting one after a friendship ending.

The follow-up letters make her conditions for another visit explicit and keep the difference between the Trickster path and ordinary correspondence visible.

The altered wing remains present, and affection does not cure it, erase her distress, or require her to praise its appearance.

The scene acknowledges that Anograt's earlier note says nothing about this evening.

It assumes neither her presence nor absence, her location, nor her consent, and says a shared invitation would need to reach her separately and leave her room to answer.

## Counts and limitations

The full eight-scene module currently contains 8,112 distinct normalized text-and-choice words by the same local counter.

The six previously reviewed scenes were previously reported as 39 pages and 91 writing / 93 canon by an independent bounded review of source hash `D1552944742E7D3F4C59F900CDE634C8C43939D1C297CEA301FBF4C95126D369`.

That review does not cover this increment, and its scores must not be carried forward as scores for the eight-scene module or the assembled route.

The 2,757-word increment and 8,112-word total are arithmetic measures, not proof of meaningful selected-playthrough length, RanRomance parity, or quality acceptance.

The new module alone remains below the 21,000-word per-character planning floor.

Adding its 8,112 distinct words to the parent's reported 18,359-word aggregate does not prove a qualifying playthrough, because some pages are alternatives and actual delivery and reachability remain unverified.

A selected-path word count for the assembled route has not been measured.

The wayhouse is a newly authored temporary assignment on Golarion and is not a native confirmed location.

The player-facing narration names it as Targona's current post without stepping outside the scene to explain that it is new.

The courier road provides an ordinary same-plane return; the magical branch names both anchors, tests the passage in both directions with an empty dispatch pouch, and closes a failed opening before anyone crosses.

The module still has no commissioned artwork, live actor placement, in-game scene execution, actual save/load test, ToyBox verification, or whole-route evaluation.

It also does not implement the necessary runtime to display the authored wayhouse, construct the passage, or stage Targona's arrival, so the Trickster visit remains manuscript content awaiting integration review.

The original six-scene support remains limited to no-power / small-power, Angel, Azata, Aeon, and Trickster histories and continues to exclude materially changed demon, lich, devil, swarm, mortal Legend, and Gold Dragon states.

The `close_passage` and `close_road` responses now take Targona straight back to the wayhouse, without saying she wants to leave and then continuing the evening.

The two new scenes retain the required parent finale and active parent romance gates.

The route also checks the current Trickster state and the mutually exclusive preceding paper-trick or ordinary-writing result before offering either authored Trickster setup.

The `targona.visit_correspondence` outcome is consumed by the follow-up letter page.

The `targona.key_reciprocal` and `targona.key_unpressured` reply flags have no current scene consumer.

Their pending consumer is a future Targona visit scene that must read them to vary the next invitation and encounter; until that scene exists, they are recorded preferences rather than completed branching consequences.

The current generic RulesTests isolated walk fails on `the_key_remains_hers/start` because its snapshot lacks the preceding visit outcome required by the scene.

The source dependency remains intentional, and a dedicated sequential test is pending in the root task.

A production implementation must verify all current-state, parent-history, romance, and finale gates without creating an impossible save state.

## Next authored beats before route review

The next writing should leave correspondence-as-therapy behind and let Targona choose and lead an active problem that draws on her life as an angelic warrior.

A second substantial beat should stage an ordinary shared activity where her confidence, humor, irritation, and appetite for pleasure can coexist without resolving the wing or the captivity.

A later relationship beat should develop Targona and Anograt's mutual attraction separately from their existing attraction to the Commander, respecting Anograt's autonomy and the parent's separation limits.

That beat must offer private acceptance and refusal from each woman before any joint invitation, and it must preserve Targona's existing parent-romance decision rather than silently starting a new one.

A full route still needs path-specific continuations for every currently excluded or transformed outcome, including credible Trickster recovery and contact options for histories whose ordinary endings leave no local body.

Before any readiness claim, the expanded module requires independent canon, writing, intimacy, art, runtime, and integration reviews against the exact frozen source.
