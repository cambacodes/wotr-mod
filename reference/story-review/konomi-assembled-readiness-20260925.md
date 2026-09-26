# Konomi assembled narrative readiness, 2026-09-25

## Verdict

The aggregate planning floor passes, but full narrative readiness does not.
Konomi now has a substantial playable romance with an authored post-dismissal continuation, rather than the short outline assessed in the earlier audit.
The assembled route still needs work at the transitions between those narratives and in the ordinary Chapter 5 campaign.
The dismissed courtship has earned a provisional complete local arc from invitation through renewed plans and departure.
That does not make every ordinary, interrupted, new, or established relationship history complete.
I am not assigning an overall numerical quality score to the unfinished assembled campaign or averaging prior scene scores.

This is an independent literary and narrative-structure audit.
I read the four source modules and compared their scene objects with the actual development export.
All 40 Konomi scene objects match exactly, including text, choices, and conditions.
The export contains 142 scenes across all relationships.
Runtime presentation, native progression, artwork, and the parent's rule assertions are not independently certified by this review.

## Source fingerprints

| Artifact | SHA256 |
| --- | --- |
| storylines/konomi.py | `702855D59922B48B0C88145AE7034A4EA417CC53FBEA82F984C0BA3AE928B235` |
| storylines/konomi_private.py | `E4A570ED6CB6CD5BF4287D04D49E393945915671341C1D4A720E34D94D127EE4` |
| storylines/konomi_distance.py | `BA7AB0AD64D3ECA8053E2DC82DE3B81424C0F2A24850E413420ED334A9E8A403` |
| storylines/konomi_future.py | `7877AD77F2711421A30BA2449955648A503BBB633EADC2740F4ADAC8F893F57E` |
| development/Story.json | `A8FC9B76D8C9DBE6268E74DC067F0F6AB502430E85D25BAF6A674628D8A16C95` |

## Independently checked inventory

Using the project's existing tokenizer and normalized whole-segment deduplication, I reproduce 22,051 raw words and 21,893 distinct-segment words.
The raw total contains 18,941 prose words and 3,110 choice-label words.
Only 158 words are removed by exact-segment deduplication.
That small difference does not measure semantic repetition or the words a player actually experiences.
Titles, entry labels, journal metadata, and existing game or external RanRomance material are excluded.

| Narrative group | Scenes | Aggregate prose and choice words | Sum of largest single paths through each scene |
| --- | ---: | ---: | ---: |
| Ordinary presence route, including its optional Abyss letter and breakup | 16 | 9,536 | 6,058 |
| Dismissed private route, from impossible post through final departure | 12 | 11,652 | 8,098 |
| Ending variants | 12 | 863 | Not additive in a playthrough |
| Total | 40 | 22,051 | Not an attainable campaign total |

There are 28 campaign scenes and 12 ending objects, not 40 successive meetings.
The ordinary group contains eleven main progression scenes and five optional scenes: unsent, parting, hearing, hearing_after, and new_letter.
All twelve dismissed campaign scenes are marked optional, although their authored prerequisites form a progression.

For the final column, I followed each scene's directed choices from start and retained the largest non-abort path, counting its prose and selected labels.
I deliberately ignored flag compatibility, history consistency, scene ordering, and mutually exclusive outcomes to obtain generous upper bounds.
These are not engine-tested attainable counts.
Even adding every campaign scene's independent maximum and the longest single ending gives only 14,262 words.
That already overgenerous figure includes combinations such as breakup and later relationship continuation that cannot form an actual successful campaign.
It also combines ordinary and dismissed content without subtracting scenes lost to dismissal.
No claim that a player receives 21,893 words in one campaign is supportable.
The 21,000 requirement was a planning-inventory floor, so this observation is not a new per-playthrough word requirement.
It explains why passing that floor cannot establish full content depth.

## What is now meaningfully complete

The hearing addresses several concrete failures identified in the earlier reference/canon-review/konomi-full-arc-gap-audit.md.
The player now attends the complaint, chooses between evidentiary strength and privacy, can withdraw permission before reading, and lives with the association's different findings.
The denied-letter history receives an actual public acknowledgment and later trust response.
The new-letter outing replaces some former summarized courtship with a played invitation and shared activity.
These are substantive improvements, not additional versions of reassurance.

The dismissed route gives the loss of office a personal and professional aftermath.
Fate changes the possibility of delivering an invitation, while Konomi decides whether to meet.
She chooses paid independent work, resolves a carriers' dispute, leaves for Nerosyan, sends readable letters, returns temporarily for a lease, and makes a further career choice before departing again.
The work and addresses connect those stages coherently.
The final lease choice lets her want influence even when it costs trust or money.
Her answer is not that romance has taught her to stop wanting power.
The career consequence appears at supper before either intimate or quiet companionship.

New and established lovers have different initial meeting and pre-departure responses.
The final refusal now distinguishes rejecting a new courtship from ending an existing relationship.
An existing commitment can be renewed rather than rediscovered as a first promise.
The quieter route reaches breakfast after an explicit parting for the night, and its ending no longer invents an unselected kiss.
Neither professional choice blocks affection, and acknowledging other partners changes scheduling rather than demanding exclusivity.

## Priority 1: carry unfinished relationships across dismissal

Every ordinary disagreement, leak, reckoning, hearing, and hearing_after follow-up requires konomi.present.
The dismissed route requires the opposite presence state and does not inherit their unfinished stakes.
Consequently, dismissal after disagreement can strand the grain petition.
Dismissal after leak can strand the response to the stolen letter and the request to deny it.
Dismissal after reckoning can strand the promised hearing or the trust repair that the hearing was meant to test.
The later private scenes offer another relationship but never establish what became of these particular obligations.
This is a material assembled-narrative gap even if all individual scenes run correctly.

Add a short state-aware reckoning after the courtyard meeting, before the first departure.
If the petition is pending, let Konomi identify who now handles it and what she can still do privately.
If the letter complaint is pending, let her decide whether to pursue the association hearing through private correspondence, withdraw it for a stated reason, or arrange a later hearing without restoring her office.
If the Commander proposed denial and has not repaired it, the reunion needs that specific hurt rather than only an apology about dismissal.
If the hearing already happened, carry its privacy or evidence disagreement into one later private exchange instead of replaying the complaint.
Author only the unresolved histories and their consequences, not copies of every former scene.

The binary lovers versus not-lovers split also leaves a middle history under-described.
A player may have attended the reception, exchanged personal letters, and accepted an evening before konomi.lovers is set.
The later new-acquaintance responses do not explicitly contradict every such history, but they under-recognize what has already been offered.
Add one recognition variant for an interrupted courtship using reception, terms, or attraction history.
It should neither invent an established relationship nor introduce two people who have already invited one another privately.

## Priority 2: give the ordinary Chapter 5 route its own developed culmination

The ordinary route still moves from return through power, ordinary, and farewell in four short scenes.
Their independent maximum paths total only 854 words, before an ending.
Return.talk summarizes the entire Abyss disclosure.
Power.commit summarizes future plans and an amusing disagreement without specifying either.
Ordinary.honesty summarizes another disputed account.
The private career sequence cannot repair this route because it requires dismissal.

Expand return into a specific exchange about something Konomi did during the Commander's absence, then let the player offer an equally concrete disclosure.
Give the political history a real role in that conversation.
The earlier canon audit cites the national crisis in Diplomacy_Officer/Cue_0032, foreign garrisons in Cue_0029, and the alternative internally resolved crisis in Cue_0042.
Its Diplomacy_8/Cue_0081 also identifies an outcome where the Diplomatic Council has served its purpose.
These alternatives should change her immediate work and desired future rather than be collapsed into generic administrative fatigue.
The native sources are documented with blueprint identifiers in reference/canon-review/konomi-full-arc-gap-audit.md.

Follow with a played professional choice that the Commander cannot solve merely by complimenting her or apologizing for tone.
The private lease offer is the useful structural precedent, not text to duplicate.
For ordinary Konomi, the issue should involve the access, loyalty, or obligations she actually retains in that native history.
Then make the chosen future concrete through a later shared task or visit that encounters its cost.
Rewrite the present summarized plans around that event.
The final letter can remain concise once it closes an experienced development.

## Priority 3: account for Act 4 and the loss of Trickster power

The only authored Chapter 4 scene is unsent, which requires the original ordinary evening.
A new dismissed courtship cannot receive it even after letters and affection become important.
The twelve dismissed scenes allow Chapters 3 and 5 only.
A Chapter 4 interruption therefore supplies no authored personal bridge for that history.
Add an appropriate unsent private letter or remembered intended reply that uses the Nerosyan correspondence, without pretending ordinary delivery from the Abyss is safe or available.
Its Chapter 5 payoff should respond to the actual topic selected, not merely thank the Commander for keeping a letter.

The source requires active Trickster only for fate_post.
All later steps use the established contact flags instead, so their narrative does not demand a second magical delivery after a switch to Legend.
That is a sensible structure for Trickster followed by Legend.
The game-state mappings and timing still require the parent's integration evidence.
A player who has already left Trickster before sending the first post is not covered by this route's current entry condition.
Do not advertise that history as reachable through these scenes without a separately justified access design.

Once contact exists, add a brief, substantive acknowledgment of choosing Legend if that transition occurs during the courtship.
Konomi has already expressed concern about the power to alter unwilling people.
Her response should consider the Commander's decision and the changed future, not congratulate a presumed moral improvement.
A normal invitation that survives the loss of the original magic is a good payoff, but the present route leaves that interpretation entirely to the player.

## Priority 4: preserve costs beyond the next conversation

The public scandal reports a loss of access to a noble household's courier and dinner network.
The hearing argues about that history, but never settles what access Konomi can recover or replace.
A later independent introduction could show a correspondent accepting or refusing her after the scandal.
Do not confuse the association's ruling with restoration of unrelated patronage.

The lease choice has immediate costs, but its endings converge into generic clients and influence.
Add a modest consequence later: the former tenant refuses a useful introduction, or the delayed start changes which contact Konomi can approach.
The cost should matter without proving one choice universally correct.
The ending then needs only a short corresponding acknowledgment.

The provision dispute still resolves through better information and outside aid that largely vindicate every approach.
Keep that particular resolution if desired, but do not count it as a sustained disagreement in which one partner loses something she still values.
The hearing and lease do better at this, provided their consequences survive the move between routes.

## Prose and relationship depth across the whole route

Konomi's sharpest voice appears when she enjoys finding the leak channel, challenges the buyer's excuse, plans a breakfast between rival contacts, or admits wanting influence.
These moments align with the native political hunt and layered strategy described in Diplomacy_Officer/Cue_0040 and Cue_0016.
Much of the remaining connective prose repeats a narrower pattern: papers put aside, an almost-formal answer abandoned, a small embarrassment exposed, and reassurance that disagreement can coexist with affection.
The exact-word deduplication does not detect this repetition.

Keep several of those habits, but cut explanations once the action has already shown them.
Vary later interaction through an actual third person's competing aim, a decision she makes without waiting for approval, and a shared activity whose result remains present next time.
The gardening, pear, and unfinished-tune motifs provide personal texture.
They should accumulate changing meaning rather than repeatedly demonstrate that an organized politician can be charmingly unguarded.
The tune continuation is stronger than another furniture accident because it brings her independent life into the room.

The private reunion's good_evening still summarizes its amusing story rather than supplying the story's crucial line.
Several breakup scenes similarly summarize the explanation and response.
Prioritize replacing those summaries where a choice would reveal the Commander or Konomi, rather than expanding every transition.
Explicit sexual detail is not the missing ingredient.
The route needs more particular shared experience and fewer descriptions assuring the reader that meaningful conversation occurred.

## Approval boundary and next review

The export and aggregate inventory are verified for the fingerprints above.
The dismissed campaign has an intelligible local beginning, middle, and ending, and its individual revised scenes retain their bounded assessments.
The whole route remains unapproved because ordinary Chapter 5 development and dismissal carryover are materially incomplete.
The next assembled review should follow three concrete histories: ordinary through Chapter 5, an interrupted early courtship dismissed before resolution, and established lovers dismissed after the scandal with a later Legend transition.
A new dismissed courtship crossing Act 4 should also receive its own authored bridge and review.
Record the actual scenes and choices experienced in those histories instead of using aggregate word totals as their proxy.
No further volume should be added merely to exceed the already-passed inventory floor.

## Follow-up inspection of the early invitation refusal

The parent added ending_dismissed_apart while this audit was being written.
The revised konomi.py SHA256 is `4BC95F60FB700FF30CCFEAEE5D6AA155D9A7D3C04691365B0D58A555EA311F92`.
The revised development/Story.json SHA256 is `9E7A287C64F0BB5727158F98A908F1EF0B047A8F5A879CEC2408662A6B868A56`.
I inspected the added ending and verified all current konomi.py scene objects against that export.
The new ending acknowledges declining a private invitation and Konomi continuing toward Nerosyan when her work permits.
It does not restore official correspondence or imply that she is still waiting for romance.
This is an appropriate correction for the early refusal history.

The final export now contains 143 scenes overall and 41 Konomi objects.
Konomi's classification is unchanged at 28 campaign scenes, with the ending count increased to 13.
The new aggregate inventory is 22,124 raw words, comprising 19,013 prose words and 3,111 choice words.
The normalized distinct-segment total is 21,965, with 159 exact-repeat words removed.
The ordinary and dismissed campaign counts and their generous single-path upper bounds remain unchanged.
The additional ending contributes 73 raw words, bringing the ending aggregate to 936.
It does not increase the longest ending or the generous combined campaign upper bound of 14,262 words.

This correction closes the identified early-refusal ending gap only.
Shipment and letter carryover after dismissal, the new-courtship Act 4 gap, and the ordinary Chapter 5 development remain open.
The aggregate planning floor still passes, and full narrative readiness still does not.
