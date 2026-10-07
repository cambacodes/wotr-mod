# Tirabade scar and Queen revision review

Date: 2026-09-26.
Verdict: scoped pass for the seven new nodes and four appended entry choices, after two author corrections.
This review does not approve the complete Tirabade route, its art, or an in-game release.
The reviewer authored the separate opening and late pacing revisions, but did not author these scar and Queen branches.
Those other revisions are excluded from this verdict.

## Reviewed material

| File or artifact | SHA256 |
| --- | --- |
| storylines/tirabade_chronology.py | 340148AF8DE96167A300E8888CC4A30FD98DA11F036D4B19A57F078065909891 |
| expansion.py | 3156B082C1077D170D31293F29221197C5F44E8B1BDAA917B25C055E66E27972 |
| tests/TirabadeChronologyTests.cs | BC62DC18DA9056D2053550BA99AE3223AA8C4E1805F36FC9DF085B977FFD47DE |
| reference/canon-dialogue.txt | E10DD05FA5D08FF7AFD3DB4700433EDD65160F46D6FDC69DA3BCD4131ED2AE2B |
| Root isolated candidate Story.json | AA5EBA954381257410A69CB51A37A6E5FBAE7D4269AD63368B01142A44E52C44 |
| Committed morale candidate Story.json | 1DD0CDE6C952ADAAF50CD676C33848014AFD36B5E54E4EECE7693E86780A988F |

Read the actual source diff, surrounding return and power scenes, final-watch joins, native excerpts, and reference/canon-review/tirabade-shared-history-branch-audit.md.
The reviewed additions are return/scar, scar_quiet, scar_disputed, queen, queen_letters and last_watch/scar_unsettled, queen_letters.
The root candidate excludes the separately authored, unreviewed late pacing edits.

## Character and history findings

Irabeth's first response to the scar repeats her native desire not to discuss it.
The Commander can respect that request, offer a limited acknowledgement, or defend the original act as necessary.
The defensive answer does not force repentance, consent to a new moral judgment, or a claim that violence was beneficial.
Irabeth retains her own judgment while refusing to spend the evening defending it to either her wife or the Commander.
Anevia remains angry and leaves with Irabeth.
This is credible marital solidarity with disagreement inside the marriage, rather than two interchangeable speakers delivering a relationship lesson.

Native Irabeth Cue_0071, GUID c7a7717c516039d498a7525baf6abe04, justifies the Commander's intervention and asks that the subject not be raised again.
Native Anevia Cue_0044, GUID 0986b5a3bc4f7ae4aa858dcb4aa8e9e6, already reports her wife's justification while expressing her own anger.
Cue_0045, GUID 8e808b69a43ed4f43b8eb39d27990a4a, explains Irabeth's refusal to remove the scar.
Consequently, Anevia's new disagreement does not require her to have overheard a private Commander conversation.

I flagged the earlier wording that implied the Commander had directly heard Irabeth's answer before.
The scar history alias can come from Anevia alone.
The author replaced that line with a refusal to defend her answer to either person, removing the unsupported direct-conversation claim.
The current version passes both native witness histories.
The entry deliberately recalls an observed scar discussion; it does not claim to cover every save in which the injury occurred but nobody subsequently discussed it.

The quiet and disputed endings both leave the matter unresolved.
The disputed answer additionally records tirabade.scar_defended.
That extra flag currently has no distinct final-watch response, which is acceptable because the common callback acknowledges remaining disagreement without attributing an apology or a particular argument to the Commander.
The final watch preserves Anevia's anger and Irabeth's wish to stop discussing it that night.
Wanting everyone to survive is not presented as forgiveness.

The Queen entry requires the actual observed Irabeth report, d47bcd8d88f8ea149a596ca927e1153f, rather than chapter number, Broken, or a generic Queen death flag.
Its opening explicitly recalls what Irabeth said about Iz.
Her statement that the Queen did not return belongs to that remembered event and does not assert the Queen's permanent current state across later supernatural developments.
Her refusal to be relied upon follows native Cue_0197.
The three unfinished letters, their unnamed recipients, the shared writing evening, and their later dispatch are authored developments, not claimed native facts.
No named relationship, completed native errand, or existing letter history is invented.

The letters provide a small action within grief rather than curing it.
Irabeth chooses the words, does not read the difficult sentence aloud, and offers no assurance about future deaths.
The Commander can leave that activity for another time and use the existing future branch.
The later dispatch is recalled only after the player chose to remain during the writing scene.
The author also changed the final-watch reference from an assumed battle tomorrow to the next battle, removing an unsupported calendar claim.

The scar exits and letter-writing exit complete return without traversing its warmer future conversation.
The next power scene already permits Irabeth to reject the Commander's choices and demands that disagreement be heard.
It does not assume the prior dispute was settled.
The new final-watch callbacks return through the existing Broken-sensitive life alternatives.
They neither clear Broken nor manufacture Encouraged.

## Scoped assessment

These are editorial judgments of the reviewed additions, not measured probabilities or guarantees of player approval.

| Discipline | Score | Reason |
| --- | --- | --- |
| Native history fidelity | 95/100 | Uses observed conversations and preserves the distinction between native history and new letters. |
| Character voice and marriage | 93/100 | Anevia's anger differs from Irabeth's defensive restraint; their marriage remains an active relationship. |
| Mature conflict and player agency | 94/100 | The Commander may defend the harm, and the women may remain dissatisfied without mandatory rehabilitation. |
| Pacing and prose | 92/100 | The disputed evening ends when it should, while the letter scene uses a concrete task instead of a long explanation. |
| Choice joins and earned continuity | 95/100 | Entry memories and later shared memories are separately gated, with stable old choices and morale joins. |

These scenes appropriately add no erotic intensity to the injury or grief discussion.
Their mature content lies in responsibility, disagreement, grief, and an intimate relationship that does not erase any of them.
A sexual-intensity target would be misplaced for this particular branch.
Some familiar staging remains, including cups, a lamp, hands, and a quiet departure.
That is a minor style limitation here, not a reason to lengthen the scenes or add another explanatory exchange.

## Independent verification

Temporary evidence directory: C:/Users/Z/AppData/Local/Temp/tirabade-history-independent-bksz7b99.

Compared root candidate C:/Users/Z/AppData/Local/Temp/tirabade-native-history-dwxtqxfy/Story.json with committed morale candidate C:/Users/Z/AppData/Local/Temp/tirabade-morale-fixed-g9omrnz0/Story.json.
All 585 scene positions and their pre-existing fields match.
Every pre-existing node position, ID, text, speaker, portrait, and other non-choice field matches.
All 5,709 existing choices match exactly at their existing indices, including Next, Set, Check, Abort, labels, and gates.
Only the seven new nodes and four appended entry choices differ.
In particular, the existing final-watch Broken alternative retains its index.
The structural results are recorded in structural-result.json.

Independently assembled current source with independent_tirabade both true and false.
Both modes register the exact scar and Queen seen-cue arrays.
The false mode still contains no Irabeth solo relationship scenes.
Inspection confirms irabeth_independent.integrate only registers seen-cue and chapter-etude metadata, so moving that call does not accidentally install the solo route.
The existing Main snapshot reader treats the scar array as alternative observed witnesses.

Compiled actual src/Story.cs in an isolated net8 project and ran 1,102 assertions successfully.
The checks call Rules.Validate for both assembly modes and Rules.Match over all 64 combinations of the two native history aliases, two authored callback memories, Broken, and Encouraged.
They verify scar and Queen entry eligibility, separately earned final-watch callbacks, exactly one correct morale continuation, absence of native history or morale writes in these scenes, and the disputed-choice flag.
The harness is Review.csproj with Program.cs beside it.
Run from that directory with C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe run --project Review.csproj.
An initial Python fixture check incorrectly indexed an optional Relationship field; changing the probe to use the JSON default corrected that probe error without changing production files.

Read the new root tests that traverse return, power, future, and last_watch across eight history/Broken combinations.
They verify preserved foreign romance flags and earned callback reachability.
The reported full-suite result of 25,961,852 assertions belongs to the root's run and was not independently rerun here.
This review's independently executed result is the bounded 1,102-assertion harness plus exact JSON comparison and both assembly checks.
No Unity scene, save load, native dialogue display, portrait, or voiced delivery was executed.
No production source, shared export, installed asset, native state, or other author's files were edited by this review.
