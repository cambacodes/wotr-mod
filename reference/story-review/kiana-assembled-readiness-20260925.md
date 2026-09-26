# Kiana assembled readiness audit

Kiana has substantial later development, but the assembled route is not ready under the full-character requirements.
The principal remaining delivery defect is that ordinary rest selection reaches the old farewell before the appended continuation, then closes access to that continuation.
The route also remains below the content floor, lacks a later commitment decision and choice-aware full-campaign endings, and supplies no native investigation or exploration gameplay.
I do not assign a full-route score.
I edited only this report and did not author the three reviewed modules.

## Reviewed assembly

The initial main export was `3FE9752DFE46B98F8FA0878088192CE671FAC1346DBA65BCBE3D640F3176C357`.
During the audit, the parent corrected the first-invitation prerequisite defect described below.
The current reviewed main export is `D042C85C5F5AE98C1BF591BC3380B335203F5601DEE074C6842E2CB5E390F595`.
Its Kiana scenes exactly equal the concatenated current modules, including the consequences module's effective combined preparation/supper graph.

| File | Current SHA256 |
| --- | --- |
| `storylines/kiana.py` | `01EAB47BE6FF3476A2AF415F163FD8A5EDCFEF1DE89B40DA4A85A02272BDD715` |
| `storylines/kiana_consequences.py` | `75CAAD005CC28DAF4AE54690C9CEADAC997A4668C6CB5C5C98A8CA83903E2AC6` |
| `storylines/kiana_followthrough.py` | `C0EFDA58BBB848C758E46B1E17D175733C9E701EF89A486DE59C1B9D9077DC5C` |
| `src/Main.cs` | `8DECA7B215868CAA7BA48B8665885F9B3F8D82B178D3CD10B132E202F0EF1819` |
| `src/Story.cs` | `FDC3D586E51A99B501B47562500D82E597A6C6624CD26077E3D3BCBAE6058B19` |
| Parent's focused `tests/KianaEntryTests.cs` | `D63B1DBBD0ADDEC05AE1213772ECFE802E764C74CD1EC052A7137BE0B9185EDE` |

The initial Kiana base source was `B2203669D965FE57CAA4566BB023072F089AD6672DB2D73FDEAA563CFF9F64A7`.
The parent's prerequisite correction changes no prose or choice ordering.
Earlier bounded contribution scores do not approve this assembled campaign.

## Content and selected-path measurements

The project tokenizer gives the following inventory, excluding titles and metadata.

| Module | Scenes | Raw words | Distinct whole-segment words |
| --- | ---: | ---: | ---: |
| Base route and endings | 17 | 3,976 | 3,958 |
| Consequences | 4 | 6,368 | 6,316 |
| Follow-through | 6 | 8,326 | 8,320 |
| Combined | 27 | 18,670 | 18,588 |

The combined count removes repeated segments across modules as well as within them.
It is 2,412 words below the current 21,000-word planning floor even before semantic duplication and meaningful-content review.
No external native or RanRomance text is credited in these numbers.
Adding 2,412 words alone would not satisfy the structural requirements identified here.

I walked the actual authored nodes and eligible answers for three consistent native histories, excluding closure and deferral outcomes from completed paths.
The short chain omits optional stagecraft, Seelah and both extension batches.
The full chain includes stagecraft, Seelah, all four consequences events, all six follow-through events, farewell and one matching normal committed ending.
Both measurements count each visited page and only the answer selected there.
Equivalent flag states were merged while preserving minimum and maximum cumulative word counts.
These are controlled graph paths, not a Unity playthrough or the default rest scheduler.

| History | Short committed path, including ending | Full optional chain, including ending |
| --- | ---: | ---: |
| Waited, then separated | 1,338-1,515 | 11,213-11,862 |
| Kiss before disclosure, then separated | 1,411-1,589 | 11,354-12,004 |
| Widowed | 1,097-1,275 | 10,869-11,639 |

The full separated path contains 20 scenes including its ending; the widow path contains 19 because it does not need the married answer scene.
These longer paths are reachable through deliberate selection of available books before choosing farewell.
They are not the path the current automatic rest selection reliably delivers.
The aggregate 18,588 words must not be described as the amount a player reads on any single demonstrated route.
Conversely, this audit does not invent a separate 21,000-word requirement for every mutually exclusive path or a RanRomance selected-path measurement that has not been performed.

## Progression findings

### Corrected during audit: deferral unlocked an empty rehearsal

Originally, rehearsal required `kiana.started` instead of a completed reply.
Main.Update sets the relationship StartedFlag before opening the invitation, including when the player then selects its flag-free deferral.
The rehearsal's first page offers only moon and guest branches.
A deferred invitation leaves neither flag, so the prematurely available rehearsal opens with no eligible answer.

There was also no reliable 48-hour wait in this state.
Main.Update sets StartedFlag directly, without an hour timestamp, and RecordProgress skips already-positive flags.
The delay's missing-history fallback can therefore make the rehearsal immediately eligible.
An unfinished invitation remains earlier in automatic rest order, but the manual Read menu can select the broken rehearsal.
This reproduction needs only ordinary invitation deferral and the existing menu, not a forged save.
The generic scene test seeded `kiana.moon` for rehearsal and therefore could not expose it.

The parent reports reproducing the failure with KianaEntryTests, covering actual invitation replies and abort after the journal-started flag.
I inspected the test and independently verified the current source/export correction.
Rehearsal now requires `kiana.invitation`, which is written on genuine completion and receives its own timestamp.
The deferred state fails that prerequisite, while either completed reply has the corresponding first-page answer.
This finding is closed at source/graph scope; I did not execute the parent's C# suite or Unity.

### Unresolved: automatic farewell suppresses the longer route

`kiana.farewell` requires only the base `kiana.morning` milestone and the common completed soul quest.
Its delay is 48 hours.
`kiana.guest_table`, the first continuation, also becomes available 48 hours after morning.
Farewell precedes guest_table and every follow-through scene in the assembled export.
Main.Update selects `story.Scenes.FirstOrDefault` among available remote scenes when a rest event is pending.
There is no rule that treats Optional scenes as opt-in, and no prioritization of unfinished character arcs.

Other earlier scenes can postpone this moment, but do not make guest_table precede an eligible farewell.
When Kiana's farewell completes, all ten extension scenes forbid its scene ID and cease to be available.
The extension is therefore not merely optional content that some players choose to skip: ordinary delivery selects the closing event before its entry point.
Manual Read selection can preserve the long chain, which explains why direct chain tests and large aggregate counts do not reveal the defect.

The farewell is also not attached to an observed endgame departure or Threshold condition.
A delay after a private conversation can close the route's continuing social life early in chapter 5.
Correct the progression policy, not merely the volume total.
A full-route milestone or explicit final-departure choice should govern the farewell, with a compatible route for transformed Commanders and existing saves already past the old marker.
Do not silently remove an established farewell flag from saves or require an unavailable branch to unlock a finale.

### Unresolved: commitment and endings bypass the developed relationship

`kiana.morning/yes` is the only authored writer of `kiana.committed` in the entire assembly.
It occurs before either extension batch.
After choosing uncertainty there, the player can play every later social and writing scene, keep several concrete arrangements, and still has no later opportunity to make the postwar commitment.
The later committed/uncommitted callbacks correctly read existing history, but cannot resolve it.

The together and bereaved endings require commitment plus the appropriate separation/bereavement flag, without farewell, consequences or follow-through milestones.
An abbreviated early relationship can therefore receive the same broad fulfilled ending as the developed route.
The only unclosed, uncommitted ending remains unfinished, even after followthrough_kept.
Its eventual fading is possible fiction, but it ignores the newly played choice to maintain an ongoing relationship without promising a lifetime.
The assembly needs a later decision or a deliberate continuing, uncommitted outcome rather than treating all such histories as unfinished pursuit.

Main.RecordProgress also completes the relationship objective when commitment is set.
This occurs before the substantial campaign work under the current sequence.
A later-phase objective or revised journal progression should tell the player that more of Kiana's arc remains.

## Native history and continuity

The actual entry uses completed Seelah Q3, quest `5a5a533c9ce630a48b877f9a194840cb`, and `kiana.aftermath_seen`.
That seen-cue alias is the union of married aftermath `81109ea8fb20dbc478cf67116740f4a1` and widow aftermath `aebbc1845e827dd4da4e28014e7b4162`.
The export's `seelah.elan_dead` alias reads native Elan_Dead, `148423f1d35917946a5ebeeb4f19246c`.
This is genuine quest/dialogue history, not an invented native romance flag.

Native married Cue_0006, `a819e8c85ef23324bb0d8117bb9d7df3`, describes enjoying marriage while Elan is away crusading.
Cue_0007, `df45181e1968f26459f9e8bc2b995a34`, supplies frank adult humor about their interrupted wedding night.
The native couple embrace and express affection; the script does not establish a failed marriage, cruelty by Elan, nonmonogamous agreement or intended separation.
The widow root explicitly establishes bereavement, and Cue_0010, `e0abe01a6531ec6499f21e44cc81afe6`, asks Seelah for future friendship while requesting solitude for the present.
Those facts must remain distinct from the authored Commander romance and writing career.

The existing married route does preserve Elan as a good man whom Kiana still loves.
It distinguishes waiting from a chosen undisclosed kiss and lets her own the resulting hurt.
The spouse does not have to become a villain for an affair or separation to be authored.
However, the decisive move from an affectionate native marriage to separation is largely compressed into her reported conversation after one initial shared reading and an optional rehearsal.
Five days of delay do not provide the missing played development.
A fuller route needs particular experiences that reveal what she wants and what continuing the marriage would mean to her, plus a consequential aftermath of the decision.
This is a request to earn the alternate development, not to disqualify a married candidate.

The widow path provides a week after the earlier company milestone before its explicit romantic uncertainty, and another week before the date.
The later memories, old letter, stairwell anecdote and friends' awkwardness preserve Elan's place in her life.
They do not make romance a cure or ask her to stop missing him.
The new Meral visit does not assume a living Elan attended, approved the relationship, or waived his own discomfort.

The source does not bind ElanDesperate, despite the native aftermath holders using it to choose married versus widow contact.
The union seen-cue plus dead-flag split is adequate only while those native outcomes remain consistent.
The existing predicate research already flags conflicting death/desperate/restoration histories as needing dedicated reconciliation.
If Elan's state changes after an authored separation, the widow scene can still become eligible from company, potentially adding bereaved to separated.
Later extension history pages require exactly one consistent marital history and can then have no eligible answer.
If only the native death state changes, an existing separated or bereaved extension can likewise lose both history answers.
These are interrupted or modified-history hazards, not a claim that ordinary unmodified quest progression produces both outcomes.
They must be resolved before promising experimental fate changes or compatibility with state-altering play.

The appearance is consistent with the independently established oread unit `180b0eaa5dce387458d2ebf0ee943985`: blue skin, pale crystals and blue-green eyes.
The vampire princess is a performed role, not actual undeath or a physical result of soul theft.
The current prose does not claim every successful wedding history included Kiana's soul being stolen.

The previously corrected later-text joins remain sound.
The long-speech revision acknowledges a shared experiment instead of claiming the Commander opposed it.
The retained short-speech material is not falsely burned.
Farewell refers to a next draft, and together/bereaved endings progress from readings to staged productions.
The apart ending no longer denies earlier performance.
Those corrected sentences should be preserved while the structural ending rules are revised.

## What the longer scenes accomplish

The social chain gives Kiana friends who can wound her without becoming monsters, and lets her repair that friendship through an actual awkward visit.
The Commander's earlier intervention or silence changes Lenna's later complaint.
Public and quiet preferences lead to different supper activities.
Preparing the shawl and attending supper are one effective book, so an obsolete intermediate rest and late pin-selection abort are not counted as current defects.

The follow-through delivers an actual authored reading with separate public-room and small-workshop outcomes.
The long/short speech choice changes performance and revision, and Commander/Edris casting remains consistent.
The quiet desk versus shared room changes cost, copying, interruptions and the later week's report.
Kiana pays her own narrated expenses and remains a beginner rather than becoming famous through the Commander's approval.
The physical intimacy is voluntary, adult and non-graphic, with worthwhile quieter alternatives.

These are meaningful developments, not disposable filler.
They also occupy a narrow range of settings and concerns: meals, paper, borrowed rooms, rehearsals and negotiating enough time to enjoy company.
The next additions should pay off the existing practical and romantic choices under a new campaign pressure.
Another supper that mainly explains that joy and grief may coexist would repeat work already done.

## Gameplay, access and required next developments

All 21 non-ending scene definitions are remote-rest books in chapter 5 and Drezen.
They narrate physical meetings rather than a Jerribeth-style magical correspondence.
None has ContactUnit, a repeatable native answer-list attachment, or a native SkillCheck in the current export.
The relationship has empty UnavailableFlags and FailureFlags.
Historical aftermath contact does not independently prove that Kiana remains present and available for a later physical date.
This audit does not claim a universal native Kiana death flag exists; prior research explicitly did not establish one.
Safe new encounter staging and interruptions require their own implementation and verification.

The invitation is quest-linked, but finding venues, moving through Drezen, examining the chair, delivering a line and paying expenses are currently narration or deterministic choices.
The performance recovery is written, not rolled.
Actual original-style discovery and practical gameplay remain necessary.
The following additions have specific unfinished work to resolve rather than merely adding words.

1. Finish the core progression repair, then create a late relationship decision after the tested work arrangements.
   Let commitment, a continuing uncommitted relationship, or parting arise from what has actually been played.
   Reflect the chosen room, reading outcome, marital history and kept appointments in appropriate endings.
2. Fulfill the recorded morning-market or music wish with an actual outing and a discoverable opportunity in a verified location.
   Give Kiana a goal beyond explaining the relationship or repairing another social misunderstanding.
   Preserve the option to attend alone or with friends rather than making every wish wait for the Commander.
3. Develop the separation or bereavement history under a concrete later obligation.
   For separation, settle a real shared arrangement or encounter an independent decision by Elan without forcing forgiveness or villainy.
   For bereavement, let an inherited responsibility, chosen remembrance or future plan conflict with the new relationship in a way she resolves through action.
   Bind only native facts the game actually establishes; new letters or meetings must be labeled authored developments and staged safely.
4. Make preparation for a later reading or production involve a playable practical obstacle.
   A verified Perception or Knowledge World check can change setup or script continuity, with a written failure recovery and a non-roll alternative.
   A performance approach needs an appropriate native mechanic rather than an invented Performance stat or a roll that purchases attraction.
   Preserve the long-speech literary consequence even if delivery succeeds.
5. Implement an attainable Trickster access/restoration path tied to her quest history and voluntary decisions.
   Resolve which non-Trickster paths can pursue or continue the relationship.
   The original transformed-date accommodation followed by an inhuman ban on all ten longer scenes is not a completed mythic policy or equal-depth route.

Existing Seelah participation is optional and has native dead/gone exclusions.
Arsinoe's proposed introduction remains a wish, not verified joint-scene presence.
The Kiana/Aranka rehearsal draft outside the export does not count as delivered guest or two-woman content.
Any future mutual-attraction route must develop the women's relationship independently and reconcile actual contact/history, rather than importing that draft's mere existence as proof.

No reviewed scene closes another romance or demands Commander exclusivity.
Kiana's marriage-related choices are her own authored relationship developments, not ToyBox jealousy cleanup.
This source property does not certify actual ToyBox execution, saves or final mod compatibility.
Current art assets and earlier crop reviews are not a full scene-art or runtime likeness audit here.
Full independent writing/canon/art/technical approval, meaningful volume, game verification and the remaining campaign work are still required.

## Verification limits

I performed read-only assembly comparisons, tokenizer measurements, actual choice-graph traversal, current flag-writer/skill-check inventories and focused prerequisite reproduction.
I inspected native extracted dialogue, predicate research, appearance adjudication and the earlier independent contribution reviews.
I read the parent's new first-invitation test but did not run the C# suites.
No source, export, tests, plan, installation or artwork was edited.
The current audit leaves the automatic farewell issue and the full-route requirements open while recognizing the corrected first-invitation defect.
