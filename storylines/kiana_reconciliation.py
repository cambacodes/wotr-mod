"""Authored responses to changed Elan reports; historical romance flags stay intact."""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"

# Each join is after the existing marital-history passage, before the shared action.
BRIDGES = {
    ("guest_table", "history"): ("end",
        '''"We separated. Then he died. You need not choose which of those facts may sit at my table."
{n}Kiana looks at Lenna, then at Odrin.{/n}
"I miss him, Lenna. I also left him. Pass the onions before this becomes a trial."
{n}Lenna puts her spoon down.{/n} "I'm sorry. I was trying to say something kind."
"I know. Tell me something else. Tell me how Odrin came to owe your butcher money."
"That was the dog," {n}Odrin says immediately.{/n}
{n}Kiana reaches for the onions. "Then begin with the dog."{/n}''',
        '''"Every letter gives Elan a different fate. I have not finished reading them. Eat before you write another."
{n}Lenna looks at you as though the Commander might supply a verdict. Kiana catches the movement.{/n}
"No. I asked you both to supper. If there is something certain to tell you, I will tell you. Until then, you may ask whether I want another onion."
"Do you?" {n}Odrin asks.{/n}
"No. That one was terrible. Explain how you can afford to offend the butcher and still eat this well."
{n}He looks relieved to have a question he can answer.{/n}'''),
    ("market_weather", "past"): ("shut",
        '''"I remember our last quarrel far too well. I should have spared him one sharp word. I could not have spared him the truth."
{n}She holds the cloth against her chest, protecting it from the rain.{/n}
"If Lenna mentions Elan, I shall survive it. Her silence has been much harder to endure."
"Would you rather go home?"
"No. I want to return the jar. I can manage a jar. Tomorrow I may manage something more impressive."''',
        '''"People keep beginning with 'if.' If he is alive. If somebody has mistaken another knight for him. If I ought to have waited longer before wanting anything."
{n}A drop strikes the cloth. She brushes it away with unnecessary force.{/n}
"Give me a witness, not a sermon about what I should have done while I thought him dead."
"What would help today?"
"Returning this jar. Asking Lenna why she didn't answer. Something somebody in this street can actually tell me."'''),
    ("blue_room", "box"): ("pin",
        '''"I kept things when we separated. Now he is dead, I keep being tempted to treat every object as though I must either bury it or worship it."
{n}She turns the cracked comb in her hand.{/n}
"Some of it is simply mine. He knew that too. He would have been very impatient with this comb."
{n}A laugh escapes her, and she puts it back.{/n}
"The picture stays where it is. Look at me instead, before I lose my nerve about this shawl."
{n}She closes the box and draws the blue cloth toward her.{/n}''',
        '''"I started sorting things when I believed there would be no more of his things to sort. Now I don't know whether I should have left everything untouched."
{n}She pauses with the comb above the box.{/n}
"That is foolish, isn't it? Leaving a comb where it was cannot keep a person safe."
"The comb will keep until after supper."
"No. I do have to decide what to wear. A smaller calamity."
{n}She shuts the lid gently and takes the shawl from the chair.{/n}'''),
    ("blue_room", "supper_later"): ("supper_stairs",
        '''"I remember that table," {n}Kiana says.{/n} "Elan and Meral got it wedged on the stairs. Each insisted the other should have measured something."
{n}Edrava begins to apologize. Kiana shakes her head.{/n}
"Tell that one. I supplied excellent advice and they ignored every word."
{n}Her fingers stop turning her cup.{/n}
"Have Meral write. I want to see whether that table has recovered from the journey."
"I'll tell him."
"Tell him to write. Let me answer him."''',
        '''"Ask Meral to write to me," {n}Kiana says.{/n} "And please don't arrange a surprise reunion because somebody thinks they have heard something."
{n}Edrava's face changes.{/n} "I wouldn't."
"Good. Send me the guest list. I refuse to be surprised halfway up those stairs."
{n}Edrava nods, more slowly this time.{/n}
"I'll ask him to write."
"Thank you. Now help Odrin with those plates before he proves his drink can dissolve them."'''),
    ("bakery_stairs", "history"): ("room",
        '''"Meral wrote that I could change my mind at the door. He remembered Elan and the table. So did I."
{n}She looks up the stairs, then tears another piece from the loaf.{/n}
"I refuse to surrender every room Elan ever entered. Meral's shelf may yet frighten me out of this one."
"Shall we go up?"
"Up we go. Take the bread before I eat our entire contribution."
{n}She passes you the loaf and puts her hand on the rail.{/n}''',
        '''"I asked Meral who would be here. He said Edrava, us, and an alarming quantity of paper. No surprises."
{n}She rubs a spot of flour from the note.{/n}
"The table was surprise enough when he moved in. Elan and Meral wedged it between these walls and argued about whose end needed turning. I stood down here offering advice. They were united in refusing it."
"Meral has sent the names. I can stop imagining a surprise behind every door."
"Shall I guard the bread or the stairs?"
"The shelf today. The impossible letters tomorrow. Come up before I lose my nerve."
{n}She takes the first step, checking that you follow.{/n}'''),
    ("a_place_afterward", "history"): ("promise",
        '''"We separated, and then he died. I cannot quarrel with the second fact as I did with him."
{n}She lays her hand across the list.{/n}
"I miss Elan. I want you here. Stop looking for the moment one of those facts will defeat the other."
"Then ask me for the evening you want."
"Good. I have spent a considerable amount of ink trying to find the words."''',
        '''"I made plans when I thought him dead. I will not throw them out because somebody has brought another rumour."
{n}Her finger rests beside the heading Afterward.{/n}
"If Elan comes, I shall speak to him. You will have to wait for the next scene; I haven't written it yet."
"What can you promise?"
"The truth, when I have it. Tonight, supper and my atrocious company."'''),
    ("yard_evening", "history"): ("after",
        '''"Elan and I separated before he died. I will not make him cruel to justify leaving, and I will not pretend I never left because he cannot answer you."
{n}Orvenna opens her mouth. Kiana continues before she can speak.{/n}
"You have heard enough. Criticize the princess if you like; she has better insults prepared than I do."
{n}She collects her pages. Rovan moves to help and stops when she shakes her head.{/n}
"I am going home. Good evening."''',
        '''"I believed my husband dead. I mourned him. Now there are reports I cannot settle. You will have to survive knowing as little about the answer as I do."
{n}Orvenna looks toward you. Kiana gathers her pages.{/n}
"The Commander cannot turn that into a pleasing story for you either. I came to discuss a page somebody had borrowed. I have done that."
"I didn't mean..."
"Then take more care with what you say. Good evening."
{n}She stands without waiting for the apology to find an ending.{/n}'''),
    ("unborrowed_evening", "history"): ("desire",
        '''"She dragged Elan into that filthy yard. I wanted to slap her for it."
{n}She turns your hand over and runs her thumb along your palm.{/n}
"Next time I remember Elan, I want wine and a better view. Next time I visit that yard, I may bring a whip."
"We can leave it alone tonight."
"Yes. We can. I have spent quite enough time discussing people who aren't in this room."
{n}Her fingers close around yours.{/n}''',
        '''"I told her I didn't know. I hated giving her even that much."
{n}She watches your joined hands.{/n}
"No messenger tonight. I wanted you, and here you are. Come closer."
"You have it."
"Then let me enjoy you before another impossible letter ruins my temper."
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
"I found a ridiculous story about Elan in my head. Read it before the solemn people smother it with sympathy."
{n}There is a second sheet, folded inside the first.{/n}''',
        c('[Read the second sheet.]', "memory"), c('[Put the letter somewhere private until you can read it carefully.]', abort=True)),
    n("memory", "Kiana", '''"Once, before all this, he brought me a ribbon that was entirely the wrong color. I told him it was lovely. It wasn't. He had chosen it himself and was so pleased that I could not bear to say anything else.
"A week later he brought another one. He had remembered exactly what I said. I realized I was going to acquire enough of this dreadful ribbon to clothe a theater unless I spoke honestly.
"I told him. He looked wounded. Then he laughed. After that he would point out the ugliest thing on a stall and ask whether I might like two.
"I had forgotten the second ribbon until yesterday. I remember the difficult conversations so clearly. It seems unfair that a happy one should need so much searching for."
{n}Below the story, she has left enough blank paper for your answer.{/n}''',
        c('[Write that the second ribbon made you laugh.]', "kindness"),
        c('[Ask what became of the ribbons.]', "separation")),
    n("kindness", "Narrator", '''{n}You write that Elan should have bought the ugliest ribbon in the city and dared her to wear it.{/n}
{n}Her reply arrives on the back of your own sheet.{/n}
"He would have done it, too. Then I would have had to wear the damned thing to supper.
"Thank you for laughing. I wanted somebody to laugh at the right part. I tried telling it to an acquaintance and she squeezed my arm before I reached the second ribbon. I spent the rest of the conversation comforting her."
{n}The ink changes a little farther down. She seems to have returned to the page after a pause.{/n}''', c('[Read the rest.]', "request")),
    n("separation", "Narrator", '''{n}You ask whether the ribbons ever appeared in the vampire princess's wardrobe.{/n}
{n}Her reply is longer than your question.{/n}
"One became a trimming on something that needed to look absurd. I won't tell you what until I can find it. I don't remember what happened to the other. That has been bothering me more than it ought to.
"I began defending the separation again. You asked about a ribbon. How dreadfully solemn I have become."
{n}There is more below, written after the ink on the first paragraph had dried.{/n}''', c('[Continue reading.]', "request")),
    n("request", "Kiana", '''"Meral knew Elan. I want his worst story over supper, followed by his best one. No solemn toasts; they spoil the bread."
"Help me invite Meral. Come if you can bear our stories; if not, I shall save the most embarrassing one for you."
"If I try to invite half of Drezen, hide the rest of the paper."
{n}You turn the sheet over to find room for an answer.{/n}''',
        c('[Help her invite Meral to supper.]', "invite"),
        c('[Suggest sending Meral the ribbon story first, without arranging a gathering.]', "story")),
    n("invite", "Narrator", '''{n}You send a draft invitation to Kiana. She returns a copy with the ceremonious opening crossed out and Meral's name at the top.{/n}
"He knows who I am. He once saw me argue with a door that opened the other way. We can begin with the question.
"I have sent it. I feel rather foolish now, which probably means I shall spend tomorrow checking for an answer. You needn't check for me.
"I would still like to see you soon. Bring a story in which nobody behaved particularly well. I think I have had enough exemplary conduct for one week."
{n}You keep the copy. Meral's answer, and any gathering that follows it, remain ahead of her.{/n}''', c('[Answer that you will bring a story.]', flags=("kiana.former_grief_kept", "kiana.memory_invitation_sent"))),
    n("story", "Narrator", '''{n}You suggest sending Meral the ribbon story. Kiana sends you a copy of her letter to him, with a note beneath it.{/n}
"I have sent him the ribbon story. I nearly added an explanation of why I was sending it. Then I noticed the explanation was longer than the story and removed it.
"This was good advice. I am putting that in writing so that you won't need to ask me to repeat it.
"When we next have an evening, I would like to hear something foolish that happened to you. You cannot possibly have reached your present importance without doing something embarrassing. I promise to be attentive."
{n}For once the last line has no correction crowded beneath it.{/n}''', c('[Promise her an embarrassing story worth hearing.]', flags=("kiana.former_grief_kept", "kiana.memory_story_sent"))),
], requires=("kiana.separated", "seelah.elan_dead"), forbids=("kiana.bereaved",)),
letter("uncertain_reports", "Before another answer", [
    n("start", "Narrator", '''{n}A letter from Kiana contains no greeting. She has written one sentence, crossed it out, and begun again.{/n}
"Someone claims to have seen Elan alive. I want a name, a place and a date before anybody offers me hope."
"I mourned him. Now every caller brings a different tale, and nobody will say where they heard it."
"Neither is helping. Could you read what I mean to send them?"
{n}A draft follows.{/n}''', c('[Read her draft.]', "draft"), c('[Set it aside until you can give it your attention.]', abort=True)),
    n("draft", "Kiana", '''"Please tell me whether you saw Elan yourself. If you did, tell me where and when. If somebody told you, tell me who. If you don't remember, say so.
"I am grateful that you thought of me. I would be more grateful if you stopped telling me how I ought to receive the news before giving it to me."
{n}The second paragraph is crossed out, restored, then crossed out again. A small note beside it reads: Too much?{/n}
{n}The crossed-out paragraph has nearly worn through the paper.{/n}''',
        c('[Suggest keeping the factual questions and asking people to send answers in writing.]', "written"),
        c('[Suggest that Lenna collect the witnesses\' names.]', "helper")),
    n("written", "Narrator", '''{n}You suggest written replies; Kiana underlines the request for names and dates twice.{/n}
{n}Her answer is brief at first.{/n}
"Yes. In writing. I can put a letter down without worrying that I have offended it.
"I kept the questions. I removed the second paragraph. I have put it here instead, where it can offend you at leisure."
{n}She has copied the offending sentence below with one addition: I am very tired.{/n}
{n}Farther down, she has returned to the page.{/n}''', c('[Continue.]', "fear")),
    n("helper", "Narrator", '''{n}You suggest Lenna; Kiana writes her name at the top of a fresh sheet.{/n}
{n}Kiana replies that she has written to Lenna to ask. She has not yet had an answer.{/n}
"I wrote Lenna a splendid speech instead of a question. I have torn it up. She shall have the question."
"Laugh. I did. Lenna will probably send me a bill for the paper I wasted."
{n}There is another paragraph on the reverse.{/n}''', c('[Turn the sheet.]', "fear")),
    n("fear", "Kiana", '''"If Elan walks through that door, I may kiss him or throw a cup. I want him alive. The cup can survive the suspense."
"I keep imagining his face, then yours, until I could scream. What an audience I have invented for myself."
"This is where a princess would receive a revelation from a beautiful stranger. I am receiving a headache. Please be an ordinary person when you answer. I don't think I could endure a revelation today."''',
        c('[Tell her you remember every evening you shared.]', "answer"),
        c('[Tell her you are afraid of the news too.]', "honest")),
    n("answer", "Narrator", '''{n}You remind her of the onions, the paper moon and the line she laughed too hard to finish.{/n}
{n}You ask her to send you the next witness's name as soon as she has it.{/n}
{n}Her reply begins with a complaint about your handwriting and becomes gentler halfway through.{/n}
"You shall have the next letter. If it contradicts the last, I may set fire to both."
"Come for supper. If the letters bore us, we can curse the soup instead."''', c('[Accept her invitation to supper.]', "end")),
    n("honest", "Narrator", '''{n}You write that you dread the next messenger too, and ask her to send whatever news comes.{/n}
{n}Her reply takes up most of a fresh sheet.{/n}
"That was a dreadful sentence to read. I am glad you wrote it; I had begun suspecting you were made of marble."
"You shall have the news. If you are frightened, curse about it. I cannot guess what lurks behind a general's noble expression."
"Would you come to supper? I cannot promise a useful conversation. I can promise there will be food, and that I will be pleased to see you."''', c('[Accept her invitation.]', "end")),
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
