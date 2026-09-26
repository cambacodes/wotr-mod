"""Irabeth's individual campaign; all new cases and private events are authored.

Native marriage, morale and actor availability remain read-only.
The shared route retains its own history and ending arbitration.
"""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"
ANEVIA = "b5e867e13503c6f41bb1316705efb4a2"
I_ANSWERS = "871af36f2ab2b1f40b5de77976c54276"
A_ANSWERS = "33960c7f7af40cd43b7f801a76c87a0b"
RELATIONSHIP = dict(
    Title="Irabeth: The name she would make",
    Description="Irabeth has a difficult case and an invitation of her own. Her marriage, her judgment and the life she wants beyond the war all matter to what follows.",
    Objective="Make time for Irabeth",
    Guidance="Speak with Irabeth in Drezen. Keep the appointments you choose, and speak with Anevia when Irabeth asks. A private relationship does not require a shared romance.",
    StartedFlag="irabeth.started", ClosedFlag="irabeth.closed", CommittedFlag="irabeth.committed",
    UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"],
    FailureFlags=["irabeth_dead", "irabeth_gone", "inhuman"])
SCENES = []


def s(identity, title, entry, nodes, *, requires=(), forbids=(), any_of=(), chapters=(3, 5), delay=24, owner="Irabeth", remote=False):
    item = scene("irabeth." + identity, title, owner, min(chapters), entry, nodes,
        requires=requires, forbids=("closed", "irabeth.closed", "inhuman", *forbids),
        delay=delay, last=max(chapters), optional=True, Relationship="irabeth",
        Chapters=list(chapters), RequiresAny=list(any_of), Remote=remote)
    if not remote:
        wife = owner == "Anevia"
        item.update(Areas=[DREZEN], AnswerLists=[A_ANSWERS if wife else I_ANSWERS],
                    ContactUnit=ANEVIA if wife else IRABETH)
        item["Forbids"].append("anevia_away" if wife else "irabeth_away")
        if wife:
            item["Forbids"].extend(["anevia_dead", "anevia_gone"])
    for page in item["Nodes"]:
        if not page["Portrait"]:
            page["Portrait"] = "Anevia" if page["Speaker"] == "Anevia" else "Irabeth"
    SCENES.append(item)
    return item


s("a_name_on_the_list", "A name she had written herself",
  '"Irabeth, what is that list? You looked pleased with it before I arrived."', [
    n("start", "Irabeth", '''{n}Irabeth folds the lower half of a page beneath her palm. The visible half contains six names, each followed by a number. Hers is fourth. Someone has drawn a small crown above it in charcoal.{/n}
"That depends on whether you are about to add an obligation to it."
{n}She looks surprised by her own answer. Then she removes her hand.{/n}
"Forgive me. No, don't. I meant the question."
{n}The page announces a recitation at a disused storehouse. Each participant has ten minutes. A line at the bottom forbids appeals for money, military announcements and the use of live animals. Irabeth follows your glance to the last restriction.{/n}
"I asked. There was a goat. Apparently the performance improved when it escaped."
{n}Her name is written in her own firm hand. She has put no title before it.{/n}
"I put myself down for a piece I used to know. Then spent a considerable time deciding whether that was an absurd thing to do."''',
      c('"Which piece? I would like to hear it."', "piece"),
      c('"Who drew the crown?"', "crown"),
      c('[Give her time to prepare. Ask another day.]', abort=True)),
    n("crown", "Irabeth", '''"The woman arranging it. Dema. I asked whether she was making a joke about my rank. She said she was making a joke about my handwriting."
{n}Irabeth holds up the page. Every other name leans one way or another. Hers stands above the number like a guard who expects trouble from it.{/n}
"She asked me to write 'eggs' beneath it. I did. It looked like an order to take a hill."
"Did you object?"
"I laughed. She seemed relieved. That annoyed me more than the crown."
{n}She folds the list again, leaving her name visible.{/n}
"I would like to be good at this. There. The unreasonable part. If I wanted merely to fill ten minutes, there would be no difficulty. I have filled longer intervals by explaining where to store spare buckles."
{n}Her mouth curves.{/n}
"I have even received applause. From a man who thought I had finished."''', c('"Then choose something you want them to hear."', "piece")),
    n("piece", "Irabeth", '''"A boast. A caravan guard arrives at a duke's hall to claim a reward. He describes every creature he fought on the road. The duke asks why the caravan is three weeks late."
{n}She clears her throat, broadens her stance and gives you the guard's first line in a resonant voice.{/n}
"'My lord, the beasts upon that road have heard my name and fled.'"
{n}Her expression changes. The duke is thinner, colder, and considerably less impressed.{/n}
"'A pity. Had they stopped to eat you, I might have received my wool.'"
{n}She breaks off with a laugh.{/n}
"It was better when the woman who taught me did it. We were paid to escort a wagon through the River Kingdoms. She could make three men arguing out of one mouth. I can remember the words, but I keep making the guard sound as though he is delivering evidence."
"Perhaps he believes himself."
"He has slain a serpent longer than the road. Even his own boots ought to doubt him."
{n}Irabeth looks down at the list, then back at you.{/n}
"Will you hear a little? You may say it is poor. That would be useful. But please do not begin by saying it is brave of me to try."''',
      c('"Give me the guard who believes himself."', "guard", flags=("irabeth.boast_guard",)),
      c('"Let the duke be the ridiculous one. I would enjoy that."', "duke", flags=("irabeth.boast_duke",))),
    n("guard", "Narrator", '''{n}Irabeth begins again. This time the guard is tired. He is hungry, his boots leak, and every beast grows larger when the duke mentions reducing the fee. She discovers a pause between the serpent and the dragon. You can almost watch the guard decide that the serpent has not done enough work.{/n}
{n}By the dragon, you are laughing. Irabeth looks at you and loses the next line.{/n}
{n}"Don't stop," you tell her.{/n}
{n}"I don't know what follows."{/n}
{n}"Neither does he."{/n}
{n}She straightens with immense dignity.{/n}
{n}"'The beast was so large, my lord, that I could see the weather change across its back.'"{/n}
{n}It is a dreadful line. Her pleasure in it makes you laugh harder. She holds the solemn expression until you recover, then bows with one hand spread across her heart.{/n}
{n}"I will have to keep that. You have made it impossible to discard."{/n}''', c('"It earned its place."', "interest")),
    n("duke", "Narrator", '''{n}The duke begins with a finger raised. He has a correction for every creature. Serpents are measured by girth. Dragons are not normally found near toll bridges. A guard whose contract specifies wolves should have asked permission before encountering anything larger.{/n}
{n}Irabeth gives him a small, irritated cough. When she reaches the question of wool, she looks at an imaginary clerk, waiting for someone else to explain why the world has failed to arrange itself properly.{/n}
{n}"I have met him," you say.{/n}
{n}"So have I. Three times. Under different names."{/n}
{n}She returns to the guard. This time he has the exhausted courtesy of a man who has spent three weeks hoping to be paid by someone with less imagination than a wolf.{/n}
{n}The exchange runs faster. She forgets a line, substitutes a complaint about damp socks and makes herself laugh.{/n}
{n}"That is not in the piece."{/n}
{n}"It should be."{/n}
{n}"I shall blame you if anyone remembers the original."{/n}''', c('"I will accept the accusation."', "interest")),
    n("interest", "Irabeth", '''{n}She sits at last. The chair creaks beneath a movement she has not thought to make carefully.{/n}
"I used to do that while walking. Recite things, I mean. It passed the time between one very similar stretch of road and the next. When I arrived in Kenabres I began remembering how every word might be repeated."
{n}She stretches one leg and looks at the scuffed toe of her boot.{/n}
"There were good reasons. A woman who has been called a stupid brute does not improve matters by performing a stupid brute in an inn. I learned that early. Then I discovered that being faultless was no protection either. They could always dislike how pleased I looked with myself."
{n}She glances up.{/n}
"I am not asking you to answer them for me. I signed the page. I would like the evening. I would particularly like the part where I have done it well and can enjoy being told so."
{n}The admission brings color into her cheeks. She leaves it there.{/n}''',
      c('"I would like to see that look on your face."', "flirt", forbids=("anevia_dead", "anevia_gone")),
      c('"I would like to see that look on your face."', "careful", requires=("anevia_dead",)),
      c('"I would like to see that look on your face."', "careful", requires=("anevia_gone",), forbids=("anevia_dead",)),
      c('"I like your company, Irabeth. I would like more of it."', "company"),
      c('"I hope the evening goes well. Let us keep this friendship."', "friend")),
    n("flirt", "Irabeth", '''"You are looking at it already."
{n}For a moment she lets the answer stand. Then her eyes fall to her ring.{/n}
"I know what you mean. I am pleased by more than your opinion of my recitation."
{n}She lays the list between you.{/n}
"Anevia is my wife. I love her. Whatever you and I might decide, that is a person and a marriage, not a difficulty for us to solve in her absence."
{n}Her thumb rests beside her written name.{/n}
"I would like to see you again. Without making every pleasant minute into a concealed appointment. Let us begin there. If you mean something more, we will have to say it plainly when we have had time to consider what we are asking."''', c('"I mean the invitation. We can take the time."', "finish", flags=("irabeth.interest",))),
    n("careful", "Irabeth", '''"You are looking at it already."
{n}Her smile softens. Her gaze falls briefly to her ring.{/n}
"I am pleased by your attention. I also have a great deal to think about before I could answer a more private invitation. Anevia belongs in that conversation. What has happened to us cannot be made simpler by my enjoying a compliment."
{n}She looks back at you.{/n}
"For now, come again because you enjoy my company. If we ask for more, we will have to speak plainly about the life I actually have."''', c('"I would like to come again."', "finish", flags=("irabeth.interest",))),
    n("company", "Irabeth", '''"So would I."
{n}Her answer comes promptly, followed by a small, pleased uncertainty about where to put her hands.{/n}
"I have been imagining the audience. It keeps becoming a collection of people who look as though they have something more important to do. I should like to know one person came because the performance interested them."
{n}She reaches for the list and stops before folding it out of sight.{/n}
"I can enjoy having another person to tell about something. I keep arranging my life as though everyone needs a clear military reason to stand beside me. Then I complain that I am never off duty."
{n}She looks directly at you.{/n}
"Come again. I would like the chance to discover what you talk about when I have finished talking about myself."''', c('"I will."', "finish")),
    n("friend", "Irabeth", '''"Yes. I would like that."
{n}She gives the list one final look before folding it. The crown disappears inside the paper.{/n}
"You may still laugh at the performance. I will know which lines worked, and I shall blame you for the others."
{n}When she stands, there is no apology in the movement. She has somewhere she wants to be, and a name already waiting for her there.{/n}''', c('[Keep this relationship as friendship.]', flags=("irabeth.closed",))),
    n("finish", "Irabeth", '''{n}A folded requisition waits beneath the list. She picks it up reluctantly, then frowns.{/n}
"This arrived before you. A lieutenant has impounded a wagon of cold iron. There is a dispute about who owned the load when he took it."
{n}She turns the page toward you. A small sketch shows a cart with one wheel drawn much larger than the other.{/n}
"The sketch is the owner's. She says my officer asked for the purchase agreement, and she gave him a picture because she cannot write. He has filed it as an attempt to obstruct an inquiry."
{n}Irabeth's eyes narrow.{/n}
"I know the lieutenant. He has pulled people out of places most men would not enter. He is also quite capable of deciding that a woman laughing at him must have something to hide."
{n}She places the requisition apart from the list.{/n}
"I will hear them both. You are welcome to come, if you want to see how poorly the real disputes compare with my duke. Another day. I have given this one to the guard and his dragon."''',
      c('[Leave her with the piece she chose.]', flags=("irabeth.started", "irabeth.first_hour_kept",))),
], forbids=("i_affair", "trying", "committed", "irabeth.personal_ready", "irabeth.courtship_requested"), delay=0)


s("the_seized_wagon", "Iron that belonged to somebody",
  '"You meant to hear the dispute over the cold iron."', [
    n("start", "Narrator", '''{n}The wagon stands in the headquarters service yard. Its load has been covered, but a corner of the cloth shows thick, dark bars packed into straw. A woman in a leather apron waits by the wheel. One of her sleeves is rolled above the elbow. The other is tied closed beneath it.{/n}
{n}Irabeth introduces her as Brena, a smith who brought the iron into Drezen. Lieutenant Hadran waits on the opposite side of the wagon. He has a written order, a narrow face and the patient expression of a man who believes the paper will do his arguing for him.{/n}
{n}"You may both begin by leaving the word 'obvious' out of your account," Irabeth tells them.{/n}
{n}Brena gives a short laugh. Hadran lowers his order.{/n}
{n}"I was going to say authorized, ma'am."{/n}
{n}"Then begin there."{/n}
{n}He explains that the bars were being moved after an inspection bell. The wagon's driver could produce no written bill of sale. A patrol had already found mismarked iron in another consignment. Hadran detained the load before someone could carry it out of the city.{/n}
{n}Brena listens with her head tilted.{/n}
{n}"I was carrying it to a forge. There was a forge at the end of the road. I showed him the forge."{/n}''',
      c('[Ask Hadran what connected this wagon to the false consignment.]', "officer"),
      c('[Ask Brena how she purchased the iron.]', "smith"),
      c('[Return when you can hear both accounts.]', abort=True)),
    n("officer", "Irabeth", '''"That is the point I want settled."
{n}Hadran indicates a stamped mark on one of the bars. The same mark appeared on the false load. He asked where this one had come from, and Brena laughed.{/n}
"I asked whether he expected me to smelt it myself," she says. "That was the laugh."
"You would not give a name."
"I gave two. You disliked both."
{n}Irabeth holds up a hand. Hadran presses his lips together.{/n}
"A mark may identify a supplier," she says. "It does not establish that every bar bearing it is false. What did you test?"
"The papers."
"What did you test on the iron?"
{n}He has no answer. Irabeth lets the silence run until Brena stops looking satisfied with it.{/n}
"That does not establish the opposite either. We will hear where she obtained it. Then we will inspect the material you detained."''', c('[Listen to Brena.]', "smith")),
    n("smith", "Narrator", '''{n}Brena names a factor outside Drezen and a carrier who shared the journey. She paid part in coin and part in repaired tools. The factor gave a receipt to the carrier, who kept the common road expenses. Brena expected him to arrive after her. He has not.{/n}
{n}"You understand why that troubles me," Hadran says.{/n}
{n}"I understand why it should trouble you. What you did was ask me to write it down again."{/n}
{n}She taps the side of the wagon with two fingers.{/n}
{n}"These are the things I can write. I can tell you which bar will split if you bend it cold. I can tell you the weight a hinge will bear. I told him who to ask. He handed me a pen."{/n}
{n}Irabeth takes the lieutenant's page. She reads it once, then asks Brena to repeat the two names. One is recorded incorrectly. The other is absent.{/n}
{n}"I assumed the second was an associate of the suspect," Hadran says.{/n}
{n}"She is the suspect," Irabeth replies. "You assumed a witness could be left out because he might know her."{/n}
{n}His jaw tightens. Brena looks away, unexpectedly uncomfortable with the reprimand.{/n}''', c('[Move to the covered load.]', "test")),
    n("test", "Irabeth", '''{n}Irabeth pulls back the cloth. The bars bear several shallow stamps. One is crisp. Another has been struck twice, leaving a blurred impression.{/n}
"Brena says the iron is sound. Hadran says the mark is evidence of a false shipment. I will not decide which person tells the truth by choosing whose manners I prefer."
{n}She gives Hadran the order back.{/n}
"You were right to stop a suspect load long enough to investigate it. You have kept it here for two days while repeating the same question. Those are different decisions."
{n}Brena draws a small hammer from her belt and offers it handle first.{/n}
"Pick the bar. I won't choose the good one for you."
{n}You can inspect the alloy and the altered stamps yourself. A proper assay at Brena's forge would take longer, under observation, but it would not depend on your recognizing the material at a glance. Hadran offers to arrange that escort. Irabeth does not relieve him of the task.{/n}''',
      c('[Knowledge: World 25] Examine the bars and the stamps.', check=dict(Skill="SkillKnowledgeWorld", DC=25, Success="tested", Failure="uncertain", CommanderOnly=True)),
      c('"Take a sample to the forge. Test it before either of us gives a verdict."', "assay", flags=("irabeth.iron_assay",))),
    n("tested", "Narrator", '''{n}The doubled stamp crosses a shallow scrape. Beneath it, the original mark survives at one edge. You turn the bar so both people can see. The newer mark identifies the factor, not the maker. Several lots have been sold under the same name.{/n}
{n}A cut on an existing damaged end exposes consistent material. It supports Brena's account of the load. It does not show who owned it on the road.{/n}
{n}"Then I detained good iron," Hadran says.{/n}
{n}"Apparently," Irabeth answers. "We still have the question of its purchase. You will now ask it accurately."{/n}
{n}Brena takes the bar back. Her fingers close over the old mark.{/n}
{n}"I'd like that question asked before rain gets through your cloth."{/n}
{n}Irabeth orders the wagon moved beneath the eaves. Hadran and two yard workers do it while Brena walks beside the smaller wheel, listening for a problem she can identify more readily than any of you.{/n}''', c('[Discuss the remaining evidence.]', "cost", flags=("irabeth.iron_read",))),
    n("uncertain", "Narrator", '''{n}The stamp looks familiar. You begin to identify it, then notice a second impression crossing the first. Your explanation no longer fits what is on the metal.{/n}
{n}Brena waits. Hadran looks from your face to Irabeth's.{/n}
{n}"I cannot establish it from this," you say.{/n}
{n}Irabeth nods. "Then we will use the forge."{/n}
{n}The sample is carried under escort. You wait through the preparation of a small test piece, the heat and the repeated examination. Brena does not let anyone hurry the work. The material proves sound, with a factor's stamp struck over the maker's. By the time you return, the yard is in shadow and a crew has gone home without the hinges Brena meant to finish.{/n}
{n}"Tomorrow," she tells the boy who came to collect them. "Tell your mother I know. Tomorrow."{/n}
{n}Irabeth watches him leave. The failed shortcut has cost an afternoon. She puts that afternoon into her account without enlarging it into a confession.{/n}''', c('[Discuss what remains unsettled.]', "cost", flags=("irabeth.iron_uncertain",))),
    n("assay", "Narrator", '''{n}You accompany the sample to the forge. Brena lays out what will be tested and lets Hadran mark the chosen piece. He records the process. This time he asks whether his description is correct before writing the next line.{/n}
{n}Heat builds in the small room. Irabeth removes her gloves and stands out of Brena's working space. When the smith asks for the shorter tongs, Hadran passes them before anyone else can move.{/n}
{n}"You know a forge?" Brena asks.{/n}
{n}"My uncle had one."{/n}
{n}"Then you know why I wanted my wagon at it."{/n}
{n}The test establishes sound material and a factor's mark over the maker's. It takes most of the afternoon. A waiting customer leaves without her hinges. Brena promises them tomorrow, angry at the lost time and unwilling to pretend the test was useless merely because it inconvenienced her.{/n}
{n}On the way back, Hadran carries the cooled sample. Nobody suggests his helpfulness has settled the missing account.{/n}''', c('[Discuss the remaining evidence.]', "cost")),
    n("cost", "Irabeth", '''{n}When the wagon is covered again, Irabeth asks Brena to wait by the gate. Hadran returns to duty with an instruction to locate the carrier and correct the two names. She does not ask either person to thank the other.{/n}
"The carrier has left something more awkward than a missing receipt. Hadran says he was paid from a watch purse to identify diverted supplies. His account may be in a sealed intelligence docket."
{n}She looks toward the gate, where Brena is inspecting her wheel.{/n}
"If that is true, the man who could establish her purchase was also being paid to report on her supplier. Opening his account might expose people still tracing the false iron. Keeping it sealed leaves her answering an accusation she cannot examine."
{n}She folds her arms.{/n}
"I dislike how readily that becomes a fine speech. I have made similar speeches. Some protected people who needed protection. Some protected an officer from admitting that he had made a poor decision."
{n}A runner crosses the yard. Irabeth waits until he has passed.{/n}
"I want this stopped properly. I also want the false iron found. Bad weapons kill people who never had the chance to argue about a receipt."''',
      c('"Find out what the docket contains before choosing what can be opened."', "next"),
      c('"Brena should hear what you can tell her now."', "brena")),
    n("brena", "Narrator", '''{n}Irabeth calls Brena back and explains that the carrier may have worked for the watch. She gives no name beyond the one Brena already supplied. The smith's expression hardens.{/n}
{n}"So your witness is also your man."{/n}
{n}"Possibly. I will establish that before I ask you to accept it."{/n}
{n}"And if he says I stole it?"{/n}
{n}"You will hear the accusation."{/n}
{n}"From him?"{/n}
{n}Irabeth hesitates. "I cannot promise that yet."{/n}
{n}Brena turns toward the wagon. "Then you've got work before you can promise anything."{/n}
{n}She goes to collect her tools. Irabeth lets her leave without trying to recover the last word.{/n}''', c('[Stay with Irabeth a moment.]', "next", flags=("irabeth.brena_told",))),
    n("next", "Irabeth", '''"I will ask for the docket. You can return when I have it."
{n}She rubs at a dark streak on her thumb, then stops trying to remove it with the other hand.{/n}
"I keep imagining the boy Hadran must have been. Eager to prove he knew what he was doing, desperate to be trusted with the next task. He has saved good people. I would like that to make him right."
{n}Her gaze returns to the empty yard.{/n}
"Brena has probably been unfair to someone too. It would be comforting to find out. Then I could stop feeling that the watch has put its boot on her goods."
"Will you look?"
"For a reason to dislike her? No. There are enough actual questions."
{n}She gives you a tired, wry smile.{/n}
"I am sorry the real duke was less amusing. Next time I shall at least provide a better place to sit."''',
      c('[Agree to return for the docket.]', flags=("irabeth.wagon_heard",))),
], requires=("irabeth.personal_ready",), delay=24)


s("the_question_outside_duty", "The question she did not owe you",
  '"I want to court you, Irabeth. May we speak about what that would mean?"', [
    n("start", "Irabeth", '''{n}Irabeth puts down the cup she was holding. She has heard you clearly. The pause belongs to her answer.{/n}
"Yes. I have thought about asking you the same thing."
{n}She moves a chair away from the desk and sits where she can face you without a report between you.{/n}
"I enjoy being wanted. That sounds embarrassingly simple. I keep expecting to find a better reason for how pleased I am when you come looking for me."
{n}Her ears darken. She does not look away.{/n}
"I do not mean being useful to the Commander. I mean noticing that you are looking at my mouth and wanting to give you a reason to continue."
{n}A smile interrupts the seriousness with which she has begun.{/n}
"There. I have said something sufficiently reckless to make the rest easier."''',
      c('"What do you want to keep separate from this?"', "rank"),
      c('"I want that too. Tell me what you need before we begin."', "rank"),
      c('"I have changed my mind. I value the friendship."', "friend")),
    n("rank", "Irabeth", '''"My judgment. You know I serve under you. I cannot make that disappear by removing my sword belt."
{n}She rests her forearms on her knees.{/n}
"If I advise against a march, I need to know that you will hear the advice. If you reject it, I need to argue the question without wondering whether a private evening has given me the right to insist. That is a temptation on my side too."
"And away from council?"
"I want to be able to disappoint you. Not as a test. Because one day I shall want sleep when you want company, or I shall have promised an hour to somebody else. I would rather endure your disappointment than spend the rest of the night performing pleasure I do not feel."
{n}She straightens a little.{/n}
"I am capable of wanting you very much. I am also capable of being tired, stubborn and convinced that my plan is excellent when it is merely mine. You ought to meet that woman before you promise anything to the one who salutes."''',
      c('"I want the woman who can refuse me. I will keep my own right to refuse."', "marriage"),
      c('"I expect a lover to support my decisions."', "refused")),
    n("marriage", "Irabeth", '''"Good. Then there is something more particular."
{n}She looks at her ring and turns it once, a familiar movement rather than a hesitation.{/n}''',
      c('"We should speak about Anevia."', "wife", forbids=("anevia_dead", "anevia_gone")),
      c('"We should speak about what losing Anevia means for this."', "bereaved", requires=("anevia_dead",)),
      c('"Anevia is gone. I will not treat that as an answer from her."', "gone", requires=("anevia_gone",), forbids=("anevia_dead",))),
    n("wife", "Irabeth", '''"I love her. I do not want to leave her."
{n}The words are firm, without apology.{/n}
"I can imagine loving another person and remaining her wife. Imagining it does not tell me what she wants, or what she would ask of me. I will speak to her first. Then I want you to speak with her yourself."
"Separately?"
"Yes. She must be able to say something to you without watching me receive it. Afterward she and I will speak again. This is not an inquiry in which the first consistent account wins."
{n}Irabeth's expression softens.{/n}
"Do not go to her as though asking to borrow a sword. You are asking for a change that reaches into her life. She is allowed to dislike a part of it. I may dislike a part of what she asks. We are accustomed to surviving that."
{n}She leans back, letting out a breath.{/n}
"If she wants time, we give it. I would rather wait for a real answer than keep finding ways to pretend I already have one."''',
      c('"Speak with her. I will meet her when she wants that conversation."', "wait"),
      c('"I would rather leave this as friendship."', "friend")),
    n("wait", "Irabeth", '''{n}Her hand moves toward yours, then settles on the chair between you.{/n}
"I would like to kiss you now. I shall probably still want to when you leave."
"That sounds inconvenient."
"Extremely. I have arranged it myself."
{n}She laughs, briefly and without disguising the frustration beneath it.{/n}
"Do not mistake waiting for a lack of interest. I am trying to make an invitation I can enjoy accepting. There are enough rooms in my life in which I look over my shoulder."
{n}At the door she pauses, one hand against the wood.{/n}
"You can still come to hear me recite. That invitation requires no secrecy. I have every intention of making the duke sound worse."''',
      c('[Give her time to speak with Anevia.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.spousal_conversation_requested"))),
    n("bereaved", "Irabeth", '''{n}Irabeth holds the ring still between finger and thumb.{/n}
"I do not want you to become a replacement for the person I look for when I enter a room. I shall look. You may see me do it."
{n}For a while she studies her own hand.{/n}
"I also do not want every future pleasure measured against how much I miss her. She loved me alive. She was particularly insistent about it when I became solemn."
{n}The effort to smile does not quite succeed.{/n}
"You can ask me to spend an evening with you. I can answer for that evening. If I speak of her, let me finish. If I cannot, do not make me finish to prove I trust you."
{n}She releases the ring.{/n}
"I would like to begin slowly. An invitation, then another. I will not ask a dead woman to deliver the answer I am afraid to give."''',
      c('"An evening, then. We can decide the next one when it comes."', "widow_yes"),
      c('"I cannot offer what you are asking. Let us remain friends."', "friend")),
    n("gone", "Irabeth", '''"Thank you."
{n}The relief is brief. She looks down at her ring.{/n}
"I cannot make her absence say what she would have said in this room. I will not invent a release from our marriage because it would let me kiss you with less to think about."
{n}She lifts her eyes.{/n}
"I want your company. I can ask for that openly. I am not ready to make it a courtship while the answer I owe her remains beyond my reach."
{n}Her hand closes around the arm of the chair, then relaxes.{/n}
"You do not have to wait. I would dislike hearing that you had made loneliness into a service you performed for me."''',
      c('[Leave the question open. Keep her company without making a romance promise.]', flags=("irabeth.started", "irabeth.absence_wait",)),
      c('[Keep this relationship as friendship.]', flags=("irabeth.closed",))),
    n("widow_yes", "Irabeth", '''{n}She offers her hand. You take it, and she holds yours with a quiet firmness that asks for no interpretation beyond the touch itself.{/n}
"There is a case I meant to show you. Afterward, I would like an hour that belongs to neither the case nor the war. I have put my name down to recite at a storehouse. A ridiculous little piece about a guard and a duke."
{n}Her thumb moves over your knuckles.{/n}
"You may come because you want to hear it. I should like to look up and find you there."
{n}She lets your hand go before returning to the desk. Her ring remains where it was. Nothing in the room has been cleared away to make the invitation possible.{/n}''',
      c('[Accept the first evening she has offered.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.bereaved_courtship", "irabeth.lover", "irabeth.personal_ready"))),
    n("refused", "Irabeth", '''{n}The warmth leaves her expression.{/n}
"Then I have answered too soon. I will remain your officer. I will not add that condition to my bed."
{n}She stands and moves the chair back to the desk. There is no further argument to win.{/n}''', c('[Accept her refusal.]', flags=("irabeth.closed",))),
    n("friend", "Irabeth", '''"Yes. I would rather hear that now."
{n}She takes a moment before rising. When she does, she offers her hand in farewell, without holding it out long enough to turn the gesture into another question.{/n}
"I meant that I enjoy your company. We can keep what we have without pretending it was merely a prelude to something else."''', c('[Remain friends with Irabeth.]', flags=("irabeth.closed",))),
], any_of=("irabeth.first_hour_kept", "irabeth.courtship_requested"),
    forbids=("i_affair", "trying", "committed", "irabeth.personal_ready", "irabeth.spousal_conversation_requested", "irabeth.absence_wait"))


s("one_truth_to_tell", "The affair they actually had",
  '"We promised to tell Anevia about us. I will not leave you to do it alone."', [
    n("start", "Irabeth", '''"I remember. I have not stopped remembering."
{n}Irabeth stands beside the window where you spoke before. This time she turns away from it when you arrive.{/n}
"I have told her that there is something she needs to hear from both of us. I did not tell her that I had simply become confused about a friendship."
{n}Her hands rest at her sides.{/n}
"She asked whether you knew I was married. I said yes. Then she asked whether I thought she was going to be comforted by how miserable I looked."
{n}Irabeth gives a short, humorless breath.{/n}
"I did. That is the part I disliked discovering."
{n}She faces you squarely.{/n}
"She wants to speak with you without me in the room. She and I will have our own conversation afterward. I said that was reasonable. Then I spent the next hour wishing I could hear it. Neither feeling has gone away."''',
      c('"What have you told her about the evening?"', "account"),
      c('"I will answer her myself. What are you asking for afterward?"', "after"),
      c('[Return when you can give this the attention you promised.]', abort=True)),
    n("account", "Irabeth", '''"That I wanted you. That we kissed. That I knew I was hiding it from her. I left the private details for her to ask about if she wants them."
{n}She touches the window frame, then lowers her hand.{/n}
"I have not called you the person who made me forget myself. I knew myself rather well that night. I was tired of being careful. I chose something I wanted."
"Do you want me to say the same?"
"I want you to say what is true of you. She will notice if we have rehearsed identical sentences. She deserves better than a polished pair of witnesses."
{n}For the first time, Irabeth's mouth curves.{/n}
"So do we, if there is to be anything left worth having."''', c('"What are you hoping she will say?"', "after")),
    n("after", "Irabeth", '''"That she still wants to be my wife. That she believes I can tell her an unwelcome truth before she has to dig it out of me."
{n}She pauses before the rest.{/n}
"And that she might accept my loving you too. I have not earned that answer by admitting what I did. I am going to ask for it anyway."
{n}Her gaze stays on yours.{/n}
"You may decide that you do not want the work that follows an evening you enjoyed. I would rather know before I ask her to make room for us."
{n}There is hurt in the possibility, but no effort to make it your punishment.{/n}
"If we stop, I shall still tell her. If she refuses, I shall not describe her refusal as cruelty. If she agrees, I shall not begin behaving as though the agreement happened before the kiss."''',
      c('"I want a relationship we can acknowledge. I will speak to her."', "agree"),
      c('"I will tell her the truth, but I do not want to continue as lovers."', "stop")),
    n("agree", "Irabeth", '''{n}Irabeth closes her eyes for a moment. When she opens them, she looks relieved and frightened in almost equal measure.{/n}
"Go when you can listen. I have said enough that she knows what conversation she is agreeing to."
{n}She steps aside from the door, leaving the way clear.{/n}
"I am going to find something useful to do while I wait. Probably badly. If you see a requisition with three different totals, you may know why."
{n}The joke makes a little room to breathe. She does not ask for a kiss before you leave.{/n}''',
      c('[Keep the promised conversation with Anevia.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.single_affair_disclosed", "irabeth.spousal_conversation_requested"))),
    n("stop", "Irabeth", '''"Then that is what I shall tell her."
{n}She takes the answer standing still. After a moment she looks toward the window.{/n}
"I am sorry it has ended here. I am glad you did not let me speak of a future you had already decided against."
{n}She turns back before you leave.{/n}
"You do not need a romantic promise to answer her honestly. Please remember that when she asks."''',
      c('[End the affair as a romance; leave its history intact.]', flags=("irabeth.closed",))),
], requires=("i_affair", "i_morning", "i_will_tell"),
    forbids=("a_affair", "trying", "committed", "irabeth.spousal_conversation_requested", "irabeth.personal_ready", "anevia_dead", "anevia_gone"))


s("anevias_answer", "The answer only Anevia could give",
  '"Irabeth said you wanted to speak with me."', [
    n("start", "Anevia", '''{n}Anevia closes the drawer she was searching. She leaves its key on the table and turns the chair beside it toward you.{/n}
"I do. Sit if you're going to sit. You're makin' the doorway look guilty."
{n}She waits until you have settled before taking the other chair. Irabeth is not here.{/n}
"Beth and I have talked. We've still got things to say. This part's between you and me."
{n}Her hand rests beside the key. She turns it once with a fingertip, then stops.{/n}''',
      c('"I want to hear what you think about the courtship we have asked for."', "asked", forbids=("irabeth.single_affair_disclosed",)),
      c('"I chose to be with her while hiding it from you. I will answer for that."', "affair", requires=("irabeth.single_affair_disclosed",))),
    n("asked", "Anevia", '''"I think my wife's been walkin' about lookin' as though she's stolen a whole bakery because she wants a second person to kiss her."
{n}Anevia's mouth twists with affection and exasperation.{/n}
"I told her wantin' wasn't the part that needed an apology. Then she apologized for apologizin'. We took a break."
{n}She leans back.{/n}
"I'm glad she told me. I'm glad you waited. That doesn't mean every arrangement anybody suggests is going to suit me. I've spent enough evenings eating alone while she explains why the next report will be the last one. I'm not signin' up to become the reliable person whose time can always be moved."
"What would suit you?"
"An actual answer when I ask whether she's comin' home. An evening we planned staying ours unless something real changes it. And no whisperin' in the next room about how difficult I might be. I'm right here. Be brave enough to find me."''', c('"We can speak directly. What else should I understand?"', "other")),
    n("affair", "Anevia", '''"Good. Start there."
{n}She watches you without helping the silence along.{/n}
"I've heard Beth say she wanted it. I believe her. Don't make a kinder story in which you happened to be standin' there when she became too sad to choose. She'd hate that. So would I."
"I wanted her. I knew you were married."
"And you thought I could be told afterward."
{n}The answer is yes. She looks down at the key.{/n}
"I can hear yes. It's all the soft cloth people wrap round it that makes me want to throw something."
{n}For a while she says nothing. When she looks up, the anger has not disappeared.{/n}
"I still love her. I can imagine her loving somebody else. Those two facts have been made to do a great deal of work for a choice neither of you asked me about."
{n}She draws a breath.{/n}
"I'm willing to try a different arrangement. Willing. I'm not sayin' the evening was secretly all right because I can find a way forward now. Don't turn my answer into a better past."''',
      c('"I will not. We concealed it. Any agreement begins now."', "other"),
      c('"Then why keep being angry if you are willing?"', "refuse")),
    n("other", "Anevia", '''{n}Anevia moves the key out from beneath her hand.{/n}
"One other thing before you begin trying to be impressively considerate."''',
      c('"You and I have a relationship too. I will not ask you to answer as though we do not."', "lovers", requires=("anevia.lover",), forbids=("anevia.closed",)),
      c('"You and I were lovers. I will not pretend that history disappears because it ended."', "past", requires=("anevia.lover", "anevia.closed")),
      c('"You are not being asked to become my lover."', "separate", forbids=("anevia.lover",))),
    n("past", "Anevia", '''"Good. I remember it. I remember why it ended too."
{n}She leaves her chair where it is.{/n}
"I'm answering about my marriage and Beth's invitation. I'm not offering to reopen ours. Those are different questions, even when the same people make them awkward."
{n}She studies you for a moment.{/n}
"I can be willing for her to see you without saying I want the same thing again. Don't ask me to prove I'm comfortable by making myself affectionate. I'll be honest. That's what I'm offering."''', c('"I understand. Tell me what you and Irabeth have discussed."', "terms")),
    n("lovers", "Anevia", '''"Good. Because I'd noticed."
{n}A little warmth returns to her face, but she keeps her chair where it is.{/n}
"What we've chosen doesn't answer this for Beth. And what she wants doesn't make our evenings part of a bargain in which everybody has to do the same thing. I might want you alone one night. She might want me alone the next. Nobody gets a receipt to cash in against the other two."
{n}She studies you with a rueful smile.{/n}
"We may want a shared evening later. Then we'll ask about that evening. I'd like to see whether we actually enjoy it before someone starts ordering a larger bed."
{n}She taps the table.{/n}
"For now, you're asking about her. I'm answering about my marriage. I still mean the things I said to you in our own time."''', c('"Then let us keep those choices distinct."', "terms")),
    n("separate", "Anevia", '''"Glad to hear it. I like choosin' my own invitations."
{n}She smiles briefly, then becomes serious again.{/n}
"You can have supper with us without it being a rehearsal for anything. You can see Beth on her own without making me the person who keeps watch outside. If I want somethin' with you, you'll hear it from me."
"And if you don't?"
"Then you'll have the terrible burden of knowin' two married women without kissing both of them. People have survived worse."
{n}The joke lets the room relax. Anevia does not use it to leave the question behind.{/n}
"I mean it. Don't try to repay my agreement by flirtin' at me. A quiet thank-you will do."''', c('"Thank you. I would like to hear the terms you and Irabeth discussed."', "terms")),
    n("terms", "Anevia", '''"She tells me when she's spending the evening with you. I don't want the private details. I do want to know whether to keep supper warm. We keep the time we've already promised each other. If the war takes it, we say so and find another day. We don't use the war to avoid sayin' we wanted something else."
{n}Anevia reaches for a loose thread at her cuff, considers pulling it and leaves it alone.{/n}
"You don't have to become exclusive to make me comfortable. Neither does she get to decide who else you love. But if somebody is waiting for you, tell them where you've gone. I have no use for the kind of freedom that depends on someone else not knowing when to stop waiting."
"And if this stops working?"
"We talk before we've spent a month collecting grievances like spare arrows. Beth and I talk as wives. You and she talk as lovers. If a thing concerns all of us, we can find a room big enough for three people with opinions."
{n}Her smile turns crooked.{/n}
"Drezen has survived worse rooms."
{n}She lets you consider the answer without filling the pause.{/n}''',
      c('"I can agree to that. I will speak to her about the evening we actually want."', "yes"),
      c('"I cannot agree to those terms. I will not begin the relationship."', "no")),
    n("yes", "Anevia", '''{n}Anevia nods. The motion is small, but the conversation changes after it.{/n}
"I'll tell her what I said. Tell her what you heard. If there's a difference, we'll find it before anyone spends a week being noble about a misunderstanding."
{n}She gets up to retrieve the key. At the drawer she pauses.{/n}
"She wants to be asked because somebody enjoys her. Not because she has looked tired long enough to deserve a treat. She's funnier than she thinks. Worse at losing than she admits. And she likes being admired, which she'll confess with the expression of someone handing over a stolen relic."
{n}Anevia looks back at you.{/n}
"Don't make me regret tellin' you that by repeating it word for word. Find out for yourself."
{n}Her hand rests on the drawer.{/n}
"Give us tonight. Then go and ask her."''',
      c('[Leave them their evening; return to Irabeth later.]', flags=("irabeth.spouse_heard",))),
    n("no", "Anevia", '''"Then say that to her. Plainly."
{n}She pushes her chair back beneath the table.{/n}
"I won't be pleased if it hurts her. I would be less pleased if you agreed while planning to see how little of it you could keep."
{n}She opens the drawer again. There is nothing more to negotiate on Irabeth's behalf.{/n}''', c('[End the proposed romance with Irabeth.]', flags=("irabeth.closed",))),
    n("refuse", "Anevia", '''"Because wanting a future doesn't make me stupid about the past."
{n}Her chair scrapes against the floor as she stands.{/n}
"We're done for now. I'll tell Beth exactly why. You're not getting an arrangement that begins by telling me which feelings make it convenient for you to stay."
{n}She opens the door and waits for you to leave.{/n}''', c('[Accept that this proposal has failed.]', flags=("irabeth.closed",))),
], requires=("irabeth.spousal_conversation_requested",), owner="Anevia", delay=48,
    forbids=("irabeth.spouse_heard", "irabeth.personal_ready", "irabeth_dead", "irabeth_gone"))


s("the_evening_she_chose", "An invitation in her own name",
  '"I have spoken with Anevia. I would like your answer now."', [
    n("start", "Irabeth", '''{n}Irabeth has laid two cups beside a jug of water. She notices you looking at them and gives a small, embarrassed shrug.{/n}
"I thought of wine. Then I thought of spending the conversation wondering whether the wine had made either of us more agreeable. Water is less ambitious."
{n}She pours, gives you a cup and sits.{/n}
"Anevia told me what she said. I agree with the terms. I want to keep the time I have promised her. I want to make time for you, with an actual day attached to it."
{n}She takes a drink before continuing.{/n}
"I also asked her not to describe every pleasant expression on my face as evidence. She said she would try, unsuccessfully. I believe that was an honest undertaking."
{n}Her smile lasts a little longer than the joke.{/n}''',
      c('"We have waited to begin. What would you like?"', "new", forbids=("irabeth.single_affair_disclosed",)),
      c('"We have already been lovers. What do you want to change?"', "old", requires=("irabeth.single_affair_disclosed",))),
    n("new", "Irabeth", '''"To ask you out without first explaining why the appointment might be useful."
{n}She puts down her cup.{/n}
"There is a room above the old tack store. Dema uses it to keep benches for the recitations. She lets people practice there when nobody needs the benches. I asked for an hour. There is a window, two chairs that do not match, and no desk."
"You make it sound magnificent."
"I have been imagining it rather extravagantly. The absence of a desk has become important."
{n}She reaches across the space between you, palm upward.{/n}
"Come with me. Hear the guard. Tell me something you want from an evening, even if it has nothing to do with my plans. Then, if we both still want to, I would like to kiss you."
{n}She pauses, catches herself adding another qualification, and laughs.{/n}
"That is the invitation. I shall leave it alone long enough for you to answer."''', c('"Yes. I would like that evening."', "room")),
    n("old", "Irabeth", '''"I want to stop making the door the most important object in a room."
{n}She looks toward it now, acknowledging the habit.{/n}
"I knew where it was when we kissed. I thought about who might use it. Even while I was happy, I was composing an explanation for being there."
{n}Her fingers close around the cup and then release it.{/n}
"I have not forgotten how much I wanted you. I would like to discover what wanting is like when I have also said where I am going. Anevia knows I have asked you for an evening. She has made plans of her own. I am not borrowing an hour she thinks I am spending over a report."
{n}Her voice becomes warmer.{/n}
"There is a room above the old tack store. I have asked to use it for practice. I thought I might recite something dreadful, let you laugh at me, and kiss you when we have both stopped laughing."
"And if we cannot stop?"
"Then I shall have to become unusually inventive."''', c('"I would like to discover that with you."', "room")),
    n("room", "Narrator", '''{n}You walk to the tack store together. Irabeth takes the key from a hook beside Dema's notice and returns it to the same hook after opening the upstairs door. The arrangement requires no whispered explanation.{/n}
{n}The room contains more benches than Irabeth promised. They stand on end against one wall, leaving the window clear. Two chairs wait beneath it. One has a cushion; the other has a leg strengthened with an iron brace.{/n}
{n}"Choose carefully," Irabeth says. "Comfort or confidence in the structure."{/n}
{n}You test both, then move them close enough that neither of you needs to raise your voice. She takes out a folded page and discovers that she has brought the list of participants instead of the piece.{/n}
{n}For a moment she looks appalled. Then she sits down and laughs.{/n}
{n}"The whole plan depended on remembering paper. I have finally found a reason to regret leaving the desk."{/n}
{n}"Do you need the words?"{/n}
{n}"Probably less than I need to stop being angry with myself for forgetting them."{/n}''',
      c('"Give me the version you remember. I will fill any gaps very badly."', "play"),
      c('"Let us leave the performance for another day. I want to hear what you hoped for tonight."', "hope")),
    n("play", "Narrator", '''{n}Irabeth stands and begins. You take the duke's part from the questions she gives you, then begin supplying questions of your own. When the guard claims to have slain a monster with three mouths, you ask whether it charged three tolls.{/n}
{n}She loses her solemn expression.{/n}
{n}"It charged whatever it liked. It had three mouths."{/n}
{n}The argument becomes increasingly unreasonable. The duke demands receipts for the monsters. The guard offers a tooth and refuses to say which monster it belonged to. By the time the wool arrives, nobody has asked about it for several minutes.{/n}
{n}Irabeth sits beside you, laughing hard enough to need a moment before speaking.{/n}
{n}"I had hoped you would enjoy it. I had not considered the danger of giving you a speaking part."{/n}
{n}Her knee rests against yours. When she notices, she stays where she is.{/n}
{n}"I did not have to be good enough to deserve that," she says, almost to herself. "You were enjoying doing it with me."{/n}''', c('"I was. I would like more evenings in which I get to be foolish too."', "yours")),
    n("hope", "Irabeth", '''"I hoped you would look pleased to be alone with me. You have managed that part."
{n}She turns in her chair, bringing one knee near yours.{/n}
"I wanted to stop wondering whether I had made this too solemn to enjoy. We have had necessary conversations. I keep thinking I ought to follow them with another necessary conversation, until someone declares us fit for a pleasant one."
{n}Her smile reveals the tips of her tusks.{/n}
"I wanted to see whether you would kiss me if I stopped explaining myself. And I wanted to hear something you do not say in council. Something foolish you would like, perhaps. I have brought enough earnestness for two people. You need not supply more for my benefit."
{n}She rests her hand on the edge of your chair.{/n}
"What did you hope would happen when you said yes?"''', c('[Tell her what you wanted from the evening.]', "yours")),
    n("yours", "Irabeth", '''{n}You tell her about wanting an hour in which you are neither a solution nor an explanation. She listens, occasionally asking a question instead of offering reassurance.{/n}
"I may be poor company for that if you expect me never to notice who you are."
"I do not expect you to forget."
"Good. I would like to tell you when you are making something unnecessarily difficult. I have several examples, but they can wait."
{n}The laughter comes more easily now. Irabeth leans closer, then waits, letting the change in distance become a question.{/n}
"I would like to kiss you. I have thought of it several times while you were talking. You may take that as a compliment to the talking or a confession of poor attention."''',
      c('[Meet her kiss.]', "kiss", flags=("irabeth.first_open_kiss",)),
      c('"Hold my hand tonight. I want to take this slowly."', "hand")),
    n("kiss", "Narrator", '''{n}Her hand rises to your cheek. She kisses you gently at first, then pauses close enough that you can feel her breath when she laughs.{/n}
{n}"I was trying to remember where to put my other hand."{/n}
{n}You take it and bring it to your waist. Her fingers settle there, warm and assured. The next kiss lasts until one of you shifts against the chair and its iron brace gives a startling creak.{/n}
{n}You break apart laughing. Irabeth looks at the chair with personal offense.{/n}
{n}"I chose that one for confidence."{/n}
{n}"The room has benches."{/n}
{n}"On end. I am enthusiastic, not reckless."{/n}
{n}She stands and offers her hand. You move to the window, where the sill gives her somewhere to lean while you come close again. This time there is no furniture to interrupt. When she finally rests her forehead against yours, she is smiling.{/n}''', c('[Stay with her until the hour is nearly gone.]', "end")),
    n("hand", "Narrator", '''{n}She turns her palm toward yours and threads your fingers together.{/n}
{n}"Then I can enjoy being asked for that."{/n}
{n}She shifts her chair close enough that you can sit without stretching your arms. For a while you talk about the worst performances either of you has endured. Irabeth remembers a mercenary who sang an entire ballad in the wrong order and became angry when anyone died twice.{/n}
{n}When the street grows noisier beneath the window, she leans toward you to finish the story. Her shoulder rests against yours. She does not try to turn the touch into something you did not ask for.{/n}
{n}"Another evening," she says. "I would like another, at this pace if it suits us."{/n}''', c('[Enjoy the hour you chose.]', "end")),
    n("end", "Irabeth", '''{n}Before leaving, Irabeth puts the chairs back where she found them. You open the door while she checks the window latch.{/n}
"There is a disagreement over a wagon of cold iron I would like to hear properly. Come if you want to. It is work, and I shall not pretend otherwise."
{n}She turns toward you.{/n}
"Tonight I wanted your company in a room without a report. Tomorrow I shall ask you to hear a difficult report with me. I would like to discover how we manage that kind of day too."
{n}At the foot of the stairs she takes your hand once more, in full view of the open street. She holds it only a moment before going her own way.{/n}
"Good night. I am pleased you came."''',
      c('[Begin the relationship you have now chosen openly.]', flags=("irabeth.marital_terms_agreed", "irabeth.lover", "irabeth.personal_ready"))),
], requires=("irabeth.spouse_heard",), delay=24, forbids=("irabeth.personal_ready", "anevia_dead", "anevia_gone"))


s("a_day_of_our_own", "Something they had not done yet",
  '"We have a life with Anevia. I would also like another day with you."', [
    n("start", "Irabeth", '''"So would I."
{n}Irabeth moves a book from the chair beside her. She smiles before you sit, with the ease of a woman who has already found your hand in less convenient places.{/n}
"I do not want to turn that into a second beginning. We have been lovers. We have made choices with Anevia. I remember them."
{n}She sets the book on the desk.{/n}
"But there are things I have not asked you to do with me because I kept thinking of how they would fit into an evening for all three of us. Some do not fit. Anevia has heard me argue with imaginary dukes often enough to ask for a holiday from them."
{n}Her expression becomes a little mischievous.{/n}
"You have not exhausted your patience yet. I thought I should take advantage."''',
      c('"An imaginary duke? I may need warning."', "piece"),
      c('"You can ask for a day with me without making it useful to all three of us."', "ours"),
      c('[Keep the invitation for another day.]', abort=True)),
    n("piece", "Irabeth", '''"A caravan guard, a missing load of wool and a duke who suspects every beast in the story has been hired to delay his delivery."
{n}She gives you a few lines. The guard's monsters grow with every question. The duke's patience shrinks until he begins charging the guard for the time spent describing them.{/n}
"I used to know it. I have put my name down for a recitation and discovered that knowing words in your head is easier than knowing them in front of people."
"Did Anevia draw you into this?"
"No. I signed the page myself. She found out afterward and looked so pleased that I briefly considered denying it."
{n}Irabeth laughs.{/n}
"She has plans for the day. I would like you to hear the piece before I face the audience. Then perhaps help me decide which parts deserve to survive."''', c('"I would like that."', "ours")),
    n("ours", "Irabeth", '''"I know. I am trying to act as though I know."
{n}She rests her hand against yours.{/n}
"I have spoken with her about wanting this. She said she likes being my wife considerably more when it does not require attending every performance I rehearse. Then she made me do the duke twice."
{n}Her thumb moves over your knuckles.{/n}
"I am not asking to withdraw the promises we made together. I am asking for a day within them. If we later decide the shared arrangement no longer suits us, we will have to say that honestly. A walk with you cannot do that work in secret."
{n}She looks at you directly.{/n}
"Would you like to spend the afternoon with me? We can hear the piece, then find something neither of us has rehearsed."''', c('"Yes. Show me what you have chosen."', "walk")),
    n("walk", "Narrator", '''{n}You go to the storehouse where the recitation will take place. Dema, the woman arranging it, points out the standing place and warns Irabeth that the back of the room swallows quiet voices. Irabeth thanks her and waits until she has gone downstairs.{/n}
{n}Then she stands where the performers will stand and begins. The first lines are too measured. You ask her what the guard wants. She answers, "His money," with such immediate conviction that the whole piece changes.{/n}
{n}He wants his money. He wants a dry bed. He wants the duke to stop correcting the geography of a road the duke has never seen. Irabeth gives him a muttered complaint between the grand claims, and suddenly he is a man you can imagine sitting beside a fire.{/n}
{n}When she finishes, she looks at you without the protection of a joke.{/n}
{n}"Was it good?"{/n}
{n}You tell her which part made you laugh. She asks you to repeat the exact line, then tries it again, enjoying that you are watching.{/n}''', c('[Let her enjoy doing it well.]', "desire")),
    n("desire", "Irabeth", '''"I want them to applaud. There. A remarkably small ambition to make me so uncomfortable."
{n}She comes to stand beside you, looking back at the empty place where she performed.{/n}
"I have wanted larger things. A name people recognize. A reason for someone who shut a door in my face to hear what I have become. I do not always like the woman who wants that. I am tired of pretending she never speaks."
{n}She leans her shoulder against yours.{/n}
"You have heard me laugh over a bad book. You have heard me say I wanted somewhere to go. This is one place I chose before the war has finished granting me permission."
{n}Her hand finds yours.{/n}
"I would like you in the room. I shall know where to look if I forget the next line."''',
      c('[Kiss her, then ask for the most ridiculous verse again.]', "kiss"),
      c('[Hold her hand and let her choose the next verse.]', "hand")),
    n("kiss", "Narrator", '''{n}She turns toward your kiss, smiling before your mouths meet. The empty room makes every small movement audible. When you part, she looks toward the door, then laughs at herself.{/n}
{n}"Dema has probably endured worse rehearsals."{/n}
{n}She keeps your hand while giving you the verse about the serpent. This time she directs the duke's most offended look at you. You interrupt with a kiss to her knuckles, and she loses the line completely.{/n}
{n}"You will not do that during the performance."{/n}
{n}"Is that a request?"{/n}
{n}"A desperate one."{/n}''', c('[Promise to behave badly only afterward.]', "end")),
    n("hand", "Narrator", '''{n}Irabeth remains beside you while reciting the next exchange. Without an audience to face, she begins giving the guard little asides meant only for you. The duke grows increasingly annoyed at being excluded from his own hall.{/n}
{n}When the passage ends, she presses your joined hands against her side.{/n}
{n}"I like this too. I was so occupied with giving you a performance that I forgot I could share the joke."{/n}
{n}You stay until Dema calls from downstairs to ask whether the benches are behaving themselves. Irabeth answers that she has had no complaints, then looks at you as though inviting one.{/n}''', c('[Leave the benches their reputation.]', "end")),
    n("end", "Irabeth", '''"There is a real dispute waiting for me. A wagon of cold iron, a lieutenant I respect and a smith who has reason to be angry with him."
{n}Outside, she pauses at the turn back toward headquarters.{/n}
"I would like your help hearing it. If you are willing, come to the yard. I shall keep the performance for another evening, with less iron and more ridiculous creatures."
{n}She kisses your cheek before releasing your hand.{/n}
"Find me when you have time. I have not run out of things I want to do with you."''',
      c('[Keep the individual invitation within the relationship already chosen.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.legacy_shared_history", "irabeth.boast_guard"))),
], requires=("i_self", "i_seen", "ordinary"), any_of=("trying", "committed"), forbids=("irabeth.personal_ready", "tirabade.group_closed", "anevia_dead", "anevia_gone"))


s("the_sealed_account", "What the watch was protecting",
  '"You have the carrier\'s account. What does it establish?"', [
    n("start", "Irabeth", '''{n}Irabeth has taken over a narrow room usually used to count stores. The account lies open on a table. Beside it are three plain sheets and a little heap of sand shaken from a packet.{/n}
"His name is Ordel. He bought Brena's repaired tools for the factor and carried the balance of her payment. She paid for the iron. That much is clear."
{n}She shows you the relevant entry. The figures match the value Brena described, including an allowance for a repaired wagon axle.{/n}
"He was also paid by the watch to follow the factor's purchases. He supplied the warning about false iron. Hadran recognized the factor's mark because Ordel taught him to recognize it."
{n}Irabeth turns to the next page without inviting you to read the unrelated names above it.{/n}
"Ordel said to watch the loads entering a particular warehouse. Brena's wagon had left that warehouse. The warning justified stopping it. It did not justify making her prove innocence against an account she was never allowed to see."
{n}She puts a clean sheet over the names.{/n}
"He has returned. He will speak with me. He does not want his paid work for the watch made public."''', c('"Let us hear him."', "ordel")),
    n("ordel", "Narrator", '''{n}Ordel comes in carrying his cap. He is older than Hadran, with a pale scar disappearing into his beard. He looks at the account before looking at you.{/n}
{n}"I gave you the warning," he tells Irabeth. "I didn't tell you to take the woman's livelihood."{/n}
{n}"No. You helped her purchase the iron. Can you say that before her and the lieutenant?"{/n}
{n}"I can say I sold the tools. I can show my mark. I won't say why you have my mark in that book."{/n}
{n}He points to the covered pages.{/n}
{n}"The factor thinks I carry for him because he pays on time. I know where he puts the bad bars. He doesn't know I know. If he hears I've been paid by the watch, there's a boy who carries his messages who'll get the blame before I do. I can leave. The boy lives with his sister over the warehouse."{/n}
{n}Irabeth asks whether he has told the watch about them before. He names the page. She finds it, reads and nods.{/n}
{n}"Then we have a protection to arrange whether we use your evidence or not."{/n}
{n}Ordel's grip on his cap loosens slightly.{/n}''',
      c('"Could a copy of the purchase entry clear Brena without identifying your work?"', "copy"),
      c('"Why should she bear the cost of keeping this secret?"', "cost")),
    n("copy", "Irabeth", '''"It could clear the purchase. It would not explain why the watch had an account from a man now called as its own witness."
{n}She draws one of the blank sheets toward her.{/n}
"I could give her a copy of the sale entry and ask her to trust that I removed nothing relevant. She would have good reason to ask who decided relevance."
{n}Ordel sets his cap on the table.{/n}
"I can tell her she paid. In my own name."
"And when she asks why Hadran trusted your warning but not her account of meeting you?"
{n}He looks away.{/n}
"Then you explain you made a mistake."
"We did. There is still a choice about how much of the mistake she can inspect."
{n}Irabeth looks at you.{/n}
"I will not pretend a clean copy answers the whole complaint. I would like it to. We could all leave earlier."''', c('[Hear what keeping the account sealed would cost.]', "cost")),
    n("cost", "Irabeth", '''"She should not. That is why I have not asked her to accept the delay as patriotic generosity."
{n}Irabeth opens a small purse and places it beside the account.{/n}
"These are watch discretionary funds. I can pay for the delayed work and return the wagon under my own signed responsibility. No finding of theft, no charge against her, and a record that the detention outlasted its justification. She would have the purchase extract. Ordel's work and the rest of his account would remain sealed."
"What does the purse otherwise buy?"
"Repairs to a batch of practice weapons. I would postpone those and ask the next training groups to share. It is inconvenient. It should be our inconvenience."
{n}Ordel watches her carefully.{/n}
"The other course is to disclose why we paid him and give Brena the relevant original pages. We could then investigate the failure with evidence she can challenge. We would need to move the boy and his sister before the disclosure. Ordel would lose his access to the warehouse. The false-iron inquiry would continue with less help."
{n}She closes the purse.{/n}
"I favor protecting the source and taking the cost ourselves. I want the people sending brittle weapons to our soldiers. I also know Brena would be asked to accept limits imposed by the organization that wronged her. She may refuse to call that justice, however carefully I explain it."''',
      c('"Protect the source. Return her goods and pay the cost from the watch\'s own purse."', "sealed", flags=("irabeth.account_sealed",)),
      c('"Protect the people first, then open the relevant original record to Brena."', "open", flags=("irabeth.account_open",))),
    n("sealed", "Irabeth", '''"Then I will sign it. My name, not a sentence about the Commander having advised me."
{n}She turns to Ordel.{/n}
"You will give Brena the account of her payment in person. I will explain why some records remain withheld. You will not tell her that my discretion proves she should stop asking."
"I wasn't going to."
"Good. It will be easier not to begin."
{n}She counts the compensation from the purse and records the loss against the practice repairs. The amount is substantial enough to make her pause. Then she finishes counting.{/n}
"She may still take her future work elsewhere. I will not ask her to become grateful for being paid what we cost her."
{n}Ordel reaches for his cap, then stops.{/n}
"The boy?"
"We will arrange somewhere he and his sister can go if the warehouse becomes unsafe. Keeping your name quiet does not excuse leaving them without a way out."
{n}He nods. It is the first time he has looked at the decision as more than a reprieve for himself.{/n}''', c('[Stay while the terms are given to Brena.]', "answer_sealed")),
    n("open", "Irabeth", '''{n}Irabeth studies the covered page for a long moment.{/n}
"Then we move the boy and his sister before opening it. Ordel will have to arrange new work. I will explain why the watch has chosen this, and I will not tell him the consequences are imaginary because the choice is defensible."
{n}Ordel puts on his cap.{/n}
"I don't thank you for it."
"I did not expect you to."
"I gave you good information."
"You did. You have not been exposed for misconduct. That may make very little difference to the next person you ask to hire you."
{n}He looks at her, anger giving way to an exhausted attention.{/n}
"You know that?"
"Yes. I prefer the other course. I can still carry out this one properly."
{n}She writes the relocation instruction, then a payment for Ordel's lost commission. She does not write a reward. When he leaves to make the arrangements, Irabeth remains beside the table, watching the door for a few seconds after it has closed.{/n}''', c('[Return when the witnesses are safe and Brena can inspect the account.]', "answer_open")),
    n("answer_sealed", "Narrator", '''{n}Brena hears the offer with Ordel beside the door and Hadran standing opposite her. She checks the purchase figures aloud, making Irabeth repeat the repaired axle's value. Then she takes the compensation and asks for the wagon keys.{/n}
{n}"Is that your agreement?" Hadran asks.{/n}
{n}"That's my money. Don't make it say more."{/n}
{n}He looks at Irabeth. She nods toward the keys.{/n}
{n}Brena puts them into the pocket of her apron. She tells Ordel she is glad to see him alive and displeased to discover how many people have been paid to know things about her cargo except her.{/n}
{n}"You can bring repairs to my forge," she tells Irabeth. "For a price. If you want me at a meeting to praise this, find another smith."{/n}
{n}"I will not ask."{/n}
{n}"Remember that when someone says the matter is settled."{/n}
{n}After she has gone, Irabeth changes the heading on her report from 'Settlement' to 'Return and compensation.' The alteration takes less time than the silence following it.{/n}''', c('[Ask about Hadran.]', "lieutenant")),
    n("answer_open", "Narrator", '''{n}It takes another day. Ordel returns with confirmation that the siblings have moved into a room belonging to their aunt. He does not give the address in front of Brena. Irabeth accepts the confirmation and opens only the pages concerning the warning and the purchase.{/n}
{n}Brena cannot read the figures fluently, so she asks for each entry to be read aloud. She challenges a date. Ordel checks his road notes and concedes that he recorded arrival rather than payment. She asks for that distinction to be written on the copy she will keep.{/n}
{n}Hadran hears every question. By the end, his written account looks much less certain than it did in the yard.{/n}
{n}"I shouldn't have dismissed the second name," he says.{/n}
{n}"No," Brena replies. "You shouldn't."{/n}
{n}She takes the corrected copy and the wagon keys. At the door she thanks Ordel for answering. He replies that she paid for good iron and deserved to take it away. There is no thanks between him and the watch.{/n}
{n}Irabeth closes the account after they have left. The inquiry into the false load has lost its easiest way into the warehouse. She notes that beneath the record of what disclosure established.{/n}''', c('[Ask about Hadran.]', "lieutenant")),
    n("lieutenant", "Irabeth", '''"I have removed him from independent seizure decisions until he has completed a review with another officer. He remains on patrol. He will take no testimony from Brena again."
{n}She gathers the spare sheets.{/n}
"He thinks I should either clear him or remove him entirely. A clean judgment would be easier to carry. I have given him work and restrictions instead."
"Do you trust him?"
"With a frightened recruit in a burning building? Yes. With a woman who makes him feel foolish? Not yet. I need officers to be more than the best thing they have ever done."
{n}She looks toward the small purse, now lighter than when you arrived.{/n}
"I also need to be able to keep a capable officer without inventing a defense for every mistake he makes. That is the part I shall be asked to explain to people who did not see the wagon."
{n}Her mouth sets.{/n}
"Let them ask. I have the account."''', c('[Leave the report with her own signature on it.]', "private")),
    n("private", "Irabeth", '''{n}At the doorway she catches your sleeve, lightly enough that you can keep walking if you wish.{/n}
"I was irritated with you at least once. I wanted you to agree before I had finished explaining."
"Which part?"
"The part in which I had already decided I was being very reasonable."
{n}She lets go, smiling reluctantly.{/n}
"I would still like you to come to the recitation. I have nearly learned the ending. The guard gets paid by mistake, which seems less plausible after this week than any of his monsters."
{n}She steps closer and waits. You touch her hand. The pressure of her fingers is warm and familiar, with nothing settled by it except your wish to remain another moment.{/n}''',
      c('[Keep the invitation to the performance.]', flags=("irabeth.account_resolved",))),
], requires=("irabeth.wagon_heard",), delay=48)


s("ten_minutes_in_a_hall", "The applause she wanted",
  '"Your name is fourth on the list. May I come with you?"', [
    n("start", "Irabeth", '''"Please. I have revised the piece until I no longer remember which version was funny."
{n}Irabeth holds the folded page without looking at it. She has put on a plain dark shirt beneath her coat. The collar sits open at her throat. She notices your glance and touches it once.{/n}
"I tried fastening it. I looked as though I intended to inspect the audience."
{n}She starts toward the door, stops and puts the page on the desk.{/n}
"If I carry it, I shall stare at it. I know the words. I may know too many of them."
{n}Outside, she walks quickly enough that you have to remind her the performance will not begin earlier because you arrive breathless. She slows, gives you a look of gratitude mixed with annoyance, and deliberately takes the next corner at an ordinary pace.{/n}
"You are enjoying this."
"I enjoy being invited."
"Keep that answer ready. I may need to hear it again."''', c('[Go to the storehouse with her.]', "hall")),
    n("hall", "Narrator", '''{n}Dema has arranged the benches around a cleared space. The audience consists of people in work clothes, a pair of soldiers sharing a wrapped supper and a woman who has brought mending. Nobody appears to have dressed for an officer's visit.{/n}
{n}Irabeth looks relieved until Dema greets her by rank. Then she asks to be introduced by name. Dema nods and crosses something off her page.{/n}
{n}"You still have ten minutes," she says. "I took two away from a captain last week. Don't make me develop a reputation."{/n}
{n}The first speaker tells a story about an ox that understood every instruction except the useful ones. The second reads a poem too quietly for the rear benches. Irabeth leans forward, listening hard. A man behind you mutters that he cannot hear. She turns halfway toward him, catches herself and faces front again.{/n}
{n}"I am not in charge of the room," she whispers.{/n}
{n}The third speaker is brief, funny and already known to half the audience. The applause lasts long enough for Irabeth to look alarmed.{/n}
{n}Then Dema calls her name.{/n}''',
      c('[Meet her eyes and smile before she stands.]', "perform"),
      c('[Squeeze her hand once, then let her go.]', "perform")),
    n("perform", "Narrator", '''{n}Irabeth takes her place. Her first words have the careful weight of a formal address. Someone shifts on a bench. She hears it. The next line catches in her throat.{/n}
{n}For a moment you can see the whole performance threatening to become something she will apologize for later. Then she looks at the woman with the mending, who is waiting with her needle suspended above the cloth.{/n}
{n}Irabeth gives the guard his wet boots.{/n}
{n}He has walked all the way to the duke's hall. He wants to be paid. He would particularly like the duke to stop standing near the fire while asking how cold the road was. The woman laughs before Irabeth reaches the first monster.{/n}
{n}The next laugh comes from the soldiers. Irabeth waits for it to finish. You recognize the moment she begins enjoying the room. Her shoulders loosen. The duke becomes magnificently offended by a serpent's refusal to respect a toll exemption.{/n}
{n}At the back, somebody calls, "Make the duke carry the wool!"{/n}
{n}Irabeth turns the guard toward the invisible duke.{/n}
{n}"My lord, the road has expressed a wish to meet you personally."{/n}
{n}The room laughs. Irabeth grins before recovering her solemn face.{/n}''', c('[Listen to the ending she has chosen.]', "ending")),
    n("ending", "Narrator", '''{n}The guard receives his money because the duke's clerk has grown tired of correcting the account. He leaves with his fee, a stolen bun and the conviction that he has survived the most unreasonable creature on the road.{/n}
{n}Irabeth gives the clerk the final line. It is quiet enough to require attention, loud enough to reach the rear bench. The audience is still for half a breath. Then the woman with the mending laughs, and the others follow.{/n}
{n}The applause begins before Irabeth has decided how to bow. She starts a formal inclination, abandons it and gives the room an awkward, delighted smile.{/n}
{n}On the way back to you, she nearly sits in the wrong place.{/n}
{n}"I remember every line," she whispers. "Now. All of them. Including two I left out."{/n}
{n}Her hand finds yours beneath the edge of the bench. She holds it firmly through the next introduction.{/n}
{n}You stay for the remaining speakers. Irabeth laughs generously at a joke that needs it, listens through a song with too many verses and looks pleased whenever somebody glances toward her as though recognizing the guard.{/n}''', c('[Leave after the last performer.]', "outside")),
    n("outside", "Irabeth", '''{n}Outside, Irabeth stops under the overhanging roof and laughs without saying anything first.{/n}
"I wanted that so much."
{n}She looks almost astonished by her own happiness.{/n}
"They laughed at the toll exemption. I knew it was funny. Then I began wondering whether I merely wanted it to be."
"You were good."
"Say which part."
{n}She catches herself and shakes her head.{/n}
"No. I am not correcting the compliment. I want to hear it again with more detail. I warned you I might be vain."
{n}You tell her about the clerk's final line. She listens with shameless attention. When you imitate the duke badly, she corrects the voice and makes you try it a second time.{/n}
"There. Now you sound like a man who believes damp wool is a personal insult."
{n}She leans closer, her coat brushing your arm.{/n}
"I would like to celebrate. What would you enjoy?"''',
      c('"A walk. Tell me every moment you want to remember."', "walk", flags=("irabeth.applause_walk",)),
      c('"A quiet corner, with your attention on me for a while."', "corner", flags=("irabeth.applause_close",))),
    n("walk", "Narrator", '''{n}You take the lane around the storehouse. Irabeth recounts the performance in an order that has more to do with pleasure than chronology. She remembers the woman putting down her mending, the soldier leaning forward, Dema covering a smile when the road invited the duke to visit.{/n}
{n}At the next crossing she stops herself.{/n}
{n}"You were there. I am telling you things you saw."{/n}
{n}"You are telling me what you saw."{/n}
{n}She considers that, then continues without apologizing. The walk becomes longer than either of you proposed. When you pass a dark shop window she looks at your reflections walking together, then takes your hand.{/n}
{n}"I shall want this again. It may be less good. I shall probably have to endure that."{/n}
{n}"Probably."{/n}
{n}"You might have lied a little."{/n}
{n}She is still smiling when you turn toward headquarters.{/n}''', c('[Let the walk take the time you both want.]', "kiss_question")),
    n("corner", "Irabeth", '''"That is a fair complaint against an evening in which I have been applauded."
{n}She takes you to a sheltered doorway away from the departing audience. It is open to the lane, quiet enough that you do not have to compete with conversation.{/n}
"Tell me what you wanted to say while I was describing myself so enthusiastically."
{n}You begin with something that troubled you earlier in the day. Irabeth listens. Once, she opens her mouth to suggest a solution, then asks whether you want one. You tell her. She accepts the answer and stays with the part you actually wanted to say.{/n}
{n}When you have finished, she touches your forearm.{/n}
"I enjoyed being seen tonight. I do not want to become so absorbed in it that I forget to look at you. You may remind me before I have made an entire speech."
{n}Her smile returns.{/n}
"A small reminder. I have become dangerously fond of speeches."''', c('[Stay close in the quiet doorway.]', "kiss_question")),
    n("kiss_question", "Irabeth", '''{n}She turns toward you. The merriment in her face has softened into something more intent.{/n}
"May I kiss you before we go? I have wanted to since you told me about the clerk."
{n}Her hand rests near yours. She has asked plainly and waits just as plainly for your answer.{/n}''',
      c('[Kiss her and let the celebration linger.]', "kiss"),
      c('[Take her arm and walk back together.]', "arm")),
    n("kiss", "Narrator", '''{n}Irabeth's kiss is warm and rather less careful than her first entrance into the hall. She draws you close, then eases her hold when you shift, letting you find the distance you want.{/n}
{n}When you part, she rests her cheek against yours for a moment.{/n}
{n}"I am going to be very difficult to live with this evening."{/n}
{n}"Only this evening?"{/n}
{n}"You have become bold."{/n}
{n}She kisses you once more, briefly, as though agreeing with the accusation.{/n}''', c('[Walk back with her.]', "end")),
    n("arm", "Narrator", '''{n}She offers her arm with a little flourish borrowed from the guard. You take it, and she immediately complains that the guard would have charged a toll.{/n}
{n}The joke lasts half the walk. Afterward, you fall into a quieter conversation about the song's unnecessary verses. Irabeth remembers a better ending, sings two lines under her breath and stops when she sees you listening.{/n}
{n}"Another performance costs extra."{/n}
{n}She does not move her arm away.{/n}''', c('[Enjoy the walk without asking for more.]', "end")),
    n("end", "Irabeth", '''{n}At headquarters she stops before the door.{/n}
"Thank you for coming. I am trying to say that without suggesting your presence was a charitable act. I wanted you there because I wanted to share the evening."
{n}She glances back toward the lane.{/n}
"Tomorrow I have to answer what happened to the practice repairs and the warehouse inquiry. Tonight I would like to remember that a room full of people laughed when I intended them to."
{n}Her smile broadens again.{/n}
"I may even remember it while answering the difficult questions. That would be a useful improvement."''',
      c('[Keep the evening as something you did together.]', flags=("irabeth.performance_kept",))),
], requires=("irabeth.account_resolved",), delay=48)


s("the_cost_afterward", "The part the report did not finish",
  '"What has happened since the wagon was returned?"', [
    n("start", "Irabeth", '''{n}Irabeth has two practice swords across her knees. One has a split grip. The other is sound, but the leather binding is worn almost through.{/n}
"There are several answers. None fits into the line where I wrote that the goods had been returned."
{n}She sets the swords on the bench, leaving the damaged one apart.{/n}
"Hadran has completed the first review. He can repeat everything he should have done. He still believes Brena would have been easier to treat fairly if she had been more respectful. I told him that was precisely why the review was not complete."
{n}Her expression hardens, then eases.{/n}
"He stayed to help sort these. I think he hoped it would let us end the day on something he knew how to do well. I let him. Then reminded him which conversation we would resume tomorrow."
{n}She moves over to make room for you.{/n}
"As for the choice we made about Ordel..."''',
      c('[Ask what keeping the account sealed has cost.]', "sealed", requires=("irabeth.account_sealed",)),
      c('[Ask what followed the disclosure.]', "open", requires=("irabeth.account_open",))),
    n("sealed", "Irabeth", '''"The warehouse inquiry has continued. Ordel has identified a second delivery point. I cannot tell you that the whole business is ended. It has given the investigators somewhere useful to look."
{n}She touches the split practice grip.{/n}
"These have not been repaired. Two groups will share the sound weapons. I shall hear complaints. I have written the reason down so that nobody invents a shortage caused by Brena's compensation. The detention caused it. Paying for the detention merely made the loss visible."
"And Brena?"
"She has finished the delayed work. She declined a request to attend an officers' discussion of supply rules. The clerk had described her as a satisfied claimant. I corrected the description."
{n}Irabeth rubs a thumb along the sound sword's binding.{/n}
"She sent a message that was mostly unflattering. It ended with a price for new grips. A fair price. I have accepted it."
{n}Her smile is small.{/n}
"She may dislike me and still do good work. I have no intention of requiring affection from my suppliers."''', c('"And what do the officers say about your decision?"', "officers")),
    n("open", "Irabeth", '''"Ordel has found work with a different carrier. The pay is worse. He brought the final account himself so that I could see the difference."
{n}She folds her hands between her knees.{/n}
"The warehouse has changed its delivery arrangements. The investigators have lost the easy trail. They have other methods. They are slower. I was asked whether clearing one smith was worth it."
"What did you say?"
"That if we intended to charge people the cost of being suspected, we should stop pretending our inquiries were protection. Then I returned to my room and became angry about how much more difficult the investigation had become."
{n}She looks at you without asking you to repair the contradiction.{/n}
"Brena has taken another watch order. She says she prefers knowing how to make us answer. Ordel says he prefers the wage he had before. The boy and his sister are safe with their aunt. None of those facts cancels the others."
{n}She draws the damaged sword toward her and examines the grip.{/n}
"I can defend the decision. I have not come to like every part of it."''', c('"What will you do when the next officer has to make the same choice?"', "officers")),
    n("officers", "Irabeth", '''"I have drafted an instruction. A seizure must name the grounds, record the owner's answer as given and have a review time attached to it. A missing document is a question to investigate. It is not permission to keep asking until the owner gives up."
{n}She hands you the short page. The last paragraph concerns protected sources.{/n}
"That part is harder. I can make an officer record that evidence has been withheld. I cannot make every source safe to expose. I want a second officer to review those cases, one who did not order the seizure."
"Does that solve it?"
"No. It gives the next Brena someone to argue with who has not already spent two days explaining why she ought to be grateful. That is worth the inconvenience."
{n}She points to a line beneath the heading.{/n}
"The instruction is mine. One of the senior officers suggested sending it out under your name. He said it would meet less resistance. He may be right. I dislike how much I want my own name left on it."''',
      c('"Keep your name. Argue for it in the officers\' meeting."', "name", flags=("irabeth.instruction_her_name",)),
      c('"Send it as your instruction with my explicit support. Let them dispute the work instead of your authority."', "support", flags=("irabeth.instruction_supported",))),
    n("name", "Irabeth", '''"Then I will."
{n}She sounds relieved, then annoyed at the relief.{/n}
"I was about to thank you for allowing it. That is a habit I should notice more often. I have authority to issue this. I wanted somebody to tell me that enjoying the authority did not make the instruction suspect."
{n}She folds the page along its existing crease.{/n}
"I shall have to stand there while men who have never lost a night's sleep over their own names explain why mine is a distraction. Some will have useful objections. I will need to hear those too."
{n}Her smile acquires a hard edge.{/n}
"I intend to be unpleasantly well prepared. I may even enjoy that part."''', c('[Ask what help she actually wants.]', "help")),
    n("support", "Irabeth", '''"I would welcome the support. Leave the instruction in my name. I want the responsibility where I can answer for it."
{n}She takes a clean sheet and writes a space for your endorsement beneath her signature.{/n}
"They may say I obtained it because you enjoy my company. Some would say that about any woman you listened to. I will not make my work less effective to satisfy an accusation that changes shape whenever it is answered."
{n}She looks up.{/n}
"Read it again before you sign. If you disagree with the review period, say so. I do not want to find out that a private kindness has put a poor instruction into the watch's hands."
{n}You review the wording together. She accepts one clarification and argues against another until you understand why she wants it left in. The endorsement goes beneath a document you have actually considered.{/n}''', c('[Ask what she wants after the meeting.]', "help")),
    n("help", "Irabeth", '''"An audience who will ask the difficult question before the people determined to embarrass me do. You have been reasonably effective at that."
{n}She leans back against the wall.{/n}
"And afterward, I want to stop. I know that is the difficult part. I could spend every evening revising the instruction until it anticipates every bad officer in Mendev. I would become a very tired woman with a very long page."
{n}Her gaze rests on you.{/n}
"I would like an evening in which I can want your hands on me without first describing everything I have accomplished. You may be disappointed by how little useful information I intend to provide."
{n}The directness makes her blush. It does not make her withdraw the invitation.{/n}''',
      c('"I would like that evening. Ask me when you are ready."', "end", flags=("irabeth.private_invitation",)),
      c('"I want time with you, but I would rather keep it gentle for now."', "gentle", flags=("irabeth.private_gentle",))),
    n("gentle", "Irabeth", '''"Then gentle. I shall still want you there."
{n}She offers her hand and lets you choose whether to take it.{/n}
"I am learning that asking directly makes disappointment much simpler. I can be disappointed for a moment instead of constructing an entire explanation in which you were secretly unhappy all evening."
{n}Her fingers settle comfortably around yours.{/n}
"Do not look so concerned. I am pleased. I would like to keep finding out what we enjoy together."''', c('[Arrange the quieter evening.]', "end")),
    n("end", "Narrator", '''{n}You leave the swords on the bench for the next inspection. Irabeth folds her instruction and puts it with the papers she will take to the meeting. Then she takes a separate scrap and writes the evening you have chosen.{/n}
{n}She pins it where she will see it when reaching for the report.{/n}
{n}"There. An order addressed to someone particularly difficult."{/n}
{n}"Will she obey?"{/n}
{n}"She has excellent reasons to consider it."{/n}''', c('[Keep the appointment.]', flags=("irabeth.costs_kept",))),
], requires=("irabeth.performance_kept",), delay=48)


s("without_an_account", "No account of the day required",
  '"We kept this evening free."', [
    n("start", "Irabeth", '''{n}Irabeth meets you at headquarters and takes you to the room above the tack store. She has brought a blanket for the window bench and a small loaf wrapped in cloth. There are no pages in her hands.{/n}
"Dema says she recently replaced a troublesome chair. She advised me to avoid testing this one too enthusiastically."
{n}Irabeth sets the bread aside before turning toward you.{/n}
"I thanked her for the warning. I believe she was disappointed that I gave her nothing better to repeat."
{n}The window is open a little. The room smells of cool air and the leather stored below. She shakes out the blanket, spreads it over the bench and sits, testing whether it has improved the boards.{/n}
"It has not become a palace. I thought you should know before becoming attached to the luxury."
{n}She reaches for your hand.{/n}
"I have been looking forward to seeing you all day."''', c('[Sit with her.]', "morale")),
    n("morale", "Irabeth", '''{n}For a moment she seems about to give you a report. She notices the impulse, closes her mouth and considers a different beginning.{/n}''',
      c('"How are you, apart from the work?"', "broken", requires=("broken",)),
      c('"How are you, apart from the work?"', "encouraged", requires=("encouraged",), forbids=("broken",)),
      c('"How are you, apart from the work?"', "ordinary", forbids=("broken", "encouraged",))),
    n("broken", "Irabeth", '''"Tired. Pleased to be here. Both."
{n}She keeps your hand, but looks toward the open window.{/n}
"This morning I could not bear the sound of someone correcting a recruit in the yard. Nothing cruel was happening. I knew that. My body had already decided otherwise."
{n}She draws a breath and lets it go slowly.{/n}
"I did my work. I am not telling you that to make the rest unimportant. I know what I have said about myself on bad days. I still hear it when nobody else is speaking."
{n}Her thumb moves against your knuckles.{/n}
"Do not ask this evening to prove I am better. I would like to enjoy it even if tomorrow is difficult. I can tell you when I want to stop. I would like you to believe me about wanting to begin."''', c('"I believe you. Tell me what would feel good tonight."', "want")),
    n("encouraged", "Irabeth", '''"Better able to answer that without looking for a reason I ought to be worse."
{n}She smiles, then becomes thoughtful.{/n}
"I still have days when every mistake feels like evidence in a case that has already been decided. The good days have begun to feel less like something I must preserve by refusing to notice them."
{n}She lifts your joined hands and kisses your fingers.{/n}
"Today I wanted the meeting to end because I had somewhere I wanted to go. That is a rather ordinary wish. I was pleased to discover how strong it was."
{n}Her eyes stay on yours.{/n}
"I do not want to turn you into the explanation for all of it. You are the person I wanted to meet tonight. That is quite enough to make me happy to see you."''', c('"Then let us enjoy the evening we have."', "want")),
    n("ordinary", "Irabeth", '''"Interested in seeing what happens when I stop preparing for the next question."
{n}She smiles at the answer, as though it has surprised her.{/n}
"I thought about this room during the meeting. That was unprofessional of me. I continued to hear the objections, so I believe the watch survived."
{n}She turns your hand in hers, examining a small mark as though it deserves attention simply because it belongs to you.{/n}
"I do not have a grand account of myself tonight. I wanted an evening with you. I made arrangements. Now you are here, and I would rather find out whether you are comfortable than explain why I deserve it."
{n}She moves closer, leaving you room to choose the same distance or a different one.{/n}''', c('[Tell her what you want tonight.]', "want")),
    n("want", "Irabeth", '''"I want to be touched because you like touching me. I want to hear if something is awkward, without having to guess from how politely you hold still."
{n}The frankness brings warmth to her face. She brushes a stray strand of hair away from her temple.{/n}
"I am stronger than some people expect and less certain than others assume. Neither tells you what I enjoy. You can ask. I can answer. We have been reasonably good at conversation when I remember to let you speak."
{n}Her smile grows.{/n}
"Would you like me to begin by being quiet?"''',
      c('[Kiss her and draw her close.]', "close"),
      c('"Hold me. I want a quiet evening against you."', "rest"),
      c('"I want your company, but no touch tonight."', "space")),
    n("close", "Narrator", '''{n}You kiss her. Irabeth leans into it, one hand warm at the back of your neck, the other braced beside you on the bench. When you touch the open collar of her shirt, she pauses and looks at you.{/n}
{n}"Yes," she says, before you need to finish the question.{/n}
{n}You smooth the cloth aside at her shoulder and kiss the warm skin there. Her breath catches. She laughs softly when you look up, then pulls you close enough to kiss you again.{/n}
{n}The bench is narrow. You adjust, she moves the blanket, and both of you discover that enthusiasm does not improve the furniture. Irabeth rests her forehead against yours while the laughter passes.{/n}
{n}"We could stand," she suggests.{/n}
{n}You do. The window is cool against her back until she guides you a little farther into the room. Her hands settle at your waist. She watches your face as you find a comfortable closeness, then kisses the corner of your mouth with deliberate care.{/n}
{n}"Better."{/n}''',
      c('[Keep the rest of the evening private together.]', "private", flags=("irabeth.private_night",)),
      c('"This is what I wanted. Let us stay here a while."', "held", flags=("irabeth.private_kissed",))),
    n("private", "Narrator", '''{n}You close the window. Irabeth checks that the door is latched, then comes back to you without looking for another task. She asks what you want. You ask her. The answers are given in words and in the small, unmistakable ways you move toward one another.{/n}
{n}Later, the blanket is around your shoulders and the bread has been reduced to an uneven heel. Irabeth sits close, her collar still loose. She looks at the empty space where she usually puts papers and begins to laugh.{/n}
{n}"I have spent an entire evening without explaining a shortage."{/n}
{n}"There is very little bread left."{/n}
{n}"Then we must ration the final piece. I volunteer to conduct the inspection."{/n}
{n}She breaks it in half and gives you the larger portion, then steals a bite from it when you begin to object. Her satisfaction makes the theft impossible to regard as accidental.{/n}''', c('[Stay until it is time to leave together.]', "end")),
    n("held", "Narrator", '''{n}Irabeth settles her arms around you and rests her cheek against yours. There is no hurry in the way she holds you. When your position becomes uncomfortable, you tell her, and she shifts with a murmured complaint about architects who have never wanted to embrace anybody.{/n}
{n}Eventually you return to the bench, sitting sideways beneath the blanket. You share the bread and talk about nothing that needs to be completed before leaving. Once she reaches to kiss you, then waits for your smile before closing the distance.{/n}
{n}"I would like to remember this room for something besides its excessive supply of benches," she says.{/n}
{n}You tell her it is improving its reputation.{/n}''', c('[Let the evening end at the pace you chose.]', "end")),
    n("rest", "Narrator", '''{n}She puts an arm around you. You find a comfortable place against her shoulder, and she draws the blanket over both of you without making a ceremony of it.{/n}
{n}For a while she watches the window. Then you feel her settle more fully beside you. Her hand rests open against your arm.{/n}
{n}"I had a speech prepared about not being very good at this," she says.{/n}
{n}"You may omit it."{/n}
{n}"A merciful decision."{/n}
{n}The street sounds drift in through the narrow opening. When you begin to grow cold, she asks before pulling you closer. Later you share the bread and remain on the bench until the room has grown dim enough that she must light the lamp to find her coat.{/n}
{n}She looks rested when she turns back to you, without making the evening responsible for every tired morning still to come.{/n}''', c('[Thank her for the quiet company.]', "end", flags=("irabeth.private_rest",))),
    n("space", "Irabeth", '''"Then I am glad you said so."
{n}She gives you room on the bench, moving the bread between you where either can reach it.{/n}
"I may look a little disappointed. I can survive that without making you repair it. I asked what you wanted because I wanted the answer."
{n}She takes a piece of bread and considers it.{/n}
"Would you prefer talk, or shall I attempt the remarkable discipline of sitting quietly?"
{n}You choose. She follows your lead, sometimes speaking, sometimes content to share the room. By the time the loaf is nearly gone, she has stopped measuring the evening against whatever she imagined before you arrived.{/n}
"I am pleased you came," she says when you rise. "That has remained true."''', c('[Leave with the affection you actually chose.]', "end", flags=("irabeth.private_space",))),
    n("end", "Irabeth", '''{n}You fold the blanket together. Irabeth takes one end, you take the other, and the simple task takes longer than it should because she keeps finding reasons to look at you.{/n}
"I would like to do this again. Some version of it. We need not preserve every detail as though we have found the only successful arrangement."
{n}Downstairs, she returns the key and pauses at the open door.{/n}
"Go where you promised to go next. I shall do the same. I would like our next meeting to begin with neither of us wondering who spent tonight waiting."
{n}She smiles at you before stepping into the lane.{/n}
"And I shall bring more bread."''',
      c('[Part for the night with another invitation welcome.]', flags=("irabeth.private_evening_kept",))),
], requires=("irabeth.costs_kept",), delay=48)


s("after_the_shared_answer", "The invitation that remained",
  '"You invited me to continue with you separately. I would like to answer."', [
    n("start", "Irabeth", '''"I did. I have not changed my mind."
{n}Irabeth gives you room to sit beside her. There is no effort to make the moment resemble a first confession.{/n}
"We have been lovers. We have spoken with Anevia about what we could make together, and we have decided to continue separately. I will not pretend the decision was a return to the day before anything happened."
{n}She turns her ring once.{/n}
"Anevia said she is willing for our marriage to include my continuing with you. She and I have spoken again about the time we want for ourselves. I want that time. I also want to see you."
{n}Her expression becomes intent.{/n}
"I am asking for our own relationship. No promise that it will quietly become a shared romance if we behave well enough. No pretending the things we enjoyed together were a mistake merely because we are choosing differently now."''',
      c('"I want that too. What do you want us to keep?"', "terms"),
      c('"I do not want to continue as your lover."', "stop"),
      c('[Think about the invitation and return later.]', abort=True)),
    n("terms", "Irabeth", '''"The ability to say where we are going. The private kindness. The right to argue without treating every disagreement as evidence that we should never have begun."
{n}She rests her palm on the bench between you.{/n}
"And I want more days we have actually chosen. I do not want this to become a conversation we repeat whenever we are afraid to make an appointment."
"What about other people?"
"You remain free to love them. I remain Anevia's wife. If you and she have a relationship of your own, this invitation neither grants it nor takes it away. I will answer for what I want with you."
{n}Her smile returns, small and determined.{/n}
"At present I want you to hear a rather ridiculous recitation I have volunteered to give. After that, I want your help with a dispute over a wagon of cold iron. They are separate invitations. I am trying to become less apologetic about having several interests."''', c('"I accept the relationship and the invitations."', "yes")),
    n("yes", "Narrator", '''{n}She takes your hand. The touch is familiar, the relief in her face less guarded than she probably intended.{/n}
{n}"Good. I have spent enough time rehearsing the question."{/n}
{n}You sit together while she describes the guard, the duke and the missing wool. She gives the duke an offended cough and laughs when you immediately recognize the sort of man she means.{/n}
{n}The afternoon does not erase the shared conversation. It gives you something to do after it. When you part, Irabeth names a day instead of leaving the invitation suspended between you.{/n}''',
      c('[Continue the individual relationship you both chose.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.marital_terms_agreed", "irabeth.legacy_separate_history", "irabeth.boast_guard"))),
    n("stop", "Irabeth", '''{n}She lowers her eyes for a moment, then meets yours again.{/n}
"Thank you for telling me. I would have preferred the other answer. I will not ask you to give it for my sake."
{n}She folds her hands together and gives you the time to leave without finding a kinder version of what you have said.{/n}''', c('[Close only the individual romance with Irabeth.]', flags=("irabeth.closed",))),
], requires=("tirabade.group_closed", "tirabade.irabeth_continuation_invited"),
    any_of=("i_affair", "trying", "committed"), forbids=("irabeth.personal_ready", "anevia_dead", "anevia_gone"))


s("before_the_unmapped_road", "The distance they could not schedule",
  '"Before the campaign takes me away, I want to spend an hour with you."', [
    n("start", "Irabeth", '''{n}Irabeth closes the door to the counting room after asking a runner to take any urgent message to the officer on duty. She has brought no bundle of provisions. Her hands are empty.{/n}
"I nearly packed you a second whetstone. Then remembered that you already have people determined to make your baggage heavier."
{n}She sits beside you.{/n}
"I would like to give you something less sensible. A line from the guard. You can take it wherever you go and be annoyed with me whenever it becomes useful."
{n}She assumes the guard's wounded dignity.{/n}
"'I have survived three monsters on this road, my lord, and still the longest delay was a man asking whether I had filled the proper box.'"
{n}The imitation falters into a smile.{/n}
"There. Entirely impractical. I have been practicing."''', c('[Let the joke make room for the goodbye.]', "distance")),
    n("distance", "Irabeth", '''"I do not know how long you will be gone. I am resisting a strong desire to turn that into a schedule anyway."
{n}She looks at her hands.{/n}
"I can wait badly. I can become very busy, then resent a person who asks why I have not eaten. I know these things about myself. Knowing has not always prevented them."
"What would help?"
"An honest message, if there is a way to send one. No date invented to make me sleep. If you cannot send anything, I shall have to live with that. You do not need to carry the impossible task of making me unworried."
{n}She takes your hand.{/n}
"I will keep doing things here. Work, certainly. Some of the other things too. I do not want my account of the months to be only that I waited for you."''',
      c('"When I can write, I want to tell you ordinary things too."', "ordinary", flags=("irabeth.departure_ordinary",)),
      c('"I may not be able to write. I want you to have a life while I am gone."', "silence", flags=("irabeth.departure_silence",))),
    n("ordinary", "Irabeth", '''"Tell me something badly described. I have read enough precise reports."
{n}She smiles.{/n}
"A street you disliked. A meal that made you miss a less ambitious cook. Someone who said something so foolish that you looked around for a person to share it with. I would like to be that person, even if I receive the story late."
{n}Her fingers tighten briefly around yours.{/n}
"I shall try to answer in kind. I cannot promise the letters will find you. I can promise not to fill them entirely with assurances that everything is well. You know too much about Drezen to believe that."
{n}She leans closer.{/n}
"And if I write that I miss you, you are not to take it as an instruction to abandon the road. It will mean I miss you."''', c('[Tell her what you will miss about these evenings.]', "touch")),
    n("silence", "Irabeth", '''"I intend to. You may need to remind me when you return and find I have written an instruction longer than the city walls."
{n}She studies your joined hands.{/n}
"If you cannot send a word, I shall not decide that silence proves you have stopped caring. I may fear it. That is different from turning the fear into an accusation."
{n}Her eyes rise to yours.{/n}
"You may change. So may I. I would rather meet the person who returns than demand that you spend every dangerous day preserving the exact evening I liked best."
{n}She laughs quietly.{/n}
"Though I reserve the right to remind you that the evening was very good."''', c('[Let her know what you want to return to.]', "touch")),
    n("touch", "Irabeth", '''{n}She stands and holds out her arms, leaving the invitation clear.{/n}
"I have said the sensible things. Some of them twice. I would like to hold you before I discover another."''',
      c('[Step into her embrace and kiss her goodbye.]', "kiss"),
      c('[Let her hold you quietly.]', "hold")),
    n("kiss", "Narrator", '''{n}Irabeth gathers you close. Her kiss begins urgently, then slows when you rest your hand against her cheek. She stays with that touch for a moment, eyes closed, before kissing your palm.{/n}
{n}"I would like you back," she says. "That is the whole unreasonable wish."{/n}
{n}You hold her until neither of you is trying to make the goodbye shorter by making it sound easier. When she steps back, she keeps one hand in yours long enough to look at you properly.{/n}''', c('[Carry the goodbye you actually shared.]', "end")),
    n("hold", "Narrator", '''{n}You step into her arms. She holds you firmly, adjusts when you shift and rests her cheek beside yours. For a while there are no words to arrange.{/n}
{n}Footsteps pass outside. Irabeth hears them without moving away. Only when they have faded does she loosen her hold.{/n}
{n}"Come and find me when you can," she says. "I would like the next conversation."{/n}''', c('[Keep the quiet goodbye.]', "end")),
    n("end", "Irabeth", '''{n}At the door she gives you the guard's most solemn bow. It is ridiculous and exactly what she promised.{/n}
"Go before I put the whetstone in your pocket after all."
{n}Her smile lasts until you turn away. When you look back, she has begun gathering the cups you used, doing an ordinary thing with more care than it needs.{/n}''',
      c('[Leave for the campaign when you are ready.]', flags=("irabeth.departure_kept",))),
], requires=("irabeth.private_evening_kept",), chapters=(3,), delay=24)


s("an_unposted_line", "A line with nowhere to send it",
  '[During a quiet rest, write something for Irabeth.]', [
    n("start", "Narrator", '''{n}You find a few minutes in which no one needs an answer. The surface beneath your paper is uneven. You move the page twice, then begin anyway.{/n}
{n}There is no reliable route by which this letter will reach Drezen. You write her name without pretending that ink can solve the distance.{/n}
{n}The first sentence sounds like a report. You cross out the rank, start again and discover that describing an ordinary moment can be harder than naming a danger. You want to tell her something that belongs to the person who laughed at the guard, not only the officer who will ask whether the road is passable.{/n}''',
      c('[Describe a small absurdity that made you wish she were beside you.]', "absurd", flags=("irabeth.abyss_absurd",)),
      c('[Write honestly about a moment when you were frightened.]', "fear", flags=("irabeth.abyss_fear",)),
      c('[Put the paper away for another rest.]', abort=True)),
    n("absurd", "Narrator", '''{n}You write about a conversation in which every answer made the next question less sensible. You cannot capture the speaker's expression, so you describe how Irabeth might have played it: a dignified pause, a wounded look, a refusal to admit that the wool had never been mentioned.{/n}
{n}You hear her answering in your imagination. It is an answer made from memory, not a message crossing the planes. You leave room beside the paragraph for whatever she actually says if she ever reads it.{/n}
{n}Then you write that you wanted her hand in yours afterward. It is the plainest sentence on the page. You resist improving it.{/n}''', c('[Finish the letter without inventing a delivery.]', "end")),
    n("fear", "Narrator", '''{n}You describe the moment without making yourself either invulnerable or helpless. There was something you had to do. You were afraid. You did it, or chose another way, and the fear did not vanish merely because the decision had been made.{/n}
{n}You remember that Irabeth has asked you for honesty, not a heroic account. You let this page contain a difficult moment without requiring the next paragraph to cure it.{/n}
{n}At the end, you write that you would like to sit beside her without explaining every silence. You do not ask her to become responsible for carrying what happened here. You tell her what you miss.{/n}''', c('[Fold the page for a possible return.]', "end")),
    n("end", "Narrator", '''{n}You fold the letter and keep it with your own belongings. Nobody comes with a letter from Drezen. You smooth the fold once more, then stop before the paper wears through.{/n}
{n}The page is something you may choose to give her if you meet again. For now, it has let you say what the next interruption might otherwise have swallowed. You put it away and return to the place where you actually are.{/n}''', c('[Keep the unposted letter.]', flags=("irabeth.abyss_written",))),
], requires=("irabeth.departure_kept",), chapters=(4,), remote=True, owner="Rest", delay=0)


s("the_person_who_returns", "The person at the door",
  '"We have time to speak again. What has changed for you?"', [
    n("start", "Irabeth", '''{n}Irabeth looks up as you approach. Whatever she was about to say about the papers before her stops when she sees that you have come to stay a while.{/n}
"Yes. I would like that."
{n}She puts the papers aside and moves to the chair near the window. The room is familiar. The expression with which she waits for you belongs to this particular day.{/n}''',
      c('"We said goodbye before I left. I wanted this conversation."', "returned", requires=("irabeth.departure_kept",)),
      c('"We were already lovers before I left, though we had no private farewell."', "earlier", requires=("irabeth.began_chapter_three",), forbids=("irabeth.departure_kept",)),
      c('"These new evenings matter to me. I want to keep finding time for them."', "late", requires=("irabeth.began_chapter_five",), forbids=("irabeth.departure_kept", "irabeth.legacy_shared_history", "irabeth.legacy_separate_history", "irabeth.single_affair_disclosed", "irabeth.legacy_bereaved_history")),
      c('"We have an older relationship as well as these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_bereaved_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We have an older relationship as well as these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_shared_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We have an older relationship as well as these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_separate_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We have an older relationship as well as these new days. I want to hear how you are now."', "older", requires=("irabeth.single_affair_disclosed",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three"))),
    n("earlier", "Irabeth", '''"I missed you. We did not have to make a farewell for that to happen."
{n}She lets the words stand before reaching for your hand.{/n}
"I kept living here. I thought about the evenings we had, sometimes when I ought to have been thinking about something else. I wanted to know whether you would come back wanting another."
{n}Her smile is a little uncertain.{/n}
"I am glad you have. I will not demand an account of every silence between then and now. Tell me what you want me to know, and ask me the same. We can begin with the people actually in the room."''', c('[Begin the conversation you did not need a farewell to want.]', "history")),
    n("older", "Irabeth", '''"Thank you for remembering that. I do not want our new appointments to make everything before them disappear."
{n}She moves closer, giving you room to take her hand if you wish.{/n}
"We have chosen things together before. We are choosing more now. I can be glad of a new day without pretending I met you for the first time at the storehouse."
{n}She smiles at the thought.{/n}
"I might have been less solemn if I had. Or more. I have never been particularly reliable about that."
{n}Her attention settles on you.{/n}
"Tell me what you want me to know about today. We need not make a complete history out of one afternoon."''', c('[Speak about the present without erasing the earlier relationship.]', "history")),
    n("returned", "Irabeth", '''"So did I. I imagined it badly several times. You were always either in desperate need of comfort or inexplicably untouched by everything. Neither version gave you much room to speak."
{n}She offers her hand, then waits for you to take it.{/n}
"I am glad you are here. I have questions. I may ask the wrong one first. You may tell me to leave a thing alone."
{n}Her fingers close around yours when you sit.{/n}
"I kept remembering the guard's complaint about the proper box. It became useful more often than I hoped. I wanted to tell you when it did."
{n}She smiles, then grows quiet.{/n}
"I will not put the whole time between us into one embrace. But I would like the embrace, if you would."''',
      c('[Hold her before beginning the conversation.]', "history"),
      c('[Keep her hand and begin with words.]', "history")),
    n("late", "Irabeth", '''"I am glad we found our way to these evenings."
{n}She sits beside you, close enough to make the invitation clear without assuming you will want to take it.{/n}
"I remember the uncertainty before we began meeting as lovers. We need not turn that waiting into a farewell we never made. I have enjoyed the days we have actually had, and I would like to hear how they have been for you."
{n}She glances at the papers she left behind.{/n}
"The city can make every new pleasure seem badly timed. There is always a list of people who need something first. I am trying to remain useful without requiring every evening to pass that test."
{n}Her smile becomes warmer.{/n}
"You have been a considerable distraction from the list. I would like to continue being distracted."''', c('[Talk about the days you have actually shared.]', "history")),
    n("history", "Irabeth", '''{n}The conversation moves slowly enough for both of you to choose what to say. Some subjects ask for more care than others.{/n}''',
      c('[Give her the letter you wrote and kept.]', "letter", requires=("irabeth.abyss_written",)),
      c('"You told me about the Queen at Iz. I have not forgotten what you said."', "queen", requires=("irabeth.queen_loss_known",)),
      c('"I want to speak once about the harm I did to you. You need not answer me."', "scar", requires=("irabeth.scar_known",)),
      c('"Tell me what you want from the days ahead."', "ahead")),
    n("letter", "Narrator", '''{n}Irabeth takes the folded page. She sees the wear along its creases before reading the first line.{/n}
{n}"You kept it."{/n}
{n}You tell her there was no reliable way to send it. She nods and reads without treating the absence of a delivery as another wound to be explained.{/n}
{n}Halfway down, her thumb stops moving along the paper's edge. She finishes, folds it carefully and keeps it in her hand.{/n}
{n}"I am glad to know this about the time I could not see," she says. "I do not have the answer I would have written then. I have the one I can give you now."{/n}
{n}She takes your free hand. For a while that is the answer. Later she asks one question about the moment you described and listens to what you choose to add.{/n}''', c('[Let the letter become part of a real conversation.]', "ahead", flags=("irabeth.letter_given",))),
    n("queen", "Irabeth", '''{n}Her face stills.{/n}
"I said that people should not rely on me. I remember."
{n}She looks toward the window, giving herself time before continuing.{/n}
"I had been entrusted with something I did not keep safe. There is no clever sentence that makes me comfortable with it. I do not want you to find one because you would like me to smile at you."
{n}She turns back.{/n}
"I can want you here and still be angry with myself. I can hear that you care without letting it decide what I believe about Iz. Those things may remain beside each other for a long time."
{n}Her hand rests near yours.{/n}
"Today I would like a conversation about something I can still do. I am not asking you to forget what I told you. I am asking to choose the next subject."''', c('"Choose it. I will listen."', "ahead")),
    n("scar", "Irabeth", '''{n}Her hand rises toward her cheek, then lowers.{/n}
"I have told myself that I deserved to be stopped. I do not want to spend tonight defending that thought or discussing the mark."
{n}She holds your gaze.{/n}
"I do not want a private evening spent persuading you that I bear it nobly. If you mean to acknowledge it, do so without asking me to make you feel forgiven."
"I hurt you. I will not call that proof that I knew what you needed."
{n}She is silent for a while.{/n}
"I have heard you. I do not want to discuss the mark tonight. And I do not want you to touch my face while we leave the subject."
{n}You keep your hands where she can see them. She draws a breath and chooses what to say next herself.{/n}''', c('[Respect the boundary she has stated.]', "ahead", flags=("irabeth.harm_acknowledged",))),
    n("ahead", "Irabeth", '''"I want the instruction to work when I am not standing over the officer using it. I also want to go somewhere after the war without being invited to inspect the defenses."
{n}The second admission brings a little warmth back into her voice.{/n}
"There is a route-maker in the city. Sella. She has a collection of old road drawings, some useful and some apparently intended to make travelers admire the artist. I asked whether she would show me how she chooses between them."
"For the watch?"
"For me. She asked the same question. I found it irritating both times."
{n}Irabeth smiles to soften the rebuke.{/n}
"The instruction will need a final review. After that, I would like to spend an afternoon learning enough about a road to choose it for pleasure. You could come. You are allowed to prefer a different road."''', c('"I would like to see what you choose."', "end")),
    n("end", "Irabeth", '''{n}She returns to the desk only long enough to take a small sheet from beneath the work papers. It names Sella and an hour, with two alternative days beneath it.{/n}
"She gave me alternatives because I kept saying that something might happen. Apparently something may also happen to her. I found the reminder helpful and mildly offensive."
{n}You choose a day together. Irabeth puts it where she will have to see it before accepting another appointment.{/n}
"There. A future small enough to put on a page, and large enough that I want it."''',
      c('[Keep the next day you have chosen together.]', flags=("irabeth.return_kept",))),
], requires=("irabeth.private_evening_kept",), chapters=(5,), delay=48)


s("when_the_instruction_is_used", "A rule in somebody else's hands",
  '"You wanted to see the instruction used without you directing every answer."', [
    n("start", "Narrator", '''{n}Irabeth meets you at headquarters with a short stack of completed reviews. She has arranged for you to observe one of the cases being reconsidered under her instruction. It concerns a basket of healing supplies held after a delivery tally failed to match the contents.{/n}
{n}"Before we go," she says, "the officer must give her answer before I improve it for her."{/n}
{n}"Does she know you are coming?"{/n}
{n}"Yes. It is an observation, not an ambush. She has been warned that I may look displeased while thinking."{/n}
{n}The review takes place in a room beside the stores. Officer Vela has set out the tally, the basket and a written statement from the carrier. She asks Irabeth to sit where the claimant can still see her clearly. Irabeth obeys with a look that suggests the request has already made the visit worthwhile.{/n}
{n}The claimant, a woman named Pella, has brought an empty medicine jar and an angry account of the time she lost returning for her goods.{/n}
{n}Vela lets her finish before asking about the missing packets.{/n}''', c('[Listen without answering for the officer.]', "hearing")),
    n("hearing", "Narrator", '''{n}Pella says three packets had been combined into one larger packet because the smaller cloths were wet. Vela opens the bundle in her presence. The quantities match. The tally describes containers, not measures.{/n}
{n}"Then the goods are yours to take," Vela says. "The hold should have ended when the quantities were checked."{/n}
{n}"They weren't checked."{/n}
{n}"No. That is the failure I will record."{/n}
{n}Vela asks whether Pella wants a copy. Pella says she wants the half day back. The officer does not offer to provide it. She asks what work was delayed and writes the answer separately from the return of the goods.{/n}
{n}Irabeth shifts beside you when Vela begins to close the review. Her hand rises slightly, then settles again. Vela sees it.{/n}
{n}"Something missing, ma'am?"{/n}
{n}"You tell me."{/n}
{n}The younger officer looks over the instruction. Her face changes. The detention had no review time entered. She adds that omission to the account, then reads the entire finding to Pella.{/n}
{n}The woman takes her basket. She remains annoyed, but she no longer has to ask permission to leave with it.{/n}''', c('[Speak with Vela after Pella leaves.]', "vela")),
    n("vela", "Irabeth", '''"You established the quantities and returned the goods promptly. You let her disagree with the way the delay was described. Those parts worked."
{n}Vela nods, then looks at the last addition.{/n}
"I missed the review time until you moved."
"Yes."
"Would you like another requirement in the instruction?"
{n}Irabeth looks at you, then back at Vela.{/n}
"I would like to know why you missed it."
{n}The officer explains that the form puts the review time beneath the final finding. It looks like an ending field. She had treated it as something to fill after reaching the decision.{/n}
{n}Irabeth turns the form around. She considers it for several seconds before answering.{/n}
"That is poorly placed. I wrote the form. Move it beside the grounds for detention, where the person beginning the hold must answer it."
{n}Vela reaches for a clean sheet. Irabeth stops her only long enough to ask her to show the proposed change to another officer before having copies made.{/n}
"If I am the only person who finds it clear, that is not enough."''', c('[Walk back with Irabeth.]', "result")),
    n("result", "Irabeth", '''"I wanted it to work exactly as I had written it. That was an unreasonable hope. I enjoyed it for several minutes."
{n}She carries the corrected example beneath her arm.{/n}
"Pella recovered her supplies. Vela found the actual question. The form made one part harder than it needed to be. That is a result I can use."
{n}At the turning she pauses, letting a laden cart pass.{/n}''',
      c('"How has keeping it in your own name affected the review?"', "name", requires=("irabeth.instruction_her_name",)),
      c('"Has my endorsement helped or complicated things?"', "endorsement", requires=("irabeth.instruction_supported",))),
    n("name", "Irabeth", '''"Two officers objected to taking instruction from me on a matter they considered beneath command attention. One had three useful changes. The other had an impressive number of ways to avoid saying he disliked being corrected."
{n}Her mouth curves.{/n}
"I accepted the changes. I asked the other man to propose a time limit for holding someone's property. He finally gave one. I put his number beside mine and made him explain the difference."
"Did he?"
"Poorly. It was a satisfying afternoon. I shall try not to let that become my preferred measure of success."
{n}She taps the example beneath her arm.{/n}
"Vela used it without asking whether I would be present to protect her from complaints. That matters more. I still intend to remember the afternoon."''', c('[Let her enjoy the achievement without enlarging it.]', "last_cost")),
    n("endorsement", "Irabeth", '''"It made them read it. A useful beginning. After that, they argued with me about the form, the compensation and whether reviewing a detention requires another officer every time."
{n}She smiles.{/n}
"They were irritated enough that I think they forgot to be impressed by your signature. I preferred them that way."
"And the personal accusation?"
"One person implied that I had an unusual way of obtaining support. I asked which paragraph he wanted changed. He had no answer prepared. I gave him time."
{n}She touches the folded page.{/n}
"You supported work you had read. I defended it. Vela used it. There will be other whispers. I am not going to spend my life waiting for every room to deserve my comfort before I enter it."''', c('[Ask about the cost still attached to the first case.]', "last_cost")),
    n("last_cost", "Irabeth", '''{n}She takes a second page from the stack. This one is short enough to read while standing.{/n}''',
      c('[Read the training and source update.]', "sealed_end", requires=("irabeth.account_sealed",)),
      c('[Read the carrier and investigation update.]', "open_end", requires=("irabeth.account_open",))),
    n("sealed_end", "Irabeth", '''"The repaired grips have arrived. The training groups are no longer sharing quite so resentfully. Brena charged what she quoted and refused to reduce the price for the watch. I paid it."
{n}She points to the next line.{/n}
"Ordel's information led the investigators to a stored lot of false bars. That lot has been seized and tested. I will not tell you it means every bad supplier is gone. It means those bars will not be issued as sound metal."
"Will Brena hear that?"
"If she asks. I am not sending the news to prove she ought to like what we did. Her complaint remains attached to the account. I have not renamed it gratitude because the investigation produced something useful."
{n}Irabeth folds the update.{/n}
"That is where the matter stands. I can close my part of the file without pretending nobody paid for it."''', c('[Let the case be complete enough to leave at work.]', "end")),
    n("open_end", "Irabeth", '''"Ordel has accepted the final payment for his lost commission. It does not make his new work as profitable. He knows I know. He has stopped bringing the difference to my door every week."
{n}She shows you the last paragraph.{/n}
"The investigators traced one false shipment through its buyer instead of the warehouse. It took longer. They recovered less than they hoped. The recovered lot has been tested and kept out of issue."
"And Brena?"
"Her next delivery was checked by quantity and returned to her forge before noon. She sent Vela a note explaining three ways to improve the tally. Vela used two. I believe that is the closest thing to praise we are likely to receive."
{n}Irabeth folds the update.{/n}
"I still prefer a course that protects a source when we can do so honestly. I also know what opening the account allowed us to correct. I do not need to stop believing one to admit the other."''', c('[Let the work have its actual result.]', "end")),
    n("end", "Irabeth", '''{n}Back at headquarters she ties the completed papers together. The changed form remains out for copying. She places the case on the finished side of the shelf and leaves it there.{/n}
"Now I would like to see Sella's road drawings. I am going to ask a question whose answer need not improve military readiness."
{n}She turns toward you with a look of deliberate challenge.{/n}
"Which view would I enjoy waking up to? I have several preferences. Some are inconvenient. I intend to defend them."''',
      c('[Keep the appointment about a road chosen for pleasure.]', flags=("irabeth.instruction_tested",))),
], requires=("irabeth.return_kept",), chapters=(5,), delay=48)


s("a_road_she_would_choose", "A road without an assignment",
  '"Sella is expecting us. Have you decided what you want to ask?"', [
    n("start", "Irabeth", '''"Whether a view described as 'sublime' can be reached without spending four days climbing through rain. The descriptions are remarkably evasive about rain."
{n}Irabeth has brought a small notebook. She holds it up before you can object.{/n}
"Personal use. I am allowed to remember things."
{n}You walk to Sella's room above a provisioner's shop. The route-maker is sorting drawings by age rather than destination. She explains that an old bridge remains an old bridge even when someone copies it beautifully onto new paper.{/n}
{n}Irabeth looks immediately interested.{/n}
"That is an excellent reason to distrust attractive handwriting."
"Only when it describes a bridge," Sella replies. "Otherwise it depends on what you want from the writer."
{n}Irabeth glances at you and discovers you already looking at her.{/n}
"We are here for roads," she says, less firmly than she intended.{/n}''', c('[Make room for the drawings.]', "drawings")),
    n("drawings", "Narrator", '''{n}Sella spreads three routes across the table. One follows a broad road between settled towns. It has inns, tolls and long views of cultivated land. Another turns into hills above a lake, with fewer stopping places and a stretch that becomes unpleasant after heavy rain. The third promises an impressive ruin and offers almost no useful information about the way home.{/n}
{n}Irabeth puts the third aside.{/n}
{n}"I have seen enough impressive ruins without arranging a holiday around another."{/n}
{n}Sella nods and shows you the notes beneath the first two. They are accounts from travelers, some agreeing, some contradicting one another. She distinguishes what she has walked herself from what she has only been told.{/n}
{n}Irabeth asks about beds. Then about whether the lake can be seen from a sheltered place. Then, with a slightly defiant look, whether anyone describes the food.{/n}
{n}"You may laugh," she tells you. "I have eaten enough meals whose chief virtue was being available."{/n}''',
      c('"I would choose the towns. A comfortable room at the end of the day matters to me."', "towns", flags=("irabeth.road_towns",)),
      c('"I would choose the lake. Fewer people, and time to stop where we like."', "lake", flags=("irabeth.road_lake",))),
    n("towns", "Irabeth", '''"So would I, some days. Then I look at the lake and imagine being somewhere no one expects me to recognize a name."
{n}She lays a finger beside the hill route.{/n}
"I would like a room. I would also like a morning outside a room with nothing to do except decide when to leave. Perhaps we could stay in the last town and walk partway rather than make every desire choose a different holiday."
{n}Sella measures the distance with a strip of cord. The walk is possible, but it would be a long day. Irabeth considers the note about rain.{/n}
"Then we keep a day with no plan after it. If the weather is bad, I intend to become very interested in the inn's breakfast."
{n}She looks pleased with the compromise, then looks at you.{/n}
"Would that be a journey you would actually enjoy, or have I merely made my preference sound reasonable?"''', c('"I would enjoy it. I want the unplanned day too."', "practice")),
    n("lake", "Irabeth", '''"That was the answer I hoped you would give. I should admit it before pretending I am considering all options impartially."
{n}She studies the stopping places again.{/n}
"But I want a bed at least some nights. And I want to be able to say I am cold without somebody reminding me that I have endured worse. I have endured many things I do not intend to buy as recreation."
{n}Sella points to a longer way with a reliable inn before the hill section. It adds distance and removes a difficult crossing.{/n}
"That one," Irabeth says, then stops. "If it suits you. I have begun giving orders to an imaginary journey."
{n}Her smile is rueful.{/n}
"I do like choosing. I also like the thought of arriving with someone who wanted to come, rather than someone who followed the most confident finger across the map."''', c('"I want to come. Keep the inn and the slower crossing."', "practice")),
    n("practice", "Narrator", '''{n}Sella gives Irabeth a copy of the relevant section and shows her how to compare the road's turns with the landmarks described beneath it. Then she sets a smaller drawing beside it: a route through Drezen with several deliberately misleading details.{/n}
{n}"You can try the method without leaving the city," she says. "Bring back the error you dislike most."{/n}
{n}Irabeth looks suspiciously pleased by the challenge.{/n}
{n}You spend the next hour following the drawing. The first mistake is easy: a stair has been shown on the wrong side of a wall. The second sends you into a yard where a man politely asks whether you intend to buy onions. Irabeth considers the mistake, buys two and announces that the detour has therefore produced a useful result.{/n}
{n}The third is harder. Two passages resemble the sketch. One looks shorter. The other follows the measurements.{/n}
{n}Irabeth looks at you, waiting to see which you prefer.{/n}''',
      c('[Follow the measurements, even though the route looks less direct.]', "measured", flags=("irabeth.walk_measured",)),
      c('[Try the shorter passage and accept the risk of returning.]', "shorter", flags=("irabeth.walk_shorter",))),
    n("measured", "Narrator", '''{n}The longer-looking route curves behind the building and reaches the marked arch without a second turning. From there, you can see why the sketch made the other passage tempting: its entrance faces the destination, but a wall blocks the way beyond it.{/n}
{n}Irabeth notes the error and then looks back along the route.{/n}
{n}"I would have chosen the other one if I had been hurrying."{/n}
{n}"We are not hurrying."{/n}
{n}"I am beginning to enjoy remembering that."{/n}
{n}You sit on a low step near the arch. She places the onions between her feet so they will not roll away, then leans back on her hands and lifts her face toward the pale afternoon light.{/n}
{n}For a few minutes she has nothing to improve about where you have arrived.{/n}''', c('[Sit beside her without finding another destination.]', "want")),
    n("shorter", "Narrator", '''{n}The passage ends at a locked service gate. Beyond it, the arch is visible and entirely unreachable without returning the way you came.{/n}
{n}Irabeth regards the gate with an expression you have seen directed at particularly poor explanations.{/n}
{n}"We are not climbing it," she says.{/n}
{n}"I had not suggested it."{/n}
{n}"I had. Silently. I am answering myself before I become persuasive."{/n}
{n}You return, take the measured route and reach the arch considerably later. Irabeth puts an emphatic note beside the misleading passage. Then she looks at the time she has spent recovering the mistake and begins to laugh.{/n}
{n}"A whole afternoon, and the only casualties are my dignity and the onions if I drop them."{/n}
{n}You find a low step where she can put the onions down. She sits beside you, still smiling at the gate she has chosen not to conquer.{/n}''', c('[Enjoy having time to get something wrong.]', "want")),
    n("want", "Irabeth", '''"I want a journey like this. Longer, with better views and fewer purchased onions."
{n}She rests her hand beside yours on the step.{/n}
"I want to choose some of it. I want to discover that I have chosen badly and be allowed to laugh before finding another road. I have spent so long treating mistakes as evidence about what sort of person I am. Sometimes a wrong passage is only a wrong passage."
{n}She looks at the drawing in her lap.{/n}
"I am not going to become a woman with no duties. I like some of my duties. I want a life in which leaving them for a while is an ordinary decision, not a dramatic betrayal of everyone who has relied on me."
{n}Her gaze meets yours.{/n}
"Would you like a place in that life? I do not mean promising to take every road I choose. I mean continuing to ask where we want to go."''',
      c('"Yes. I want a lasting relationship with you, with room for the other people we love."', "lasting", flags=("irabeth.future_lasting",)),
      c('"I want you in my life. I cannot promise a settled future, but I want to keep choosing our time."', "open", flags=("irabeth.future_open",)),
      c('"I care for you, but I want us to become friends rather than continue as lovers."', "friend", flags=("irabeth.future_friends",))),
    n("lasting", "Irabeth", '''"So do I."
{n}She takes your hand and holds it while giving the answer time to become real.{/n}
"There will be work, and other people with claims we have freely given them. I cannot promise that we will always live under one roof. I can promise that I want to keep making room for you, in days rather than only in speeches."
{n}Her smile becomes unexpectedly shy.{/n}
"I would like the journey. Afterward, I would like to come back and argue about which parts were worth the rain. I would like enough ordinary history with you that neither of us needs a war to explain why we stayed."
{n}She leans toward you and waits for your answering movement before kissing you.{/n}''', c('[Make the continuing commitment you have both chosen.]', "end", flags=("irabeth.committed",))),
    n("open", "Irabeth", '''"I can want that without pretending you offered more."
{n}She studies your hand near hers, then takes it.{/n}
"I would like another day. I would like the possibility of the road. If one of us begins wanting something the other cannot offer, we will have to say it before the disappointment becomes a private accusation."
{n}She smiles.{/n}
"For now, I am pleased to have someone with whom I can get lost near an onion seller. That is a less solemn foundation than some, but it has advantages."
{n}She leans against you briefly, choosing the small closeness without asking it to become a larger promise.{/n}''', c('[Keep the open relationship as it was actually offered.]', "end")),
    n("friend", "Irabeth", '''{n}She draws a breath and lets it go before answering.{/n}
"I am sorry. I wanted another answer."
{n}She looks at the drawing rather than turning the disappointment into a smile for your benefit.{/n}
"I can keep the friendship. I may need a little time before the next private evening. That is not a punishment. I would like to arrive because I am ready, rather than because I think you require proof that I have accepted it gracefully."
{n}After a moment she folds the drawing and looks back at you.{/n}
"The afternoon was good. I would rather keep that true than ruin it trying to make it say something you no longer want."''', c('[Respect the change in the relationship.]', "end")),
    n("end", "Narrator", '''{n}You return the exercise to Sella. Irabeth describes the misleading passage in detail. Sella asks which clue finally made her trust the drawing or doubt it, and listens to the answer before returning the exercise to its place.{/n}
{n}The real road drawing stays with Irabeth. She pays for the copy, places it inside her notebook and carries the onions home in the other hand. The afternoon has produced a plan, a mistake worth laughing at and an answer neither of you needs to improve before remembering.{/n}''',
      c('[Leave with the future you actually chose.]', flags=("irabeth.future_chosen",))),
], requires=("irabeth.instruction_tested",), chapters=(5,), delay=48)


s("the_hour_before_battle", "What she asked you to keep",
  '"Before the final fighting, I want to see you."', [
    n("start", "Irabeth", '''{n}Irabeth meets you at headquarters. She has left a clear space beside the window and moved the chair that always catches against the uneven stone. The small preparation makes the invitation feel more deliberate than a room full of candles would have.{/n}
"I have told the officer on duty where I am. We have some time. I cannot promise the city will behave itself for the whole of it."
{n}She offers you the place beside her.{/n}
"I wanted to ask you before the last preparations became an excuse for leaving everything unsaid. I have already made one speech in my head and disliked it. Too many noble sentiments. Not enough of the things I actually wanted."''', c('"Then begin with those."', "wanted")),
    n("wanted", "Irabeth", '''"I wanted to be admired. I wanted somebody to laugh because I had made a joke worth hearing. I wanted to stop being grateful whenever somebody discovered I could be gentle."
{n}She looks at you with a small, crooked smile.{/n}
"I wanted your company. Your attention. Your mouth, on several occasions when the conversation had barely begun. I have had some of those things. I am glad."
{n}She glances toward the shelf holding her completed account.{/n}
"I also wanted to do work I could defend. The wagon case was untidy. The instruction had to be changed. I can still put my name beneath it. I would like to remember that when someone tells me a good officer must never look uncertain."
{n}She turns back.{/n}
"Those are things we have actually done. I do not need to promise that the next battle will make them more deserving of memory."''', c('[Speak about the future you chose at Sella\'s drawing.]', "future")),
    n("future", "Irabeth", '''{n}She takes the road drawing from a narrow shelf. It is folded along the same lines you made together.{/n}''',
      c('"I mean the lasting relationship we chose."', "lasting", requires=("irabeth.future_lasting",)),
      c('"I mean the time we chose to keep, without pretending it was a settled household."', "open", requires=("irabeth.future_open",)),
      c('"I value the friendship we chose to keep."', "friends", requires=("irabeth.future_friends",))),
    n("lasting", "Irabeth", '''"I mean it too. I am not asking the battle to decide whether I was sincere."
{n}She unfolds the drawing enough to show the route.{/n}
"If we have the days afterward, I want to begin with a visit we can actually keep. Then the journey, when our other commitments allow it. I would like us to continue choosing each other without turning every absence into a test."
{n}Her fingers rest beside the inked road.{/n}
"I will have work to do. You may have more than either of us can imagine. I am not promising to live on the edge of your life and call every scrap of time enough. I will ask for what I need. I want you to ask too."
{n}She looks up, her expression warm and quite serious.{/n}
"That is the promise I can make before a battle. A person who will keep speaking, if we are given the chance."''', c('[Confirm the commitment without promising survival.]', "wife")),
    n("open", "Irabeth", '''"Good. I would have noticed if the goodbye suddenly supplied a house and a lifetime."
{n}Her smile softens the words.{/n}
"I want more time with you. I do not know how it will fit into every future. That was true when we sat beside the arch. It is still true while people sharpen swords downstairs."
{n}She folds the drawing again.{/n}
"I will not make the possibility of losing you an argument for obtaining a larger promise tonight. I would rather you return to an invitation you can accept honestly."
{n}She lays the paper between you.{/n}
"Come and find me, if you can. We will decide what the next day asks of us when there is a next day to choose."''', c('[Keep the invitation as open as you chose it.]', "wife")),
    n("friends", "Irabeth", '''"So do I. I have had time to be disappointed without making you watch every moment of it."
{n}She smiles with some of the ease you remember from the storehouse.{/n}
"I still want you to survive. I still want to hear what you think of a road. I may take somebody else, or go alone, or discover that the inn is more interesting than the lake. You do not need to promise to stand in the same place in every version."
{n}She puts the drawing away.{/n}
"The work mattered. The laughter mattered. I can keep them without asking the friendship to impersonate the romance."
{n}Her hand rests open on her knee.{/n}
"Thank you for coming before the fighting. I wanted this conversation."''', c('[Stay for the friendship you both value.]', "wife")),
    n("wife", "Irabeth", '''{n}Her gaze falls briefly to the ring on her hand. The movement asks for its own moment in the conversation.{/n}''',
      c('"What do you want to say about Anevia tonight?"', "wife_living", forbids=("anevia_dead", "anevia_gone")),
      c('[Give her room to speak about Anevia\'s death.]', "wife_dead", requires=("anevia_dead",)),
      c('[Give her room to speak about Anevia\'s absence.]', "wife_gone", requires=("anevia_gone",), forbids=("anevia_dead",))),
    n("wife_living", "Irabeth", '''"That I love her. That I have things to say to her which belong to us. I am glad I do not have to hide this hour from her to have it."
{n}She turns the ring once, then leaves it alone.{/n}
"We will have our own goodbye. I will probably try to make it too sensible. She will notice. We have had considerable practice."
{n}The smile carries affection without asking you to step into it.{/n}
"Whatever you and I have chosen, I will not make her part of this conversation by inventing an answer for her. She has always been very capable of supplying one herself."''', c('[Let her keep the goodbye that belongs to her marriage.]', "choice")),
    n("wife_dead", "Irabeth", '''{n}She is silent long enough that you begin to hear the small sounds outside the room.{/n}
"I wanted another goodbye with her. I do not know whether it would have been a better one. I wanted it anyway."
{n}Her hand closes around the ring, then opens.{/n}
"I can be here with you and miss her. I need neither feeling to defend itself against the other. I have become very tired of imagining a court in which every pleasure must answer for the dead."
{n}She looks at you.{/n}
"Tonight I would like to remember her laugh before I remember what I lost. You do not have to find the right thing to say. There may not be one."
{n}You sit with her while she tells a small story about a pen Anevia insisted she had not stolen. It belongs to a marriage that has not been erased by the room you now share.{/n}''', c('[Stay while she finishes the story.]', "choice")),
    n("wife_gone", "Irabeth", '''"I do not know what goodbye I am allowed to imagine. That is the honest answer."
{n}She watches the ring on her hand.{/n}
"I will not turn absence into death because death would let me finish a sentence. Nor will I tell you I know when she will return. I have neither answer."
{n}She draws a breath.{/n}
"I know what you and I have said. I know what she and I said when we could speak. I can keep those truths without filling the silence with something more convenient."
{n}Her eyes rise to yours.{/n}
"Thank you for leaving room for that. I would like the rest of this hour to belong to the people actually in it."''', c('[Let the uncertainty remain honest.]', "choice")),
    n("choice", "Irabeth", '''{n}The room grows quieter as the traffic outside moves elsewhere. Irabeth looks toward the door, then back at you.{/n}
"We still have a little time. What would you like?"''',
      c('[Kiss her, and keep the rest of the hour private.]', "night", forbids=("irabeth.future_friends",)),
      c('[Ask her to hold you.]', "hold", forbids=("irabeth.future_friends",)),
      c('[Stay and talk until it is time to leave.]', "talk")),
    n("night", "Narrator", '''{n}Irabeth stands when you do. She meets your kiss with both hands warm against your back, then draws away just far enough to see your face.{/n}
{n}"Yes?"{/n}
{n}You answer. She latches the door and returns, letting the last few steps belong to anticipation rather than haste. The hour becomes private. Neither of you asks the closeness to promise an outcome beyond the room.{/n}
{n}Later, she smooths your clothing where it has folded awkwardly and lets you do the same for her. The ordinary tenderness makes it harder to leave. You leave when you must, carrying the warmth of her hands rather than a claim that love has made the road safe.{/n}''', c('[Keep the goodbye you chose.]', "end", flags=("irabeth.farewell_private",))),
    n("hold", "Narrator", '''{n}She draws you into her arms. The hold is firm, then gentler when you settle against her. For several minutes the only words are small adjustments, a question about comfort, an answer close to her ear.{/n}
{n}When you step back, she keeps your hand long enough to press it between both of hers.{/n}
{n}"I would like to do this on a day when leaving means only going across the street."{/n}
{n}You tell her you would like that too. It remains a wish you share, without becoming a prediction.{/n}''', c('[Let her release you when it is time.]', "end", flags=("irabeth.farewell_held",))),
    n("talk", "Narrator", '''{n}You remain by the window. The conversation moves from practical matters to the storehouse, then to a particularly implausible section of Sella's drawing. Irabeth gives the misleading passage a final offended description and makes you laugh.{/n}
{n}When the hour has nearly gone, she falls quiet. You do not hurry to fill it. She looks at you as though taking the time to remember a person, without asking memory to become a defense against what comes next.{/n}
{n}"I am glad we had the days," she says.{/n}
{n}You stay until it is time to stand.{/n}''', c('[Leave with the affection of the conversation.]', "end", flags=("irabeth.farewell_talked",))),
    n("end", "Irabeth", '''{n}Irabeth opens the door. She stands beside it, giving you space to leave and one last unhurried look.{/n}
"Go and do what you choose to do. I will do what is mine. If we have a road afterward, we will choose that too."
{n}She smiles, with none of the guard's borrowed grandeur.{/n}
"I shall be difficult about the inns. You have been warned."''',
      c('[Finish the farewell you earned together.]', flags=("irabeth.campaign_kept",))),
], requires=("irabeth.future_chosen",), chapters=(5,), delay=24)


def ending(identity, title, nodes, *, requires=(), forbids=(), any_of=(), owner="Epilogue"):
    SCENES.append(scene("irabeth.ending_" + identity, title, owner, 0, "", nodes,
        requires=("irabeth.lover", *requires),
        forbids=("closed", "irabeth.closed", "trying", "committed", *forbids),
        last=99, Relationship="irabeth", RequiresAny=list(any_of),
        ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))


ALIVE_END = ("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich", "sacrifice", "ascended")

ending("lasting", "The journeys she chose", [
    n("start", "Narrator", '''{n}The war did not leave Irabeth with an empty life waiting to be filled. There was work she still wanted, and a name she had earned the right to use without apologizing for how much it pleased her. The Commander returned to a woman who expected to be asked about her plans.{/n}
{n}They began with a visit they could keep. Later came the journey from Sella's drawing, altered by weather, obligations and Irabeth's increasingly specific opinions about inns. She chose some roads badly. She enjoyed others enough to tell the story twice. The Commander learned that a complaint about the rain might be followed, without contradiction, by a request to stay another day.{/n}
{n}Their commitment survived through such particulars: a changed appointment honestly explained, an argument finished before it became a month of silence, a private evening neither had to earn by being useful first.{/n}''', c('[Remember the other life she kept with it.]', "marriage")),
    n("marriage", "Narrator", '''{n}Irabeth's ring remained part of the woman the Commander loved. The shape of her marriage and its losses could not be decided by a promise made to somebody else.{/n}''',
      c('[Remember the living marriage.]', "living", forbids=("anevia_dead", "anevia_gone")),
      c('[Remember the wife she mourned.]', "dead", requires=("anevia_dead",)),
      c('[Remember the absence she would not invent an answer for.]', "gone", requires=("anevia_gone",), forbids=("anevia_dead",))),
    n("living", "Narrator", '''{n}Anevia and Irabeth remained wives. The Commander joined the days Irabeth chose to share without claiming every evening the marriage had already promised. There were visits together when all wanted them, and separate visits when that was the invitation. No larger household was declared on anyone's behalf.{/n}
{n}Irabeth kept asking for what she wanted. Sometimes it was a road. Sometimes it was a room, a hand against her cheek, or an audience for a ridiculous guard whose monsters grew larger with every telling. She liked the applause. She liked still being wanted after it ended.{/n}'''),
    n("dead", "Narrator", '''{n}Anevia's death remained a loss. The Commander did not inherit her place, and Irabeth did not have to empty that place before accepting another happy day. She spoke of her wife when she wanted to, kept some memories private and allowed laughter to return without putting it on trial.{/n}
{n}The road drawing stayed in her notebook beside things she would not discard. What she made afterward belonged to a living woman who could mourn and still ask where they might go next.{/n}'''),
    n("gone", "Narrator", '''{n}Anevia's absence had not supplied an answer about her fate or her marriage. Irabeth refused to manufacture one. The Commander kept the promises actually exchanged with her and made no claim to inherit the silence left by someone else.{/n}
{n}Their continuing relationship had to leave room for that uncertainty. It also had room for the next visit, the work Irabeth chose and the journeys they could honestly arrange.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_lasting"), forbids=ALIVE_END)

ending("open", "Another day freely chosen", [
    n("end", "Narrator", '''{n}Irabeth and the Commander had declined to turn affection into a promise of a settled household. After the war, they kept making invitations they could mean. Some became journeys, some became short visits between obligations, and some had to be postponed with disappointment plainly admitted.{/n}
{n}The relationship had warmth without a claim on every future. Irabeth still liked choosing the road. The Commander still had the right to prefer another. They found that an honest disagreement was less lonely than an agreement neither intended to keep.{/n}
{n}Her marriage's history remained her own, including any loss or absence it carried. Other relationships did not have to disappear to make these days worthwhile. When they met, the pleasure was in finding that they wanted the next hour together, and in giving that hour the attention they had once thought only a war could demand.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_open"), forbids=ALIVE_END)

ending("friends", "The friendship after the courtship", [
    n("end", "Narrator", '''{n}The courtship ended before the war did. Irabeth did not immediately become effortless company, and the Commander did not ask her to perform that kindness. Given time, they found a friendship that no longer needed to disguise itself as either a failed romance or a romance waiting to resume.{/n}
{n}They remembered the seized wagon, the performance and the afternoon spent following Sella's drawing. The work did not become worthless because the lovers had chosen differently. Neither did the kisses become a debt that friendship must repay.{/n}
{n}Irabeth kept the road drawing. Where she went, and with whom, remained a choice she could make. When she told the Commander about it later, she expected interest, laughter at the right places and no claim to have been promised a place in every story.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_friends"), forbids=ALIVE_END)

ending("unfinished", "An invitation with days still to come", [
    n("end", "Narrator", '''{n}Irabeth and the Commander had begun a relationship. They had not completed every day they meant to share before the fighting ended. The unfinished work did not become a remembered achievement, and a road never walked was not added to their private history.{/n}
{n}What remained was the affection they had actually chosen, with whatever promises they had spoken before the interruption. Irabeth wanted the chance to discover what those choices would mean in ordinary time. She also had work and other loyalties, along with the marriage and losses she brought into every new day.{/n}
{n}The Commander could return to an invitation, if both still wanted it. The next visit would have to be lived before either could call it part of the life they had made.{/n}'''),
], forbids=(*ALIVE_END, "irabeth.campaign_kept"))

ending("loss", "The woman who was not waiting", [
    n("start", "Narrator", '''{n}The Commander's private history with Irabeth did not exempt her from the war's other outcomes. What had been said between them could be remembered. It could not prove that she was alive and waiting at the end of the road.{/n}''',
      c('[Remember Irabeth, who died.]', "dead", requires=("irabeth_dead",)),
      c('[Remember Irabeth, who was gone.]', "gone", requires=("irabeth_gone",), forbids=("irabeth_dead",))),
    n("dead", "Narrator", '''{n}Irabeth's death left the Commander with the days they had actually shared. There might have been many more. Grief did not supply them. A private promise had not made her invulnerable, and no story about the power of their love brought her body back.{/n}
{n}She had been an officer with difficult judgments, a woman who liked being admired, and a lover who wanted to be asked what she enjoyed. Those particulars outlasted the temptation to turn her into a flawless example. The memory worth keeping had room for her laugh, her stubbornness and the answers she had insisted were her own.{/n}'''),
    n("gone", "Narrator", '''{n}Irabeth was gone. Her absence did not establish her death, a reunion or a secret promise fulfilled elsewhere. The Commander could not name an ending to her life from the fact that she no longer stood in the place where they had met.{/n}
{n}The days before that absence remained real. So did their limits. The Commander could remember her last words. What she chose afterward remained beyond the reach of that memory.{/n}'''),
], any_of=("irabeth_dead", "irabeth_gone"))

ending("changed", "A choice she did not follow", [
    n("end", "Narrator", '''{n}The Commander's transformation left no ordinary future for the relationship Irabeth had chosen. She did not surrender her judgment because she had once offered tenderness. The person who had required the right to say no kept that right when saying it cost her something.{/n}
{n}She remembered the affection without allowing it to conscript her into a life she could not accept. There was grief in the distance, and anger too. Neither made her devotion to Iomedae, her marriage's history or the work of protecting others a disguise she would discard for a lover.{/n}
{n}The route between them ended with what had actually been shared. No amount of remembered warmth made her an obedient witness to everything the Commander became.{/n}'''),
], any_of=("inhuman", "swarm", "true_lich"), forbids=("irabeth_dead", "irabeth_gone"))

ending("ascent", "The distance beyond the map", [
    n("end", "Narrator", '''{n}The Commander's ascent changed the distance between them in ways no road drawing could describe. Irabeth had loved a person she could disagree with across a table. She would not let worshipers replace that history with a legend in which she had always known whom she served.{/n}
{n}She kept her own faith, work and loyalties. Any future contact would have to meet the woman she remained, rather than summon a lover whose affection had been mistaken for worship. The promises actually exchanged still mattered to her. They did not explain how a mortal life should be rearranged around divinity.{/n}
{n}When asked what the Commander had been like in private, she sometimes told a small, unflattering story. It annoyed the more solemn devotees. Irabeth found that she could bear their disappointment.{/n}'''),
], requires=("ascended",), forbids=("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich"))

ending("sacrifice", "The answer she could no longer hear", [
    n("end", "Narrator", '''{n}The Commander's sacrifice ended the possibility of another private answer. Irabeth did not make a romance out of having foreseen it. She had wanted the Commander alive. The magnitude of the deed did not make that wish small or shameful.{/n}
{n}She kept the days they had actually shared, including their disagreements and the promises they had chosen. She added no unspoken vow to make the loss seem more complete. Some mornings she could tell a funny story about the Commander. On others, she could not bear hearing strangers explain why she should be comforted.{/n}
{n}Her own life continued, with work she believed in and people whose presence mattered. Continuing did not mean the loss had been corrected. It meant she was still a woman entitled to choose a road after the person she had wanted beside her could no longer come.{/n}'''),
], requires=("sacrifice",), forbids=("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich", "ascended"))

ending("aeon", "A history without its meeting", [
    n("end", "Narrator", '''{n}When the Worldwound's history was rewritten, the private sequence that had brought Irabeth and the Commander together no longer belonged to the world that followed. Their encounters could not be claimed as memories by people who had never lived those days.{/n}
{n}Irabeth's altered life was her own. The erased Commander had no right to a romance as payment for changing the world, nor to a convenient certainty about whom she would love in a history shaped by other meetings.{/n}
{n}What had been chosen in the vanished life had mattered while it existed. That was a truth about the lost history, not a summons sent into the new one.{/n}'''),
], owner="AeonEpilogue")


s("after_the_answer_was_lost", "The answer grief could not supply",
  '"Anevia has died. I will not pretend that makes our unfinished conversation simple."', [
    n("start", "Irabeth", '''{n}Irabeth sits very still. Her ring is visible on the hand resting against her knee.{/n}
"No. It does not."
{n}She gives herself time before continuing.{/n}
"I remember what you and I said. I cannot ask her for another answer. I cannot turn what happened into permission she gave because she loved me."
{n}Her gaze rises to yours.{/n}
"I still have to decide what I want from the life I have. I want company. Sometimes I want to be left alone so strongly that the kindness of someone asking becomes difficult to bear. I will have to tell you which is true, and I may answer differently tomorrow."''',
      c('"We were lovers before this loss. I remember what we chose, including what we concealed."', "affair", requires=("i_affair",)),
      c('"We had asked about a courtship. I will not turn that question into a promise you already made."', "question", forbids=("i_affair",))),
    n("affair", "Irabeth", '''"So do I. I will not rewrite it into something easier to remember."
{n}She touches the ring once, then leaves it alone.{/n}
"I wanted you. I knew what I was doing. Whatever conversations followed, I cannot go back and begin with the honesty I should have had."
{n}Her voice grows steadier.{/n}
"I can decide whether I want to see you again. I do. Slowly. Without making every meeting an attempt to prove I have grieved correctly. If I speak about her, listen. If I need to stop, let me stop. I can offer no simple account in which the loss has made our path clear."''', c('"I can meet you as you are now."', "choice", flags=("irabeth.legacy_bereaved_history",))),
    n("question", "Irabeth", '''"Thank you. I had begun hearing other people's assurances before anyone spoke them. She would want me happy. I deserve a future. All the things that might be true and still do nothing to tell me what I want this afternoon."
{n}She looks toward the window.{/n}
"I would like an evening with you. I would like the freedom to enjoy it and miss her in the same hour. I am not offering a replacement marriage or asking you to wait until grief has become convenient."
{n}She turns back.{/n}
"If that is an invitation you can accept, I would like to make it."''', c('"I can accept an evening without asking it to settle your grief."', "choice")),
    n("choice", "Irabeth", '''{n}She holds out her hand, leaving the space between you open.{/n}
"Then we can begin with a day. I have work I would like your help hearing, a dispute over cold iron. After that, something without a report attached. I have signed my name for a recitation. I would like to find out whether I can still enjoy making a room laugh."
{n}Her mouth moves toward a smile without quite reaching it.{/n}
"I may be disappointed by the answer. I would rather discover it than be told what the evening ought to mean."''',
      c('[Accept the slow courtship she has chosen herself.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.bereaved_courtship")),
      c('"I cannot offer that relationship. I would like to remain a friend."', flags=("irabeth.closed",))),
], requires=("anevia_dead",), any_of=("irabeth.courtship_requested", "i_affair", "tirabade.irabeth_continuation_invited"),
    forbids=("irabeth.personal_ready",))


def integrate(payload):
    """Register observed native dialogue only; never write native morale or life states."""
    payload.setdefault("SeenCues", {}).update({
        "irabeth.scar_known": ["c7a7717c516039d498a7525baf6abe04", "8e808b69a43ed4f43b8eb39d27990a4a"],
        "irabeth.queen_loss_known": ["d47bcd8d88f8ea149a596ca927e1153f"],
    })
    payload.setdefault("Etudes", {}).update({
        "irabeth.chapter_three": "15e0048c7daf0ac4999c2313b58df0e3",
        "irabeth.chapter_five": "5b01aa690202e584888dfc600a4aac0a",
    })


# Date acquisition itself; an optional goodbye cannot establish when love began.
for _book in SCENES:
    for _page in _book["Nodes"]:
        _choices = []
        for _choice in _page["Choices"]:
            if "irabeth.personal_ready" not in _choice["Set"]:
                _choices.append(_choice)
                continue
            for _chapter in ("three", "five"):
                _dated = dict(_choice)
                _dated["Set"] = [*_choice["Set"], "irabeth.began_chapter_" + _chapter]
                _dated["Requires"] = [*_choice["Requires"], "irabeth.chapter_" + _chapter]
                _dated["Forbids"] = [*_choice["Forbids"], *(["irabeth.chapter_five"] if _chapter == "three" else [])]
                _choices.append(_dated)
        _page["Choices"] = _choices
