"""Authored responses to changed Elan reports; historical romance flags stay intact."""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"

# Each join is after the existing marital-history passage, before the shared action.
BRIDGES = {
    ("guest_table", "history"): ("end",
        '''"We had separated before he died. Please don't make me choose which part I am allowed to remember."
{n}Kiana looks at Lenna, then at Odrin.{/n}
"I can miss him and still mean what I said when I left. I am glad I have company tonight. I would rather it were company than a hearing."
{n}Lenna puts her spoon down. "I'm sorry. I was trying to say something kind."
"I know. Tell me something else. Tell me how Odrin came to owe your butcher money."
"That was the dog," Odrin says immediately.
{n}Kiana reaches for the onions. "Then begin with the dog."{/n}''',
        '''"I mourned Elan. I meant what I said to you then. Now people bring me reports that disagree with one another, and expect me to know what to call myself before I have finished reading them."
{n}Lenna looks at you as though the Commander might supply a verdict. Kiana catches the movement.{/n}
"No. I asked you both to supper. If there is something certain to tell you, I will tell you. Until then, you may ask whether I want another onion."
"Do you?" Odrin asks.
"No. That one was terrible. Explain how you can afford to offend the butcher and still eat this well."
{n}He looks relieved to have a question he can answer.{/n}'''),
    ("market_weather", "past"): ("shut",
        '''"Since the news about Elan, I keep remembering our last conversation. There are things I wish I had said more gently. That doesn't mean I wish I had lied."
{n}She holds the cloth against her chest, protecting it from the rain.{/n}
"Lenna may have been afraid of saying the wrong thing. I would have understood that better than silence. I cannot spend every visit reassuring people that I won't break if they speak his name."
"Would you rather go home?"
"No. I want to return the jar. I can manage a jar. Tomorrow I may manage something more impressive."''',
        '''"People keep beginning with 'if.' If he is alive. If somebody has mistaken another knight for him. If I ought to have waited longer before wanting anything."
{n}A drop strikes the cloth. She brushes it away with unnecessary force.{/n}
"I want reliable news. I don't want to spend the rest of my life defending what I did with the news I had. Those are different requests."
"What would help today?"
"Returning this jar. Asking Lenna why she didn't answer. Something somebody in this street can actually tell me."'''),
    ("blue_room", "box"): ("pin",
        '''"I kept things when we separated. Now he is dead, I keep being tempted to treat every object as though I must either bury it or worship it."
{n}She turns the cracked comb in her hand.{/n}
"Some of it is simply mine. He knew that too. He would have been very impatient with this comb."
{n}She laughs once, then puts it back.{/n}
"The picture can stay where it is. You needn't admire it on entering. I would like you to look at me, preferably before I lose my nerve about this shawl."
{n}She closes the box and draws the blue cloth toward her.{/n}''',
        '''"I started sorting things when I believed there would be no more of his things to sort. Now I don't know whether I should have left everything untouched."
{n}She pauses with the comb above the box.{/n}
"That is foolish, isn't it? Leaving a comb where it was cannot keep a person safe."
"You don't have to decide what to keep tonight."
"No. I do have to decide what to wear. A smaller calamity."
{n}She shuts the lid gently and takes the shawl from the chair.{/n}'''),
    ("blue_room", "supper_later"): ("supper_stairs",
        '''"I remember that table," Kiana says. "Elan and Meral got it wedged on the stairs. Each insisted the other should have measured something."
{n}Edris begins to apologize. Kiana shakes her head.{/n}
"You may tell stories about him. I was there for that one. I offered excellent advice, which neither of them took."
{n}Her fingers stop turning her cup.{/n}
"Ask Meral to write to me. I would like to see the room. I may need to decide the afternoon itself whether I can bear the stairs."
"I'll tell him."
"Tell him to write. Let me answer him."''',
        '''"Ask Meral to write to me," Kiana says. "And please don't arrange a surprise reunion because somebody thinks they have heard something."
{n}Edris's face changes. "I wouldn't."
"I know. I would still like it said. I want to see his room. I want to know whom he has invited before I open the door."
{n}Edris nods, more slowly this time.{/n}
"I'll ask him to write."
"Thank you. Now help Odrin with those plates before he proves his drink can dissolve them."'''),
    ("bakery_stairs", "history"): ("room",
        '''"Meral wrote that I could change my mind at the door. He remembered Elan and the table. So did I."
{n}She looks up the stairs, then tears another piece from the loaf.{/n}
"I don't want every place we went together to become somewhere I cannot enter. We had already begun living apart. I was learning which visits were mine to make. I would like to keep learning."
"Shall we go up?"
"Yes. And if I need to leave, I will say so. You may carry the bread. I keep eating it before we reach anyone."
{n}She passes you the loaf and puts her hand on the rail.{/n}''',
        '''"I asked Meral who would be here. He said Edris, us, and an alarming quantity of paper. No surprises."
{n}She rubs a spot of flour from the note.{/n}
"The table was surprise enough when he moved in. Elan and Meral wedged it between these walls and argued about whose end needed turning. I stood down here offering advice. They were united in refusing it."
"I am tired of pausing at doors because I don't know what somebody thinks would be good for me. Meral understood when I asked. I wish I had asked sooner."
"You can still change your mind."
"I know. Today I would like to go upstairs and find out whether his shelf is as dangerous as everyone says. The things I cannot settle will still be there afterward."
{n}She takes the first step, checking that you follow.{/n}'''),
    ("a_place_afterward", "history"): ("promise",
        '''"Elan and I had separated. Then he died. I keep catching myself trying to arrange those facts so that one will hurt less. They refuse to cooperate."
{n}She lays her hand across the list.{/n}
"I have enjoyed the evenings we made. I don't want to apologize for that each time I miss him. And I don't want you listening for the moment I stop missing him, as though that will finally make us safe."
"I am listening to what you want now."
"Good. I have spent a considerable amount of ink trying to find the words."''',
        '''"I made plans after losing Elan. Now there are things about his fate I cannot honestly settle. I won't mend that by pretending the plans never mattered."
{n}Her finger rests beside the heading Afterward.{/n}
"If reliable news comes, I will face it. If he comes himself, there will be a conversation neither you nor I can rehearse for him. I can't promise the answer to that conversation today."
"What can you promise?"
"To tell you the truth when I know it. To ask for what I want while I am here. That last part has been surprisingly difficult."'''),
    ("yard_evening", "history"): ("after",
        '''"Elan and I separated before he died. I will not make him cruel to justify leaving, and I will not pretend I never left because he cannot answer you."
{n}Orvenna opens her mouth. Kiana continues before she can speak.{/n}
"You have heard enough of my life for an evening at the wagon yard. You may dislike the princess. You may write a different play. My grief is not a better ending for yours."
{n}She collects her pages. Rovan moves to help and stops when she shakes her head.{/n}
"I am going home. Good evening."''',
        '''"I believed my husband dead. I mourned him. Now there are reports I cannot settle. You will have to survive knowing as little about the answer as I do."
{n}Orvenna looks toward you. Kiana gathers her pages.{/n}
"The Commander cannot turn that into a pleasing story for you either. I came to discuss a page somebody had borrowed. I have done that."
"I didn't mean..."
"Then take more care with what you say. Good evening."
{n}She stands without waiting for the apology to find an ending.{/n}'''),
    ("unborrowed_evening", "history"): ("desire",
        '''"I thought of Elan while she was speaking. Then I became angry that I was thinking of him in that yard, as though he had been called there to defend me."
{n}She turns your hand over and runs her thumb along your palm.{/n}
"I want to remember him somewhere better. I want to remember that evening for something better too."
"We can leave it alone tonight."
"Yes. We can. I have spent quite enough time discussing people who aren't in this room."
{n}Her fingers close around yours.{/n}''',
        '''"I am glad I said I didn't know. I hated saying it to her. Both seem likely to remain true."
{n}She watches your joined hands.{/n}
"If there is news, I will tell you. You needn't sit waiting for a messenger every time I invite you here. I invited you because I wanted your company."
"You have it."
"I know. I would like to enjoy it for a while without turning it into another question I cannot answer."
{n}She draws your hand closer.{/n}'''),
}


def letter(id, title, nodes, requires=(), forbids=()):
    return scene("kiana." + id, title, "Kiana", 5, "", nodes,
        Relationship="kiana", Remote=True, ManualOnly=True, Chapters=[5], Areas=[DREZEN],
        requires=("seelah.souls_returned", "kiana.lovers", *requires),
        forbids=("kiana.closed", "inhuman", *forbids), optional=True)


SCENES = [letter("former_grief", "What she still remembers", [
    n("start", "Narrator", '''{n}Kiana's letter begins with a request to read it somewhere quiet.{/n}
"I keep being asked whether I wish I had stayed. I have discovered that a person can ask this with a sympathetic face. That makes it harder to tell them to leave.
"There were reasons I left Elan. You know them. I have been trying to write down something else about him and finding that every pleasant memory looks like evidence someone will use against me. I thought you might help by reading one without deciding what it proves."
{n}There is a second sheet, folded inside the first.{/n}''',
        c('[Read the second sheet.]', "memory"), c('[Put the letter somewhere private until you can read it carefully.]', abort=True)),
    n("memory", "Kiana", '''"Once, before all this, he brought me a ribbon that was entirely the wrong color. I told him it was lovely. It wasn't. He had chosen it himself and was so pleased that I could not bear to say anything else.
"A week later he brought another one. He had remembered exactly what I said. I realized I was going to acquire enough of this dreadful ribbon to clothe a theater unless I spoke honestly.
"I told him. He looked wounded. Then he laughed. After that he would point out the ugliest thing on a stall and ask whether I might like two.
"I had forgotten the second ribbon until yesterday. I remember the difficult conversations so clearly. It seems unfair that a happy one should need so much searching for."
{n}Below the story, she has left enough blank paper for your answer.{/n}''',
        c('[Write about the care it took to remember her first answer, and the kindness in laughing at the second.]', "kindness"),
        c('[Tell her she may keep a happy memory without changing her account of the separation.]', "separation")),
    n("kindness", "Narrator", '''{n}You answer the story she sent. You do not offer a verdict on the marriage. You write that the second ribbon made you smile, and that you can imagine how much harder it must have been to tell the truth after receiving it.{/n}
{n}Her reply arrives on the back of your own sheet.{/n}
"Yes. It was harder. I was cross with him for being so pleased, which was remarkably unjust of me.
"Thank you for laughing. I wanted somebody to laugh at the right part. I tried telling it to an acquaintance and she squeezed my arm before I reached the second ribbon. I spent the rest of the conversation comforting her."
{n}The ink changes a little farther down. She seems to have returned to the page after a pause.{/n}''', c('[Read the rest.]', "request")),
    n("separation", "Narrator", '''{n}You write that the story belongs among her memories whether or not she would choose the marriage again. You ask what happened to the ribbons.{/n}
{n}Her reply is longer than your question.{/n}
"One became a trimming on something that needed to look absurd. I won't tell you what until I can find it. I don't remember what happened to the other. That has been bothering me more than it ought to.
"You were right about the separation. I know I don't have to defend it to you. Sometimes I begin defending it before anyone has asked. That was unfair to your letter. I was glad you asked about the ribbons."
{n}There is more below, written after the ink on the first paragraph had dried.{/n}''', c('[Continue reading.]', "request")),
    n("request", "Kiana", '''"I would like to tell Meral. The story, I mean. He knew Elan. He might remember something I have forgotten. I don't want an evening where everybody is instructed to remember him beautifully. I want someone to say he could be exasperating and then pass the bread.
"Will you help me ask? You needn't attend. I know that could be difficult, and I don't want to make accepting every difficult invitation the price of loving me.
"You may also tell me I am trying to arrange too much at once. I reserve the right to disagree."
{n}You turn the sheet over to find room for an answer.{/n}''',
        c('[Help her compose a plain invitation, leaving attendance for a later conversation.]', "invite"),
        c('[Suggest sending Meral the ribbon story first, without arranging a gathering.]', "story")),
    n("invite", "Narrator", '''{n}You suggest asking whether Meral would like to exchange a few memories of Elan, and letting him choose a day. You leave your own attendance out of the invitation. That is a separate question for the people who would be there.{/n}
{n}Kiana sends back a copy with most of your polite opening crossed out.{/n}
"He knows who I am. He once saw me argue with a door that opened the other way. We can begin with the question.
"I have sent it. I feel rather foolish now, which probably means I shall spend tomorrow checking for an answer. You needn't check for me.
"I would still like to see you soon. Bring a story in which nobody behaved particularly well. I think I have had enough exemplary conduct for one week."
{n}You keep the copy. Meral's answer, and any gathering that follows it, remain ahead of her.{/n}''', c('[Answer that you will bring a story.]', flags=("kiana.former_grief_kept", "kiana.memory_invitation_sent"))),
    n("story", "Narrator", '''{n}You suggest letting the story make its own small journey first. Meral can answer it without finding chairs or wondering whom he ought to invite.{/n}
{n}Kiana copies it onto another sheet. She sends you the draft, with a note beneath it.{/n}
"I have sent him the ribbon story. I nearly added an explanation of why I was sending it. Then I noticed the explanation was longer than the story and removed it.
"This was good advice. I am putting that in writing so that you won't need to ask me to repeat it.
"When we next have an evening, I would like to hear something foolish that happened to you. You cannot possibly have reached your present importance without doing something embarrassing. I promise to be attentive."
{n}For once the last line has no correction crowded beneath it.{/n}''', c('[Promise her an embarrassing story worth hearing.]', flags=("kiana.former_grief_kept", "kiana.memory_story_sent"))),
], requires=("kiana.separated", "seelah.elan_dead"), forbids=("kiana.bereaved",)),
letter("uncertain_reports", "Before another answer", [
    n("start", "Narrator", '''{n}A letter from Kiana contains no greeting. She has written one sentence, crossed it out, and begun again.{/n}
"I need to ask you for something awkward. When people bring me news about Elan, I want to know what they actually know. I don't want the most comforting version first.
"I believed him dead. I grieved. There are now reports I cannot reconcile, and I find that some people would rather have me hopeful than informed. Others seem determined to prepare me for disappointment before telling me anything at all.
"Neither is helping. Could you read what I mean to send them?"
{n}A draft follows.{/n}''', c('[Read her draft.]', "draft"), c('[Set it aside until you can give it your attention.]', abort=True)),
    n("draft", "Kiana", '''"Please tell me whether you saw Elan yourself. If you did, tell me where and when. If somebody told you, tell me who. If you don't remember, say so.
"I am grateful that you thought of me. I would be more grateful if you stopped telling me how I ought to receive the news before giving it to me."
{n}The second paragraph is crossed out, restored, then crossed out again. A small note beside it reads: Too much?{/n}
{n}You have no new witness to offer her. You can answer the question about the letter without inventing one.{/n}''',
        c('[Suggest keeping the factual questions and asking people to send answers in writing.]', "written"),
        c('[Suggest asking one trusted correspondent to collect the answers, if someone agrees to do it.]', "helper")),
    n("written", "Narrator", '''{n}You suggest that written answers would spare her from questioning every visitor at the door. Someone who cannot remember a place or a date can admit that on paper. She could read the replies when she has the strength for them.{/n}
{n}Her answer is brief at first.{/n}
"Yes. In writing. I can put a letter down without worrying that I have offended it.
"I kept the questions. I removed the second paragraph. I have put it here instead, where it can offend you at leisure."
{n}She has copied the offending sentence below with one addition: I am very tired.{/n}
{n}Farther down, she has returned to the page.{/n}''', c('[Continue.]', "fear")),
    n("helper", "Narrator", '''{n}You suggest asking someone she trusts whether they would be willing to collect names, dates and places. You make no appointment on her behalf. Whoever helps would need to agree, and would need to pass on uncertainty as carefully as good news.{/n}
{n}Kiana replies that she has written to Lenna to ask. She has not yet had an answer.{/n}
"I told her she could refuse. Then I spent half a page explaining why she might want to refuse. I had to start again.
"You may laugh. I did, eventually. It is surprisingly difficult to ask for help without trying to perform the help yourself."
{n}There is another paragraph on the reverse.{/n}''', c('[Turn the sheet.]', "fear")),
    n("fear", "Kiana", '''"There is something worse than the letters. I am afraid of what I will feel if he walks through a door. I want him alive. I also know that seeing him would mean having conversations I have spent months believing impossible.
"Then I become ashamed that I can put those two thoughts in the same sentence. I imagine you reading it and wondering whether I have merely been passing time with you. I imagine him hearing it and wishing he had returned to somebody simpler.
"This is where a princess would receive a revelation from a beautiful stranger. I am receiving a headache. Please be an ordinary person when you answer. I don't think I could endure a revelation today."''',
        c('[Tell her that wanting reliable news does not make the life she built afterward dishonest.]', "answer"),
        c('[Admit that uncertainty is hard for you too, and ask her to keep speaking plainly as she learns more.]', "honest")),
    n("answer", "Narrator", '''{n}You write about the evenings you have actually shared. They were real when you lived them. They will still have happened if tomorrow brings news neither of you expected.{/n}
{n}You do not promise that an encounter with Elan would be easy. You ask her to tell you what she learns before deciding on your behalf what you can bear.{/n}
{n}Her reply begins with a complaint about your handwriting and becomes gentler halfway through.{/n}
"I will tell you. I cannot tell you now how every conversation would end. I am glad you didn't ask me to.
"I would like an evening with you that begins with supper. We may discuss the letters if we want to. We may also complain about the supper. I am determined to retain some ambitions within my reach."''', c('[Accept the invitation without asking it to settle the reports.]', "end")),
    n("honest", "Narrator", '''{n}You tell her it is hard to wait for news that could change a life you are already sharing. You also tell her that you would rather hear uncertainty from her than receive assurances she had written to keep you quiet.{/n}
{n}Her reply takes up most of a fresh sheet.{/n}
"Thank you for saying it. I didn't enjoy reading it. Then I read it again and was glad you trusted me with something I might not enjoy.
"I will tell you what I learn. Please tell me when you are frightened, before you become magnificently reasonable and make me guess. I am very bad at guessing reasonable people.
"Would you come to supper? I cannot promise a useful conversation. I can promise there will be food, and that I will be pleased to see you."''', c('[Accept, and promise to speak plainly.]', "end")),
    n("end", "Narrator", '''{n}You send your answer. The reports remain unsettled.{/n}
{n}Kiana's next note is about supper. She has changed her mind about what to serve and asks which of two alternatives you prefer. At the bottom she adds a line in smaller writing.{/n}
"No new answers today. I will tell you when there are. I still want you to come."
{n}You choose a meal and tell her when you can arrive.{/n}''', c('[Send the answer.]', flags=("kiana.uncertain_reports_kept",))),
], requires=("kiana.bereaved",), forbids=("kiana.separated", "seelah.elan_dead"))]


def integrate(payload):
    """Append compatible alternatives without replacing old nodes or answer indices."""
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for (sid, nid), (join, grief, uncertain) in BRIDGES.items():
        book = scenes["kiana." + sid]
        pages = {page["Id"]: page for page in book["Nodes"]}
        if join not in pages:
            raise ValueError("Missing Kiana reconciliation join: " + sid + "/" + join)
        for suffix, text, requires, forbids in (
            ("former_grief", grief, ("kiana.separated", "seelah.elan_dead"), ("kiana.bereaved",)),
            ("uncertain", uncertain, ("kiana.bereaved",), ("kiana.separated", "seelah.elan_dead")),
        ):
            target = nid + "_" + suffix
            if target in pages:
                raise ValueError("Kiana reconciliation applied twice: " + sid + "/" + target)
            pages[nid]["Choices"].append(c('[Listen to what Kiana can say about Elan now.]', target, requires=requires, forbids=forbids))
            book["Nodes"].append(n(target, "Kiana", text, c('[Continue with her.]', join), portrait="Kiana"))
