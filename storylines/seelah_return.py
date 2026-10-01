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
"I told him to wait. You and I have a few things to say about that stall before I give him a story."''',
      c('"All right. Let me see it."', "unfinished", forbids=("seelah.letter_discussed",)),
      c('"All right. Let me see it."', "discussed", requires=("seelah.letter_discussed",)),
      c('"I cannot sit down with this now. Keep him waiting."', abort=True)),
    n("unfinished", "Seelah", '''"I told you to leave me to my temper that night. But we were supposed to talk afterward."
{n}She hands you the page. Beneath the heading, Halven has left space for the story. He has already written Seelah's name below it.{/n}
"We made it all the way home without a word about it. Well, we're sitting down now. No more walking past each other with our mouths shut."
{n}She pulls a chair away from the table and sits with its back against the wall.{/n}
"I can think of several impressive excuses. I'd rather hear what you actually think."''',
      c('"Then let us talk about the letter."', "public", requires=("seelah.letter_public",)),
      c('"Then let us talk about the letter."', "burned", requires=("seelah.letter_burned",))),
    n("discussed", "Seelah", '''"We did talk. I haven't forgotten."
{n}She pulls a chair away from the table and sits with its back against the wall.{/n}
"But talking to each other didn't tell us how things turned out for her. Now there's a blank space here waiting for a happy ending, and I have no idea what to put in it."
{n}She taps the name Halven has already written beneath the empty page.{/n}
"He's made room for me to sign it, though. Very thoughtful."''',
      c('"I remember. Two taps, and we stop and look."', "old_signal", requires=("seelah.check_signal",)),
      c('"I remember. Watch the person we went to help."', "old_person", requires=("seelah.check_person",), forbids=("seelah.check_signal",)),
      c('"Tell him what happened at the stall. We do not know the rest."', "known", forbids=("seelah.check_signal", "seelah.check_person"))),
    n("old_signal", "Seelah", '''"Two taps. I stop and look. Yes."
{n}She lays her wrist on the table, then takes it back to unfold the page.{/n}
"I'll remember. Now, what are we going to put on this damned page?"''', c('[Look at the unfinished account.]', "known")),
    n("old_person", "Seelah", '''"Watch the person we went to help. Even when one of us is making a speech. Especially then."
{n}She gives you a brief, crooked smile.{/n}
"Yes, yes, I remember. Spare you another speech, shall I? Halven's still waiting for his story."''', c('[Look at the unfinished account.]', "known")),
    n("known", "Seelah", '''"Start there, then. Before I get annoyed enough with his title to throw out the whole page."
{n}She finds a pen, tests its point, and waits for you to speak.{/n}''',
      c('"She had the letter when she left us."', "public", requires=("seelah.letter_public",)),
      c('"He burned it before she could take it back."', "burned", requires=("seelah.letter_burned",))),
    n("public", "Seelah", '''"She did get it back. I remember her opening it in that passage. I was so pleased with us for about half a breath."
{n}Seelah looks at the title.{/n}
"Then she told us she would have to go back to those stalls. People knew whose sister had written it. She had asked us not to tell him it was hers, and somebody recognized her when she took it."
{n}She sets the pen down.{/n}
"I wanted to shut that bastard's mouth. I still do. But those people saw her take the letter. I doubt they forgot her face just because we walked away."
{n}She meets your eyes.{/n}
"Do you still think we did the right thing?"''',
      c('"I would stop him again. Her letter was worth getting back, even after what happened."', "public_defend", flags=("seelah.letter_return_stood",)),
      c('"I wish we had got it back without showing the whole crowd her face."', "public_regret", flags=("seelah.letter_return_reconsidered",))),
    n("public_defend", "Seelah", '''"It was worth getting back. No argument there. It was her sister's letter, for gods' sake."
{n}She leans forward, elbows on her knees.{/n}
"Would she thank us for doing it that way again? I don't know. She's the one who has to go back to those stalls."
{n}For a moment she looks ready to argue further. Instead she picks up the pen and strikes out the word RESCUED.{/n}
"I still think we should have done it differently. But I can write down what happened without winning an argument first."''', c('"Write that she got her letter back, and the crowd saw who took it."', "limits")),
    n("public_regret", "Seelah", '''"So do I."
{n}She rubs a hand over her face.{/n}
"I've invented several ways since. They all work beautifully now that nobody is shouting and I know what the crowd is going to do. Very useful. Perhaps I should have brought that Seelah with us."
{n}Her laugh is short.{/n}
"We can regret it. We can't send the regret back and collect a better afternoon."''', c('"Then keep both parts of what actually happened."', "limits")),
    n("burned", "Seelah", '''"She left empty-handed. But we stopped him reading the rest aloud. That's what happened."
{n}Seelah scratches out RESCUED so heavily that the pen catches in the paper.{/n}
"I keep thinking about the little house her sister drew beside her name. Then I get angry with you for distracting him, and remember that I helped her toward the counter because I thought it would work."
{n}She puts the damaged pen aside.{/n}
"I was there. I helped her toward that counter. If I had a better plan, I certainly kept it to myself!"''',
      c('"I would still try to keep him from telling the crowd whose letter it was."', "burned_defend", flags=("seelah.letter_return_stood",)),
      c('"I saw the fire. I wish I had taken it seriously."', "burned_regret", flags=("seelah.letter_return_reconsidered",))),
    n("burned_defend", "Seelah", '''"And she said it mattered that he didn't reach the end. I'm glad of that."
{n}She turns the page sideways, studying the tear left by the pen.{/n}
"But she never got to read it herself. That still makes me furious. I know you weren't trying to burn her letter. I wish we'd been cleverer than that bastard."
{n}She looks up.{/n}
"There. That's all I've got. Nobody's going to put that speech on a banner."''', c('"It is a more honest account than his title."', "limits")),
    n("burned_regret", "Seelah", '''"I saw it too. Sparks coming up under the counter. Then you started talking about tassels, and I saw a way to get her closer."
{n}Seelah shakes her head.{/n}
"I helped. Don't go claiming the whole blunder just because I'm scowling at you."
{n}She finds a second pen and checks it before using it.{/n}
"And let's stop trying to outdo each other at kicking ourselves. It won't fish her letter out of the ashes."''', c('"Then what shall we tell Halven?"', "limits")),
    n("limits", "Seelah", '''"I don't know how she's faring. I'd send her a letter if I knew where to send it. Or who could get it there without making more trouble for her."
{n}Seelah looks toward the door, her fist clenched against her knee.{/n}
"I'd rather be doing something for her than sitting here grinding my teeth. But I'm not going to tell people she's safe just so they can slap us on the back."
{n}She turns the page over.{/n}
"Halven wants a story about us. Fine, we can tell him how we blundered. No word about her trade, her sister, or where to find that stall. Or he can leave the whole thing out. Her letter isn't going into another man's mouth."''',
      c('"Tell him what we did. Leave out anything that could name her. People should hear who paid for our mistake."', "account", flags=("seelah.letter_return_account",)),
      c('"Leave the whole incident out. We know what we did. He can fill his book with something else."', "withhold", flags=("seelah.letter_return_withheld",))),
    n("account", "Narrator", '''{n}Between you, you fill a few lines with the ugly business in Alushinyrra. Your names go at the top. The copyist's trade, her sister and the stall's whereabouts stay off the page. You write what you did, what you failed to see, and how the woman you went to help bore the consequences. The account ends where you lost sight of her.{/n}
{n}Seelah reads it, circles the phrase COMPLETE SUCCESS that Halven has penciled beside the old heading, and draws a line through that as well.{/n}
{n}"He is going to wish he'd asked someone with better adventures."{/n}
{n}She pauses, then adds her name beneath the new passage.{/n}
{n}"Come on. I'll give him this myself."{/n}''', c('[Go with her.]', "deliver_account")),
    n("withhold", "Seelah", '''"All right. He can wait for a different story. I've no taste for telling one tonight."
{n}She folds Halven's unfinished account. On the outside she writes: Do not include this incident.{/n}
"Plain enough, you'd think. Watch him find a way to misunderstand it."
{n}She stands, chair legs scraping against the floor.{/n}
"I'll tell him myself as well. I want to hear him agree before I let it go."''', c('[Go with her.]', "deliver_withheld")),
    n("deliver_account", "Narrator", '''{n}Halven is a narrow-faced man with gray in his beard and a dark ink stain along the side of his hand. He reads the passage standing beside his table, then looks at Seelah.{/n}
{n}"There is not much of the actual incident here."{/n}
{n}"That is all we are giving you."{/n}
{n}"I could make the wording more encouraging."{/n}
{n}"Show us any changes first. Dress it up behind our backs, and you can tear out the page."{/n}
{n}He looks from her to you. Neither of you speaks. He reads the passage again, lays it atop his other pages, and crosses the old title out of his notes.{/n}
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
"I'm still angry about that letter. You've said your piece, and I've said mine. I won't keep hauling you back to this table for the same argument."''',
      c('"Walk with me for a while."', "company", flags=("seelah.letter_return_company",)),
      c('"I would rather walk alone for a while."', "space", flags=("seelah.letter_return_space",))),
    n("company", "Seelah", '''"Yes."
{n}She falls into step beside you. At the first turning, somebody hurries past carrying an unstable pile of folded cloth. Seelah moves aside, watches it tilt, and catches the top piece before it reaches the floor.{/n}
"There. A complete success. I shall have Halven give it a whole page."
{n}The carrier thanks her and goes on. Seelah's laugh comes out tired, but it is a laugh.{/n}
{n}She keeps pace beside you, her shoulder brushing yours as you turn down the passage.{/n}''', c('[Continue the walk.]', flags=("seelah.letter_return_addressed",))),
    n("space", "Seelah", '''"All right."
{n}She steps aside, her hand dropping to her sword belt.{/n}
"Thanks for seeing it through. Rotten evening, wasn't it?"
{n}She starts toward the other end of the passage, then looks back.{/n}
"Next time, let's talk about something else. I used to be good company, you know. I'll try to remember a story that doesn't end with me wanting to hit someone."
{n}She gives you a tired nod and heads down the passage.{/n}''', c('[Walk alone for a while.]', flags=("seelah.letter_return_addressed",))),
])
