"""Candidate continuation of an accepted, living post-Book5 Nurah romance.

New people, printing intrigue, and operations are authored fiction.
Physical delivery is provisional until the retained-actor helper is integrated.
No authored effect starts or completes a parent relationship or native quest.
"""
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
CAPITAL_NURAH = "f999fc37ddb225640b7f98c0a05d6948"
ETUDES = {
    "nurah.parent_romance": "9f655e252d334f04884f10188b0d8928",
    "nurah.parent_good": "91f7abac0d8e46e19ce8fc45fa3df58e",
    "nurah.parent_chaos": "f74eaab69b3d49d0a222eb1b2834777e",
    "nurah.parent_evil": "3d2d02611cd24f579e7b7b411b94263e",
    "nurah.parent_lich": "857c9366224c4b278fcc4ba3273b4b6b",
    "nurah.parent_queen": "c27a359a6e4e44b9b9cd9c0e54a1dd41",
    "nurah.dead_drezen": "a837c3bc9cbb4e846ab5565915165c91",
    "nurah.dead_camellia": "739b9fe9b8998c641b4b3dfed40bc217",
    "nurah.killing_mechanism": "20927a9471c00814b808fd69e88879c7",
    "nurah.prison": "c922e0cbe25a0cf4dad4ce7a3ca81935",
}
SEEN_CUES = {
    "nurah.camellia_disclosed": ["c2d5a4b359e17bc42aca9dc22b9369d3"],  # Camelia/Cue_0056
    "nurah.parent_finale_seen": ["f8a7511233524742bc42b25190609f4c"],
    "nurah.friedhelm_sold_seen": ["a81d2fc67aa9435999b2eba84eabf368"],
    "nurah.friedhelm_rich_seen": ["64bd5f9b742d4033b17f12b9b519970e"],
    "nurah.friedhelm_soldier_seen": ["5a06af413442436a88c2362c9e9dcbd0"],
}
BAD = ("nurah.dead_drezen", "nurah.dead_camellia", "nurah.killing_mechanism",
       "nurah.prison", "nurah.parent_lich", "nurah.closed", "inhuman")
BASE = ("nurah.parent_romance", "nurah.parent_finale_seen")
PERSONALITIES = ("nurah.parent_good", "nurah.parent_chaos", "nurah.parent_evil")
RELATIONSHIP = dict(
    Title="The borrowed author", Description="Nurah has found a new use for the reputation she stole from her old master.",
    Objective="Read Nurah's letter", Guidance="An existing romance and the accepted final tavern night are required. Courier replies can arrange a standing appointment in Drezen; physical meetings require Nurah's verified arrival.",
    StartedFlag="nurah.started", ClosedFlag="nurah.closed", CommittedFlag="nurah.complete",
    UnavailableFlags=list(BAD[:-2]) + ["inhuman"], FailureFlags=[])
SCENES = []


def f(*names):
    return tuple("nurah." + name for name in names)


def temperament(text, next, kind):
    key = "nurah.parent_" + kind
    return c(text, next, requires=(key,), forbids=tuple(k for k in PERSONALITIES if k != key))


def visit(id, title, nodes, previous, delay=12, remote=False, extra_requires=(), extra_forbids=()):
    contact = ("nurah.correspondence_available",) if remote else ("nurah.meeting_arrived", "nurah.meeting_accepted")
    SCENES.append(scene("nurah." + id, title, "Memory" if remote else "Nurah", 5, title, nodes,
        requires=BASE + contact + (("nurah." + previous,) if previous else ()) + tuple(extra_requires),
        forbids=BAD + ("nurah.meeting_declined", "nurah.meeting_withdrawn") + tuple(extra_forbids),
        delay=delay, optional=True, Relationship="nurah", Remote=remote,
        ContactUnit=None if remote else CAPITAL_NURAH, Areas=[DREZEN], Chapters=[5]))


visit("borrowed_name", "A book you did not commission", [
    n("start", "Narrator", '''{n}The messenger carries a cheap book wrapped in a sheet of fine paper. He has been instructed to wait for the wrapping, not the book.
Its title promises an account of the Fifth Crusade by Nurah Dendiwhar. Underneath, in smaller letters, it promises revelations concerning the Commander's private conduct. Someone has stamped a magnificent seal over the corner where the price ought to be.
Inside the front cover, in a hand you know, are the words: I did not write this. My obscenities are better.
The wrapper unfolds into a letter.{/n}
"Before you become interestingly angry, turn to page nine. No, the other page nine. There are two. The binder had a difficult afternoon.
"Someone has found an early edition of my account of Trezbot and decided that an author who made that man sound heroic could make anybody sound useful. They have added a few pages about you and offered to buy my corrections. This is how respectable people threaten a writer. They pretend the threat is an advance.
"I thought of sending them a correction with a poisoned spine. Then I read the offer properly. There may be something here worth taking before we ruin it.
"You have been rather good at the taking part. Occasionally at the ruining, too. Would you like to see how much trouble we can make with a book neither of us intends to praise?
"Send the wrapper back with your answer. Keep the book. If anyone catches you reading it, tell them you are investigating sedition. I find that makes the dirty passages much more convincing."
{n}Beneath the signature she has drawn a small arrow toward a paragraph about the virtues of obedience. The ink pressed hard enough to score the page.{/n}''',
      c('[Read the marked passage before answering.]', "passage"),
      c('[Inspect the offer concealed in the wrapper.]', "offer")),
    n("passage", "Narrator", '''{n}The marked passage describes Lord Axilar Trezbot's household as a school of character. Its servants supposedly emerged from instruction prepared to meet hardship with gratitude. A new footnote credits Nurah's later accomplishments to the discipline she received there.
The original account was written to make a dead man useful to its living author. This added note wants to make the dead man's ownership useful to somebody else.
Nurah has drawn a neat line through gratitude. Beneath it she has written: They forgot to ask the stick what it taught me.
The next page is less accomplished. It describes the Commander as a patron who recognizes obedience in every station of life, citing Nurah as an example. The author has mistaken her connection to you for a convenient illustration. A printed flourish occupies the space where a source ought to appear.
Between those pages is a sliver cut from a different sheet. It bears a printer's mark, a little bird with one raised foot. The words on its reverse are an instruction to delay the remaining copies until the author supplies her name in her own hand.
The messenger shifts his weight. He tells you he was paid to wait until sunset. If your answer takes longer, he will come back in the morning. His concern is the supper he will miss, not the book's account of your authority.{/n}''', c('[Ask what the proposed buyer wants.]', "offer")),
    n("offer", "Narrator", '''{n}The offer is from Istrene Vhal, a collector who has acquired papers from several Isgerian households and hopes to publish an account of their service in the crusades. She calls it a necessary correction to the fashionable ingratitude of former dependents.
Vhal proposes an authorial appearance before a small group of subscribers visiting Drezen. Nurah is to approve selected passages, authenticate a handful of documents, and permit her earlier biography to be republished with an additional dedication. There is money. There are introductions. There is a promise that the Commander's association with the project will be treated discreetly.
Nurah has circled discreetly and written: She has already printed your name.
The collector's local representative is an editor named Reth Carrow. He will receive revisions and arrange the subscribers' evening. Nurah proposes meeting you first, privately, to decide what to do with him. She has enclosed a smaller note for the courier to deliver if you agree.
It gives no place yet. She wants a way into Drezen that does not walk her past soldiers who remember the siege, and she means to walk it once herself before she trusts it.{/n}
"Do not send me an honor guard," {n}she adds.{/n} "If I wanted a row of men discussing whether I deserve to live, I would attend a temple. Name me a door nobody salutes. If I find a sentry on it, I shall assume you put him there to watch me, and I shall be right, and you will not see me again."
{n}The courier has a blank sheet, a clean reed pen, and the patient look of a man determined not to ask why the author of the book hates it.{/n}''',
      c('[Send her a door nobody salutes, and an invitation to use it.]', "sent"),
      c('[Keep the packet and put off your answer.]', "later"),
      c('[Tell her you will have no part of Vhal\'s book.]', "decline")),
    n("sent", "Narrator", '''{n}You write her the back stair that climbs from the kitchen yard to the private door of your chambers, which the clerks use to smuggle wine and nobody guards because nobody admits it exists. You add that she may come by it whenever the book gives her an excuse, and that you will not ask what she does with the excuse on the nights it doesn't.
You do not describe the stair. She will not believe a description; she will want to find the loose step herself.
The courier folds your reply into the wrapper and slips it beneath his coat. Before leaving, he asks whether the book should be delivered to the keep's shelves. You keep it beside you instead.
You leave a space after the hour for whatever insult she sends back. Its first page bears a printed signature that imitates Nurah's. The N is too careful. Whoever wrote it had time to practise and no reason to hurry through the name.
You turn back to the sentence about her exemplary obedience. The correction she wrote beneath it is almost small enough to miss, but the point of the pen has torn a hole through the final word.{/n}''', c('[Await her actual reply.]', flags=f("started", "invitation_sent"))),
    n("later", "Narrator", '''{n}You tell the courier that the reply must wait. He takes the empty wrapper and asks whether he should return for an answer another day. You tell him he may.
The book stays on your table, open at the other page nine.
Before the messenger leaves, he turns the volume facedown. Asked why, he points to the seal on its cover. It has left a dark circular stain on every other parcel he carried.
"Fine ink," he says, with a look which suggests he has heard fine promises before.
You put a spare sheet beneath it. Nurah's drawing of the little bird remains between the two copies of page nine.{/n}''', c('[Leave the invitation unanswered.]', abort=True)),
    n("decline", "Narrator", '''{n}You send the offer back with one line across the top of it: you will not put your name, or your door, anywhere near Istrene Vhal's book. You add a second line underneath, for Nurah, that has nothing to do with the book at all.
The courier reads the address on the outside, carefully avoiding the words beneath, and secures it in his case. He has been paid to carry an answer, not obtain a favorable one.
You keep the book long enough to cut the false signature out of its opening page. The cut leaves an awkward gap below the title. It is less elegant than the forgery and more accurate.
Whatever Nurah does to Vhal now, she will do it without you, and she will probably do it better out of spite.{/n}''', c('[Stay out of Vhal\'s book.]', flags=f("meeting_declined"))),
], None, delay=0, remote=True)


visit("invitation_reply", "The answer in the margin", [
    n("start", "Narrator", '''{n}The reply arrives in the hands of a different courier, an older woman carrying a basket of mended gloves. She produces Nurah's letter from beneath a patchwork mitten and waits while you check the seal.{/n}
"She said you might be suspicious," {n}the woman says.{/n} "I told her I would charge extra if the suspicion involved a search."
{n}Nurah has written on the back of your own invitation. She has struck out a sentence about discretion and replaced it with something more specific: nobody is to announce her name to a room full of strangers.{/n}
"A cloak is not a miracle," {n}the reply begins.{/n} "I have walked your stair. The fourth step from the top squeals; I have put candle-wax on it, and if it squeals again I shall know somebody scraped the wax off, and who. I will use your door on one condition: nobody makes the meeting into a spectacle. That includes you, on the evenings you have had a very clever idea.
"I will come when I send word that I am coming, and not otherwise. If you ever send a man to fetch me, he will find a room with nobody in it and a very rude note on the pillow.
"Now to the interesting part. Carrow sent me a sample of the dedication. It thanks my former master for discovering the talent that would otherwise have wasted itself in idleness. You may imagine the notes I have made in the margin.
"I have decided to hear his offer. I have not decided to let him finish it. Come prepared to give me a reason."
{n}Underneath she has added a postscript in a smaller hand.{/n}''',
      temperament('[Read the postscript about a name she refuses to print.]', "good", "good"),
      temperament('[Read the postscript about the subscribers\' expectations.]', "chaos", "chaos"),
      temperament('[Read the postscript about what the offer is worth.]', "evil", "evil")),
    n("good", "Narrator", '''"There is a name in the enclosed sample. A woman who carried Trezbot's accounts before I did. Istrene calls her a grateful retainer. I knew her as someone who could make half an onion last through a punishment.
"Do not look for a public appeal underneath this. I am not asking you to commission a monument to her suffering. I do not even know whether she is alive. I want to know who supplied her name and what they intend to sell with it.
"If your next thought was to tell me that at least people will hear her story, swallow it. They are being offered somebody else's lie with her name nailed to the front.
"There. Now you know which part has spoiled my mood. You may bring something to improve it, provided the something does not rhyme with forgiveness."
{n}The postscript ends with a scratched-out word. Beneath it, still legible, was please. Nurah has replaced it with an arrow directing your attention to the proposed meeting time.
The courier asks whether there is a reply. Her gloves are intended for people who will notice their absence before they notice the finer points of literary ownership.{/n}''', c('[Turn to the last lines of her letter.]', "terms")),
    n("chaos", "Narrator", '''"Carrow expects an author terrified of losing her reputation. I cannot decide whether to send him one or let him meet me. The first would be easier to write. The second ought to be more educational.
"Vhal has invited subscribers who want to hear that their ancestors were indispensable. There is probably no gathering in the city with more money and worse judgment. I would hate to waste it by giving them a simple scandal they can agree to suppress.
"Bring whatever expression you use when deciding to do something entirely unwise. I want to see whether I can distinguish it from the expression you use when somebody else is watching.
"And no, this is not a coronation. If we start handing out titles every time somebody pays for a drink, the titles will become less valuable than the drinks."
{n}She has drawn an alternative seal beside Vhal's: a fat purse trying to swallow its own string. The detail is careful enough to suggest she spent more time on it than on the polite reply enclosed for Carrow.
The courier turns the basket on her arm. Nurah has paid her for one return journey, and she intends to know where she is returning before she sets off.{/n}''', c('[Turn to the last lines of her letter.]', "terms")),
    n("evil", "Narrator", '''"Do not arrive with a scheme to spend the money before I have stolen it. Vhal's offer is good. That is the insulting part. She thinks the right sum will make me grateful for another opportunity to write what a better-dressed fool tells me to write.
"I may take the sum anyway. Gratitude costs extra.
"Carrow has copies of papers I would like to possess. Vhal has a distribution business I would like to hurt until it becomes useful. You have a name that makes people mistake an invitation for an instruction. I think there is a pleasant evening somewhere among those advantages.
"You may tell me I am being greedy. I will accept the observation as evidence that you have been paying attention. If you intend to tell me I have enough already, do us both a kindness and postpone it until I am holding a knife suitable for cutting the subject short."
{n}The blade she has drawn in the margin pierces a little moneybag, and the coins falling out have faces. One looks very much like the printed portrait on Vhal's sample.
The courier glances toward the door. The people waiting for her mended gloves are unlikely to enjoy the joke as much as its author did.{/n}''', c('[Turn to the last lines of her letter.]', "terms")),
    n("terms", "Narrator", '''{n}Her letter names a night, an hour, and your stair. Everything else in it is about Carrow.
The courier waits while you consider it, turning her basket to keep its repaired gloves out of the draft.
At the bottom of the sheet, below the business about discretion, Nurah has written one last sentence: I am looking forward to seeing whether you kiss me before asking about the book.
She has left no space beneath it for a written answer.{/n}''',
      c('[Write back: the night, the hour, and the stair.]', "accepted"),
      c('[Ask for a later night; the war has this one.]', "wait"),
      c('[Write back that you will not meet her over Vhal\'s book after all.]', "withdraw")),
    n("accepted", "Narrator", '''{n}You write the night and the hour back under hers, and the one word "stair", and return it by the courier. She makes you place the reply beneath the correct glove so that she can produce it without emptying the basket.
When she leaves, you are left with the book and Carrow's sample dedication. You do not put Nurah's name on any roster, any gate list or any sentry's orders. She would find out.
You turn to the dedication again. Its printer has left a space for her approval beneath the sentence about talent rescued from idleness. Nurah's correction fills that space completely.
The first word would have cost a soldier a reprimand. The rest would have earned a much more interesting conversation.{/n}''', c('[Wait for her on the night she named.]', flags=f("meeting_accepted"))),
    n("wait", "Narrator", '''{n}You ask the courier to carry word that the night she named belongs to the war, and that you want another. She accepts the message without asking for a reason.
Nurah's letter stays on your desk, with the candle-wax on the fourth step still unscraped.
The messenger secures the basket's cloth and goes back to her other deliveries. Under the book's loose cover, Vhal's portrait looks serenely unaware that its proposed author has drawn teeth on it.{/n}''', c('[Leave confirmation pending.]', abort=True)),
    n("withdraw", "Narrator", '''{n}You write that you will not meet her over Vhal's book, and you scrape the candle-wax off the fourth step yourself so that she will know you meant it. You do not explain. She would only correct the explanation.
The courier folds the message into a small square and places it beneath the patched mitten.
You close the book. Its binding makes a faint crack where the duplicate page has been forced against the spine. Someone tried to fit too much into a cover that had already been chosen.{/n}''', c('[Send it.]', flags=f("meeting_withdrawn"))),
], "invitation_sent", remote=True)


visit("the_author_arrives", "The author arrives", [
    n("start", "Narrator", '''{n}Nurah waits at the private doorway of your chambers. Her cloak is plain, its hood lowered only far enough for you to see her face.
She looks past you before looking at you. From the passage comes the rattle of a tray being collected. Nurah waits until the sound has receded.{/n}
"No procession. No herald. I was afraid you would be tempted to improve the arrangement."
"If you hired trumpeters, tell them to stand in front of Vhal when they miss a note."
{n}She takes the book from under your arm without asking, opens it to the false dedication, and wrinkles her nose. Then she looks up at you.{/n}
"You asked about neither the book nor the letter. That leaves the other part of my question."
"You were holding it where it inconvenienced me."
{n}She closes the volume with a soft thump against your chest. Her free hand catches the edge of your coat, drawing you down toward her.{/n}''',
      c('[Kiss her before she can improve the invitation.]', "kiss"),
      c('"Show me whether you have brought your own corrections first."', "corrections")),
    n("kiss", "Nurah", '''{n}Nurah meets you halfway. Her fingers tighten on your coat, then slide upward until they rest along your jaw. A servant turns into the passage behind her, carrying an empty tray. She breaks the kiss just long enough to turn a blandly polite smile toward him.
He recognizes the Commander and makes a clumsy attempt to straighten. Nurah has pulled her hood forward before he can take a closer look.{/n}
"Good evening," {n}she says, in a voice so harmless that you nearly laugh.{/n} "The Commander is helping me with a difficult passage."
{n}The man wishes you luck and hurries away. Nurah waits three breaths, then leans against you, laughing into your coat.{/n}
"I thought he was going to offer to hold the book."
"He would have been slow with that too."
{n}She puts the volume back into your hands and straightens the part of your coat she has crushed. Her thumb stays at the collar for a moment longer than the task requires.{/n}
"That will do for the greeting. I have something you ought to see before I decide whether to burn it."
{n}She steps inside and closes the door. From her satchel she takes a second copy of the same book.{/n}''', c('[Compare the two copies.]', "two_copies", flags=f("first_kiss"))),
    n("corrections", "Nurah", '''"Oh, a demanding reader. I had hoped to distract you before we reached the difficult words."
{n}She produces a second copy from her satchel and holds it beside yours. Its edges have been trimmed neatly. The imitation signature is identical down to the last, overcareful stroke.{/n}
"I have corrected this one. The editor has not thanked me yet."
"A sample. If he wants the rest, he can arrange to disappoint me in person."
{n}You reach for her copy. She holds it behind her back.{/n}
"Now you want the one I am holding. You could have said so before making me wonder whether I chose the wrong coat."
"Underneath. I refuse to explain every layer before you have made an effort."
{n}You step closer. She lifts her chin, watching you decide whether to reach for the book or her. When you put a hand lightly against her shoulder, she catches your fingers and kisses their tips.
Then she gives you the second volume, briskly enough to suggest she has remembered an appointment of her own.{/n}
"Read. We can be distracting afterward."''', c('[Open her corrected copy.]', "two_copies", flags=f("first_teasing"))),
    n("two_copies", "Narrator", '''{n}Nurah has not merely crossed out the false dedication. She has replaced its flattering phrases with notes on the kinds of error a wealthy subscriber is likely to overlook. A date has moved by three years. A campaign has acquired a commander who was dead when it began. A servant who carried a message has become the lord who dictated it.
She has left the imitation of her own signature untouched.{/n}
"That is the useful part," {n}she says.{/n} "If we only tell Carrow he forged a name, he will say the printer made a mistake. If we ask him to defend the chapter, we may find out who told him which mistakes to make."
"Tell him I noticed. Not how much."
{n}A gust lifts the loose dedication page. Nurah traps it against your arm, her hand flattening over the line about obedience.{/n}
"I wrote enough lies for Trezbot while he was alive. I have no intention of letting this woman own the profitable ones now that he is dead."
"I intend to write plenty of things. This is about the one she has decided I already wrote."
{n}She folds the page along an existing crease, once, then again. The paper is thick and resists the second fold.{/n}''',
      temperament('"The name in your letter. What have you learned about her?"', "good", "good"),
      temperament('"How many subscribers can we make defend contradictory versions?"', "chaos", "chaos"),
      temperament('"You have already decided what you want to take from Vhal."', "evil", "evil")),
    n("good", "Nurah", '''"Bressa. That is her name. Not 'the grateful maid.' Not 'a trusted dependent.' Bressa."
{n}The second fold tears. Nurah looks at it as though the paper has chosen an inconvenient moment to be weak.{/n}
"She carried accounts between houses in Isger. She knew which doors opened for a delivery and which ones opened because somebody had been told to make an example. She taught me to hear the difference in a latch."
"Does Vhal have her testimony?"
"She has a sentence. Bressa supposedly said that service in Trezbot's household gave her a purpose. It sounds like something you could make a woman say while standing between her and a meal."
{n}Nurah tucks the torn dedication inside the book instead of dropping it.{/n}
"I have sent a question through an old contact. It may come back unanswered. If it does, we do not turn that into a convenient death. I want to know who supplied the sentence."
"We can ask Carrow."
"He will lie. That is why I want you there. You have a remarkably useful face when somebody believes you are about to be reasonable."
{n}Her fingers brush your sleeve. She studies your expression and gives a short, reluctant smile.{/n}
"There. Nearly perfect. You should save it for him."''', c('"Then let us find the lie he is prepared to defend."', "plan")),
    n("chaos", "Nurah", '''"Enough to make the room worth attending. I have already found two dedications that describe the same battle as the exclusive achievement of different families."
"You have two?"
"Carrow sent one to the author he expects me to be. I asked a bookseller what he was offering everybody else. It was a very educational errand."
{n}She takes a small folded prospectus from the book's spine and lets you see the second family's name.{/n}
"This one wants their ancestor to have devised the retreat. That one wants theirs to have held the line. Neither has noticed the line was abandoned before the retreat was ordered."
"You could tell them."
"I could also throw the wine away before they arrive. Why waste a perfectly good evening?"
{n}She moves the two dedications like cards, exposing one name and hiding the other.{/n}
"If we do this well, each of them will insist on the part of the truth that ruins the other. I may not have to say anything at all."
"You would find that difficult."
"Painfully. You can admire my discipline afterward."
{n}She smiles up at you, bright with the prospect of people making fools of themselves while trying to buy a better history.{/n}''', c('"First we need to know which version Carrow believes he can sell."', "plan")),
    n("evil", "Nurah", '''"Her copies. Her subscribers. Whatever makes her think she can print my name and invite me to negotiate the price afterward."
"You cannot take a reputation off a shelf."
"No, but you can make someone pay to stop you reading its contents aloud."
{n}She turns the book so that Vhal's printed seal faces you. Someone has scraped the center away with a small blade, leaving the proud border surrounding an empty space.{/n}
"I could cut the supply of corrections, embarrass her editor, frighten the printer. She expects those things. She has probably decided what she can afford to lose. I want the thing she thinks nobody has noticed."
"Which is?"
"She is selling different families the right to be indispensable. Somewhere she has written down what each one was promised. I would like to read that list. Then I would like them to know I have read it."
{n}Nurah closes her hand around your wrist, guiding your finger over the hollow seal.{/n}
"You look as though you are calculating something. I hope it is the price of being quiet rather than the pleasure of advising me to be satisfied."
"You would not be satisfied."
"Now you are remembering why we enjoy each other."''', c('"Then Carrow is the first person who needs to underestimate us."', "plan")),
    n("plan", "Nurah", '''"He wants an interview with the author. He can have one. I will decide how much author he survives hearing."
{n}She has arranged for Carrow to send a proof of the disputed chapter before the subscribers' evening. The sheet will be brought to the same appointment by a compositor named Sava Lorn, whom the editor trusts to keep her mouth shut about work.
Nurah has already asked the woman to stay long enough to discuss the printing. Carrow does not know that part.{/n}
"I am going to need you to do something difficult," {n}she says.{/n}
"Listen?"
"Worse. Let him think he has pleased you before he learns what you noticed."
{n}Footsteps pass outside. Nurah glances at the closed door, her hand resting on your wrist until they fade.{/n}
"I will come back with the proof," {n}she says.{/n} "We can decide how to dress the lie once we know where it is weakest."
"And the book?"
"Keep both. If you lose the corrected one, I will expect you to remember every insult."
{n}She gives your wrist a final squeeze and lets go. Before leaving she listens at the door, then takes the quieter passage away.{/n}''', c('[Keep the copies and prepare to examine Carrow\'s proof.]', flags=f("first_meeting_finished"))),
], "invitation_reply")


visit("a_page_with_teeth", "A page with teeth", [
    n("start", "Narrator", '''{n}Nurah has a visitor waiting with her: a broad-shouldered human woman with ink ground into the creases of her hands. A covered bundle rests against her boot. When you arrive, the woman straightens without bowing.
"Sava Lorn," she says. "I set the lines. I do not choose them."
Nurah tilts her head.{/n}
"What a useful sentence. Have you considered putting it on the cover?"
"I have considered putting it on every bill Mr. Carrow refuses to pay."
{n}Sava unwraps a printer's proof and smooths it against the bundle. The page is crowded with corrections in two inks. One hand wants a sentence made more flattering; another wants the name of a witness removed. Neither has initialed the change.
Nurah gives you a clean copy. Sava retains the marked one.{/n}
"He told me to take your corrections and leave," {n}the compositor says.{/n} "He did not tell me how long you would take to make them."
"An encouraging omission," {n}Nurah says.{/n} "We may be able to work with it."
{n}The disputed paragraph describes a retreat near the Worldwound. Its date is written out in full. Beneath it, a footnote cites a supply book and the name of a commander. Nurah places a scrap beside the page: a copied entry from that supply book, with a change of command recorded at its head.
She rests one finger on the two dates and waits.{/n}''',
      c('[Compare the dates and the authority named in the two accounts. Knowledge: World, DC 31.]', check=dict(Skill="SkillKnowledgeWorld", DC=31, Success="chronology", Failure="wrong_year", CommanderOnly=True)),
      c('"You have already found something. Tell me what you want to do with it."', "her_error")),
    n("chronology", "Nurah", '''{n}The proof has preserved the date of an order and given it to the officer who succeeded its author. The supply book distinguishes the two appointments. The printed account does not.
You turn the copied entry so Sava can see the heading and point out the change. She reads it twice.{/n}
"That footnote was added yesterday," {n}she says.{/n} "It was not in the first copy."
"Whose correction?" {n}you ask.{/n}
"Carrow brought it. The writing was already on the sheet."
{n}Nurah's smile has narrowed. She takes the clean proof from you, holds it against the marked one without touching Sava's copy, and compares the spaces left for the missing witness.{/n}
"Somebody wanted the old commander gone and his successor in the room," {n}she says.{/n} "It is a remarkable improvement for a man who arrived after the retreat."
"An error they may correct if we point it out now."
"Then we will point at something else. Sava, tell your editor I object to the word exemplary. It is lazy."
{n}Sava copies that complaint in the margin, leaving the useful error untouched. Nurah catches your eye while the compositor is writing.{/n}
"You found the interesting one. I was afraid you would stop at the bad prose. There is so much of it to choose from."''', c('[Keep the hidden chronological defect for the interview.]', "witness", flags=f("chronology_kept"))),
    n("wrong_year", "Narrator", '''{n}You begin with the date in the proof, treating the adjacent name as the officer who held command at the time. Sava glances at Nurah. Nurah reaches across and puts a finger over the later appointment in the supply book.{/n}
"That is his successor," {n}she says.{/n} "Read the heading."
{n}The mistake becomes plain. Sava has already written the opening of your objection on the correction sheet. She draws a line through it.{/n}
"I cannot take that line off the paper," {n}she says.{/n} "He numbers the sheets. If I return a clean one, he will ask for this one."
"Let him ask," {n}Nurah says.{/n}
"He will ask me."
{n}Nurah looks at the scored-out words, then at the copied entry. Her jaw tightens.{/n}
"Fine. Tell him we were looking at the date. He can waste an evening working out how much we noticed."
"He will check it."
"I know."
{n}She gives the proof back to you. The useful omission is still there, but the editor will know where to look before he sees you again.{/n}
"We can make him talk about the revision," {n}Nurah says.{/n} "It would have been more entertaining to watch him defend the original. Do not offer to apologize to the paper. It has suffered enough."''', c('[Let the visible correction warn Carrow; prepare for a revised defense.]', "witness", flags=f("editor_warned"))),
    n("her_error", "Nurah", '''"I want him to explain a little miracle. His officer has managed to command a retreat before being given command."
{n}She lays the supply entry across the proof. You can see the succession now: one officer in the heading, another beneath the later appointment. The printed account has given the second man the first man's order.{/n}
"You could have told me that immediately."
"Yes. And missed the pleasure of watching you decide whether to ask."
{n}She takes a pencil from Sava, adds a complaint about the adjective exemplary, and returns it. The compositor copies the harmless objection without asking about the dates.{/n}
"Now I want to choose our first question at the interview," {n}Nurah says.{/n} "Carrow will be expecting you to ask about your own reputation. I want to ask him who died before this officer arrived."
"You have a name?"
"The name of the woman whose account he removed. It is still visible under the correction on Sava's sheet."
{n}Sava turns the marked proof slightly away. Nurah stops reaching for it.{/n}
"You may look," {n}Sava says.{/n} "You are not keeping it."
"I was going to ask very charmingly."
"You were going to fold it into the other one."
{n}Nurah grins, caught and unashamed.{/n}
"Then we had better both be careful. I will ask the first question. You may watch whether he looks at you or the door."''', c('[Let Nurah control the first question and retain the unexposed flaw.]', "witness", flags=f("nurah_leads_interview"))),
    n("witness", "Narrator", '''{n}Sava lays her proof flat again. A name remains faintly visible beneath the removed footnote: Bressa. Nurah has stopped smiling.{/n}
"The sentence was longer in the first copy," {n}Sava says.{/n} "It described a woman sent back along the road to recover a case of papers. She was missing when the rest reached the next camp."
"Missing," {n}Nurah repeats.{/n}
"That is what it said."
"And now she is grateful."
{n}The compositor's fingers close around the edge of the page. You notice a band of clean skin where a ring has been removed.{/n}
"I did not write it."
"You set the lines. We have established that."
{n}Nurah's voice is quiet enough that Sava has to lean forward to hear it. The halfling lifts the clean proof and holds its new footnote beside the erased name.{/n}
"Who brought the first copy?"
"A messenger from Vhal's agent. I never saw the woman."
"Does Carrow still have it?"
"In a locked case. With the subscriber list. He says it is the only part of the project worth protecting."
{n}Nurah looks at you, then slides the clean proof underneath Sava's hand, preventing her from wrapping the bundle without moving it.{/n}
"That case," {n}she says.{/n} "I want it open."''',
      c('"Give us a way to see it. You will be paid for the work and kept out of the public accusation."', "paid_help"),
      c('"Carrow will blame the printer if this fails. Help us, and we can put his own corrections in front of him."', "shared_danger"),
      c('"Return the proof. We will find our own way into his case."', "leave_sava")),
    n("paid_help", "Sava", '''"I want what he owes me first. Three weeks of wages and the paper I bought when he said he would reimburse me. I can show you the bills."
{n}Nurah makes an impatient movement. You wait. Sava takes a narrow roll from inside her sleeve and flattens it beside the proof.
The sum is written at the bottom, with each late payment marked above it. Nurah reads down the marks.{/n}
"He is paying subscribers' expenses with your wages," {n}she says.{/n}
"I know what he is doing. I want to stop financing it."
{n}Nurah counts coins from her own purse. She pays the arrears recorded on the roll, then pushes the purse closed before Sava can mention the paper.{/n}
"The paper when you bring what you promised. I am not buying a second promise on the strength of the first."
"You are not Carrow."
"Correct. You may find me considerably more irritating."
{n}Sava counts the coins without apologizing. In return she describes the case's brass clasp, its false bottom, and the editor's habit of leaving a key on a cord beneath his waistcoat. She will make sure the first proof remains in that false bottom until the interview.
Nurah lets her gather the pages. When Sava has gone, she holds out the lightened purse for you to feel.{/n}
"A generous decision. You may owe me something enjoyable before the end of it."''', c('[Keep Sava\'s paid assistance and Nurah\'s purchase on record.]', flags=f("proof_examined", "sava_paid"))),
    n("shared_danger", "Sava", '''"You think I have not noticed? He makes me initial every sheet he dislikes and signs none of them himself."
{n}She opens the bundle and shows you a folded dedication. Carrow has approved it in a different ink beneath the compositor's mark. Sava has kept it wrapped separately from the copies intended for delivery.{/n}
"One time he forgot. I told him I needed his signature to order a different paper. He was in a hurry."
{n}Nurah looks almost delighted.{/n}
"I begin to like you."
"You may like me after I have been paid."
"One ambition at a time."
{n}Sava lets you copy the signed sentence and describes the false bottom of Carrow's case. She will leave the old proof there through the interview. She will not remove it herself. If Carrow searches his case and finds it gone before you arrive, he will know who last handled it.
Nurah objects. Sava begins wrapping the bundle. The halfling lets the objection die before the last fold closes.{/n}
"All right. We will open it. Keep your signed dedication somewhere he cannot burn it while apologizing."
{n}Sava nods once. She has left with her wages still unpaid, and she makes sure Nurah remembers that before she goes.{/n}''', c('[Keep the shared evidence and Sava\'s limited cooperation.]', flags=f("proof_examined", "sava_evidence"))),
    n("leave_sava", "Nurah", '''{n}Nurah takes her hand off the proof. Sava wraps it before she can reconsider.{/n}
"Tell Carrow we are interested," {n}the halfling says.{/n} "Use whatever tone makes him most pleased with himself."
"That will not be difficult."
{n}The compositor carries the bundle away without giving you the case's construction or the place where Carrow keeps its key. Nurah watches her go.{/n}
"You have left us with more work."
"I do not want her carrying our plan back to him."
"Then we had better perform it well enough that she wishes she had asked to join us."
{n}Nurah turns the clean proof over, finding a streak of ink where Sava's thumb pressed it.{/n}
"He keeps the first copy in his case. We know that much. I will have to find the clasp while you keep his attention. If it takes longer than you expect, say something expensive. Men like Carrow will listen to an expensive idea long after they have ceased to understand it."
{n}She folds the proof into her satchel and looks up at you.{/n}
"I hope you will enjoy being the distraction. I certainly intend to."''', c('[Proceed without the printer\'s assistance.]', flags=f("proof_examined", "sava_uninvolved"))),
], "first_meeting_finished")


visit("the_borrowed_audience", "An audience in borrowed clothes", [
    n("start", "Narrator", '''{n}At the next appointment Nurah takes one look at your clothes and makes a noise of profound disappointment.{/n}
"You look like the Commander," {n}she says.{/n}
"A difficult habit to break."
"We are not trying to convince Carrow you are somebody else. We are trying to convince him you are a particular kind of fool. There is a difference."
{n}For the rehearsal she has borrowed a small room near the tavern. She leads you there from the appointment, shuts the door, and sets two chairs on opposite sides of a narrow table. A third stands against the wall with a coat hanging over it.
She pushes the better chair toward you, then pulls it back when you reach for it.{/n}
"Too eager. Let him offer. People who pay for importance expect to be kept waiting just long enough to notice how expensive the wait is."
"Have you been practicing my entrance?"
"I have been improving it. Your actual entrance tends to involve someone saluting and another person wishing they had tidied the floor."
{n}She steps onto the lower rung of her chair so she can adjust your collar without asking you to bend. Her fingertips are warm against your neck. When you turn toward her, she taps your chin with the folded prospectus.{/n}
"Later. I want this particular piece of vanity fitted properly first."
{n}On the table she has laid three possible introductions. One presents you as a patron interested in an authorized account. Another offers a discreet purchase of Vhal's embarrassing original materials. Beside the third lie two dedication proofs, each promising a different household the exclusive honor of sponsoring the edition. Nurah taps the repeated word exclusive. The third introduction turns the subscriber invitations themselves into the subject of the meeting.{/n}''',
      c('"I will play the patron who wants a flattering account. Show me where I look too pleased."', "patron"),
      c('"Let him think I want the damaging papers for myself."', "buyer"),
      c('"Invite him to explain why both rival patrons own the same exclusive dedication."', "double", requires=("trickster",)),
      c('"You already have a crown. Make him explain why he printed your approval before asking his queen."', "queen", requires=f("parent_queen"))),
    n("patron", "Nurah", '''"Sit. Try not to look as though you have rescued the chair from a burning building."
{n}She takes the place opposite you and changes her expression. Her back straightens, her smile softens, and for a moment the old court historian sits before you with a page full of diligent notes.{/n}
"An invaluable opportunity, Commander. Posterity is so easily misled by those who were never present at the great events. A volume under your protection would reassure many anxious families."
"Which families?"
{n}The smile disappears.{/n}
"Too fast. A vain person asks where their own name will appear before asking whose money paid for the ink."
"I do have some experience with vanity."
"Then use it. Tell me what you want them to write."
{n}She rests the pen against her lower lip, waiting. You give her a sentence about the army's confidence. She shakes her head. You add the Commander's exceptional judgment. Her mouth begins to curve.{/n}
"There. You almost believe it. Another adjective and I shall have to open a window."
{n}She circles the line you have supplied. In the interview you will let Carrow offer the dedication before turning his dates against him. Until then, Nurah will be the author whose temper you appear willing to manage.
She sees you glance at that last sentence.{/n}
"Appear. If you forget the distinction, I will correct you in front of him."''', c('[Rehearse the vain patron until the false interest holds.]', "test", flags=f("cover_patron"))),
    n("buyer", "Nurah", '''"Good. People trust greed much sooner than they trust curiosity. Greed has a number they can argue with."
{n}She pushes the coat-covered chair toward you. You discover a folded page pinned inside the sleeve: Carrow's request for a discreet meeting about materials that may prove distressing to certain patrons.{/n}
"He sent this after the offer. He is already considering a second buyer."
"He expects us to betray Vhal."
"He expects us to pay him for helping us betray Vhal. Do not deprive him of his expertise."
{n}Nurah sits on the table's edge and lets one foot swing above the floor.{/n}
"Tell me why you want the original papers."
"They could embarrass people whose support I may need."
"Boring. Accurate enough. Now tell me why he should prefer selling them to you over keeping them against her."
"Because I can make his next buyer wonder whether there is another copy."
{n}Her foot stops swinging. She studies you, then pulls the letter free of the sleeve.{/n}
"That one is good. Keep it. Do not smile when you say it."
"You are smiling."
"I am enjoying myself. You are purchasing a difficulty. It is a solemn occupation."
{n}She jumps down and gives you the page. Her shoulder brushes your thigh as she passes, and she takes a little longer than necessary to move the chair out of your way.{/n}''', c('[Rehearse the interested buyer.]', "test", flags=f("cover_buyer"))),
    n("double", "Nurah", '''"We would need both invitations. He will claim one is a printer's draft if he only has to look at a copy."
"Then ask both patrons to have their representatives confirm the wording before the subscribers' evening. Separately."
"At the same appointment."
"With Carrow."
{n}Nurah presses the blank side of the prospectus against the table and starts writing. She leaves a broad space between two proposed arrival times, then crosses it out.{/n}
"No. If we stagger them, he can tell the first man that the second is mistaken. Let them arrive together, each carrying the exclusive dedication he paid to approve."
"Will they agree?"
"A man who has bought an exclusive privilege will usually travel a considerable distance to make sure somebody else has not been given it for free."
{n}She reads the invitation aloud in a brisk, officious voice. The authority in it belongs to the appointment itself: the editor must reconcile the submitted wording before the Commander can endorse the edition. She has promised no endorsement.{/n}
"He may refuse," {n}you say.{/n}
"Then he tells both men he cannot put their claims beside each other. That is also an answer."
{n}She holds the page up for you to see, but takes it back when you reach for it.{/n}
"I am sending these. If either representative asks who arranged the collision, I want to have the pleasure of being difficult to find."''', c('[Send the incompatible claims to the same appointment.]', "ready_double", flags=f("cover_double"))),
    n("queen", "Nurah", '''{n}Nurah puts down the prospectus. Slowly, she smiles.{/n}
"That would be rude. Using a title for something other than persuading people to buy another drink."
"He has printed the title when it suits him. He can answer to it when it does not."
"He will ask for a public audience. A painting for his little book, with himself standing beside the throne. We would never get rid of the engravings."
{n}She takes the pencil and writes a short refusal on the back of the invitation. The meeting will remain private. The editor may bring the disputed originals and explain which authority he believed he had to publish a royal dedication before obtaining approval.{/n}
"I am not going to sit at the end of a row of soldiers while he performs his astonishment," {n}she says.{/n} "If he wants to address a queen, he may do it in a room small enough that I can hear him swallow."
"You enjoyed deciding that."
"I am beginning to understand why people defend hereditary privilege so enthusiastically. It saves them from having to be interesting before they are obeyed."
{n}She places the completed refusal in your hand and curls your fingers over it.{/n}
"This time I intend to be both. Do try to keep up."''', c('[Keep the audience private and use the actual earned title.]', "ready_queen", flags=f("cover_queen"))),
    n("test", "Nurah", '''{n}Nurah puts the two clean proofs between you. One bears the flattering dedication. The other contains the line that gives a retreat to a commander who had not yet arrived.
"Again," she says. "This time I am Carrow, and I have decided you are easier to flatter than to inform."
She praises your insight, your patience, and the exceptional fortune of being allowed to profit from either. On the word fortune she slides the flattering sheet toward you and rests her other hand over the disputed date.
You have to keep her talking without looking at the place she is concealing.
She knows exactly where you want to look. That is why she keeps moving her hand.{/n}''',
      c('[Maintain the false interest while she tries to break your attention. Bluff, DC 32.]', check=dict(Skill="CheckBluff", DC=32, Success="held_cover", Failure="broken_cover", CommanderOnly=True)),
      c('"We should use my reputation openly. Let him worry about refusing to bring the originals."', "open_pressure")),
    n("held_cover", "Nurah", '''{n}You let her finish, ask about the size of the dedication, and wonder aloud whether the portrait should show the Commander at a desk or on horseback. Nurah offers to have you painted atop a dragon. You ask whether that would distract from the title.
Her laugh breaks the performance before yours does.{/n}
"Stop. If you say one more word, I will have to believe somebody actually commissioned this."
{n}She takes her hand off the date. You have kept her attention on the flattery long enough to see how she conceals the page beneath it.{/n}
"That will work. If Carrow has any sense, he will begin worrying after he has already opened the case."
"You were supposed to be difficult."
"I was. You became embarrassing. It is a surprisingly effective defense."
{n}She reaches for the papers. You catch the flattering one first and read her absurd addition about the dragon aloud. Nurah lunges for it, one hand braced on your knee, and tears the margin rather than let you finish.
For a moment neither of you moves. Then she kisses you, hard enough to make the chair creak when you draw her closer.{/n}
"Practice is over," {n}she says against your mouth.{/n} "Do not use that voice again until somebody is paying to hear it."''', c('[Use the rehearsed deception at the interview.]', flags=f("audience_ready", "cover_held"))),
    n("broken_cover", "Nurah", '''{n}Your eyes follow her hand. Nurah stops speaking in the middle of a compliment and lifts the concealed sheet.{/n}
"There. He sees that, and the case stays shut."
"You knew what I was looking for."
"So will he. It is his forgery."
{n}She separates the pages and puts the marked proof underneath the clean one. The new arrangement hides the date entirely.{/n}
"We can still get him to talk. I will interrupt when he begins to retreat into compliments. You keep him answering long enough for me to look at the clasp."
"You make that sound easy."
"It is not. You have made it harder."
{n}She lets the words stand. When you reach for the clean proof, she gives it to you without another demonstration.
You try the entrance once more. She corrects the first sentence, then the way you wait for a reply. By the time she is satisfied, the light at the window has changed and she has abandoned the idea of an unhurried evening.{/n}
"Next time," {n}she says, collecting the papers.{/n} "Unless you intend to rehearse falling asleep in the chair as well."''', c('[Proceed with Nurah covering the weakness in the performance.]', flags=f("audience_ready", "cover_fragile"))),
    n("open_pressure", "Nurah", '''"That will get him through the door. It will also make him bring the least useful things he can call originals."
"Then we catch the substitution."
"We had better."
{n}Nurah changes the invitation. The Commander expects Carrow to bring the earliest proof and its supporting materials. She gives him no pretext to mistake the word earliest.
Then she scratches out the sentence about being delighted by the proposed edition.{/n}
"I will miss that sentence. It would have looked very good beneath the bill for his mistake."
"You can keep it for another occasion."
"I keep far too many things waiting for you to become unreasonable."
{n}She pushes the better chair back into place. This time she sits in it herself, stretching out her legs and letting you find somewhere else to stand.
The interview will begin with a demand rather than a deception. Carrow will have time to prepare for that demand, and Nurah makes you repeat which original you want before she lets the subject go.{/n}''', c('[Use open authority and expect a prepared answer.]', flags=f("audience_ready", "cover_open"))),
    n("ready_double", "Nurah", '''{n}She rereads both invitations, making a small change to one greeting and none to the other. The two claims now lead to the same place at the same time for reasons their owners will find entirely flattering.{/n}
"The dangerous moment is when they realize each has been promised something the other cannot permit," {n}she says.{/n} "If we let them quarrel only with each other, Carrow may escape with the case."
"So we keep him between them."
"Verbally, if possible. The room is rather small for wrestling."
{n}She measures the gap between the chairs with a glance, then looks at you with fresh amusement.{/n}
"Although you would make an excellent obstacle."
"I can be difficult to move."
"I know. I have had to work around it."
{n}She comes close enough to rest the two folded invitations against your chest, one on either side.{/n}
"There. Conflicting interests. You should be used to those by now."''', c('[Keep the deliberate collision and watch the editor\'s exit.]', flags=f("audience_ready", "cover_collision"))),
    n("ready_queen", "Nurah", '''{n}Nurah practices the opening once. She begins too grandly, stops, and starts again in her own voice.{/n}
"Mr. Carrow. You have put words in my mouth. I hope you brought enough money to pay for the ones I intend to use."
"That may not be the customary royal greeting."
"Good. He can write it down and improve his education."
{n}She folds the invitation without a seal. Carrow will have to read it before deciding which parts he wishes he had not seen.
The title will get you a guarded editor and an audience in which he cannot pretend he does not know who is asking. It will not open his case by itself. Nurah turns the practice clasp toward you and makes you work out where his hand must go when he unlocks it.{/n}
"Watch that," {n}she says.{/n} "Even kings have to put their keys somewhere. Queens, naturally, are less careless."
{n}She holds up the ribbon from your sleeve, which you had not noticed her untying, and drops it into her pocket.{/n}''', c('[Prepare for a guarded royal interview.]', flags=f("audience_ready", "cover_royal"))),
], "proof_examined")


visit("the_editor_opens", "The earliest surviving proof", [
    n("start", "Narrator", '''{n}Carrow has hired the back room of a wine merchant for the interview. Nurah meets you at the agreed appointment and takes you there by a side street. She has pinned her hair differently. When she catches you looking, she asks whether you expect a woman to be recognized by her crimes rather than her hairstyle.
The editor rises when you enter. His case is on the chair beside him. A little brass hook secures the lid; his hand rests on it until Nurah chooses the chair nearest the window.
"Madam Dendiwhar. Commander. I hope we may settle the unfortunate misunderstanding before it spoils an enterprise intended to honor you both."
"I have brought a pencil," Nurah says. "We should be able to spoil it very precisely."
She lays the clean proof on the table. Carrow looks at it, then at you. He has polished his boots but missed a spot of ink on the cuff of his coat.{/n}''',
      c('[Begin the rehearsed performance.]', "flattery", requires=f("cover_held")),
      c('[Let Nurah interrupt before the performance gives too much away.]', "interruption", requires=f("cover_fragile")),
      c('"Show us the earliest proof. We can discuss your intentions afterward."', "demand", requires=f("cover_open")),
      c('[Ask whether he is expecting any other visitors.]', "collision", requires=f("cover_collision")),
      c('[Let Nurah receive the editor under the title he printed.]', "royal", requires=f("cover_royal"))),
    n("flattery", "Nurah", '''{n}Carrow has prepared compliments, but you give him something easier to work with: questions whose answers might lead to money. How many subscribers? How expensive a binding? Could a portrait be changed without delaying delivery?
His hand leaves the case. He brings out a prospectus, then a larger sheet showing two possible arrangements for the title page. Nurah shifts in her chair as though bored. The movement puts her beside his elbow.{/n}
"The original authorial materials would naturally remain under our protection," {n}he says.{/n}
"Naturally," {n}you answer.{/n} "May I see what that protection has preserved?"
{n}He produces a key from his waistcoat. Nurah studies the engraving on the title page while he turns it. The case opens toward you. Under the prospectuses lies an older folded proof, bound with a red thread.{/n}
"That one," {n}she says.{/n}
"It is very rough."
"So was the subject."
{n}He smiles because he cannot decide whether she has made a joke he ought to understand. He lifts the folded proof, leaving the open case within her reach.
Nurah does not touch it. She is watching his face now, waiting for the first lie worth keeping.{/n}''', c('[Examine the page he has brought out.]', "read", flags=f("case_opened"))),
    n("interruption", "Nurah", '''{n}Carrow notices your glance at the case. The heel of his hand settles against the clasp. He begins a long account of Vhal's devotion to neglected historical figures.
Nurah drops her pencil. It rolls under his chair.{/n}
"Oh, do not trouble yourself," {n}she says, already leaning down.{/n}
{n}He troubles himself immediately. The chair scrapes. Nurah emerges with the pencil in one hand and a dust mark on her sleeve. Carrow's key cord has fallen outside his waistcoat. She looks at it openly.{/n}
"Does your devotion have a lock? I should like to see what it is hiding."
"We have had difficulties with unauthorized copies."
"You have had considerable success with mine."
{n}She waits. You ask him which of the materials carries Nurah's actual signature. He explains the distinction between a facsimile and an endorsement. You make him explain it again, using the forged page he has already distributed.
At last he opens the case and removes a folded proof. Then he shuts the lid and winds the key cord around two fingers. Nurah's interruption has obtained the page, but he will not let either of you near the remaining papers.{/n}
"There," {n}she says.{/n} "We have reached the part of the interview that requires reading."''', c('[Read the proof while he guards the case.]', "read", flags=f("case_guarded"))),
    n("demand", "Nurah", '''{n}Carrow has the requested proof ready in a separate folder. He slides it across the table without opening the case.{/n}
"The earliest surviving impression. I had it prepared as soon as your message arrived."
{n}Nurah holds the sheet toward the window. A narrow strip has been pasted over the bottom line. She puts it down with the care she might give a dead insect she intended someone else to identify.{/n}
"Surviving is a useful word. What happened to the footnote?"
"An error corrected before circulation."
"Whose error?"
"The compositor's."
{n}She looks at you. Carrow notices the exchange and changes his answer.{/n}
"Possibly mine. We worked in some haste."
"Then we are fortunate to have the editor here," {n}you say.{/n} "Take the correction off."
{n}The paper tears when he tries. He stops, lifts the damaged sheet, and finally unlocks the case. The older folded proof comes out with its red thread still tied. He places the damaged substitute beside it, keeping one finger over the torn footnote.
Nurah moves his finger with the blunt end of her pencil.{/n}
"We will need that as well."''', c('[Compare the substitute with the older proof.]', "read", flags=f("case_guarded", "substitute_exposed"))),
    n("collision", "Nurah", '''{n}Carrow opens his mouth to answer. Someone knocks. Nurah calls for the visitor to come in before he can decide whether he is receiving anyone.
Two men enter, each carrying an invitation, each determined to explain why the other has made a mistake. One is short and magnificently dressed. The other has brought a clerk who knows the exact wording of every promise his employer purchased.
Carrow rises. You move your chair to make room for the clerk, leaving the editor neatly between the table and the wall.{/n}
"A misunderstanding," {n}he says.{/n}
"We have collected several," {n}Nurah replies.{/n} "Please sit down."
{n}She asks the clerk to read his invitation. Before the first man can object, she gives him the dedication bearing his employer's name. The word exclusive becomes the loudest word in the room.
Carrow tries to explain that the edition can have more than one issue. The clerk asks whether each issue will claim to be the only one. The other representative begins demanding his deposit.
While Carrow unlocks the case to produce the subscriber terms, Nurah puts a steady hand on your knee beneath the table. Her fingers tighten when the folded red-thread proof appears. She has seen it. So have you.
The clerk reaches for the terms. You ask Carrow to leave the older proof beside them. He cannot refuse without explaining why he opened the wrong part of the case.{/n}''', c('[Keep the editor answering while Nurah reads.]', "read", flags=f("case_opened", "subscribers_witnessed"))),
    n("royal", "Nurah", '''{n}Carrow bows too deeply. Nurah lets him remain bent while she moves the clean proof to the middle of the table.{/n}
"You have a talent for finding titles when there is room for them in the price," {n}she says.{/n} "I hope you are equally good at finding the papers behind them."
"Your Majesty, we understood the proposed dedication would be welcome."
"By whom?"
"By the court."
"How convenient. I have brought enough of it to ask."
{n}She points at the case. He opens it, removes the folded proof, and immediately closes it again. The key vanishes into his waistcoat. He has prepared for an offended queen, and he intends to leave with every scrap he did not come to surrender.
Nurah notices. Instead of ordering the case seized, she asks him to read the proposed dedication aloud. He gets as far as obedient service before faltering.{/n}
"That is the phrase you chose," {n}she says.{/n} "Do finish it."
{n}He does. By the final line his voice has become almost inaudible.
She turns the page toward you. Her face is composed, but her foot has hooked around the leg of his chair. If he rises abruptly, he will have a much less dignified audience.{/n}''', c('[Inspect the proof before deciding how to answer the insult.]', "read", flags=f("case_guarded", "royal_discomfort"))),
    n("read", "Narrator", '''{n}The old proof is full of corrections in several hands. Nurah's writing crosses the middle of a paragraph about Trezbot's arrival. Beneath it, in another hand, a footnote names Bressa and the case of accounts she was sent to recover. A line has been drawn through the note, hard enough to split a letter.
Nurah puts her pencil beside that line. She does not yet touch it.
Carrow begins explaining that the original author frequently revised her own work. His explanation grows more confident when neither of you interrupts. He mistakes the silence for uncertainty.{/n}''',
      c('[Use the chronological error he has not been warned about.]', "caught", requires=f("chronology_kept")),
      c('[Let him reveal how he prepared for the objection already sent.]', "warned", requires=f("editor_warned")),
      c('[Give Nurah the first question you promised her.]', "her_question", requires=f("nurah_leads_interview"))),
    n("caught", "Nurah", '''"You revised the date of the retreat," {n}you say.{/n} "But you left this officer in command. He arrived afterward."
"The author supplied the date."
"No," {n}Nurah says.{/n} "The author supplied an account in which the officer had not yet arrived. Show us where I changed that."
{n}Carrow searches the page. He finds the line she wrote, follows it to the later correction, and stops. The ink is his own. He looks at the clean proof on the table as if it might offer a kinder sequence of events.{/n}
"A necessary clarification."
"Whose necessity?"
{n}You wait. At last he says Vhal wanted the household's contribution placed earlier, before a rival family's officers could claim credit. Nurah asks him to repeat that slowly while she writes it on the reverse of the damaged proof.
He refuses to sign. She has not asked him to.{/n}
"Now we know what an improvement costs," {n}she says.{/n} "And which part of the history changes when somebody pays for one."''', c('[Keep the exposed alteration as the basis for the next move.]', flags=f("interview_finished", "editor_exposed"))),
    n("warned", "Nurah", '''{n}Carrow produces a second sheet before you finish the objection. He has prepared a note explaining that the disputed officer directed events through correspondence before his arrival. No surviving letter is attached.{/n}
"We are grateful to the compositor for raising the question," {n}he says.{/n}
"Gratitude seems to be the cheapest material in your workshop," {n}Nurah replies.{/n} "May we see the correspondence?"
"It is not presently available."
"Then you have improved a mistake into an invisible source."
{n}He will not abandon the explanation. Nurah cannot make him. The earlier warning has given him time to turn a contradiction into a dispute over missing documents.
You ask who first mentioned the correspondence. He says Vhal. When you ask where she keeps it, he says her secretary handles such matters. Nurah writes secretary on the margin and draws a small, ugly face beneath it.{/n}
"We will ask her," {n}she says.{/n}
{n}Carrow smiles. He has kept this answer intact. The smile annoys Nurah enough that she snaps the point of her pencil against the paper.{/n}''', c('[Seek evidence he has not had time to explain away.]', flags=f("interview_finished", "editor_defense_ready"))),
    n("her_question", "Nurah", '''"Who told you Bressa was grateful?"
{n}Carrow looks down. Nurah does not. She keeps her eyes on his face until he answers.{/n}
"It was inferred from her continued service."
"By you?"
"By the collector."
"Did she write the sentence?"
"I prepared the final wording."
"Then you inferred it."
{n}He explains the demands of readable history. A footnote about an insignificant servant would distract from the larger account; a brief statement about the household's loyalty conveys the appropriate spirit. Nurah listens to the whole explanation. By the end you can hear him wishing she would interrupt.
She folds the older proof along its existing crease.{/n}
"I used to write appropriate spirits for a man who hit me when his soup cooled. You are better paid. Have you considered being more imaginative?"
{n}Carrow starts to answer, then decides against it. He cannot take back the admission that he supplied Bressa's gratitude himself. Nurah has stopped asking about the date, but she has obtained a different lie in his own voice.{/n}''', c('[Keep his admission about the invented testimony.]', flags=f("interview_finished", "false_witness_admitted"))),
], "audience_ready")


visit("the_case_goes_missing", "What leaves with the editor", [
    n("start", "Narrator", '''{n}At the next appointment Nurah is carrying a parcel tied with ordinary string. Inside it are a blank notebook, two lengths of thread, and a cheap lock.
"Carrow is leaving Drezen before the subscribers' evening," she says. "He means to return with Vhal's secretary and a better set of answers. I would rather meet the papers before they do."
She leads you to the room she has borrowed and puts the parcel on the bed. The lock clicks when she turns it over.
"He has rooms above the wine merchant. He has also acquired the habit of taking supper where people can see how much business he has. There is a stair at the back. We have time to decide what happens at the top."
She lays the notebook beside the lock. Its pages have been cut to the size of the older proof.{/n}''',
      c('"We can copy what matters and leave him wondering what we know."', "copy_plan"),
      c('"Take the originals. Let him try to explain why he no longer has them."', "take_plan"),
      c('"Ask for the case openly. I will make the demand worth answering."', "buy_plan")),
    n("copy_plan", "Nurah", '''"You want him comfortable."
"I want him to go on using the papers. He may show us something we would miss if we frighten him into silence."
{n}Nurah opens the notebook. On its first page she has already drawn a rough plan of the upstairs passage.{/n}
"And I want to know who paid him to improve Bressa. We shall have to be quick. I can copy a cramped hand, but I cannot copy an entire household's vanity between supper and pudding."
"Choose the pages."
"The first proof. The subscriber list. Any letter that tells him which names to remove."
{n}She tears out the page with the plan and hands it to you. The remaining notebook can pass for an editor's unused stock if it is found. You turn the plan toward the lamp and see a second mark beside the window.{/n}
"An exit?"
"A bad one. I prefer to draw those before I need them."
{n}She watches you fold the page rather than burn it. A quick smile appears and goes.{/n}
"Keep it. If we have to leave through the window, you may complain about my handwriting on the way down."''', c('[Prepare to copy selected papers without announcing the intrusion.]', "access", flags=f("operation_copy"))),
    n("take_plan", "Nurah", '''{n}Nurah puts the notebook aside and tests the string around the parcel.{/n}
"The whole case is heavier than it looks. He has padded the useful papers with prospectuses and an astonishing number of accounts for wine."
"We only need what he cannot replace."
"He can replace almost anything if nobody remembers seeing the first version."
{n}She leans against the bedpost, considering you. The smile she gives you now has less humor in it.{/n}
"You know he will call it theft."
"He has printed my endorsement without asking. I expect a lively discussion about ownership."
"Good. I would hate to spend the evening making excuses for you."
{n}She lifts the notebook again, tears out several sheets, and folds them into the parcel. They will keep the recovered papers from rubbing against one another. The care seems oddly domestic until she takes a knife from her sleeve and cuts the string to the exact length she wants.{/n}
"When we have the originals, I read them first."
"Why?"
"Because some of the lies are mine. You can wait until I have decided which ones still amuse me."''', c('[Prepare to remove the original papers.]', "access", flags=f("operation_take"))),
    n("buy_plan", "Nurah", '''"With your money?"
"With the value of being able to leave Drezen after admitting he forged an endorsement. He gives us the papers, and we settle that particular offense here."
"He will hear a threat."
"I intend him to."
{n}Nurah closes the parcel. For a moment she seems more interested in you than in the plan.{/n}
"Do not offer to forget the whole affair. Vhal will only hire him to remember it differently."
"The forged endorsement. Nothing else."
"And no promise about what I may publish."
{n}She presses the flat of her knife against the cheap lock, testing its weight rather than its mechanism. Then she puts both away.{/n}
"I want to hear him price his own innocence. People become wonderfully exact when they believe they are selling the last of it."
{n}You send a short summons. Carrow arrives before supper, carrying the case against his chest. He begins with an objection to the word forged. Nurah places the false signature beside a fresh example of her own writing.
The discussion becomes shorter after that. He will surrender the originals in return for your undertaking not to pursue his unauthorized use of your name. Nurah insists that he say aloud which offense the undertaking covers. His voice shakes when he does.{/n}''', c('[Accept that narrow settlement and take the papers he surrenders.]', "papers", flags=f("operation_bargain", "case_surrendered"))),
    n("access", "Nurah", '''{n}At dusk you take the back stair above the wine merchant. Nurah goes first. Halfway up, she stops to listen to someone laughing in the kitchen below. When the laughter passes into an argument about onions, she continues.
Carrow's door is locked. The window beside it opens onto a narrow roof. Nurah peers through the glass and points to the case on the desk.
"He has left it," she whispers. "Either he trusts the door, or he is becoming more interesting."
The room beyond is empty. A coat hangs from a peg, its waistcoat folded underneath. The candle on the desk is cold.
Nurah gives you the little knife. Its handle is warm from her sleeve.{/n}''',
      c('[Use the construction details Sava supplied to prepare the approach.]', "informed", requires=f("sava_paid")),
      c('[Use Sava\'s account of the case and preserve her signed evidence.]', "informed", requires=f("sava_evidence")),
      c('[Inspect the room and case without inside help.]', "unaided", requires=f("sava_uninvolved"))),
    n("informed", "Nurah", '''{n}Sava's description tells you which part of the case to inspect before opening it. Nurah works the door with a narrow strip of metal while you watch the stair. The lock yields on her third attempt.
Inside, the brass clasp faces the room. She stops your hand before you lift it. There is a fresh thread looped beneath the hinge, thin enough to pass for a loose fiber in the lining. Opening the lid carelessly would pull it free.
"He has become interesting," she whispers.
You hold the case steady while she loosens the thread with the tip of her knife. Her shoulder is pressed against your arm. Neither of you has room to move without moving the other.
At last the thread slips clear. She hooks it over the knife and nods toward the false bottom. It fits exactly where Sava said it would.
Under it are the folded proof, two letters, and a list divided into paid and promised. Nurah's own name appears in the promised column.
She touches it with a fingernail and looks up at you. Even in the dim room you can see the anger in her face.{/n}''', c('[Secure the papers without disturbing the warning thread.]', "papers", flags=f("entry_unnoticed"))),
    n("unaided", "Narrator", '''{n}Nurah opens the door with a narrow strip of metal and stands aside. The case looks ordinary from the passage. Up close, one hinge sits higher than the other and the lining seems too thick for the depth of the lid.
You cannot tell which irregularity matters without handling it. Nurah watches the stair while you kneel beside the desk. Somewhere below, the argument about onions has become an argument about a missing spoon.
"If you find the spoon," she whispers, "leave it. I do not want the cook pursuing us as well."{/n}''',
      c('[Examine the concealed fittings before opening the case. Trickery, DC 31.]', check=dict(Skill="SkillThievery", DC=31, Success="clean_entry", Failure="marked_entry", CommanderOnly=True)),
      c('[Open it and accept that Carrow may discover the intrusion.]', "marked_entry")),
    n("clean_entry", "Nurah", '''{n}You find the warning thread tucked into the hinge and lift it free before it can tear. The raised lining conceals a false bottom. Nurah exhales through her nose, impressed despite her effort to look merely impatient.{/n}
"There you are. I was beginning to wonder whether you intended to seduce the lock."
"Would that have worked?"
"It has a much simpler arrangement of weaknesses than you. I expect so."
{n}She holds the candle while you lift the hidden papers. The folded proof lies above two letters and a subscriber list. Nurah is named among the promised contributions, as though her presence were another item Carrow could deliver by a specified date.
She reads the entry twice. Then she reaches past you for the letters, her sleeve brushing your cheek. The joking has stopped.{/n}''', c('[Keep the intrusion concealed and read what he hid.]', "papers", flags=f("entry_unnoticed"))),
    n("marked_entry", "Nurah", '''{n}A thread snaps under the hinge. Nurah hears it from the door and closes her eyes for a brief, furious moment.{/n}
"Tell me that was your sleeve."
{n}You show her the torn fiber. She examines it, compares the ends, and shakes her head.{/n}
"He will know. We can make it look untidy, but we cannot make it unbroken."
"Then we use the time we have."
{n}She joins you at the desk and lifts the lining with the knife. The hidden papers slide out together: a folded proof, two letters, and a subscriber list. Nurah's name appears under promised contributions.
She takes the list first. Her eyes move over it rapidly, then return to the line about her.{/n}
"We finish before he comes back. And when he changes his plans, we do not pretend he did it by chance."
{n}Footsteps cross the passage outside. Nurah catches your wrist, pulls you down behind the desk, and waits until they pass. Her grip remains hard for several seconds afterward.{/n}''', c('[Work quickly, knowing the broken thread will warn Carrow.]', "papers", flags=f("entry_detected"))),
    n("papers", "Narrator", '''{n}The subscriber list is unpleasantly clear. Several families have paid to improve their ancestors' conduct. Beside those payments Carrow has recorded what their representatives expect to hear Nurah confirm. One wants an execution called discipline. Another wants an unpaid debt described as a gift.
Vhal's first letter names the account carrier Bressa. The collector has obtained a later record of her sale to a household outside Isger, dated after the retreat in which she disappeared. She intends to keep that record out of the new edition. It would complicate the claim that Bressa remained voluntarily in Trezbot's service.
The second letter is addressed to Nurah. Carrow has not delivered it. Vhal offers the original sale record in exchange for a signed account praising the household. The last paragraph is written in a different ink.
If Nurah refuses, the collector will publish a facsimile of a much older letter in which Nurah herself praised Trezbot's generosity and asked to remain under his protection.
Nurah reads the threat without moving. Then she folds it along a fresh crease, hiding the last paragraph inside.{/n}''',
      c('[Make the selected copies and return the originals to their places.]', "copied", requires=f("operation_copy")),
      c('[Wrap the original papers for removal.]', "taken", requires=f("operation_take")),
      c('[Keep the papers Carrow has surrendered under the settlement.]', "settled", requires=f("operation_bargain"))),
    n("copied", "Nurah", '''{n}Nurah copies the sale reference first. Her handwriting becomes smaller as she reaches the edge of the page. She refuses another sheet until she has fitted the last number into the margin.
You copy the subscriber names while she works through Vhal's letters. She does not copy the old praise quoted in the threat. When you reach for that letter, she lays it flat and points to the closing instructions instead.{/n}
"Those. The date, the place, and the price. We can discuss her taste in literature afterward."
{n}The originals go back beneath the lining. Nurah reties the red thread around the proof and checks its knot against the small impression it left in the paper. She has copied enough of the correspondence to expose the bargain. Vhal and Carrow will still possess the sheets themselves.
Outside, the stair seems louder under your feet than it did on the way up. Nurah waits until you have reached the street before she takes your arm. Her hand remains cold through your sleeve.{/n}''', c('[Leave with the copies and the reference to Bressa\'s later sale.]', flags=f("papers_recovered", "papers_copied"))),
    n("taken", "Nurah", '''{n}Nurah wraps the originals in the blank sheets she prepared. When she reaches the threatening letter, she stops, reads the quoted praise once more, and folds it with the rest.
The case looks absurdly empty. Prospectuses and wine accounts slide into the space where the hidden papers had been.{/n}
"He will miss them," {n}she says.{/n}
"That was the plan."
"Yes. I am reminding myself that I like it."
{n}She gives you the parcel because it fits beneath your coat more easily than hers. At the door she turns back and takes the case's little brass key as well. You raise an eyebrow.{/n}
"For his next case," {n}she says.{/n} "He should learn to change his habits."
{n}You leave by the stair. In the street she checks the parcel once, touching it through your coat, then walks ahead before you can ask what part of the letter has made her so quiet.{/n}''', c('[Leave with the originals and expect their owners to notice.]', flags=f("papers_recovered", "papers_taken"))),
    n("settled", "Nurah", '''{n}Carrow attempts to exclude Vhal's private correspondence from the settlement. Nurah reads his entry describing her promised appearance and asks which part of his promise he actually owns.
He gives up the letters.
You put the narrow undertaking in writing: the Commander's unauthorized endorsement will not be pursued further against him in exchange for these identified materials. Carrow reads it twice. Nurah stands behind his chair, close enough that he cannot look at her without turning his whole body.
When he has gone, she takes Vhal's threat from the parcel and holds it above the lamp. For a moment you think she means to burn it. Instead she reads the paper against the light, looking for writing on the other side.{/n}
"He knew about this," {n}she says.{/n} "He kept it until she could decide how much to ask."
"We have it now."
"We have this copy. She kept the letter she is threatening to print."
{n}She lowers the page. The room has grown darker while you were bargaining. She asks you to leave the lamp where it is.{/n}''', c('[Keep the surrendered evidence and the specific cost of the settlement.]', flags=f("papers_recovered", "papers_settled"))),
], "interview_finished")


visit("the_letter_she_wrote", "In her own hand", [
    n("start", "Nurah", '''{n}Nurah arrives without the parcel. She puts a single sheet on your table, then moves the lamp so that you can read it without taking the page from her.
It is her copy of the letter Vhal means to publish. She has reconstructed the quoted passage from memory and left a blank where she cannot remember the wording.
The letter praises Trezbot's generosity. It asks to remain in his household. Its concluding flourish is graceful, almost affectionate.{/n}
"I wrote it," {n}she says.{/n} "Before you decide the interesting question is whether she forged it. She did not."
{n}You look at the blank. Nurah taps it with the end of a pen.{/n}
"An adjective. I cannot remember which one. There were so many available, and he liked most of them."
"Why does she have it?"
"Because people keep evidence that they were loved. Especially when they have had to dictate the evidence."
{n}She takes the chair sideways, one elbow over its back. Her expression dares you to ask the obvious question badly.{/n}''',
      c('"What did you need him to believe?"', "reason"),
      c('"She can print it. You do not owe her a better explanation."', "print_it"),
      c('"We could make her doubt whether she still has the original."', "steal_back", requires=("trickster",))),
    n("reason", "Nurah", '''"That I was grateful. That was the usual requirement."
"For what, that time?"
{n}The irritation in her face changes direction. She looks down at the sheet, not at you.{/n}
"He was considering sending me with a man who liked his servants silent. I had already learned Trezbot's temper. It seemed wasteful to begin another education."
"So you persuaded him to keep you."
"I praised his judgment. I praised his instruction. I said I had become too attached to the household to bear leaving it. He asked whether I meant that."
{n}She presses the pen against the blank until a dark bead spreads into the paper.{/n}
"I said yes. He kept the letter."
{n}A small drop of ink reaches her finger. She wipes it on the underside of the chair without looking for a cloth.{/n}
"Vhal thinks I will be ashamed of having lied convincingly. I am much more annoyed that she has found a way to charge me for doing it twice."
"Then we change the price."
"We change who pays it. I would rather enjoy that."
{n}She lifts her eyes to yours. The invitation in them is dangerous and unmistakably personal.{/n}''', c('[Ask what she intends to do with the threat.]', "temper", flags=f("old_letter_understood"))),
    n("print_it", "Nurah", '''"How magnificent. Shall I write that beneath the facsimile? The Commander says I owe you nothing. I am sure they will find it decisive."
{n}She turns the sheet toward herself and reads the first sentence aloud. In her voice it sounds careful, even tender. She stops before the second.{/n}
"They will call this affection. Some will know better and call it affection anyway. Vhal is selling them the opportunity."
"Would an explanation stop them?"
"No. But leaving her with the only interesting page would make her very happy."
{n}She takes the pen and writes a short sentence beneath the praise: He was considering sending me to another owner. Then she draws a line through it, hard enough to score the table through the sheet.{/n}
"There. A true sentence. Already I dislike the people who would expect me to prove it."
"You can use the letter against her without asking them to pity you."
{n}Nurah studies you. Her fingers release their tight grip on the pen.{/n}
"That is a better suggestion. Keep making those. I was beginning to worry about the evening."''', c('[Find an answer that does not depend on their sympathy.]', "temper", flags=f("old_letter_defied"))),
    n("steal_back", "Nurah", '''{n}Nurah leans forward. The old letter is momentarily forgotten beneath her forearm.{/n}
"Go on."
"She owns a page because she believes you cannot bear having it read. Give her reason to think you have circulated three different versions already. Let her try to authenticate the one she means to sell."
"She will compare the handwriting."
"With yours. You are available to make it unhelpfully accurate."
{n}Nurah takes a fresh sheet. She copies the opening line, then writes it again with a different word in the middle. The second version accuses Trezbot of an embarrassing culinary preference. She reads it aloud and begins to laugh.{/n}
"No. Too funny. She would know I enjoyed that one."
{n}She tries again, keeping the praise plausible while changing which relative Trezbot supposedly favored. The altered line could start an argument at a family dinner and remain unresolved for years.{/n}
"We would have to let her see a variant before the evening. Enough to make her fear the original has lost its rarity."
"Can you do it?"
"I can do worse. That is what you like about me."
{n}She writes a third version. This one is close enough that you have to compare the sheets to find the insult.{/n}''', c('[Send a plausible variant into the collector\'s market.]', "temper", flags=f("letter_variants"))),
    n("temper", "Narrator", '''{n}The lamp catches a rough edge where Nurah cut the sheet. She rubs it with her thumb until a tiny curl of paper comes away.
"The sale record says Bressa was alive after the retreat," she says. "It tells us who bought her then. It does not tell us where she is now. Vhal knows exactly how far that scrap will make a person run."
She drops the paper curl into the lamp's cold tray and looks at the door. For a moment she seems to be measuring the distance to somewhere much farther away.{/n}''',
      temperament('"Tell me which part you refuse to sell."', "good", "good"),
      temperament('"You have already thought of something she will hate."', "chaos", "chaos"),
      temperament('"What would make this worth taking from her?"', "evil", "evil")),
    n("good", "Nurah", '''"I will not stand beside her and say the household taught us gratitude."
{n}She says it quickly, before you can mistake the condition for a request that you decide it for her.{/n}
"I can praise a dead man until the ink curdles. I have had practice. But she wants Bressa's name under mine, as though we compared our good fortune over breakfast."
"Then we obtain the record another way."
"And if the other way fails?"
"We follow the reference we have."
"That may lead nowhere."
{n}You do not promise otherwise. Nurah studies your face, then pulls the chair closer with one heel.{/n}
"I wanted you to say something foolish," {n}she admits.{/n} "I had a very good answer ready."
"Save it. I have a long evening ahead."
{n}Her laugh is brief. She reaches for your hand and turns it palm upward, tracing a small ink stain at the base of your thumb.{/n}
"So do I. And I would rather spend part of it on something she cannot price."''', c('[Stay while she decides how much of the old letter to use.]', "near", flags=f("bressa_priority"))),
    n("chaos", "Nurah", '''"She has invited people who paid to hear a flattering history. I want them competing to prove it is a forgery."
"Their own history?"
"Especially their own. One sentence that ruins a rival is irresistible. Two sentences that contradict it are somebody else's problem."
{n}She lays the subscriber names beside the old letter and begins pairing them with the claims they purchased. Her finger moves faster as the idea develops.{/n}
"We let them authenticate one another. By the end of the evening, a man who wanted a noble ancestor may pay simply to be left out."
"And Bressa's record?"
"Vhal must bring it if she means to sell my performance. We take it while her audience is busy defending their grandparents."
{n}She looks up with a bright, wicked grin.{/n}
"You thought I had forgotten."
"I wanted to hear where it fitted."
"Beside the part where I enjoy myself. I am very fond of fitting things there."
{n}Her hand settles on your thigh. She waits until you look down, then shifts it just enough to make looking back at her difficult.{/n}''', c('[Help turn the subscribers against the history they bought.]', "near", flags=f("subscriber_game"))),
    n("evil", "Nurah", '''"Her collection. The useful part. Not every aunt's account of a heroic breakfast."
"You want her trade."
"She has spent years finding the things families want hidden and the lies they want admired. Then she had the poor judgment to threaten someone who could improve her methods."
{n}Nurah draws a line down the subscriber list. On one side she marks names worth embarrassing. On the other she marks names likely to pay.{/n}
"Bressa's record brings her to the table. The rest keeps her there. I want the names of the collectors who sold her material. I want to know which households still send her papers."
"That gives her something to bargain with."
"Of course. A woman with nothing to lose is an inconvenience. A woman who thinks she can still save her business is a conversation."
{n}She stops writing and looks at you with frank appraisal.{/n}
"You understand that expression. I have seen you use it."
"Does that trouble you?"
"At the moment? No. I find it very attractive. Try not to waste it on generosity before we have finished."''', c('[Prepare to take the collector\'s sources as well as the record.]', "near", flags=f("collection_priority"))),
    n("near", "Nurah", '''{n}Nurah sets the pen down. When you move the old letter away from the lamp, she catches your wrist.{/n}
"Leave it. I know where it is."
{n}She rises onto the chair to reach you without pulling you down. Her hands settle on your shoulders, then slide beneath the edge of your collar. The touch is slow now, with none of the performance she used in front of Carrow.
You kiss the corner of her mouth. She turns toward you and makes you begin again properly. One knee presses against your hip as she steadies herself. The chair protests.{/n}
"This furniture has no discretion," {n}she murmurs.{/n}
"The bed. Quickly, before this thing breaks."
{n}You lift her from the chair. She makes a small, affronted sound that turns into a laugh halfway through, and wraps an arm around your neck. On the way past the table she reaches down to extinguish the lamp. The old letter disappears into darkness with everything else.
At the bed she twists out of your arms before you can set her down, lands on her knees on the cover, and hauls you after her by the collar she has already half unfastened.{/n}
"Still thinking about Vhal?" {n}she catches your collar again.{/n} "She can wait. I want you here." {n}She pulls the pins out of her hair one at a time and drops them on the floor, and puts one ink-stained hand flat on your chest and pushes.{/n}
{n}In the morning she retrieves the letter without hurrying, folds it into her sleeve, and steals the warmer side of the cover before you can object. When you reach for her she does not pretend to be asleep. From that night she stops knocking at your door; she simply comes in, and tells you what she has been writing, and sits where she likes.{/n}''', c('[Let the work wait until she comes up the stair again.]', flags=f("letter_faced"))),
], "papers_recovered")


visit("the_price_of_a_warning", "The invitation changes", [
    n("start", "Narrator", '''{n}Nurah is waiting in your chambers with a new invitation and a boot resting on the lowest rung of a chair. There is mud on the sole. She has apparently decided the chair can afford it.
"Vhal has arrived. Her secretary came to find out whether I had learned to be sensible. I told him I was considering it. He looked relieved, so I charged him for the consultation."
She flicks a small coin across the table. It spins, falls, and rolls into the folded invitation.
"The evening is still going ahead. Our host has changed the arrangement."{/n}''',
      c('[Hear how the unnoticed copying has left the original plan intact.]', "quiet", requires=f("papers_copied", "entry_unnoticed")),
      c('[Hear what Carrow changed after finding the broken warning thread.]', "warned", requires=f("papers_copied", "entry_detected")),
      c('[Hear the response to the missing originals.]', "theft", requires=f("papers_taken")),
      c('[Hear how Vhal answered the editor\'s settlement.]', "settlement", requires=f("papers_settled"))),
    n("quiet", "Nurah", '''"Carrow still has his proofs. He has given them to Vhal to carry into the room. She intends to use the oldest one to show how carefully she has preserved my work."
{n}Nurah taps the invitation. A place has been left for her signature beneath the proposed reading order.{/n}
"She has put Bressa's record immediately after the biography. I read the praise, she lets me inspect the record. A well-trained animal receives its treat in the right sequence."
"She does not know we have copies."
"No. And I should like to preserve that pleasant ignorance until it becomes expensive."
{n}She turns the invitation over. On its blank side she has drawn the room: a long table, a sideboard, a pair of doors. The record will be displayed beside the book while Nurah reads. Vhal wants the audience to see the reward being offered.
There is no screened recess for the papers and no secretary assigned to hold them throughout the evening. Nurah has confirmed both details by asking where she may stand to be seen most flatteringly.{/n}
"Vanity is excellent reconnaissance," {n}she says.{/n} "People become suspicious when you ask about the lock. Ask about the light, and they move the table for you."''', c('[Use the unsuspicious display arrangement.]', "sava", flags=f("display_open"))),
    n("warned", "Nurah", '''"He found the broken thread. He has not proved what was read, which has encouraged him to imagine everything."
{n}Nurah unfolds a second sheet. The revised arrangement places Vhal's documents behind a folding screen. Her secretary will bring out each one only when she asks for it.{/n}
"We will not get a hand on the record simply by leaning across the table. Carrow has also warned her that I may ask about the subscriber list."
"Will she cancel?"
"And admit she cannot control a small woman with a book? Her pride is more reliable than her editor."
{n}Nurah scratches a line through the sideboard on her sketch. The secretary's position behind the screen leaves him within hearing of the room but outside its argument. Someone will have to make him leave it or force the record into public view.{/n}
"The thread has bought us a second obstacle," {n}she says.{/n} "We can still cross it. I would prefer not to buy a third."
{n}She nudges your hand with the blunt pencil. Her anger has become practical again, though she has not forgotten whose hand was on the hinge.{/n}''', c('[Plan around the guarded document screen.]', "sava", flags=f("display_guarded"))),
    n("theft", "Nurah", '''"Vhal has called the missing papers stolen property. Carrow has called them several less printable things. Neither has dared accuse the Commander in writing."
{n}Nurah has kept their messages. The collector's is elegantly furious; the editor's has a stain where his hand smeared the final line.{/n}
"She still has Bressa's sale record and my old letter. She will bring both. The rest of her display is now copies."
"And the originals we took?"
"Remain ours until somebody persuades us otherwise. She wants an exchange before the reading. I told her I cannot negotiate a return of objects I have not been formally accused of possessing."
{n}She shows you the room sketch. Vhal's secretary will stay behind a screen with the surviving originals. Two hired porters will stand at the outer door. Nurah has crossed out the word porter and written watcher above it.{/n}
"No blades unless they decide to improve their occupation. I would rather defeat her in front of people who can repeat what she said."
"But you have a way out."
"I have two. I am allowing for your tendency to become difficult to conceal."''', c('[Keep the stolen originals and prepare for a guarded exchange.]', "sava", flags=f("display_guarded", "vhal_demands_return"))),
    n("settlement", "Nurah", '''"She dismissed Carrow. He sent me an account of her ingratitude which I have saved for a particularly dull evening."
"Will he appear?"
"He would not miss the chance to see somebody else blamed. Vhal has invited him to explain the editorial errors, so the feeling is mutual."
{n}The new invitation removes Carrow's name from the list of organizers. His duties have passed to the secretary. Nurah points to the last line.{/n}
"She accepts that we have the surrendered papers. She means to call them unauthorized drafts when we quote them. Then she will offer the sale record as proof that she, at least, respects original evidence."
"She has made it part of her defense."
"Which means she must show it. I do like a woman who arranges her own inconvenience so thoughtfully."
{n}The documents will sit on the table during the reading. Vhal has not hired extra watchers. She is relying on the Commander's public settlement with Carrow to make an outright seizure look like a broken undertaking, though the undertaking says nothing about her record.{/n}
"We shall be precise," {n}Nurah says.{/n} "It annoys people much more than shouting."''', c('[Make her display the original she has used to defend herself.]', "sava", flags=f("display_open"))),
    n("sava", "Narrator", '''{n}Nurah draws a small square beside the room's entrance.
"The compositor has been invited too. Vhal wants someone available to accept responsibility for an unfortunate printing error."
She looks up from the sketch. The square is empty. She has not written Sava's name inside it.{/n}''',
      c('[Ask whether Sava will use the wages and information already exchanged.]', "paid", requires=f("sava_paid")),
      c('[Ask whether Sava will stand behind her signed evidence.]', "evidence", requires=f("sava_evidence")),
      c('[Keep Sava outside the operation, as agreed.]', "outside", requires=f("sava_uninvolved"))),
    n("paid", "Nurah", '''"She has bought enough paper to finish the run without Carrow's credit. That makes her less afraid of displeasing him. It does not make her fond of us."
{n}Nurah produces a sample sheet. Sava has offered to print a short replacement at her own rate if you provide the wording before the evening. She will not set type during an argument or accept payment in promises of future gratitude.{/n}
"I paid her the paper balance," {n}Nurah says.{/n} "Do not look so startled. I intend to recover it from somebody much less sympathetic."
"What will she print?"
"Our answer. Once we have decided whether it is a correction, an accusation, or an invitation to buy something worse."
{n}She folds the sample and puts it with the sketch. The small square gains a name now, followed by the word printer.
Sava will bring blank stock and the copies prepared in advance. She will leave if anyone tries to make her swear to a conversation she did not hear. Nurah reports that condition with an irritated respect.{/n}''', c('[Use the paid print run for the eventual answer.]', flags=f("evening_prepared", "print_run_ready"))),
    n("evidence", "Nurah", '''"She has made two copies of the signed instruction. One is going to the evening. The other is with a friend who dislikes Carrow on her own account."
"A precaution."
"An expense. She has asked what we intend to do if Vhal decides the compositor is easier to punish than the author."
{n}Nurah has already written an answer. Sava's part will be limited to reading the instruction and identifying the proof she set. The Commander will say, in the same room, that the document was requested for this inquiry. No promise of employment, no place in a retinue, no claim that Sava became a conspirator merely by bringing her own work.
Nurah pushes the sheet toward you.{/n}
"It gives Vhal someone more troublesome to argue with. I thought you might enjoy volunteering."
"You wrote this before asking."
"I left the signature blank. My restraint is extraordinary."
{n}You sign. Nurah gives the page a moment to dry, then folds it for delivery. Sava will appear as a witness, with the scope of her testimony settled beforehand.{/n}''', c('[Take public responsibility for requesting Sava\'s evidence.]', flags=f("evening_prepared", "witness_ready"))),
    n("outside", "Nurah", '''"I told her not to come. She asked whether that meant Carrow would pay the remaining bill."
"It does not."
"No. She noticed."
{n}Nurah crosses out the square beside the entrance. There will be no compositor to identify the printing changes, and no extra copies waiting to circulate while Vhal is still talking.
She moves the invitation into the empty space. Its false signature will have to introduce the dispute. Nurah can identify her own writing. You can identify the endorsement you never gave. Neither requires Sava to stand between you and the collector.{/n}
"She may sell her account later," {n}Nurah says.{/n} "We did not buy her silence."
"Would you have preferred to?"
"I prefer knowing which inconvenience I have paid for. This one remains a surprise."
{n}She picks up the coin from the secretary's visit and balances it on the chair's rung beside her muddy boot. It falls before she can make it stand. She leaves it on the floor.{/n}
"Then we will have to be memorable without assistance. I have managed it before."''', c('[Proceed without the compositor\'s testimony or printing help.]', flags=f("evening_prepared", "no_public_compositor"))),
], "letter_faced")


visit("the_subscribers_evening", "A reading before friends", [
    n("start", "Narrator", '''{n}Nurah comes to your chambers dressed for the subscribers' evening. Her sleeves are fine enough to draw attention and loose enough to conceal a surprising number of objects. She lets you admire them, then asks which part of the evening you intend to survive by looking at her arms.
You leave together after she has checked the passage. At the hired room, the wine is already being poured.
Istrene Vhal receives you beside a display of books. She is a spare woman with an expensive ring and the habit of leaving other people to finish approaching her. When Nurah stops a pace short, Vhal has to take the final step herself.
"At last," she says. "I have read so much of your work."
"I hear you have been adding to it."
The collector's smile remains in place. Her secretary, a narrow man called Edran, moves a stack of papers out of Nurah's reach. Carrow watches from the far end of the room.
Vhal introduces the Commander as a distinguished supporter of the enterprise. Nurah turns toward you with an expression of delighted expectation. She wants to hear what you do with the word supporter.{/n}''',
      c('"I have come to discover what my name has been supporting."', "opening"),
      c('"The author persuaded me this would be worth attending."', "opening"),
      c('"I am told this evening offers an unusually good return on misplaced confidence."', "opening", requires=("trickster",))),
    n("opening", "Nurah", '''{n}Vhal takes the answer as graciously as she can and calls the room to order. A dozen subscribers and representatives turn from their wine. Several already have their copies open to the proposed dedication.
Nurah climbs onto the low reading platform without accepting the secretary's hand. She puts her own book on the stand, opens it, and waits until the room is quiet.{/n}
"This edition contains an account of a woman named Bressa," {n}she says.{/n} "Before I read it, I would like to see the document Mrs. Vhal has offered in support."
"After the introduction," {n}Vhal replies.{/n}
"This is the introduction."
{n}A man near the front laughs, thinking the exchange rehearsed. Vhal looks at him. The laughter dies.
Nurah keeps her finger on the page. She has made the record part of the reading in front of everyone. The collector can refuse, but she can no longer pretend the request was never made.{/n}''',
      c('[Call attention to the document already displayed on the table.]', "open_record", requires=f("display_open")),
      c('[Make the secretary bring the guarded record into view.]', "guarded_record", requires=f("display_guarded"))),
    n("open_record", "Narrator", '''{n}You indicate the sheet beneath the glass weight. Vhal lifts the weight herself, holding the document by its corners. The old ink is brown; the later collector's notation is black.
She begins reading the notation. Nurah asks her to read the actual entry instead. It names Bressa, gives the date of sale, and identifies the purchasing household. There is no expression of gratitude. There is a price.
The room has become attentive in a different way. Vhal lowers the page, but you ask Edran to place it on the reading stand so the author can compare it with the printed claim.
He looks to his employer. She cannot refuse without making the comparison itself suspicious.
Nurah receives the sheet. Her eyes find the name first, then the date. For a moment her thumb covers the price. She shifts it deliberately and looks at the whole entry.
"This woman was sold," she says. "Who decided she stayed because she loved the household?"
Vhal turns toward Carrow. He puts down his wine.{/n}''', c('[Keep the original in view while the editor answers.]', "proof", flags=f("record_seen", "record_on_stand"))),
    n("guarded_record", "Narrator", '''{n}Edran remains behind the screen. Vhal says the record is too fragile to be passed around a room. Nurah closes her book.
"Then we can all admire your concern while you read it to us."
"I had hoped to hear the author's work first."
"You have printed rather a lot of it without waiting to hear from the author. This should be a welcome change."
Several guests smile. Vhal notices them, then you. She has to choose whether to bring the document out or turn the evening into an argument about why she will not.
Edran shifts behind the screen. You can see his hand on a folded leather cover through the gap. He is waiting for a signal to close it and leave by the service door.{/n}''',
      c('[Draw the audience into insisting on the source. Diplomacy, DC 32.]', check=dict(Skill="CheckDiplomacy", DC=32, Success="public_demand", Failure="record_withdrawn", CommanderOnly=True)),
      c('"If the document cannot be shown, say plainly that this edition asks for belief without evidence."', "record_withdrawn")),
    n("public_demand", "Nurah", '''{n}You ask whether the subscribers paid for original research or merely a well-bound assertion. The distinction interests them. One requests the record in a tone that makes it difficult for Vhal to pretend the question is yours alone.
Another wants to know whether his own household's documents are being treated with similar delicacy. Nurah offers to read those next.
Vhal tells Edran to bring the sheet.
He places it on the stand, keeping the leather cover under his arm. Nurah reads the sale entry aloud. The name of the purchasing household carries clearly to the back of the room. So does the price.
When she finishes, she leaves the sheet beside the printed claim of grateful service. Nobody needs her to explain why the two do not belong together.{/n}
"Mr. Carrow," {n}she says.{/n} "You remember discussing this sentence. I would hate to deprive you of an audience now that we have found one."''', c('[Use the original sale entry beside the invented testimony.]', "proof", flags=f("record_seen", "record_on_stand"))),
    n("record_withdrawn", "Nurah", '''{n}Vhal does not yield. She says the Commander is turning a literary evening into a tribunal and asks Edran to secure the collection.
The secretary closes the leather cover. Nurah watches him go through the service door. Her hand tightens on the edge of the stand, but she does not follow him.
You have the copied reference from her correspondence. You do not have the original sale sheet, and the audience has not seen it. Vhal intends to exploit that difference.{/n}
"Mrs. Vhal offered me that record for a signed performance of gratitude," {n}Nurah says.{/n} "If she does not wish to show the record, perhaps she would like to explain the offer."
"A private letter has been misunderstood."
"Then we should read the whole of it. I am sure context will improve your evening."
{n}Nurah takes out the recovered correspondence or its copy, opens it to the promised exchange, and begins before Vhal can interrupt. The guests lean forward. The original record has escaped the room, but its owner's bargain has not.{/n}''', c('[Expose the bargain without claiming to possess the withdrawn original.]', "proof", flags=f("record_withdrawn"))),
    n("proof", "Narrator", '''{n}Carrow says he worked from materials supplied by the collector. Vhal says she trusted the editor to distinguish testimony from interpretation. Between them, the printed gratitude becomes a sentence neither remembers choosing.
Nurah asks you for the evidence prepared before the evening. Her voice is light. The room has begun enjoying the quarrel, and she means to keep it listening.{/n}''',
      c('[Circulate the paid replacement sheets.]', "printed", requires=f("print_run_ready")),
      c('[Call Sava to identify her signed instructions.]', "witness", requires=f("witness_ready")),
      c('[Identify the unauthorized endorsement and let Nurah identify her own hand.]', "alone", requires=f("no_public_compositor"))),
    n("printed", "Nurah", '''{n}Sava has brought a stack of sheets with the false endorsement on one side and the relevant passages of Vhal's offer on the other. She hands them to the nearest guests, then tells them to pass the copies along. She refuses to answer a question about the binding until the sheets have reached the back of the room.
Vhal takes one. Her ring leaves a faint dent in the paper.{/n}
"This was prepared in advance."
"So was your edition," {n}Nurah says.{/n} "We admired your method."
{n}A subscriber compares the offer with the promise printed in his own book. Another asks why his family's name appears beside a payment in the reproduced list. The room begins asking questions faster than Vhal can choose who may ask them.
Sava stays by the door, protecting the remaining copies beneath one arm. She has been paid to print. She has no intention of being persuaded to surrender the stock because the customer has become unpopular.{/n}''', c('[Let the copies carry the accusation beyond the room.]', "letter", flags=f("public_copies"))),
    n("witness", "Nurah", '''{n}Sava steps forward with the signed instruction. Before she speaks, you state that she brought it at your request. Vhal's glance moves from the compositor to you.
Sava identifies Carrow's correction, the proof she set, and the instruction replacing Bressa's missing account with grateful service. She refuses to guess whether Vhal dictated the wording. Carrow seizes on that refusal until Sava turns the sheet over and reads his note about the collector's requested emphasis.
Nurah watches him lose the advantage he thought he had found.{/n}
"You see," {n}she tells Vhal,{/n} "a witness becomes much more troublesome when she is allowed to remember the parts you did not order."
{n}Sava finishes, folds the document, and steps back beside you. When a guest asks whether she will print an account of the evening, she gives him a price. Nurah's laugh interrupts the next question.{/n}''', c('[Keep the accusation attached to the witnessed instruction.]', "letter", flags=f("public_witness"))),
    n("alone", "Nurah", '''{n}You place the false endorsement beside the original invitation. Nurah writes her name on a clean sheet, then points out the identical hesitation in every printed imitation. Someone copied a single model badly enough to make even the mistake repeat.
Vhal calls this a trivial editorial matter. You ask whether she would accept a similarly trivial imitation of her signature on a debt.
The answer takes her too long.
Nurah reads the offer concerning Bressa. Without Sava, there is no compositor to identify who ordered the altered line. Carrow and Vhal keep passing that part of the accusation between them. But neither can explain why a genuine authorial appearance had to be purchased with a withheld record while a false signature was already selling the book.
A guest tears the dedication from his copy. The small sound carries surprisingly far.{/n}
"That is one correction," {n}Nurah says.{/n} "Do leave room for the others."''', c('[Keep the narrower accusation on what you can personally identify.]', "letter", flags=f("public_authors"))),
    n("letter", "Narrator", '''{n}Vhal takes a folded page from inside her sleeve. Nurah recognizes the gesture before the paper opens.
"Since we are discussing authentic writing," the collector says, "perhaps the author will explain this expression of affection for the household she now finds so convenient to condemn."
She begins reading Nurah's old praise of Trezbot. The room falls quiet. Nurah leaves the stand and walks toward her, slowly enough that nobody mistakes it for an attempt to snatch the letter.
Vhal finishes the first paragraph. Nurah holds out her hand.
"The next line," she says. "You have skipped it."
The collector looks down. Whatever Nurah expected to find, it is there. Vhal's certainty, which has lasted all evening, develops a small visible crack: she is no longer sure she has chosen the right page.{/n}''',
      c('[Watch her compare the original against the variants Nurah circulated.]', "variants", requires=f("letter_variants")),
      c('[Let Nurah finish the sentence her former master kept.]', "original", forbids=f("letter_variants"))),
    n("original", "Nurah", '''{n}Vhal folds the bottom of the page under her fingers.
Nurah does not lower her outstretched hand.{/n}
"You were willing to read my affection to a roomful of strangers. I am willing to read the next sentence. Which of us has become shy?"
"There are private matters in this letter."
"There were private matters in it when you opened it."
{n}The guest who laughed at the beginning of the evening asks to hear the missing line. Vhal looks toward Carrow, but he is studying the wine in his glass.
She places the page in Nurah's hand. Nurah unfolds the bottom edge with one finger, taking care not to tear the crease.{/n}
"Thank you. I had forgotten which adjective I used."
{n}Vhal's hand closes on empty air. Nurah turns toward the room with the letter held where everyone can see it.{/n}''', c('[Hear her read the entire sentence.]', "reading", flags=f("letter_taken_public"))),
    n("variants", "Nurah", '''{n}Vhal turns the page toward the light. From her other sleeve she takes a second sheet, compares the opening, and puts it away too quickly.
Nurah has seen enough.{/n}
"Another edition? I hope you obtained the author's permission."
{n}A guest asks whether the collector has been sold a copy. Vhal insists the original is authentic. Another asks how she knows. The plausible variants Nurah sent into circulation have reached their intended buyer, and now every guest wants the explanation the collector hoped to avoid.
Nurah lets the questions continue until Vhal holds the original out in exasperation. Then she takes it.{/n}
"This one is mine," {n}she says.{/n} "I remember the sentence you omitted. We can begin there."
{n}She has not made the old praise disappear. She has made Vhal surrender control of its reading in order to defend the value of her own collection. The collector's hand stays outstretched for a moment after the paper is gone.
You catch Nurah's eye. Her smile is small enough that only you see it.{/n}''', c('[Let the author read the original she has identified.]', "reading", flags=f("variants_paid_off"))),
    n("reading", "Nurah", '''"I beg you not to send me from the household whose kindness has taught me to love my place."
{n}Nurah reads the sentence in the same careful voice with which Vhal read the praise. The room is quiet enough that you hear the page move against her sleeve.{/n}
"He was considering sending me to another owner," {n}she says.{/n} "I preferred the temper I already knew. So I wrote him something he would enjoy keeping."
"We cannot possibly establish what you meant at the time," {n}Vhal says.{/n}
"You seemed very sure a moment ago."
{n}The collector draws herself up. Nurah does not raise her voice to follow her.{/n}
"You may dislike the household now, but this is still evidence of your own words."
"Yes. They worked. He kept me. I was good at my work."
{n}A man in the second row shifts his feet. Nurah looks at him until he stops.{/n}
"She has offered to buy more words," {n}Nurah continues.{/n} "This time she wants me to say another woman was grateful. You have heard the offer. Is there anyone here who would like to pay extra to hear me mean it?"
{n}Nobody answers. Vhal reaches for the letter. Nurah folds it once and puts it inside her bodice, watching the collector decide whether to reach farther.{/n}
"That belongs to my collection."
"You have used it. Send me the bill. We can compare it with the price of the signature you printed."
{n}Carrow gives a small, involuntary cough. The guests turn toward him, and Vhal loses the moment in which she could have called for help without making a spectacle of the retrieval.{/n}''',
      c('[Keep the original record on the stand while Vhal tries to dismiss the comparison.]', "visible_close", requires=f("record_on_stand")),
      c('[Keep the accusation on the bargain the room heard, despite the withdrawn record.]', "withdrawn_close", requires=f("record_withdrawn"))),
    n("visible_close", "Nurah", '''{n}You put a hand beside Bressa's sale entry before Edran can clear the stand. He stops. The document remains between the invented gratitude and Nurah's open book.{/n}
"An interpretation has been disputed," {n}Vhal says.{/n} "A correction can be made."
"Which interpretation?" {n}you ask.{/n}
{n}She will not say slavery. She calls it service, then circumstance, then a regrettable imprecision. Nurah waits through each attempt.{/n}
"The price is legible," {n}she says at last.{/n} "You may borrow the number if the word troubles you."
{n}The finely dressed subscriber asks whether the other testimonies have similar records behind them. His tone has lost its pleasure. Vhal offers him a private explanation; he asks why privacy has suddenly become necessary.
Nurah steps down from the platform. As she passes you, her fingers close briefly around your wrist. Her hand is shaking. Her voice, when she asks Edran for a clean sheet to trace the record, is perfectly steady.
He brings it. Vhal watches the tracing begin and says she would like to discuss a settlement somewhere less crowded.{/n}''', c('[Leave with the witnessed evidence and her request to negotiate.]', flags=f("reading_confronted"))),
    n("withdrawn_close", "Nurah", '''"The document would have settled this," {n}Vhal says.{/n} "Unfortunately the Commander's manner made its removal necessary."
"Then bring it back," {n}you answer.{/n}
{n}She refuses. A guest complains that his evening has been spoiled by accusations neither side can settle. Nurah turns to him.{/n}
"The record may wait. The offer did not. You heard what she wanted me to say before she would let me see it. Would you pay a historian to work that way?"
"We pay for a finished history."
"Then you have had an unusually good view of its manufacture."
{n}He closes his book. Vhal keeps repeating that the original remains available to a properly arranged inquiry. But when another subscriber asks whether his deposit purchased research or a performance, she cannot answer by blaming the Commander.
Nurah takes your arm and walks toward the door. Vhal catches you before you leave, lowering her voice so the guests cannot hear the word settlement.
Nurah makes her repeat it.{/n}''', c('[Take the offer. The record stays missing.]', flags=f("reading_confronted"))),
], "evening_prepared")


visit("the_unpurchased_sentence", "The unpurchased sentence", [
    n("start", "Nurah", '''{n}When Nurah next comes to your chambers, she takes the old letter from inside her book and puts it on the table. The crease beneath the omitted line is still visible.
She rubs it flat with her thumb, then stops before she wears through the paper.{/n}
"Kindness," {n}she says.{/n} "I remembered the wrong adjective. I would have chosen a worse one if I had known how long people intended to keep reading it."
"Would he have noticed?"
"He noticed anything that made him sound less important. Cruelty was a much smaller concern."
{n}She glances toward the chair, but remains standing beside you.{/n}
"Vhal wants to settle. She has offered us a private conversation before she leaves. The audience cost her enough that she would prefer not to acquire another."
"Us?"
"She has noticed you. I tried to warn her you could be inconvenient."''',
      c('"She handed over the original to defend it against your variants."', "variants_memory", requires=f("variants_paid_off")),
      c('[Ask what became of the sale record displayed during the reading.]', "record", requires=f("record_on_stand")),
      c('[Ask what can still be pursued after the original was withdrawn.]', "missing", requires=f("record_withdrawn"))),
    n("variants_memory", "Nurah", '''"She had to prove which one was worth keeping. I was happy to assist."
{n}Nurah takes out one of her altered versions and puts it beside the original. The changes are tiny. Side by side, the two sheets look like an innocent writer deciding which words she prefers.{/n}
"She could have kept holding the letter and refused to compare them," {n}you say.{/n}
"Then every collector in that room would have wondered what she was afraid to discover. You chose her vanity very well."
{n}She tears the variant down the middle, folds the pieces together, and places them in the lamp tray. The original goes back into the book.{/n}
"That one has finished its work. This one is mine again."
{n}She catches your hand before you can move the book and presses a kiss against your knuckles. Then she turns your hand over and studies a small ink mark on your palm.{/n}
"We should find you a less innocent occupation. You have a talent for this."''',
      c('[Turn to the witnessed sale record.]', "record", requires=f("record_on_stand")),
      c('[Turn to the original Vhal still withheld.]', "missing", requires=f("record_withdrawn"))),
    n("record", "Nurah", '''"I kept it on the stand until the guests had finished looking. Vhal could hardly take it away while insisting it explained everything."
{n}Nurah produces a tracing of the entry. The original remains with the collector, but the name, date, price, and witnessing marks have been copied in front of people who saw them. One subscriber wrote his initials beside the tracing because he wished to appear useful.{/n}
"She may still bargain over the sheet," {n}Nurah says.{/n} "She cannot pretend we invented what it says. I have sent the buyer's name to a correspondent who knows that district."
"Will they find Bressa?"
"They may find a household that changed its name twice and burned its accounts. I have asked for the accounts anyway."
{n}She holds the tracing against the light, checks that the smallest mark can still be read, and puts it back into her sleeve.{/n}
"If Vhal hands over the original, it will make the inquiry easier. It will not make a road shorter. I would rather she knew we can begin without her permission."''', c('[Enter the settlement with the witnessed record already copied.]', "method", flags=f("bressa_trace_witnessed"))),
    n("missing", "Nurah", '''"Edran carried it to her rooms. He has since acquired a second lock for the traveling chest. I hope it brings him comfort."
{n}Nurah sets out the reference copied from Vhal's letter. It identifies the purchaser and the collector's catalog number. It lacks the witnessing marks on the original sheet.{/n}
"I can begin with this. A correspondent knows the district. But if the household denies the sale, we will have a collector's description instead of the entry itself."
"Then the original still has a price."
"Yes. I would have preferred the price of a sheet left carelessly on a table. We did not obtain that arrangement."
{n}She taps the catalog number, memorizing it once more before putting the copy away.{/n}
"Vhal wants us to stop circulating the bargain she offered. I will let her explain how much she wants it. She may discover that paper is expensive in Drezen."
{n}Her voice is steady. The loss of the public record has narrowed the next negotiation, and she intends to make the collector pay for every remaining advantage.{/n}''', c('[Keep the missing original among the settlement demands.]', "method", flags=f("bressa_trace_unwitnessed"))),
    n("method", "Nurah", '''{n}Nurah turns the old praise letter facedown. Beside it she places Vhal's invitation to settle. The new invitation contains no flattering description of the Commander.
"An improvement," she says. "Now we decide what she leaves behind."
She has already written a demand concerning the sale record. She leaves space beneath it for the rest.{/n}''',
      temperament('"Make her release the record and identify the source she bought it from."', "good", "good"),
      temperament('"Give her subscribers something worth fighting over."', "chaos", "chaos"),
      temperament('"Take the profitable part of her collection while she still hopes to keep the rest."', "evil", "evil")),
    n("good", "Nurah", '''"And withdraw the grateful testimony. In the same edition, where people can find it."
"Will she agree?"
"She can keep selling the rest of her dreary family histories. That is more business than she deserves and less trouble than I intend to pursue forever."
{n}Nurah scratches out a sentence in the proposed settlement. It would have described Vhal as acting in good faith. She scratches it out again, through the first line.{/n}
"No pardon. She can behave herself for commercial reasons."
"You would enjoy ruining her more thoroughly."
"I would. I would also enjoy obtaining the record before she flees with it. Some days one must choose which pleasure arrives first."
{n}She moves the corrected demand toward you. The terms leave Vhal's unrelated collection intact in exchange for the original, its purchase history, and a printed correction naming Bressa without invented testimony. Nurah keeps the right to publish the letters exposing the bargain if the correction is withheld.{/n}
"Do not ask me to thank her when she signs," {n}she says.{/n} "I have used up my supply."''', c('[Support the narrow exchange and preserve the inquiry.]', "settle", flags=f("demand_record"))),
    n("chaos", "Nurah", '''{n}She lays out two dedication proofs and the subscriber list. Every exclusive claim has a rival. Every offended patron knows somebody who would enjoy hearing about the offense.{/n}
"Vhal returns the deposits or gives each subscriber the source material behind the rival claim. Their choice. We publish the choice before she can persuade them to make it quietly."
"Some will take the material."
"The interesting ones. She has cultivated their appetite for years. I would hate to see it go unfed."
{n}Nurah adds the sale record and its source to her own share of the settlement. Then she underlines the sentence permitting subscribers to compare the documents they receive.{/n}
"She will lose control of the collection. Pieces of it will turn up in family arguments for decades."
"And people outside those families?"
"Some names will become public. Some should have been public years ago. I cannot promise every beneficiary will be charming."
{n}She looks at you without apology. This is the part she enjoys: private pride made vulnerable to other people's malice, with herself deciding which door to open.{/n}
"We can make it smaller," {n}she says.{/n} "I will be less entertained, but I am willing to hear an interesting objection."''',
      c('[Release the rival source packets and let the subscribers choose their quarrels.]', "settle", flags=f("demand_rivals")),
      c('"Keep the quarrel to the paid dedications. Do not release unrelated names."', "limited", flags=f("demand_limited"))),
    n("limited", "Nurah", '''{n}Nurah draws a line around the dedication claims. The circle excludes most of the collection.{/n}
"You have made my evening smaller."
"I have kept it aimed at the people who bought it."
"You say that as though I had mistaken them for someone else."
{n}She studies the shortened terms, then changes the remedy. Vhal must distribute both exclusive dedications together, identifying which patrons paid for each. There will be fewer secrets released, but no subscriber will be able to claim he was the only person flattered.{/n}
"There. Their children can still quarrel over who was deceived more expensively."
"Can you live with that?"
"I can improve on it later."
{n}Her smile warns you not to treat the concession as a conversion. She keeps the excluded names in a separate fold and places them in her own pocket. You have limited this settlement. You have not acquired her curiosity.{/n}''', c('[Use the narrower dedication remedy.]', "settle")),
    n("evil", "Nurah", '''"Her supplier names. Her purchase records. The correspondence that distinguishes a source from a rumor."
{n}Nurah writes quickly. Vhal may keep the bound volumes and the contracts already fulfilled. The private papers that make the business profitable will pass to Nurah, including the sale record and the collector's acquisition notes.
In exchange, Nurah proposes withholding the recovered private correspondence from further publication. The copies already given or testimony already heard cannot be recalled. Vhal will be paying for what Nurah still controls; any separate promise of publication will have to be settled at the table.{/n}
"She may rebuild," {n}you say.{/n}
"Certainly. I intend to leave her enough ambition to try. If she finds another useful collection, I would like to hear about it."
"You could destroy the business instead."
"And waste the work? I dislike her, not her shelves."
{n}She looks up, measuring whether you mean to interfere. Her hand stays on the demand sheet.{/n}
"If you wanted me to become virtuous whenever profit entered the room, you have chosen a very tiring affection. I can offer you something much more entertaining."
{n}She leaves space for your answer beside the terms. The confidence in her face is genuine. So is the edge beneath it.{/n}''',
      c('[Back her demand for the sources and profitable private collection.]', "settle", flags=f("demand_collection")),
      c('"Keep the sale record and the evidence against Vhal. I will not help you acquire everyone else\'s secrets."', "refused", flags=f("demand_refused"))),
    n("refused", "Nurah", '''{n}Nurah sets down the pen very carefully.{/n}
"You waited until we had the buyer cornered to object to the purchase."
"I object to becoming another collector's enforcer."
"How grand. I was offering to let you share the interesting part."
{n}She takes the page back. For a while she writes without looking at you. When she returns it, the demand is limited to Bressa's record, its source, and the materials needed to expose Vhal's coercive offer.
The profitable supplier list is gone from the terms. Nurah has copied its title onto a separate scrap, which she does not offer you.{/n}
"I will make this settlement with you. If I later buy information from somebody else, do not congratulate yourself on having taught me otherwise."
"I did not ask you to pretend."
"Good. You would dislike how well I could do it."
{n}She lets the silence last. Then she adds the date of the meeting. She is still coming. She is no longer sharing every intention she has concerning the collection.{/n}''', c('[Accept the narrower joint operation and her continuing disagreement.]', "settle")),
    n("settle", "Narrator", '''{n}You accompany Nurah to Vhal's hired rooms. The collector has packed her books but left the traveling chest open. Edran stands beside it with a list.
Nurah puts the terms on the table. Vhal reads the first line and pushes the sheet back.{/n}
"The sale record is mine. I paid for it. Nothing said at that gathering transferred ownership to either of you."
"You offered it to me," {n}Nurah says.{/n}
"For work you have not supplied."
{n}Nurah puts her hand on the rejected terms. Vhal has begun with the one thing she knows Nurah came to take.{/n}
"Tell me what you think it is still worth," {n}Nurah says.{/n}
{n}The collector looks at you before answering.{/n}''',
      c('[Place the publicly witnessed tracing beside the demand.]', "witnessed_terms", requires=f("record_on_stand")),
      c('[Question the secretary who handled the withheld original.]', "missing_terms", requires=f("record_withdrawn"))),
    n("witnessed_terms", "Nurah", '''{n}You unfold the tracing. Vhal recognizes the subscriber's initials beside it.{/n}
"He had no authority to certify that."
"He saw it. If you dispute his memory, we can ask him to explain it again."
{n}Vhal reaches for the tracing. Nurah slides it back.{/n}
"Your original is worth the convenience of not finding another copy at the purchaser's end. I would enjoy the convenience. I will not perform gratitude to purchase it."
"Then why are you here?"
"Because you have other things to lose. We can discuss them together, or I can leave you to explain why an accurate history required selling its author her own witness."
{n}Vhal studies the initials once more. The subscriber is one of the people whose next commission she wants. Challenging his memory would give him another reason to reconsider it.
She tells Edran to bring the sheet and acquisition note to the table. He leaves them under Vhal's hand. They are available for the bargain now, not yet surrendered.{/n}''', c('[Negotiate with the identified original now on the table.]', "choose_terms", flags=f("record_leverage_witnessed"))),
    n("missing_terms", "Nurah", '''"You have a number copied from a private letter," {n}Vhal says.{/n} "You have not seen what it identifies. I could have been mistaken about the document myself."
{n}Edran looks down at his inventory. You turn toward him.{/n}
"Did you prepare that description?"
"He is my secretary," {n}Vhal says.{/n}
"Then he can distinguish your mistake from his."
{n}Nurah follows your glance and takes out a clean sheet.{/n}
"We are writing an account of the evening. Mrs. Vhal appears ready to explain that her staff supplied the wrong evidence. Would you prefer to have your own statement beside hers?"
"You would print what I wrote?"
"If you sign it. Including the part where you knew she was withholding the record."
{n}He looks at Vhal. She tells him to be quiet. That decides him more effectively than your offer.{/n}
"I described it correctly. I will say that. And who ordered me to take it out of the room."
{n}Nurah's mouth tightens. His statement will name his role, but also let him explain it in his own words. She will not control the whole account.{/n}''', c('[Give Edran space for his signed admission and explanation.]', "secretary", flags=f("secretary_statement"))),
    n("secretary", "Nurah", '''{n}Edran admits preparing the description and removing the original on Vhal's signal. He adds that he believed the reading legitimate until she made the record conditional on Nurah's praise.
Nurah draws a line beneath that sentence.{/n}
"You expect me to believe you noticed nothing before that?"
"I expect you to print what I have signed. That was the offer."
{n}She looks at you, annoyed, then writes a reply underneath: The editor had already circulated my imitation signature. She shows Edran both statements together.
He signs. He also opens the chest and lays the sale record beside his description. The catalog number matches. Vhal slams the lid after he removes the acquisition note.{/n}
"You are dismissed."
"He can finish identifying the papers first," {n}you say.{/n}
{n}Nurah places the statement beyond the collector's reach. You have an identified original at the cost of giving a compromised witness his own defense in the final account. Vhal cannot remove that witness by closing a chest.{/n}''', c('[Keep the witness\'s agreed statement and continue the bargain.]', "choose_terms")),
    n("choose_terms", "Narrator", '''{n}Bressa's record lies on the table. Nurah reads the purchaser's name once, then places the demand sheet beside it.
"Now the rest," she says.
Vhal has begun calculating what she can keep. Her gaze moves from the correspondence to the packed volumes by the door.{/n}''',
      c('[Exchange limited publication restraint for the correction.]', "bargain_record", requires=f("demand_record")),
      c('[Make retaining the rival claims more expensive than releasing them.]', "bargain_rivals", requires=f("demand_rivals")),
      c('[Leave unrelated papers outside the paired-dedication dispute.]', "bargain_limited", requires=f("demand_limited")),
      c('[Separate her private sources from the public business she hopes to save.]', "bargain_collection", requires=f("demand_collection")),
      c('[Hold to the narrower joint demand.]', "bargain_refused", requires=f("demand_refused"))),
    n("bargain_record", "Nurah", '''"A printed correction will follow every volume," {n}Vhal says.{/n}
"A refusal gives me a short book to print beside it. Your offer, my answer, and the price beside Bressa's name."
"You would destroy the edition for a footnote?"
"You risked it to invent one."
{n}Nurah opens the recovered letter. Vhal covers the paragraph offering the record, then withdraws her hand when she realizes how the gesture looks.{/n}
"If I correct it, you stop publishing this letter."
"I stop circulating reproductions of it. Copies already held belong to their readers. Witnesses can still give their accounts, including in mine."
{n}The collector demands the phrase editorial oversight. Nurah crosses out oversight and writes unsupported testimony. They argue until you place the sale entry beside the proposed correction and ask which word is inaccurate.
Vhal signs. Nurah signs the limited restriction on reproducing the letter while the correction stands, with witness accounts expressly excluded. She retains the right to publish the offer if Vhal removes that correction from later impressions.{/n}''', c('[Accept the limited publication restraint.]', "signed", flags=f("bargain_publication_limited"))),
    n("bargain_rivals", "Nurah", '''"The subscribers did not purchase my sources."
"Then return their deposits," {n}Nurah says.{/n} "All of them. Together."
{n}Vhal asks Edran for the account. The money has already paid for paper, binding, and this room. Nurah watches her reach the total.{/n}
"They can accept a rival packet instead. Most will consider it a better investment. You taught them that."
"Those families will never employ me again."
"If you cannot fulfill the dedications or return the money, they may reach the same conclusion with less amusement."
{n}Vhal demands a limit: only packets concerning the subscribers' disputed claims. Nurah counts them against the recovered list. They contain enough dangerous material to satisfy her.
She accepts. Unrelated boxes stay with Vhal. The specified packets retain their witness names and accusations; Vhal may not substitute an expurgated version.
The collector signs the list before Edran separates the packets from the chest. Nurah checks each one, refusing a promise of delivery after departure.{/n}''', c('[Take the specified packets and leave the unrelated remainder.]', "signed", flags=f("bargain_named_packets"))),
    n("bargain_limited", "Nurah", '''"Printing both dedications will humiliate my clients."
"They were promised something impossible," {n}you say.{/n} "You can explain it with the two pages, or Nurah can print the subscriber list with her own explanation."
{n}Nurah smiles and lays the list flat.{/n}
"I have written a very good opening. You would hate it."
{n}Vhal demands that unrelated household papers remain outside the publication. You agree. Nurah has already accepted that limit privately, but makes the collector wait while she reads it again.
The paired pages will identify both purchasers and amounts. Vhal may add her explanation that she offered separate issues. Nurah insists the original word exclusive remain visible above it.
Vhal signs. When Nurah adds her signature, the collector watches it with an expression that suggests she has finally learned why an imitation was easier.{/n}''', c('[Keep the paired pages and Vhal\'s explanation together.]', "signed", flags=f("bargain_paired_pages"))),
    n("bargain_collection", "Nurah", '''"Those sources are my livelihood."
"The volumes are your livelihood," {n}Nurah says.{/n} "The sources are why your clients sometimes pay twice."
{n}She turns the list toward Vhal. A second payment, entered privately, suppressed an earlier account. Vhal calls it additional research. Nurah asks whether the family would like to compare the invoices.{/n}
"You would destroy the value by publishing them."
"Yes. I would prefer you to sell me the value instead."
{n}Now they look like competitors who understand the same business.
Vhal demands that existing contracts remain hers and that Nurah approach no current client for a new commission until those contracts are delivered. Nurah resists the delay. You point to the suppliers and former clients outside that list. She checks the names, calculates, and agrees.
Vhal keeps a public trade to rebuild. The proposed transfer gives Nurah the private purchase records, supplier correspondence, and coercive material. Her first offers must go to former clients and people outside the protected list, rather than the easiest buyers she wanted.
The collector adds a prohibition on publishing evidence of the offer she made concerning Bressa. Nurah places her pen beside the sentence rather than signing it.{/n}''',
      c('[Reserve the secretary\'s promised statement before accepting the publication restriction.]', "statement_scope", requires=f("secretary_statement"), flags=f("bargain_clients_reserved")),
      c('[Accept the current-client delay and the restriction on publishing the recovered correspondence.]', "collection_agreed", forbids=f("secretary_statement"), flags=f("bargain_clients_reserved"))),
    n("collection_agreed", "Nurah", '''{n}Nurah changes evidence to recovered private correspondence and reads the revised sentence aloud. Vhal asks whether she intends to commission a witness to tell the same story for her.{/n}
"Not as a device to evade this exchange," {n}Nurah says.{/n} "People who were in the room may talk. I have promised you no power over their memories."
{n}Vhal accepts the wording. It protects the letters Nurah is acquiring without pretending the guests can be made to forget the reading.
Nurah signs beside the client restriction, then holds out her hand for the inventory. She will not sign the receipt until every listed packet has left the chest.{/n}''', c('[Complete the private collection exchange.]', "signed")),
    n("statement_scope", "Nurah", '''{n}Nurah places Edran's signed statement across the proposed restriction.{/n}
"This is reserved. It goes into my account exactly as he signed it, with my reply. We agreed before you offered the collection."
"I agreed to no such reservation," {n}Vhal says.{/n} "You obtained his help by promising to publish the very transaction I am paying you to stop publishing."
"Then pay for the letters. You cannot buy a promise I have already made to him."
{n}Vhal looks from the statement to the inventory. She strikes a name in the former-client column: the buyer who paid most lavishly to conceal an earlier history.{/n}
"That packet stays with me. The statement has reduced the silence I receive. It reduces the collection you receive in return."
{n}Nurah presses the pen against the table until its nib bends.{/n}
"Or," {n}Vhal continues,{/n} "you give my signed reply the same place beside his statement. No omissions. No invented commentary inside my words. Your objections may follow them. I intend to answer the allegation in the publication that carries it."
{n}Nurah turns toward you. She wants the packet. She also wants to deny the collector an audience purchased at her expense. Neither desire can be satisfied by pretending Edran's statement was already covered.{/n}''',
      c('[Keep Edran\'s statement unchanged and leave Vhal the named client packet.]', "reserve_packet", flags=f("collector_packet_reserved")),
      c('[Keep the full collection and print Vhal\'s signed reply beside Edran\'s unchanged statement.]', "reserve_reply", flags=f("collector_reply_reserved"))),
    n("reserve_packet", "Nurah", '''{n}You put a line through the packet on Nurah's copy of the inventory. Vhal draws the same line on hers, slower than necessary.{/n}
"The statement remains outside the publication restriction," {n}you say.{/n} "Its admission, its explanation, and Nurah's reply."
"Those pages only. The recovered private letters remain covered."
{n}Nurah writes the exception beneath that sentence and makes Vhal initial it. Then she watches Edran return the valuable packet to the chest. Its red cover disappears beneath the papers the collector still owns.{/n}
"I would have enjoyed that one," {n}Nurah says.{/n}
"You can decline the exchange," {n}Vhal answers.{/n}
"And deprive you of all the less expensive things you have lost? No."
{n}She signs. When Edran offers to thank her, she tells him to save his gratitude for the employer who next believes his account of himself.
The rest of the collection passes across the table. Nurah counts it twice, leaving the crossed-out name visible on top of her copy.{/n}''', c('[Accept the smaller collection and the explicit publication exception.]', "signed")),
    n("reserve_reply", "Nurah", '''"Write it now," {n}you tell Vhal.{/n} "Edran's statement stays intact. Your answer follows it, and Nurah's reply follows yours."
{n}Vhal asks for fresh paper. Nurah gives her the sheet with the disputed clause on its reverse.{/n}
"You may find it inspiring."
{n}The collector writes that she sought an authorized account and offered a rare document as compensation. She calls Edran an employee who misjudged her instructions. She acknowledges withdrawing the record, describing the act as protection against a hostile gathering.
Nurah reads the completed reply, then underlines the word compensation on her own sheet.{/n}
"You will leave it as written," {n}Vhal says.{/n}
"Every word. My readers may enjoy comparing your compensation with the praise you demanded for it."
{n}They attach both signed statements to the settlement. The publication exception names them and permits Nurah's separate response; the private correspondence remains restricted.
Edran sets the disputed client packet with the rest of the transferred collection. Nurah takes it without smiling. She has kept its value by giving Vhal room to defend herself in Nurah's next account.{/n}''', c('[Accept the collector\'s printed reply as the cost of the complete collection.]', "signed")),
    n("bargain_refused", "Nurah", '''{n}Vhal sees the deleted demand and offers the supplier list at a reduced price. Nurah looks at it. She does not reach for it.{/n}
"The record, its source, and the correspondence about this offer," {n}you say.{/n}
"Such admirable restraint," {n}Vhal replies.{/n} "Would installments preserve it?"
"Do not confuse my disagreement with the Commander for permission to insult me," {n}Nurah says.{/n}
{n}She pushes the list back. You offer to exclude unrelated papers from this account. Vhal demands that her present buyers remain unnamed except where they purchased the disputed dedication. Nurah adds an exception for anyone directly identified in the offer concerning Bressa.
After rereading the correspondence, Vhal accepts. The settlement is narrower than Nurah wanted and less damaging than Vhal feared. When the collector begins speaking of future opportunities, Nurah interrupts to ask for the acquisition note already promised.{/n}''', c('[Take the limited evidence without buying the wider collection.]', "signed", flags=f("bargain_scope_narrow"))),
    n("signed", "Narrator", '''{n}You compare the sale sheet's catalog number with the earlier reference. Nurah checks the date and witnessing marks against the acquisition note, then places both inside her book.
Edran reads the list of exchanged materials aloud. Vhal tries to exclude a letter named in the terms she just signed. Nurah turns the page toward her signature. The letter joins the others.
Nurah takes her own copy of the settlement last, folding it around the damaged proof.
In the street, she stops beneath a lamp and checks the record once more. Only then does she look at you.{/n}
"Next time I write a flattering biography, remind me to make the subject's enemies rich enough to buy it first."
{n}She puts the book away, takes your hand, and leads you toward the fortress before the cold can spoil her temper.{/n}''', c('[Leave with the exchanged evidence and the costs actually agreed.]', flags=f("settlement_finished", "bressa_record_obtained"))),
], "reading_confronted")


visit("the_copies_that_survive", "The copies that survive", [
    n("start", "Narrator", '''{n}Nurah brings the finished answer to your chambers in a plain wrapper. The name on the front is hers. There is no invented signature, no claim that the Commander commissioned a history of private conduct.
She puts it on your table and goes straight to the chair she prefers. You have moved it since her last visit. She moves it back before sitting down.
"Vhal has left," she says. "Edran sent the final inventory. Carrow has offered to edit my next work at a reduced rate."
"Will you employ him?"
"I am considering sending him a book with no pages and asking which errors he would improve."
She opens the wrapper. The settlement has produced something less tidy than Vhal's proposed edition, and Nurah appears pleased by that.{/n}''',
      c('[Read the secretary\'s statement she agreed to include.]', "statement", requires=f("secretary_statement")),
      c('[Examine the finished answer.]', "results", forbids=f("secretary_statement"))),
    n("statement", "Nurah", '''{n}Edran's admission appears before Nurah's answer. He names the withheld document and Vhal's order, then defends how late he claims to have understood the bargain.
Nurah has printed the whole statement, including that defense. Her reply below it is considerably less forgiving.{/n}
"He sent a revised version," {n}she says.{/n} "It contained fewer things he remembered doing. I kept the signed one."
"He still gets his explanation."
"Yes. That was the price. You need not remind me how fairly I have paid it."
{n}She turns the sheet over. Edran has also asked permission to use the account when seeking new employment. Nurah answered that she does not own his signature and recommends he find an employer who reads past the first paragraph.
The record itself lies safely inside her book. She touches its edge, then smooths the statement flat rather than tearing out the part she dislikes.{/n}''',
      c('[Check the missing client packet on her inventory.]', "packet_cost", requires=f("collector_packet_reserved")),
      c('[Read the collector\'s signed reply printed beside it.]', "reply_cost", requires=f("collector_reply_reserved")),
      c('[Keep the bargain\'s cost beside the evidence it obtained.]', "results", forbids=f("collector_packet_reserved", "collector_reply_reserved"))),
    n("packet_cost", "Nurah", '''{n}The crossed-out name remains on Nurah's inventory. Beside it she has written the amount that former client once paid for silence. She taps the figure.{/n}
"That is what his explanation cost us. I hope Edran finds it beautifully phrased."
"You kept the rest."
"I can count. So can Vhal. She has already offered that buyer a private consultation."
{n}Nurah folds the inventory with the publication exception facing outward. Edran's complete statement is printed, and the collector has no right under their settlement to demand its removal.
The missing packet has left Nurah with fewer profitable names. It has not diminished her interest in the ones she acquired.{/n}
"Next time we buy a witness with space in my book, remind me to find out who else will try to charge for the page."''', c('[Keep the actual loss on the inventory.]', "results")),
    n("reply_cost", "Nurah", '''{n}Vhal's reply follows Edran's statement without a word removed. Nurah has printed her own response below it, beginning with the price of the praise the collector calls an authorized account.{/n}
"She sent another version," {n}Nurah says.{/n} "This one blamed a misunderstanding with the editor. I told her we purchased the signed performance, not unlimited revisions."
"Her defense may persuade someone."
"Yes. That is why she wanted it here."
{n}Nurah closes the pamphlet and opens the red-covered client packet. The invoices inside are worth more than she expected. She lets you see the figures, then puts them away.{/n}
"There. My consolation. Do not expect me to enjoy reading her answer merely because I made a profit from it."
{n}The collector has her reply. Edran keeps his admission and explanation. Nurah keeps the full transferred collection, and her own final word beneath both accounts.{/n}''', c('[Keep the printed reply and the collection bought with it.]', "results")),
    n("results", "Narrator", '''{n}Nurah lays the finished pages between you. Corrections crowd the margin of her own copy. She has left yours clean, except for one small arrow pointing to the passage she wants you to read first.{/n}''',
      c('[Read the correction and follow the source inquiry.]', "record", requires=f("demand_record")),
      c('[Inspect the rival source packets released to the subscribers.]', "rivals", requires=f("demand_rivals")),
      c('[Read the paired dedications and their named purchasers.]', "limited", requires=f("demand_limited")),
      c('[Examine the collection she acquired from Vhal.]', "collection", requires=f("demand_collection")),
      c('[Read the narrower settlement after refusing the collection.]', "distance", requires=f("demand_refused"))),
    n("record", "Nurah", '''{n}The correction names Bressa, states the recorded sale, and withdraws the invented account of her gratitude. It offers no substitute speech in her voice. Vhal's signature appears beneath the acknowledgment that the testimony was unsupported.
Nurah taps the signature with evident pleasure.{/n}
"She asked to call it incomplete. I asked which part of a sentence she had entirely invented was merely missing. Edran advised her to sign."
{n}The acquisition note identifies the dealer who sold the record. Nurah has sent an inquiry with a copy of the witnessing marks. She has received a confirmation that the dealer's former clerk still works in the district, though not an answer about Bressa herself.{/n}
"That is the next person to ask," {n}she says.{/n} "I have paid the messenger. If there is an answer, it will come after the road has had its turn."
"Will you keep following it?"
"Yes."
{n}She gives you the answer without ornament, then turns back to Vhal's signature.{/n}
"I may frame this part while I wait. Somewhere ugly. It should feel at home."''', c('[Keep the correction and the still-open inquiry.]', "history", flags=f("outcome_correction"))),
    n("rivals", "Nurah", '''{n}Two subscribers took their deposits back. The others took documents. Within a day, three families had accused one another of paying to improve their ancestors, each brandishing a packet that proved the accusation against somebody else.
Nurah has received copies of the first angry letters. She reads the best sentences aloud, improving the voices as she goes.{/n}
"This one calls the other a merchant of inherited dishonor. His grandfather sold the same regiment its boots twice."
"And the unrelated names?"
{n}She turns a page. A clerk named in one packet has written asking that his former employer's accusation not be repeated as fact. Nurah has marked the letter for an answer. She intends to print his correction beside the accusation, which will make the family's history still more awkward.{/n}
"He has a witness. That makes him useful. I have asked for the witness's account."
{n}The quarrel has escaped the room in precisely the way she wanted. People with less money than the subscribers now have to answer pieces of it. Nurah is interested in those answers when they sharpen the dispute, and she does not disguise the interest as charity.
Bressa's record is separate from the packets. A copy has gone to a correspondent near the purchasing household. The original remains with Nurah.{/n}''', c('[Keep the released dispute and follow what it draws into the open.]', "history", flags=f("outcome_rivals"))),
    n("limited", "Nurah", '''{n}The revised dedication prints both exclusive claims on facing pages. Under each is the amount paid for the privilege. Nurah has insisted on identical type, so neither patron can accuse the other of buying larger letters after the fact.
The subscribers have demanded explanations from Vhal. Their quarrel concerns the edition itself. The unrelated household papers remain outside the publication.{/n}
"One has offered to buy every remaining copy," {n}Nurah says.{/n} "I asked whether he wanted them bound together. He did not appreciate the economy."
"You sound satisfied."
"I am enjoying the part we kept. You need not mistake that for agreement about the part you removed."
{n}She lays the paired pages aside. Bressa's sale record has been copied for an inquiry to the purchasing household's district. Nurah has retained the acquisition note and the original sheet.
There is no answer yet. While waiting, she has begun a short account of the subscribers' evening in which none of the wealthy guests can quite recognize himself without admitting that he paid to be flattered.{/n}
"You may read it when I have made you less obvious," {n}she says.{/n} "That will take the longest."''', c('[Keep the narrowed public quarrel and her unfinished account.]', "history", flags=f("outcome_limited"))),
    n("collection", "Nurah", '''{n}Nurah has arranged the transferred papers by usefulness. The largest stack concerns households that paid Vhal to conceal information while publicly praising the accuracy of her histories.
She has already written to two former clients outside the protected list. The letters offer private research services at prices calculated from what the recipients previously paid for silence.{/n}
"You have not wasted time."
"Neither have they. One former client tried to purchase his own file before Edran finished packing it. The present clients must wait until Vhal delivers their contracts. I have marked the dates."
{n}She shows you the offer, then the answer she sent. Her price is higher. She has no intention of transferring the only copy.
Bressa's record sits in a smaller folder with the acquisition note. Nurah has sent a query about the purchaser, partly to follow the woman's disappearance and partly to test a source named in the collection. She has kept the expense against the new business.{/n}
"Does everything become useful?" {n}you ask.{/n}
"No. Some things become expensive. I try to notice the difference before I acquire them."
{n}Her gaze settles on you, warm and deliberately appraising.{/n}
"You are making that calculation difficult. I resent it more attractively on some evenings than others."''', c('[Let her keep her collection, and name her own price for it.]', "history", flags=f("outcome_collection"))),
    n("distance", "Nurah", '''{n}The settlement releases Bressa's record and the evidence concerning Vhal's offer. The wider supplier list remains outside your joint undertaking. Nurah has copied the record for an inquiry and paid to have it carried to the purchaser's district.
She gives you the account without mentioning the separate scrap she kept when you refused her larger plan.{/n}
"You are waiting for me to ask," {n}you say.{/n}
"I am waiting to see whether you can resist."
"Have you bought another collection?"
"No. I have written a letter. It is my letter."
{n}You leave the question there. Nurah looks almost disappointed, then amused by the disappointment.{/n}
"We worked rather well together until you began editing my ambitions."
"We still obtained the record."
"We did. I am capable of remembering a useful partner while being annoyed with one."
{n}She puts the final inventory beside you and leans back in the chair. The scrap she kept stays folded in her sleeve, and she makes sure you see her not taking it out.
She folds the scrap into her sleeve, then closes her hand on yours.{/n}''', c('[Keep the record, and let her keep her scrap.]', "history", flags=f("outcome_distance"))),
    n("history", "Nurah", '''{n}Nurah rolls the wrapper into a narrow tube and looks through it at the finished pages.{/n}
"There. A much more respectable distance from the subject. Historians should be issued these."
{n}She lowers it when you laugh. The inquiry into Bressa has begun, but the present answer ends at a record, a purchaser, and a road someone still has to travel. Nurah has not written an ending for the woman simply because the edition needs one.
She sets the paper tube on your knee and waits to see whether you will look through it too.{/n}''',
      c('"I remember how you looked when Friedhelm returned as a soldier."', "soldier", requires=f("friedhelm_soldier_seen")),
      c('"Friedhelm also found a way to profit after taking your advice."', "rich", requires=f("friedhelm_rich_seen")),
      c('"The master who thanked us for Friedhelm\'s return would find this collection useful."', "sold", requires=f("friedhelm_sold_seen")),
      c('[Put the pages away and stay with Nurah.]', "done")),
    n("soldier", "Nurah", '''{n}Nurah's expression changes before she can improve it into a joke.{/n}
"He was very pleased with himself. People ought to warn me before doing that in public."
"You were pleased too."
"I survived it. Let us not dwell on the symptoms."
{n}She unrolls the paper tube, smoothing it against her knee. The gesture gives her something to do while she considers the comparison.{/n}
"Bressa may not want a uniform. Or a conversation with someone who remembers Trezbot. If we find her, I intend to ask what she wants before you begin recruiting a happy conclusion."
"I can ask a question without offering a commission."
"You can. I have observed occasional evidence."
{n}She gives you a sideways smile and steals the paper tube back before you can look through it again.{/n}
"I hope she has become troublesome. I would like to hear that she was expensive to keep."''', c('[Leave room for an answer that belongs to Bressa.]', "done", flags=f("friedhelm_recalled"))),
    n("rich", "Nurah", '''"He had excellent advice. I remember the adviser being exceptionally modest about it."
{n}She tilts the paper tube toward you like a toast, then abandons the joke and looks at the purchaser's name copied from the sale record.{/n}
"People with property are always astonished when somebody else develops an interest in owning it. That is one of their most enjoyable qualities."
"You expect Bressa to have done the same?"
"I know nothing about what she did after that entry. She may have escaped. She may have died. She may have found a way to make the household regret keeping accounts at all. I would prefer the last."
{n}She folds the wrapper around the smaller papers, tucking the corners in carefully.{/n}
"A preference is useful. It tells you which answer to celebrate if it arrives. It does not carry the message for you."
{n}She leans over to place the packet beyond your reach, then remains close enough to turn the movement into a kiss on your jaw.{/n}''', c('[Let the inquiry find its own answer.]', "done", flags=f("friedhelm_recalled"))),
    n("sold", "Nurah", '''"He would. That is one reason I would charge him more than he could afford."
{n}Her mouth tightens, then eases into a colder smile.{/n}
"He thought paying us had bought the right to be pleased with himself. I disliked the way he enjoyed it."
"You took the payment."
"Yes. You were there."
{n}She turns the sale record facedown beside the other papers.{/n}
"If you want to argue about the man, pick a night when I have not spent the afternoon reading collectors congratulate themselves. If you want to know whether I can still be bought, bring an interesting price. I would enjoy disappointing you."
{n}She takes the paper tube off your knee, and her hand stays there after the paper is gone.{/n}''', c('[Keep the remembered choice in its actual terms.]', "done", flags=f("friedhelm_recalled"))),
    n("done", "Nurah", '''{n}Nurah puts the packet in a drawer you have left empty for it. She notices the space and glances back at you.{/n}
"You have been expecting me to leave things."
"You already do."
"Those are usually the things I intend you to find."
{n}She closes the drawer, then opens it again to move the old praise letter behind the finished pages. When she shuts it the second time, she leaves it shut.
At the door she catches a split glove seam on the latch. She pulls the glove off and leaves it in your hand.{/n}
"Bring it next time," {n}she says.{/n} "I want to see whether you have hidden a proclamation inside."
{n}The other glove remains on her hand. She touches your cheek with it before she leaves.{/n}''', c('[Keep the glove for the next private evening.]', flags=f("copies_settled"))),
], "settlement_finished")


visit("a_margin_for_you", "A margin for you", [
    n("start", "Nurah", '''{n}You have the glove when Nurah arrives. She inspects the repaired seam, turns it inside out, and finds no concealed proclamation. Her disappointment is theatrical.{/n}
"A lost opportunity. You could have declared my fingers a protectorate."
"To the administrative burden. I have plans for them."
{n}She draws the glove on slowly, testing the seam by spreading her fingers. Then she takes it off again and puts it on the table beside the unlit lamp.
There are no proofs under her arm tonight. No list of paid subscribers. She notices you looking for them.{/n}
"The work is finished. For once I have come with nothing you need to correct."
"Unless you count your collar. That needs opening."
{n}She moves close enough to touch the fastening at your collar. Her attention stays on your face while her fingers test whether it will yield.{/n}''',
      c('"You started our first meeting by stealing the book out of my hands."', "teasing", requires=f("first_teasing")),
      c('"This greeting is missing an inconvenient witness."', "kiss", requires=f("first_kiss")),
      c('"Stay. We can leave the clever answers until morning."', "stay"),
      c('"Sit with me tonight. I would rather hear you than undress you."', "quiet")),
    n("teasing", "Nurah", '''"You were using it badly."
"You hid behind it. There is nothing to hide behind tonight."
{n}The fastening gives. Nurah looks down at her success with exaggerated surprise, then catches your hand before you can reach for hers.{/n}
"Patience. I am revising the order of events."
{n}She draws you toward the chair and sits you down in it, close enough that her knee presses yours. For a while she seems content to examine the face of the person who helped her ruin an evening, acquire an enemy, and get an old letter back. Her thumb moves along your jaw, stopping where she wants your attention.
You kiss the inside of her wrist. Her breath catches, briefly enough that she could deny it, and her fingers curl against your cheek.{/n}
"That was not in my order," {n}she says.{/n}
"Do that again."
{n}She leans down over the chair and makes a correction of her own, with her mouth, slowly, the way she strikes a line she means nobody to read again. Then she sits back far enough to take hold of the hem of her dress and stays there, deliberately, to see how long you will let her.{/n}
"Now," {n}she says, and takes your hands, and puts them at her waist, and leans down into you.{/n}''', c('[Let the private argument continue without an audience.]', "morning", flags=f("private_night"))),
    n("kiss", "Nurah", '''"I could ask someone to stand outside and become embarrassed at the appropriate moment."
{n}You rub two fingers together in a show of avarice. Nurah grins.{/n}
"Only if you insisted on being impressive."
{n}Her teasing falters when you draw her closer. She rests a hand against your chest, feels the movement beneath it, and looks up without the harmless smile she used for the servant.
The first kiss is brief. The second is her answer to its brevity. She pulls your collar open another inch and lets the cool air reach the place her mouth has warmed.{/n}
{n}Your questioning look earns a small, wicked smile.{/n}
"I am considering the ending. Be quiet while I work."
{n}You carry her the few steps to the bed. She keeps hold of your collar, laughing when the loose fastening catches in her sleeve, and when you set her down she does not let go of it; she pulls, and you come down with her.
Outside the room, someone passes without stopping. Nurah hears the footsteps, glances at the door, and turns back to you.{/n}
"Much better," {n}she says.{/n} "They have learned to miss the interesting part."
{n}She pulls you down beside her with a small grunt of effort, her hair closing round both your faces like a curtain.{/n}''', c('[Close the evening around the two of you.]', "morning", flags=f("private_night"))),
    n("stay", "Nurah", '''"That is a long time to leave you without assistance."
{n}She says it softly. Her fingers leave your collar and rest against the side of your neck. You feel the small movement when she swallows.
You draw her into an embrace. For a moment she stands still inside it, her face hidden against you. Then she reaches around your back and finds the seam she wants, pulling you closer by it.{/n}
"I am staying," {n}she says.{/n} "You may stop looking as though you expect me to turn into a letter."
"I have more than ink to work with tonight."
{n}She lifts her head. The smile that follows is slow and very much aware of what she has to work with instead.
When you kiss her, she takes her time answering. The lamp remains unlit. You know the way across the room without it, and Nurah discovers several reasons to delay you before you reach the bed: your belt, which she dislikes; your shirt, which she likes better on the floor; a kiss against the bedpost that she says is research.
At the bed she stops you with one hand flat on your chest and pushes, and you sit. She stands between your knees, which puts her eyes level with yours for once, and reaches behind her for the hooks of her dress without looking.{/n}
"I am staying," {n}she says again, quieter, and takes your face in both inky hands and pulls you down onto the bed with her.{/n}''', c('[Spend the night together.]', "morning", flags=f("private_night"))),
    n("quiet", "Nurah", '''{n}Nurah leaves the fastening open, as though declining to surrender the small victory entirely.{/n}
"A dangerous preference. I could talk until you regret it."
"And yet you continue inviting me. A mystery for a more diligent historian."
{n}She sits beside you and tucks her feet beneath the edge of the cover. After a while she tells you about a copyist in Isger who could imitate six noble hands but could never make his own accounts add up. The story becomes increasingly insulting as she remembers details. You suspect she has supplied several new ones.
When you point this out, she tells you which detail was invented and refuses to identify the rest.
Later you read a page of her unfinished account aloud. She interrupts to change a word, then another, until you put the page aside and ask whether she intends to dictate the entire night. Her laughter subsides against your shoulder.
She stays there after the laughter is over. The conversation wanders into less polished things, and neither of you reaches for a pen.{/n}''', c('[Keep the quiet night she chose to share.]', "morning", flags=f("private_quiet"))),
    n("morning", "Narrator", '''{n}Near morning, Nurah opens the drawer with the finished pages. She takes out the old letter and places it inside her own copy of the book. The rest remains where you left it.
"That one travels with me," she says. "You can keep the improved edition."
Vhal's book is finished, and so is Vhal. There is no proof left to fight over and no courier waiting on the stair. Nurah has other schemes, and you have a crusade that has never had much respect for anybody's private plans.
She stands beside the drawer with her own book under her arm, watching you, with the candle-wax from the fourth step still under one thumbnail.
"Well, Commander. The book is done. Say something I can quote."{/n}''',
      c('"Bring me the next scheme before you sell the interesting part to someone else."', "partners"),
      c('"Bring yourself. I would like some evenings that do not begin with a forged dedication."', "lovers"),
      c('"Keep the stair. Use it when you like. I won\'t ask when."', "old_bond")),
    n("partners", "Nurah", '''"Before I sell it? That depends on the price."
{n}Nurah considers the proposal with entirely unnecessary seriousness. Her hand remains on the book containing the old letter.{/n}
"I will bring you the schemes that improve when you are involved. You will tell me when you intend to become principled halfway through one. We may still disagree. I am keeping that part."
"Good. I would hate to begin our next undertaking by disappointing you predictably."
{n}She takes the repaired glove and touches its seam to your mouth. The gesture lasts only a moment, but her gaze stays on you after she lowers her hand.
At the door she looks back.{/n}
"I have not promised to become less trouble."
{n}Her laugh follows her into the passage. The next scheme will need its own invitation and its own occasion. This one is finished, and the book on your table has the right author's name.{/n}''', c('[Finish this undertaking as lovers and willing accomplices.]', flags=f("complete", "ending_partners"))),
    n("lovers", "Nurah", '''"An ambitious request. I do enjoy a forged dedication."
"I could bring an authentic insult instead. Something written especially for you."
{n}She steps between your knees and lays the repaired glove across one of them. Her bare hand finds yours.{/n}
"There will still be things I want that you dislike," {n}she says.{/n} "And people who think your taste has become indefensible."
"Then we should give them something worth improving it over."
{n}She kisses you with no hurry at all. When she draws back, her expression has become mischievous again.{/n}
"Next time, no proofs. Unless they concern your conduct. I reserve the right to make careful observations."
{n}She leaves with her book and the old letter. The completed edition stays in your drawer. Its margin contains a small correction she made while you were looking elsewhere: beside a solemn reference to the Commander's judgment, she has written, occasionally excellent taste.{/n}''', c('[Finish this undertaking with room for more private evenings.]', flags=f("complete", "ending_lovers"))),
    n("old_bond", "Nurah", '''{n}Nurah studies you for a moment, then slips the repaired glove into her pocket instead of putting it on.{/n}
"I was wondering when you would try to make the arrangement sound less like a meeting of editors."
"A necessary disguise. You are much easier to summon when somebody has misused your name."
{n}She straightens the open fastening at your collar without closing it, the way she would straighten a page she has decided to keep.{/n}
"I will come when I choose and when we can make it possible," {n}she says.{/n} "You may write if you miss me. Try to include something worth answering."
"I will consider whether you have made it sound interesting."
{n}She kisses your cheek before you can offer a revision. At the door she turns the book over in her hands, checking that the letter remains inside.
On the stair you hear the fourth step squeal. She has scraped off her own wax, so that you will always know when she is coming. You keep the finished pages. She keeps the stair. Three evenings later the fourth step squeals again; she comes in with her book and a complaint about the watch at the gate.{/n}''', c('[Let her go down the stair.]', flags=f("complete", "ending_old_bond"))),
], "copies_settled")


def integrate(payload):
    """Register read-only source bindings; root owns scenes and runtime delivery."""
    for name, bindings in (("Etudes", ETUDES), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(name, {})
        for key, value in bindings.items():
            if key in target and target[key] != value:
                raise ValueError("Conflicting Nurah source binding: " + key)
            target[key] = deepcopy(value)
    relationships = payload.setdefault("Relationships", {})
    if "nurah" in relationships and relationships["nurah"] != RELATIONSHIP:
        raise ValueError("Conflicting Nurah relationship registration")
    relationships["nurah"] = deepcopy(RELATIONSHIP)


# Round 2: correspondence never records Nurah's physical arrival.
_mail = next(s for s in SCENES if s['Id'] == 'nurah.borrowed_name')
_mail.update(Kind='letter', Parcel=True, Sender='Nurah')

# Keep the letter-night's legacy exit and its receipt on the original near node.
_night = next(s for s in SCENES if s['Id'] == 'nurah.the_letter_she_wrote')
_near = next(n for n in _night['Nodes'] if n['Id'] == 'near')
_before, _after = _near['Text'].split('{n}In the morning', 1)
for _node in _night['Nodes']:
    for _choice in _node['Choices']:
        if _choice.get('Next') == 'near':
            _choice['Next'] = 'near.build_up'
_near['Text'] = '{n}In the morning' + _after
_night['Nodes'].append(n('near.build_up', 'Nurah', _before,
    c('Continue', 'nurah.the_letter_she_wrote.explicit.1'), portrait='Nurah'))
# Brief: established lovers choose a night while Vhal's plot remains unresolved.
_night['Nodes'].append(n('nurah.the_letter_she_wrote.explicit.1', 'Narrator',
    '{n}Nurah braces a hand beside your head on the mattress and leans down to kiss you. '
    'Her other hand slips to your belt; the cold lamp and the letter stay out of reach on the table.{/n}', c('Continue', 'near'), portrait='Nurah'))

_margin = next(s for s in SCENES if s['Id'] == 'nurah.a_margin_for_you')
for _nid, _number, _cut in (
    ('teasing', 1, '{n}She settles against you in the chair, bare shoulders warm beneath your '
     'hands, and kisses away the clever answer you were about to give.{/n}'),
    ('kiss', 2, '{n}Nurah presses closer, her open bodice brushing your chest. '
     'Her hand finds your belt while her mouth keeps yours occupied.{/n}'),
    ('stay', 3, '{n}Nurah pulls you close on the bed and catches your mouth again. '
     'When the passage falls quiet, she draws your hand down her bare side.{/n}'),
):
    _branch = next(n for n in _margin['Nodes'] if n['Id'] == _nid)
    _slot = 'nurah.a_margin_for_you.explicit.' + str(_number)
    _branch['Choices'][0]['Next'] = _slot
    # Brief: deepening on this branch, never a second first night or quiet sex.
    _margin['Nodes'].append(n(_slot, 'Narrator', _cut, c('Continue', 'morning'), portrait='Nurah'))


# Heat pass: each build-up reaches the start of the act; the cuts lead into the reserved segments.
_HEAT = {
    ('nurah.the_letter_she_wrote', 'near.build_up'): '''
{n}Her mouth goes down your throat in quick, hungry bites, and her laugh is short and low against your skin.{/n}
"I have spent a month writing other people's passion. I want you here, and I want you loud." {n}Her breath is ragged at your ear and her fingers are quick at your belt.{/n}''',
    ('nurah.a_margin_for_you', 'teasing'): '''
{n}Her mouth is on your throat as she works your shirt open one button at a time, and she hisses in satisfaction at what she finds. The chair groans, and neither of you can pretend to be amused.{/n}
"Revisions," {n}she pants,{/n} "are best done by hand."''',
    ('nurah.a_margin_for_you', 'kiss'): '''
{n}She kisses you again, deeper, then pulls back with a wicked look and tugs your belt loose.{/n}
"There. Now you are as exposed as my footnotes."
{n}The laces of her bodice slip under her fingers while she watches your face.{/n}''',
    ('nurah.a_margin_for_you', 'stay'): '''
{n}The bed takes your weight; she takes the rest. Her mouth drags down your throat and her fingers close hard on your hip, and she smiles with her teeth when your breath breaks.{/n}
"I am staying," {n}she says a third time, as if the word were a thrilling new vice,{/n} "and I intend to be thorough."''',
}
_CUT = {
    'nurah.the_letter_she_wrote.explicit.1': '{n}The dress comes off in the dark, and the rest follows. Her skin is hot under your hands, her ink-stained fingers are fisted in your shirt, and her breath breaks against your ear. "Mine," she murmurs, "for the length of one letter." The cold lamp and the old letter stay out of reach on the table.{/n}',
    'nurah.a_margin_for_you.explicit.1': '{n}She kisses away the clever answer you were about to give, and the chair takes the rest of the argument. Her skin is warm under your hands, the hem of her dress rides up, and "I am not done editing" is the last thing either of you says for a long while.{/n}',
    'nurah.a_margin_for_you.explicit.2': '{n}The laces give, her hair falls round you both, and her mouth finds yours again, open and unhurried. Skin, breath, the complaint of the bedframe. In the corridor the footsteps pass. "They still miss the interesting part," she whispers against your lips.{/n}',
    'nurah.a_margin_for_you.explicit.3': '{n}She kisses a path to your ear and draws your hand along her bare side. "Chapter and verse," she murmurs, breathless, and the dark keeps the rest of it.{/n}',
}
for _scene in SCENES:
    for _node in _scene['Nodes']:
        _key = (_scene['Id'], _node['Id'])
        if _key in _HEAT:
            _node['Text'] = _node['Text'].rstrip() + _HEAT[_key]
        elif _node['Id'] in _CUT:
            _node['Text'] = _CUT[_node['Id']]
