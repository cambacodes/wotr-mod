# Aranka path-acquisition independent review

Status: revision required for source-backed access predicates; no route is approved.

Reviewed source SHA-256: `E171CEB7DBEF9FD897D474123490ED889E66901489DC52CA48673F79CD4DFD01`.

Reviewed development report SHA-256, recorded before review: `41BDCEAA17844D7E1EFD9D26D240566625E01CBFD75A1AF3942EE4BB7D7FA744`.

## Findings

**[High] The `chapter.5` requirement has no producer or registered meaning, so all synthetic success cases overstate what the game can satisfy.**

The module requires `chapter.5` for every route, while `src/Main.cs:469` currently emits only `chapter_one` or `chapter_later` as chapter-derived flags.

`src/Story.cs:194-203` checks numeric `Snapshot.Chapter` against `MinChapter`, `MaxChapter`, and `Chapters`, and `src/Story.cs:249-258` lists recognized derived flags without `chapter.5`.

Search found `chapter.5` only in this module, with no producer or registered Story alias.

The `_self_check()` fabricates every required flag directly from `entry_requires`, so its passing Chapter 5 assertions do not establish that an actual Chapter 5 snapshot satisfies the predicate.

Represent this condition using a source-supported numeric chapter check or scene chapter metadata, or add and verify a real producer before describing it as an executable proof.

**[High] The other required proofs are contracts only, not current runtime state.**

`aranka.path_contact_verified` and `native.aranka_island_actor_live` occur in this design module but have no producers or Story registration in `src`, `storylines`, or `development/Story.json`.

The report acknowledges that contact must be runtime-produced and that the prototype is unregistered, but the pure predicate checks cannot establish identity, life, location, consent, message authenticity, or live actor presence.

The shared contact boolean also does not encode which audited contact source or history established it, so an eventual adapter must bind the proof to verified route-specific evidence and current state.

**[Medium] The all-ten-path matrix is a design inventory, not an attainable all-path access system.**

The ten path aliases and GUIDs match the current `development/Story.json` etude identities, including the intended `gold_dragon` to `dragon` mapping.

However, this module has no runtime adapter, invitation scene, producer, or registration, and `invitation_entry_ready` only tests caller-supplied boolean flags.

Swarm is deliberately rejected while its availability begins with `Unresolved`, so there are ten definitions but only nine potentially passable synthetic cases.

The report appropriately calls the work design-only and says Trickster access remains unsolved; neither the module nor its self-check proves a bespoke, attainable Trickster route or access for every path.

**[Medium] The Azata live-actor predicate is not backed by this module's checks.**

The development report identifies the existing island area `31bab5549f7ea384186159a238360c8d` and Aranka unit `430cba7801b149b4e8494ace6baf4f7c`, and the current `development/Story.json` contains scenes using that area and contact unit.

The module's `native.aranka_island_actor_live` requirement is still an invented proof alias with no observer, and no save/runtime check confirms that the actor is alive, usable, and present when the scene is entered.

The report correctly requires an in-game Chapter 5 check and warns against duplicating the existing Azata entry, so its caveat is directionally accurate.

**[Low] The report's invitation word count is off by one under a reproducible word-count rule.**

Counting the `invitation` values in the reviewed Python file with `re.findall(r"\b[^\W_]+(?:['’][^\W_]+)*\b", text)` yields 278 words, while the report states 277.

This does not affect functionality, but the report should name its tokenizer or correct the count for reproducibility.

## Confirmed strengths and report fidelity

The path alias-to-etude mapping matches the current Story export for all ten entries, and `gold_dragon` correctly checks the native `dragon` alias.

The source explicitly labels itself design-only and unregistered, does not set romance or parent quest state, does not create or move Aranka, and avoids modifying the existing Azata scene.

Its invitation prose preserves voluntary refusal and silence, and the proposed Trickster intervention is framed as a route to contact rather than fabricated consent or forced romance.

The report accurately states that the module is not integrated, lacks a runtime producer, does not establish content parity, has no approved art or independent reviewer scores, and has not been tested in Unity.

The report's safety boundaries around Swarm, Lich, absent or dead actors, remote-message provenance, and unverified native state are appropriately cautious, though they remain future implementation requirements.

## Required follow-up before access review

Replace `chapter.5` with a check grounded in the actual numeric chapter state or verified scene metadata.

Implement and test current-path, contact, and Azata live-actor producers against real save-derived state, including negative cases for stale path state, missing or conflicting evidence, refusal, silence, death, absence, and duplicate identity.

For each non-Azata path, establish source-backed contact and voluntary response evidence, with a distinct attainable Trickster intervention; leave Swarm closed unless affirmative canon evidence supports survival and agency.

Register and exercise the access scenes only after those producers exist, while preserving the existing Azata acquisition and parent relationship state.

This review covers a path-acquisition prototype and its report only; it does not approve a complete romance route, route length or quality, art, reviewer scores, integration, or runtime behavior.
