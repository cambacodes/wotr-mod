# Areelu Trickster opening: development record

Status: revised unintegrated nine-scene route prototype, still incomplete and not approved or runtime implemented.

Source: `storylines/areelu_trickster_rivalry_opening.py`.

This revision responds to `reference/story-review/areelu-trickster-opening-rereview-7.md`, SHA256 `7ED231C7FCB177D347DB0164C9D93D9905DDA829DBB2528D7CEA4289F3F43B97`.

The reviewer report is unchanged.

## Authored scope and chronology

The first scene names the exact alternate chronology: before the graft, the mortal soul belonged to an unrelated adult who had already lived an adult life.

The cited native script does not establish the soul's age or prior biography, so this is explicitly a continuity change authored for this route.

The Commander continues that adult's identity.

The dead child's remnants, Areelu's ritual, the failed restoration, the effects of the graft, and her grief remain part of this branch.

Areelu's maternal projection is preserved as a grief-driven false conclusion about identity, not as evidence that the Commander was her child.

The opening's current path contract requires the player to acknowledge this AU chronology before contact.
Every scene now requires the current Trickster path as a live condition.
An accepted contact reply may persist, but `entry_ready` alone cannot open a scene after the Commander leaves the Trickster path.

Areelu retains uncertainty about how the graft affected the Commander and resists the Commander's claim that the native answer proves his origin or settles what she felt.

She also challenges the AU premise as an assertion they have agreed to use, not something verified by the native record.

The player can assert the identity boundary, decline the memory test, leave, or choose a nonromantic rivalry.

The third scene lets the Commander state attraction without asking for an immediate answer.
In the fourth scene, only if that interest remains unwithdrawn, Areelu may state reciprocal adult attraction.
The Commander can return it, pause, decline, or end contact.
Areelu offers a hand only after mutual interest is spoken, and the Commander must ask before touching her.
This is an authored early romance step, not a commitment, a healing arc, or proof that the relationship is safe.

No scene records a committed relationship.

## Native outcome veto contract

`NATIVE_ENDING_VETO_MATRIX` identifies actual blueprint paths and asset IDs listed by the project-generated `reference/expansion/etudes.json`.

Its hard veto includes `Ending_AreeluDead` (`936af39436c74953b43a4165bfbcc9f9`), `Ending_AreeluKilledByLegend` (`26d8e09c942e4ec2a13c834706cbfc12`), `Ending_AreeluSacrifice` (`f455dbe5ddfbc454380ce27bc93795d5`), `Ending_AreeluSacrificeBefore` (`2667b0fda8704432bc35ace995e8022e`), `Ending_AreeluSacrificeTrickster` (`29c5c64462384fa3b8aae34e4c9ebce9`), and `AreeluIncinerated` (`23983059575fff749ae1446eba539260`).

If one of those terminal etudes is active, the future observer must set the mod-owned `native_conflict` outcome and block all further contact.

`Ending_AreeluSacrificeTrickster` is listed as its own terminal veto.

This report does not assert that its blueprint starts `Ending_AreeluDead`; the extracted repository inventory provides path and GUID records, not the trigger payload required to substantiate that relationship.

`Ending_AreeluRedeemed` (`127e8a018a0840b080c276b4704e58a2`) and `TE_AscendAreelu` (`63279a971792474ba0439b9f75795a7a`) require independent proof that Areelu remains alive, contactable, and willing before any continuation.

The future observer must never clear, complete, or rewrite a native ending etude.

This is an exact source-backed decision matrix, not an implemented reader or veto.

`NATIVE_CONTINUITY_VETO_MATRIX` separately names the native c6 cue `AreeluBurnTheWitch/Cue_0069` (`ec2ae0db3ba72a545b56a4fac08ecd06`), whose text says Areelu cannot think of the Commander as anything but her child.

If that cue is in native seen-cue history, the future gate must set `native_conflict` and withhold this alternate route; if it occurs during the branch, the branch must close without clearing or reinterpreting it.

This continuity veto is a design contract with no history reader or writer.

The source separates invitation eligibility from `entry_ready`.

A future interaction offers the player an explicit action to request contact after the availability and conflict gates pass.

Areelu's reply then records `contact_accepted` or `contact_declined`; only explicit acceptance can satisfy the scene gate.

The source contains a deterministic authoring-level resolver for eligibility and a one-time response transition that reject native vetoes, unavailable inputs, repeated results, and contradictory accepted/declined results.

The first scene requires both `entry_ready` from explicit acceptance and the current active Trickster path.

The solicitation, native-state readers, and game writers are not implemented.

The fourth scene's sealed chamber, bounded planar fold, and live field test are new authored campaign events.
They are not claimed as recovered native locations, scripted game events, or existing Trickster mechanics.
The scene has a knowledge check, an authored Trickster contradiction, risk and refusal options, and a choice to abandon the measurement.
Its dialogue and flags only specify desired future behavior.

## Native memory source and Trickster test

The proposed red signal is a new authored remote channel and is not the native projector crystal.

The test is grounded in the c5 `AreeluLabAgain/AreeluCell` exchange.

Native `Cue_0010` (`7faf68a4a3ef2394397fdd22efd80ffd`) asks what the Commander felt near the crib in Areelu's ruined home.

The answer choices used for this test are `Answer_0013` sadness (`0853df779fb798c4dbf2d6e106674170`), `Answer_0014` rage (`f0d826fb7b99a1e4c9e23e46534a2993`), and `Answer_0015` closeness to mystery (`9c9655606788f8b4cb039e48b2739c25`).

`Answer_0016` (`84de666a567b51c46900cc799b2237b8`) is a refusal and explicitly disqualifies the memory intervention, but not all future nonromantic contact.

The physical projector and crystal shatter at native `Cue_0009` (`591acfaf8500cc94aa7a8918db767d43`).

The story therefore never claims the object can be recovered or altered.

The state at risk is specifically the surviving native history pair `Cue_0010` plus one recorded answer, not the destroyed projector prop.

`memory_protected` now requires `cradle_memory_record_verified`, which means native `Cue_0010` and exactly one answer among `Answer_0013` through `Answer_0016` were verified.

The memory-centered second scene requires the verified record, current active Trickster path, `entry_ready`, the second-contact flag, and rivalry.
It therefore cannot display Areelu's assent dialogue after the Commander leaves the Trickster path or loses the accepted-contact gate.

`memory_contested` additionally requires the derived non-refusal answer gate, current Trickster path, scene entry, Areelu's conditional assent, and the Commander's choice to accept risk.

The contested branch leaves native answer history unchanged; the protected and contested outcomes are mutually exclusive, one-way, save-safe requirements.

No writer or save/load test exists.

The knowledge check uses the supported `SkillKnowledgeArcana` check with DC 31 to distinguish the native prompt and answer from Areelu's later interpretation.

The Trickster's authored intervention adds an impossible second annotation to a present reconstruction: its footnote cites both the question and the answer as its author, making a self-contradictory claim beside the unchanged answer.

The dialogue's memory-result choices call `memory_choice`, which builds their `Set`, `Requires`, and `Forbids` fields from the same `MEMORY_CHOICE_EFFECTS` table used by `apply_memory_choice`.

The adapter rejects unavailable path/gate/consent inputs, unverified, declined, or invalid native answers for the intervention, prior terminal state, duplicate transitions, and contradictory prior flags.

For an accepted terminal action, it preserves the native answer key and returns exactly one of the protected or contested mod-owned outcomes.

Rejected inputs return the prior state unchanged.

The graph check exercises unverified records, eligibility, non-Trickster state, Areelu's refusal, invalid and declined answers, protection, accepted risk, Commander withdrawal, repeated and contradictory prior state, and native-answer preservation.

It also checks that every dialogue choice setting a memory result forbids both terminal results, and that the contested choice carries its declared path, entry, and answer requirements.
Separate entry and choice assertions remove the current-path flag and verify that neither the memory scene, assent choice, nor safeguard choice is reachable.

Areelu now has a refusal branch before a separate conditional agreement node, so her assent is an authored dialogue choice point rather than a presumption.

This executable adapter is an authoring contract and local verification, not a game producer or runtime integration.

The second Trickster puzzle now also uses a `trickster_copy_choice` adapter and `apply_trickster_copy_choice` contract.

They permit the self-citing contradiction only against a page explicitly treated as a new authored copy, require current Trickster path, reject replay, and report that native history remains unchanged.

Local assertions confirm these choice effects and reject any attempt to use a native page as the target.

That Trickster action challenges Areelu's inference by making the margin's certainty collapse; it does not rewrite native prompt, answer, cue history, soul, graft, or past event.

Areelu consents only to testing that reconstruction and explicitly refuses to treat the effect as proof that the past changed.

The Commander may accept a lasting loss of confidence in the exact feeling he reported, protect the native answer, keep the dispute theoretical when no eligible answer exists, or withdraw.

The proposed persistent mod-owned outcomes `memory_contested` and `memory_protected` must be mutually exclusive, save-safe, and one-way in a future game writer.

`memory_contested` records only loss of confidence in the interpretation of the selected non-refusal answer; it never removes that answer from native dialogue history.

`memory_protected` retains the native answer as the only factual record.

Persistence across actual saves is still an unimplemented requirement.

Neither outcome deletes or changes native cue history.

No contact producer, state reader, intervention writer, save/load test, or runtime effect exists yet.

## Other state and review limits

The future invitation gate requires verified native soul/graft/restoration revelations, the authored adult unrelated-continuity decision, a living/contactable Areelu, current active Trickster, and no ending or continuity veto.

The separate accepted-contact result is then required by the future `entry_ready` writer.

The opening stores rivalry separately as `areelu.trickster_opening.rivalry`.

The `CommittedFlag` remains reserved as `areelu.trickster_opening.relationship_committed` and no choice sets it.

The local graph check validates scene targets, the composite-gate reference, named ending and continuity vetoes, the shared dialogue-choice/state-transition mapping, targeted memory and contact-gate cases, and the separation of rivalry from relationship commitment.

It does not validate native history reads, ending vetoes, check execution, access timing, actual flag persistence, route integration, ToyBox, or game rendering.

The third scene continues the planar-research rivalry with a working copy of a Worldwound calculation, advances Areelu's grief without implying that it is healed, and lets the Commander state attraction without demanding reciprocity.

The fourth scene makes that work consequential through an authored bounded planar fold and lets Areelu name physical and intellectual attraction only after the Commander has stated interest and left it open.

Areelu does not grant romantic consent; she says she has not decided whether she wants the same thing.

She retains explicit refusal, withdrawal, and strictly intellectual continuation options.

The nine scenes contain 9,130 words of node dialogue and 2,105 words of choice labels, for 11,235 aggregate authored words before route-specific attainability and semantic review.

The added beats are an accountability ledger with recoverable identities and an independent archivist, a relationship conversation that sets consent and non-exclusivity terms, an alternate graft proposal with destroy, research-only, and refusal outcomes, an adult private-intimacy scene with explicit pauses and non-escalation branches, and a public hearing where Areelu accepts scrutiny while protecting the assistant's choice to remain unnamed.

The graft proposal does not restore the dead child or claim that a future person could be the lost child.

It makes Areelu's desire to continue the work a conflict she must govern, including the possibility that the Commander ends the relationship because the boundary is not trusted.

The private scene stays graphic and explicit and branches on spoken consent, changed consent, touch declined, a request for space, and relationship pause or ending.

The route has not yet been measured against the 21,000 meaningful-word floor on a modeled compatible playthrough.

Its current volume is substantially below that floor, and the unintegrated source does not justify a complete-route or readiness claim.

The new prose is author-authored continuation pending adversarial canon, characterization, romance, gameplay, and line review; no reviewer score is claimed.

The local checks pass source compilation, nine-scene/72-node graph integrity, the existing memory transition contract, contact ending and cue vetoes, field-scene choice conditions, the copy-only Trickster intervention contract, and new route gate and progression assertions.

Still open are additional route progression and distinct endings, route-path word measurement toward 21,000, character art and independent art review, actual Unity dialogue binding, ToyBox compatibility, persistent writer and save/load checks, native-state readers, integration, and manual in-game verification.

Independent canon, character, romance, dialogue, gameplay, art, and integration reviews must assess the revised source separately.

No review score is claimed.

Manual in-game verification remains required after integration.
