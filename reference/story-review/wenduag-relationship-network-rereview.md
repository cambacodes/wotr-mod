# Wenduag and Vellexia relationship-network independent rereview

Review date: 2026-09-27.

Reviewed source SHA-256: `9C84D12E81A07636042A68CE4343FBF5B701A2A8B71760CF0F9E7574D6970109`.

Reviewed development report SHA-256: `D6C3EC315BBF67C0070F755EE85AF6A14BE9FF5459BFB512AEB83F1B0E5C74DB`.

Prior review SHA-256: `A05A403DC7FC8E2DCCBB222B4EB9A223D8DA0F04B435EE2B2AC27108C13397B7`.

This review inspected those exact source and report hashes, the prior findings, the relevant Story runtime contact and relationship-state checks, the native Wenduag jealousy flag record, and the cue action that unlocks it.

I did not edit the source, the author's report, integration files, or generated story data.

Disposition: revision still required before integration review.

The source remains an unregistered interlude draft, not a completed Wenduag route, Vellexia route, triad, or romance outcome.

## Prior findings

**[Fixed] Wenduag's native unit identifier now uses N format.**

The value is `ae766624c03058440a036de90a7f2009`, which matches the audited native unit after GUID normalization and satisfies the project's `Guid.TryParseExact(..., "N", ...)` validator.

**[Fixed in source, still blocked at runtime] Both current actors use supported contact fields.**

The scene now uses `ContactUnit` for Wenduag and `AdditionalContactUnits` for Vellexia.

`src/Story.cs` recognizes both fields and checks both IDs against `Snapshot.AvailableContacts`, along with the scene's chapter, area, requirements, and relationship availability.

The scene is still unavailable in an integrated build because `wenduag.vellexia_network.reception_history_verified` has no producer and the file is unregistered.

The author correctly labels the producer as unimplemented and does not claim that metadata alone proves current actor presence.

**[Mostly fixed] The native reception history is distinguished from the authored interlude.**

The scene requires the addon-owned `wenduag.vellexia_network.reception_history_verified` alias, and the proposed producer observes native unlockable flag `23cacf7a07480da459b3a59d0fd6da82`.

The native flag record is a `BlueprintUnlockableFlag`, and the inspected native `Velexia_Main/Cue_0104` on-stop action sets it after its preceding cue conditions.

The report calls the new encounter authored material and says event timing still needs verification.

The alias has no implementation, so the exact cue-to-history mapping remains a pre-integration task rather than a tested gate.

The authored opening places the encounter at a reception, but no runtime evidence yet shows the scene can follow the native event at that same reception with both original units available.

**[Fixed as a claim, unresolved as a scope choice] The nonexistent active-romance alias is gone.**

The source no longer requires `wenduag.ran_romance_active`, and the report does not claim that this scene requires an active Wenduag romance.

It now presents this as an independent relationship-network interlude gated by the jealousy-history alias.

Whether the native jealousy flag can be earned without an active Wenduag romance, and whether this authored scene should appear in that state, still need an explicit design decision and a source-backed predicate.

The draft does not establish that either woman is attracted to the other.

**[Fixed] The entry label is framed as a recall rather than a native quotation.**

`[Recall Wenduag's jealousy at Vellexia's reception]` no longer attributes a paraphrase to an exact native line.

## Remaining findings

**[High] Vellexia's acceptance is still selected by the Commander rather than stated by Vellexia.**

At `vellexia_answer`, her last authored line is, `Then let me make my own answer.`

The next player option is `Let Vellexia accept a conversation on her own terms.`

Choosing it sets `wenduag.vellexia_network.invited` and advances directly into the conversation without an affirmative answer spoken by Vellexia.

The added decline branch is a real improvement, and Vellexia clearly says no there.

The privacy branch also allows no answer that night.

The acceptance branch still asks the player to choose Vellexia's yes immediately after she says she will make her own answer.

Give Vellexia a separate, visible affirmative response before the conversation begins, or leave the scene at an unanswered invitation.

**[High] The committed relationship flag says this one-conversation interlude has chosen a relationship.**

`RELATIONSHIP.CommittedFlag` is `wenduag.vellexia_network.invited`.

`src/Main.cs` treats a set `CommittedFlag` as a chosen relationship and displays, `You have chosen a relationship. Later meetings follow campaign progress.`

The `vellexia_answer` acceptance choice sets that flag for one conversation, and the privacy choice also sets it despite explicitly asking for no answer that night.

That conflicts with the source and report, which say that the scene establishes no romance or shared arrangement.

Do not use the committed state for a conversation invitation or an unanswered deferral.

Keep an accepted conversation, a pending response, and an actual relationship commitment separate.

**[Medium] `followup_possible` is written but has no consumer in this draft.**

The conversation and privacy branches can set `wenduag.vellexia_network.followup_possible`, but this source contains no callback scene or response handler that reads it.

The report accurately says this is only one interlude, so the missing scene is not misrepresented as complete route content.

Before integration, either remove the persistent flag or implement a reachable later callback that rechecks both women's independent consent.

The privacy path must not make a later meeting look scheduled or accepted by either woman.

**[Medium] The native history producer and reception timing remain unevidenced implementation work.**

The code's `PRODUCER_CONTRACT` explicitly has `implemented: False`, and the report says the scene is unregistered.

No current integration writes the required alias.

The proposed producer should verify the native flag's actual unlock action and its cue prerequisites, then confirm the exact units, Chapter 4 state, manor area, and valid timing together.

Do not treat Wenduag's historical jealousy flag alone as proof that Vellexia is presently reachable or open to a new conversation.

**[Medium] The report's local graph-check claim is not covered by this module's own assertions.**

I independently checked all ten choice targets and found no unresolved internal target.

The source's `__main__` assertions verify path-map size, node count, contact-field shape, the N-format identifier, and the unimplemented producer marker, but do not traverse the choice graph.

This is a report precision issue rather than a graph defect.

## Confirmed checks and limits

Both supplied current hashes match the inspected files.

Running the module's local assertions succeeds.

The scene has ten nodes, and every non-empty internal choice target resolves to one of those nodes.

A whitespace split of node prose and choice text yields 1,120 words, matching the development report's count.

The development report correctly identifies the slice as unregistered, below each character's content floor, and incomplete for path access, full routes, art, independent reviews, and runtime testing.

The source and report do not establish mutual attraction, romance, or a triad, and this rereview does not infer any of those outcomes.

No Unity save, actor presentation, current-contact behavior, campaign timing, path eligibility, or ToyBox behavior was tested.

## Disposition

The Wenduag unit format, supported additional contact field, refusal dialogue, and corrected entry label address the corresponding prior findings.

The acceptance still lacks Vellexia's own explicit affirmative response, and the committed flag incorrectly announces a chosen relationship for a conversation or unanswered deferral.

The unused follow-up flag, reception-history producer, exact reception timing, and deliberate decision about whether an active Wenduag romance is required remain unresolved.

Do not register or count the slice as a completed romance route until those issues are resolved and the separate content, path-access, review, art, and in-game gates are met.
