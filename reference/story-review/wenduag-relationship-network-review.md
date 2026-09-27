# Wenduag and Vellexia relationship-network independent review

Status: revision required for interaction consent and actor-contact metadata; this is an unregistered interlude, not an approved romance or triad.

Reviewed source SHA-256: `983D158E8C6147FD4EB214B936E696F458F7FF00262E9D0480CB00311C4498FB`.

Reviewed development report SHA-256: `F35BBE30BA0D0533DE6615608E9268201AB2143784AE076E7FA4CE13EF70619E`.

## Findings

**[High] Vellexia has no authored refusal outcome, contrary to the report's consent claim.**

The invitation says Vellexia can refuse, and the report says she is free to refuse, but the only response node states, "I will grant you a conversation."

Its choices let the Commander stay silent or withdraw the invitation, but none lets Vellexia decline, defer, or leave without accepting.

Add a direct refusal or postponement response and ensure no follow-up flag is set as an accepted conversation unless she affirmatively chooses it.

**[High] The declared actor fields do not make both women live contact requirements in the current Story schema.**

`src/Story.cs` defines `ContactUnit` and `AdditionalContactUnits` and `Rules.ContactAvailable` checks those fields against current available contacts.

This scene uses `ContactUnit=WENDUAG_UNIT` but puts Vellexia in the unrecognized `PartnerUnit` field and puts the proposed contact proof in unrecognized `ContactProof` metadata.

The only Vellexia requirement in `Requires` is `vellexia.greeted`, which is a historical greeting cue, not proof that her actor is presently alive, usable, and in the manor.

Use the supported additional-contact field or a real producer-backed state gate and verify current presence at the scene; keep the integration blocked until the proof is implemented.

**[High] Wenduag's ContactUnit is not in the GUID format required by the project validator.**

The source supplies `ae766624-c030-5844-0a03-6de90a7f2009` with hyphens, while `src/Story.cs` validates `ContactUnit` using `Guid.TryParseExact(..., "N", ...)` and requires a 32-character N-format identifier.

Use `ae766624c03058440a036de90a7f2009` to match the audited native Wenduag blueprint and the project format before integration.

**[Medium] The source does not gate the specific native reception or jealousy history it names as the scene's continuity anchor.**

The native records establish Wenduag's jealousy about Vellexia, and a later vulnerability line recalls "the same look you saw that time at Vellexia's"; the route audit cautions that this proves rivalry and shared history, not mutual attraction.

Here the code requires `vellexia.greeted`, which maps to the initial native manor greeting cue, plus Chapter 4 and the manor area; it does not require a reception cue or Wenduag's native Vellexia-conflict flag.

The custom `native.wenduag_vellexia_reception_both_actors_verified` is not included in `Requires` and has no producer, so it currently does not bind the scene to that event.

The prose may use the reception as a new authored shared moment, but the entry contract and report must distinguish this from verifying that the native jealousy event occurred.

**[Medium] The active-romance alias is not bound to a native state in this module or current Story export.**

`wenduag.ran_romance_active` appears only as a required flag in this file and is absent from the current `development/Story.json` and project story sources.

The report accurately describes the intention to require active Wenduag romance, but no native alias or producer currently establishes it.

Bind the predicate to an audited native romance state before treating it as executable, and test its lifecycle against parent endings.

**[Low] The Entry label quotes a different, later vulnerability line and is not text from the reception itself.**

The native transcript records the later line as "I must look like a snotty messy now," while this scene uses "I must look like a snotty mess now" as its Entry label.

Use an accurate short label or identify it as a later callback rather than implying it is the reception's spoken line.

## Confirmed strengths and report fidelity

The native material supports a Wenduag and Vellexia jealousy/rivalry connection, but does not establish attraction between the women; the report makes that distinction accurately.

Wenduag's authored dialogue names curiosity, competitive respect, and possible appetite without claiming she is already in love, and the Commander is not positioned as a prize by the consent language.

The nine-node graph imports successfully, all local targets resolve, and the module's local assertions pass.

A direct whitespace split of the authored node and choice text yields 1,031 words, matching the report's approximate count.

The report accurately calls the file unregistered and incomplete, marks nine path concepts unresolved and Trickster as proposal-only, and says this slice is not a missed-romance acquisition route.

It also accurately leaves both complete route floors, future triad opt-in, independent reviews, art, integration, and runtime verification unfinished.

## Disposition

Fix the missing Vellexia refusal path, actor-contact schema, Wenduag GUID format, reception-history distinction, and romance-state binding before any integration review.

The authored scene is an early relationship conversation only; no mutual attraction or triad outcome is established by it.

This review does not approve a complete Wenduag route, a Vellexia route, a triad, path access, art, or runtime behavior.
