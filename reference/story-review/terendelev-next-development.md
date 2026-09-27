# Terendelev next development checkpoint

This is a draft checkpoint for an authored continuation, not a completed route or an approval.

The authored scenes are in `storylines/terendelev_continuation.py`.

The module is deliberately not registered in `expansion.py` and does not alter generated story data.

Its only purpose at this stage is to establish distinct, character-led narrative branches and expose their missing implementation dependencies.

## Evidence boundaries

The source for this checkpoint is the independently reviewed [Terendelev continuation audit](../canon-review/terendelev-continuation-audit.md), the [parent route join contract](../canon-review/terendelev-parent-join-contract.md), and the [materialization API review](../canon-review/terendelev-materialization-api.md).

The audit distinguishes native game facts from RanRomance continuity and new authored proposals.

Native game material supports Terendelev's protection of Kenabres, her Iomedaean obligations, her opposition to innocent suffering, and the use of a human form in the city.

The existing RanRomance route already contains the split-scale premise, the accepted courtship, nonexclusive relationship terms, the star ritual, and separate returned and scale-confined endings.

The continuation treats those events as history that must be checked, not as scenes to replay or proof that Terendelev remains romantically willing in every later moment.

The new Kenabres rebuilding petition, its organizer, its residents, the fixed-sky investigation, and the new private oath are authored alternate developments.

They are not represented as recovered native quests, native dialogue, or universal Pathfinder lore.

The continuation does not turn Sevalros into a former spouse, Halaseliax into a romantic rival, or any male character into a participant.

The candidate two-woman relationship is Targona, because the existing parent ending supplies conditional attraction between the women.

That ending is evidence for an opportunity to write mutual courtship, not evidence that Targona and Terendelev have already agreed to a triad.

No Targona relationship scenes are included in this checkpoint.

## Manuscript in this checkpoint

The returned-person branch begins after a verified accepted RanRomance romance ending.

Terendelev sends a new invitation and explicitly says that the old oath does not replace present choice.

The meeting allows the Commander to answer without claiming credit for her return.

Terendelev chooses physical affection, asks before escalating, and can decline or defer intimacy without ending the relationship.

The civic story asks the pair to answer for a rebuilding petition that uses her name as a public seal.

The Commander can find discrepancies, ask about notices, listen to Terendelev's concerns, or make a less informed decision.

The petition branches into a suspension and repair plan, narrow verified evacuation with lodging and return rights, or a costly decision to proceed with weaker oversight.

Terendelev disagrees when the Commander leaves risk with residents and does not reward agreement as the price of romance.

The inspection follow-through turns the petition decision into a second playable consequence, including who bears the repair cost and who can challenge the revised schedule.

The private oath continues the relationship through desire, duty, affection, non-ownership, and the ability to revise a promise.

The windward book-event memory gives Terendelev a sensual adult scene in which she decides whether to recall flight, remain in human form, accept touch, and choose the pace of intimacy.

The event is explicitly a memory and does not claim that the party traveled to a real map or that she transformed.

The returned-person branch also includes a narrated Kenabres vigil where Terendelev chooses how to remember the dead, rejects being used as a public endorsement, and can ask the Commander to leave her answer to her.

A morning-after scene lets both characters discuss desire, boundaries, and the ordinary work that resumes after intimacy.

The scale-confined branch is separately gated as a Trickster proposal.

It begins with Terendelev asking for evidence rather than a performance of power.

The player can investigate the scale, the preserved claw, a living witness, and the Storyteller's prior account.

The intended clue model distinguishes evidence of a bounded memory from evidence that a crossing is safe.

Knowledge: Arcana and Knowledge: World provide approaches to the same rule, while a failed roll leaves a second-witness path open.

Terendelev stops a nonliving boundary test when it produces a crack and an unknown darkness.

She explicitly rejects the idea that the possibility of escape makes the risk automatically worth taking.

The draft now includes a non-romantic continuation for a parent friendship or rejection terminal.

Terendelev explicitly says that success in the investigation cannot cancel her refusal, and the Commander can withdraw without another contact.

Only after an independent identity-history review and a later choice by Terendelev does the draft offer a new courtship conversation.

This is authored alternate development, not an existing parent option or a canonical claim that Terendelev will change her mind.

It remains a proposal pending independent character and consent review.

The draft also contains a separate no-parent-romance lead using the native Storyteller account, native scale, claw, and Ravener history.

This scene requires a future integration predicate named `terendelev.continuation.native_lead_available`.

That predicate must be produced by exact current inventory, clue, and encounter checks, not by a text choice or a substitute item.

The current scene only establishes a research path and explicitly does not turn a collectible into a person or a soul-vessel.

It does not yet create a verified way to contact Terendelev after the parent romance route was never entered.

For a save with no RanRomance Terendelev route or completed parent quest, the current blocker is specific: the script can establish where the claw collectible was placed and what the Storyteller once searched for, but it does not establish a present communication channel or currently available soul.

The next design decision is to identify a real, chapter-five source of voluntary contact after the Trickster verifies the native clue and Ravener state.

Until the game evidence supports that source, the no-parent-romance lead remains a gated research scene, not an attainable route.

The draft stops before a crossing, a resurrection, or physical arrival.

The new other-half sequence uses the audited distinction between the native Ravener death event and the scale-bound fragment.

If the Ravener remains active, the Trickster waits for the actual Iz encounter rather than suppressing it.

If the verified `MonsterDead` history is present, Terendelev may choose whether to investigate what is missing, while the dialogue states that the death is not a soul reunion.

The scene does not reset Iz, replay combat rewards, hide the remains, or alter Galfrey's history.

The `native.terendelev.ravener_dead` binding comes from the reviewed native recovery evidence and still needs a binding-loader and lifecycle review before use.

This stop is intentional because the other soul fragment, current native encounter state, destination, and live delivery service have not been resolved by the manuscript.

The scale scenes are intended as remote contact and do not imply a living body.

The current source metadata now marks all ten scale and memory scenes as remote with no physical contact unit.

A previous source revision accidentally marked them as physical contact, as recorded in the correction section below.

## Evidence carried by the manuscript

The returned ending cue set is `8bf0fdc74bae4ef79dcfe04036e813ab`, `4791f49d19624dafa2ea1ae6dd18c588`, `30b3341acced4fa793dcc92dfe3587a9`, and `10fe0c7bd80d441c8688c37babc19f66`.

The scale-confined ending cue set is `0e09ddffd8fb40e7b1a0b147906b57cd`, `f0233d7ac79b4557b0f8f5f18a077940`, `2ef521fa2e8d468db335980dc2166174`, `1a10b8880b054837b2bb2802d11020b7`, and `48a730e870d94c73bc61afecaf1c8540`.

The shared parent quest is `a1d66e27b73d4d819d138868d681280b`.

These identities come from the separate reviewed parent binding manifest.

Their presence in this manuscript does not mean that the route loader has registered them or that the game has constructed these scenes.

The returned-person chapter combines its exact ending cue set with the parent romance and completed quest requirements, and every physical scene additionally requires confirmed actor delivery.

The scale-confined Trickster chapter does not require the parent romance etude, allowing a separately authored route after a completed friendship, rejection, or separation outcome.

It still depends on the parent quest, scale-bound state, and exact cue history, whose runtime lifecycle requires independent confirmation.

An integration reviewer must confirm the installed parent's exact etude lifecycle and the game's cue-history semantics before this can be treated as an executable gate.

The physical contact blueprint in the module is a candidate identity from the recovery research, not approval of its appearance, components, caller, or runtime behavior.

## Remaining narrative and content work

The independent audit estimates 22,000 to 25,000 distinct new words across a full continuation and requires at least 21,000 meaningful words after review.

That is a target, not the count of this draft.

The current module is a partial manuscript with its returned invitation, civic issue and follow-through, private oath, windward intimacy, Kenabres vigil, morning-after scene, and expanded Trickster investigation.

An import and scene-text count on the previous checkpoint found 9 scenes and 6,969 node-text words.

The present version adds parent-rejection and friendship handling, native-evidence acquisition design, and an identity review, so that earlier count is stale.

The current version has 17 scenes and 98 nodes.

The repository tokenizer measures 9,845 node-text words plus 1,585 choice-text words, for 11,430 combined raw words before deduplication.

Those counts include repeated or structurally necessary text and are not a content-quality judgment.

The route therefore has at least 11,258 additional words to write before it could possibly reach the 21,000-word minimum, with more likely needed after distinct-prose and playthrough checks.

The count includes repeated text across branches and therefore is not the meaningful distinct-word count used for route acceptance.

It has no complete physical-return campaign, no sustained sequence of subsequent Kenabres visits, and no complete scale-escape route.

It does not yet support the missing-scale history, a consumed claw, a destroyed connection, released soul, former Lich coercion, an interrupted finale, incompatible terminal histories, or a late-install path.

Those histories must be separately researched and given attainable story paths rather than being folded into a universal success flag.

The authored civic issue needs review against the native rebuilding and crusade state before production can claim any changed town, quest, budget, evacuation, or resident outcome.

The current scene text narrates a proposed result, but no game action currently produces it.

The manuscript has no independent content-word audit yet.

No single-playthrough word range has been computed.

Repeated strings, scene metadata, choice boilerplate, and unreachable alternatives must not inflate the final distinct-word count.

The draft remains far below the route's 21,000-word acceptance floor and must be expanded with consequential scenes rather than repetitive interior monologue.

## Character and relationship review still required

An independent reviewer must check Terendelev's voice against the native and parent scenes and flag every place where grief, romance, or Trickster cleverness makes her too agreeable.

The reviewer must check that she retains agency over civic work, memory, bodily intimacy, her oath, escape, and any possible relationship with Targona.

The review must decide whether the authored rebuilding conflict follows her demonstrated duty and mercy without reducing her to a civic symbol.

A separate reviewer must assess the mature romance for adult desire, chemistry, negotiated power, meaningful disagreement, and consistency with the existing courtship.

The current kiss and private-oath scenes are not evidence that the route's maturity or spice target has passed review.

An independent canon reviewer must examine all authored claims and verify every parent ending gate against its exact outcome.

No reviewer should be asked to approve an unregistered draft as though it were playable content.

## Targona opportunity

The parent ending can place Targona and Terendelev in a later mutual-attraction context when the relevant dragon and romance conditions apply.

The continuation should use that as a first meeting point for a separate women-only relationship arc, not as an automatic triad award.

Both women need private scenes in which they choose each other independently of the Commander.

They need a shared task, a genuine disagreement about duty and transformation, a private conversation, and separate opportunities to accept or decline a three-person relationship.

No shared dialogue scene should erase one woman's refusal because the other has accepted.

The actual ending conditions, character state, and delivered identities need to be rechecked before those scenes are written.

## Art and adult design

No art is included or approved by this checkpoint.

The existing audit requires visual inspection of the native human render and the parent portrait as separate references before producing a new design.

The character should read as an adult Terendelev through her facial identity, hair, silhouette, and recognizable clothing motifs while remaining conventionally attractive.

Her design must preserve the visual language of the model and parent portrait rather than replacing her with generic formalwear or generic dragon seduction imagery.

Adult sensuality may appear in private relationship scenes and art, but a reusable identity portrait does not need nudity or an erotic pose.

The image reviewer must judge resemblance, attractive humanized treatment, age presentation, material details, composition, and consistency with the in-game counterpart.

The image reviewer must not be told that a high rating is expected.

## Runtime and verification gates

This module has no integration with `expansion.py`, no registered relationship metadata, and no compiled or managed construction test.

The code uses known project authoring helpers, but that is not proof that its IDs, choice graph, conditions, or scene metadata are accepted by the production loader.

The parent bindings must be wired through the reviewed fixture system and verified against the installed RanRomance assembly.

The runtime must reconcile prior returned, scale-confined, Aeon-survivor, aware-undead, Lich, and native death outcomes without deleting unrelated actors or replaying a parent ending.

Trickster escape needs a real state machine for investigation, accepted consent, native other-half resolution, destination authorization, and a stable saved actor identity.

The reviewed delivery service must be registered before save deserialization, submit at most one stable entity identity, await the creation tick, and confirm the exact usable actor in the intended scene state.

No dialogue can narrate successful arrival before that postcondition is true.

The restored actor needs a verified conversation caller and safe unit behavior without inheriting inappropriate prologue behavior or combat recruitment.

The civic choices need actual state changes or their text must be revised to remain explicitly hypothetical.

Headless checks must cover route seeding, every branch, failed checks, deferrals, declines, mutually exclusive ending histories, idempotent delivery, save/load, and preservation of the parent's action lists.

Actual Unity testing must cover rendered appearance, physical placement, interaction startup, load and reload, area transitions, and duplicate prevention.

The full game test must use the installed parent mod and ToyBox Free Love and No Jealousy, and it must check that the parent and addon consequences remain coherent.

## Current checkpoint assessment

The work is a useful narrative and topology draft, not a route ready for the user's manual playtest.

The separation between living-return and scale-confined branches is present in concept and cue gating, but still needs code review for parent lifecycle correctness.

The relationship contains adult affection and negotiated intimacy, but it has not been reviewed for character fidelity, pacing, or maturity.

The Trickster has a plausible investigative approach based on evidence and a testable contradiction, but no complete attainable escape, other-half resolution, or confirmed return.

The story does not yet meet the minimum word count, does not include its Targona relationship, and has no approved art.

The module must remain an unregistered candidate until those gaps are closed and the independent reviewers approve its actual content.


## Independent review revision and current gate status

This section supersedes earlier checkpoint wording wherever it described the no-parent acquisition route as presently attainable or implied that the authored boundary experiment and returned meeting already occur.

The independent review of source SHA256 `35B1B32313537767ABDDDCD9BFE3CEDDA5ABAEC6CE7A39940907C8ECA02EC823` identified unproduced state hooks and unsupported encounter narration.

The revised source removes `native_lead_available` and specifies a one-use authored Storyteller memory-signal that carries one invitation and permits an explicit yes, refusal, or silence.

The proposed cost is the currently held native claw, if available, or a unique Storyteller favor if the claw is absent.

Neither cost action nor signal is implemented, and the clue is never described as a soul vessel.

A response handler must persist the attempt, enforce one use, reject missing or conflicting native history, and set the answer state only after an explicit affirmative reply from Terendelev.

The no-parent scene remains unavailable until a registered caller supplies verified Chapter 5, Trickster, native quest, original clue, and native Ravener-outcome state, then opens contact only after the voluntary response.

The native scale is a finite consumable and its possession, collection history, and charge are distinct facts, so the draft does not nominate it as an unverified message carrier.

Parent outcome research confirms that terminal cues, rather than the common completed quest alone, distinguish the returned finale from the scale-confined finale.

The returned terminal cue set is `8bf0fdc74bae4ef79dcfe04036e813ab`, `4791f49d19624dafa2ea1ae6dd18c588`, `30b3341acced4fa793dcc92dfe3587a9`, and `10fe0c7bd80d441c8688c37babc19f66`.

The scale-confined terminal cue set is `0e09ddffd8fb40e7b1a0b147906b57cd`, `f0233d7ac79b4557b0f8f5f18a077940`, `2ef521fa2e8d468db335980dc2166174`, `1a10b8880b054837b2bb2802d11020b7`, and `48a730e870d94c73bc61afecaf1c8540`.

The returned scene now also requires `terendelev.continuation.returned_actor_confirmed`, which only a future registered delivery service may set after confirming the exact actor is alive, usable, and present in the expected destination.

A returned-ending cue does not by itself create a persistent actor, and neither the invitation nor the garden prose may run while delivery remains pending.

The inspected parent etude definitions are marked action-startable, but the available decompilation does not demonstrate a complete start/stop lifecycle for `RanRomTereBound` or `RanRomTereRavener`.

The continuation therefore uses terminal cue history for scale-confined entry and does not use the parent Ravener etude as evidence that the native Ravener is alive.

The native living branch requires a future verified-live predicate and forbids the verified-dead predicate.

The native dead branch requires the exact native `MonsterDead` outcome and forbids the verified-live predicate.

The live predicate must require the actual native encounter actor to be present and alive while `MonsterDead` is absent; absence of the death etude alone is unresolved, not proof of life.

The native death binding is `42e220d5dadc4dfd8bb3ef23cae832eb`.

No native state reader currently produces either of the new mutually exclusive verification flags, so both Ravener pages remain unavailable until that reader and its lifecycle tests are registered.

The identity review now sends witness and remains evidence through distinct prose and distinct verification flags.

The combined review choice requires both verified flags, and its text makes no claim of full soul recovery or living return.

The boundary experiment now routes through changed, unchanged, and unsafe reports from an observer contract instead of narrating a successful crack automatically.

Only the changed result permits a recorded changed outcome, and even that result does not authorize crossing.

The unchanged result records a null result, while the unsafe result closes further experimentation.

No observer, persistent result writer, or runtime test exists yet, so those outcomes remain design branches rather than playable test results.

The route source now includes a ten-path availability contract for Angel, Aeon, Azata, Trickster, Lich, Demon, Devil, Gold Dragon, Swarm, and Legend.

That contract is a project requirement, not evidence that any route adapter exists.

At this checkpoint, no path-specific no-parent contact or scale-bound escape adapter is registered or tested, including the Trickster adapter.

Path-specific hooks must change the credible intervention and its consequences without changing Terendelev's consent or bypassing native encounter outcomes and confirmed physical delivery.

The scope still does not provide an attainable no-parent route for missed, interrupted, consumed-clue, incompatible-history, or late-install states.

Those states need separate predicates and authored outcomes before universal Trickster availability can be claimed.

The wider ten-path requirement also remains unimplemented for every path-specific continuation adapter.

## Remaining acceptance gates

The manuscript must exceed 21,000 meaningful words, with selected-playthrough depth assessed rather than raw choice inflation.

The repository tokenizer counts 17 scenes, 98 nodes, 9,845 raw node-text words, and 1,585 raw choice-text words, or 11,430 combined raw words before deduplication.

At least 9,570 additional combined raw words are needed to reach 21,000, and a meaningful-word audit remains outstanding.

A meaningful-word audit has not been completed, and the draft is not a complete route.

The new contact mechanism, its exact cost behavior, persistence, voluntary reply, refusal, silence, expiry, and replay prevention need registered game code and focused state-machine tests.

Native item possession and history, native quest completion, and mutually exclusive living/dead encounter evidence need typed readers and tests against real saves.

The boundary observer must produce exactly one save-safe result and tests must establish that an unsafe result cannot reopen the experiment or enable escape.

The parent cue histories and parent etude lifecycle require fixture tests against the installed parent assembly, including interrupted dialogue, each terminal cue, and incompatible histories.

The returned actor needs private blueprint registration, a stable identity, delivery caller, ordinary creation-tick confirmation, save/load adoption, usable physical conversation, duplicate prevention, and in-game area-transition tests.

Every mythic path needs a distinct attainable route adapter and character-consistent resolution, with Trickster preserving the deliberate fate intervention and other paths preserving fitting restrictions.

The full romance still needs an independent canon review, writing and maturity review, art review, word-count audit, registration review, ToyBox compatibility run, and manual game test.

No reviewer has approved the revised source, and no route, art asset, resurrection, or physical arrival is marked complete.


The previous source measurement of 10,267 node-text words is superseded because it does not reproduce the repository tokenizer.

The current tokenizer totals 9,845 node-text words and 1,585 choice-text words, for 11,430 combined raw words before deduplication.

No distinct-word or substantial single-playthrough measurement has been established.

The returned scene requires the unproduced actor-confirmation state, and the unresolved `native_lead_available` placeholder is absent.

These checks validate source structure only and do not verify runtime registration, actual source-state predicates, scene insertion, resurrection, or physical delivery.


## Remote contact correction and reopened review gates

The previous source revision passed uppercase `Remote=True` to the local `add` helper, which silently discarded it and emitted all ten scale and memory scenes as physical contact with Terendelev's living blueprint.

The current source passes lowercase `remote=True`, rejects the unsupported uppercase spelling, and runs construction assertions that each of the ten remote scenes has `Remote: true` and no `ContactUnit`.

The seven physical scenes receive the future `returned_actor_confirmed` requirement centrally in the helper, retain the physical Terendelev blueprint as `ContactUnit`, and are checked at module construction.

Those delivery flags are still unproduced, so this is a corrected scene contract rather than a working actor-delivery implementation.

The scale-evening continuation previously required the original `PARENT_ROMANCE` etude after the authored new-courtship scene, which blocked later romance progression for parent friendship, rejection, or separation histories.

It now requires the newly authored `new.courtship.open` and `romance.confirmed` states instead, preserving the original parent history while allowing the explicitly accepted new courtship to continue.

This repairs that local gate only; the new scene graph remains unregistered and untested in game.

The repository measurement on the revised module is 17 scenes, 98 nodes, 9,845 node-text words, 1,585 choice-text words, and 11,430 combined raw words before deduplication.

The same repository tokenizer reports 11,430 distinct normalized whole-segment words for this snapshot, but this is not a meaningful-word or attainable-playthrough certification.

The revised source SHA256 is `D1744F54076BE63536232ED45D040D266CAB74DE1425B138A0EA93E14C1A30CD`.

Focused checks confirm ten remote scenes with null contact units and seven physical scenes gated on confirmed actor delivery.

The original independent reviewer has not approved this revision, and the full route remains far below the 21,000 meaningful-word floor.
