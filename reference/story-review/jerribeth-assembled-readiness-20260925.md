# Jerribeth assembled readiness audit, 2026-09-25

**Decision: not ready for full-route approval.**
The additions contain substantial dramatic material; the original automatic breakup-delivery defect is now repaired in the separately inspected combined stage described below.
The older future/farewell chain can also bypass and suppress both expansions.
Aggregate length remains below the documented floor.
No full-route score is assigned before those issues and the remaining campaign development are resolved.
Only this report was written.

## Inspected snapshot and content

The inspected main `development/Story.json` has 198 scenes and SHA256 `D042C85C5F5AE98C1BF591BC3380B335203F5601DEE074C6842E2CB5E390F595`.
A read-only import and complete normalized scene-dictionary comparison found exact equality between its 29 Jerribeth scenes and the three current modules.

| Module | SHA256 |
| --- | --- |
| `jerribeth.py` | `F607D73B030A2640A809081E53022938E62FF3FEBA4C66001BC485AC41FDD03B` |
| `jerribeth_consequences.py` | `F91B1B0CA826F19B6A0077CBF069DABF6B6D40F98CBAACB08146FF91EBB3DB71` |
| `jerribeth_counteroffer.py` | `1B9B535C113624FA1B31C6F6B0FCAE4729DA235051E29AD95B64953A8398A9D8` |

The project inventory function reports 18,101 raw words, including 15,307 prose words and 2,794 choice words.
Distinct-segment words total 18,059, with 42 exact-repeat words.
The remaining arithmetic gap to the 21,000 aggregate floor is 2,941 distinct-segment words before semantic and attainable-depth review.
That subtraction is not a prescription to write 2,941 filler words.

The 29 entries include five alternative epilogues and a repeatable breakup offer.
They are not 29 sequential romance meetings.
The remaining optional scenes include native-knowledge-dependent material that cannot be credited indiscriminately to every playthrough.

I also walked representative coherent scene schedules through the exported choices, respecting their Requires/Forbids, applying their actual flags and counting only visited prose and selected answers.
At each scene I selected the shortest or longest local continuing path available under the resulting history.
These are four concrete sampled chains, not exhaustive global minimum/maximum bounds or native campaign execution.

| Sample schedule | Meetings | Selected words in shorter-choice sample | Selected words in longer-choice sample |
| --- | ---: | ---: | ---: |
| Basic invitation through future, ordinary and farewell | 9 | 1,893 | 2,564 |
| Basic route plus the four general purchaser scenes and six counteroffer scenes, before future/farewell | 19 | 9,318 | 10,858 |

The second schedule omits optional native-knowledge scenes rather than inventing knowledge flags to obtain their text.
Titles, epilogues, aborted repeats and unselected answers are not included.
The fuller sample is authored-graph attainable with deliberate selection and time, but it is not what the current automatic rest order reliably delivers.
There is no requirement here that a selected path itself contain 21,000 words; the contractual floor is aggregate.

## 1. Breakup delivery starves the later content

The main export appends all core Jerribeth scenes before the consequences module and later counteroffer module.
`jerribeth.parting` is Remote, requires only `jerribeth.lovers`, and is not ManualOnly.
Its relationship-preserving choice aborts without completing the scene.
`Rules.NextRemote` chooses the first available non-manual remote scene, and `Main.Update` uses that helper for rest delivery.

After any earlier eligible core entries have been consumed, a continuing relationship reaches parting again at each rest.
The same abort leaves it eligible and earlier than every scene in the two expansions.
In an Act 3 history, commission can play first, followed by any eligible earlier native-knowledge scene, but parting then remains ahead of the purchaser invitation.
In Act 5, future, ordinary and farewell can run even before parting, creating the additional cutoff below.
Other romances in the global queue can delay these events further; they do not repair the within-route ordering problem.

The GUI Read buttons can manually select available later scenes while the relationship remains open and before farewell.
That is a workaround, not evidence that the advertised rest progression is working.
Choosing to stay in a relationship should not require the player to keep dismissing the same breakup offer to discover the campaign.

During this audit, the parent reproduced the starvation through actual `Rules.NextRemote` using the original ordered parting/offered_signature subset and valid continuation prerequisites.
The focused `--jerribeth-delivery` test fails against main198 as expected before a fix.
That parent-run red test corroborates the source-order finding; it does not reproduce the separate full future/farewell bypass or establish Unity delivery.

Required repair: make parting a manual offer using the already implemented ManualOnly contract, preserve its old ID and choices, and test that rest advances to an eligible later scene after the relationship-preserving answer.
Do not mark the breakup completed merely to hide it, since players must retain an explicit way to leave later.

## 2. Future and farewell still bypass the sustained development

`future` requires only `commission` and Act 5.
Its current continuing answers grant commitment without the purchaser consequence or counteroffer confrontation.
`ordinary` follows future and commitment, and `farewell` follows ordinary.
Both expansion modules forbid the completed farewell.
Thus the older nine-meeting core can deliver the same positive epilogue while excluding roughly ten substantial general expansion meetings.

Moving parting to manual delivery alone will not solve this.
In Act 5, the earlier future/ordinary/farewell sequence can still win the rest-order race against the expansion chain.
An early starter who stays in earlier chapters long enough can experience more content, but late installation and fast campaign advancement must not silently produce an abbreviated version presented as complete.

Required integration: define an earned future conversation using actual completed bargain/consequence evidence, with an explicit shorter-relationship choice if desired.
Give already committed saves a voluntary reaffirmation after the later development.
Add an informed farewell review and an explicit catch-up invitation for compatible old farewell saves, preserving completed history.
Use the existing narrow engine mechanism; do not clear farewell, commitment or native unavailability to manufacture availability.

## 3. The ending ignores what the new campaign costs

The ordinary positive ending currently remembers the imperfect horizon and continued private conversations.
Ascension adds access to a god, while apart and unfinished address a closed or fading connection.
These texts do not distinguish an early promise from the full purchaser and counteroffer experience.
They also do not consume the public-account/private-catalogue settlement, Serit's agreement disposition, later work or lost patronage.

The counteroffer follow-up itself is good evidence of consequences.
The public account costs invitations and exposes Jerribeth's own work to scrutiny.
The private catalogue supplies contacts while leaving Vardess able to complete the concealed recorder.
Both return the working adjustments, so neither should later become a destroyed-room victory.
Serit can be paid and released without becoming a redeemed innocent or permanently grateful follower.

Required development: at least one later played consequence of the chosen settlement before its strongest ending.
For example, use the public inspection or the private client's competing demand as an actual decision, then show what Jerribeth keeps, loses or refuses.
The counterpart should challenge something she wants beyond another private evening.
The resulting ending can remember that cost and the relationship response without listing every flag.

## 4. Canon identity is preserved; remote access remains limited

The source correctly treats Jerribeth as an oolioddroo, preserving antennae, linked delicate hands, narrow form and the high mental voice.
The invented elven guise is knowingly selected and visibly artificial.
The native evidence supports her self-interested allegiance, taste for sophisticated cruelty and desire to preserve an enemy as a possession.
The authored purchaser, Vardess and Serit are new characters, not replacements for native victims or patrons.

Wintersun condemnation and the borrowed-sun study require actual observed native dialogue.
The Xanthir conversation uses the witnessed-torture cue rather than assuming that learning his name proves the Commander saw the act.
The Vellexia-related material distinguishes knowledge of her refuge from the patron-loss state.
The native departure evidence after Vellexia's death describes leaving and despawning, not Jerribeth dying.
The correspondence fiction can therefore continue without claiming that she physically remains at the manor.

The chosen-image and spoken-thought charm is an explicit authored addition.
It does not infer unlimited cross-planar access from her native telepathy alone.
The counteroffer keeps all objects and third parties physically on her side, relaying their words through her rather than granting them a new mental channel.
The private scenes describe desired or imagined closeness without asserting touch through the frame.
These are meaningful limits, not obstacles the text has secretly already solved.

The current met-cue and unavailable-native-state gates support a narrow starting contract.
They do not establish an attainable route after every death/hostility outcome or prove uninterrupted validity inside an already open remote book.
`ContactUnit` is absent on these remote scenes, so the physical-contact continuation helper does not supply that proof.
The misleading native affection marker is correctly not used as consent.

Required work: verify native unavailability through death and scripted hostility, then implement the user's bespoke Trickster restoration/contact opportunity with actual quest connections and voluntary terms.
The existing fate line asks for a loophole; it does not create one.
Other mythics need reviewed character-appropriate conditions rather than an assumption that a lack of extra forbids means universal approval.

## 5. Writing, gameplay and art limits

The route's strongest material now has actions to judge: selling an association with the Commander, revising the sale, dismantling the recorder, using testimony or rehearsal, and choosing exposure or commercial silence.
Jerribeth remains dangerous and sometimes pleased by an outcome the Commander may dislike.
A private agreement does not acquit her native cruelty.
This is a substantial improvement over repeatedly explaining why voluntary affection interests her.

The six-scene counteroffer's Perception DC 25 has actual success and failure destinations, and the latter changes the available evidence arrangement.
The patient non-roll method sacrifices the miniature, while the earlier illusion study supplies an earned alternative.
The check is not a test for affection or access to intimate dialogue.
These distinctions deserve preservation when integrating the route.

Most gameplay nevertheless remains selecting pages in rest-delivered books.
The frame invitation, room, guests and artifacts have no demonstrated physical acquisition scene, placed actors or inventory delivery in this review.
Choose one meaningful discovery or investigation opportunity for native gameplay delivery rather than adding rolls to every conversation.
A later physical meeting would require separately established locations and access; it must not be implied by artwork of a shared embrace.

The repository contains a true-form source portrait, whose provenance explicitly uses an installed custom reference rather than a verified native raster.
Its earlier bounded art score does not establish native-likeness fidelity, guise consistency or runtime crops.
Those disciplines remain unscored or unfinished according to the art record.
No new visual inspection or art approval was performed in this assembled story audit.

## Necessary next tasks

1. Fix the repeatable breakup scheduler blocker and verify the actual rest-selection order.
2. Integrate earned future/farewell progression, a clearly labeled shorter option, and old-save opt-in continuation without rewriting history.
3. Author one sustained settlement-dependent consequence and connect it to an earned future decision and ending.
4. Implement a credible attainable Trickster contact/restoration case, preserving native outcome facts and Jerribeth's agency.
5. Deliver one original-style discovery/investigation interaction and the required portrait/guise assets, then verify real game saves, native guards, checks and ToyBox coexistence.

Those missing developments can supply necessary volume if written fully; an arbitrary additional date should not be commissioned solely to close the arithmetic gap.
The current contribution-level reviews remain useful evidence, but the assembled campaign cannot yet claim the user's full-length, original-game-quality result.

## Bounded delivery repair rereview

I inspected corrected `storylines/jerribeth.py` SHA256 `F38DB0B5CD7FBDC58001DE0D3157B0B43190687137FD4C0D3031E9CB3FFFC8A0`.
Its helper now forwards extra scene metadata, and parting explicitly sets ManualOnly true.
The behavior is supported by the independently reviewed shared engine's manual-delivery contract.
The conversation remains eligible for GUI Read and no longer competes for automatic rest selection.

A fresh read-only comparison between main198 and `development/combined-progression-review.json`, containing 207 scenes, found exactly one changed field across all Jerribeth objects: `jerribeth.parting/ManualOnly`, absent before and true afterward.
All existing scene IDs, nodes, choice labels, indices, destinations and effects remain identical.
Current source dictionaries exactly match the combined stage's Jerribeth dictionaries.
The inspected combined-stage SHA256 is `70D09CC9150AF3141ECC72C8934FA16A56AF69599701A57017B8C9A60F5EED79`.

The parent reports that the formerly failing queue fixture now passes and that the combined stage passes 8,146,173 rule assertions.
This reviewer independently checked the source and object delta, not the execution of that suite.
The bounded breakup-scheduling fix is accepted.

The separate future/ordinary/farewell bypass remains unchanged.
The repair does not make full development mandatory, reopen old farewells, add earned ending variants, implement Trickster contact, close the volume gap or establish game-level delivery.
Finding 1 above documents the reproduced defect and its cause; its requested ManualOnly repair is now complete in the inspected stage.
All other assembled readiness findings remain open.
