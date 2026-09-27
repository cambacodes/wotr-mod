# Seelah aftermath contribution

The new module provides four connected Chapter 5 scenes for independent review and integration.
It is a contribution to the unfinished campaign, not a full-route completion claim.
I authored this material and assign it no quality score.
The root worker owns integration, shared rules, export, existing scenes, and all production changes beyond this new module.
No Story.json was generated and no existing source was edited.

## Source snapshot

New storylines/seelah_aftermath.py SHA256 is 2777ADBD4D2300D3535DCF876C13CAF85B0726CF77BAD0B20D4A80D9DFA10BD3.
Read reference/story-review/seelah-full-arc-gap-audit.md and the retained native Seelah text and outcome evidence.
The existing input hashes were:

- storylines/seelah.py: CD550DE0692956A984DA36360B780A85D33BF9C9C0BBB82827668C7758F1CAAF.
- storylines/seelah_later.py: A8D257D7E675B938EAC487025F465A93FDCB135610CA4ADFDC091B31CE19D625.
- storylines/seelah_abyss.py: 47CFAD1DBA6621CC99FCD6F4243B75BBC5F0BC3728C51289929BCE9674A881F3.

The module has 59 nodes and approximately 5,218 raw dialogue and choice words under a simple word-token count.
That includes alternative nodes and markup tokens and is not a meaningful-playthrough length certification.
This contribution does not bring Seelah to the requested independently verified 21,000 meaningful-word full-campaign standard.

## Progression and integration

All four scenes use the existing seelah relationship and native answer list 417fa384f3250634bb71859fbc913453.
They are ordinary dialogue entries restricted to Drezen area 2570015799edf594daf2f076f2f975d8 and Chapter 5.
They do not create remote actors or assume native quest NPCs are present.
Each requires seelah.courting and seelah.weight and forbids inhuman, seelah.farewell, seelah_dead, and seelah_gone.
The relationship's existing closure rule also applies after integration.
Each is optional and uses a minimum 24-hour delay.

| Scene | Additional prerequisite | Played consequence |
| --- | --- | --- |
| seelah.borrowed_saw | None | Earlier learning lets Seelah listen before judging; a fallback without that history makes and corrects the accusation. Both help build a temporary crossing and choose a gift or affordable loan for a damaged tool. |
| seelah.platform_finished | seelah.saw_arranged | The repair is finished, the recipient exercises agency, and Seelah reflects differently on the gift and loan before inviting prayer or a later meeting. |
| seelah.inheritors_corner | seelah.platform_kept | Shared or private prayer leads to actual quest-outcome concerns and a planned evening. |
| seelah.roof_evening | seelah.faith_spoken | The invitation is kept, earlier home/road/uncertain preferences return, and the couple acknowledges what those concerns mean for their future. |

Completion flags are saw_arranged, platform_kept, faith_spoken, and aftermath_ready, all prefixed seelah.
The gift and loan flags saw_gift and saw_loan are mutually exclusive on an ordinary playthrough.
prayer_company and prayer_private determine how the faith scene begins, without grading the Commander's belief.
aftermath_grief, aftermath_questions, aftermath_hope, and aftermath_unfinished record the outcome discussion actually heard.
These history flags must not override later native quest changes or select native endings by themselves.
roof_kissed and roof_quiet distinguish physical choices, and aftermath_otherpartners records the optional practical discussion of other relationships.
None of these flags changes the native romance, quest, alignment, resource, or companion state.

Recommended integration is before the existing seelah.road future choice for new Chapter 5 progression, with aftermath_ready as the new prerequisite if the root chooses to make this reckoning required.
The module alone does not alter road, so the original bypass remains until integration explicitly addresses it.
Existing saves that already completed road but have not reached farewell can still play this module: its final promised node acknowledges existing commitment instead of pretending to make the first promise again.
The final consider node prepares an uncommitted player for the road conversation.
Late saves after farewell intentionally do not receive a scene pretending another preparatory evening remains available.
No new ending variant is supplied and no existing ending is silently rewritten.

## Native evidence and authored limits

The native sources retain Seelah's warm, impulsive generosity, street experience, awkward relationship to being treated as a holy exemplar, and faith in Iomedae.
reference/canon-review/seelah.txt includes her discomfort with younger warriors revering her, her desire to recover Elan's trust, and her actual recitation of the paladin oath in the Abyss.
The new prayer is personal authored wording, not a purported canonical liturgy or divine reply.
No celibacy requirement, revelation, divine approval of the romance, or abandonment of Iomedae is introduced.
The Commander may share faith, express uncertainty, ask respectfully, or meet after Seelah prays alone.

| Existing alias | Type and GUID | Source and meaning used |
| --- | --- | --- |
| seelah.souls_returned | Completed BlueprintQuest 5a5a533c9ce630a48b877f9a194840cb | World/Quests/Companions/Seelah/Q3_WeightOfMySword/WeightOfMySword_SeelahQ3_quest.jbp. Uses the existing CompletedQuests binding, not Playing. |
| seelah.elan_dead | Playing BlueprintEtude 148423f1d35917946a5ebeeb4f19246c | World/Etudes/Common/WrathOfTheRighteous/ImportantNPCs_fate/Seelah_Friends/Elan_Dead.jbp. Dead memory versus his ability to answer for himself, only after the completed-quest branch. |
| seelah.ending_bad | Playing BlueprintEtude e438007efc4f1474eb447031d4b5a60e | World/Etudes/Common/WrathOfTheRighteous/Companions/SeelahCompanion/SeelahInParty/Seelah_BadEnding.jbp. Takes precedence over moderate when both are present. |
| seelah.ending_moderate | Playing BlueprintEtude 2bb1f6f30ca9bb1408f720d6f10c5c05 | World/Etudes/Common/WrathOfTheRighteous/Companions/SeelahCompanion/SeelahInParty/Seelah_ModerateEnding.jbp. Questions and independent travel, only if bad is absent. |

All these bindings already exist in expansion.py; no new binding is requested.
The incomplete branch does not assume the wedding happened, that the rescue remains available, or that a particular failure occurred.
The complete branches do not claim that every stolen soul or every friend was saved.
Kiana, Jannah, Curl, Arsinoe, and Elan are not spawned or given new current conversations.
Elan's dead branch avoids assigning him a convenient posthumous opinion; the other branch proposes a future conversation without claiming it has happened.
Kiana's marital or survival state is not asserted by this module.
A later actual friend encounter still needs its own verified presence and outcome gates.

Mera, Orsa, the smith, washer's customer, alcove, washing platform, and terrace are authored additions.
Mera and Orsa are explicitly adults and have no romantic role.
Money, damage, repayment, and repair are narrated circumstances in a small civilian incident, not an inventory transaction or native construction quest.
The gift and loan have distinct consequences rather than treating the recipient's gratitude as proof that Seelah is right.
The roof scene offers voluntary graphic and explicit affection or quiet company and preserves other partners without jealousy tests.
This humanoid-only contribution adds no Trickster resurrection or departure repair; existing fate work remains separately required and must be reviewed independently.

## Checks performed

Imported the module successfully using existing story_format helpers.
Checked unique node IDs and all local choice targets.
Exhaustively traversed every eligible non-abort choice through all four scenes over 3,072 combinations of earlier judgment terms, early activity preference, Q3 completion, bad/moderate markers, Elan death, existing commitment, and all combinations of check_signal, check_person, and knows_need.
The graph check followed 811,392 non-abort choice transitions and every completed chain reached aftermath_ready.
It included simultaneous bad and moderate flags, incomplete Q3 with those markers present, and absence of any early activity preference.
These are source-graph checks, not the root's rule engine or in-game verification.

Root integration checks should cover scene availability on native companion contact, closure/death/kickout/inhuman/farewell blocking, real timing and quest-state changes between scenes, export inclusion, and an old save already committed at road.
The existing judgment-term flags are expected to be produced by weight; a corrupted or manually fabricated weight completion without any term flag is not a supported source-graph history.
The new scene should not leave the root's real validator with an unhandled visible node if that validator deliberately tests such malformed histories.

A compact reproducible structural check, run from the repository root, is:

```python
from storylines.seelah_aftermath import SCENES
for scene in SCENES:
    nodes = {node['Id']: node for node in scene['Nodes']}
    assert len(nodes) == len(scene['Nodes'])
    for node in nodes.values():
        for choice in node['Choices']:
            assert not choice['Next'] or choice['Next'] in nodes
```

## Remaining review and campaign work

Independent reviewers must assess the new voice, pacing, native outcome interpretations, scene joins, and whether the incident repeats the Abyss lesson too closely.
The saw incident deliberately makes Seelah's own premature judgment the mistake and follows the practical and financial consequences, but the broader campaign must not consist only of learning to ask before helping.
The existing optional souls scene and this reckoning should be ordered deliberately so they do not repeat the same initial observation without development.
The older road commitment and epilogues still need integration with what is now said before them.
A full Jannah decision aftermath, native friend encounter, broader mythic reactivity, longer sustained middle campaign, finished art, and actual game/save verification remain outstanding.
The user's minimum meaningful campaign depth and independent greater-than-90 review targets apply to Seelah separately from other characters.
This handoff provides no self-awarded score, release approval, or assurance that those targets are already met.


## Independent-editor revision

The root returned these two files for revision after independent review identified a repeated apology, inconsistent prayer timing, and failure to recognize earlier learning.
All three have been revised in the current source hash above.

The saw-yard introduction now branches before Seelah makes an accusation.
check_signal takes precedence and permits the exact previously agreed two taps on her wrist.
Without that flag, check_person makes the pair observe both women before intervening.
Without either Abyss flag, knows_need makes Seelah ask Orsa what help she wants and wait for Mera's account.
Those three branches set the new seelah.saw_listened flag and enter listened, then the existing broken-saw and practical work sequence.
They do not contain the accusation or require an apology for an accusation never made.
The later walk goes to practice and thanks, where she recognizes the difficult success of waiting and thanks Mera for her instruction.

Only a history without any of those three growth flags receives hasty_start and the existing premature accusation.
The agreement node now acknowledges missing information without already delivering an apology.
The later hasty node says she has not yet admitted being unfair, and the single apology is delivered explicitly in apology.
This resolves the duplicate-apology problem on both incoming hasty branches.
The normal morning completion sets knows_need, so ordinary current progression necessarily receives a learned approach even if the optional Abyss scenes were skipped.
The hasty route remains for earlier or incomplete development histories lacking those recorded flags.

Gift and loan decisions and their follow-through are retained after every approach.
platform_finished.outside now proposes quiet time tomorrow rather than suggesting prayer before the current walk home and then scheduling tomorrow in both choices.
The shared/private prayer options still lead to their respective next-day openings.

The revised source graph was traversed again across all 3,072 combinations, including mixed growth flags.
Every eligible yard history has exactly one approach choice.
The check asserts that learned histories never enter hasty_start, hasty, or apology, and that practice and thanks require recorded learning.
All completed chains still reach aftermath_ready.
The total checked transitions are 811,392.
This is verification of the revised source graph only; the independent editor must still rereview the prose and integration.

Both owned files are frozen at this handoff and their ownership is released back to the root worker.
The new source SHA256 is 2777ADBD4D2300D3535DCF876C13CAF85B0726CF77BAD0B20D4A80D9DFA10BD3.
No shared file or Jerribeth source was edited during this revision.
