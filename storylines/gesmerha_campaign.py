"""Gesmerha's living campaign continuation, with a bounded native C5 reunion.

The songs, apprentices and relationship are authored developments.
The capital visit is restricted to the actual guest etude, actor and answer list.
No revival, permanent guest, sight restoration or native outcome is written.
"""
from story_format import c, n, scene
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
"A place I have never been," she says. "And something you enjoyed. I remember my commission."
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
"You could have gone down and found out," she says.
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
"My grandmother had a song about a woman who wished to be left alone," she says at last. "Every verse brought someone else to her door. By the end she had gone out through the roof."
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
"A poor bargain," Gesmerha says. "He would practice."
"You taught me the wedding verse."
"Did I? Then I was younger and less considerate."
{n}Dera settles on the bench's far end. She once helped finish larger pieces in Gesmerha's workshop, she tells you. Now she spends more of her time preparing hides. Her mother still knows songs Gesmerha has forgotten.{/n}
"We could ask her to sing them," you suggest.
"We could," Dera says. "And she would ask who wanted them, and whether we had finished the work she actually asked us to do."
"Your mother has an excellent memory," Gesmerha says. "Unfortunately it includes debts."
{n}Dera's amusement fades a little.{/n}
"Vesk wants the old winter song for his brother's leaving. He says everybody knows it. I do not. I know the beginning and whatever words fit after it."
{n}Gesmerha's fingers stop moving over the comb.{/n}
"Bring him here tomorrow. Bring your mother if she will come. I can find an hour."
"Not to make everybody sing your version?"
{n}Gesmerha takes a moment before answering.{/n}
"Bring yours too."''', c('[Wait until Dera has taken the wool away.]', "alone")),
    n("alone", "Gesmerha", '''"I was about to say that there is a right version," Gesmerha admits. "Then I remembered the man on the roof."
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
"You brought me a good hour," she says. "I should like another."''',
      c('"I will come and listen."', flags=("gesmerha.story_kept",))),
], "gesmerha.opening_kept")

s("the_unfinished_verse", "Who may finish the song", '"Has Vesk brought his winter song?"', [
    n("start", "Gesmerha", '''{n}Three people have brought versions of the same song. Vesk has brought a fourth, copied onto a sheet by a passing clerk, which has already become the most troublesome because it looks settled.{/n}
{n}Gesmerha sits with Dera on one side and Dera's mother, Runa, on the other. Runa has a voice strong enough to make an interruption sound like the beginning of her own verse. Vesk is standing. He seems to have tried sitting and found that he could not stay there.{/n}
"You are in time," Gesmerha says when you speak. "We have agreed that there was a winter. Nothing following it has survived examination."
"There was a ford," Vesk says.
"There were two," Runa says. "That is why the second verse matters."
{n}He offers you the sheet. It gives the departing travelers a triumphant welcome before describing their journey. Gesmerha asks you to read it aloud. At the first mention of the ford, Runa objects. Dera waits until she has finished and quietly sings a different line.{/n}
"That is not what my brother remembers," Vesk says.
"Your brother wants a farewell," Dera answers. "He has not asked to examine our memories under oath."''',
      c('[Examine the repeated lines and the clerk\'s ordering of the verses.]', check=dict(Skill="SkillKnowledgeWorld", DC=24, CommanderOnly=True, Success="read", Failure="missed")),
      c('"Put the sheet down. Let each singer finish once without interruption."', "listen"),
      c('"I cannot give this the time it needs today."', abort=True)),
    n("read", "Narrator", '''{n}The clerk has treated every returning line as the beginning of a new verse. On the sheet, a repeated answer has become a command, and the second ford has been moved ahead of the first. You read the passages back in their probable order without pretending to restore the missing words.{/n}
{n}Runa sings against your reading. For the first time, the remembered route and the rhythm fit together. Vesk sits down.{/n}
"There," Gesmerha says. "A person copying words has to decide where they belong. Ink does not excuse the decision."
"Nor does a good ear," Dera says.
{n}Gesmerha turns toward her, then nods.{/n}
"No. Mine is about to receive the same examination."
{n}The sheet is useful now, but it cannot settle the last verse. Runa remembers the travelers coming home with hides. Gesmerha remembers a woman turning back alone. Dera says her mother used to omit both when she was tired.{/n}''', c('[Ask why the last verse matters to Vesk.]', "need")),
    n("missed", "Narrator", '''{n}You choose a sequence that appears sensible on the page. Runa tries to sing it. The rhythm carries her into the welcome before the travelers have crossed the river, and Vesk interrupts to ask whether his brother is supposed to arrive home before leaving.{/n}
"An efficient journey," Gesmerha says. "We should charge by the distance avoided."
{n}Your second attempt tangles the repeated answer with the next verse. You put the page down.{/n}
"I cannot settle this from the writing."
"Then we shall stop asking the writing," she says.
{n}Runa sings the first crossing. Gesmerha answers, then stops when Dera catches a word neither uses in ordinary speech. Working by voice takes the rest of the morning. By the time the repeated lines have found their places, Vesk has missed the man who offered to lend him a drum.{/n}
"I shall have to knock on a bowl," he says.
"Use an empty one," Runa says. "We have already lost enough time."
{n}Vesk laughs despite himself. He remains to hear the disputed ending.{/n}''', c('[Ask what he wants the song to do for his brother.]', "need")),
    n("listen", "Narrator", '''{n}The sheet lies facedown while Runa sings. Gesmerha counts the verses on her fingers. Twice she takes a breath to correct a word and lets it go. Dera's version follows, shorter and less certain, with an ending that leaves the travelers on the far bank.{/n}
{n}Vesk begins reluctantly. Halfway through, he finds a phrase none of the others remembered. Runa asks him to repeat it. He does, with visible satisfaction.{/n}
"That was my father's line," she says. "He always put his own part where it would be noticed."
{n}Gesmerha sings last. By then the man who offered Vesk a drum has gone, and Vesk will have to supply another accompaniment. He objects to losing him, but not enough to leave before Gesmerha has finished.{/n}
"You all want the song to end somewhere different," he says.
"Yes," Gesmerha answers. "Now we can discuss where your brother is going."''', c('[Ask Vesk what his brother requested.]', "need")),
    n("need", "Gesmerha", '''"He asked to hear us," Vesk says. "Before he could not. I thought there would be less difficulty in that."
{n}Gesmerha lets the silence last until Runa has stopped arranging the folds of her shawl.{/n}
"I wanted the old ending because it is the one I remember hearing when my hands were first trusted with a proper tool," she says. "I did not want to be the last person who could sing it. That is my reason. It need not be his."
"If we change everything," Runa says, "he will hear strangers."
"If you make me copy it exactly," Dera says, "you will hear me trying to sound like you."
{n}Vesk rubs his forehead. The departing brother, it appears, would be satisfied with a song that ended before his cart left.{/n}
"Two evenings from now," he says. "Whatever we do, I need it by then."
{n}Gesmerha asks for your judgment. She is not giving you the song to dispose of. Runa and Dera are still listening, with opinions of their own.{/n}''',
      c('"Sing the remembered version together. Let Dera answer it with her own ending afterward."', "answer"),
      c('"Make one version you can all sing. Keep the disputed endings for another evening."', "together")),
    n("answer", "Gesmerha", '''"Then I must leave her enough breath to answer," Gesmerha says.
"And enough evening," Dera adds.
{n}Runa will agree if the first song is allowed to finish without anyone laughing over its last line. Dera agrees to that. Vesk agrees to two songs, provided they do not become six while his back is turned.{/n}
"You are not required to like my ending," Dera tells Gesmerha.
"That is fortunate. I have not heard it yet."
"You have been preparing to dislike it."
{n}Gesmerha smiles reluctantly.{/n}
"I have been preparing several things. Bring it tomorrow. I shall restrict myself to the words you actually sing."
{n}When the others leave, she keeps her hand on the bench where Dera had been sitting.{/n}
"My grandmother would have approved of the argument," she says. "Then she would have sung whatever she pleased. I am attempting a more difficult accomplishment."
"Which?"
"Listening to the answer without composing my next correction."''',
      c('[Agree to return for the two songs.]', flags=("gesmerha.verse_kept", "gesmerha.song_answer"))),
    n("together", "Gesmerha", '''"A shorter song," Gesmerha says. "I can hear Runa calculating how much of hers will survive."
"Most of it," Runa answers promptly.
{n}Dera insists on changing the line that promises every traveler will return. She will sing that they know the road home. Runa dislikes the change. Vesk likes being able to sing it without deciding what his brother must do after reaching the south.{/n}
{n}Gesmerha repeats the new line, tests it against the rhythm, and gives it back to Dera on the right note.{/n}
"That will fit," she says. "We shall have to agree on the rest before the evening, or Vesk will leave with his brother merely to escape us."
{n}When the others go, she asks you to repeat the replacement line once more.{/n}
"I miss the old one already. I can still sing it when I want it. That does not make this an easy choice."
"Would you change your answer?"
"No. I wanted them to sing with me. I have discovered the expense."''',
      c('[Agree to return for the shared song.]', flags=("gesmerha.verse_kept", "gesmerha.song_shared"))),
], "gesmerha.story_kept")

s("the_evening_answer", "A voice among the others", '"Is there a place for me at the singing?"', [
    n("start", "Gesmerha", '''{n}There is a place, and Gesmerha has saved it by laying her shawl across the seat. She tells you to put the shawl into her hands rather than moving it somewhere she will have to search.{/n}
"I have already lost an argument about where to sit," she says. "I will not also lose my clothes."
{n}A few people have gathered beside the workshop. Vesk's brother has brought the straps from his cart to mend while he listens. Runa calls this a discourtesy. He answers that he will enjoy the song less if his bedding falls into a ditch tomorrow.{/n}
"A useful audience," Gesmerha murmurs. "They may prevent us becoming solemn."
{n}She turns toward your shoulder at the sound of your reply.{/n}
"Dera wanted me to begin. I thought she should. We have settled on Runa, who was already singing while we discussed it."
{n}The first verse rises over the scrape of an awl. Gesmerha waits for the answering line, then enters without hesitation. You follow. Her knee shifts against yours when you come in too early, and her mouth bends around the next word.{/n}''',
      c('[Listen for Dera\'s separate answer.]', "answer", requires=("gesmerha.song_answer",)),
      c('[Join the version they agreed to share.]', "shared", requires=("gesmerha.song_shared",)),
      c('"I cannot stay for the song. I am sorry."', abort=True)),
    n("answer", "Narrator", '''{n}The old song ends with Runa holding the last note longer than anyone else. Dera waits. She does not begin until the cart straps have been set down and the listeners have stopped talking over their cups.{/n}
{n}Her answer follows the traveler who stayed beyond the second ford. It has no marvels. There is a landlord who asks too much, a roof that leaks, and a neighbor who finally learns to pronounce the traveler's name. The returning line is the familiar one, with a single changed word.{/n}
{n}Gesmerha hears the change before you do. Her hand tightens on the shawl. On the next repetition, she joins it.{/n}
"I could not make the roof rhyme," Dera confesses when she finishes.
"Roofs seldom cooperate," Gesmerha says. "Keep it."
{n}Runa asks about one line that sounds like a complaint against the people at home. Dera says it is. The answer unsettles the listeners more than the song did. Vesk's brother eventually remarks that he would rather send a complaint than be forbidden to send anything until he was happy.{/n}
{n}The discussion continues over the unmusical business of his departure. Dera has been heard separately, and several people remember her version more readily than the older song. Runa notices. She does not pretend to be pleased.{/n}''', c('[Stay while the departing traveler says his goodbyes.]', "after")),
    n("shared", "Narrator", '''{n}At the changed line, Runa hesitates. Dera keeps singing. Gesmerha comes in beside her, and the rest follow a little raggedly. The travelers know the road home; the song does not bring them back before they have chosen to return.{/n}
{n}Vesk's brother sets the straps down to join the last verse. He sings the old words once, stops, and tries again. By the end he has learned enough to carry the new line with him.{/n}
"That was shorter than I remember," he says.
"You are welcome," Dera answers.
{n}Runa objects that a song should not be praised for ending. Gesmerha asks whether she would prefer the departure delayed until they have performed every verse anybody can remember. Runa says she might.{/n}
{n}The laughter is affectionate, but Dera grows quiet when two listeners praise Gesmerha for improving the song. Gesmerha corrects them by name. One apologizes; the other merely asks Dera to sing the changed line again. She does, without smiling.{/n}
{n}They have a song the group can use. It will take more than a single correction for everybody to remember whose voice altered it.{/n}''', c('[Stay while the departing traveler says his goodbyes.]', "after")),
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
"We shall ask Runa," she says. "And I shall tell her why. She deserves the pleasure."
{n}The experiment has given you a joke, not a recovered account. Gesmerha sings the spoon into the verse once more, this time entirely with her own voice.{/n}''', c('[Offer your arm for the short walk back to her bench.]', "close")),
    n("close", "Gesmerha", '''{n}She rests her hand above your elbow. At the change in ground you tell her where the low step begins. She knows it, but asks whether the cups have all been moved out of the way. You check before answering.{/n}
"I like having you here when other people are speaking," she says. "You sound different when you do not think you are being listened to."
"What did I sound like?"
"Pleased. Occasionally early."
"I was following your lead."
"Then I shall have to find another excuse."
{n}At the bench she lets go of your arm and turns to face you.{/n}
"Come when I have no singers expected. I have been thinking about the afternoons we have kept for ourselves. There is something I would like to ask while nobody is waiting for the answer to rhyme."''', c('"I will come."', flags=("gesmerha.singing_kept",))),
], "gesmerha.verse_kept", delay=48)

s("what_she_asks", "The question without a chorus", '"You wanted an afternoon without singers."', [
    n("start", "Gesmerha", '''{n}Gesmerha has put her tools away. The game remains on a shelf within reach, but no pieces have been set out. She has left the afternoon empty on purpose.{/n}
"Dera accepted two afternoons," she says. "She named a price and then began apologizing for it so quickly that I nearly offered less out of habit. I accepted before either of us could become sensible."
"And the tools?"
"They will wait. I am allowed to want more than one thing and buy only one of them."
{n}She pats the clear place beside her. When you sit, she asks whether your sleeve is caught beneath the edge of her shawl. You free it before she draws the wool around herself.{/n}
"I have also asked her to sell a small batch of her own work. Away from my bench. She said yes much faster to that."
"Does that trouble you?"
"A little. I wanted to be the person she would choose to learn from. She still has things to learn that I cannot teach. I should like to dislike that less than I do."
{n}Her shoulder settles back against the wall.{/n}
"There. My confession of the afternoon. Yours may be less respectable if you prefer."''',
      c('[Tell her you have been looking forward to this private hour.]', "romance", requires=("gesmerha.courting",)),
      c('[Ask whether she still wants to explore what might be between you.]', "slow", requires=("gesmerha.slow",)),
      c('[Tell her something you have been saving for your friend.]', "friend", requires=("gesmerha.friendship",)),
      c('"I want to hear this properly. May I come back when I can stay?"', abort=True)),
    n("romance", "Gesmerha", '''"So have I. Rather more than was convenient. Yesterday someone brought me a difficult piece and I found myself wishing it would belong to somebody else for an hour."
"A serious complaint."
"I did finish it. I am not ready to become entirely irresponsible."
{n}She holds out her hand. You meet it, and her thumb moves along the side of yours.{/n}
"I want to be your lover," she says. "I have tried saying it more elegantly while you were elsewhere. Every attempt made it harder to tell what I meant."
{n}She pauses, giving you time to answer without releasing your hand.{/n}
"I do not mean that you should leave your road and live at my bench. I do mean that I want to know whether you wish to come here with the same hope I have when I hear you arrive."
"What hope?"
"That we shall want each other when the talking stops. And still have something to say afterward."
{n}Her fingers tighten briefly around yours.{/n}
"That is the question. I would rather hear your answer than any of my elegant inventions."''',
      c('"I want that too. I want you."', "terms"),
      c('"I care for you, but I am not ready for that. Can we keep our slower pace?"', "wait"),
      c('"My feelings have changed. I would like to stay your friend, if you can welcome that."', "friends")),
    n("slow", "Gesmerha", '''"Yes. I do. I thought I should say it before making a joke. I have a very good one prepared, but it might obscure the answer."
{n}She turns her hand palm upward on her knee.{/n}
"I would like to kiss you. I would like to discover whether that makes the next silence comfortable or alarming. I would also like you to come back if the answer today is still that you need time."
"You have thought about this."
"Frequently. It has done very little to make me composed."
{n}She laughs under her breath, more at herself than at you.{/n}
"I am not offering patience as a way to collect a debt. I know what I want. I am asking what you want, now that we have had more than one afternoon to consider it."''',
      c('"I want to begin being your lover. We can discover the pace together."', "terms"),
      c('"I still need time. I want our afternoons to continue."', "wait"),
      c('"I know now that I want friendship. I should say so plainly."', "friends")),
    n("terms", "Gesmerha", '''"Then I shall stop preparing speeches for a refusal. I had accumulated several."
{n}She moves closer. Before she leans into you, she asks where your shoulder is, then finds it with the back of her fingers.{/n}
"There is one thing to discuss before I become agreeably distracted. I cannot make myself the whole of your life. I would not enjoy the occupation. If you love someone else, tell me when it matters to what you and I have promised. I will do the same."
"You are not asking for exclusivity?"
"I am asking not to discover that my own evenings have been promised away on my behalf. I want room for us that actually exists."
{n}Her hand rests against your collar.{/n}
"And I do not want a place in your household that requires me to leave mine without thinking. Perhaps I shall want to travel. Perhaps I shall be impossible to move. You may ask. You may not pack my tools while I am answering."
"That sounds difficult to mistake."
"People have mistaken clearer instructions. I have spent a life working with customers."
{n}She smiles, then waits for your answer to the terms she has actually offered.{/n}''',
      c('"Time we choose, honest answers, and no promises made for each other. Yes."', "touch"),
      c('"I cannot offer that honestly yet. Let us keep taking our time."', "wait")),
    n("touch", "Gesmerha", '''{n}You tell her where your face is, and she raises her hand to your cheek. Her thumb rests beside your mouth. She comes close enough for you to feel her breath before she asks the small, final question.{/n}
"May I?"
{n}At your answer she kisses you, gently at first. Then she draws back just far enough to murmur that she has thought about this more than was wise, and you feel her smile before the next kiss.{/n}
{n}Her hand slips to the back of your neck. When you shift, she asks you to wait while she frees the shawl from beneath her hip. The interruption leaves both of you laughing. Once the wool is out of the way, she settles closer with considerably less ceremony.{/n}
"I would like you to stay," she says. "We can close the door. Or remain here until the light changes. Tell me what would please you."''',
      c('"Close the door. I would like the rest of this afternoon with you."', "private"),
      c('"Here, today. Hold me a little longer."', "hold")),
    n("private", "Gesmerha", '''{n}You close the workshop door and tell her when the latch has caught. She takes your offered hand, then leads the short way herself, warning you about the low crosspiece that she no longer needs to think about.{/n}
"I refuse to begin by explaining you to a healer," she says.
{n}Inside, she tells you where to put your things. You tell her where you have put them. The ordinary exchange becomes unexpectedly intimate when she reaches for you and finds you exactly where you said you would be.{/n}
{n}There is time to ask, to hesitate, to laugh and begin again. The sounds beyond the door continue without requiring an answer. When you later sit together with her hair loose against your shoulder, she takes your hand and guides it away from a tender place beside the old scars.{/n}
"Here is better."
{n}You follow her guidance. She sighs, comfortable, and asks whether you are hungry.{/n}
"Eventually," you say.
"An excellent answer. I can improve on eventually. At present I am unwilling to move."''', c('[Stay until she is ready to get up.]', "road")),
    n("hold", "Gesmerha", '''"Come nearer, then. I have developed ambitions for this bench."
{n}She adjusts your arm so that its weight rests comfortably across her shoulders. You ask before touching her hair. She says yes, then catches your fingers to show you where the tie is tangled.{/n}
"Do not pull. It has already won one argument today."
{n}You loosen the knot. Her hair falls against your sleeve, and she lets out a long breath. For a while you sit without finding another subject. When someone passes outside, she calls a greeting and tells them the tools are put away until tomorrow.{/n}
"Was that true?" you ask.
"It is now."
{n}She tilts her face toward your voice. The next kiss is unhurried. After it, she settles against you again, one hand resting over yours as though it has found a place it intends to remember.{/n}''', c('[Stay while the afternoon grows quiet.]', "road")),
    n("road", "Gesmerha", '''"When you leave for somewhere I cannot reach," she says after a while, "do not make the goodbye impressive. Tell me what you can tell me. Let the rest remain uncertain."
"You expect a long absence?"
"I expect that your road will not consult my calendar."
{n}She lifts your joined hands and kisses your knuckles.{/n}
"If I can send word, I will. If no word comes, it will not be a message hidden inside the silence. I want you to remember that."
"And when I return?"
"Ask whether I still want you here. I expect to say yes with very little dignity. But come and ask me."
{n}She rests your hands in her lap again.{/n}
"For today, you are here. There is no reason to begin being absent early."''',
      c('"Then today is ours."', flags=("gesmerha.campaign_kept", "gesmerha.lover", "gesmerha.committed"))),
    n("wait", "Gesmerha", '''"Yes. I can keep wanting an answer without pretending we have reached it."
{n}She sits back, leaving a little more room between you. Her disappointment is visible in the care with which she straightens the edge of her shawl.{/n}
"I shall not ask every time you come. If something changes, say it. I will not become expert at interpreting how long you keep your hand on a cup."
"I would rather speak."
"Good. We shall both be spared a tedious education."
{n}She asks you to bring the game down. Before you begin, she speaks again.{/n}
"If your travels keep you away, do not treat my patience as a promise to remain exactly as I am. I may have another answer by the time you return. You may too. We can still ask each other."
{n}She finds her pieces by touch and arranges them within reach.{/n}
"Now. Show me whether you have learned anything about that outer row."''',
      c('[Play, and leave the larger answer open.]', flags=("gesmerha.campaign_kept", "gesmerha.campaign_slow"))),
    n("friends", "Gesmerha", '''{n}She draws her hand back into her lap. For a while you listen to the ordinary sounds outside the workshop.{/n}
"I can welcome the truth," she says. "Friendship may require a little time to catch up with it."
"Would you like me to go?"
"Not abruptly. I would like to finish this afternoon without either of us behaving as though the bench has caught fire."
{n}She reaches for her shawl and folds it over her knee.{/n}
"Tell me something about the road you will take next. Something you actually know. I am tired of making plans from the things people hope will happen."
{n}You tell her what you can. She asks a practical question, then another. Before you leave, she says she would like to hear more when you return. There is warmth in it, though the ease will take longer.{/n}''',
      c('"I will come back as your friend."', flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends"))),
    n("friend", "Gesmerha", '''{n}You tell her what you have been saving. She listens with the pleased attention of someone who knows the account was meant for her before the telling began.{/n}
"I shall miss this when you are elsewhere," she says. "Not only the news. People bring news when they want me to do something about it. You have occasionally brought a story that required nothing except a place to sit."
"Occasionally?"
"I am leaving myself room to complain later."
{n}She asks you to bring the game down. Before you start, she tells you that Dera wants to learn the longer song, including the verses nobody had time to sing. Runa has offered to help. The proposed afternoon is likely to become an argument, and Gesmerha sounds almost eager for it.{/n}
"When you return, ask what we have accomplished. If I say that everybody agreed, you may assume I am concealing something."
"I will remember."
"Remember to come back, if you can. The rest I can remind you of."''',
      c('[Play another game with your friend.]', flags=("gesmerha.campaign_kept", "gesmerha.campaign_friends"))),
], "gesmerha.singing_kept")

s("the_voice_at_court", "The voice that came back", '"Before you go, may we speak about something of our own?"', [
    n("start", "Gesmerha", '''{n}Gesmerha has come to court with the road still on her clothes. You have heard what she intends for her people. At your question she turns toward you, and the careful formality of her voice gives way.{/n}
"Yes. I hoped you would ask. There are a great many people in this room who appear to be waiting for permission to make you useful again."
{n}You ask the nearest attendants for a little space. They withdraw far enough to leave the conversation to you. Gesmerha remains beside the place where she has given her report; no one needs to hurry her through an unfamiliar doorway.{/n}
"Tell me how near you are."
{n}You answer and offer your hand. She takes it, drawing you a little closer.{/n}
"There. I wanted something more convincing than a rumor. Your voice was a good beginning."
{n}Her fingers close firmly around yours before relaxing.{/n}''',
      c('"I missed you. I missed being wanted for myself."', "lover", requires=("gesmerha.lover",)),
      c('"I have thought about the answer we left open."', "slow", requires=("gesmerha.campaign_slow",)),
      c('"I missed my friend."', "friend", requires=("gesmerha.campaign_friends",)),
      c('"I cannot speak privately now. I am glad you came."', abort=True)),
    n("lover", "Gesmerha", '''"Then you should know I was very angry with the silence. It was easier than being frightened of it all day."
"I could not send you word."
"I know what we said. I remembered it even when I disliked it."
{n}She raises your hand to her mouth and kisses it. The gesture is brief, but when she lowers it she keeps hold of you.{/n}
"Do you still want me here?" you ask.
"Yes. There. Almost no dignity at all, as promised."
{n}Her laugh trembles once. She takes a breath and tries again.{/n}
"I have no private room to offer you today, and too many people depending on when I leave. I would like to stand with you for a while without pretending this handclasp is an official courtesy."
"So would I."
"Good. Let them be patient. I have acquired an impressive amount of practice."''', c('[Ask what she has carried with her.]', "songs")),
    n("slow", "Gesmerha", '''"So have I. Several answers, depending on the day. None of them was improved by not knowing whether there would be anyone left to hear it."
{n}She rubs your knuckles once with her thumb, then loosens her hold.{/n}
"I am pleased you are here. I am not ready to make this hurried meeting answer for all the days between."
"We do not have to."
"No. We can begin by speaking to the people who came back, rather than the people each of us kept rehearsing a conversation with."
{n}She asks whether the handclasp is welcome. At your answer she keeps your hand in hers.{/n}
"There. Something simple enough to decide today. I have missed simple questions."
"You did not usually find simple answers."
"You remember me accurately. That is a promising beginning."''', c('[Ask what she has carried with her.]', "songs")),
    n("friend", "Gesmerha", '''"And I missed hearing a story whose ending did not require me to find beds for everybody in it."
{n}She presses your hand before releasing it. Her shoulders ease a little.{/n}
"I am pleased you are alive," she says. "It sounds absurdly small beside everything people have been saying. I find it enough to occupy me."
"It is enough for me too."
"Then we shall spare each other a speech. I have one for the people waiting to travel with me, and I do not want to waste all my convincing words in the same room."
{n}She asks whether you have eaten. At your answer she observes that returning from the dead ought to improve a person's authority over mealtimes, then admits she has missed her own.{/n}
"We remain excellent advisers to everyone except ourselves."''', c('[Ask what she has carried with her.]', "songs")),
    n("songs", "Gesmerha", '''{n}At your question she touches the small bundle at her side.{/n}
"Clothes. A few tools. A game that takes more room than I intended."
"You brought it?"
"I have had cause to learn which things I reach for when somebody says there is little time. The answer was not entirely sensible."
{n}She tells you that Dera is with the traveling party. Runa is not. Her daughter has been singing softly while they stop at night, sometimes the same few lines until someone asks for a different tune. Gesmerha does not supply an account of Runa's last hours. She was not there.{/n}
"Dera asked me to remember the version I used to argue with," she says. "I could remember most of it. She supplied a line I had forgotten. Then we disagreed about another. That was a relief neither of us expected."
{n}Her hand rests on the bundle's knot.{/n}
"I have not told her that she must preserve every song now. There are mornings when getting up is work enough. If she sings, I answer. When she stops, I let her."
"And your own singing?"
"Some nights. Not all of them."
{n}She shifts the bundle away from her foot.{/n}
"I am keeping the game. That much I have decided."''',
      c('[Remember the two trays made after the wood split.]', "trays", requires=("gesmerha.grain_missed",)),
      c('[Remember the narrow board and the names of its rows.]', "board", forbids=("gesmerha.grain_missed",))),
    n("trays", "Gesmerha", '''"Two awkward pieces to pack," she says. "I wrapped them separately. Dera asked why I had not made something that folded. I told her I had entertained that ambition once."
{n}Her mouth curves into a brief smile.{/n}
"We played on a cloth beneath one of them. It still needs folding twice where the ground is uneven. I considered carving new feet. Then we had to move. The cloth was faster."
"Does Dera defend the outer row?"
"She attacks it. I told her she was not the first person to make that particular mistake. She improved before I had finished enjoying myself."
{n}Gesmerha's fingers trace the shape of the bundle through its wrapping.{/n}
"It has done what I wanted. People hold it before they ask what it means. Sometimes they never ask. I am grateful for those evenings."''', c('[Return to the future she has described for her people.]', "future")),
    n("board", "Gesmerha", '''"Dera thinks I made the rows too narrow," she says. "I told her they were made for people willing to learn where their fingers belonged. She told me that sounded expensive."
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
"Not every person will want the same thing. Dera wants to sell work somewhere her mother was not already known. I told her that was a reasonable ambition. I managed to sound as though I meant it before I had quite caught up with the words."
"Will you ask her to stay?"
"I have asked her to help while we travel. I have not asked for the rest of her life. If I want her to return, I can make something worth returning to."
{n}Gesmerha straightens the tie at her wrist.{/n}
"That will take longer than an encouraging speech. I am trying to remember it when an encouraging speech seems easier."''', c('[Ask how she wants this meeting to end.]', "choice")),
    n("choice", "Gesmerha", '''"With a little time still belonging to us," she says. "I have given the report. I can spend a few more breaths deciding what I want to remember of your welcome."
{n}She turns toward you, waiting for you to speak before reaching out.{/n}''',
      c('"I still choose the time we promised each other. May I kiss you before you go?"', "kiss", requires=("gesmerha.lover",)),
      c('"Stay beside me a moment. Let us keep this much without hurrying the rest."', "quiet"),
      c('"I cannot keep courting you honestly. I want you to hear that from me."', "part", requires=("gesmerha.lover",))),
    n("kiss", "Gesmerha", '''"Yes. Come here, then. I will not attempt to find your mouth by judging the silence."
{n}You tell her where you are. Her hand finds your cheek, and she kisses you with the same deliberate warmth you remember. This time she does not laugh when you part. She rests her forehead against yours for a breath, then another.{/n}
"There," she says softly. "I wanted that. I am pleased I asked for time."
{n}When she draws back, you help settle the bundle where she can lift it without catching the strap. She asks you to describe the space ahead before she turns toward the waiting attendants.{/n}
"You still owe me an ordinary story," she says. "Not today. Today I am willing to be impressed by your arrival."
{n}She leaves the next meeting unpromised. The affection she has chosen to give you is warm against your mouth as the room becomes a court again.{/n}''',
      c('[Let her finish her native audience when she is ready.]', flags=("gesmerha.reunion_kept", "gesmerha.reunion_lovers"))),
    n("quiet", "Gesmerha", '''{n}You stand together while the court gives you what little quiet it can. She asks about one familiar person, and you tell her what you know. When your answer reaches its limit, she accepts it without asking you to make the missing part kinder.{/n}
"I am glad I came," she says. "Whatever happens after I leave, I wanted to have heard you answer me."
{n}You tell her the same. She holds your hand briefly, then asks where the attendants are waiting. You describe the clear space between her and them.{/n}
"We should let them earn their patience," she says. "I have not finished being inconvenient for the day."
{n}Her smile returns as she lifts the bundle. There is still business to conclude before she goes. You have had a few minutes that belonged to neither the business nor the road.{/n}''',
      c('[Return to the audience together.]', flags=("gesmerha.reunion_kept", "gesmerha.reunion_quiet"))),
    n("part", "Gesmerha", '''{n}Her hand becomes still. She lets go of yours and takes a breath before answering.{/n}
"Thank you for saying it. I should have disliked learning it from the way everybody avoided the subject."
"I did not want to hurt you here."
"There is no place I would have preferred. We are here. That will have to serve."
{n}She finds the strap of her bundle and smooths it between her fingers.{/n}
"I meant what I offered you. I shall not pretend otherwise because the answer has changed. I will need time before I know whether I want another of our afternoons."
"I understand."
"I hope so. For now, let us finish the matters I came to discuss. The people waiting for me should not have to guess which silence belongs to them."
{n}You tell her where the attendants are. She turns toward them with her bundle in hand.{/n}''',
      c('[Respect her request and return to the audience.]', flags=("gesmerha.reunion_kept", "gesmerha.closed"))),
], "gesmerha.campaign_kept", chapter=5)


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("gesmerha.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Gesmerha")], Relationship="gesmerha", last=99,
        requires=("gesmerha.campaign_kept", *requires), forbids=forbids))


ending("living_reunion", "An answer kept", '''{n}At court, Gesmerha and the Commander had found time for a private answer. It did not settle where the clan would live, or give either traveler possession of the other's days. Gesmerha carried the game away with her, its familiar edges packed among the things she had chosen to keep.{/n}
{n}The next stretch of road was not made shorter by remembering the welcome. But when she told Dera that the Commander had asked about the songs, she found herself smiling before she reached the end of the account. She refused to improve the story when Dera asked for details. Then she supplied one anyway.{/n}
{n}No date had been fixed for another meeting. The words actually spoken remained a better comfort than a promise invented after the parting.{/n}''',
    requires=("gesmerha.reunion_kept",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice"))
ending("unmet_again", "The afternoon remembered", '''{n}The Commander had shared work, songs and private afternoons with Gesmerha in Wintersun. The later road did not bring them another meeting that could answer all the questions left at her bench.{/n}
{n}There had been a woman laughing over a song about a caller at the door. There had been a difficult discussion about what each could honestly offer, and an answer given without hiding behind the Commander's title. Those memories kept their particular warmth, including the awkward parts that a polished account might have omitted.{/n}
{n}What Gesmerha would have said at another meeting remained hers to say. The Commander could remember the last afternoon without supplying that missing conversation.{/n}''',
    forbids=("gesmerha.reunion_kept", "gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice"))
ending("loss", "The answering voice", '''{n}Gesmerha died. Neither the game nor the songs could be made to answer in her place. People who remembered her sometimes disagreed about a line she had sung, and for a moment the argument left room for the correction that would not come.{/n}
{n}The Commander's memories were less orderly than a tribute. Her irritation at being interrupted. Her hand waiting to be met. The exact pause before she admitted wanting something. The days at the bench had belonged to a woman with unfinished work and wants of her own.{/n}
{n}Her death did not make those days a completed life. The next question remained unasked.{/n}''', requires=("gesmerha.dead",))
ending("changed", "A welcome withdrawn", '''{n}The Commander became someone Gesmerha could no longer welcome on the strength of an earlier afternoon. She had spent too long among reassuring appearances to take a familiar voice as sufficient reason to set aside her judgment.{/n}
{n}She kept the memory of what she had chosen. She also kept the right to refuse what came afterward. When she spoke of the old visits, she did not change every pleasant hour into a warning she claimed to have understood at the time. There had been pleasure. The door could still close.{/n}''',
    requires=("inhuman",), forbids=("gesmerha.dead", "gesmerha.closed"))
ending("demon", "No borrowed welcome", '''{n}Gesmerha would not let the Commander's demonic path borrow the welcome she had once offered a traveler at her bench. She knew too much about a pleasing voice making cruelty sound necessary. The earlier songs and private hours gave the Commander no authority over her answer.{/n}
{n}She remembered wanting that company. She did not have to forget the wanting in order to refuse what it had become.{/n}''',
    requires=("demon",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman"))
ending("devil", "A promise is not a chain", '''{n}The Commander's infernal path did not acquire Gesmerha along with its other claims. She had offered time she could choose, not a pledge whose wording might be turned against her. The things she had said beside the bench remained part of her life. They were not permission to decide the rest of it.{/n}
{n}She had no appetite for debating that distinction with a power that profited by misunderstanding it. Her refusal was short.{/n}''',
    requires=("devil",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon"))
ending("ascent", "Beyond the next verse", '''{n}News of the Commander's ascent made Gesmerha fall silent. Then she asked the messenger to repeat what was known, without improving the account for her benefit.{/n}
{n}She had known someone who could arrive with an ordinary story and sit down to lose a game. She did not know whether a god would still want such an afternoon. Wanting the answer gave her no certainty about it.{/n}
{n}Sometimes she sang the caller's song with a new hesitation before the answering line. At other times she finished it briskly, as though the person at the door ought to have learned some patience. She made no announcement that a silence had replied.{/n}''',
    requires=("ascended",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil"))
ending("sacrifice", "The words already spoken", '''{n}Gesmerha heard what the Commander's sacrifice had accomplished. She asked one question about the end, then declined the offer of a longer account. She would ask for it when she wanted it.{/n}
{n}For a time the caller's song was impossible to finish. The answering line came too easily to her mouth and stopped there. Later she could sing it again, though not always when someone asked.{/n}
{n}She remembered the words actually spoken between them. She added no promises to them and erased none because keeping them had become painful. There had been time freely given beside her bench. She wanted more of it, and there was no one left to ask.{/n}''',
    requires=("sacrifice",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended"))
ending("aeon", "A song in another history", '''{n}In the history remade without the Worldwound, no returning Commander came to Gesmerha with the same story. The village's deception, the investigation and the afternoons that followed had not led two people to that bench.{/n}
{n}Whatever songs Gesmerha knew in the altered world, they did not owe their ending to shared afternoons erased with their cause. Her life belonged to that world. The vanished traveler had no answer to claim from it.{/n}''', owner="AeonEpilogue")


def integrate(payload):
    payload.setdefault("Etudes", {}).update(ETUDES)
    payload.setdefault("SeenCues", {}).update(SEEN_CUES)
