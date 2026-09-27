# Aranka path acquisition development

Status: design draft only, not registered, not implemented in the game, and not a completed romance route.

This work adds path-specific invitation concepts and a small pure-Python predicate check in `storylines/aranka_path_acquisition.py`.

It does not edit the existing romance, the island continuation, generated Story data, or any integration.

No invitation grants affection, starts the parent romance etude, changes `RanRomCount`, makes Trickster Azata, moves or clones Aranka, or asserts that she is alive.

The proposed invitation entry condition is numeric Chapter 5, the exact active mythic path, and a runtime-produced `aranka.path_contact_verified` proof.

The path proof alone is not enough to show an invitation.

The producer must verify Aranka's identity, her living and usable state when an in-person meeting is proposed, her location, and an actual willing reply or her authored invitation before it sets the proof.

Silence, inability to find her, an absent or dead actor, an unverified memory, or an answer attributed to a duplicate must leave the proof unset.

For remote correspondence, the producer must verify that the message is authored by Aranka and that the current story state supports delivery.

An invitation's accept choice should record only that the Commander accepts a conversation.

It must not convert that choice into affection or an active romance.

Aranka must retain a plain refusal, silence, and a no-pursuit outcome.

## Path predicates and authored invitation concepts

The story baseline already resolves these aliases: `angel`, `aeon`, `azata`, `demon`, `devil`, `dragon`, `legend`, `trickster`, `lich`, and `swarm`.

The new module records their native etude GUIDs so a future integration can compare its path checks with the baseline rather than invent new path identities.

Each non-Azata draft entry requires its exact path alias, numeric chapter value 5, and `aranka.path_contact_verified`.

The runtime must treat the exact active path as current save state, not as proof that the player once selected that path.

**Angel.** Entry requires `angel`, Chapter 5, and verified contact.

The proposed invitation asks for a meeting as two people rather than a confession or absolution.

Its possible courier is a surviving Desnan pilgrim carrying Aranka's sealed reply.

No reviewed script evidence establishes that pilgrim or the message, so the producer remains unresolved.

**Aeon.** Entry requires `aeon`, Chapter 5, and verified contact.

The proposed invitation asks for one conversation without judgment about what either person must become.

An Aeon intervention could preserve a dated ordinary courier appointment, but it cannot create Aranka's presence or consent.

No inspected source establishes the appointment, courier, or an Aeon contact scene.

**Azata.** Entry requires `azata`, numeric chapter value 5, and the exact live island actor proof `native.aranka_island_actor_live`.

The existing island route remains the only evidenced acquisition context and must be reused without a duplicate invitation.

Its known island area is `31bab5549f7ea384186159a238360c8d` and its Aranka unit is `430cba7801b149b4e8494ace6baf4f7c`.

Its actor presence must still be confirmed in a Chapter 5 game save.

**Demon.** Entry requires `demon`, Chapter 5, and verified contact after the actual Demon confrontation history.

The proposed invitation lets the Commander refuse, answer plainly, or leave the letter unanswered.

The parent route excludes Demon histories in relevant continuations, and the inspected sources do not prove Aranka's survival or willingness after each confrontation.

An in-person or remote invitation remains unavailable until those exact histories and a contact source are audited.

**Devil.** Entry requires `devil`, Chapter 5, and verified contact after any applicable contract history.

The invitation explicitly places the meeting outside all bargains and gives Aranka no debt or obligation.

The parent continuation excludes the native deception and contract etudes `0b129925567b68d4fb712b4bee6c0f9a` and `5f72b252bd7fa8d48bd04c27982a4f9c`.

Neither history proves Aranka remains available for contact, and a Devil contract cannot be used to compel it.

**Gold Dragon.** Entry requires the `dragon` alias, Chapter 5, and verified contact.

The proposed invitation is an ordinary meeting where Aranka may ask about the Commander's change without turning the evening into an inspection.

No inspected source establishes Aranka's Gold Dragon placement or a witness who can deliver a message.

The `dragon` alias resolves to `PlayerIsDragon` in this project baseline.

**Legend.** Entry requires `legend`, Chapter 5, and verified contact through a mundane route.

The invitation asks for an evening without either person becoming a symbol.

The native island mechanics are nested under `PlayerIsAzata`, so Legend cannot inherit the island by reusing its area identifier.

No source-backed Legend courier or meeting point has been identified.

**Lich.** Entry requires `lich`, Chapter 5, and proof that an actual living Aranka can answer freely.

The invitation names the cost of the Commander's path and does not ask Aranka to approve it.

No corpse, memory, reanimation, or proxy may answer in her place.

The parent continuation excludes high-level Lich, and the inspected records do not establish post-Lich contact or consent.

This path remains design-only until identity, survival, location, and voluntary response evidence exist.

**Swarm.** Entry has the same formal predicate as the other path concepts, but the implementation helper deliberately rejects it while its availability is unresolved.

The proposed scene would begin with no assumed invitation and default to silence if Aranka's identity and agency cannot be confirmed.

The reviewed script evidence does not establish her survival or an authentic contact channel under Swarm.

Do not create a swarm copy, puppet, memory stand-in, or posthumous consent.

This route is presumptively unavailable unless new source evidence supports a living, self-directed Aranka.

**Trickster.** Entry requires `trickster`, Chapter 5, and verified contact.

The authored concept is a one-use chain of in-world evidence and couriers prepared by the Commander, followed by Aranka's independent choice to answer or not.

The invitation admits that the Commander made a route where events had left none, then asks whether she wants to take it.

It cannot set `PlayerIsAzata`, teleport an actor, manufacture consent, or start the parent romance.

The parent Chapter 2 and Chapter 3 introductions require Azata acceptance, while the island mechanics are nested beneath `PlayerIsAzata`.

This proposal does not solve Trickster romance acquisition because the native clue chain, courier, one-use cost, and response producer have not been found or implemented.

## Proposed runtime hook contract

1. An integration-owned observer reads the current Chapter 5 state and the exact active mythic-path alias.

2. It resolves Aranka's identity and state from a source-backed native event, not from the capital `DefaultActor`, a hidden spawn action, or a historical cue alone.

3. For an in-person invitation, it confirms the exact living actor is usable and present in the expected area when the player enters and continues the scene.

4. For a remote invitation, it confirms a real authored message or reply and a credible delivery source before writing `aranka.path_contact_verified`.

5. The observer must not write the proof for unknown, conflicting, dead, absent, hostile, coerced, silent, or unverified states.

6. A scene can be shown only when Chapter 5, the exact active path, and `aranka.path_contact_verified` are all true.

7. The scene is optional and path-specific, with an accept-to-talk choice, an explicit decline, and no penalty for silence.

8. Its choices may record invitation response state only.

9. The parent romance etude `2e98dbe685f045cdabf88b66e4cde9ff`, parent quest `1dacd3dfe1bf47c8a73074814e40b1c8`, and parent romance count remain untouched.

10. The existing Azata island scene remains under its existing live-unit and area checks.

11. The integration must register each new scene only after its path-specific contact producer and save-state tests exist.

The source-backed Chapter 5 island actor and area are known only for Azata.

The native Chapter 1 `Aranka_DesnaPriest_Spawn` action `c707b25030a78b24dab3b5d01d623a04` is not evidence of an evergreen actor.

The capital `ArankaDesnaPriest_DefaultActor` `547921e48f8f2ac42b6a79be55ba6b2d` applies a hide action and is not a safe presence check.

The massacre and fear flags `b65f601e60499194f96e551a4c833af3` and `79d2c536db98a9d43840da7ee5ee34a0` have unverified consumers and must not be treated as universal death predicates.

## Checks and limits

`python storylines/aranka_path_acquisition.py` runs a synthetic predicate-contract check for all ten path definitions, including numeric chapter gating, required proof flags, missing Trickster contact, and conflicting path flags.
The test supplies its own flag dictionary and does not verify any runtime producer, current save, Aranka identity, location, consent, or live actor.

The module is intentionally absent from `expansion.py` and `Story.json` because its required contact proof has no producer.

No Unity scene, dialogue registration, flag writer, save migration, or in-game path has been exercised.

Required next evidence includes the native outcome and contact audit for Angel, Aeon, Demon, Devil, Gold Dragon, Legend, Lich, and Trickster.

Swarm additionally requires affirmative evidence that Aranka can remain herself and answer voluntarily.

Azata requires a live Chapter 5 test confirming the existing actor and scene predicates.

Every path needs a negative test for wrong-path state, missing contact proof, refusal, silence, and conflicting contact history.

This is a path-acquisition design increment, not a completed route and not evidence of RanRomance content parity, independent review scores, approved art, or runtime quality.

The source has 10 path definitions and 278 words of authored invitation copy under the independent reviewer's recorded tokenizer.

The source SHA-256 is `7F7CA38A934ED03AE75651F8688C2C2184A799D6A0C927EE4FEB36D94B6DE3C1`.

Python syntax parsing and the predicate matrix pass for all ten paths, missing proof, conflicting path flags, and Trickster without contact proof.
