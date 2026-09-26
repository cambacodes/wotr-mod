"""Chapter 5 bridge for the unfinished authored Abyss copyist episode."""
from story_format import c, n, scene

SCENES = []


def s(id, title, entry, nodes):
    for node in nodes:
        node["Portrait"] = "Seelah"
    SCENES.append(scene("seelah." + id, title, "Seelah", 5, entry, nodes,
                        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
                        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5],
                        requires=("seelah.letter_unsettled",),
                        RequiresAny=["seelah.letter_public", "seelah.letter_burned"],
                        ForbidOverrides={"seelah.farewell": "seelah.catchup_requested"},
                        forbids=("seelah.copyist_followed", "seelah.letter_return_addressed",
                                 "seelah.closed", "seelah.farewell", "seelah_dead", "seelah_gone", "inhuman"),
                        optional=True, delay=0))


s("letter_return", "The part we left behind", '"You wanted to speak about the copyist."', [
    n("start", "Seelah", '''{n}Seelah has a folded page in her hand. She smooths it against her thigh, reads a line, and folds it again.{/n}
"Halven is putting together accounts of the Abyss. He's a writer here, not somebody who went with us. He asked me for a story people would want to hear. I said I had a few."
{n}She unfolds the page and shows you the heading: A LETTER RESCUED FROM A DEMON'S CITY.{/n}
"I mentioned the stall. He came back with this. I haven't given him an account yet, and already we're doing splendidly."
{n}Her expression hardens.{/n}
"I told him to wait. We need to talk about what happened before I answer him."''',
      c('"All right. Let me see it."', "unfinished", forbids=("seelah.letter_discussed",)),
      c('"All right. Let me see it."', "discussed", requires=("seelah.letter_discussed",)),
      c('"I cannot give this the attention it needs now. Keep him waiting a little longer."', abort=True)),
    n("unfinished", "Seelah", '''"I asked you for a night to be angry. We were supposed to speak afterward."
{n}She hands you the page. Beneath the heading, Halven has left space for the story. He has already written Seelah's name below it.{/n}
"We made it home without doing that. I don't want this to become something we avoid because we've managed to avoid it so far."
{n}She pulls a chair away from the table and sits with its back against the wall.{/n}
"I can think of several impressive excuses. I'd rather hear what you actually think."''',
      c('"Then let us talk about the letter."', "public", requires=("seelah.letter_public",)),
      c('"Then let us talk about the letter."', "burned", requires=("seelah.letter_burned",))),
    n("discussed", "Seelah", '''"We did talk. I haven't forgotten."
{n}She pulls a chair away from the table and sits with its back against the wall.{/n}
"But talking to each other didn't tell us how things turned out for her. Now there's a blank space here waiting for a happy ending, and I have no idea what to put in it."
{n}She taps the name Halven has already written beneath the empty page.{/n}
"He's made room for me to sign it, though. Very thoughtful."''',
      c('"Our agreement still matters."', "old_signal", requires=("seelah.check_signal",)),
      c('"Our agreement still matters."', "old_person", requires=("seelah.check_person",), forbids=("seelah.check_signal",)),
      c('"We can say what we know without inventing what followed."', "known", forbids=("seelah.check_signal", "seelah.check_person"))),
    n("old_signal", "Seelah", '''"Two taps. I stop and look. Yes."
{n}She lays her wrist on the table, then takes it back to unfold the page.{/n}
"I still mean it. We don't need to make the promise again. We need to decide what to do with this."''', c('[Look at the unfinished account.]', "known")),
    n("old_person", "Seelah", '''"Watch the person we went to help. Even when one of us is making a speech. Especially then."
{n}She gives you a brief, crooked smile.{/n}
"I remember. I'm not asking you to sit through my discovery of it a second time. But I haven't decided what to tell Halven."''', c('[Look at the unfinished account.]', "known")),
    n("known", "Seelah", '''"Start there, then. Before I get annoyed enough with his title to throw out the whole page."
{n}She finds a pen, tests its point, and waits for you to speak.{/n}''',
      c('"She had the letter when she left us."', "public", requires=("seelah.letter_public",)),
      c('"He burned it before she could take it back."', "burned", requires=("seelah.letter_burned",))),
    n("public", "Seelah", '''"She did get it back. I remember her opening it in that passage. I was so pleased with us for about half a breath."
{n}Seelah looks at the title.{/n}
"Then she told us she would have to go back to those stalls. People knew whose sister had written it. She had asked us not to tell him it was hers, and somebody recognized her when she took it."
{n}She sets the pen down.{/n}
"I wanted that bastard to stop reading. I still want him to have stopped. But I can't tell you that the crowd forgot her when we walked away."
{n}She meets your eyes.{/n}
"Do you still think we did the right thing?"''',
      c('"I would stop him again. Getting her letter back mattered, even with that cost."', "public_defend", flags=("seelah.letter_return_stood",)),
      c('"I wish we had found a way to get it back without making her visible."', "public_regret", flags=("seelah.letter_return_reconsidered",))),
    n("public_defend", "Seelah", '''"It did. I'm not going to say the letter was worthless just because the rest went badly."
{n}She leans forward, elbows on her knees.{/n}
"But I don't know whether she would choose our way again. I won't put an answer in her mouth because it would make ours easier."
{n}For a moment she looks ready to argue further. Instead she picks up the pen and strikes out the word RESCUED.{/n}
"I can disagree with you about what we should have done and still write down what happened."''', c('"Write that she recovered the letter, and that we exposed her while doing it."', "limits")),
    n("public_regret", "Seelah", '''"So do I."
{n}She rubs a hand over her face.{/n}
"I've invented several ways since. They all work beautifully now that nobody is shouting and I know what the crowd is going to do. Very useful. Perhaps I should have brought that Seelah with us."
{n}Her laugh is short.{/n}
"We can regret it. We can't send the regret back and collect a better afternoon."''', c('"Then keep both parts of what actually happened."', "limits")),
    n("burned", "Seelah", '''"She went away without it. And he never got to read the rest to that crowd. Both happened."
{n}Seelah scratches out RESCUED so heavily that the pen catches in the paper.{/n}
"I keep thinking about the little house her sister drew beside her name. Then I get angry with you for distracting him, and remember that I helped her toward the counter because I thought it would work."
{n}She puts the damaged pen aside.{/n}
"I was there. I don't get to stand here pretending I had a perfect plan you ignored."''',
      c('"I would still try to keep her identity out of his performance."', "burned_defend", flags=("seelah.letter_return_stood",)),
      c('"I wish I had seen the fire as more than a risk we could get past."', "burned_regret", flags=("seelah.letter_return_reconsidered",))),
    n("burned_defend", "Seelah", '''"And she said it mattered that he didn't reach the end. I'm glad of that."
{n}She turns the page sideways, studying the tear left by the pen.{/n}
"I also wish she had been able to read it herself. I can be glad of one thing and furious about the other without deciding you set out to hurt her."
{n}She looks up.{/n}
"That is where I've got to. It isn't a very stirring speech."''', c('"It is a more honest account than his title."', "limits")),
    n("burned_regret", "Seelah", '''"I saw it too. Sparks coming up under the counter. Then you started talking about tassels, and I saw a way to get her closer."
{n}Seelah shakes her head.{/n}
"Don't take my share of that because I'm the one looking angry. There is plenty to go round."
{n}She finds a second pen and checks it before using it.{/n}
"I don't want to spend the rest of this conversation proving who feels worse. She still doesn't have the letter at the end of that."''', c('"Then let us decide what we can truthfully tell him."', "limits")),
    n("limits", "Seelah", '''"We don't know how she is living now. I can't promise that a message from here would reach her. I don't even know where she would want one sent."
{n}Seelah looks toward the door, as if the distance might briefly take a shape she could hit.{/n}
"I'd like to do something better than sit in a comfortable room and feel bad. But pretending we found her a safe life would be a particularly rotten way to cheer ourselves up."
{n}She turns the page over.{/n}
"Halven wants a story about us. We can give him a short account of our own mistake, without her trade, her sister, or where it happened in the city. Or we can tell him to leave the whole incident out. I won't give him her letter to read aloud a second time."''',
      c('"Give him the limited account. Let people hear that intervening can leave someone else with the cost."', "account", flags=("seelah.letter_return_account",)),
      c('"Leave her out of his collection. We do not need to make this public to face what we did."', "withhold", flags=("seelah.letter_return_withheld",))),
    n("account", "Narrator", '''{n}Together, you write a short passage about interrupting a cruel performance in Alushinyrra. It names you and Seelah. It identifies no other person or stall. It says that you acted with incomplete knowledge, that the intervention had a cost for the person you meant to help, and that you cannot report what followed after your part in it.{/n}
{n}Seelah reads it, circles the phrase COMPLETE SUCCESS that Halven has penciled beside the old heading, and draws a line through that as well.{/n}
{n}"He is going to wish he'd asked someone with better adventures."{/n}
{n}She pauses, then adds her name beneath the new passage.{/n}
{n}"Come on. I'll give him this myself."{/n}''', c('[Go with her.]', "deliver_account")),
    n("withhold", "Seelah", '''"All right. He can have another story when I am ready to tell one."
{n}She folds Halven's unfinished account. On the outside she writes: Do not include this incident.{/n}
"That should be difficult to misunderstand. I ought to leave room for him to surprise me."
{n}She stands, chair legs scraping against the floor.{/n}
"I'll tell him myself as well. I want to hear him agree before I let it go."''', c('[Go with her.]', "deliver_withheld")),
    n("deliver_account", "Narrator", '''{n}Halven is a narrow-faced man with gray in his beard and a dark ink stain along the side of his hand. He reads the passage standing beside his table, then looks at Seelah.{/n}
{n}"There is not much of the actual incident here."{/n}
{n}"That is all we are giving you."{/n}
{n}"I could make the wording more encouraging."{/n}
{n}"You can ask before you change it. Otherwise you can leave it out."{/n}
{n}He looks from her to you. You leave the decision where she has put it. After another reading he sets the passage on top of his other pages and draws a line through the old title in his notes.{/n}
{n}"As written, then. With your names?"{/n}
{n}"Our names. Nobody else's."{/n}
{n}He nods. Seelah waits while he writes that instruction beneath the passage, then leaves the page with him.{/n}''', c('[Leave with Seelah.]', "outside")),
    n("deliver_withheld", "Narrator", '''{n}Halven is a narrow-faced man with gray in his beard and a dark ink stain along the side of his hand. He reads Seelah's instruction twice.{/n}
{n}"I had set aside a page."{/n}
{n}"Use it for something else."{/n}
{n}"I would have shown it to you before copying it."{/n}
{n}"Good. I'm telling you now. No account of this incident."{/n}
{n}He presses his lips together, then crosses the heading out of his notes. He gives her the empty page back.{/n}
{n}"Another story, perhaps?"{/n}
{n}"Perhaps. I'll choose it before you choose the ending."{/n}
{n}Outside the room, Seelah folds the returned page into a small square and puts it away.{/n}''', c('[Leave with Seelah.]', "outside")),
    n("outside", "Seelah", '''{n}Seelah stops beside an open doorway, out of the flow of people along the passage. For a while she says nothing.{/n}
"Well. We've dealt with the one man I can actually find."
{n}The attempt at humor fades, but she does not take it back.{/n}
"I still wish we knew how she was doing. I expect I will keep wishing it."
{n}She looks at you.{/n}
"And I don't want to keep making you guess whether I'm angry about that or angry with you. You have told me what you think. I've told you. I can stop leaving the next conversation hanging over us."''',
      c('"Walk with me for a while."', "company", flags=("seelah.letter_return_company",)),
      c('"I would like some time alone after this."', "space", flags=("seelah.letter_return_space",))),
    n("company", "Seelah", '''"Yes."
{n}She falls into step beside you. At the first turning, somebody hurries past carrying an unstable pile of folded cloth. Seelah moves aside, watches it tilt, and catches the top piece before it reaches the floor.{/n}
"There. A complete success. I shall have Halven give it a whole page."
{n}The carrier thanks her and goes on. Seelah's laugh comes out tired, but it is a laugh.{/n}
{n}She walks beside you without reaching for more than you have offered.{/n}''', c('[Continue the walk.]', flags=("seelah.letter_return_addressed",))),
    n("space", "Seelah", '''"All right."
{n}She steps back to give you room to leave.{/n}
"Thank you for staying through that. I know it wasn't the evening either of us would have chosen."
{n}She starts toward the other end of the passage, then looks back.{/n}
"We can speak about something else next time. I do still know other subjects. I may need a little practice finding one that doesn't involve a very satisfying threat."
{n}She leaves you to your own way without asking you to smile for her before you go.{/n}''', c('[Take the time you asked for.]', flags=("seelah.letter_return_addressed",))),
])
