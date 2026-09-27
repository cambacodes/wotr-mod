# Mielarah route opening rereview 4

Review target: `storylines/mielarah_route_opening.py`.

Target SHA-256 before review: `6A750C71CBFAC2F12C991680E14302EA10AF4CBFA35D761AC4400DEDFCCC041C`.

Author report: `reference/story-review/mielarah-route-opening-development.md`.

Author report SHA-256 before review: `D13D5D269C534FDF05FAD35CC084033DA2D2C6A30979990645B04D4F52B5EEA4`.

Both hashes were recomputed after review and still match.

## Verdict

This revision fixes the earlier source-model gap between the successful Trickster landing and Mielarah's later invitation.

The seven-scene graph now connects the ordinary opening and the successful Trickster branch to a delayed note, then to the amulet discussion, private evening, crew meeting, and quay day.

The focused local checks pass for those authored transitions, including refusal and delay cases.

The content is still an unregistered opening of 8,921 authored words, far short of the 21,000-word floor.

It is not all-path content, has no reviewed art, and cannot currently pass the mod's own scene validator if registered as written.

All seven scenes set `ManualOnly=True` but omit `Remote=True`.

`src/Story.cs` explicitly throws `InvalidOperationException("Manual-only delivery requires a remote scene")` for that combination.

The Trickster intervention also remains a hypothetical answer-to-cue override with no native selected-answer binding, cue suppression, scene registration, or proof that the campaign continues correctly after the changed landing.

This is not ready for integration or in-game testing.

## Independent scores

These scores assess this exact opening and its authoring contract, not a projected complete route.

Every applicable dimension is a separate gate and must strictly exceed 90.

- Character fidelity: 90/100. Mielarah keeps the captain's pride, defenses, self-contradiction, and capacity to make a coercive choice again. The dialogue still explains its ethical themes too directly and repeatedly, so it does not yet read as indistinguishable from her game writing.
- Canon and chronology: 74/100. I rechecked the installed blueprints. `Cue_0426` requires selected answer `Answer_0351` and the `CaptainMielara` etude playing; `Cue_0482` requires the separate piracy answer and the same etude. The draft correctly distinguishes those native outcomes. It still proposes interrupting the crash without a runtime hook or evidence that the cue's removal preserves the campaign state. The rough landing also strands the ship before the authored arrival/contact story, and the revision supplies no verified route from that location to its delayed berth meeting.
- Dramatic chemistry: 90/100. The shared chart task, continued conflict over the amulets, and later walk give attraction more time and character-specific behavior. The story still declares its emotional conclusions in explicit explanatory lines, and the opening's sensual content remains brief. It does not clear the required gate.
- Trickster specificity and access: 76/100. Arcana and Perception checks, a bounded weather trick, refusal, and consequence branches make the proposal legible and more specific than a route-note. The hook still exists only as the external string `mielarah.native_answer_0351_before_cue0426`; no selected-answer binding or live interruption produces it. The nine other mythic entries remain `implemented=False`, so the universal all-path access requirement is unmet.
- Authored inter-scene state: 93/100. The respectful Trickster endings now set the states required by the delayed contact, and the accepted note can set the case prerequisites. The case can produce the evening state, the evening can produce the crew meeting state, and the crew meeting can produce the quay-day state. The source's focused assertions exercise representative success and failure states and do pass. This score is limited to the Python authoring model; it is not evidence that the game persists these flags or schedules these scenes.
- Consent and agency: 96/100. The player can decline the note, evening, crew meeting, or intimacy. Mielarah keeps command and explicitly permits stopping. A successful rescue buys no gratitude or romance. The ordinary branch's delayed note is nevertheless activated by the player's choice to wait, so the authored text must continue to make clear that Mielarah herself chooses to send it, rather than implying that the player's flag creates her consent.
- Mature scene craft: 89/100. The crew meeting adds useful conflict and the kisses are mutual, bounded, and adult. Much of the prose repeats moral framing already established in the prior scene, while the promised mature romance has not advanced beyond a few kisses and a possible later day.
- Content scope: 32/100. The source has seven scenes, 72 nodes, 8,921 raw and distinct-segment words, and no complete route. The author's modeled ordinary and Trickster continuations are 5,137 and 4,440 words respectively, both far below the 21,000-word floor.
- Art and visual fidelity: 0/100 for readiness. There is no Mielarah art asset to compare with her in-game appearance or the requested redesign.
- Runtime and integration: 5/100. The module is not in `development/Story.json`. More importantly, registering the seven scenes unchanged fails validation because every scene has `ManualOnly=True` and none is remote. The native hook, contact producer, actor availability, flag persistence, and cue override are also unimplemented.

Only consent and the bounded source-model state design exceed 90.

The package fails the acceptance gate.

## Evidence checked

`py -3.12 -m py_compile storylines/mielarah_route_opening.py` passes.

Running the module with the repository root on `PYTHONPATH` reports seven unregistered scenes and 72 nodes, with valid intra-scene topology and cross-scene state assertions.

The repository tokenizer reports 8,921 raw words, 7,127 prose words, 1,794 choice words, and 8,921 distinct normalized segment words.

The export currently contains zero scenes with relationship `mielarah.opening`.

The author report correctly marks the Colyphyr parent-choice binding, Trickster interception, native cue suppression, all-path implementation, art, runtime checks, and full route as missing.

In the installed `blueprints.zip`, `Cue_0426` has `AnswerSelected` for `Answer_0351` and `EtudeStatus` playing for the `CaptainMielara` etude.

`Cue_0482` has the same etude condition with `Answer_0404` selected.

These native conditions establish the two branch gates; they do not establish a mod hook between answer selection and cue execution.

In `src/Story.cs`, scene validation rejects `ManualOnly` scenes unless they are remote.

The Mielarah module marks all seven scenes manual-only, and none sets `Remote=True`.

That validation error is deterministic before any game runtime test.

## Required work before another review

- Resolve the `ManualOnly`/`Remote` contradiction and choose a delivery model that matches a real Mielarah contact location.
- Bind the Colyphyr contact and the Trickster answer/cue transition to verified native state, then prove save, load, and campaign progression after the alternate landing.
- Explain and verify how the ship and crew get from the Ishiar hard landing to each later scene.
- Implement and test attainable routes for all ten mythic paths, including unavailable, expelled, and dead histories.
- Expand the selected playable route to at least 21,000 distinct authored words and measure an actual integrated path.
- Submit and independently review character art, then complete the separate canon, writing, path, and runtime gates.
- Keep this contribution unregistered until validation succeeds, then run headless checks on the integrated export before in-game testing.
