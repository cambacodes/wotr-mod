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
    Guidance="Speak with Irabeth in Drezen. Keep the appointments you choose, and speak with Anevia when Irabeth asks. Her marriage is her own; whatever you have with Anevia is yours.",
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
    n("interest", "Irabeth", '''{n}She sits at last. The chair creaks under her; she has never learned to sit carefully.{/n}
"I used to do that on the march. Recite things. It passed the miles between one stretch of road and the next one just like it. Then I came to Kenabres and started weighing every word before I said it."
{n}She stretches one leg out and scowls at the scuffed toe of her boot.{/n}
"A half-orc who plays the brute in a taproom only proves what they already think. A half-orc who plays it straight gets called surly. You can't win that one, so I stopped playing."
{n}She glances up.{/n}
"I signed the page anyway. Don't ask me why. No, ask. Because I want them to laugh where I mean them to, and then clap, and I want to stand there and enjoy it like a recruit with a new sword. It's vanity. I've confessed it. Iomedae can take it up with me."
{n}The admission brings colour into her cheeks. She leaves it there.{/n}''',
      c('"I would like to see that look on your face."', "flirt", forbids=("anevia_dead", "anevia_gone")),
      c('"I would like to see that look on your face."', "careful", requires=("anevia_dead",)),
      c('"I would like to see that look on your face."', "careful", requires=("anevia_gone",), forbids=("anevia_dead",)),
      c('"I like your company, Irabeth. I would like more of it."', "company"),
      c('"I hope the evening goes well. Let us keep this friendship."', "friend")),
    n("flirt", "Irabeth", '''"You're looking at it already."
{n}She lets that stand a breath too long. Then her eyes drop to her ring, and she turns it once with her thumb.{/n}
"I know what you meant. And I liked it. That's the trouble."
{n}She flattens the list on the table between you like a map before an advance.{/n}
"Nevi is my wife. I love her. Whatever this is, it doesn't get settled behind her back like a supply dispute. I'm no good at sneaking, Commander. I clank."
{n}Her thumb rests beside her written name.{/n}
"Come again. Come to the recitation. If you mean more than that, say it out loud one day, and I'll answer out loud. Not tonight."''', c('"I mean the invitation. We can take the time."', "finish", flags=("irabeth.interest",))),
    n("careful", "Irabeth", '''"You're looking at it already."
{n}The smile comes, and goes. Her eyes drop to her ring.{/n}
"Don't. Not yet. I'm glad you said it, and I've no idea where to put it. Nevi is in any answer I give you, whether she's here to give it with me or not."
{n}She looks back at you, jaw set.{/n}
"Come again because you like my company. That much I can manage."''', c('"I would like to come again."', "finish", flags=("irabeth.interest",))),
    n("company", "Irabeth", '''"So would I."
{n}She says it fast, then seems not to know what to do with her hands, and settles them on her knees like a recruit at inspection.{/n}
"I keep picturing the audience as officers waiting for me to finish so they can give their reports. It'd be good to know one person came for the guard."
{n}She reaches for the list and stops before folding it out of sight.{/n}
"Every hour of the day somebody needs the Knight-Captain for something. Then I complain nobody talks to me about anything else. Nevi says I built the cage myself and polish the bars on Sundays."
{n}She looks straight at you.{/n}
"Come again. Tell me what you talk about when you're not giving orders. I honestly don't know."''', c('"I will."', "finish")),
    n("friend", "Irabeth", '''"Yes. Good."
{n}She gives the list one last look before folding it. The crown disappears inside the paper.{/n}
"You can still laugh at the performance. I'll know which lines worked, and I'll blame you for the rest."
{n}When she stands there is no apology in it. She has somewhere to be, and a name already waiting for her there.{/n}''', c('[Leave it at friendship.]', flags=("irabeth.closed",))),
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
"I asked whether he expected me to smelt it myself," {n}she says.{/n} "That was the laugh."
"You would not give a name."
"I gave two. You disliked both."
{n}Irabeth holds up a hand. Hadran presses his lips together.{/n}
"A mark may identify a supplier," {n}she says.{/n} "It does not establish that every bar bearing it is false. What did you test?"
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
    n("uncertain", "Narrator", '''{n}The stamp looks familiar. You begin to name it, then notice a second impression crossing the first. Your explanation no longer fits what is on the metal.{/n}
{n}Brena waits. Hadran looks from your face to Irabeth's.{/n}
{n}"I cannot establish it from this," you say.{/n}
{n}Irabeth nods. "Then we use the forge."{/n}
{n}The sample goes under escort. You wait through the preparation of a small test piece, the heat and the repeated examination. Brena does not let anyone hurry the work. The material proves sound, with a factor's stamp struck over the maker's. By the time you return, the yard is in shadow and a crew has gone home without the hinges Brena meant to finish.{/n}
{n}"Tomorrow," she tells the boy who came to collect them. "Tell your mother I know. Tomorrow."{/n}
{n}Irabeth watches him go. Then she writes "one afternoon: the Commander's guess" in the margin of her report, and underlines it.{/n}''', c('[Discuss what remains unsettled.]', "cost", flags=("irabeth.iron_uncertain",))),
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
    n("start", "Irabeth", '''{n}Irabeth puts down the cup she was holding. She heard you. She is only making sure of it.{/n}
"Yes. Iomedae help me, I've thought about asking you the same thing."
{n}She drags a chair out from behind the desk and sits facing you, with no report between you. It looks like it costs her something.{/n}
"I like being wanted. There. Embarrassingly simple. I kept looking for a nobler reason for how pleased I get when you come looking for me, and I didn't find one."
{n}Her ears darken. She doesn't look away.{/n}
"I don't mean useful to the Commander. I mean I've caught you looking at my mouth, and I want to give you a reason to keep doing it."
{n}She blows out a breath that is nearly a laugh.{/n}
"That's the reckless part said. The rest should be easier."''',
      c('"What do you want to keep separate from this?"', "rank"),
      c('"I want that too. Tell me what you want before we begin."', "rank"),
      c('"I have changed my mind. I value the friendship."', "friend")),
    n("rank", "Irabeth", '''"My judgment. I serve under you. Taking off my sword belt doesn't change that."
{n}She rests her forearms on her knees, the way she sits with sergeants.{/n}
"When I say don't march, you hear the Knight-Captain saying it. Not your lover sulking. And when you overrule me, I salute, and I still think you're wrong, and I leave it on the council table. I'll try to. I'm stubborn, Commander. You know that."
"And away from council?"
"Some nights you'll want me and I'll want sleep. Some nights I'll have promised Nevi. Then it's no, and you grumble, and that's the end of it. I won't lie there pretending. I'm a bad liar in armour and a worse one out of it."
{n}She straightens.{/n}
"I can want you very badly. I can also be tired, pig-headed and sure my plan's the best one when it's only mine. Meet that woman before you promise anything to the one who salutes."''',
      c('"I want the woman who can tell me no. You\'ll hear it from me too."', "marriage"),
      c('"I expect a lover to support my decisions."', "refused")),
    n("marriage", "Irabeth", '''"Good. Then there is something more particular."
{n}She looks at her ring and turns it once, a familiar movement rather than a hesitation.{/n}''',
      c('"We should speak about Anevia."', "wife", forbids=("anevia_dead", "anevia_gone")),
      c('"We should speak about what losing Anevia means for this."', "bereaved", requires=("anevia_dead",)),
      c('"Anevia is gone. I will not treat that as an answer from her."', "gone", requires=("anevia_gone",), forbids=("anevia_dead",))),
    n("wife", "Irabeth", '''"I love her. I'm not leaving her. Get that out of your head first."
{n}No apology in it. A flat fact, the way she gives a casualty count.{/n}
"I can picture loving you and staying her wife. Picturing it doesn't tell me what Nevi will say. So I tell her first. Then you go and talk to her yourself."
"Separately?"
"Yes. She'll say things to you she won't say with me in the room watching her face. Then she and I have it out again. It's not an inquiry. Nobody wins by getting their story in first."
{n}Her mouth twitches.{/n}
"And don't go to her like you're borrowing a sword. You're asking to walk into her house. She's allowed to hate part of it. So am I. We've survived worse than each other."
{n}She leans back, and the breath goes out of her.{/n}
"If she wants time, she gets it. I'll wait for a real answer before I pretend I've got one."''',
      c('"Speak with her. I will meet her when she wants that conversation."', "wait"),
      c('"I would rather leave this as friendship."', "friend")),
    n("wait", "Irabeth", '''{n}Her hand moves toward yours, then settles on the arm of the chair between you, as if she had posted it there.{/n}
"I'd like to kiss you now. I'll probably still want to when you leave."
"That sounds inconvenient."
"Very. And my own doing."
{n}She laughs, short, not hiding the frustration under it.{/n}
"Don't take the waiting for cold feet. I'm just not sneaking about in my own marriage. I did enough creeping through cellars in Kenabres to last me."
{n}At the door she pauses, one hand flat on the wood.{/n}
"You can still come and hear me recite. Nothing secret in that. I mean to make the duke even worse."''',
      c('[Give her time to speak with Anevia.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.spousal_conversation_requested"))),
    n("bereaved", "Irabeth", '''{n}Irabeth holds the ring still between finger and thumb.{/n}
"You won't be her. Don't try. I'll still look for her when I walk into a room. You'll see me do it. Don't make a face about it."
{n}She studies her own hand a while.{/n}
"And I won't hold every good hour up against her either. Nevi loved me alive. She was very loud about it whenever I went solemn on her."
{n}The smile doesn't quite hold.{/n}
"Ask me for an evening. I can answer for an evening. If I start talking about her, let me finish. If I stop in the middle, don't make me go on."
{n}She lets go of the ring.{/n}
"Slowly, then. One evening, then another. And I won't pretend a dead woman gave me leave. She didn't. I'm giving it myself."''',
      c('"An evening, then. We can decide the next one when it comes."', "widow_yes"),
      c('"I cannot offer what you are asking. Let us remain friends."', "friend")),
    n("gone", "Irabeth", '''"Thank you."
{n}The relief doesn't last. She looks down at her ring.{/n}
"I can't make her silence say what she'd have said in this room. And I won't forge her a release so I can kiss you with a clear head. That's deserter's paperwork."
{n}She lifts her eyes.{/n}
"Your company I'll take, openly. Anything more waits until I've had my answer from her. However long that is."
{n}Her hand closes on the arm of the chair, then eases.{/n}
"And don't stand guard over me while I wait. I'd hate that more than you going."''',
      c('[Keep her company. Promise nothing yet.]', flags=("irabeth.started", "irabeth.absence_wait",)),
      c('[Leave it at friendship.]', flags=("irabeth.closed",))),
    n("widow_yes", "Irabeth", '''{n}She holds out her hand as if closing a bargain. You take it. Her grip is hard and warm and in no hurry to let go.{/n}
"There's a case I want to show you. After that, an hour with no case and no war in it. I've put my name down to recite at a storehouse. A ridiculous little piece about a guard and a duke."
{n}Her thumb moves over your knuckles.{/n}
"Come because you want to hear it. I'd like to look up and find you there."
{n}She lets go and goes back to her desk. The ring stays on her finger.{/n}''',
      c('[Accept the first evening she has offered.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.bereaved_courtship", "irabeth.lover", "irabeth.personal_ready"))),
    n("refused", "Irabeth", '''{n}The warmth goes out of her face.{/n}
"Then I answered too soon. I'll stay your officer. That order doesn't follow me to bed."
{n}She stands and puts the chair back behind the desk. There is nothing left to argue.{/n}''', c('[Accept her refusal.]', flags=("irabeth.closed",))),
    n("friend", "Irabeth", '''"Yes. Better now than later."
{n}She takes a moment before she gets up. When she does, she offers her hand like a sergeant closing a parley, brief and firm.{/n}
"Damn. I had hoped for the other answer. I'm glad you told me now."''', c('[Remain friends with Irabeth.]', flags=("irabeth.closed",))),
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
"I want you to say what's true of you. Nevi has questioned better liars than either of us. If we've rehearsed, she'll hear it in the first sentence and throw us both out."
{n}For the first time, Irabeth's mouth curves.{/n}
"And she'd be right to."''', c('"What are you hoping she will say?"', "after")),
    n("after", "Irabeth", '''"That she still wants to be my wife. That she believes I'll bring her a bad truth myself, before she has to dig it out of me like a splinter."
{n}She stops, then makes herself go on.{/n}
"And that she'll let me go on loving you too. I haven't earned that by confessing. I'm going to ask anyway. I'm a paladin, not a saint."
{n}She holds your gaze.{/n}
"If you want out, say so now. I'd rather know before I stand in front of her asking her to make room."
{n}Her jaw is tight, but none of it is aimed at you.{/n}
"Either way, she hears it from me. All of it."''',
      c('"I want this out in the open. I\'ll speak to her."', "agree"),
      c('"I will tell her the truth, but I do not want to continue as lovers."', "stop")),
    n("agree", "Irabeth", '''{n}Irabeth closes her eyes for a moment. When she opens them, she looks relieved and frightened in almost equal measure.{/n}
"Go when you can listen. I have said enough that she knows what conversation she is agreeing to."
{n}She steps aside from the door, leaving the way clear.{/n}
"I am going to find something useful to do while I wait. Probably badly. If you see a requisition with three different totals, you may know why."
{n}The joke makes a little room to breathe. She does not ask for a kiss before you leave.{/n}''',
      c('[Keep the promised conversation with Anevia.]', flags=("irabeth.started", "irabeth.courtship_requested", "irabeth.single_affair_disclosed", "irabeth.spousal_conversation_requested"))),
    n("stop", "Irabeth", '''"Then that's what I'll tell her."
{n}She takes it standing still. After a moment she looks toward the window.{/n}
"I'm sorry it ends here. I'm glad you didn't let me talk about a future you'd already walked away from."
{n}She turns back before you leave.{/n}
"She'll ask you things. Answer her straight. You don't need to be my lover to do that much."''',
      c('[End it. Do not pretend it never happened.]', flags=("irabeth.closed",))),
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
"I still love her. I can imagine her lovin' somebody else. You two leaned on both of those like a pair of drunks on a fence, and neither of you thought to ask me first."
{n}She draws a breath.{/n}
"I'm willing to try somethin' different. Willing. That doesn't make the evening all right after the fact. Don't go tellin' yourself the past's improved 'cause I've got a future in mind."''',
      c('"I will not. We concealed it. Any agreement begins now."', "other"),
      c('"Then why keep being angry if you are willing?"', "refuse")),
    n("other", "Anevia", '''{n}Anevia moves the key out from beneath her hand.{/n}
"One other thing before you begin trying to be impressively considerate."''',
      c('"You and I have our own thing. I won\'t ask you to answer as if we don\'t."', "lovers", requires=("anevia.lover",), forbids=("anevia.closed",)),
      c('"You and I were lovers. I will not pretend that history disappears because it ended."', "past", requires=("anevia.lover", "anevia.closed")),
      c('"You are not being asked to become my lover."', "separate", forbids=("anevia.lover",))),
    n("past", "Anevia", '''"Good. I remember it. I remember why it ended, too."
{n}She leaves her chair where it is.{/n}
"I'm answerin' about my marriage and Beth's invitation. I'm not offerin' to open ours back up. Different questions, even when the same people make 'em awkward."
{n}She studies you a moment.{/n}
"I can let her see you without wantin' you back myself. Don't expect me to be sweet about it to prove I've made my peace. I'll be civil. That's what's on offer."''', c('"I understand. Tell me what you and Irabeth have discussed."', "terms")),
    n("lovers", "Anevia", '''"Good. Because I'd noticed."
{n}A little warmth returns to her face, but she keeps her chair where it is.{/n}
"What we've chosen doesn't answer this for Beth. And what she wants doesn't make our evenings part of a bargain in which everybody has to do the same thing. I might want you alone one night. She might want me alone the next. Nobody gets a receipt to cash in against the other two."
{n}She studies you with a rueful smile.{/n}
"We may want a shared evening later. Then we'll ask about that evening. I'd like to see whether we actually enjoy it before someone starts ordering a larger bed."
{n}She taps the table.{/n}
"For now, you're asking about her. I'm answering about my marriage. I still mean the things I said to you in our own time."''', c('"Then those are separate questions."', "terms")),
    n("separate", "Anevia", '''"Glad to hear it. I like choosin' my own invitations."
{n}She smiles briefly, then becomes serious again.{/n}
"You can have supper with us without it being a rehearsal for anything. You can see Beth on her own without making me the person who keeps watch outside. If I want somethin' with you, you'll hear it from me."
"And if you don't?"
"Then you'll have the terrible burden of knowin' two married women without kissing both of them. People have survived worse."
{n}The joke lets the room relax. Anevia does not use it to leave the question behind.{/n}
"I mean it. Don't try to repay my agreement by flirtin' at me. A quiet thank-you will do."''', c('"Thank you. I would like to hear the terms you and Irabeth discussed."', "terms")),
    n("terms", "Anevia", '''"She tells me when she's with you. I don't want the details. I do want to know whether to keep supper warm or feed it to the dog. The nights we've promised each other stay ours. If the war eats one, we say so and pick another. Nobody hides behind the war to cover wantin' to be somewhere else."
{n}Anevia finds a loose thread at her cuff, considers pulling it and leaves it alone.{/n}
"You don't have to swear off everybody else to keep me sweet. And she doesn't get a say in who else you tumble. But if somebody's sittin' up waitin' for you, tell 'em where you've gone. I've done my share of waitin' up. I know what it tastes like."
"And if this stops working?"
"Then we have it out before we've spent a month collectin' grudges like spare arrows. Beth and I row as wives. You and she row as whatever you are. If it's all three of us, we find a room with enough chairs."
{n}Her smile goes crooked.{/n}
"Drezen's survived worse rooms."
{n}She lets you chew on it without filling the pause.{/n}''',
      c('"I can agree to that. I will speak to her about the evening we actually want."', "yes"),
      c('"I can\'t live by that. I won\'t start this."', "no")),
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
"I also asked her not to describe every pleasant expression on my face as evidence. She said she would try, and fail. It is the most truthful promise she has ever made me."
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
{n}She stops, hears herself starting a second paragraph, and laughs.{/n}
"That is the invitation. Answer before I add a clause."''', c('"Yes. I would like that evening."', "room")),
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
{n}"I haven't laughed like that since Kenabres," she says, almost to herself, and goes dark to the tips of her ears. "I liked hearing you laugh. Don't you dare repeat that to anyone."{/n}''', c('"I was. I would like more evenings in which I get to be foolish too."', "yours")),
    n("hope", "Irabeth", '''"I hoped you would look pleased to be alone with me. You have managed that part."
{n}She turns in her chair, bringing one knee near yours.{/n}
"I wanted to stop wondering whether I had made this too solemn to enjoy. We have had necessary conversations. I keep thinking I ought to follow them with another necessary conversation, until someone declares us fit for a pleasant one."
{n}Her smile reveals the tips of her tusks.{/n}
"I wanted to see whether you would kiss me if I stopped explaining myself. And I wanted to hear something you do not say in council. Something foolish you would like, perhaps. I have brought enough earnestness for two people. You need not supply more for my benefit."
{n}She rests her hand on the edge of your chair.{/n}
"What did you hope would happen when you said yes?"''', c('[Tell her what you wanted from the evening.]', "yours")),
    n("yours", "Irabeth", '''{n}You tell her you want an hour in which nobody needs you to solve anything. She listens with her chin on her fist, the way she listens to scouts, and asks one question about it. A good one.{/n}
"You picked the wrong woman for that. I'll always know who you are. I know who you are when you're asleep in council."
"I do not expect you to forget."
"Good. Then I get to tell you when you're making something harder than it needs to be. I've got a list. It can wait."
{n}The laughing comes easier now. She leans in, stops halfway, and doesn't pretend she stopped for any reason but nerve.{/n}
"I want to kiss you. I've been thinking about it half the time you were talking. Take that as a compliment to the talking, or a confession of poor attention."''',
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
    n("hand", "Narrator", '''{n}She turns her palm up and laces her fingers through yours, carefully, as if your hand were kit she had been issued and meant to return in good order.{/n}
{n}"All right. I can live with being asked for that."{/n}
{n}She drags her chair close enough that neither of you has to stretch. For a while you trade the worst performances either of you has sat through. Irabeth remembers a mercenary who sang a whole ballad in the wrong order and got angry when anyone died twice.{/n}
{n}When the street grows loud under the window, she leans in to finish the story. Her shoulder stays against yours after the punchline.{/n}
{n}"Another evening," she says. "This one's been good. I want more of them."{/n}''', c('[Enjoy the hour.]', "end")),
    n("end", "Irabeth", '''{n}Before leaving, Irabeth puts the chairs back where she found them. You open the door while she checks the window latch.{/n}
"There is a disagreement over a wagon of cold iron I would like to hear properly. Come if you want to. It is work, and I shall not pretend otherwise."
{n}She turns toward you.{/n}
"Tonight I wanted you in a room without a report. Tomorrow I shall drag you through a bad one. We'll see how you are on a bad day. I'm worse."
{n}At the foot of the stairs she takes your hand once more, in full view of the open street. She holds it only a moment before going her own way.{/n}
"Good night. I am pleased you came."''',
      c('[Walk her to the corner, in full view of the street.]', flags=("irabeth.marital_terms_agreed", "irabeth.lover", "irabeth.personal_ready"))),
], requires=("irabeth.spouse_heard",), delay=24, forbids=("irabeth.personal_ready", "anevia_dead", "anevia_gone"))


s("a_day_of_our_own", "Something they had not done yet",
  '"We have a life with Anevia. I would also like another day with you."', [
    n("start", "Irabeth", '''"So would I."
{n}Irabeth moves a book from the chair beside her. She smiles before you sit, with the ease of a woman who has already found your hand in less convenient places.{/n}
"Don't treat it like a first evening. We've been lovers. The three of us sat at one table and hammered it out. I remember every word."
{n}She sets the book on the desk.{/n}
"But there are things I have not asked you to do with me because I kept thinking of how they would fit into an evening for all three of us. Some do not fit. Anevia has heard me argue with imaginary dukes often enough to ask for a holiday from them."
{n}Her expression becomes a little mischievous.{/n}
"You have not exhausted your patience yet. I thought I should take advantage."''',
      c('"An imaginary duke? I may need warning."', "piece"),
      c('"You can ask me for a day without it being useful to anybody."', "ours"),
      c('[Keep the invitation for another day.]', abort=True)),
    n("piece", "Irabeth", '''"A caravan guard, a missing load of wool and a duke who suspects every beast in the story has been hired to delay his delivery."
{n}She gives you a few lines. The guard's monsters grow with every question. The duke's patience shrinks until he begins charging the guard for the time spent describing them.{/n}
"I used to know it. I have put my name down for a recitation and discovered that knowing words in your head is easier than knowing them in front of people."
"Did Anevia draw you into this?"
"No. I signed the page myself. She found out afterward and looked so pleased that I briefly considered denying it."
{n}Irabeth laughs.{/n}
"She has plans for the day. I would like you to hear the piece before I face the audience. Then perhaps help me decide which parts deserve to survive."''', c('"I would like that."', "ours")),
    n("ours", "Irabeth", '''"I know. I'm trying to act like I know."
{n}She rests her hand against yours.{/n}
"I told Nevi I wanted this. She said she likes being my wife a great deal more when she doesn't have to sit through every rehearsal. Then she made me do the duke twice."
{n}Her thumb moves over your knuckles.{/n}
"I'm not taking back anything the three of us said. This is a day inside it. That's all it is."
{n}She looks straight at you.{/n}
"Spend the afternoon with me? Hear the piece, then find something neither of us has rehearsed."''', c('"Yes. Show me what you have chosen."', "walk")),
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
"You have heard me laugh over a bad book. You have heard me say I wanted somewhere to go. I signed that page before anyone could remind me there was a war on."
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
      c('[Kiss her back, then go and hear the dispute.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.legacy_shared_history", "irabeth.boast_guard"))),
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
    n("open", "Irabeth", '''{n}Irabeth studies the covered page a while.{/n}
"Then we move the boy and his sister before we open it. Ordel will need new work. I'll tell him why the watch chose this, and I won't tell him the cost is imaginary because the choice is defensible."
{n}Ordel puts on his cap.{/n}
"I don't thank you for it."
"I didn't expect you to."
"I gave you good information."
"You did. You haven't been exposed for misconduct. That may make very little difference to the next man you ask to hire you."
{n}He looks at her, the anger giving way to an exhausted attention.{/n}
"You know that?"
"Yes. I'd have chosen the other course. I can still carry this one out properly."
{n}She writes the relocation order, then a payment for Ordel's lost commission. She does not write a reward. When he leaves to make the arrangements, Irabeth stays by the table, watching the closed door for a few seconds.{/n}''', c('[Return when the witnesses are safe and Brena can inspect the account.]', "answer_open")),
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
{n}You ask whether she trusts him.{/n}
"With a frightened recruit in a burning building? Yes. With a woman who makes him feel foolish? Not yet. He stays on patrol. Seizures go through another officer until the review is done. Brena has had enough of him."
{n}She looks toward the small purse, now lighter than when you arrived.{/n}
"The officers will ask why I kept him. I'll show them the restrictions. Hadran can argue with those for a change."
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
    n("corner", "Irabeth", '''"Fair. I've talked about myself for an hour. Somebody ought to court-martial me."
{n}She pulls you into a sheltered doorway out of the stream of the departing audience. It is open to the lane and quiet enough to hear each other.{/n}
"Go on. Whatever you were chewing on while I was busy being magnificent."
{n}You tell her something that has sat badly with you all day. Irabeth listens. Once she opens her mouth with a plan already in it, shuts it again, and waits. When you have finished, all she says is, "That's a rotten thing to carry," and she grips your forearm.{/n}
"There. I've looked at you. Kick me if I start another speech."
{n}The grin comes back.{/n}
"A small kick. I've grown fond of speeches."''', c('[Stay close in the quiet doorway.]', "kiss_question")),
    n("kiss_question", "Irabeth", '''{n}She turns toward you. The laughter has gone out of her face, and what is left is more intent.{/n}
"I've wanted to kiss you since you told me about the clerk. I'm going to, unless you've got a better idea."
{n}Her hand is already fisted in your sleeve.{/n}''',
      c('[Kiss her and let the celebration linger.]', "kiss"),
      c('[Take her arm and walk back together.]', "arm")),
    n("kiss", "Narrator", '''{n}Irabeth's kiss is warm and a good deal less careful than her entrance into the hall. She hauls you in by the coat, and for once she does not apologise for her strength.{/n}
{n}When you part, she rests her cheek against yours for a moment.{/n}
{n}"I'm going to be impossible to live with this evening."{/n}
{n}"Only this evening?"{/n}
{n}"You've got bold."{/n}
{n}She kisses you once more, briefly, as though conceding the point.{/n}''', c('[Walk back with her.]', "end")),
    n("arm", "Narrator", '''{n}She offers her arm with a little flourish borrowed from the guard. You take it, and she immediately complains that the guard would have charged a toll.{/n}
{n}The joke lasts half the walk. Afterward, you fall into a quieter conversation about the song's unnecessary verses. Irabeth remembers a better ending, sings two lines under her breath and stops when she sees you listening.{/n}
{n}"Another performance costs extra."{/n}
{n}She does not move her arm away.{/n}''', c('[Enjoy the walk without asking for more.]', "end")),
    n("end", "Irabeth", '''{n}At headquarters she stops before the door.{/n}
"Thank you for coming. Not as a kindness. I wanted you there. There's a difference, and I want it on the record."
{n}She glances back toward the lane.{/n}
"Tomorrow I answer for the practice repairs and the warehouse inquiry. Tonight a room full of people laughed where I meant them to. I'm keeping that."
{n}Her grin widens.{/n}
"I might even think of it while they're shouting at me. A useful improvement."''',
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
{n}You ask how Brena has fared.{/n}
"She has finished the delayed work. She declined a request to attend an officers' discussion of supply rules. The clerk had described her as a satisfied claimant. I corrected the description."
{n}Irabeth rubs a thumb along the sound sword's binding.{/n}
"She sent a message that was mostly unflattering. It ended with a price for new grips. A fair price. I have accepted it."
{n}Her smile is small.{/n}
"Hadran can explain the wait to his recruits. Brena has done enough explaining."''', c('"And what do the officers say about your decision?"', "officers")),
    n("open", "Irabeth", '''"Ordel has found work with a different carrier. The pay is worse. He brought the final account himself so I could see the difference."
{n}She folds her hands between her knees.{/n}
"The warehouse has changed its delivery arrangements. The investigators have lost the easy trail. They have other methods. Slower ones. I was asked whether clearing one smith was worth it."
{n}You ask what she told them.{/n}
"That we'd held good iron for two days. Then I went back to my room and was furious about losing Ordel's way into the warehouse."
{n}She says it flatly, and does not ask you to fix it.{/n}
"Brena has taken another watch order. She says she prefers knowing how to make us answer. Ordel says he preferred his old wage. The boy and his sister are safe with their aunt. None of that cancels the rest."
{n}She draws the damaged sword toward her and examines the grip.{/n}
"I signed the order. I'll answer for Ordel's lost access too."''', c('"What will you do when the next officer has to make the same choice?"', "officers")),
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
{n}She sounds relieved, and then annoyed at being relieved.{/n}
"I nearly thanked you for permission. I don't need your permission. I'm Knight-Captain; I could issue this in my sleep. I wanted somebody to tell me it's all right to like issuing it. Iomedae forgive me, I do."
{n}She folds the page along its old crease.{/n}
"I'll have to stand there while men who've never lost a night's sleep over their own names explain why mine's a distraction. Some of them will have real objections. I'll have to hear those too."
{n}Her smile gets an edge.{/n}
"I mean to be unpleasantly well prepared. I may even enjoy that part."''', c('[Ask what help she actually wants.]', "help")),
    n("support", "Irabeth", '''"I would welcome the support. Leave the instruction in my name. I want the responsibility where I can answer for it."
{n}She takes a clean sheet and writes a space for your endorsement beneath her signature.{/n}
"They'll say I got your signature because you enjoy my company. Let them. If they find a bad clause, I'll hear it at the meeting."
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
    n("gentle", "Irabeth", '''"Gentle, then. I'll still want you there."
{n}She holds out her hand, palm up, the way she holds it out for a report.{/n}
"Don't look so worried. I asked, you answered. That's quicker than a week of guessing."
{n}Her fingers close around yours, comfortable.{/n}
"I'm pleased. Honestly. We'll find out what we like as we go."''', c('[Arrange the quieter evening.]', "end")),
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
    n("broken", "Irabeth", '''"Tired. Glad to be here. Both."
{n}She keeps your hand, but her eyes go to the open window.{/n}
"This morning a sergeant was chewing out a recruit in the yard. Nothing cruel. Ordinary. And my hands started shaking like I was back in the ruins of Kenabres. I finished the inspection with them behind my back."
{n}She lets out a slow breath.{/n}
"I did my work. I still hear the things I say about myself on the bad days. They're louder when it's quiet."
{n}Her thumb moves against your knuckles, rough.{/n}
"So don't make tonight a cure. It isn't one. I want it anyway."''', c('"I believe you. Tell me what you want tonight."', "want")),
    n("encouraged", "Irabeth", '''"Better. I can say that now without looking over my shoulder for the reason it's wrong."
{n}She smiles, then goes thoughtful.{/n}
"Some days every mistake still reads like evidence at my own trial. Fewer of them. I've started letting the good days be good without checking them for cracks."
{n}She lifts your joined hands and kisses your fingers, quick, the way a soldier kisses a holy symbol before a charge.{/n}
"Today I wanted the meeting over because I had somewhere to be. That's all. An ordinary thing. It hit me like a warhorse, how much I wanted it."
{n}Her eyes stay on yours.{/n}
"Don't let it go to your head."''', c('"Then let us enjoy the evening we have."', "want")),
    n("ordinary", "Irabeth", '''"Curious what happens when I stop getting ready for the next question."
{n}The answer seems to surprise her.{/n}
"I thought about this room all through the meeting. Unprofessional. I still heard every objection, so the watch survived."
{n}She turns your hand over in hers and frowns at a small scar on it, as if it were a breach in a wall she is answerable for.{/n}
"No grand account of myself tonight. I wanted you. I made arrangements. Here you are."
{n}She shifts along the bench until her knee is against yours, and leaves it there.{/n}''', c('[Tell her what you want tonight.]', "want")),
    n("want", "Irabeth", '''"I want your hands on me because you like them there. Not because you're being kind to the half-orc."
{n}The bluntness brings heat to her face. She shoves a strand of hair back from her temple and does not take the words back.{/n}
"People think I'm made of iron or of glass, depending on who's looking. I'm neither. I'm a woman who's been thinking about your mouth all day and is sick of thinking."
{n}The grin shows the tips of her tusks.{/n}
"Should I stop talking? Nevi says it's my worst tactic."''',
      c('[Kiss her and draw her close.]', "close"),
      c('"Hold me. I want a quiet evening against you."', "rest"),
      c('"I want your company, but no touch tonight."', "space")),
    n("close", "Narrator", '''{n}You kiss her. Irabeth leans into it the way she leans into a shield wall, one hand hot at the back of your neck, the other braced on the bench. When your fingers find the open collar of her shirt she makes a low sound and yanks the laces loose herself, out of patience with them.{/n}
{n}You push the cloth off her shoulder and put your mouth to the scarred skin there. Her breath goes ragged. She laughs, low, and drags you back up to kiss you again.{/n}
{n}The bench groans under the two of you. Dema's warning was fair. Irabeth plants a boot, hauls you up with her in one motion and steers you backward across the room until the stacked benches knock against your shoulders.{/n}
{n}"Better," she says against your mouth.{/n}''',
      c('[Keep the rest of the evening private together.]', "private", flags=("irabeth.private_night",)),
      c('"This is what I wanted. Let us stay here a while."', "held", flags=("irabeth.private_kissed",))),
    n("private", "Narrator", '''{n}You shove the window shut. Irabeth kicks the blanket off the bench onto the floorboards, then turns back to you and drags her shirt over her head in one soldierly pull, as if it had been disobeying orders. Old scars run white across her ribs and shoulders. She watches your face while you look.{/n}
{n}"Don't just inspect it, Commander."{/n}
{n}Her hands go to your belt. She is quicker with buckles than anyone you have ever met; she does armour for a living. She sinks down onto the blanket, pulls you down after her with a grip that does not ask twice and rolls you under her, her weight settling over your hips as her mouth comes down on yours.{/n}
{n}Later, the bell for the night watch is ringing across the rooftops when she lifts her head. Irabeth goes very still and listens to it the way other people listen for their names.{/n}
{n}"That's the roll. I sign it. Every night for two years, I've signed it." She drops back onto the blanket. "Hadran will sign it. Hadran will enjoy signing it. Hadran will tell everyone."{/n}
{n}She glares at the ceiling a moment longer. Then she reaches past you for the bread, tears off the heel and gives you the larger half.{/n}
{n}"Let him."{/n}''', c('[Stay until it is time to leave together.]', "end")),
    n("held", "Narrator", '''{n}Irabeth wraps both arms around you and props her chin on your shoulder, and it is plain she has no plans to move for some time. When the stacked benches start digging into your back she notices before you say anything, grumbles about carpenters who have never held anybody in their lives, and walks you three steps sideways without letting go.{/n}
{n}Eventually you end up on the bench again, sideways under the blanket, sharing the bread and talking about nothing that needs finishing. Once she kisses you in the middle of a sentence, then finishes the sentence.{/n}
{n}"I'd like this room remembered for something besides its benches," she says.{/n}
{n}You tell her its reputation is improving.{/n}''', c('[Let the evening end where you left it.]', "end")),
    n("rest", "Narrator", '''{n}She puts an arm around you. You find a place against her shoulder, and she drags the blanket over you both without making a ceremony of it.{/n}
{n}For a while she watches the window. Then you feel her settle, all of her at once, like a soldier told to stand down. Her hand rests open against your arm.{/n}
{n}"I had a speech ready about not being much good at this," she says.{/n}
{n}"You may omit it."{/n}
{n}"Merciful."{/n}
{n}Street noise drifts in through the gap in the window. When you start to shiver she hauls you closer without a word and tucks the blanket in round you both like a quartermaster squaring a bunk. Later you share the bread and stay on the bench until the room is dim enough that she has to light the lamp to find her coat.{/n}
{n}When she turns back to you she looks rested, which on Irabeth is rare enough to notice.{/n}''', c('[Thank her for the quiet company.]', "end", flags=("irabeth.private_rest",))),
    n("space", "Irabeth", '''"Fine."
{n}She shifts along the bench to give you room and sets the bread down between you like a border marker.{/n}
"Disappointed? Yes. Don't look so stricken. Pass the knife."
{n}She cuts the loaf, hands you the heel and considers her own piece.{/n}
"Talk, or shall I attempt the remarkable discipline of sitting quietly?"
{n}You choose. She follows your lead, sometimes talking, sometimes content to sit. By the time the loaf is gone she has stopped glancing at the blanket.{/n}
"I'm glad you came," {n}she says when you rise.{/n} "Still true."''', c('[Leave while she is still smiling.]', "end", flags=("irabeth.private_space",))),
    n("end", "Irabeth", '''{n}You fold the blanket together. Irabeth takes one end and you take the other, and the simple job takes longer than it should because she keeps finding reasons to look at you.{/n}
"Again. Some version of it. I'm not writing this one up as standing procedure."
{n}Downstairs, she hangs the key back on its hook and stops at the open door.{/n}
"Go where you said you'd go next. I'll do the same. Nobody sits up waiting on either of us tonight."
{n}She grins at you before stepping into the lane.{/n}
"And I'll bring more bread."''',
      c('[Part for the night.]', flags=("irabeth.private_evening_kept",))),
], requires=("irabeth.costs_kept",), delay=48)


s("after_the_shared_answer", "The invitation that remained",
  '"You invited me to continue with you separately. I would like to answer."', [
    n("start", "Irabeth", '''"I did. I haven't changed my mind."
{n}Irabeth makes room for you beside her. She does not try to make it look like a first confession.{/n}
"We've been lovers. We sat down with Nevi about what the three of us could make, and we decided to go on separately. I won't pretend that took us back to the day before any of it."
{n}She turns her ring once.{/n}
"Nevi says our marriage can hold me going on with you. She and I have sorted the time we keep for ourselves. I want that time. I want you, too."
{n}She gets to the point, as she does with dispatches.{/n}
"Just us. Not a trial run for the three of us, and nothing I'll hang my head over. Say yes or no. I can take either."''',
      c('"I want that too. What do you want us to keep?"', "terms"),
      c('"I do not want to continue as your lover."', "stop"),
      c('[Think about the invitation and return later.]', abort=True)),
    n("terms", "Irabeth", '''"Knowing where you are when you're not with me. Your hand on my back when nobody's looking. And a good row now and then without either of us deciding it means we never should have started."
{n}She puts her palm flat on the bench between you.{/n}
"And days with actual dates on them. I won't have this be a conversation we keep repeating instead of making appointments."
{n}You ask where other lovers would fit.{/n}
"Love who you like. I'm Nevi's wife; that doesn't change. If you and she have something of your own, that's between you two. I answer for me."
{n}Her smile comes back, small and stubborn.{/n}
"Right now I want you at the recitation. After that, there's a wagon of cold iron to argue over. You may enjoy the duke more. I certainly do."''', c('"Yes. To both invitations, and to you."', "yes")),
    n("yes", "Narrator", '''{n}She takes your hand. The touch is familiar, the relief in her face less guarded than she probably intended.{/n}
{n}"Good. I have spent enough time rehearsing the question."{/n}
{n}You sit together while she describes the guard, the duke and the missing wool. She gives the duke an offended cough and laughs when you immediately recognize the sort of man she means.{/n}
{n}When you part, Irabeth names a day and writes it on the back of the recitation list, where she cannot lose it.{/n}''',
      c('[Take her hand and keep the day.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.marital_terms_agreed", "irabeth.legacy_separate_history", "irabeth.boast_guard"))),
    n("stop", "Irabeth", '''{n}She lowers her eyes for a moment, then meets yours again.{/n}
"Thank you for telling me. I would have preferred the other answer. I will not ask you to give it for my sake."
{n}She folds her hands together and does not make you say it twice.{/n}''', c('[Leave her be.]', flags=("irabeth.closed",))),
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
    n("distance", "Irabeth", '''"I don't know how long you'll be gone. Every bone in me wants to draw up a schedule anyway."
{n}She looks at her hands.{/n}
"I wait badly. I'll bury myself in work and bite the head off anyone who asks if I've eaten. Nevi's told me so. Knowing hasn't cured it."
"What would help?"
"A true letter, if one can get through. Don't give me a date just to make me sleep. If nothing can get through, then nothing does, and I'll manage. I'm a soldier. I've managed before."
{n}She takes your hand.{/n}
"And I won't sit here counting days. There's work, and other things. I'll have stories of my own when you're back."''',
      c('"When I can write, I want to tell you ordinary things too."', "ordinary", flags=("irabeth.departure_ordinary",)),
      c('"I may not be able to write. I want you to have a life while I am gone."', "silence", flags=("irabeth.departure_silence",))),
    n("ordinary", "Irabeth", '''"Tell me something badly described. I have read enough precise reports."
{n}She smiles.{/n}
"A street you disliked. A meal that made you miss a less ambitious cook. Someone who said something so foolish that you looked around for a person to share it with. I would like to be that person, even if I receive the story late."
{n}Her fingers tighten briefly around yours.{/n}
"I shall try to answer in kind. I cannot promise the letters will find you. I can promise not to fill them entirely with assurances that everything is well. You know too much about Drezen to believe that."
{n}She leans closer.{/n}
"And if I write that I miss you, you are not to take it as an instruction to abandon the road. It will mean I miss you."''', c('[Tell her what you will miss about these evenings.]', "touch")),
    n("silence", "Irabeth", '''"I will. You may come back to an instruction longer than the city walls."
{n}She studies your joined hands.{/n}
"If no word comes, I'll think the courier's dead in a ditch, not that you've gone cold on me. I might be frightened. I'll keep it to myself."
{n}Her eyes come up to yours.{/n}
"And whoever walks back through that gate, I'll take them. You don't have to spend the road keeping yourself exactly the way I liked you."
{n}She laughs quietly.{/n}
"Though I reserve the right to remind you the evening was very good."''', c('[Let her know what you want to return to.]', "touch")),
    n("touch", "Irabeth", '''{n}She stands and holds out her arms, and waits.{/n}
"I have said the sensible things. Some of them twice. I would like to hold you before I discover another."''',
      c('[Step into her embrace and kiss her goodbye.]', "kiss"),
      c('[Let her hold you quietly.]', "hold")),
    n("kiss", "Narrator", '''{n}Irabeth hauls you in. The kiss is urgent, and then it isn't: you put your hand to her cheek and she goes still under it, eyes shut, then turns her head to kiss your palm.{/n}
{n}"I want you back," she says. "That's the whole unreasonable wish."{/n}
{n}You hold her until the runner's boots have gone past the door twice. When she steps back she keeps one hand in yours long enough to look you over properly, the way she checks a recruit's straps before a march.{/n}''', c('[Carry the goodbye with you.]', "end")),
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
      c('[Write plainly about a time you were frightened.]', "fear", flags=("irabeth.abyss_fear",)),
      c('[Put the paper away for another rest.]', abort=True)),
    n("absurd", "Narrator", '''{n}You write about a conversation in which every answer made the next question less sensible. You cannot capture the speaker's expression, so you describe how Irabeth might have played it: a dignified pause, a wounded look, a refusal to admit that the wool had never been mentioned.{/n}
{n}You hear her answering in your imagination. It is an answer made from memory, not a message crossing the planes. You leave room beside the paragraph for whatever she actually says if she ever reads it.{/n}
{n}Then you write that you wanted her hand in yours afterward. It is the plainest sentence on the page. You resist improving it.{/n}''', c('[Finish the letter.]', "end")),
    n("fear", "Narrator", '''{n}You write it plainly. There was something you had to do. You were afraid. You did it, or found another way, and the fear stayed after the doing.{/n}
{n}Irabeth would want it that way. She reads reports for a living and can smell a heroic one from across the room.{/n}
{n}At the end you write that you want to sit beside her on the tack-store bench and eat her bad bread. You don't ask her to carry any of the rest. You tell her what you miss.{/n}''', c('[Fold the page for a possible return.]', "end")),
    n("end", "Narrator", '''{n}You fold the letter and keep it with your own belongings. Nobody comes with a letter from Drezen. You smooth the fold once more, then stop before the paper wears through.{/n}
{n}If you see her again, you may give it to her. If not, it is written. You put it away and go back to the Abyss.{/n}''', c('[Keep the unposted letter.]', flags=("irabeth.abyss_written",))),
], requires=("irabeth.departure_kept",), chapters=(4,), remote=True, owner="Rest", delay=0)


s("the_person_who_returns", "The person at the door",
  '"We have time to speak again. What has changed for you?"', [
    n("start", "Irabeth", '''{n}Irabeth looks up as you approach. Whatever she was about to say about the papers before her stops when she sees that you have come to stay a while.{/n}
"Yes. I would like that."
{n}She puts the papers aside and moves to the chair near the window. The room is familiar. The expression with which she waits for you belongs to this particular day.{/n}''',
      c('"We said goodbye before I left. I wanted this conversation."', "returned", requires=("irabeth.departure_kept",)),
      c('"We were already lovers before I left, though we had no private farewell."', "earlier", requires=("irabeth.began_chapter_three",), forbids=("irabeth.departure_kept",)),
      c('"These new evenings matter to me. I want to keep finding time for them."', "late", requires=("irabeth.began_chapter_five",), forbids=("irabeth.departure_kept", "irabeth.legacy_shared_history", "irabeth.legacy_separate_history", "irabeth.single_affair_disclosed", "irabeth.legacy_bereaved_history")),
      c('"We go back further than these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_bereaved_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We go back further than these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_shared_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We go back further than these new days. I want to hear how you are now."', "older", requires=("irabeth.legacy_separate_history",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three")),
      c('"We go back further than these new days. I want to hear how you are now."', "older", requires=("irabeth.single_affair_disclosed",), forbids=("irabeth.departure_kept", "irabeth.began_chapter_three"))),
    n("earlier", "Irabeth", '''"I missed you. I didn't need a farewell for that."
{n}She lets it stand, then reaches for your hand.{/n}
"I kept on here. I thought about our evenings at times when I should have been thinking about grain. I wanted to know whether you'd come back wanting another."
{n}The smile is not quite sure of itself.{/n}
"You have. Good. I won't ask for a report on every week you were gone. Tell me what you want to. I'll do the same."''', c('[Take her hand and start talking.]', "history")),
    n("older", "Irabeth", '''"Good. I'd hate for the new days to wipe out the old ones."
{n}She shifts closer and puts her hand where you can take it.{/n}
"We had what we had before. We've got more now. I didn't meet you for the first time at the storehouse, and I won't pretend I did."
{n}She snorts at the thought.{/n}
"I might have been less solemn if I had. Or more. I've never been reliable on that."
{n}Her attention settles on you.{/n}
"Tell me about today. One afternoon. We don't need the whole history."''', c('[Tell her about today.]', "history")),
    n("returned", "Irabeth", '''"So did I. I pictured it badly, several ways. Either you came back in pieces and needed nursing, or you strolled in untouched and bored. Neither one let you get a word in."
{n}She holds out her hand and waits for you to take it.{/n}
"I'm glad you're here. I've got questions. I'll ask the wrong one first; I always do. Tell me to shut up if I do."
{n}Her fingers close around yours when you sit.{/n}
"That line about the proper box. It came in useful more often than I'd like. I kept wanting to tell you."
{n}She smiles, then goes quiet.{/n}
"Come here first. The questions will keep."''',
      c('[Hold her before beginning the conversation.]', "history"),
      c('[Keep her hand and begin with words.]', "history")),
    n("late", "Irabeth", '''"I'm glad we found our way to these evenings."
{n}She sits down beside you, close enough that her shoulder is against yours.{/n}
"I remember how long we circled it before we started. No point turning that into some grand farewell we never had. I've liked the days we've actually had. Tell me how they've been for you."
{n}She glances at the papers she left behind.{/n}
"This city makes every pleasure look badly timed. There's always a list of people who need something first."
{n}Her smile warms.{/n}
"You've been a considerable distraction from the list. Keep it up."''', c('[Talk about the days you have had.]', "history")),
    n("history", "Irabeth", '''{n}The talk wanders. Some subjects she takes at a run. Others she walks all the way round first, the way she walks round a suspect wagon.{/n}''',
      c('[Give her the letter you wrote and kept.]', "letter", requires=("irabeth.abyss_written",)),
      c('"You told me about the Queen at Iz. I have not forgotten what you said."', "queen", requires=("irabeth.queen_loss_known",)),
      c('"I want to say one thing about what I did to you. You need not answer me."', "scar", requires=("irabeth.scar_known",)),
      c('"Tell me what you want from the days ahead."', "ahead")),
    n("letter", "Narrator", '''{n}Irabeth takes the folded page. She sees the wear along its creases before she reads the first line.{/n}
{n}"You kept it."{/n}
{n}You tell her there was no way to send it. She nods and reads it standing, like an order that arrived late and still stands.{/n}
{n}Halfway down, her thumb stops on the paper's edge. She finishes, folds it along the old creases and keeps it in her fist.{/n}
{n}"I couldn't see any of that from here," she says. "I haven't got the answer I'd have written then. I've got the one I can give you now."{/n}
{n}She takes your free hand. For a while that is the answer. Later she asks one question about what you described, and listens to the answer without interrupting once, which from Irabeth is a declaration.{/n}''', c('[Let her keep the letter.]', "ahead", flags=("irabeth.letter_given",))),
    n("queen", "Irabeth", '''{n}Her face goes still.{/n}
"I said nobody should rely on me. I remember."
{n}She looks at the window a while.{/n}
"I was given the Queen to guard, and I didn't bring her home. There's no clever way to say that. Don't go looking for one to make me smile at you."
{n}She turns back, jaw set.{/n}
"I'm glad you're here. I'm still angry at myself. Those will sit side by side a good long while, and neither of us is arguing them out of it tonight."
{n}Her hand rests near yours.{/n}
"Let me pick something I can still do something about. That's all I ask."''', c('"Choose it. I will listen."', "ahead")),
    n("scar", "Irabeth", '''{n}Her hand starts toward her cheek, then drops.{/n}
"I told myself I deserved to be stopped. I'm not arguing that with you tonight, and I'm not discussing the mark."
{n}She holds your gaze, hard.{/n}
"And I won't sit here playing the noble scarred knight so you can feel better about it. Say it if you mean to say it. Don't ask me to forgive you on the spot."
"I hurt you. I won't pretend I knew better."
{n}She is quiet a while.{/n}
"Heard. That's the end of it for tonight. And keep your hands off my face."
{n}You keep your hands where she can see them. She draws a breath and picks the next subject herself.{/n}''', c('[Keep your hands where she can see them.]', "ahead", flags=("irabeth.harm_acknowledged",))),
    n("ahead", "Irabeth", '''"I want the instruction to work when I am not standing over the officer using it. I also want to go somewhere after the war without being invited to inspect the defenses."
{n}The second admission brings a little warmth back into her voice.{/n}
"There is a route-maker in the city. Sella. She has a collection of old road drawings, some useful and some apparently intended to make travelers admire the artist. I asked whether she would show me how she chooses between them."
"For the watch?"
"For me. She asked the same question. I found it irritating both times."
{n}Irabeth smiles to soften the rebuke.{/n}
"The instruction will need a final review. After that, I would like to spend an afternoon learning enough about a road to choose it for pleasure. You could come. You may prefer a different road. You will be wrong."''', c('"I would like to see what you choose."', "end")),
    n("end", "Irabeth", '''{n}She returns to the desk only long enough to take a small sheet from beneath the work papers. It names Sella and an hour, with two alternative days beneath it.{/n}
"She gave me alternatives because I kept saying that something might happen. Apparently something may also happen to her. I found the reminder helpful and mildly offensive."
{n}You choose a day together. Irabeth puts it where she will have to see it before accepting another appointment.{/n}
"There. Sella's expecting us. Don't let me give the hour away to another report."''',
      c('[Keep the day.]', flags=("irabeth.return_kept",))),
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
"Vela used it without asking whether I would be present to protect her from complaints. That matters more. I still intend to remember the afternoon."''', c('[Let her enjoy it.]', "last_cost")),
    n("endorsement", "Irabeth", '''"It made them read it. A useful beginning. After that, they argued with me about the form, the compensation and whether reviewing a detention requires another officer every time."
{n}She smiles.{/n}
"They were irritated enough that I think they forgot to be impressed by your signature. I preferred them that way."
"And the personal accusation?"
"One person implied that I had an unusual way of obtaining support. I asked which paragraph he wanted changed. He had no answer prepared. I gave him time."
{n}She touches the folded page.{/n}
"You supported work you had read. I defended it. Vela used it. There will be other whispers. I am not going to stand outside every room until it has decided to like me."''', c('[Ask about the cost still attached to the first case.]', "last_cost")),
    n("last_cost", "Irabeth", '''{n}She takes a second page from the stack. This one is short enough to read while standing.{/n}''',
      c('[Read the training and source update.]', "sealed_end", requires=("irabeth.account_sealed",)),
      c('[Read the carrier and investigation update.]', "open_end", requires=("irabeth.account_open",))),
    n("sealed_end", "Irabeth", '''"The repaired grips have arrived. The training groups are no longer sharing quite so resentfully. Brena charged what she quoted and refused to reduce the price for the watch. I paid it."
{n}She points to the next line.{/n}
"Ordel's information led the investigators to a stored lot of false bars. That lot has been seized and tested. I will not tell you it means every bad supplier is gone. It means those bars will not be issued as sound metal."
{n}You ask whether Brena will hear about the seized bars.{/n}
"If she asks. Her complaint stays in the account. Those bars belong in the warehouse inquiry. They don't cancel the two days we kept her wagon."
{n}Irabeth folds the update.{/n}
"That is where the matter stands. I can close my part of the file without pretending nobody paid for it."''', c('[Leave the case at work.]', "end")),
    n("open_end", "Irabeth", '''"Ordel has accepted the final payment for his lost commission. It does not make his new work as profitable. He knows I know. He has stopped bringing the difference to my door every week."
{n}She shows you the last paragraph.{/n}
"The investigators traced one false shipment through its buyer instead of the warehouse. It took longer. They recovered less than they hoped. The recovered lot has been tested and kept out of issue."
{n}You ask how matters stand with Brena.{/n}
"Her next delivery was checked by quantity and returned to her forge before noon. She sent Vela a note explaining three ways to improve the tally. Vela used two. I believe that is the closest thing to praise we are likely to receive."
{n}Irabeth folds the update.{/n}
"I'd still rather have kept Ordel in that warehouse. We lost his access. Brena got the original pages, and Vela used her corrections. Put all of that in the account."''', c('[Let the case close.]', "end")),
    n("end", "Irabeth", '''{n}Back at headquarters she ties the completed papers together. The changed form remains out for copying. She places the case on the finished side of the shelf and leaves it there.{/n}
"Now I would like to see Sella's road drawings. I am going to ask a question whose answer need not improve military readiness."
{n}She turns toward you with a look of deliberate challenge.{/n}
"Which view would I enjoy waking up to? I have several preferences. Some are inconvenient. I intend to defend them."''',
      c('[Keep the appointment with Sella.]', flags=("irabeth.instruction_tested",))),
], requires=("irabeth.return_kept",), chapters=(5,), delay=48)


s("a_road_she_would_choose", "A road without an assignment",
  '"Sella is expecting us. Have you decided what you want to ask?"', [
    n("start", "Irabeth", '''"Whether a view described as 'sublime' can be reached without spending four days climbing through rain. The descriptions are remarkably evasive about rain."
{n}Irabeth has brought a small notebook. She holds it up before you can object.{/n}
"Personal use. I am allowed to remember things."
{n}You walk to Sella's room above a provisioner's shop. The route-maker is sorting drawings by age rather than destination. She explains that an old bridge remains an old bridge even when someone copies it beautifully onto new paper.{/n}
{n}Irabeth looks immediately interested.{/n}
"That is an excellent reason to distrust attractive handwriting."
"Only when it describes a bridge," {n}Sella replies.{/n} "Otherwise it depends on what you want from the writer."
{n}Irabeth glances at you and discovers you already looking at her.{/n}
"We are here for roads," {n}she says, less firmly than she intended.{/n}''', c('[Make room for the drawings.]', "drawings")),
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
"That one," {n}Irabeth says, then stops.{/n} "If it suits you. I have begun giving orders to an imaginary journey."
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
    n("want", "Irabeth", '''"I want a trip like this. Longer. Better views. Fewer onions."
{n}She puts her hand down next to yours on the step.{/n}
"I want to choose a road, get it wrong, and have you beside me while I swear at the map. We can find the right turning after."
{n}She looks at the drawing in her lap.{/n}
"I won't stop being a knight. I like most of it. But I want to be able to hand my post to someone for a fortnight without the whole citadel acting as if I'd deserted."
{n}She looks up at you.{/n}
"Would you come? Not every road. Just keep asking me where we're going."''',
      c('"Yes. I want to keep coming back to you, for good, and the people we love can come too."', "lasting", flags=("irabeth.future_lasting",)),
      c('"I want you in my life. I can\'t promise you a roof, but I\'ll keep turning up."', "open", flags=("irabeth.future_open",)),
      c('"I care for you, but I want us to become friends rather than continue as lovers."', "friend", flags=("irabeth.future_friends",))),
    n("lasting", "Irabeth", '''"So do I."
{n}She takes your hand and holds on, as if that makes it official.{/n}
"There'll be work. There'll be my marriage, and whoever else you've got. We may never share a roof, and I won't pretend otherwise. But I'll keep finding you days. Actual days, not speeches."
{n}The smile comes out shy, which on her is startling.{/n}
"I want that journey. Then we'll come home, dry our boots, and argue about which inns were worth the rain. Next time I want you at the table when we choose the road."
{n}She leans in and kisses you, there on the step, and one of the onions rolls away down the lane.{/n}''', c('[Kiss her back and let the onion go.]', "end", flags=("irabeth.committed",))),
    n("open", "Irabeth", '''"I can want that without pretending you offered more."
{n}She looks at your hand near hers a moment, then takes it.{/n}
"Another day, then. Maybe the road. If one of us starts wanting more than the other can give, we say so. Out loud. I've no stomach for sulking."
{n}She smiles.{/n}
"For now I've got your hand and no report to finish. Stay a while."
{n}She leans against you a moment, and asks nothing more of it than that.{/n}''', c('[Lean back against her.]', "end")),
    n("friend", "Irabeth", '''{n}She breathes in, and lets it go before she answers.{/n}
"Damn. I wanted the other answer."
{n}She looks at the drawing, not at you, and does not force a smile.{/n}
"Friends, then. Give me a few weeks before I'm easy company. I'm not sulking. I'm regrouping."
{n}After a while she folds the drawing and looks back at you.{/n}
"It was a good afternoon. I'm keeping it."''', c('[Accept the change in where you stand.]', "end")),
    n("end", "Narrator", '''{n}You return the exercise to Sella. Irabeth describes the misleading passage in detail. Sella asks which clue finally made her trust the drawing or doubt it, and listens to the answer before returning the exercise to its place.{/n}
{n}The real road drawing stays with Irabeth. She pays for the copy, places it inside her notebook and carries the onions home in the other hand. The afternoon has produced a plan, a mistake worth laughing at and an answer she does not bother to write down.{/n}''',
      c('[Carry the onions home.]', flags=("irabeth.future_chosen",))),
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
"That's done. Whatever happens tomorrow can't take it back."''', c('[Ask about Sella\'s drawing.]', "future")),
    n("future", "Irabeth", '''{n}She takes the road drawing from a narrow shelf. It is folded along the same lines you made together.{/n}''',
      c('"I meant what I said at the arch. All of it."', "lasting", requires=("irabeth.future_lasting",)),
      c('"I meant the days, not a house. I still do."', "open", requires=("irabeth.future_open",)),
      c('"I\'m glad we stayed friends."', "friends", requires=("irabeth.future_friends",))),
    n("lasting", "Irabeth", '''"I meant it too. I don't need a battle to prove it."
{n}She unfolds the drawing far enough to show the road.{/n}
"If we get the days after, we start with a visit we can keep. Then the journey, when duty lets us. And when you're gone, I won't be counting it against you."
{n}Her fingers rest beside the inked road.{/n}
"I'll have work. You'll have more than either of us can guess. I won't live at the edge of your life grateful for scraps, either. When I want you, I'll come and take you by the collar. You'd best do the same."
{n}She looks up, warm and very serious.{/n}
"That's the promise I can make before a battle. That I'll still be talking to you after it, if we're both breathing."''', c('[Kiss her hand. Promise nothing about tomorrow.]', "wife")),
    n("open", "Irabeth", '''"Good. I'd have noticed if a goodbye suddenly came with a house and a lifetime."
{n}The smile takes the edge off it.{/n}
"I want more time with you. I don't know where it fits. That was true at the arch, and it's true with men sharpening swords downstairs."
{n}She folds the drawing again.{/n}
"I'm not going to squeeze a bigger promise out of you because you might die. That's a recruiting sergeant's trick."
{n}She lays the paper between you.{/n}
"Come find me after, if you can. We'll decide what the next day wants when there is one."''', c('[Leave it open.]', "wife")),
    n("friends", "Irabeth", '''"So do I. I've had my sulk. You were spared most of it."
{n}She smiles with some of the ease you remember from the storehouse.{/n}
"I still want you alive. I still want to hear what you think of a road. I might take someone else, or go alone, or find the inn's better than the lake. You don't have to stand in the same spot in every version."
{n}She puts the drawing away.{/n}
"The work mattered. The laughing mattered. That's enough to keep."
{n}Her hand rests open on her knee.{/n}
"Thank you for coming before the fighting. I wanted this."''', c('[Stay a while.]', "wife")),
    n("wife", "Irabeth", '''{n}Her gaze drops to the ring on her hand. She turns it once.{/n}''',
      c('"What do you want to say about Anevia tonight?"', "wife_living", forbids=("anevia_dead", "anevia_gone")),
      c('[Give her room to speak about Anevia\'s death.]', "wife_dead", requires=("anevia_dead",)),
      c('[Give her room to speak about Anevia\'s absence.]', "wife_gone", requires=("anevia_gone",), forbids=("anevia_dead",))),
    n("wife_living", "Irabeth", '''"That I love her. That there are things I've got to say to her that are ours. And that I don't have to sneak this hour from her to have it."
{n}She turns the ring once, and leaves it.{/n}
"We'll have our own goodbye. I'll try to make it sensible. She'll laugh at me for it. We've had plenty of practice."
{n}The smile is for someone else in this city, not for you, and she does not apologise for it.{/n}
"And I won't speak for her. She's always been very capable of speaking for herself. Loudly."''', c('[Let her keep that goodbye for Anevia.]', "choice")),
    n("wife_dead", "Irabeth", '''{n}She is quiet long enough that you start hearing the small noises outside the room.{/n}
"I wanted one more goodbye with her. Maybe it'd have been no better than the last. I wanted it anyway."
{n}Her hand closes on the ring, then opens.{/n}
"I miss her, and I'm here with you. I'm done putting every good hour on trial for her sake. She'd have laughed at me for it."
{n}She looks at you.{/n}
"Tonight I want to remember her laugh before I remember the rest. Don't try to say the right thing. There isn't one."
{n}You sit with her while she tells a small story about a pen Anevia swore she had not stolen. The marriage in it is still hers, whatever this room now holds.{/n}''', c('[Stay while she finishes the story.]', "choice")),
    n("wife_gone", "Irabeth", '''"I don't know what goodbye I'm allowed to picture. That's the truth."
{n}She watches the ring on her hand.{/n}
"I won't bury her to make things tidy. And I won't tell you I know when she's coming back. I don't."
{n}She draws a breath.{/n}
"I know what you and I said. I know what she and I said when we still could. That'll have to do."
{n}Her eyes come up to yours.{/n}
"Thank you for not pushing. The rest of this hour, I want it here."''', c('[Leave the uncertainty as it is.]', "choice")),
    n("choice", "Irabeth", '''{n}The room grows quieter as the traffic outside moves elsewhere. Irabeth looks toward the door, then back at you.{/n}
"We still have a little time. What would you like?"''',
      c('[Kiss her, and keep the rest of the hour private.]', "night", forbids=("irabeth.future_friends",)),
      c('[Ask her to hold you.]', "hold", forbids=("irabeth.future_friends",)),
      c('[Stay and talk until it is time to leave.]', "talk")),
    n("night", "Narrator", '''{n}Irabeth stands when you do. She takes your kiss with both hands flat against your back, hard, then pulls away just far enough to look at you.{/n}
{n}"Yes," she says. It is not a question.{/n}
{n}She is already working at her own buckles. The breastplate hits the floor with a clang the whole landing must hear, and she does not care. Vambraces, gambeson, shirt: all of it goes onto the chair that catches on the uneven stone. Then she has your clothes by the fistful, and they go the same way. She walks you back to the window seat, pushes you down onto it and straddles your lap, knees clamped either side of your hips, one hand knotted in your hair, and brings her mouth down on yours.{/n}
{n}Later she arms you strap by strap, as if you were a squire she did not trust with buckles, and lets you do hers. On the way down she stops at the duty board, takes the chalk and writes her own name on the line beside yours for the morning's muster. The officer on duty watches her do it and says nothing. Neither does she.{/n}''', c('[Go down to the muster together.]', "end", flags=("irabeth.farewell_private",))),
    n("hold", "Narrator", '''{n}She pulls you into her arms. The hold is fierce at first, like a braced shield, then eases as you settle against her. For a while the only words are small ones, said into your hair.{/n}
{n}When you step back she keeps your hand long enough to press it between both of hers.{/n}
{n}"Next time I do this, I want it to be because you're only going across the street."{/n}
{n}You tell her you would like that too. Neither of you calls it a promise.{/n}''', c('[Let her release you when it is time.]', "end", flags=("irabeth.farewell_held",))),
    n("talk", "Narrator", '''{n}You stay by the window. The talk wanders from practical matters to the storehouse, then to an especially unlikely stretch of Sella's drawing. Irabeth gives the misleading passage a last offended description and makes you laugh.{/n}
{n}When the hour is nearly gone she falls quiet. You don't hurry to fill it. She looks at you the way she looks at a map she means to carry in her head.{/n}
{n}"I'm glad we had the days," she says.{/n}
{n}You stay until it is time to stand.{/n}''', c('[Stand when it is time.]', "end", flags=("irabeth.farewell_talked",))),
    n("end", "Irabeth", '''{n}Irabeth opens the door and stands beside it, giving you room to go and one last unhurried look.{/n}
"Go and do your part. I'll do mine. If there's a road afterward, we'll pick it then."
{n}She smiles, with none of the guard's borrowed grandeur.{/n}
"I'll be difficult about the inns. You've been warned."''',
      c('[Go and do your part.]', flags=("irabeth.campaign_kept",))),
], requires=("irabeth.future_chosen",), chapters=(5,), delay=24)


def ending(identity, title, nodes, *, requires=(), forbids=(), any_of=(), owner="Epilogue"):
    SCENES.append(scene("irabeth.ending_" + identity, title, owner, 0, "", nodes,
        requires=("irabeth.lover", *requires),
        forbids=("closed", "irabeth.closed", "trying", "committed", *forbids),
        last=99, Relationship="irabeth", RequiresAny=list(any_of),
        ForbidOverrides={"trying": "tirabade.group_closed", "committed": "tirabade.group_closed"}))


ALIVE_END = ("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich", "sacrifice", "ascended")

ending("lasting", "The journeys she chose", [
    n("start", "Narrator", '''{n}After the war Irabeth kept her rank for exactly one more year, trained the officer who replaced her, and then took the fortnight's leave she had been threatening since Drezen. She slept through the first day of it. She spent the second arguing with an innkeeper about the price of a room with a view of the lake.{/n}
{n}The Commander came on that journey, and on several after it. The road from Sella's drawing was washed out in two places. Irabeth called it a disgrace, took the long way round, and told the story for years as if she had planned the detour. When it rained she complained about the rain, and then asked to stay another day.{/n}
{n}They quarrelled like soldiers: loudly, briefly, and over the washing-up. She still recited the guard and the duke whenever anyone was fool enough to ask, and the duke grew more offended every year.{/n}''', c('[Remember the other life she kept with it.]', "marriage")),
    n("marriage", "Narrator", '''{n}Irabeth's ring stayed on her finger. She turned it when she was thinking, and she never once took it off on the Commander's account.{/n}''',
      c('[Remember the living marriage.]', "living", forbids=("anevia_dead", "anevia_gone")),
      c('[Remember the wife she mourned.]', "dead", requires=("anevia_dead",)),
      c('[Remember the wife who never came back.]', "gone", requires=("anevia_gone",),
        forbids=("anevia_dead", "anevia.trickster.returned")),
      c('[Remember the wife who came back to the gate.]', "returned", requires=("anevia_gone", "anevia.trickster.returned"),
        forbids=("anevia_dead",))),
    n("returned", "Narrator", '''{n}Anevia came back as far as the Drezen gate and, for a long while, no further. Irabeth walked out to the road side of the line every evening she was off duty, and after the war she walked out one last time with both their packs and did not come back in.{/n}
{n}They took the house on the corner in the end. Anevia made the Commander knock on its door every single time, three knocks, like a person, and Irabeth pretended not to be listening for them.{/n}'''),
    n("living", "Narrator", '''{n}Anevia and Irabeth stayed wives, in the house on the corner, with the stone oven Anevia finally bullied a mason into building. The Commander came to supper on the nights Irabeth asked and to breakfast on the mornings Anevia did, and learned which of those invitations could be refused and which could not. Anevia burned the first loaf out of the new oven and made everyone eat it.{/n}
{n}Irabeth went on asking for what she wanted, in her abrupt way. A road. A room. A hand at the back of her neck while she read reports. An audience for the guard. She liked the applause. She liked the Commander still being there when it stopped.{/n}'''),
    n("dead", "Narrator", '''{n}On the first day of every month Irabeth went to Anevia's grave and told her, out loud, the price of bread and which officers were fools. The Commander learned to wait at the cemetery gate on those mornings and not to ask.{/n}
{n}The road drawing stayed in her notebook, beside a pen Anevia had sworn she never stole. Irabeth laughed again within the year. She was furious with herself the first time, and then she was not.{/n}'''),
    n("gone", "Narrator", '''{n}Anevia never came back, and no letter ever said why. Irabeth kept a lamp in the window of the house on the corner for three winters. Then she gave the house to a widow from Kenabres, moved into barracks, and kept the key on a cord round her neck.{/n}
{n}She never called herself a widow, and she never let anyone else do it. When a stranger in an inn laughed like Nevi, she turned round, every time. The Commander learned to wait until she turned back.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_lasting"), forbids=ALIVE_END)

ending("open", "Another day freely chosen", [
    n("end", "Narrator", '''{n}After the war Irabeth and the Commander never shared a roof, and never pretended they would. They met when the roads allowed: a week at the lake one summer, a night at a Nerosyan inn the next, and once, memorably, two days snowed into a posting house where Irabeth taught the ostlers the guard and the duke and made them do the chorus.{/n}
{n}Some visits were cancelled, and she said so in short, cross letters. Some were not, and she said nothing about them afterwards at all, which from Irabeth was a love letter. She went on choosing the road. The Commander went on preferring a different one, and they went on arguing about it all the way there.{/n}
{n}Her ring stayed on her finger through all of it.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_open"), forbids=ALIVE_END)

ending("friends", "The friendship after the courtship", [
    n("end", "Narrator", '''{n}The courtship ended before the war did. For a month Irabeth was stiffly polite, which was worse than her temper. Then one morning she marched into the Commander's office, dropped a bag of onions on the campaign map and announced that she was done sulking.{/n}
{n}They stayed friends. She walked the road from Sella's drawing with two old sergeants from Kenabres and wrote back four pages of complaint about the inns. She kept on reciting, kept a place at the back of the room for the Commander, and never once pretended the kisses had not happened.{/n}'''),
], requires=("irabeth.campaign_kept", "irabeth.future_friends"), forbids=ALIVE_END)

ending("unfinished", "An invitation with days still to come", [
    n("end", "Narrator", '''{n}The war ended before the two of them had finished beginning. There had been a handful of evenings. There had not been the road, or the lake, or the quarrel about inns she had been saving up.{/n}
{n}Irabeth went back to her post and her paperwork. Once a season a note in her square hand reached the Commander, with a date on it, a place, and four words: "If you still want to." Whether anyone came was never entered in any report she wrote.{/n}'''),
], forbids=(*ALIVE_END, "irabeth.campaign_kept"))

ending("loss", "The woman who was not waiting", [
    n("start", "Narrator", '''{n}Irabeth did not see the end of the war, or did not stay for it. What had been said between her and the Commander stayed said. It did not bring her back to the gate.{/n}''',
      c('[Remember Irabeth, who died.]', "dead", requires=("irabeth_dead",)),
      c('[Remember Irabeth, who was gone.]', "gone", requires=("irabeth_gone",), forbids=("irabeth_dead",))),
    n("dead", "Narrator", '''{n}They buried Irabeth in Drezen with her sword on her chest and her rank cut into the stone, because she would have filed a complaint about anything less. The Commander kept a scrap of paper with the date of their first evening on it, in her square hand, underlined twice.{/n}
{n}People who spoke of her afterwards made her into a saint. The Commander remembered a woman who liked applause, cheated at cards when she thought nobody was looking, and told the duke's lines badly on purpose to make a room laugh.{/n}'''),
    n("gone", "Narrator", '''{n}Irabeth was gone, and nobody could say where. No letter came, and no report named her among the dead. The Commander kept the scrap of paper with the date of their first evening on it, and wrote no ending beneath it.{/n}'''),
], any_of=("irabeth_dead", "irabeth_gone"))

ending("changed", "A choice she did not follow", [
    n("end", "Narrator", '''{n}When the Commander became what the Commander became, Irabeth sent back her commission with a note of four words: "I serve Iomedae. Still." She took the wounded of the Drezen garrison and three companies who would follow her south to Kenabres, and she held the wall there against whatever came up the road, including, twice, the Commander's own messengers.{/n}
{n}One of them carried a letter under the old seal. She read it at the gate, twice, the way she read every order. Then she handed it back and told him to say she was on watch.{/n}
{n}She kept the road drawing. She kept nothing else.{/n}'''),
], any_of=("inhuman", "swarm", "true_lich"), forbids=("irabeth_dead", "irabeth_gone"))

ending("ascent", "The distance beyond the map", [
    n("end", "Narrator", '''{n}When the Commander ascended, the priests of the new cult came to Irabeth for stories of their god. She told them about the night the Commander laughed so hard at the duke that a chair broke, and which inns the Commander could not abide. The priests stopped coming.{/n}
{n}She went on praying to Iomedae, keeping her post and taking her leave at the lake. Some nights she said a few words up at the sky that were not prayers, and she never told anyone what they were.{/n}'''),
], requires=("ascended",), forbids=("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich"))

ending("sacrifice", "The answer she could no longer hear", [
    n("end", "Narrator", '''{n}Irabeth did not weep at the memorial. She stood at attention through every speech and walked out before the hymn. That night she recited the guard and the duke to an empty storehouse, the whole piece, and left the duke's lines out.{/n}
{n}The next summer she walked the road from Sella's drawing alone and argued with every innkeeper on it. When strangers told her the Commander had died for something greater, she said she knew that, and that she would still rather have had the Commander.{/n}'''),
], requires=("sacrifice",), forbids=("irabeth_dead", "irabeth_gone", "inhuman", "swarm", "true_lich", "ascended"))

ending("aeon", "A history without its meeting", [
    n("end", "Narrator", '''{n}When the Worldwound's history was rewritten, the evenings Irabeth and the Commander had spent together went with it. In the world that followed, a half-orc paladin kept her post in Kenabres, married a spy who laughed at her, and never learned a piece about a guard and a duke.{/n}
{n}Or perhaps she learned it from somebody else. The Commander never went to find out.{/n}'''),
], owner="AeonEpilogue")


s("after_the_answer_was_lost", "The answer grief could not supply",
  '"Anevia has died. I will not pretend that makes our unfinished conversation simple."', [
    n("start", "Irabeth", '''{n}Irabeth sits very still. The ring is on the hand resting on her knee.{/n}
"No. It doesn't."
{n}She takes her time.{/n}
"I remember what we said. I can't ask her for another answer now. And I won't pretend she gave me leave because she loved me. She never got the chance."
{n}Her eyes come up.{/n}
"Some days I want company. Some days I want everyone out of my sight, you included. I'll tell you which. It may change by supper."''',
      c('"We were lovers before this. I remember it, including what we hid."', "affair", requires=("i_affair",)),
      c('"We had only asked about a courtship. I won\'t call it more than that."', "question", forbids=("i_affair",))),
    n("affair", "Irabeth", '''"So do I. I won't dress it up now to make it easier to carry."
{n}She touches the ring once and leaves it be.{/n}
"I wanted you. I knew what I was doing. Whatever came after, I can't go back and start honest."
{n}Her voice steadies.{/n}
"I want to see you again. Slowly. If I talk about her, you listen. If I go quiet, you pass the bread. And nobody tells me losing her cleared the road. It didn't."''', c('"Slowly, then. I\'ll pass the bread."', "choice", flags=("irabeth.legacy_bereaved_history",))),
    n("question", "Irabeth", '''"Thank you. Everyone's been at me. She'd want you happy. You're young yet. Iomedae has a plan. All of it from people who never heard her swear."
{n}She looks toward the window.{/n}
"I want an evening with you. I'll probably miss her in the middle of it, and you'll have to put up with that. I'm not offering you her chair at the table. Don't sit in it."
{n}She turns back.{/n}
"There. Asked."''', c('"An evening, then. I won\'t sit in her chair."', "choice")),
    n("choice", "Irabeth", '''{n}She holds out her hand and leaves it there between you.{/n}
"Then we start with a day. I've a dispute over cold iron I'd like your help hearing. After that, something without a report attached. I've signed my name for a recitation. I want to find out whether I can still make a room laugh."
{n}Her mouth moves toward a smile without quite getting there.{/n}
"I might not like the answer. I'd still rather find out myself than have a chaplain tell me."''',
      c('[Take her hand, and let her lead.]', flags=("irabeth.started", "irabeth.lover", "irabeth.personal_ready", "irabeth.bereaved_courtship")),
      c('"I can\'t be that for you. I\'d like to stay your friend."', flags=("irabeth.closed",))),
], requires=("anevia_dead",), any_of=("irabeth.courtship_requested", "i_affair", "tirabade.irabeth_continuation_invited"),
    forbids=("irabeth.personal_ready",))


def integrate(payload):
    """Register observed native dialogue only; never write native morale or life states."""
    from storylines import irabeth_partner_stance
    irabeth_partner_stance.integrate(payload)
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
