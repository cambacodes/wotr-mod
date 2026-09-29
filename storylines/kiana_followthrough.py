"""Authored Kiana social and writing continuation; native history is read only."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, after, delay=48):
    for page in nodes:
        page["Portrait"] = "Kiana" if page["Speaker"] == "Kiana" else ""
    SCENES.append(scene(
        "kiana." + id, title, "Kiana", 5, "", nodes,
        Relationship="kiana", Remote=True, Chapters=[5], Areas=[DREZEN],
        requires=("seelah.souls_returned", "kiana.lovers", "kiana.consequences_ready", after),
        forbids=("kiana.closed", "kiana.farewell", "inhuman"), delay=delay, optional=True,
        ForbidOverrides={"kiana.farewell": "kiana.catchup_requested"}))


s("bakery_stairs", "The room above the bread", [
    n("start", "Kiana", '''{n}Kiana waits at the foot of the bakery stairs with a folded note and a narrow loaf. The loaf has a bite missing from one end.{/n}
"Meral said to bring nothing. I have disobeyed him twice. Once by buying this, and once by beginning it without him."
{n}She offers you the bitten end. Above the stairwell a window stands open, letting out a warm smell of paint.{/n}
"I wrote to ask what he had arranged. He wrote back on the corner of a bill. Edris was quite right about the room, though she left out the part about his furniture. He owns three chairs. One is currently holding up a shelf."
{n}Kiana glances at the note.{/n}
"We are going this afternoon. Supper would involve sitting, and he has had enough trouble with that table already."''',
      c('"Lead the way. I will defend the bread."', "history"),
      c('[Explain that you cannot keep the visit and ask to arrange another afternoon.]', abort=True)),
    n("history", "Narrator", '''{n}She folds the note along its existing crease. The paper has been opened often enough to soften at the corners.{/n}''',
      c('[Ask how she arranged the visit.]', "separated", requires=("kiana.separated",), forbids=("kiana.bereaved", "seelah.elan_dead")),
      c('[Wait beside her before climbing.]', "widow", requires=("kiana.bereaved", "seelah.elan_dead"), forbids=("kiana.separated",))),
    n("separated", "Kiana", '''"I asked for a separate visit. Meral has invited Elan as well. He hasn't told me whether Elan has answered, and I haven't asked him to find out for my benefit."
{n}She tucks the note into her purse.{/n}
"Perhaps later we will manage a table together. Today I wanted to come up these stairs without wondering whether every creak meant he was behind me."
"Does Meral understand?"
"He said afternoons were convenient. He also asked whether I remembered where the shelf supports had been packed. I expect he understood as much as he needed to."
{n}Her thumb rubs at a spot of flour on the loaf.{/n}''',
      c('"You have made the arrangement you wanted."', "waited", requires=("kiana.waited",), forbids=("kiana.affair",)),
      c('"I know my being here makes some of this harder."', "affair", requires=("kiana.affair",))),
    n("waited", "Kiana", '''"Yes. It would be convenient if doing things carefully made them stop hurting. I continue to find the world badly organized in that respect."
{n}She takes your free hand.{/n}
"I am glad we waited when I asked you to. I don't want to keep making you stand on the stair because I can't promise that nobody will feel anything unpleasant at the top. Come on. He will have eaten his own bread by now."''', c('[Climb with her.]', "room")),
    n("affair", "Kiana", '''"It does. So does my wanting you here. I wrote that to Meral too, although I used fewer words and did not explain the kiss. He is allowed to invite me without receiving my entire history."
{n}She looks directly at you.{/n}
"I am not going to improve that history by telling him Elan drove me away. If the subject comes up, I will answer for myself. For now I would like you to meet an old friend who has a dreadful shelf."
"I can do that."
"Good. It may be the more dangerous encounter."''', c('[Follow her up the stairs.]', "room")),
    n("widow", "Kiana", '''"I remember the table being stuck here. I wasn't helping. I was standing at the bottom offering advice neither of them wanted."
{n}She looks up the narrow flight.{/n}
"I kept telling Elan to turn it. He asked whether I thought he was enjoying holding it in one position. I was cross with him until it was upstairs. Then he made me sit at it before anyone else."
{n}A laugh escapes her, small and surprised.{/n}
"Meral asked whether I would prefer somewhere else. I said no. I want to find out what the room looks like with the table in it. I've spent quite enough time remembering the stairs."
{n}She takes a bite from the loaf, chews, and holds out her hand.{/n}
"Come with me."''', c('[Take her hand and climb.]', "room")),
    n("room", "Narrator", '''{n}Meral is an angular man with paint on his sleeve and spectacles that slip whenever he looks down. He opens the door before Kiana can knock twice.{/n}
"You found it. Mind the shelf."
"Everyone has been warning me about furniture lately," Kiana says. "I am beginning to take it personally."
{n}The room is smaller than the table's difficult ascent had suggested. Meral has painted one wall cream; the next still carries a square of darker color where somebody's cupboard stood. Edris sits on the bed with a bundle of folded paper.{/n}
"I brought enough for everybody," Meral says, noticing the loaf.
"You may keep your own half-eaten contribution," Kiana tells him. "This is ours."
{n}He laughs and moves a stool away from the shelf. Kiana tests it before sitting, then pats the place beside her on the window ledge.{/n}''', c('[Divide the bread while Edris unfolds the papers.]', "offer")),
    n("offer", "Kiana", '''{n}"There," Edris says. "Names of people who asked about your princess. I didn't invite them. I remembered what you said."{/n}
"How many people did you tell?"
"Enough to get these names."
{n}Kiana counts, loses her place, and starts again.{/n}
"They won't all fit here."
"The baker lets a room at the back on afternoons when she isn't storing sacks in it," Meral says. "I asked the price. Then I thought I had better ask you."
"In that order?"
"Prices are easier to ask."
{n}Kiana takes the list from Edris. Her smile has become intent.{/n}
"I could read part of it. Properly this time. With the end written down before I arrive."
"People could put something toward the room," Edris says.
"People could also dislike it and tell their friends. I should like to be paid before that stage of the arrangement."
{n}She is joking, but her finger stays on the list.{/n}''',
      c('"Read it to people who have not heard it. Find out what survives a roomful of strangers."', "audience", flags=("kiana.follow_audience",)),
      c('"Ask for a smaller reading first. You wanted it finished, not merely announced."', "workshop", flags=("kiana.follow_workshop",))),
    n("audience", "Kiana", '''"Strangers. You make them sound like weather."
{n}She reads two names aloud and gives up on the third.{/n}
"I want to try. Meral, ask about one afternoon. Edris, find out who actually wants to hear a play and who was merely being polite while you described it. Those are different lists."
{n}Edris looks offended, then laughs.{/n}
"I shall make them choose."
"Let them choose a chair, not swear an oath. And tell them they can laugh. I don't want a room full of people sitting as if a commander has ordered them to enjoy themselves."
{n}Kiana folds the list into her own purse. She has already begun arranging the first line under her breath.{/n}''', c('[Stay while they work out a possible afternoon.]', "leave")),
    n("workshop", "Kiana", '''"I did. I also liked seeing all the names."
{n}She smooths the list, reluctant to put it down.{/n}
"Six people, then. People who will say something afterward. Edris, you can find six who won't all be afraid of hurting my feelings."
"I can find twelve."
"Your efficiency is alarming. Six. We can use this room if Meral lends us the furniture he hasn't built into the walls."
{n}Meral counts the chairs on his fingers and volunteers to borrow more. Kiana gives Edris the list back, keeping a blank sheet for herself.{/n}
"I can write the second invitation after I have survived the first. There. A plan involving less courage and more work. I expect I shall complain about both."''', c('[Help Meral measure where the borrowed chairs can go.]', "leave")),
    n("leave", "Kiana", '''{n}By the time you leave, the bread is gone and Meral has found the missing shelf supports inside his own coat. Kiana carries a sheet covered with dates, cancellations and one drawing of an audience member with an enormous ear.{/n}
"I drew that while they were discussing chairs. It is my ideal listener. Very attentive. Incapable of speaking."
{n}Outside, she slides her arm through yours.{/n}
"Come and hear the ending before anybody else does. I shall want an honest opinion. I am telling you now so that I cannot pretend otherwise when you give it."''', c('[Arrange an afternoon for the unfinished pages.]', flags=("kiana.bakery_visit_kept",))),
], after="kiana.consequences_ready")


s("last_page", "The sentence she keeps", [
    n("start", "Kiana", '''{n}Kiana's room is full of loose pages. The blue shawl hangs over the back of a chair; its brass pin holds three sheets together. She takes it out when she sees you.{/n}
"It has become literary equipment. I hope that doesn't disappoint you."
{n}She has set two cups well away from the writing. A third cup contains strips of crossed-out paper.{/n}
"Those are the dead. Do not mourn them. Most deserved it."
{n}Kiana offers you the cleanest copy.{/n}
"Start here. I have written something I like very much. That is usually when I need somebody to look at it."''',
      c('[Take the pages and begin reading.]', "earlier"),
      c('[Ask for another afternoon when you can read attentively.]', abort=True)),
    n("earlier", "Narrator", '''{n}The princess has acquired an entire household since your first evening in the borrowed room. The servants have names, complaints and reasons to leave before she wants them to.{/n}''',
      c('"You kept the moon."', "moon", requires=("kiana.moon",)),
      c('"The guest seems to have brought a great many problems."', "guest", requires=("kiana.guest",))),
    n("moon", "Kiana", '''"I had to. You gave it to me, and I have spent too long finding places to put it."
{n}She leans over the page and points to a line.{/n}
"There. The cook has discovered that the princess stole it because she wanted someone to come looking for her. The cook thinks a letter would have been cheaper."
"Would it?"
"Considerably. But it would have deprived me of an excellent argument about tides."
{n}She turns to the last sheet.{/n}
"Now she has to send it back. I haven't decided whether she admits why she took it first."''', c('[Read the confession she has written.]', "read")),
    n("guest", "Kiana", '''"I invited one person into the castle and found I needed to know what everybody else did while the door was locked. The cook had opinions."
{n}She points to a passage near the end.{/n}
"The princess tells the guest she sent the servants away because she wanted to be alone with him. Then the cook comes back for her wages. It makes the speech rather less magnificent."
"Is the guest staying?"
"Tonight. I won't give the princess the rest of his life because she has managed one good invitation. But she has prepared a speech anyway. She has my worst habits."''', c('[Read the speech.]', "read")),
    n("read", "Narrator", '''{n}The speech begins as a declaration. By its fourth sentence, the princess is arguing with herself. She admits that she rehearsed the welcome, complains that the guest arrived before she had finished, and finally asks whether he would like to sit down.{/n}
{n}Kiana watches you reach the end. She tries to examine her own cup without looking as though she is waiting.{/n}
"Well?"
"I like the last line."
"That is a suspiciously small part of the page."
{n}You read the middle aloud. It repeats the princess's uncertainty in three different images. Kiana interrupts at the second, defending the third before you have reached it.{/n}
"That one is funny."
"You have already made the joke."
"Not with a staircase."
{n}She takes the page, reads it herself, and frowns.{/n}''',
      c('"Keep the long speech. Let us make the pauses work, so she can hear how foolish she sounds."', "keep", flags=("kiana.follow_long_speech",)),
      c('"Keep the question at the end. Cut the explanations and let the guest answer it."', "cut", flags=("kiana.follow_short_speech",))),
    n("keep", "Kiana", '''"Yes. The third image needs somewhere to land. I have been running at it as if I were afraid you would stop me."
{n}She stands, puts the page on the mantel and begins again. This time she stops after the first grand claim. Her hand remains extended toward an invisible guest until she grows visibly tired of holding it there.{/n}
"You may sit down," she says at last, with the exhausted dignity of a woman defeated by her own hospitality.
{n}You laugh. Kiana drops the pose.{/n}
"That. I want that. It takes longer, but there is a person inside it now."
{n}She marks two pauses, then hesitates over the third.{/n}
"I am keeping it. If they get bored, you may remind me I chose to be elaborate. Once. After I have eaten."''', c('[Read the guest while she tries it again.]', "your_part")),
    n("cut", "Kiana", '''{n}Kiana draws one line through the middle paragraph. She stops before the staircase.{/n}
"I shall keep this somewhere. It has done nothing wrong except be in the wrong place."
{n}She copies the sentence onto a scrap and puts it beneath the pin. Then she reads the shortened speech.{/n}
"Would you like to sit down?"
{n}The plain question arrives before you expect it. She waits, suddenly looking more exposed than she did with an entire page between you.{/n}
"I see. Now the guest has to answer instead of listening to me explain why he ought to."
"What does he say?"
"Something inadequate, I hope. I refuse to give him all the good lines merely because I have surrendered some of mine."''', c('[Try an answer that surprises her.]', "your_part")),
    n("your_part", "Kiana", '''{n}You try three replies. The first is solemn, the second too clever. The third is a request to move the chair away from a draft. Kiana laughs and writes it down.{/n}
"Keep that. I can play a woman who has forgotten the window."
{n}She looks toward the real window and gets up to close it.{/n}
"You could read the guest. If you wanted. I have another reader in mind if you don't. Lenna wants to be the cook. She says it is the only sensible person I have written."
{n}Kiana puts the revised pages beside you.{/n}''',
      c('"Give me the guest. I have had some practice being invited by you."', "read_guest", flags=("kiana.follow_guest_role",)),
      c('"Let me listen from the room. I want to hear what happens when someone else answers you."', "listen", flags=("kiana.follow_listens",))),
    n("read_guest", "Kiana", '''"Some practice? You have been a very time-consuming research project."
{n}She hands you the second copy, keeping her fingers on its edge until you look up.{/n}
"Your part is on these pages. The rest of you is still expected afterward. I don't intend to spend the whole evening introducing you as an exceptionally convincing piece of furniture."
"The chair has an important role."
"It gets the princess out of the speech. I am deeply grateful to it."
{n}She lets you have the pages, then bends to kiss your cheek before returning to her own copy.{/n}''', c('[Read until you can find the pauses together.]', "end")),
    n("listen", "Kiana", '''"Then Edris can read the guest. She will enjoy asking Lenna where supper is. They have wanted to give each other instructions for years."
{n}Kiana settles beside you on the edge of the bed, the pages between your knees.{/n}
"I do want you where I can see you. Not in the front if you dislike it. Somewhere I can look after a dreadful line and know one person remembers it used to be worse."
"I can find somewhere."
"Good. I shall try not to look at you after every line. That would be an alarming performance for everybody else."''', c('[Read her the revised ending once more.]', "end")),
    n("end", "Narrator", '''{n}When the room begins to darken, Kiana gathers the discarded strips, checking each against the pages she intends to keep. She tips the unwanted paper into a small box beneath the table.{/n}
"For lighting the fire. There. They may yet contribute warmth."
{n}She sets the brass pin on top of the work she is keeping. You help straighten the bedcover where the papers have creased it. Kiana catches your hand before you can finish.{/n}
"Stay a little. I have heard enough imaginary people for one afternoon. Tell me something badly, without revising it."
{n}You tell her about a small irritation from your day. She interrupts twice to ask questions, then laughs at the part you had not meant to be funny.{/n}''', c('[Stay until the cups are empty.]', flags=("kiana.last_page_kept",))),
], after="kiana.bakery_visit_kept")


s("first_readers", "People who have not heard it", [
    n("start", "Narrator", '''{n}Kiana has arrived before you. Her pages are tied with a green ribbon, and she is carrying the empty cup she brought to keep her place in the reading. She has forgotten to fill it.{/n}
"Don't ask whether I am nervous. I have answered that question three times. Nobody has offered to become nervous for me."
{n}Lenna comes through the doorway behind her with a folded apron.{/n}
"Do I need this?"
"You are reading the cook. You may have whatever dignity the apron affords you."
"It has a pocket. That is more useful."
{n}Kiana laughs, then holds the cup out to you.{/n}
"Water. Before I begin delivering a tragedy in a voice like a rusty hinge."''',
      c('[Fill her cup and help her take her place.]', "setting"),
      c('[Explain that you cannot stay for the reading, and arrange to try another date.]', abort=True)),
    n("setting", "Narrator", '''{n}Meral has borrowed chairs from three households. He tests each one himself, then asks the guests to avoid rocking them. Someone immediately asks which one he means.{/n}''',
      c('[Find a place in the larger room.]', "public_room", requires=("kiana.follow_audience",)),
      c('[Join the small circle upstairs.]', "small_room", requires=("kiana.follow_workshop",))),
    n("public_room", "Kiana", '''{n}The baker's back room smells of flour and damp stone. There are fourteen people, two more than the chairs will accommodate. Meral gives up his seat and finds a crate for himself.{/n}
"I shall begin," Kiana says, before anyone can offer another chair. "There is a princess. She is not a wise woman. This is unfortunate for her household and convenient for the story."
{n}Someone laughs near the back. Kiana's grip on the pages loosens.{/n}
"If you cannot hear, tell me. If you disagree with the princess, wait. Somebody else probably does too."
{n}Edris closes the door, keeping the jar for room contributions on a stool beside it. Kiana watches one late arrival put in a coin, then makes herself look away.{/n}''', c('[Listen as she begins.]', "entrance")),
    n("small_room", "Kiana", '''{n}Six listeners fit into Meral's room, though the one near the shelf has to keep a foot against its supporting chair. Kiana looks around the circle and recognizes only two faces.{/n}
"Edris has found people with opinions. I asked her to. I intend to remember that when you give them."
{n}An older woman near the window lifts a folded sheet.{/n}
"I brought something to write on."
"How threatening. I shall begin before you improve your equipment."
{n}Kiana stands where the light reaches her page. She introduces the princess, pauses at the first laugh, and turns toward Lenna with a relief she cannot quite conceal.{/n}''', c('[Follow the opening argument.]', "entrance")),
    n("entrance", "Narrator", '''{n}Kiana has left herself a moment before the first exchange. She sets down the cup and raises her eyes from the page.{/n}''',
      c('[Watch for the quiet entrance you rehearsed.]', "quiet_entrance", requires=("kiana.quiet_entrance",)),
      c('[Watch for the comic entrance you rehearsed.]', "comic_entrance", requires=("kiana.comic_entrance",)),
      c('[Listen as the princess addresses her household.]', "role", forbids=("kiana.quiet_entrance", "kiana.comic_entrance"))),
    n("quiet_entrance", "Narrator", '''{n}She speaks the threat quietly, as she did when you rehearsed in the storeroom. A listener leans forward. Kiana holds the silence until Lenna breaks it with the cook's perfectly ordinary question about supper. The grand danger collapses into domestic inconvenience, and Kiana lets the laugh come before she answers.{/n}''', c('[Follow the cook into the argument.]', "role")),
    n("comic_entrance", "Narrator", '''{n}Kiana lets her sleeve catch on the chair beside her. She frees it without admitting that anything has happened, exactly as she practiced in the borrowed castle. The first laugh comes before the princess has finished her threat. Kiana waits for it this time, preserving her dignity while Lenna prepares to dispose of the rest.{/n}''', c('[Follow the cook into the argument.]', "role")),
    n("role", "Narrator", '''{n}Lenna reads the cook as a woman who has endured the princess for too many years to be impressed by a dramatic entrance. Her first question concerns the missing supper. Kiana gives her a lofty answer about matters of the heart.{/n}
"Will they be eating?" Lenna asks.
{n}The laugh is larger than Kiana expected. She waits for it, smiling into the edge of her page.{/n}''',
      c('[Read the guest, arriving in the middle of their argument.]', "guest_role", requires=("kiana.follow_guest_role",)),
      c('[Listen as Edris brings the guest into the argument.]', "audience_role", requires=("kiana.follow_listens",))),
    n("guest_role", "Narrator", '''{n}Your first line meets the end of another laugh and disappears. Kiana turns toward you as if the princess has failed to notice her own guest.{/n}
"You will have to announce yourself again. My household has become unruly."
{n}You repeat it more loudly. Lenna tells the guest where to put a coat, and the reading finds its pace. Kiana's glance brushes yours when you move the imaginary chair. You have learned to recognize the moment before she tries not to laugh.{/n}''', c('[Leave room for her final speech.]', "speech")),
    n("audience_role", "Narrator", '''{n}Edris enters the story in a voice much lower than her own. Lenna looks at her over the apron, loses her place, and has to ask Kiana where they are.{/n}
"Still in the castle. Though I understand the desire to escape."
{n}The room laughs with them. Edris tries her ordinary voice. It works better. From your seat you can see Kiana listening to an answer she knows by heart and finding something new in the way it is spoken.{/n}''', c('[Listen as the princess turns toward her guest.]', "speech")),
    n("speech", "Narrator", '''{n}The cook goes to fetch supper. At last the princess is alone with the person she invited. Kiana lowers the page enough to let the room see her face.{/n}''',
      c('[Follow the pauses in the longer speech.]', "long", requires=("kiana.follow_long_speech",)),
      c('[Hear the shortened question and its answer.]', "short", requires=("kiana.follow_short_speech",))),
    n("long", "Narrator", '''{n}The first pause earns a laugh. The second earns a smaller one. At the third, a chair scrapes while somebody shifts an aching leg. Kiana's eyes flick toward the sound. She reaches for the next line too quickly, swallows the end of it, and stops.{/n}
"The princess is considering whether she has made a mistake," she says. "Give her a moment. She is unused to the activity."
{n}The room laughs again. Kiana takes a breath and returns to the question. This time she lets it be plain. The guest asks to move the chair away from the draft. Lenna, waiting with the imaginary supper, snorts before she is meant to enter.{/n}
{n}Kiana gets through the final page without another rush, but the third pause stays marked beneath her thumb.{/n}''', c('[Stay through the final exchange.]', "response")),
    n("short", "Narrator", '''{n}Kiana reaches the question sooner than some listeners expect. A man near the door is still smiling at the cook when the princess asks her guest to sit down. The reply about the draft receives a surprised laugh.{/n}
{n}Then Lenna returns with supper, and the princess has to move her own chair to make room. The story ends on that small indignity. Kiana lowers the page and waits half a breath before realizing there is nothing more to say.{/n}
{n}The applause begins unevenly, then grows. She bows too soon, bumps Lenna's elbow, and laughs through the apology. The ending has worked. It has also left her with the uncomfortable feeling of having reached the bottom of a stair before she expected to.{/n}''', c('[Stay while the readers put down their pages.]', "response")),
    n("response", "Kiana", '''{n}Questions arrive before she has finished the water. One listener wants to know why the cook stayed so long. Another likes the princess better when she is being unreasonable. Kiana begins to explain, then notices that the two have started discussing it with each other.{/n}
"I appear to have become optional."
{n}Lenna offers her the cup. Kiana takes a longer drink.{/n}''',
      c('"Let them argue. You wanted readers."', "listen_response", flags=("kiana.follow_heard_readers",)),
      c('"Ask which part made them think that. There may be something you can use."', "ask_response", flags=("kiana.follow_asked_readers",))),
    n("listen_response", "Kiana", '''"I wanted agreeable readers. I may have failed to specify."
{n}She sits on the edge of a chair and lets the discussion continue. The woman with the folded paper says the princess is afraid of looking foolish, which is why she does so much of it. Kiana looks down at her own script.{/n}
"I hadn't put it quite like that."
"Did you mean it?"
"I think I did. I should like to take the credit after the fact."
{n}She writes the woman's phrase on the back of her page, asking how to spell her name before she does.{/n}''', c('[Help her collect the scattered pages.]', "cost")),
    n("ask_response", "Kiana", '''"Which part?" she asks.
{n}The man who liked the unreasonable princess points to the cook's entrance. He enjoyed the way Kiana tried to keep being grand while somebody was asking about dinner. Kiana makes him repeat the particular line.{/n}
"That was Lenna's. She refused to say it the way I wrote it."
"Because nobody would say it that way," Lenna replies.
{n}Kiana crosses out her original wording in front of them.{/n}
"There. A small public defeat. I expect it will improve the play."
{n}She smiles at Lenna, who looks absurdly pleased for a woman who has been arguing the point all afternoon.{/n}''', c('[Collect the pages once the questions have ended.]', "cost")),
    n("cost", "Narrator", '''{n}Meral begins returning the borrowed chairs. Kiana helps until Lenna makes her sit down and finish the water. There is ink on the side of her hand, where she has been writing faster than it could dry.{/n}''',
      c('[Count the room contributions with her.]', "paid", requires=("kiana.follow_audience",)),
      c('[Sort the written comments with her.]', "notes", requires=("kiana.follow_workshop",))),
    n("paid", "Kiana", '''"Enough for the room and the candles. Nearly enough for paper as well. Nobody should abandon honest employment on these figures."
{n}She separates the baker's payment before looking at what remains.{/n}
"But they paid. They came, listened, disagreed, and paid for the room in which they did it. I am going to enjoy that before I discover another expense."
{n}She leaves a small coin beside the cup for more water for the remaining guests, then closes the purse.{/n}
"Come tomorrow, or the day after. I will have become unbearable by then. You ought to see the whole progression."''', c('[Walk back with her after the room is clear.]', flags=("kiana.readers_kept",))),
    n("notes", "Kiana", '''{n}She has six sheets, three legible names and one drawing of a better arrangement of chairs.{/n}
"No coins. An impressive number of instructions. I did ask for them."
{n}She separates the chair drawing from the comments about the princess.{/n}
"I want to try the larger room after I have worked on this. Not tomorrow. If Edris asks, tell her I said not tomorrow very firmly."
{n}She glances at the closed purse she brought to buy the readers something to eat.{/n}
"This cost me an afternoon and six pastries. I think I can bear to have learned something at that price."''', c('[Carry the borrowed stools down before walking home with her.]', flags=("kiana.readers_kept",))),
], after="kiana.last_page_kept", delay=72)


s("ink_after", "What she does with applause", [
    n("start", "Kiana", '''{n}Kiana is copying the last page at a table near her window. Beside it lies a second sheet headed with the cook's name. It contains one line and a large blot.{/n}
"She has begun demanding her own story. That is what comes of giving a sensible person too much time near a princess."
{n}Kiana waves you toward the chair. There are no scattered papers on it this time.{/n}
"I cleared you a place before I began. I am capable of learning."''',
      c('[Sit and ask what she has changed.]', "change"),
      c('[Ask to come when you can stay.]', abort=True)),
    n("change", "Narrator", '''{n}The reading copy lies open beside the clean one. A thumbprint obscures the edge of the final speech.{/n}''',
      c('[Ask about the pause that gave her trouble.]', "long", requires=("kiana.follow_long_speech",)),
      c('[Ask whether she is keeping the shorter ending.]', "short", requires=("kiana.follow_short_speech",))),
    n("long", "Kiana", '''"I have cut the third image. We were both rather pleased with it, weren't we?"
"In a room with two people."
"A devastatingly appreciative audience. We shall have to stop trusting it."
{n}She taps the page.{/n}
"The first two pauses still belong. I liked hearing them think before they laughed. I lost the third because I wanted to explain something I had already let them see."
"Will you try it again?"
"Yes. With less staircase. I have enough trouble getting people into rooms without building another flight inside the speech."
{n}She keeps the crossed-out version beneath the new one.{/n}
"I don't wish I had never tried it. I wish I had heard that chair scrape while we were rehearsing. You might bring a worse chair next time."''', c('[Read the revised passage with her.]', "pages")),
    n("short", "Kiana", '''"Mostly. I have put back one sentence. Before you accuse me of smuggling the whole speech in, it is a different sentence."
{n}She reads it. The princess asks whether the guest can stay until the candles burn down, then admits that she bought very long candles.{/n}
"There. She is ridiculous again. I missed that at the end. I don't want all her bad habits cured by having someone accept an invitation."
{n}Kiana watches you smile and makes a small mark beside the line.{/n}
"I shall try it on someone who hasn't seen me decide that you liked it. You have become a rather sympathetic instrument."''', c('[Tell her where the new line made you laugh.]', "pages")),
    n("pages", "Kiana", '''"Meral can make clean copies. His ordinary work is copying accounts, but he says a princess cannot possibly have worse handwriting than his customers. I have shown him mine. He has withdrawn the comparison."
{n}She puts a written estimate beside the script.{/n}
"Three copies would let Lenna and Edris stop sharing. It would also leave me less for a room to work in. The place Meral used to copy in is available two afternoons a week. A desk. A door. No bed asking why I have covered it in paper."
{n}She looks around her own room.{/n}
"Or I could use his new room while he works downstairs for the baker. He would charge less. People would interrupt. I would have room to hear the words aloud."
"What do you want?"
"Today? Both, a new pen, and somebody to remove all the blots I have already made."''', c('"Which could you actually use next week?"', "means")),
    n("means", "Kiana", '''"I can pay for either for a month from what I have put aside. After that I shall need to decide again. My magnificent career has not yet purchased a door."
{n}She pushes the copy estimate nearer the script.{/n}
"I want a clean set before another reading. I can do that myself, slowly. It will cost evenings. If I pay Meral to copy it, I can spend those evenings writing the next part, but I would have to take the noisier room."
{n}A voice calls in the street. Kiana waits until it has passed before continuing.{/n}
"I don't want to move into your rooms and discover that every hour I fail to write feels like an expensive favor. This is small enough to try myself. Come and inspect the place I choose with me, though. I would like you there before I pay for it."''',
      c('"Take the quiet desk and make the copies slowly. You keep losing sentences to interruptions."', "quiet", flags=("kiana.follow_quiet_desk",)),
      c('"Pay for the copies and use Meral\'s room. You find things by hearing other people read."', "shared", flags=("kiana.follow_shared_room",))),
    n("quiet", "Kiana", '''"I do. Then I become cross with whoever has been living a perfectly reasonable life within earshot."
{n}She turns the copy estimate over and starts a list of pages.{/n}
"One clean page each evening. No pretending that an entire play will copy itself because I have grown tired of it. I shall keep the working afternoons for new writing."
"That sounds possible."
"What faint praise. I shall treasure it."
{n}She puts the estimate beneath the old script instead of tearing it up.{/n}
"We will look at the desk. If the room is dreadful, I reserve the right to become extravagant."''', c('[Arrange to inspect it with her.]', "company")),
    n("shared", "Kiana", '''"And I find other things by wishing they would be quiet. It may be an unusually productive room."
{n}She counts the pages once more, then signs the bottom of the estimate.{/n}
"I shall pay him for three copies. Not a fairytale edition in red ink. He suggested that. I think he wanted to find out how far my vanity extended."
"Did he?"
"Farther than my purse. Fortunately, one of them was listening."
{n}She folds the estimate and puts it beside her keys.{/n}
"We will see whether a desk fits between his table and that appalling shelf. I might require you to hold the shelf while I write."''', c('[Arrange to help measure the room.]', "company")),
    n("company", "Kiana", '''{n}With the decision made, she becomes aware that she has been holding a pen throughout the conversation. There is a dark mark on her finger.{/n}
"You came to see me. I have offered you accounts, furniture and an ink stain."
"The princess was free of charge."
"She is how I lure people in."
{n}Kiana puts the pen down and turns her chair until her knee rests against yours.{/n}
"I want to tell you something about this evening that has nothing to do with whether I have worked hard enough to deserve it."''',
      c('"Tell me."', "want"),
      c('[Take her hand and wait.]', "want")),
    n("want", "Kiana", '''"I have been thinking about kissing you since you came through the door. I thought I should finish explaining the desk first. I have begun to suspect that my priorities were poor."
{n}Her thumb rests against the inside of your wrist. She looks at your mouth, then up at you, quite deliberately.{/n}''',
      c('[Kiss her.]', "kiss", flags=("kiana.follow_ink_kiss",)),
      c('"Come out with me first. I would like an evening in which neither of us is at a desk."', "outside", flags=("kiana.follow_ink_walk",))),
    n("kiss", "Narrator", '''{n}Kiana rises into the kiss, bringing you up with her. She keeps the hand with the ink stain away from your collar until you catch it and draw it against you.{/n}
"That will mark."
"I know."
{n}Her next laugh is softer. She closes the space between you and leaves the pen, the accounts and the princess where they are. When you finally move away from the table, she reaches back only to cover the ink.{/n}
"One practical thought. Then I intend to become a very bad example."
{n}The lamp burns lower while the pages remain unread. Later, she finds the mark on your collar and refuses to look sorry for it.{/n}''', c('[Keep the evening with her.]', flags=("kiana.ink_evening_kept",))),
    n("outside", "Kiana", '''"A bold proposal. We may discover we have legs."
{n}She washes the ink from her hand before fastening the blue shawl. The water darkens, then clears beneath her fingers.{/n}
"There is a woman near the market who sells little cakes after the stalls close. I have been meaning to find out whether they are as good as they smell."
"And if they aren't?"
"We shall have something to complain about together. I have considerable confidence in our ability."
{n}She takes your arm in the doorway. You walk without the pages. At the market she buys one cake, tastes it, then orders a second before offering you the first.{/n}
"You may have that. I have established that it is safe from disappointment."''', c('[Share the walk back after the stalls have closed.]', flags=("kiana.ink_evening_kept",))),
], after="kiana.readers_kept")


s("working_room", "A place for the unfinished", [
    n("start", "Kiana", '''{n}Kiana has brought a measuring string, her purse and a sheet containing six lines of the cook's new story. She holds the sheet up before you can ask about the string.{/n}
"I intend to find out whether I can write here before I pay for the privilege. Meral thought that was very sensible. I suspect he thought I would do something involving curtains."
{n}She glances at the upper window.{/n}
"I may still do something involving curtains. After the investigation."''',
      c('[Go in with her.]', "room"),
      c('[Arrange another inspection when you can stay.]', abort=True)),
    n("room", "Narrator", '''{n}The key has been left with the baker. Kiana signs her name beside the time, then follows you upstairs.{/n}''',
      c('[Inspect the quiet copying room.]', "desk", requires=("kiana.follow_quiet_desk",)),
      c('[Measure the space in Meral\'s room.]', "shared", requires=("kiana.follow_shared_room",))),
    n("desk", "Kiana", '''{n}The old copying room has a narrow desk and a window overlooking a wall. Kiana sits, arranges her page, and listens. A cart passes. Somewhere below, a pan strikes a table. Then the room grows quiet again.{/n}
"I can hear myself being dissatisfied. Excellent."
{n}She writes half a line. The chair wobbles when she reaches for the ink. You fold a scrap beneath its short leg. Kiana tests it with an elaborate shift of weight.{/n}
"You have saved a literary career of nearly twenty minutes."
{n}She tries again. This time she finishes the sentence before looking up.{/n}
"The light goes early. I would have to begin after the midday meal. If I leave it until later, I shall spend the savings on candles."
{n}She looks toward the blank wall outside, then at the page.{/n}
"I want it. For the month. I can decide about the wall after I know what I have written beside it."''', c('[Help her measure the shelf for her papers.]', "quiet_cost")),
    n("quiet_cost", "Kiana", '''"The clean copies will take longer. I have begun the first."
{n}She shows you a page in her careful hand. Near the bottom, one word has been corrected twice.{/n}
"I changed the line while copying it. That is apparently forbidden if I ever want three copies to agree. I shall make a separate list of changes. Meral looked very tired when I asked whether that was necessary."
"Will you finish them?"
"Yes. Slowly. The next reading can wait for its own pages."
{n}Kiana sets the unfinished story on the desk and presses its corners flat.{/n}
"I will miss having someone interrupt with a better line. I can invite them to do that on another afternoon. Today I want the silence I have paid for."''', c('[Leave the story on the desk while she takes the key downstairs.]', "terms")),
    n("shared", "Kiana", '''{n}Meral has moved the shelf against the wall. It now stands on four legs, an achievement Kiana inspects with open admiration. Three clean copies of the play lie on his table.{/n}
"I see you have abandoned the chair as a building material."
"Temporarily."
{n}She reads a page from each copy, checking the same passage. The words agree. She pays Meral the sum on his estimate, then gathers the copies with a pleased care she cannot quite disguise.{/n}
"They look as though someone meant them to be read."
{n}Meral carries his account book downstairs, leaving her the table. She lays out the new story and begins. Before she reaches the end of a sentence, somebody knocks to ask whether Meral has finished a bill.{/n}
"Downstairs," Kiana says.
{n}She starts again. A second knock follows almost at once.{/n}
"If that is the same bill, I have begun to resent it personally."''', c('[Wait while she deals with the visitor.]', "shared_cost")),
    n("shared_cost", "Kiana", '''{n}It is Edris, returning a stool. Kiana lets her in, then realizes she has stood up to welcome exactly the kind of interruption she meant to prevent.{/n}
"Put it there. Sit on it if you like. I need to finish this line before I become impossible."
{n}Edris sits. Kiana writes, scratches out a word and asks what a cook would call a princess who keeps changing the supper hour.{/n}
"Hungry," Edris says.
{n}Kiana puts down the pen and laughs.{/n}
"That is better. I was going to make it much longer."
{n}She writes the word, then puts a little line beneath it.{/n}
"I want to try this room. But I shall need a notice for the door. Meral's customers must find Meral, and my guests must let me finish a sentence before improving it."
{n}Edris volunteers to write the notice. Kiana takes the paper from her before it grows elaborate.{/n}
"Meral downstairs. Kiana working. That will do."''', c('[Help her fix the small notice beside the door.]', "terms")),
    n("terms", "Narrator", '''{n}Downstairs, Kiana pays for the first month and checks the days against her own list. The baker gives her a receipt with flour along one edge. Kiana folds it carefully rather than brushing it over the counter.{/n}
{n}Outside, she looks at the key in her palm.{/n}
"Two afternoons each week. I have managed to rent a very small amount of the future."
{n}She closes her hand around it, then turns toward you.{/n}''',
      c('"Which evening shall I keep for you?"', "promised", requires=("kiana.committed",)),
      c('"I would like to see what you write here."', "unpromised", forbids=("kiana.committed",))),
    n("promised", "Kiana", '''"The one after my second afternoon here. I may have something to read, or I may want to go somewhere that has never heard of a princess."
{n}She names a day and watches you consider it.{/n}
"We said we would make room. This is the room I have made. I want to know where the evening with you goes, so that I can stop keeping every other evening empty by accident."
"That day will do."
"Good. I shall write it beside the other arrangements. You will be in distinguished company. Rent, copying, somebody who has promised to mend my shoe."''', c('[Keep the evening she has named.]', "end", flags=("kiana.follow_evening_arranged",))),
    n("unpromised", "Kiana", '''"Then come after the second afternoon. I shall have had enough time to produce something and not enough to convince myself it is all dreadful."
{n}She names a day.{/n}
"I remember what you said about afterward. I am not going to slip a lifetime into the agreement while you are admiring the key. I do want this evening."
"So do I."
"There. A manageable arrangement. You needn't stand looking relieved. I have not asked you to carry the desk home."''', c('[Agree to that evening without adding a promise about after the war.]', "end", flags=("kiana.follow_evening_arranged",))),
    n("end", "Kiana", '''{n}She drops the key into her purse. Its small sound makes her smile.{/n}
"I thought it would feel grander."
"You could announce it."
"To whom? The baker already knows."
{n}Kiana looks up at the window, then turns away from it with a sudden, pleased decisiveness.{/n}
"Come and eat something with me. I have rented the afternoons. I refuse to donate the rest of the day to imagining them."''', c('[Walk with her toward the market.]', flags=("kiana.workroom_taken",))),
], after="kiana.ink_evening_kept")


s("kept_evening", "The time beside her name", [
    n("start", "Narrator", '''{n}Kiana's door is open a little when you arrive for the evening you arranged. Inside, a pen scratches across paper, stops, then begins again. She notices you before you knock.{/n}
"I know. I am late. I thought I could finish the page before you came. Then the page acquired an objection."
{n}She puts the pen down, though she is still looking at the last sentence.{/n}
"I can stop now. Or I could have a little time to finish this without trying to remember it through supper. Tell me which would make you less inclined to curse my entire profession."''',
      c('"Finish the page. I will fetch something for us to eat."', "fetch", flags=("kiana.follow_waited_page",)),
      c('"Put it aside. I have been looking forward to seeing you."', "stop", flags=("kiana.follow_stopped_page",)),
      c('[Explain that you cannot keep the evening and ask her to arrange another.]', abort=True)),
    n("fetch", "Kiana", '''"Thank you. Bread, if they have the dark kind. And something that can be eaten without using the same hand as a pen."
{n}She catches herself and looks up.{/n}
"No. I will put the pen away before you return. Bring whatever looks good. I shall stop attempting to organize the meal around a sentence."
{n}When you come back, the page is finished and the ink covered. Kiana has washed her hands and laid the table. She takes the parcel from you with a flourish entirely disproportionate to its size.{/n}
"Supper. Delivered by an exceptionally distinguished person. I shall try not to become accustomed to this level of service."
{n}She opens it, finds the bread and tears off the end before you have sat down.{/n}''', c('[Sit with her once she has brought the cups.]', "work")),
    n("stop", "Kiana", '''"All right."
{n}She writes three words on a scrap, puts it across the page and covers the ink. The movement is reluctant, but she gets up without adding another line.{/n}
"I have left myself the end. If tomorrow's Kiana cannot understand it, she will have only tonight's Kiana to blame."
{n}She comes to you, rests her hands against your arms and looks at your face properly, as though she has only now been allowed to.{/n}
"Hello. I am pleased you came. That should have been the first thing I said."
{n}The food she has bought waits in a covered bowl. She brings it to the table, tastes a little and decides it will do without reheating.{/n}
"Cold supper. Warm company. I can work with that."''', c('[Help her set the table.]', "work")),
    n("work", "Kiana", '''{n}Over the meal she tells you about the room. There has been a difficulty she did not anticipate, and a small success she had been waiting to describe to someone.{/n}''',
      c('[Ask about the quiet afternoons.]', "quiet", requires=("kiana.follow_quiet_desk",)),
      c('[Ask whether the notice survived the first week.]', "shared", requires=("kiana.follow_shared_room",))),
    n("quiet", "Kiana", '''"I wrote more on the first afternoon than I did on the second. On the second I kept reading the first afternoon's work and finding things wrong with it. Apparently silence does not prevent that."
{n}She shows you a clean sheet with a single dark correction near the bottom.{/n}
"The copies are progressing. One is finished. The other two are making me appreciate Meral's prices. Lenna asked for hers, and I had to tell her when it would actually be ready."
"Did she mind?"
"She said she was tired of guessing the last words on every line. I think she has grounds for complaint."
{n}Kiana puts the sheet away before it can become the whole conversation.{/n}
"The new story has a cook who leaves at the end of her working day. I am beginning to understand why I like her."''', c('[Ask what the cook does with the evening.]', "hers")),
    n("shared", "Kiana", '''"The notice survived. Meral's customers mostly read it. My friends believe it means I am available for very short interruptions."
{n}She takes a clean copy of the play from the shelf and lets you see the pages.{/n}
"Lenna and Edris have theirs. We read the last scene again yesterday. Lenna found a place where the cook is still in the room after I sent her out. I have employed an extremely vigilant cook."
"Did you fix it?"
"I gave her a reason to come back. She has forgotten her wages. Lenna approves."
{n}Kiana closes the copy.{/n}
"I wrote less than I meant to. What I wrote was better when I heard it. I shall have to decide how much noise I can use before it becomes simply noise. One week has not made me an expert."''', c('[Ask what happens after the cook gets paid.]', "hers")),
    n("hers", "Kiana", '''"She goes out. I haven't decided where. Somewhere the princess cannot send for her."
{n}Kiana considers her own cup.{/n}
"I might take an evening like that. No reading. No people asking what I have finished. I shall invite you if I want company, and if you cannot come I may go anyway. I have been leaving too many pleasant things until someone can do them with me."
"Where would you go?"
"That is the difficulty. I have invented a woman with an entire city to choose from and given myself a list consisting mostly of bakeries."
{n}She smiles at you over the cup.{/n}
"You may suggest something. Nothing involving a castle. I have enough trouble maintaining the imaginary one."''',
      c('"A walk at the hour when the market opens. Let somebody else be busy for a change."', "morning", flags=("kiana.follow_market_morning",)),
      c('"Find music you do not have to explain afterward. Sit until you feel like leaving."', "music", flags=("kiana.follow_music_wish",))),
    n("morning", "Kiana", '''"You are recommending that I rise early for pleasure. I must like you a great deal to continue listening."
{n}She turns the suggestion over, less dismissively than she sounds.{/n}
"The fruit sellers do have the best things then. I could buy something before it has spent all day being admired by other people. I might even take Lenna if she promises not to ask about the pages."
{n}Kiana writes the idea on the back of the meal's wrapping paper.{/n}
"There. An intention. I have learned the difference between writing it down and having done it. You may ask me later whether I went."''', c('[Leave the invitation open for another day.]', "future")),
    n("music", "Kiana", '''"Something I haven't helped write? What an extravagant idea."
{n}She taps a finger against the cup, trying to remember a tune, then abandons it.{/n}
"I shall ask Edris what she has heard. Ask where, I mean, before she sings it all to me and saves me the journey."
"Would you want company?"
"Perhaps. I want to find it first. I like the thought of bringing you to something I have discovered, instead of asking you to watch me arrange another room."
{n}She writes a question for Edris on a scrap and leaves it where she will see it in the morning.{/n}''', c('[Let her keep the pleasure of finding it.]', "future")),
    n("future", "Narrator", '''{n}The meal is finished. Kiana carries the cups away, then returns to the place beside you. There are pages waiting, but she leaves them on the other side of the room.{/n}''',
      c('"I like the life we are finding time for."', "steady", requires=("kiana.committed",)),
      c('"I am glad we kept this evening."', "present", forbids=("kiana.committed",))),
    n("steady", "Kiana", '''"So do I. Even the parts that turn out to involve rent and copying the same sentence three times."
{n}She draws your hand into her lap.{/n}
"I don't know what the room after the war will look like. I used to furnish it in my head whenever I was frightened. Everything stayed exactly where I put it. There were never any visitors I hadn't invited."
{n}Her mouth curves.{/n}
"This is much less convenient. I have begun to prefer it. There is someone in it who might ask me to leave the work alone and eat supper."
"An unreasonable guest."
"I chose the guest. I expect to be reminded."''', c('[Stay close while the street grows quieter.]', "close")),
    n("present", "Kiana", '''"Then keep another. When you can. I would rather hear a day than a magnificent description of what might happen someday."
{n}She draws your hand into her lap.{/n}
"I am making plans of my own. I want you in some of them. That is what I know tonight."
"I want to be here."
"You are here. For once we have managed the difficult part before discussing it."
{n}Kiana leans against you. She does not ask for the lasting promise you have not made, and she does not give the evening back because it lacks one.{/n}''', c('[Enjoy the time you actually have together.]', "close")),
    n("close", "Kiana", '''"There is one more thing I wanted before you go."
{n}She turns toward you, her pale crystals catching the last of the lamplight. The blue shawl has slipped from one shoulder. She leaves it there.{/n}''',
      c('[Kiss her and stay a little longer.]', "kiss", flags=("kiana.follow_last_kiss",)),
      c('[Draw her beside you and ask her to stay there for a while.]', "quiet_end", flags=("kiana.follow_last_quiet",))),
    n("kiss", "Narrator", '''{n}She has no line prepared this time. Kiana's hand settles behind your neck as she kisses you, and the shawl slides the rest of the way onto the chair. She catches it without looking, tosses it over the back, and returns to you with a small, impatient smile.{/n}
"It will survive."
{n}The pages wait where she left them. When you part later, she walks you to the door in no hurry to open it, then laughs at herself and does.{/n}
"Go. Before I begin making tomorrow less sensible as well."''', c('[Leave her with the evening kept and another page to write.]', flags=("kiana.followthrough_kept",))),
    n("quiet_end", "Narrator", '''{n}Kiana settles against you and pulls the shawl over both your knees. For a while she tells you about a word in the old rehearsal copy that looked so much like cupboard that the princess appeared to be proposing marriage to one. Then she stops talking and listens to the street.{/n}
{n}When you get up to leave, she folds the shawl rather than putting it on. She is staying in for the rest of the night. There is water to empty from the basin, and a bed that has finally been cleared of papers.{/n}
"Good night," she says, kissing the side of your face. "I liked having you here."''', c('[Leave her to the rest of her evening.]', flags=("kiana.followthrough_kept",))),
], after="kiana.workroom_taken", delay=168)
