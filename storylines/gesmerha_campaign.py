"""Gesmerha's living campaign continuation, with a bounded native C5 reunion.

The songs, apprentices and relationship are authored developments.
The capital visit is restricted to the actual guest etude, actor and answer list.
No revival, permanent guest, sight restoration or native outcome is written.
"""
from story_format import c, n, p, reaction, scene
from storylines.gesmerha_opening import UNIT, AREA, ANSWER_LIST

CAPITAL = "2570015799edf594daf2f076f2f975d8"
GUEST_ANSWERS = "fb3a88e8ed751214c9136f87891ec07b"
ETUDES = {"gesmerha.capital_guest": "89d57f73e41040f0ab527d6e83478a64"}
SEEN_CUES = {
    "gesmerha.heard_future": ["164cf168d833c3f4ba458f72df62bda0", "64388ef1f915e8c4991848f511408fa9"],
    "gesmerha.heard_migration": ["164cf168d833c3f4ba458f72df62bda0"],
    "gesmerha.heard_staying": ["64388ef1f915e8c4991848f511408fa9"],
}
SCENES = []


def s(id, title, entry, nodes, previous, chapter=3, delay=24):
    for page in nodes:
        page["Portrait"] = "Gesmerha"
    late = chapter == 5
    SCENES.append(scene("gesmerha." + id, title, "Gesmerha", chapter, entry, nodes,
        Relationship="gesmerha", Chapters=[chapter], last=chapter,
        Areas=[CAPITAL if late else AREA], AnswerLists=[GUEST_ANSWERS if late else ANSWER_LIST],
        ContactUnit=UNIT, RequiresAny=["gesmerha.truth", "gesmerha.illusions"],
        requires=("gesmerha.wintersun_resolved", previous, *(("gesmerha.capital_guest", "gesmerha.heard_future") if late else ())),
        forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil",
                 *(("gesmerha.marhevok_rules",) if late else ())),
        delay=0 if late else delay, optional=True))


s("a_story_from_elsewhere", "The traveler in the story", '"I brought the story you asked for."', [
    n("start", "Gesmerha", '''{n}Gesmerha answers your greeting from behind a length of hanging wool. When you come around it, you find her seated with her hair loose over one shoulder. She is drawing a comb through its ends, working upward a little at a time.{/n}
"Then you have come at an excellent moment. Somebody hung this here to dry and forgot that I use the space behind it. I have been mistaken for a talking blanket twice."
"Should I move it?"
"Tell me where you put it. Then yes. Somewhere its owner will find it before I become an oracle."
{n}You shift the wool to the next peg and describe the change. She finishes the stubborn lock, gathers her hair and ties it back. The comb goes into her lap.{/n}
"A place I have never been," {n}she says.{/n} "And something you enjoyed. I remember my commission."
"There was a room above a busy street. I could hear everybody arguing below."
"That is your pleasure? I could have provided it without the journey."
"I was not responsible for any of them."
{n}Her smile broadens.{/n}
"Now we are getting somewhere. Tell me what you did with this astonishing freedom."''',
      c('"I listened until I could tell which argument belonged to which voice."', "listen"),
      c('"I leaned out and gave advice nobody had requested."', "interfere"),
      c('"I owe you a proper telling. I cannot stay long enough today."', abort=True)),
    n("listen", "Gesmerha", '''"How many did you get wrong?"
"At least two. A woman was accusing someone of stealing her place. I thought she meant a stall. She meant the sun on her doorstep."
"A serious theft."
"The accused was a dog."
{n}Gesmerha laughs, then asks whether the dog moved. It did, eventually, when the woman fetched something from the house. Neither you nor anybody leaning from the other windows could agree whether it was a bribe or a weapon.{/n}
"You could have gone down and found out," {n}she says.{/n}
"I liked not knowing."
"That I understand. People bring me the end of every story now. Often before I have asked for the beginning."
{n}She rests the comb in her lap, with both hands folded over it.{/n}
"Did you stay at the window?"
"Until somebody below noticed me laughing. Then I felt obliged to look as though I had a reason to be there."
"Poor creature. Discovered enjoying yourself without an occupation. I hope you recovered."''', c('[Ask her for a story in return.]', "song")),
    n("interfere", "Gesmerha", '''"I feared you would. Was it useful?"
"Not particularly. I suggested taking turns with the sunny doorstep. Then I learned one of the people arguing was a dog."
"A generous proposal. Half a doorstep is a considerable estate for a dog."
"The woman told me to mind my own business."
"And did you?"
"I went back inside before she found a better answer."
{n}Gesmerha lifts the comb from her lap and turns it once between her fingers.{/n}
"I like her. And I like hearing that there was a window from which you could make yourself foolish without an entire army following your example."
"You think they would?"
"Some of them. There would be a regulation by evening. Half the sunny ground reserved for dogs of proven loyalty."
{n}She gives the imagined order a solemn little nod, then loses the expression in another laugh.{/n}
"Go on. What did you do after being dismissed? I refuse to believe you ceased existing when someone no longer wanted your advice."''', c('[Finish the story, then ask for one of hers.]', "song")),
    n("song", "Gesmerha", '''{n}You tell her about the rest of that idle hour. Nothing remarkable happened. She asks enough questions to make you remember it more clearly than you expected.{/n}
"My grandmother had a song about a woman who wished to be left alone," {n}she says at last.{/n} "Every verse brought someone else to her door. By the end she had gone out through the roof."
"Did that help?"
"Not in my grandmother's version. She met a man repairing it."
{n}She sings the first few lines. Her voice is lower than her speaking voice, a little rough before it warms. The rhythm invites a response. When you miss the place for it, she gives a small, emphatic tap on the bench.{/n}
"There. You answer there. You need not sing well. You must only enter at the right moment."
"What do I answer?"
"'She is not at home.' It becomes a lie very quickly."
{n}You try again. This time your answer lands beneath her last note and sends her searching for the next line through a smile.{/n}
"I used to know all of it. Or I used to think I did. My grandmother never sang the same ending twice."
{n}From beyond the wool comes an answering fragment in a younger voice. Gesmerha stops.{/n}
"Dera?"
"I was bringing the blanket back."
"Then you have performed the first verse without instruction. Come around where we can hear you."''', c('[Make room for the visitor.]', "dera")),
    n("dera", "Gesmerha", '''{n}Dera is a young woman carrying an empty basket. She explains that her mother sang the woman straight over the roof into a wedding feast, where she married the musician so that at least one caller would already be at home.{/n}
"A poor bargain," {n}Gesmerha says.{/n} "He would practice."
"You taught me the wedding verse."
"Did I? Then I was younger and less considerate."
{n}Dera settles on the bench's far end. She once helped finish larger pieces in Gesmerha's workshop, she tells you. Now she spends more of her time preparing hides. Her mother still knows songs Gesmerha has forgotten.{/n}
"We could ask her to sing them," {n}you suggest.{/n}
"We could," {n}Dera says.{/n} "And she would ask who wanted them, and whether we had finished the work she actually asked us to do."
"Your mother has an excellent memory," {n}Gesmerha says.{/n} "Unfortunately it includes debts."
{n}Dera's amusement fades a little.{/n}
"Vesk wants the old winter song for his brother's leaving. He says everybody knows it. I do not. I know the beginning and whatever words fit after it."
{n}Gesmerha's fingers stop moving over the comb.{/n}
"Bring him here tomorrow. Bring your mother if she will come. I can find an hour."
"Not to make everybody sing your version?"
{n}Gesmerha takes a moment before answering.{/n}
"Bring yours too."''', c('[Wait until Dera has taken the wool away.]', "alone")),
    n("alone", "Gesmerha", '''"I was about to say that there is a right version," {n}Gesmerha admits.{/n} "Then I remembered the man on the roof."
"You can still prefer yours."
"I do. I am very fond of the things I can remember accurately. Sometimes I become fond of them before checking the accuracy."
{n}She rubs the comb's smooth back with her thumb.{/n}
"They are leaving with carts, not with a war band. Vesk's brother thinks there will be work farther south. The song used to be for people who expected to come home before the snow. He wants to borrow that certainty."
"Will you give it to him?"
"I shall ask what he wants to sing. That is harder than deciding what he ought to hear."
{n}She turns toward your voice.{/n}
"Would you come? You need not solve anything. I may require someone to tell me when I am being insufferably senior. Dera can do it, but she has other duties."
"And if I agree with you?"
"Then I shall be unbearable. You should consider the risk."
{n}She offers the comb for you to examine, a small plain thing whose worn handle fits her hand. Nothing about it needs repair.{/n}
"You brought me a good hour," {n}she says.{/n} "I should like another."''',
      c('"I will come and listen."', flags=("gesmerha.story_kept",))),
], "gesmerha.opening_kept")

s("the_unfinished_verse", "Who may finish the song", '"Has Vesk brought his winter song?"', [
    n("start", "Gesmerha", '''{n}Three people have brought versions of the same song. Vesk has brought a fourth, copied onto a sheet by a passing clerk, which has already become the most troublesome because it looks settled.{/n}
{n}Gesmerha sits with Dera on one side and Dera's mother, Runa, on the other. Runa has a voice strong enough to make an interruption sound like the beginning of her own verse. Vesk is standing. He seems to have tried sitting and found that he could not stay there.{/n}
"You are in time," {n}Gesmerha says when you speak.{/n} "We have agreed that there was a winter. Nothing following it has survived examination."
"There was a ford," {n}Vesk says.{/n}
"There were two," {n}Runa says.{/n} "That is why the second verse matters."
{n}He offers you the sheet. It gives the departing travelers a triumphant welcome before describing their journey. Gesmerha asks you to read it aloud. At the first mention of the ford, Runa objects. Dera waits until she has finished and quietly sings a different line.{/n}
"That is not what my brother remembers," {n}Vesk says.{/n}
"Your brother wants a farewell," {n}Dera answers.{/n} "He has not asked to examine our memories under oath."''',
      c('[Examine the repeated lines and the clerk\'s ordering of the verses.]', check=dict(Skill="SkillKnowledgeWorld", DC=24, CommanderOnly=True, Success="read", Failure="missed")),
      c('"Put the sheet down. Let each singer finish once without interruption."', "listen"),
      c('"I cannot give this the time it needs today."', abort=True)),
    n("read", "Narrator", '''{n}The clerk has treated every returning line as the beginning of a new verse. On the sheet, a repeated answer has become a command, and the second ford has been moved ahead of the first. You read the passages back in their probable order without pretending to restore the missing words.{/n}
{n}Runa sings against your reading. For the first time, the remembered route and the rhythm fit together. Vesk sits down.{/n}
"There," {n}Gesmerha says.{/n} "A person copying words has to decide where they belong. Ink does not excuse the decision."
"Nor does a good ear," {n}Dera says.{/n}
{n}Gesmerha turns toward her, then nods.{/n}
"No. Mine is about to receive the same examination."
{n}The sheet is useful now, but it cannot settle the last verse. Runa remembers the travelers coming home with hides. Gesmerha remembers a woman turning back alone. Dera says her mother used to omit both when she was tired.{/n}''', c('[Ask why the last verse matters to Vesk.]', "need")),
    n("missed", "Narrator", '''{n}You choose a sequence that appears sensible on the page. Runa tries to sing it. The rhythm carries her into the welcome before the travelers have crossed the river, and Vesk interrupts to ask whether his brother is supposed to arrive home before leaving.{/n}
"An efficient journey," {n}Gesmerha says.{/n} "We should charge by the distance avoided."
{n}Your second attempt tangles the repeated answer with the next verse. You put the page down.{/n}
"I cannot settle this from the writing."
"Then we shall stop asking the writing," {n}she says.{/n}
{n}Runa sings the first crossing. Gesmerha answers, then stops when Dera catches a word neither uses in ordinary speech. Working by voice takes the rest of the morning. By the time the repeated lines have found their places, Vesk has missed the man who offered to lend him a drum.{/n}
"I shall have to knock on a bowl," {n}he says.{/n}
"Use an empty one," {n}Runa says.{/n} "We have already lost enough time."
{n}Vesk laughs despite himself. He remains to hear the disputed ending.{/n}''', c('[Ask what he wants the song to do for his brother.]', "need")),
    n("listen", "Narrator", '''{n}The sheet lies facedown while Runa sings. Gesmerha counts the verses on her fingers. Twice she takes a breath to correct a word and lets it go. Dera's version follows, shorter and less certain, with an ending that leaves the travelers on the far bank.{/n}
{n}Vesk begins reluctantly. Halfway through, he finds a phrase none of the others remembered. Runa asks him to repeat it. He does, with visible satisfaction.{/n}
"That was my father's line," {n}she says.{/n} "He always put his own part where it would be noticed."
{n}Gesmerha sings last. By then the man who offered Vesk a drum has gone, and Vesk will have to supply another accompaniment. He objects to losing him, but not enough to leave before Gesmerha has finished.{/n}
"You all want the song to end somewhere different," {n}he says.{/n}
"Yes," {n}Gesmerha answers.{/n} "Now we can discuss where your brother is going."''', c('[Ask Vesk what his brother requested.]', "need")),
    n("need", "Gesmerha", '''"He asked to hear us," {n}Vesk says.{/n} "Before he could not. I thought there would be less difficulty in that."
{n}Gesmerha lets the silence last until Runa has stopped arranging the folds of her shawl.{/n}
"I wanted the old ending because it is the one I remember hearing when my hands were first trusted with a proper tool," {n}she says.{/n} "I did not want to be the last person who could sing it. That is my reason. It need not be his."
"If we change everything," {n}Runa says,{/n} "he will hear strangers."
"If you make me copy it exactly," {n}Dera says,{/n} "you will hear me trying to sound like you."
{n}Vesk rubs his forehead. The departing brother, it appears, would be satisfied with a song that ended before his cart left.{/n}
"Two evenings from now," {n}he says.{/n} "Whatever we do, I need it by then."
{n}Gesmerha asks for your judgment. Runa and Dera are still listening, with opinions of their own.{/n}''',
      c('"Sing the remembered version together. Let Dera answer it with her own ending afterward."', "answer"),
      c('"Make one version you can all sing. Keep the disputed endings for another evening."', "together")),
    n("answer", "Gesmerha", '''"Then I must leave her enough breath to answer," {n}Gesmerha says.{/n}
"And enough evening," {n}Dera adds.{/n}
{n}Runa will agree if the first song is allowed to finish without anyone laughing over its last line. Dera agrees to that. Vesk agrees to two songs, provided they do not become six while his back is turned.{/n}
"You are not required to like my ending," {n}Dera tells Gesmerha.{/n}
"That is fortunate. I have not heard it yet."
"You have been preparing to dislike it."
{n}Gesmerha smiles reluctantly.{/n}
"I have been preparing several things. Bring it tomorrow. I shall restrict myself to the words you actually sing."
{n}When the others leave, she keeps her hand on the bench where Dera had been sitting.{/n}
"My grandmother would have approved of the argument," {n}she says.{/n} "Then she would have sung whatever she pleased. I am attempting a more difficult accomplishment."
"Which?"
"Keeping my mouth shut until she has finished."''',
      c('[Agree to return for the two songs.]', flags=("gesmerha.verse_kept", "gesmerha.song_answer"))),
    n("together", "Gesmerha", '''"A shorter song," {n}Gesmerha says.{/n} "I can hear Runa calculating how much of hers will survive."
"Most of it," {n}Runa answers promptly.{/n}
{n}Dera insists on changing the line that promises every traveler will return. She will sing that they know the road home. Runa dislikes the change. Vesk likes being able to sing it without deciding what his brother must do after reaching the south.{/n}
{n}Gesmerha repeats the new line, tests it against the rhythm, and gives it back to Dera on the right note.{/n}
"That will fit," {n}she says.{/n} "We shall have to agree on the rest before the evening, or Vesk will leave with his brother merely to escape us."
{n}When the others go, she asks you to repeat the replacement line once more.{/n}
"I miss the old one already. I can still sing it when I want it. That does not make this an easy choice."
"Would you change your answer?"
"No. I wanted them to sing with me. I have discovered the expense."''',
      c('[Agree to return for the shared song.]', flags=("gesmerha.verse_kept", "gesmerha.song_shared"))),
], "gesmerha.story_kept")

s("the_evening_answer", "A voice among the others", '"Is there a place for me at the singing?"', [
    n("start", "Gesmerha", '''{n}There is a place, and Gesmerha has saved it by laying her shawl across the seat. She tells you to put the shawl into her hands rather than moving it somewhere she will have to search.{/n}
"I have already lost an argument about where to sit," {n}she says.{/n} "I will not also lose my clothes."
{n}A few people have gathered beside the workshop. Vesk's brother has brought the straps from his cart to mend while he listens. Runa calls this a discourtesy. He answers that he will enjoy the song less if his bedding falls into a ditch tomorrow.{/n}
"A useful audience," {n}Gesmerha murmurs.{/n} "They may prevent us becoming solemn."
{n}She turns toward your shoulder at the sound of your reply.{/n}
"Dera wanted me to begin. I thought she should. We have settled on Runa, who was already singing while we discussed it."
{n}The first verse rises over the scrape of an awl. Gesmerha waits for the answering line, then enters without hesitation. You follow. Her knee shifts against yours when you come in too early, and her mouth bends around the next word.{/n}''',
      c('[Listen for Dera\'s separate answer.]', "answer", requires=("gesmerha.song_answer",)),
      c('[Join the version they agreed to share.]', "shared", requires=("gesmerha.song_shared",)),
      c('"I cannot stay for the song. I am sorry."', abort=True)),
    n("answer", "Narrator", '''{n}The old song ends with Runa holding the last note longer than anyone else. Dera waits. She does not begin until the cart straps have been set down and the listeners have stopped talking over their cups.{/n}
{n}Her answer follows the traveler who stayed beyond the second ford. It has no marvels. There is a landlord who asks too much, a roof that leaks, and a neighbor who finally learns to pronounce the traveler's name. The returning line is the familiar one, with a single changed word.{/n}
{n}Gesmerha hears the change before you do. Her hand tightens on the shawl. On the next repetition, she joins it.{/n}
"I could not make the roof rhyme," {n}Dera confesses when she finishes.{/n}
"Roofs seldom cooperate," {n}Gesmerha says.{/n} "Keep it."
{n}Runa asks about one line that sounds like a complaint against the people at home. Dera says it is. The answer unsettles the listeners more than the song did. Vesk's brother eventually remarks that he would rather send a complaint than be forbidden to send anything until he was happy.{/n}
{n}The discussion continues over the unmusical business of his departure. Dera has been heard separately, and several people remember her version more readily than the older song. Runa notices, and says nothing all the way home.{/n}''', c('[Stay while the departing traveler says his goodbyes.]', "after")),
    n("shared", "Narrator", '''{n}At the changed line, Runa hesitates. Dera keeps singing. Gesmerha comes in beside her, and the rest follow a little raggedly. The travelers know the road home; the song does not bring them back before they have chosen to return.{/n}
{n}Vesk's brother sets the straps down to join the last verse. He sings the old words once, stops, and tries again. By the end he has learned enough to carry the new line with him.{/n}
"That was shorter than I remember," {n}he says.{/n}
"You are welcome," {n}Dera answers.{/n}
{n}Runa objects that a song should not be praised for ending. Gesmerha asks whether she would prefer the departure delayed until they have performed every verse anybody can remember. Runa says she might.{/n}
{n}The laughter is affectionate, but Dera grows quiet when two listeners praise Gesmerha for improving the song. Gesmerha corrects them by name. One apologizes; the other merely asks Dera to sing the changed line again. She does, without smiling.{/n}''', c('[Stay while the departing traveler says his goodbyes.]', "after")),
    n("after", "Gesmerha", '''{n}After the others leave, Gesmerha stays where she is. She asks you whether Dera went with Runa or followed Vesk to the cart. You tell her what you saw. Dera and her mother left together, still arguing, with the empty cups divided between them.{/n}
"Good. An argument is easier when neither person can make a grand exit without dropping something."
"Did you enjoy it?"
"Very much. I also wanted to interrupt three times. Those are compatible experiences."
{n}She stretches her fingers, one hand at a time.{/n}
"I want to ask Dera to help me remember more of them. I shall have to pay for her time. She cannot leave the hides every afternoon because I am suddenly interested in being a useful elder."
"Can you afford it?"
"A few afternoons. Fewer new tools. I am deciding how much I want the company of those songs."
{n}She draws her shawl around her shoulders.{/n}
"There is another difficulty. I remember a verse about the old stone at the eastern crossing. Dera remembers a different place. We could spend a day walking there and still disagree about what our grandmothers called it."''',
      c('"Ask both families. Let the song keep the disagreement until you know more."', "ordinary"),
      c('[Offer a Trickster experiment: ask the rhyme where it misplaced its crossing.]', "offer", requires=("trickster",))),
    n("ordinary", "Gesmerha", '''"Runa will enjoy having another reason to visit. She will pretend it is an inconvenience."
"You know her well."
"I know that much. I do not know whether she will remember the stone."
{n}Gesmerha hums the troublesome phrase and leaves a gap where the place should be.{/n}
"For now, a silence. I used to be very certain about things I had been taught to trust. We had runestones that were supposed to warn us when demons approached. I believed they worked."
"You had reason to want them to work."
"Yes. That proved an excellent reason to stop asking whether they did. I do not want to make this little song another thing nobody is allowed to question."
{n}She lets the phrase fall away.{/n}
"Tomorrow I shall ask Dera what she charges for an afternoon. I suspect she has already decided. It will be instructive."''', c('[Offer your arm for the short walk back to her bench.]', "close")),
    n("offer", "Gesmerha", '''"Will it answer in my grandmother's voice?"
"No. I would be asking a rhyme to supply a missing word. It might supply a very foolish one."
"Then we shall not mistake it for an ancestor. What else might it do?"
"Refuse to fit any of the words we remember."
{n}She considers this, then sings the phrase with the gap left open.{/n}
"One attempt. And no voice borrowed from anybody dead. I have heard enough assurances from things that wanted to be believed."
{n}You invite the rhyme to stop hiding its luggage in the wrong verse. For a moment the last syllable hangs in the air after Gesmerha has closed her mouth. It twists into the word 'spoon.'{/n}
{n}She makes a startled sound, then begins to laugh.{/n}
"The eastern spoon. A place of great ancestral importance."
{n}You dismiss the echo. The air falls quiet. When she sings the line again, the gap remains.{/n}
"We shall ask Runa," {n}she says.{/n} "And I shall tell her why. She deserves the pleasure."
{n}Gesmerha sings the spoon into the verse once more, in her own voice, and laughs again.{/n}''', c('[Offer your arm for the short walk back to her bench.]', "close")),
    n("close", "Gesmerha", '''{n}She rests her hand above your elbow. At the change in ground you tell her where the low step begins. She knows it, but asks whether the cups have all been moved out of the way. You check before answering.{/n}
"I like having you here when other people are speaking," {n}she says.{/n} "You sound different when you do not think you are being listened to."
"What did I sound like?"
"Pleased. Occasionally early."
"I was following your lead."
"Then I shall have to find another excuse."
{n}At the bench she lets go of your arm and turns to face you.{/n}
"Come when I have no singers expected. I have been thinking about the afternoons we have kept for ourselves. There is something I would like to ask while nobody is waiting for the answer to rhyme."''', c('"I will come."', flags=("gesmerha.singing_kept",))),
], "gesmerha.verse_kept", delay=48)

s("what_she_asks", "The question without a chorus", '"You wanted an afternoon without singers."', [
    n("start", "Gesmerha", '''{n}Gesmerha has put her tools away. The game sits on a shelf within reach, its pieces still in their bowl. She has cleared the afternoon the way she clears a bench, and she is sitting in the middle of it.{/n}
"Dera took the two afternoons," {n}she says.{/n} "She named her price and then apologized for it so fast that I nearly haggled out of habit. I paid before either of us could shame the other."
"And the tools?"
"They will wait. A woodshaper may want a plane and a song both, and buy the song."
{n}She pats the bench beside her. When you sit, your sleeve catches under the edge of her shawl; she tugs it free herself before drawing the wool around her shoulders.{/n}
"I have also told her to sell some of her own work, away from my bench. She said yes to that faster than to anything I have ever offered her."
"Does that trouble you?"
"It stings. I wanted to be the one she learns from. There are things she will learn that my hands cannot give her, and the spirits did not ask my leave."
{n}Her shoulder settles back against the wall.{/n}
"There. That is my confession for the afternoon. Yours may be less respectable."''',
      c('[Tell her you have been looking forward to this private hour.]', "romance", requires=("gesmerha.courting",)),
      c('[Ask what she has been waiting to say to you.]', "slow", requires=("gesmerha.slow",)),
      c('[Tell her something you have been saving for your friend.]', "friend", requires=("gesmerha.friendship",)),
      c('"I want to hear this properly. May I come back when I can stay?"', abort=True)),
    n("romance", "Gesmerha", '''"So have I. More than was convenient. Yesterday someone brought me a difficult piece, and I caught myself wishing it would belong to somebody else for an hour."
"A serious complaint."
"I finished it. My ancestors would not have let me sleep otherwise."
{n}She holds out her hand. You meet it, and her thumb moves along the side of yours, reading it.{/n}
"I want you for my lover," {n}she says.{/n} "I tried saying it more prettily while you were away. Every pretty version said less."
{n}She does not let go.{/n}
"I will not follow you onto your road, and I will not ask you to sit at my bench for the rest of your days. But when I hear your step at the door, I want it to be the step of someone coming to my bed, not to my counter."
{n}Her fingers tighten around yours.{/n}
"That is what I want. Now say whether you want it, and say it plainly. I have had enough fine words from people with something to sell."''',
      c('"I want that too. I want you."', "terms"),
      c('"I care for you, but not yet. Let the afternoons go on as they are."', "wait"),
      c('"What I feel for you is friendship. I won\'t pretend otherwise."', "friends")),
    n("slow", "Gesmerha", '''"Yes. I thought I should say it before I made a joke. I have a good one ready, and it would bury the answer."
{n}She turns her hand palm up on her knee, the way she offers it to a new block.{/n}
"I want to kiss you. I want to find out whether the silence after it is warm or cold. And if you still have no answer for me, I want you to come back anyway."
"You have thought about this."
"Every evening. It has not made me any calmer."
{n}She laughs under her breath, at herself.{/n}
"Among my people a woman does not stand at the door forever waiting for a knock. I have stood there long enough to be ashamed of it. So. I want you. What do you want?"''',
      c('"I want you too. Let this be the beginning."', "terms"),
      c('"Not yet. But I want the afternoons to go on."', "wait"),
      c('"Friendship. That is what I want from you."', "friends")),
    n("terms", "Gesmerha", '''"Good. I had carved three speeches for your refusal. I will burn them."
{n}She moves closer and finds your shoulder with the back of her fingers, and stays there.{/n}
"Two things, before I stop being able to think. The first. A commander has a great many people who want a piece of the day. Never promise me an evening and then give it away. I will know. I will be waiting with supper going cold."
{n}Her hand rests against your collar.{/n}
"My people come first. If the clan needs me on a road, I go, and you do not sulk. If I choose to stay somewhere you cannot follow, you do not pack my tools for me while I am still making up my mind."
"That is all. My grandmother had eleven conditions for her husband, and he broke nine of them. I am asking for two."''',
      c('"No evening of yours given away, and your road is your own. Yes."', "touch"),
      c('"I can\'t swear to that yet. Let the afternoons go on as they are."', "wait")),
    n("touch", "Gesmerha", '''{n}She lifts her hand to your face and finds it at once. Her thumb rests at the corner of your mouth, reading it the way she reads the edge of a cut. Then she kisses you, once, lightly, and draws back just far enough to breathe.{/n}
"I have thought about that more than was wise."
{n}The second kiss is not light. Her hand slides to the back of your neck and holds you there. When you shift toward her, the shawl pins her to the bench; she yanks it out from under her hip with a curse to the spirits that makes you both laugh, throws it to the floor, and comes back to you with a good deal less ceremony.{/n}
{n}Her hand has gone to the front of your shirt, firm and unhesitating, and her other cups the back of your head as she kisses her way along your jaw. You feel her smile when your breath stutters.{/n}
"The door," {n}she says against your mouth.{/n} "Or this bench, until the light goes. Say which. I have waited long enough."''',
      c('"The door."', "private"),
      c('"The bench. Just this, today."', "hold")),
    n("private", "Gesmerha", '''{n}You bar the workshop door. Gesmerha takes your hand and leads you to the pallet behind the curtain, ducking beneath the low shelf.{/n}
"Mind your head. I refuse to explain this to a healer."
{n}She kisses you before you can answer, and her fingers work your belt loose with the speed of long practice. When your hands find the hem of her shift she pulls it off herself and presses close, warm skin against yours, her breath short against your mouth.{/n}
"Stay. The clan has had me since dawn. I want this afternoon, and I want to learn what these hands do when they are not holding a tool."
{n}She draws you down onto the pallet, and the light through the shutter goes on moving across the wall without either of you.{/n}''',
      c('[Continue]', "after_private")),
    n("hold", "Gesmerha", '''"Come nearer, then. I have plans for this bench."
{n}She hauls your arm around her shoulders and settles its weight where she wants it. When your fingers find the tie in her hair, she catches them.{/n}
"Careful. That knot has already beaten me once today."
{n}You work it loose. Her hair falls against your sleeve, and she lets out a long breath. For a while neither of you looks for another subject. When someone passes outside, she calls a greeting and tells them the tools are put away until tomorrow.{/n}
"Was that true?" {n}you ask.{/n}
"It is now."
{n}She turns her face toward your voice. The next kiss is unhurried. After it she settles against you again, one hand over yours, as though her fingers have found a place they mean to remember.{/n}''', c('[Stay while the afternoon grows quiet.]', "road")),
    n("road", "Gesmerha", '''"When you ride out for somewhere I cannot reach," {n}she says after a while,{/n} "do not make the goodbye into a speech. Tell me what you can. Leave the rest to the spirits."
"You expect a long absence?"
"I expect your road does not ask my leave."
{n}She lifts your joined hands and kisses your knuckles.{/n}
"If I can send word, I will. If no word comes, it is only the road. Do not read omens into it. Wintersun read omens for twenty years, and look what that bought us."
"And when I come back?"
"Knock. I will open the door with no dignity at all. But knock."
{n}She settles your hands in her lap again.{/n}
"Today you are here. There is no sense in starting your absence early."''',
      c('"Then today is ours."', flags=("gesmerha.campaign_kept", "gesmerha.lover", "gesmerha.committed"))),
    n("wait", "Gesmerha", '''"Then not yet. I have waited on worse things than you."
{n}She sits back, leaving a hand's width more room between you, and straightens the edge of her shawl with more care than it needs.{/n}
"I will not ask you every time you come. If it changes, say so. I am blind, not a fortune-teller. I will not sit reading how long you hold a cup."
"I would rather say it."
"Good."
{n}She sends you for the game. Before you have set it down, she speaks again.{/n}
"And do not think I will stand at this bench unchanged until you make up your mind. I may have a different answer by then."
{n}She finds her pieces by touch and sets them within reach.{/n}
"Now. Show me whether you have learned anything about that outer row."''',
      c('[Play, and leave the larger answer open.]', flags=("gesmerha.campaign_kept", "gesmerha.campaign_slow"))),
    n("friends", "Gesmerha", '''{n}She draws her hand back into her lap. For a while you both listen to the village outside the workshop.{/n}
"Then friendship. I will get used to it. I may be angry with you while I do."
"Would you like me to go?"
"No. I will not have you run out of here as though the bench were on fire. Sit."
{n}She folds her shawl over her knee.{/n}
"Tell me something about the road you take next. Something true. I am tired of plans built out of what people hope will happen."
{n}You tell her what you can. She asks a practical question, then another. When you leave, she says she wants to hear the rest when you come back. She means it, though the ease will take longer to come back than you do.{/n}''',
      c('"I will come back as your friend."', flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends"))),
    n("friend", "Gesmerha", '''{n}You tell her what you have been saving. She listens with the pleased attention of someone who knows the account was meant for her before the telling began.{/n}
"I shall miss this when you are elsewhere," {n}she says.{/n} "Not only the news. People bring news when they want me to do something about it. You have occasionally brought a story that required nothing except a place to sit."
"Occasionally?"
"I am leaving myself room to complain later."
{n}She asks you to bring the game down. Before you start, she tells you that Dera wants to learn the longer song, including the verses nobody had time to sing. Runa has offered to help. The proposed afternoon is likely to become an argument, and Gesmerha sounds almost eager for it.{/n}
"When you return, ask what we have accomplished. If I say that everybody agreed, you may assume I am concealing something."
"I will remember."
"Remember to come back, if you can. The rest I can remind you of."''',
      c('[Play another game with your friend.]', flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends"))),
    # The aftermath of the private afternoon, its own beat after the cut (Sol 2026-09-30, Directive 12).
    n("after_private", "Gesmerha", '''{n}Later, the light through the shutter has gone from white to gold. She lies with her head on your shoulder and her hair across your chest, and when your hand wanders toward the old scars at her temple she catches it and moves it, without fuss, to the side of her neck.{/n}
"Here is better. There, the chief's knife still has the say."
{n}You leave your hand where she put it. She lets out a long breath, as satisfied as a woman who has finished a difficult cut.{/n}
"Are you hungry?"
"Eventually."
"So am I, eventually. At present I would not get up for the Lady of the Sun herself."''', c('[Stay until she is ready to get up.]', "road_private")),
    # The road page again for the private path: flags are set only on terminal choices, so this copy records the afternoon.
    n("road_private", "Gesmerha", '''{n}She lifts your joined hands and kisses your knuckles. The barred door rattles once; she ignores it.{/n}
"When your army takes you somewhere I cannot reach, tell me what you can. I will miss this. Do not send someone else's fine words to explain why I should not."
{n}She tucks your arm back around her and settles against you.{/n}
"For now, let them knock."''',
      c('"Then today is ours."', flags=("gesmerha.campaign_kept", "gesmerha.lover", "gesmerha.committed", "gesmerha.afternoon_shared"))),
], "gesmerha.singing_kept")

# PP7 (Chapter 4): she stays in Wintersun and the Commander is in the Abyss; nothing crosses the planes. What travels is
# the travelers' song settled at her bench in the_unfinished_verse / the_evening_answer (Vesk's brother's farewell song:
# the shared version, "the travelers know the road home", or Runa's song with Dera's answer). Path: N-fit (it carries the
# chain's own blockers, no trickster gate). Read in Chapter 5 by the_voice_at_court (songs) and the_things_still_here
# (without_court). Authored: the march, the humming, the Commander's verse.
ABYSS_SONG = "gesmerha.abyss_song"
SONG_SUNG = "gesmerha.abyss_song.sung"
SONG_VERSE = "gesmerha.abyss_song.verse"
SONG_HUSHED = "gesmerha.abyss_song.hushed"
SONG_CHOICES = (
    c('[Sing it through to the end, the way they agreed it at her bench, so you do not lose it down here.]', "sung"),
    c('[Add a verse of your own about this road.]', "verse"),
    c('[Stop humming. It is Wintersun\'s song, and this is no place to carry it.]', "hushed"),
)
SCENES.append(scene("gesmerha.the_road_home", "The road home", "Gesmerha", 4, "", [
    n("start", "Narrator", '''{n}Somewhere in the Abyss, on a march that began before the light last changed, you realise you have been humming for some time. Nobody in the column has complained. It takes you a dozen paces more to know the tune: the travelers' song from Wintersun, the one Vesk needed by the second evening, the one three families could not agree how to end.{/n}''',
      c("Continue", "shared", requires=("gesmerha.song_shared",)),
      c("Continue", "answer", requires=("gesmerha.song_answer",), forbids=("gesmerha.song_shared",)), portrait="Gesmerha"),
    n("shared", "Narrator", '''{n}You have the version they settled on: Runa's verses, cut short, and Dera's changed line. The travelers know the road home. Gesmerha tested that line against the rhythm and gave it back to Dera on the right note, and told you afterwards that she missed the old one already. "I wanted them to sing with me," she said. "I have discovered the expense."{/n}
{n}Down here the line sounds different. Nobody in this column is sure of the road home.{/n}''', *SONG_CHOICES, portrait="Gesmerha"),
    n("answer", "Narrator", '''{n}You have both of them: Runa's old song, held to its last note, and then Dera's answer, the traveler who stayed beyond the second ford, with a landlord who asked too much and a roof that leaked. "I could not make the roof rhyme," Dera said. "Roofs seldom cooperate," Gesmerha told her. "Keep it."{/n}
{n}Down here you find you know Dera's verse better than the old one.{/n}''', *SONG_CHOICES, portrait="Gesmerha"),
    n("sung", "Narrator", '''{n}You sing it through under your breath to its ending, the way it was settled on a bench in Wintersun while a man mended his cart straps and Runa told him it was a discourtesy. Somebody behind you in the column picks up the tune without the words. You do not teach them the words. They are not yours to teach.{/n}''',
      c('[Walk on.]', flags=(ABYSS_SONG, SONG_SUNG)), portrait="Gesmerha"),
    n("verse", "Narrator", '''{n}It is not a good verse. It has no marvels in it, only what the road is like: a sky the wrong colour, water you boil twice before you trust it, a camp where nobody sleeps on the side nearest the dark. You cannot make the sky rhyme. You keep it anyway, and sing it twice so you will still have it in Drezen.{/n}''',
      c('[Keep the verse.]', flags=(ABYSS_SONG, SONG_VERSE)), portrait="Gesmerha"),
    n("hushed", "Narrator", '''{n}You stop. It seems wrong to carry Wintersun's song through a place like this, as if the tune might come home with something on it. The march goes on in silence. Some miles later you notice you are still keeping its time with your feet.{/n}''',
      c('[Walk on.]', flags=(ABYSS_SONG, SONG_HUSHED)), portrait="Gesmerha"),
], requires=("gesmerha.campaign_kept", "gesmerha.verse_kept"),
    forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", ABYSS_SONG), delay=24, last=4, optional=True,
    Relationship="gesmerha", Chapters=[4], Remote=True, Kind="memory"))


def abyss_song_nodes():
    """PP7: the_voice_at_court's answers to the Chapter 4 song (appended after songs' own choices), each back to the bundle."""
    back = (c('[Remember the two trays made after the wood split.]', "trays", requires=("gesmerha.grain_missed",)),
            c('[Remember the narrow board and the names of its rows.]', "board", forbids=("gesmerha.grain_missed",)))
    return [
        n("abyss_sung", "Gesmerha", '''"You sang it." {n}Her hand stops on the knot of the bundle.{/n} "Down there. Which ending?"
{n}You tell her, and hum the line. Her mouth moves with it before she can stop it.{/n}
"And someone in your column took the tune without the words? Then it has travelled further than Vesk's brother, and in worse company." {n}She laughs once, and it catches.{/n} "Runa would have been insufferable about it. She would have said a song that goes into the Abyss and comes back has earned its old ending. I shall tell Dera instead, and let her be insufferable."''', *back),
        n("abyss_verse", "Gesmerha", '''"A verse of your own." {n}She turns her face toward you, the whole of her attention in it.{/n} "Sing it."
{n}You do, badly, sky and all. She does not interrupt once, and it visibly costs her.{/n}
"The sky does not scan," {n}she says when you finish.{/n} "We can mend the rhythm. Keep it." {n}She is quiet a moment.{/n} "Dera will want it. She will change two words and call it hers. Let her. That is how a song is carried, and I would rather it went on in her mouth than sat in mine."''', *back),
        n("abyss_hushed", "Gesmerha", '''"You stopped." {n}She considers it with her head a little to one side.{/n} "To keep it clean of the place."
"It felt wrong to carry it there."
"We sang it over a man mending his cart straps, with Runa scolding him between verses. It was never a clean song." {n}Her thumb rubs once over the bundle's knot.{/n} "But I understand you. I have kept things back from bad places myself. Next time, sing. If it comes home with something on it, we will wash it."''', *back),
    ]


s("the_voice_at_court","The voice that came back", '"Before you go, may we speak about something of our own?"', [
    n("start", "Gesmerha", '''{n}Gesmerha has come to court with the road still on her clothes. You have heard what she intends for her people. At your question she turns toward you, and the careful formality of her voice gives way.{/n}
"Yes. I hoped you would ask. There are a great many people in this room who appear to be waiting for permission to make you useful again."
{n}You ask the nearest attendants for a little space. They withdraw far enough to leave the conversation to you. Gesmerha stays where she gave her report.{/n}
"Tell me how near you are."
{n}You answer and offer your hand. She takes it, drawing you a little closer.{/n}
"There. I wanted something more convincing than a rumor. Your voice was a good beginning."
{n}Her fingers close firmly around yours before relaxing.{/n}''',
      c('"I missed you. I missed being wanted for myself."', "lover", requires=("gesmerha.lover",)),
      c('"I have thought about the answer we left open."', "slow", requires=("gesmerha.campaign_slow",)),
      c('"I missed my friend."', "friend", requires=("gesmerha.campaign_friends",)),
      c('"I cannot speak privately now. I am glad you came."', abort=True)),
    n("lover", "Gesmerha", '''"Then you should know I spent the whole silence angry with you. Anger is easier to carry than fear, and it keeps a woman on her feet."
"I could not send you word."
"I know. I told you not to read omens into it. I read them anyway."
{n}She raises your hand to her mouth and kisses it. It is brief, but when she lowers it she does not let go.{/n}
"Do you still want me here?" {n}you ask.{/n}
"Yes. There. No dignity at all, as I promised."
{n}Her laugh shakes once. She takes a breath and steadies it.{/n}
"I have no room of my own to take you to in this place, and half the clan is waiting on when I leave. So I will stand here holding your hand in front of your whole court, and they may call it a courtesy if they like."
"Let them."
"Yes. Let them wait. I have had a great deal of practice at waiting."''', c('[Ask what she has carried with her.]', "songs")),
    n("slow", "Gesmerha", '''"So have I. A different answer every day. None of them was improved by not knowing whether you were alive to hear it."
{n}She rubs your knuckles once with her thumb, then loosens her hold.{/n}
"I am glad you are here. I will not make one hurried meeting in a hall answer for every day in between."
"We don't have to."
"No. We start with the people who actually came back, not the ones we rehearsed speeches at."
{n}She keeps your hand.{/n}
"There. One thing decided today. I have missed small decisions."
"You never used to find them small."
"You remember me rightly. That is a good beginning."''', c('[Ask what she has carried with her.]', "songs")),
    n("friend", "Gesmerha", '''"And I missed hearing a story whose ending did not require me to find beds for everybody in it."
{n}She presses your hand before releasing it. Her shoulders ease a little.{/n}
"I am pleased you are alive," {n}she says.{/n} "It sounds absurdly small beside everything people have been saying. I find it enough to occupy me."
"It is enough for me too."
"Then we shall spare each other a speech. I have one for the people waiting to travel with me, and I do not want to waste all my convincing words in the same room."
{n}She asks whether you have eaten. At your answer she observes that returning from the dead ought to improve a person's authority over mealtimes, then admits she has missed her own.{/n}
"We remain excellent advisers to everyone except ourselves."''', c('[Ask what she has carried with her.]', "songs")),
    n("songs", "Gesmerha", '''{n}At your question she touches the small bundle at her side.{/n}
"Clothes. A few tools. A game that takes more room than I intended."
"You brought it?"
"I have had cause to learn which things I reach for when somebody says there is little time. The answer was not entirely sensible."
{n}She tells you that Dera is with the traveling party. Runa is not. Her daughter has been singing softly while they stop at night, sometimes the same few lines until someone asks for a different tune. Gesmerha does not supply an account of Runa's last hours. She was not there.{/n}
"Dera asked me to remember the version I used to argue with," {n}she says.{/n} "I could remember most of it. She supplied a line I had forgotten. Then we disagreed about another. That was a relief neither of us expected."
{n}Her hand rests on the bundle's knot.{/n}
"I have not told her that she must preserve every song now. There are mornings when getting up is work enough. If she sings, I answer. When she stops, I let her."
"And your own singing?"
"Some nights. Not all of them."
{n}She shifts the bundle away from her foot.{/n}
"I am keeping the game. That much I have decided."''',
      c('[Remember the two trays made after the wood split.]', "trays", requires=("gesmerha.grain_missed",)),
      c('[Remember the narrow board and the names of its rows.]', "board", forbids=("gesmerha.grain_missed",)),
      # PP7: the Chapter 4 song (the_road_home), appended.
      c('[Tell her you sang the travelers\' song in the Abyss.]', "abyss_sung", requires=(SONG_SUNG,)),
      c('[Tell her you made the travelers\' song a verse of your own in the Abyss.]', "abyss_verse", requires=(SONG_VERSE,)),
      c('[Tell her you stopped yourself singing it in the Abyss.]', "abyss_hushed", requires=(SONG_HUSHED,))),
    n("trays", "Gesmerha",'''"Two awkward pieces to pack," {n}she says.{/n} "I wrapped them separately. Dera asked why I had not made something that folded. I told her I had entertained that ambition once."
{n}Her mouth curves into a brief smile.{/n}
"We played on a cloth beneath one of them. It still needs folding twice where the ground is uneven. I considered carving new feet. Then we had to move. The cloth was faster."
"Does Dera defend the outer row?"
"She attacks it. I told her she was not the first person to make that particular mistake. She improved before I had finished enjoying myself."
{n}Gesmerha's fingers trace the shape of the bundle through its wrapping.{/n}
"It has done what I wanted. People hold it before they ask what it means. Sometimes they never ask. I am grateful for those evenings."''', c('[Return to the future she has described for her people.]', "future")),
    n("board", "Gesmerha", '''"Dera thinks I made the rows too narrow," {n}she says.{/n} "I told her they were made for people willing to learn where their fingers belonged. She told me that sounded expensive."
"Was it?"
"In patience, certainly. She learned. Then she began winning often enough that I regretted being such a useful teacher."
{n}Gesmerha's fingers trace the shape of the bundle through its wrapping.{/n}
"I still name the rows. It saves an argument about where somebody meant to put a piece. We have enough other arguments available."
"Has it survived the journey?"
"So far. There is a new rough place along the edge. I know where it is. When I have the time, I shall smooth it."
{n}She leaves her hand there a moment longer.{/n}
"It has done what I wanted. We can sit with it and be people playing badly, instead of people who must explain how they arrived at the same fire."''', c('[Return to the future she has described for her people.]', "future")),
    n("future", "Narrator", '''{n}Beyond the quiet space left to you, the court is beginning to move again. Gesmerha hears a chair scrape and turns her face toward the sound before returning to your voice.{/n}''',
      c('"You said you would leave in search of a new home."', "leaving", requires=("gesmerha.heard_migration",)),
      c('"You said you would shelter in the forests and mountain trails, and hope to restore Sarkoris."', "shelter", requires=("gesmerha.heard_staying",), forbids=("gesmerha.heard_migration",))),
    n("leaving", "Gesmerha", '''"Yes. I do not know where we will finish. I dislike saying that to people who are already tired. I would dislike being proved a liar more."
"Would it help to stay near Drezen?"
"For some, perhaps. I shall ask them. Near an army is not the same as safe, and I cannot choose everyone's home by standing close to someone I am glad to see."
{n}She shifts her weight and settles again.{/n}
"I want a place where the first question is not what happened in Wintersun. Work I can finish without hearing someone remember a death halfway through asking for it. Then I feel ashamed for wanting that, because they have to carry the memories somewhere too."
"Wanting a different morning does not tell them to forget."
"No. Nor does it tell us where to sleep. That is the part I must find out next."
{n}She asks you not to send someone searching every road merely to obtain a reassuring answer. If a trustworthy carrier can bring word, she will use them. She will not promise a date she cannot keep.{/n}''', c('[Ask how she wants this meeting to end.]', "choice")),
    n("shelter", "Gesmerha", '''"Yes. Leaving the houses does not mean leaving the land. I shall have to say that many times. Some people hear the first part and stop listening."
"And you still want to return?"
"I want to see what we can make there when it is possible to work without preparing to flee. I know what the old place cost us. I also know things I would not willingly hand over to the ruin."
{n}She taps the bundle beside her with two fingers.{/n}
"Not every person will want the same thing. Dera wants to sell work somewhere her mother was not already known. I told her that was a fair ambition. It stuck in my throat on the way out."
"Will you ask her to stay?"
"I have asked her to help while we travel. Not for the rest of her life. If I want her back, I had better make something worth coming back to."
{n}Gesmerha straightens the tie at her wrist.{/n}''', c('[Ask how she wants this meeting to end.]', "choice")),
    n("choice", "Gesmerha", '''"With a little time still belonging to us," {n}she says.{/n} "I have given the report. I can spend a few more breaths deciding what I want to remember of your welcome."
{n}She turns toward you, waiting for you to speak before reaching out.{/n}''',
      c('"I\'m still yours. Kiss me before you go."', "kiss", requires=("gesmerha.lover",)),
      c('"Stay beside me a moment."', "quiet"),
      c('"I can\'t go on courting you. Better you hear it from me."', "part", requires=("gesmerha.lover",))),
    n("kiss", "Gesmerha", '''"Come here, then. I will not hunt for your mouth by listening to the silence."
{n}Her hand finds your cheek, and she kisses you, deliberate and warm, the way you remember. This time she does not laugh when you part. She rests her forehead against yours for a breath, then another.{/n}
"There," {n}she says softly.{/n} "I have wanted that since I heard your step at the door."
{n}When she draws back, you settle the bundle where she can lift it without catching the strap, and tell her how the floor lies between her and the waiting attendants.{/n}
"You still owe me an ordinary story," {n}she says.{/n} "Not today. Today I will let myself be impressed that you are breathing."
{n}She leaves the next meeting unpromised. The kiss is still warm on your mouth as the room becomes a court again.{/n}''',
      c('[Let her finish her native audience when she is ready.]', flags=("gesmerha.reunion_kept", "gesmerha.reunion_lovers"))),
    n("quiet", "Gesmerha", '''{n}You stand together while the court gives you what little quiet it can. She asks about one familiar person, and you tell her what you know. When your answer reaches its limit, she accepts it without asking you to make the missing part kinder.{/n}
"I am glad I came," {n}she says.{/n} "Whatever happens after I leave, I wanted to have heard you answer me."
{n}You tell her the same. She holds your hand briefly, then asks where the attendants are waiting. You describe the clear space between her and them.{/n}
"We should let them earn their patience," {n}she says.{/n} "I have not finished being inconvenient for the day."
{n}Her smile returns as she lifts the bundle. There is still business to conclude before she goes. You have had a few minutes that belonged to neither the business nor the road.{/n}''',
      c('[Return to the audience together.]', flags=("gesmerha.reunion_kept", "gesmerha.reunion_quiet"))),
    n("part", "Gesmerha", '''{n}Her hand becomes still. She lets go of yours and takes a breath before answering.{/n}
"Thank you for saying it to my face. I would have hated to learn it from the way everyone stepped around me."
"I did not want to hurt you here."
"There is no better place. We are here. It will serve."
{n}She finds the strap of her bundle and runs it between her fingers.{/n}
"I meant what I offered you. I will not pretend otherwise because your answer has changed. I will not want your company for a long while. Do not come looking for it."
"I understand."
"Good. Now let me finish what I came to say. The people waiting on me should not have to guess which silence is theirs."
{n}You tell her where the attendants are. She turns toward them with her bundle in hand.{/n}''',
      c('[Respect her request and return to the audience.]', flags=("gesmerha.reunion_kept", "gesmerha.closed", "gesmerha.parted"))),
    *abyss_song_nodes(),
], "gesmerha.campaign_kept", chapter=5)


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue", paragraphs=(), **extra):
    SCENES.append(scene("gesmerha.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Gesmerha", paragraphs=paragraphs)], Relationship="gesmerha", last=99,
        requires=("gesmerha.campaign_kept", *requires), forbids=forbids,
        **{k: dict(v) if isinstance(v, dict) else v for k, v in extra.items()}))


# A native Trickster ending after the sacrifice brings the Commander back (trickster.commander_back, trickster_world): the
# living endings stand and the mourning page yields (Sol 2026-09-30, INT; ledger row 16).
SURVIVED = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})
ending("living_reunion", "An answer kept", '''{n}Gesmerha carried the game away from Drezen among the few things she had chosen to keep, wrapped in a shirt so the pieces would not knock. Where the clan would settle had not been decided at court, and the Commander's welcome did not decide it for her.{/n}
{n}On the road she told Dera that the Commander had asked after the songs. She was smiling before she reached the end of it. When Dera asked for more, she refused, then gave one detail anyway, and made Dera swear not to put it in a verse.{/n}
{n}No day had been fixed for another meeting. At night, when the fire was low, she said the Commander's name once to the spirits in the old way, so that they would know whose step to listen for.{/n}''',
    requires=("gesmerha.reunion_kept",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice"), **SURVIVED)
# The recollection is of the afternoons actually played: the registered Chapter 3 route, or the one claimed afternoon of the
# Trickster fallback (wrong footsteps: the trick and the lost game, or the confession).
CATCHUP = "gesmerha.trickster.cost.catchup"
TRICK = "gesmerha.trickster.cost.campaign_slow"
FIRSTMET = "gesmerha.trickster.cost.first_meeting"
ending("unmet_again", "The afternoon remembered", '''{n}The road did not bring the Commander back to Gesmerha's bench.{/n}''',
    forbids=("gesmerha.reunion_kept", "gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice"),
    paragraphs=(
        p("{n}There had been a woman laughing over a song about a caller at the door, a hard afternoon when she said what she "
          "wanted and made the Commander answer plainly, and a game neither of them finished often enough. What she would have "
          "said at another meeting stayed hers. The Commander kept the last afternoon as it had been, the awkward parts "
          "included.{/n}", forbids=(CATCHUP, FIRSTMET)),
        p("{n}Their last game began with a lie: ten afternoons invented to obtain another visit. She "
          "caught it, set out the pieces, explained the outer-row rule, and stopped a hand making a move "
          "she had just forbidden. The Commander lost and paid for the pieces. There was meant to be another "
          "game. The road did not bring it; she kept the real visits in mind, not the invented ten.{/n}", requires=(CATCHUP, TRICK)),
        p("{n}Their last visit began with a lie about ten afternoons, owned before she had finished calling it "
          "one. Honest liars pay for the pieces too, she said, and the Commander paid, and sat. She had meant to count the "
          "real visits. The false ten did not erase them. The road did not bring another.{/n}",
          requires=(CATCHUP,), forbids=(TRICK,)),
        p("{n}There had been one afternoon, late in the war, at a bench the Commander had walked past before without stopping. "
          "Two lost games, the pieces paid for, and a blind woman learning a new step. She had meant to count the afternoons "
          "from that one. The road did not bring another game.{/n}", requires=(FIRSTMET,)),
    ), **SURVIVED)
ending("loss", "The answering voice", '''{n}Gesmerha died. Neither the game nor the songs could answer in her place. People who remembered her sometimes quarrelled over a line she had sung, and for a moment the quarrel left room for the correction that would not come.{/n}
{n}The Commander's memories were less orderly than a tribute. Her temper at being interrupted. Her hand held out to be met. The exact pause before she said she wanted something, and then said it anyway.{/n}
{n}Her line had never gone to its ancestors with work on the bench. The game was still on hers when she went.{/n}''', requires=("gesmerha.dead",))
ending("changed", "A welcome withdrawn", '''{n}What the Commander became, Gesmerha would not welcome. She had knelt twenty years to a smiling Lady while demons walked the streets of Wintersun, and a familiar voice was no longer enough to open her door.{/n}
{n}She did not pretend the old afternoons had been a warning she had heard at the time. They had been good. The door stayed shut.{/n}''',
    requires=("inhuman",), forbids=("gesmerha.dead", "gesmerha.closed"))
ending("demon", "No borrowed welcome", '''{n}Gesmerha refused the Commander's demonic path in one sentence. She knew what a pleasing voice sounds like when it is making cruelty sound necessary; Wintersun had listened to one for a generation. She remembered wanting the Commander's company. She did not have to forget the wanting in order to spit on what it had become.{/n}''',
    requires=("demon",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman"))
ending("devil", "A promise is not a chain", '''{n}The Commander's infernal path did not acquire Gesmerha with the rest of its claims. She had given her afternoons, not her name on a contract, and she was a Sarkorian woman, not a fool: she knew what a devil does with an old promise. Her refusal was short, and she had it carried word for word.{/n}''',
    requires=("devil",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon"))
ending("ascent", "Beyond the next verse", '''{n}News of the Commander's ascent made Gesmerha fall silent. Then she made the messenger tell it again, all of it, plainly.{/n}
{n}She had known someone who could walk in with an ordinary story and sit down to lose a game. Whether a god would still want such an afternoon, the spirits did not say, and she did not ask them.{/n}
{n}Sometimes she sang the caller's song with a new pause before the answering line. Sometimes she finished it briskly, as though the one at the door ought to learn some patience.{/n}''',
    requires=("ascended",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil"))
ending("sacrifice", "The words already spoken", '''{n}Gesmerha heard what the Commander's sacrifice had bought. She asked one question about the end, and sent the messenger away before he could tell her how she ought to feel about it.{/n}
{n}For a season she could not finish the caller's song; the answering line came to her mouth and stopped there. Later she sang it again, though never when asked.{/n}
{n}She added nothing to what had been said between them, and struck nothing out. She lit a fire in the old way and said the Commander's name into it, so that the ancestors would know the step. She wanted more afternoons. There was no one left to knock.{/n}''',
    requires=("sacrifice",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "trickster.commander_back"))
ending("aeon", "A song in another history", '''{n}In the history remade without the Worldwound, no Commander came to Gesmerha's bench with the same story. The Lady's deception, the questions nobody else would ask and the afternoons that followed had not brought two people to that bench.{/n}
{n}Whatever songs she knew in that world, they owed nothing to afternoons erased along with their cause. Her life belonged to that world. The vanished traveler had no answer to claim from it.{/n}''', owner="AeonEpilogue")


# The companion who reacts to the private afternoon (Sol 2026-09-30, BEL): Lann, a Mongrel who knows what it is to be judged
# by a face, about a woman who cannot see one.
SCENES.append(reaction("Lann", "gesmerha.react.lann_afternoon", ("gesmerha.afternoon_shared", "lann.in_party"),
    '''"You came back from the carvers' workshop that day with sawdust in your hair and your belt done up wrong." {n}Lann does not look at you while he says it.{/n} "Mongrels don't get courted much. When we do, it's mostly someone deciding we're not so ugly in bad light. She can't see you at all, and she still picked you. I'd hang on to that."''',
    answer_list="66385ad77fa743e4bb1234078dbd804c", forbids=("lann.dead", "lann.kicked_out"), chapter=3, last=3, delay=24,
    entry='"About the carver in Wintersun..."'))


def integrate(payload):
    payload.setdefault("Etudes", {}).update(ETUDES)
    payload.setdefault("SeenCues", {}).update(SEEN_CUES)
