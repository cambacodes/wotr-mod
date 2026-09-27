# Nocticula lodge arc independent review

The seven new lodge visits pass this scoped literary and source-graph review, but the completed route still fails the minimum selected-length requirement.
The shortest measured completion is 20,141 words, 859 below 21,000.
This is not release, TTS, manual-play readiness or full-route approval.

## Frozen evidence and scope

- `storylines/nocticula_continuation.py`: `532A37F3DC2EEB30745CE84F085CC5F60E4C3F726BEA4BF7A9FFBAE434EC5763`.
- `reference/story-review/nocticula-further-development.md`: `E19A7667BA4C4FBD389D34DA0ED1CE6295C3184B2AA04AD7E1B942B1B1E01678`.

I read the actual prose and choices of `empty_chair`, `mask_and_bell`, `uninvited_guest`, `closed_gallery`, `unborrowed_evening`, `bell_without_master` and `no_applause`.
I also inspected the shared withdrawal helper, the following `what_she_keeps` visit, ending predicates, the prior current-route review, the final withdrawal rereview and the local parent-extension canon audit.
The literary scores below cover this new arc and its immediate joins, not a fresh independent approval of every older scene.
No source, test or export file was edited.

## Character and political causality

Istrava's performance follows from the harbor affair: injured investors can buy a public humiliation of the protection Nocticula has offered.
Using substitutes keeps the surviving passengers out of an implausibly repeated kidnapping while making the new danger concrete.
Istrava's interest is prestige and patronage, rather than a credible attempt to defeat a demon lord in direct combat.
Nocticula explains why simply banning dinner would concede the story her enemies want to sell.
Her intervention therefore has a reason to involve planning, witnesses and an audience despite her overwhelming personal power.

The strongest characterization is practical and occasionally unpleasant.
She wants Vhal alive for his knowledge, but tells Rhez to drop him if carrying him would cost her escape.
She values a surviving hostess who can finance her own defeat.
She favors acquiring the lodge, objects when closure costs money, and rejects the Commander's attempt to offer their private room as compensation for every concession.
The captured hostess tries another loophole concerning private rooms; the surviving informants still want distance; Rhez refuses dinner and asks for a replacement coat.
None becomes grateful or agreeable merely because a romance needs the operation to end well.

The good and ambitious choices have distinct objects: return identifiable possessions, seize an institutional foothold, reject private access, bait out additional names, close the lodge or retain an information post.
The conquest options do not offer unrestricted cruelty, but their advantage to Nocticula is explicit and the Commander must accept responsibility for it.
That is a defensible scope for this particular operation, not proof that the whole route supplies every desired evil role-playing option.

The local parent audit supports an accepted dream relationship, conditional knowledge of her larger ambition, other-lovers acceptance and a meaningful Trickster connection through Socothbenoth's scheme.
It does not establish this lodge, these agents, the bell or the political settlement as native lore.
The source and development report correctly identify them as authored additions.
No native dialogue extraction was independently repeated for this narrowly scoped review.

## Agency, intimacy and voice

`unborrowed_evening/close` contains the kiss and reciprocal initiative.
`talk` supplies a chair, a separate plate and conversation, then joins `want` and `honest` without entering `close`.
`leave` goes directly to its own completion, explicitly without a kiss or promise, and continues the investigation rather than demanding intimacy as payment.
The later bench scene offers presence and distance without narrating a new kiss.
A refusal of this evening is not a permanent breakup; the text does not mislabel it as one.

The room above the perfume seller supplies an effective personal detail because Nocticula refuses to invent a charitable outcome she does not know.
Her decision to admit wanting the Commander is earned through a disagreement about withholding facts, rather than a sudden declaration that love has changed her nature.
The romance is adult and graphic and explicit.
Danger remains in her appetite for power, withholding and manipulation, rather than relying on explicit sexual description.

Two polish issues remain below blocking severity.
At `no_applause/agent`, the narrator's explanation that nobody has acquired a permanent position in the Commander's crusade reads like an implementation assurance.
Replace it with what these particular people actually decide to do, leaving recruitment status to documentation.
At `no_applause/credit`, Nocticula says she acquired an advantage "or agreed to lose one" even though the lodge outcome is already known.
An outcome-specific sentence would sound like her recollection rather than an author accommodating both branches.
The repeated explanations that an offer does not purchase obedience sometimes over-explain behavior the scene has already shown.
The distinctive jokes, concrete objects and resistant responses keep this from becoming a blocking voice failure, but another polish pass should trim those explanations rather than add more.

## Branch and runtime-facing evidence

The engine starts a scene at `Nodes[0]`, as shown by `src/Main.cs` lines 205 and 338.
The independent traversals used that rule, not the human-facing `Entry` label.
All new first nodes are the intended starts.

The Use Magic Device check has a successful silent-bell plan and a failed-reading guest entrance.
Failure does not loop back to a repeatable check.
The direct guest option remains available without a roll.
The Trickster announcement changes public expectations and exposes Vhal; it does not magically replace the bell's activation requirements.
The remembered operation is explicitly over when shown, so the player's questions cannot retroactively command its participants.

The selected preparation controls the operation page.
The silent and announcement branches write `lodge_unmarked`; the guest branch writes `lodge_mark_ended` and `lodge_rhez_hurt`.
`no_applause` reads those flags to select either Rhez's wound and recovery or her later employment decision.
The diplomacy failure produces an overt guarded intervention rather than a successful quiet hearing.
Both private-offer choices receive separate later accounts of the evidence gained and political price.
Closing and retaining the lodge have separate outcome pages and persistent addon history.
The four earlier pressure methods mostly converge after their immediate resolution; these flags should not be advertised as implemented city simulation or an additional downstream quest.

The local choice graph has no cycle or dead end under the inspected predicates.
I independently reached every visit node and choice across the five optional-history inputs and both check outcomes.
The graph's acyclicity establishes one attempt within a completed scene traversal.
Persistence, reloading during checks and native roll execution remain engine/in-game matters outside this source review.

The new chain requires each preceding completion and uses twelve-hour delays.
`what_she_keeps` now requires the lodge consequence completion.
The additional seven intervals total 84 hours of authored minimum delay.
These are scheduling declarations, not evidence that the current save will trigger all visits correctly.

The shared withdrawal response remains phase-aware.
The new `no_applause` is correctly in the late group, after the settlement, while the unresolved visits use undertaking withdrawal.
Closure writes addon-only flags, retains the earlier bargain, grants no undertaking completion and blocks all later source visits and ordinary completion recollections.
The new arc does not override rejection, death, loss of the Gift or a missed parent encounter.

## Independent selected-length measurement

I executed a separate Python traversal using the repository's `words()` tokenizer, actual first nodes, answer predicates, both check destinations and accumulated choice effects.
It counted only displayed prose and the selected answer, with exactly one eligible ordinary recollection at completion.
Aborted postponements and permanent withdrawals were excluded from completed-route lengths.
All 32 combinations of Trickster, the two Laulieh histories, heard parent ambition and exposed Socothbenoth plan were supplied as fixtures.
These are predicate fixtures, not a claim that all combinations are organically attainable in one native campaign.

Future-equivalent states were merged only after preserving minimum and maximum prefix costs.
An independent second run merged equivalent histories across the fixture batch and reproduced the same extrema.
The different repeated-closure totals below reflect that optimization, not different story coverage.

| Measurement | Result |
|---|---:|
| Complete route plus one ordinary recollection, minimum | 20,141 words |
| Complete route plus one ordinary recollection, maximum | 22,481 words |
| Seven new visits, minimum selected path | 6,996 words |
| Seven new visits, maximum selected path | 7,838 words |
| Reached visit nodes | 185 of 185 |
| Reached visit choices | 277 of 277 |
| Checked repeated closure outcomes, separate fixtures | 65,888 |
| Checked repeated closure outcomes, merged fixtures | 7,084 |

Every examined closure lacked `noct.complete` and admitted no later visit or ordinary recollection under source predicates.
The independent private-evening check found that the refusal terminal cannot reach intimacy and the talk branch cannot reach the kiss page.
No visit choice writes the inspected parent-active, rejection, native-death or Gift bindings.
The frozen source hash was unchanged after traversal.

No aggregate source words, repeated closure boilerplate, incompatible alternative or parent-wide inventory was added to selected length.
The new arc contains substantial connected consequence material, not merely a collection of alternative responses inflating an inventory.
Its short path remains legitimate, particularly the private-evening refusal.
Additional shared story development is needed; compulsory intimacy or counting unselected material cannot repair the shortfall.

## Strict scoped assessment

| Dimension | Score | Result |
|---|---:|---|
| Nocticula voice and resistant characterization | 93 | Scoped pass |
| Antagonist motives and political causality | 93 | Scoped pass |
| Commander choices and witnessed consequences | 93 | Scoped pass |
| Earned adult intimacy and clean decline | 95 | Scoped pass |
| Prose specificity and pacing | 92 | Scoped pass, polish noted |
| New-arc source branch consistency | 95 | Source-only pass |
| Authored versus native disclosure | 95 | Documentation/source pass |
| Every completed path at least 21,000 meaningful selected words | Not met | Blocking failure |
| Native delivery, ToyBox compatibility and persistence | Not certified | Root/in-game verification required |

Scores are not averaged, and no percentage converts the length or verification failures into approval.
The root owns regenerated export validation and the updated C# suite.
I did not run that suite, Unity, an actual save, ToyBox, a rendered interaction or an art audit for this task.
Universal Trickster acquisition, parent rejection recovery, death recovery, Gift replacement, triad development and portrait review remain outside this extension's demonstrated behavior.
