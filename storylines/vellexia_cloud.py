"""Vellexia: cloud voice-owner pass (villain-route-vellexia, design-first).

Applied last in vellexia_trickster.integrate, after the opening, the campaign,
the Trickster returns and their ending paragraphs exist. Text and flag-gated
read-only paragraphs only: no scene, node or choice id, choice position, Next,
Set, gate, check or cost changes. New paragraphs are appended after the
existing ones. Review and machine truth table:
tools/route_packs/redesign/vellexia/cloud-review.md and truth-table.json.

Structure fixed here (readers for flags the route already sets):
  * promises with no reader: the Commander's choice between breaking Ilveris's
    trade in public and challenging him (method_first / challenge_first), the
    way Tessar is taken (clerk_terms / shared_account), the first kiss and the
    held hand of Chapter 4 (first_kiss / held_close), what the Commander said
    the picture showed (noticed_expectation), and the week the mirror or the
    portrait waited in Orrel Vask's crate (trickster.cost.late) now each have a
    later consumer;
  * renewed_slow is set both by a hesitant answer and by the Trickster's "You.
    Not a debt, not a trick." (it also sets trickster.courting); the one node
    where the two meanings diverge (two_unremarkable_pleasures:company_end)
    gets a courting-gated line, so the declaration is not forgotten;
  * ending_dead never read the native VellexiasSlavesFreed etude
    (vellexia.slaves_freed): it does now.

Prose that failed (CHARACTER-TRUTH 2, binding context 6): the Chapter 5
Ilveris arc ran on sealed packets, deposits, columns, second clerks, receipts
and a "published account"; Chapter 4 haggled over an artist's balance and a
price reduction; the shell gift carried the banned "nobody is inside them"
reassurance; the opening line was the flat "A hopeful opening" her voice page
names. The arc keeps every beat and choice meaning, but the menace is on
screen now: the runner kept as a hat-stand, the clerk in the blue room among
the chairs, the broken finger, the purchasers collecting from Ilveris on her
salon floor, Ilveris made into a footstool when his wager fails.

Canon used (enGB, other speakers about her; her own pack is empty): 51d80804
(old, cruel, insane; senseless violence), 8115c490 / a24eb961 (Wenduag),
cd35d1f0 (Sosiel), 3dce2b36 / eae0b475 (the arena date, its champion and the
guest who claimed him). Authored, no canon claim: Ilveris, Tessar, the blue
room, the coat-stand, the lamp with a wrist (furniture is canon: Velexia_Third_Date
Cue_0075 per writer handoffs/trickster/vellexia.md).
"""
from story_format import p

V = "vellexia."
T = "vellexia.trickster."
INVITES = (V + "the_second_invitation", V + "the_second_invitation_drezen")

# ---------------------------------------------------------------------------
# 1. Substring substitutions: (scene ids, old, new, minimum hits) on node Text.
# ---------------------------------------------------------------------------
SUBS = [
    # Chapter 4: the artist's balance and receipts stood in for menace.
    ((V + "second_painter",),
     "Astonishingly, he left with all his fingers; I considered mentioning it in his receipt.",
     "He is waiting in the entrance hall beside the coat-stand, and he has begun to notice that the coat-stand has a face. Astonishingly, he still has all his fingers. I was so looking forward to deciding which ones.", 1),
    ((V + "second_painter",),
     '''I shall ask him to bring the price of the old panel as well."''',
     '''I shall ask him where the old panel came from, who painted it, and whether they are still alive."''', 1),
    ((V + "second_painter",),
     '''"Because he will expect an argument about beauty. I would like to hear him explain a bill."''',
     '''"Because he expects an argument about beauty. I would like to watch him sweat over a provenance."''', 1),
    ((V + "second_painter",),
     "From him, I intend to demand a price reduction.",
     "From him, I intend to demand something he will miss.", 1),
    ((V + "the_price_of_tomorrow",),
     "He has not seen the work. He has seen an invoice describing the reduction in price.",
     "He has not seen the work. He has heard our artist describe the label on its back, in every wine-house below the bridges, with gestures.", 1),
    ((V + "the_price_of_tomorrow",),
     '''"Would you have kept it without the reduction?"''',
     '''"Would you have kept it without the label?"''', 1),
    ((V + "the_price_of_tomorrow",),
     '''"Our artist apparently sold his revised bill as a sample. I shall not purchase his next apology. He may keep it for a more hopeful collector."''',
     '''"Our artist apparently sold Ilveris the story of his visit here. I shall have to decide what to do with a painter who sells my rooms by the yard. Something with his hands, I think. He is so proud of them."''', 1),
    ((V + "the_price_of_tomorrow",),
     "I dislike that more than the invoice.",
     "I dislike that more than the picture.", 1),
    ((V + "the_price_of_tomorrow",),
     "We shall have to charge him for it somehow.",
     "We shall have to make him pay for it somehow, and I do not mean in silver.", 1),
    # The shell gift: voice.md never_souls names this exact reassurance.
    ((V + "the_unused_reply",),
     "Before you ask: no, nobody is inside them. Shells, silver, and a fee she still boasts about.",
     "Shells, silver, and a fee she still boasts about. I let her keep her tongue for the boasting. She understood me; I reward that.", 1),
    # Chapter 5: the clerk's sample and the silver.
    (("vellexia.the_clerks_own_price",),
     '''"I can imagine several prices."''',
     '''"I can imagine several things I could make of you instead."''', 1),
    (("vellexia.the_clerks_own_price",),
     '''"I could not afford another year of paying for his unsuccessful predictions."''',
     '''"I could not survive another year of being his demonstration."''', 1),
    (("vellexia.the_clerks_own_price",),
     "Tessar takes the silver and leaves. You hear the clasp click as she checks her case twice, then the door opens and shuts.",
     "Tessar takes her book and leaves, walking, very carefully, as if the floor of this house might change its mind about her. You hear her pass the hat-stand in the hall, then the door opens and shuts.", 2),
    ((V + "the_wager_with_an_edge",),
     "Ilveris will seal one named result before the draw, and copies of the seal will be witnessed by purchasers who have deposits at risk.",
     "Ilveris will seal one named result in his book before the draw, and three of his own purchasers will watch the wax go on, men who would very much like to see it broken.", 1),
    ((V + "an_hour_that_counts",),
     "He considers pride a predictable weakness. I am about to give that opinion a costly audience.",
     "He considers pride a predictable weakness. I am about to give that opinion a costly audience. If he is wrong, he has promised me himself, and I have already chosen the corner.", 1),
    ((V + "an_hour_that_counts",),
     '''"Your object, Ilveris. My hour. Leave before you spoil the more expensive one." Tessar counts the forfeit before letting him take it.''',
     '''"Your object, Ilveris. My hour. Leave before I remember how much I liked it." He takes the circlet and backs to the door without turning round, past every chair in the hall, and does not breathe properly until he is in the street.''', 1),
    ((V + "an_hour_that_counts",),
     '''"I have an hour I had reserved for being vindicated in public. It has become available for a less improving occupation."''',
     '''"They can finish without me. I had reserved this hour for being bored by the end of it. It has become available for a less improving occupation."''', 1),
    ((V + "an_hour_that_counts",),
     '''"I thought of inviting people to hear the account. Then I imagined the third person congratulating me on my insight, and the pleasure began to curdle.''',
     '''"Half of them will come up these stairs to congratulate me on my insight. I can already hear the third one, and the pleasure is beginning to curdle.''', 1),
    ((V + "an_hour_that_counts",),
     '''"I expected to spend tonight humiliating a man in front of people whose opinions I would dislike by morning. Instead I have humiliated him in writing and found a better use for the remaining time."''',
     '''"I expected to sit on those stairs until dawn. Instead they have dragged him out into the street to finish their conversation, and I have found a better use for the remaining time."''', 1),
    ((V + "an_hour_that_counts",),
     '''"Several. I would have enjoyed his face when he lost. I would also have disliked hearing him describe the loss as part of his plan. You have deprived me of both."''',
     '''"Several. I would have enjoyed keeping him. I would also have disliked hearing him describe it afterwards as part of his plan. You have deprived me of both."''', 1),
    ((V + "an_hour_that_counts",),
     '''"Tessar will send the final receipts. Once I have paid them, this is finished.''',
     '''"Tessar has taken his purchasers and gone. Once I have decided what to do with his book, this is finished.''', 1),
    ((V + "an_hour_that_counts",),
     "Ask it when I can answer without pretending we are still discussing an invoice.",
     "Ask it when I can answer without pretending we are still discussing a little man with a book.", 1),
    ((V + "the_question_after_business",),
     "Tessar has her silver. Ilveris has his result.",
     "Tessar has his purchasers. Ilveris has whatever he has left.", 1),
    ((V + "the_question_after_business",),
     '''After a while she tells you that Tessar demanded her last payment before letting Ilveris hear the corrected account, and held the door shut on his man until the silver was counted; the clerk, it seems, has learned something in her house worth keeping.{/n}
"I considered correcting the omission," {n}Vellexia says.{/n} "Then I decided I preferred having one person leave my house surprised."''',
     '''After a while she tells you that Tessar now sells tomorrows herself, at twice his price, and that the first thing she did with her new trade was predict, to the day, which of Ilveris's old purchasers would come to her first. She was right. She sold the prediction to Vellexia.{/n}
"I bought it," {n}Vellexia says.{/n} "Then I told no one. I preferred having a few people leave my house surprised."''', 1),
    ((V + "the_voice_after_the_abyss",),
     "Vellexia has put the final account into the same narrow case that once held Ilveris's silk. She opens it where you can see the papers arranged inside.",
     "Vellexia has Ilveris's book in her lap, the silk cover scuffed where a good many boots have stood on it. She opens it where you can see the forged pages, each one marked in Tessar's red.", 1),
    ((V + "the_voice_after_the_abyss",),
     '''"Tessar chose her next work herself. I offered another commission. She declined it, politely enough to make it difficult to enjoy being insulted."''',
     '''"Tessar has his purchasers and a room of her own. I offered her a place in this house. She declined it, politely enough to make it difficult to enjoy being insulted."''', 1),
    ((V + "the_voice_after_the_abyss",),
     '''"She wants two patrons who cannot agree on a reason to dismiss her. I understood the calculation. I disliked being included in it."''',
     '''"She says she has seen my hall, and would rather have two patrons who hate each other than one who collects. I understood the calculation. I disliked being included in it."''', 1),
    ((V + "the_voice_after_the_abyss",),
     '''She sends the account; I send the silver; our opinions of one another remain exquisitely overpriced."''',
     '''Every month she sends me a prediction about somebody I dislike. She is right far more often than he ever was. I have not decided whether that makes her useful or dangerous, and she knows it, and she still sends them."''', 1),
    ((V + "two_unremarkable_pleasures",),
     "There is no invoice to explain the remark.",
     "There is no wager to explain the remark.", 1),
    # Arueshalae's house (the pair rows are voiced in harem_rows/zzz_vellexia_pairs.py).
    # Endings that only reported.
    ((V + "ending_dead",),
     '''{n}Vellexia died. The shell could carry no answer from her. It had never contained the woman whose voice had used it.{/n}
{n}The Commander remembered her appetite for novelty, her cruelty, and the rare pleasure of having genuinely surprised her.''',
     '''{n}Vellexia died, and the shell never lit again. It had never contained the woman whose voice had used it.{/n}
{n}The Commander remembered her appetite for novelty, her cruelty, the lamp that had a wrist and the coat-stand that had a face, and the rare pleasure of having genuinely surprised her.''', 1),
    ((V + "ending_hostility",),
     '''{n}Violence overtook the invitation Vellexia had made. The shell did not preserve a safe, unchanged hostess somewhere beyond the quarrel. An earlier pleasant hour was no guarantee that either could resume the conversation that followed it.{/n}
{n}There was no new agreement between them. The recollection of her laughter remained exact and insufficient.{/n}''',
     '''{n}It ended in violence, as her affairs generally did, except that this time the guest struck first. Whatever she had meant to offer the Commander over the ring tray, she never finished offering it, and the shell on the Commander's table stayed as dark as a shut eye.{/n}
{n}No new invitation came. The Commander kept the memory of her laughter exact, and it was never enough to make the rest of the memory pleasant.{/n}''', 1),
    ((V + "ending_coercion",),
     "The Commander's demonic rage had frightened Vellexia into surrender. Her old invitations could not disguise what followed as affection, and she never pretended that they could.",
     "The Commander's demonic rage had frightened Vellexia into surrender. She had spent millennia making other people into things; she knew precisely what it meant to be handled like one, and she never pretended that her old invitations could disguise it as affection.", 1),
    ((V + "ending_interrupted",),
     "{n}The reunion went no further. Vellexia had other amusements, and no further meeting with the Commander was arranged.{/n}",
     "{n}It went no further. Vellexia had other amusements, and she was not a woman who waited: by the end of the season a new guest sat in the chair beside her ring tray, and was considerably less interesting, and did not last.{/n}", 1),
    ((V + "ending_changed",),
     "{n}The Commander changed beyond the life in which Vellexia had wanted a guest. She would not pretend that the old invitation answered for this altered existence.{/n}",
     "{n}The Commander changed beyond the life in which Vellexia had wanted a guest. She heard what the Commander had become, laughed once, and had the chair beside her ring tray carried away. She would not pretend that an old invitation answered for this altered thing.{/n}", 1),
]

# ---------------------------------------------------------------------------
# 2. Whole-node rewrites: (scene ids, node id, guard substring of the old text, new text).
# ---------------------------------------------------------------------------
NODES = [
    ((V + "unfinished_likeness",), "start", '"A hopeful opening.',
     '''{n}Vellexia turns a narrow silver bracelet around her wrist. Its clasp clicks once, then again. At your question her fingers stop, and her whole face lights up.{/n}
"A new guest who asks what interests me! How exciting. Most of them walk in and tell me what ought to. I keep the ones who tell me twice; you passed a few in the hall."
{n}She leads your gaze toward a picture standing backward against a low table. Its frame is dark, plain wood, conspicuously severe among the room's ornaments: the chairs that do not quite sit square, the lamp in the corner held up by something with knuckles.{/n}
"That arrived this morning. An artist promises that it will reveal a part of me I have never seen. Imagine! I have been alive since before this city had a name. I believe he allowed himself three days."
"Have you looked?"
"Of course. I saw an extremely handsome woman looking as though somebody had promised her a revelation. So far, the picture is admirably accurate. I am not yet bored. He had better hurry."
{n}She studies you over the bracelet.{/n}
"Would you like to be useful, sweetheart, or would that ruin your entrance?"'''),
    ((V + "unfinished_likeness",), "terms", "Such a lovely, ruinous word.",
     '''"He said it would surprise me. I asked whether he meant once or whenever I looked. He said whenever. Such a lovely, ruinous word."
"And you paid him?"
"Half. He wanted all of it. I told him the other half would be paid in whatever condition he was in when the picture stopped surprising me." {n}She glances, fondly, at the lamp in the corner. Its stand has a wrist.{/n} "He also insisted the workings were his secret. I agreed to leave them alone until he returned. I keep my word when it amuses me."
"You want me to break that agreement for you."
{n}She laughs, delighted by how quickly you have reached the possibility.{/n}
"I want to discover whether you would. But no. Today I want you to look. You have had fewer centuries to practise being disappointed. Perhaps you will notice what I am overlooking."
"What happens to him if I don't?"
"Then I shall find out for myself, and I am so much less patient than you. That lamp was a sculptor. He promised me marble that breathed. I made certain something in the room did."
{n}She turns the frame toward you.{/n}'''),
    ((V + "price_of_novelty",), "answer", "I could keep it at a lower price.",
     '''"I could keep it. He would leave this house with half his fee and the knowledge that I own a thing he lied about, which ought to keep him awake for a century. Or I could send it back with him and let him explain to his next patron why I refused it."
"You make both sound unpleasant."
"They are unpleasant. He attempted to sell me my own vanity as a discovery. I do not intend to thank him."
{n}She studies the picture, then you.{/n}
"But you have been entertaining, and I would like your preference before I give mine. Keep the disappointing object and learn what it can do, or enjoy the cleaner pleasure of sending it away?"
"Will my answer decide his safety?"
"No. I decided that when he walked in. He is worth far more alive, with all his fingers, telling the Upper City what happens to people who sell me surprises that do not surprise. Painters gossip so beautifully when they are frightened."
{n}Her tone makes his survival sound like a whim she has not yet tired of.{/n}'''),
    ((V + "price_of_novelty",), "keep", "Curiosity defeats indignation.",
     '''"Curiosity defeats indignation. I approve, though I would have enjoyed a little more indignation first."
{n}She rings a small bell. The artist comes in from the hall, walking wide around the coat-stand.{/n}
"I am keeping your picture," {n}she tells him.{/n} "With an honest label. You will paint it on the back yourself: 'This does not do what he said.' In your best hand, darling. I want my visitors to admire the lettering."
{n}He paints it. His brush shakes on the third word, and she makes him begin the line again. When he has finished, she counts the rest of his fee into the palm of the hand that shook, one coin at a time, slowly enough that he has to keep holding it out.{/n}
"There. I have purchased a flawed invention with an accurate label. My reputation may never recover."
{n}She puts the key beside your hand after he has gone.{/n}
"Next time we shall try looking together. I suspect it will find that much less comfortable."'''),
    ((V + "price_of_novelty",), "return", "A remarkably expensive way to preserve a standard.",
     '''"A remarkably expensive way to preserve a standard. I like it better when somebody else proposes it."
{n}She calls the artist in. He wraps the picture while she watches his hands, and when he asks, very quietly, about the unpaid half, she has him kneel on the rug and read his original promise aloud to the coat-stand. The coat-stand listens. Halfway through, he understands what it is, and his voice goes thin and careful and stays that way to the last word.{/n}
"Thank you," {n}Vellexia says.{/n} "He was a poet. He does so like to hear other people's work. Go."
{n}He goes, with the picture and without the half. After the outer door closes, she returns to the empty table.{/n}
"Gone. I find that I wanted the picture more once I had decided to refuse it. An irritating discovery. You owe me another."
"I did not make his promise."
"No. You made yourself interesting while he was reading it. That is less enforceable, and far more dangerous to you."
{n}She draws a chair toward the cleared space. It is an ordinary chair; you check.{/n}
"Come back. We shall attempt a portrait without purchasing another artist's disappointment."'''),
    # Chapter 5: Tessar comes to the blue room instead of selling an account by post.
    (INVITES, "evidence", "He had it printed,",
     '''"Good. A witness who changes the past to please me would be almost as useless as Ilveris. Less amusing, because I would have no reason to be surprised."
{n}She holds a printed sheet close enough for you to make out a few lines: questions she asked at her reception, and under each one several possible answers. Some resemble things you might have said. Others turn you into a pompous caricature.{/n}
"He had it printed," {n}she says.{/n} "Before our first evening, he claims. The boy who brought it to my door is still in the hall." {n}She turns the shell. By the door stands a hat-stand of pale, polished wood with a little brass cap on top and, under it, a face that has not finished being surprised.{/n} "He was very rude about my reception. I kept him for the pleasure of telling his master."
"The list could have been written afterward."
"Certainly. Or copied from someone who heard me ask the same questions of another guest. I am ancient, darling, not inexhaustible."
{n}She lowers the page.{/n}
"Then, this morning, something interesting. His clerk came to my door. Tessar. She says she wrote half his predictions in her own hand and knows which half were written after the fact, and she would like to tell me so, in return for walking out of this house on her own feet. I have put her in the blue room. She has been looking at the chairs for an hour. I want you to hear her before I decide whether she is a witness or an ottoman."'''),
    (INVITES, "clerk", "She is employed, darling, not chained.",
     '''"Do not make her a chair. How very Golarian of you, to say it before I had." {n}Vellexia laughs.{/n} "She is my guest, sweetheart. Ilveris pays her; I have not acquired her. If I had, she would be a very pretty chair by now, and she knows it. That is why she is so beautifully honest."
"A witness who walks out of here on her own feet is worth more to us than another piece of furniture."
"Is she? Very well. One account, and she walks. I want her accurate enough to shame him before everyone who ever bought from him, and frightened enough of me to stay accurate afterwards."
"And afterward?"
"Afterward she will repeat the story wherever it does him the most harm. She will not be able to help it. People who have sat in my blue room tell stories for the rest of their lives."
{n}She goes out. Through the open shell you hear a door, a woman's breath catching, and Vellexia's voice, pleasant and very close: "Good news, darling. You are going to remain a person. Do try to deserve it." When she comes back, she is smiling.{/n}'''),
    (INVITES, "copy", "A witness with an appetite for the account.",
     '''"A witness with an appetite for the account. How much more interesting than a witness who merely wants to be thanked."
"I want to know what he sold."
"So do I. We may yet quarrel over what to do with the knowledge, but at least we shall begin by wanting the same thing."
{n}She carries the shell into the blue room and sets it on the arm of a chair. The arm is warm; the glass fogs a little. Across from it a tiefling woman with short dark horns sits very straight on a stool, the only seat in the room that was never anyone.{/n}
"Tessar, this is the crusader your master put in his little play. You will tell the Commander everything you tell me. If you tell me anything you do not tell the Commander, I shall know, and you will spend the rest of the war holding up a lamp."
"Yes, my lady," {n}Tessar says to the shell, with great precision.{/n}
"You shall hear all of it," {n}Vellexia tells you.{/n} "Try to use it more ingeniously than Ilveris used your name. If you use it to flatter yourself at my expense, I shall know."'''),
    ((V + "the_claim_before_the_event",), "start", "She accepted,",
     '''"She talked all night," {n}Vellexia says as the glass clears.{/n} "I let her. Every so often I touched the back of her chair and she remembered something new. A frightened woman is very nearly as entertaining as a surprised one."
{n}She brings Ilveris's book into view: narrow, silk-bound, each page sealed shut with a blot of green wax. Some of the seals are broken. Tessar stands behind her chair with her hands folded. There is a fresh bruise on one wrist, the shape of somebody's fingers.{/n}
"His book of tomorrows. He seals a guest's page before the evening and breaks the seal afterwards before witnesses, and the purchasers gasp. Tessar says the wax is honest. She will not say the pages under it are."
"Then what is she saying?"
"That she wrote some of those pages herself, at his dictation, after the evenings they describe, and slid them under old wax with a hot knife. She will not say which. She says it is safer for her if somebody else finds them. Clever girl. If I find them, it is my discovery and not her betrayal." {n}Vellexia turns the book toward the glass.{/n} "Find them for me, sweetheart."'''),
    ((V + "the_claim_before_the_event",), "found", "The date on one prediction",
     '''{n}You read the page sealed before her first evening with you: the arena. It predicts a bloodsport, a champion and a guest who would claim him. Then one line, in ink a shade too fresh, names the champion, names the guest who claimed him and quotes the very words she used to do it. Nobody could have written that before the bout was fought.{/n}
{n}You show her. Vellexia reads it twice and gives a soft, delighted laugh.{/n}
"A prophecy of yesterday, sealed under last week's wax. How very efficient."
"It proves he altered this page. It does not prove every prediction is false."
"No. We shall have to inconvenience him with the precise accusation."
{n}You find a second forgery on the page about her perfume: the words 'without opening it' sit in fresher ink beneath an older seal.{/n}
"That one is mine," {n}she says.{/n} "I shall keep it where he can see me keeping it." {n}She looks up at Tessar.{/n} "You wrote that line?"
"At his dictation, my lady."
"With this hand?" {n}Vellexia takes the clerk's hand and spreads its fingers on the table, gently, the way one admires a ring. Tessar does not breathe. Then Vellexia lets go.{/n} "Lovely penmanship. Keep it. Now: the page about the Commander."
{n}The page concerning your evenings has no fresh ink at all. Vellexia's smile thins.{/n}
"Now we reach the part I was hoping would be equally simple."'''),
    ((V + "the_claim_before_the_event",), "missed", "You mistake the repeated date",
     '''{n}You take a page whose ink has dried unevenly for a forgery and say so. Vellexia raises an eyebrow and holds it out to Tessar.{/n}
"That one is honest, my lady," {n}Tessar says, very quietly.{/n} "The damp got into the book last summer. Those are water stains."
{n}There is a pause in which Vellexia appears to enjoy several possible remarks before selecting none of them.{/n}
"Our witness has corrected the Commander. How brave." {n}She takes Tessar's little finger between two of her own and turns it, without hurry, until it breaks. Tessar makes one small sound and stays standing.{/n} "That is for the time we have lost. You may repay me by making your next certainty more expensive to obtain, sweetheart. She has nine more."
{n}You acknowledge the mistake. Tessar, white to the mouth, finds the forged lines herself: the arena, the perfume. The page about your evenings, however, has no fresh ink. It appears to have been sealed before you ever set foot in the house.{/n}'''),
    ((V + "the_claim_before_the_event",), "ask", "You would rather hear the person who wrote it.",
     '''"You would rather hear the person who wrote it. A habit I should find less disappointing by now."
{n}Vellexia rests one hand on the back of Tessar's neck, lightly, the way she might rest it on a favourite chair. The clerk's voice is low and careful and has no polish on it at all.{/n}
"The perfume page. That is the smallest. He dictated 'without opening it' the morning after her ladyship sent the scent back. I warmed a kitchen knife, lifted the old wax and put the line underneath. The arena page is the same. I can show you where the knife slipped."
{n}She shows you. Vellexia's thumb moves on her neck once, approving, and Tessar flinches all the same.{/n}
"Now tell us about the Commander," {n}Vellexia says.{/n}
"That page was sealed before the first evening, my lady," {n}Tessar replies.{/n} "The lie is in what he says it means."'''),
    ((V + "the_claim_before_the_event",), "yours", "The prediction lists five answers",
     '''{n}The page lists five answers a visitor might give for coming to the Abyss: duty, revenge, pleasure, uncertainty, ambition. Beside each, Ilveris has written why Vellexia would eventually tire of hearing it.{/n}
"He sold the entire list," {n}she says.{/n} "He only needs one answer to fit."
"Does the page say which one I would give?"
"No. It says the page contained the answer. A claim generously assisted by containing all of them."
{n}Tessar adds, from behind the chair, that Ilveris showed each purchaser a different line and swore it was the true one. Those who caught him were offered a second evening for nothing. Most of them took it, because they would rather be fooled again than admit they had been.{/n}
"So he did not arrange what I said," {n}you observe.{/n}
"He arranged what people would pay to believe about it," {n}Vellexia answers.{/n} "I dislike that more. If he had controlled you, at least there would have been a spell worth stealing."
{n}She closes the book. For a moment her irritation is bare, and old, and very ugly.{/n}
"I was predictable enough to make his lie convenient. That is the part he will expect me to deny. We should find a better answer."'''),
    ((V + "the_claim_before_the_event",), "method", "A clean accusation.",
     '''"A clean accusation. Almost irritatingly clean. Every purchaser in one room, every forged page read aloud, and Ilveris standing in the middle of it trying to look prophetic. He loses his trade, and I lose the pleasure of watching him attempt to read me."
"You would still win something."
"Yes. I would win his face. That is why I am considering it."
{n}She asks Tessar how many purchasers there are. Tessar says forty-one, and that she remembers every name, and what each of them was ashamed of wanting. Vellexia says she knew a head that pretty could not be entirely empty.{/n}
"You have offered me a result with fewer opportunities to become magnificent. I shall remember that when you next ask why I prefer your company to an obedient audience. Sometimes I do not."
{n}Her smile returns, sharper than before.{/n}
"We shall weigh it against the more extravagant possibility before deciding."'''),
    ((V + "the_claim_before_the_event",), "challenge", "There. You do understand the expensive part.",
     '''"There. You do understand the expensive part."
{n}She tells Tessar the rule, and the clerk writes it down for her master. One question. One prediction, sealed before the choice and broken after it. No second pages. No knife from the kitchen.{/n}
"He will ask what he gains by accepting," {n}Tessar says.{/n}
"My name on the result if he is right. An admission, in my own salon, before my own guests, that a little man with a book understood me. He has been selling a counterfeit of it for a year; let him try for the original."
"And if he is wrong, my lady?"
{n}Vellexia looks at the clerk, then past her, slowly, around the room, at the chairs.{/n}
"Then he will discover what I collect. Write that down exactly, darling. I want him to read it twice."
{n}Tessar writes it, every word, and her pen does not shake until the last one. Vellexia watches you through the glass.{/n}
"This could be unpleasant," {n}she says.{/n} "I find I have missed being uncertain about which unpleasantness I will prefer."'''),
    ((V + "the_clerks_own_price",), "start", "She has asked to speak before I begin improving the proposal.",
     '''"Tessar wishes to speak before I begin improving her," {n}Vellexia says when you answer.{/n} "I find that impertinent enough to be promising."
{n}She moves the shell to show the clerk standing beside the table. Tessar has short dark horns and a mouth that looks accustomed to being held still while somebody else speaks. She has been offered a chair. She has not sat on it.{/n}
"I have agreed to tell what I know," {n}Tessar says.{/n} "Not to be introduced at parties as the conscience of Ilveris's house. You should know that before we begin."
"I had not mistaken you for it," {n}Vellexia answers.{/n} "Consciences make such poor upholstery."
"Some of your guests may. They will want an admirable reason for my changing masters. I would prefer an accurate one."
{n}She looks toward the glass, waiting for you to speak.{/n}'''),
    ((V + "the_clerks_own_price",), "reason", "I prepared the settlements.",
     '''"Because last spring he sold me." {n}She says it flatly.{/n} "A patron wanted a demonstration of how a clerk breaks. Ilveris predicted the night I would. He took the fee for the prediction, and then he took me to the patron's house, and he stood in the corner with his book to see whether he was right."
"Was he?"
"He was a day early. He wrote the correct day in afterwards." {n}Her mouth barely moves.{/n} "So now I want three things. To leave his house alive and walking. To take his purchasers with me: I know their names, their tastes and what they are ashamed of, and I can sell them better lies than he does. And to show the next patron who wants a prophet what I can prepare without his name on it."
{n}Vellexia leans back, visibly pleased by a story with room for more than one appetite.{/n}
"Whose names must you use?" {n}you ask.{/n}
"The ones in it. I can hide purchasers. I cannot hide Lady Vellexia and the Commander and still make the best page in the book make sense."
{n}She opens the silk-bound book at the page about your evenings. Beside it she lays a sheet in her own hand: the same page, the forgery marked in red, the purchasers' names struck through. Yours and Vellexia's remain, with the questions from your evenings.{/n}'''),
    ((V + "the_wager_with_an_edge",), "start", "Ilveris accepted the possibility of a demonstration.",
     '''{n}Vellexia has opened her ring tray again. Through the glass you see her lift a narrow circlet from it and set it beside Ilveris's book.{/n}
"Ilveris has answered. He refuses to be exposed quietly and he refuses to be paid to confess, which shows more taste than I credited him with. He wants a demonstration. In my salon, before my guests."
"What does he stake?"
"Himself." {n}She says it with real pleasure.{/n} "If his prediction fails, I may keep him. He wrote it in his own hand: 'as my lady keeps everything'. He has been in this house. He has walked down my hall. He knows exactly what he is offering, and he offered it anyway. I could almost love him for it."
"And you?"
"This." {n}She turns the circlet on one finger.{/n} "A piece I made when I was less easily offended by excellent work belonging to someone else. I won it back from its third owner after deciding I disliked seeing it worn badly. He wants it, and he wants me to say aloud, before everyone, that he understood something I could not bear to hear."
"Even if what he understood was how to arrange the result?"
"Precisely. He wishes to sell that distinction afterward. We must decide whether to let him try."'''),
    ((V + "the_wager_with_an_edge",), "account", "The second clerk has confirmed the additions.",
     '''"Tessar's pages are proved. I can have all forty-one of his purchasers in my salon by tomorrow night, with him in the middle of them, and let them read the forged pages aloud to him one at a time. He will lose his trade, and a good deal else. They will not be gentle. They paid him to tell them who they were."
"And you?"
"I shall sit on the stairs and watch."
{n}She lifts the circlet, then sets it back in its compartment.{/n}
"It would end our particular work cleanly. He did not control your answers. He wrote his prophecies after the fact. We could prove it, let Tessar walk off with his purchasers and find a different occupation."
"You sound disappointed."
"I am. He offered me himself, sweetheart. Nobody has offered me himself in centuries. They usually have to be persuaded."
{n}Her gaze returns to yours through the glass.{/n}
"Choose the stairs, if you prefer. I shall describe his face to you at length, and you will be sorry you were not here to see it."'''),
    ((V + "the_wager_with_an_edge",), "question", "He will prepare two sealed descriptions.",
     '''"He will seal one prediction in his book before the evening: which of three entertainments I will choose, and spend the whole hour on. A repeat of a play I once adored, a new work I have not seen, or an hour with nothing in it at all. He must name one. I must actually spend the hour on whatever I choose, and not walk out in the middle to spite him."
"He could make one of them unbearable."
"We choose who supplies the entertainments. He sees what they are, as do I. He must seal his answer before either of us sees the finished works."
{n}She lifts the circlet again.{/n}
"He proposes that you choose the order in which I sample them. I believe he wants to make my decision look like a decision about you. We could refuse that part. Or leave him the temptation to mistake my appetite for something simpler."'''),
    ((V + "the_wager_with_an_edge",), "publish", "She closes the ring tray with the circlet inside it.",
     '''{n}She closes the ring tray with the circlet inside it.{/n}
"Very well. I shall have to enjoy being right without making him bet his skin on it."
"You can let the room do the rest."
"A cruel suggestion. You are learning."
{n}She sends Tessar out with forty-one names and forty-one invitations in Vellexia's own hand, which none of them will dare refuse. Ilveris's invitation she writes last. It says only that his presence is requested, that the Commander's private questions will not be read aloud, as ordered, and that everything else will.{/n}
"I want him unable to wriggle out of a single word," {n}she says,{/n} "and I want him to know whose house he is standing in while he tries."
"And the demonstration?"
"Cancelled. I will not leave him hoping for a wager I have decided not to give him. Hope is so fattening."'''),
    ((V + "an_hour_that_counts",), "published", "Ilveris has answered. He says the altered descriptions",
     '''"Look." {n}She turns the shell toward her salon.{/n}
{n}The room is full. Forty-one purchasers of tomorrow, in their good clothes, stand in a ring. In the middle of it Ilveris is on his knees with his book open on the tiles in front of him, reading his own forged pages aloud, one at a time, while Tessar stands at his elbow and points to the fresh ink. He has lost his rings. Somebody has taken his coat. A man in green velvet, who once paid to learn that his wife would never leave him, is holding Ilveris's left hand flat on the floor with his boot.{/n}
"I told them they might collect what they were owed," {n}Vellexia says from the stairs, where she sits with her chin on her knees like a girl at a puppet show.{/n} "I did not say how. I have been sitting here for an hour, and nobody has bored me once."
"Will they kill him?"
"No. I told them not to. A dead prophet is a martyr; a live one has to keep explaining." {n}She watches the man in green shift his weight.{/n} "Fingers, perhaps. I said nothing whatever about fingers."
{n}On the far side of the ring, Tessar is collecting names. Every purchaser who leaves stops beside her first.{/n}
"And you?"
"I have my circlet and an enemy whose explanation will take longer every time he gives it. I find the result more satisfying than I expected."'''),
    ((V + "an_hour_that_counts",), "won", "She stays for the promised hour.",
     '''{n}She stays for the promised hour. By the end, the emperor has become the privy's door handle and the procession has begun praising his accessibility. Vellexia laughs so suddenly that one of the witnesses forgets to be discreet about staring.{/n}
"Yes, I enjoyed it," {n}she tells him.{/n} "You may report the astonishing event without inventing a more flattering cause."
{n}Tessar breaks the wax on Ilveris's page before the witnesses. It names the empty hour. She reads it aloud, and then she reads aloud the line he wrote beneath his signature, 'as my lady keeps everything', and steps out of the way.{/n}
"Ilveris," {n}Vellexia says, kindly.{/n}
{n}He begins to explain. She says one word over him. It is not a long word. His explanation goes on for a moment after his mouth has stopped being a mouth; then there is a small, handsome footstool of dark walnut on the tiles where he stood, with a face carved into the front of it that has not finished its sentence.{/n}
"There. Something of his that finally surprises me." {n}She sets her heel on it, testing.{/n} "A little high. I shall have the legs taken down."
{n}She asks the mechanism's maker his price for another performance, rejects the first figure with such enthusiasm that he halves it himself, and commissions a second emperor, smaller, with a face she will describe to him later. When the room has emptied she brings the shell close again, her feet still resting on the footstool.{/n}
"You stayed. Even through the parts in which I had almost nothing to say to you. I find that more pleasant than I expected."
{n}The watch outside your Drezen window changes. You reach for the cover before she can dismiss you. Vellexia stops speaking and watches your hand.{/n}
"Go to your war, then. I have not decided what I want from the rest of tonight."'''),
    ((V + "the_voice_after_the_abyss",), "papers", "The corrections circulated.",
     '''"He lived. I told them he should. He has eight fingers and a new name, and he sells something he now calls 'possibilities' from a room above a tannery, with fewer guarantees and more language nobody can disprove. Two of his old purchasers went back to him the following week. I cannot prevent people from investing in their own foolishness."
{n}She lifts the circlet, lets the light run along its edge, and puts it back in its case.{/n}
"The man in green velvet wrote to ask whether I might advise him about his wife. I sent his letter back folded into the shape of a little chair. He has not written again."
"Does Ilveris still predict you?"
"Never by name. He goes white when it is mentioned. That is the only prophecy of his I have ever found accurate."
{n}Her smile sharpens.{/n}
"We did not make him honest. We made that particular lie very expensive. I am content to have accomplished something with an ending."'''),
    ((V + "the_voice_after_the_abyss",), "won", "He paid. Reluctantly,",
     '''"He is in the hall." {n}She tilts the shell. By the door, beside the hat-stand that was once his runner, stands a walnut footstool with its legs cut down an inch and a face carved into its front, mid-word.{/n}
"I had the legs taken down. He is the right height now. Guests rest their boots on him while they wait to be announced, and the cleverer ones ask what he was. I tell them he predicted me. They laugh. He hears them laugh. That is my favourite part."
"Does he know?"
"Oh, everything in my house knows. That is the point of my house."
{n}She slides the circlet onto one finger and turns her hand to consider the silver.{/n}
"The theater's maker has acquired several commissions. I have refused two invitations to hear patrons explain how much better they understand the joke than everyone else. The little emperor deserved a less tiresome triumph."
"Would you watch it again?"
"Perhaps. I should like the maker to spend a little longer wondering whether he will end up in the hall. It improves his work."'''),
]

# ---------------------------------------------------------------------------
# 3. Choice labels that named ledgers: (scene ids, node, index, old, new).
# ---------------------------------------------------------------------------
CHOICES = [
    (INVITES, "evidence", 0, '"Buy the account, not the clerk. I want a witness with a reason to tell us the truth."',
     '''"Hear her as a witness. Don't make her a chair. A witness who is afraid of you will not lie to us."'''),
    (INVITES, "evidence", 1, '"Give me a copy of whatever we learn. I want to know how he used my name."',
     '''"Let me hear every word she says. I want to know how he used my name."'''),
    (INVITES, "clerk", 0, "[Accept that limited commission.]", "[Let Tessar walk out a witness.]"),
    (INVITES, "copy", 0, "[Accept access to the same account.]", "[Agree to hear all of it.]"),
    (INVITES, "terms_clerk", 0, "[Agree to examine the account when it arrives.]", "[Agree to hear Tessar when she is ready.]"),
    (INVITES, "terms_copy", 0, "[Agree to examine the account when it arrives.]", "[Agree to hear Tessar when she is ready.]"),
    ((V + "the_claim_before_the_event",), "start", 0, "[Compare the dated predictions with the later descriptions of the results.]",
     "[Look for pages written after the evenings they predict.]"),
    ((V + "the_claim_before_the_event",), "start", 1, '"Have Tessar choose one disputed entry and explain how it was recorded."',
     '''"Make Tessar show us one page she forged, and how she did it."'''),
    ((V + "the_claim_before_the_event",), "start", 2, "[Close the shell until you can study the account.]",
     "[Close the shell until you can study the book.]"),
    ((V + "the_claim_before_the_event",), "yours", 0, '"Expose how he changes the account after the event. Leave your tastes out of it."',
     '''"Break his trade in front of everyone who ever bought from him. Leave your tastes out of it."'''),
    ((V + "the_claim_before_the_event",), "yours", 1, '"Offer him one prediction that must name a result before either of us chooses it."',
     '''"Make him predict you once, in your own salon, with something of his on the table."'''),
    ((V + "the_claim_before_the_event",), "method", 0, "[Keep the accounting approach available.]", "[Keep the public unmasking in mind.]"),
    ((V + "the_claim_before_the_event",), "challenge", 0, "[Keep the public challenge available.]", "[Keep the challenge in mind.]"),
    ((V + "the_clerks_own_price",), "start", 0, '"Then tell me why you are willing to sell the account."', '''"Then tell me why you are selling him."'''),
    ((V + "the_wager_with_an_edge",), "start", 0, "[Ask about exposing the altered accounts without taking his wager.]",
     "[Ask about breaking his trade without taking his wager.]"),
    ((V + "the_wager_with_an_edge",), "account", 0, '"Publish the checked account. Keep the circlet and let this be enough."',
     '''"Break his trade in front of them all. Keep the circlet and let that be enough."'''),
    ((V + "the_wager_with_an_edge",), "question", 2, '"No. Publish the checked account instead."',
     '''"No. Break his trade in front of them all instead."'''),
    ((V + "the_wager_with_an_edge",), "publish", 0, "[Let the checked account stand without a wager.]", "[Let the unmasking stand without a wager.]"),
    ((V + "an_hour_that_counts",), "start", 0, "[Ask about the published account.]", "[Ask how the unmasking went.]"),
    ((V + "an_hour_that_counts",), "published_end", 0, "[Let the work end with the account actually settled.]",
     "[Let the work end with Ilveris broken and alive.]"),
    ((V + "the_voice_after_the_abyss",), "result", 0, "[Ask about the published corrections and the circlet she kept.]",
     "[Ask what became of Ilveris after the unmasking.]"),
    ((V + "the_voice_after_the_abyss",), "result", 1, "[Ask whether Ilveris paid after losing his wager.]",
     "[Ask what became of Ilveris after he lost his wager.]"),
]

# ---------------------------------------------------------------------------
# 4. Read-only consumers: (scene ids, node, paragraph), appended after existing paragraphs.
# ---------------------------------------------------------------------------
PARAGRAPHS = [
    # method_first / challenge_first had no reader: the wager scene now remembers which road the Commander asked for.
    ((V + "the_wager_with_an_edge",), "start", p(
        '''"You wanted his trade broken in public," {n}she adds.{/n} "I have not forgotten. Forty-one purchasers, one room, every forged page read aloud. It is still on the table, beside his throat."''',
        requires=(V + "method_first",))),
    ((V + "the_wager_with_an_edge",), "start", p(
        '''"You wanted him to predict me once, with something of his on the table," {n}she adds.{/n} "He has put everything of his on the table. You should be flattered. I am."''',
        requires=(V + "challenge_first",))),
    # clerk_terms / shared_account had no reader.
    ((V + "the_claim_before_the_event",), "start", p(
        '''{n}Tessar is still a person. Vellexia mentions it twice, as if it were a gift she had made to you and expects to be thanked for, and both times the clerk looks at the floor.{/n}''',
        requires=(V + "clerk_terms",))),
    ((V + "the_claim_before_the_event",), "start", p(
        '''{n}The shell sits where Vellexia promised, on the warm arm of the blue-room chair, so that you hear everything Tessar says. Once, when the clerk lowers her voice, Vellexia taps the chair, and Tessar says it again, louder, to you.{/n}''',
        requires=(V + "shared_account",))),
    # first_kiss / held_close had no reader after Chapter 4.
    ((V + "the_unused_reply",), "start", p(
        '''{n}She has not mentioned the kiss. She does not need to: once, her eyes go to your collar, as if checking that it is still where she left it.{/n}''',
        requires=(V + "first_kiss",))),
    ((V + "the_unused_reply",), "start", p(
        '''{n}She lifts a ring with the hand that held your wrist last time, and keeps that hand where you can see it.{/n}''',
        requires=(V + "held_close",), forbids=(V + "first_kiss",))),
    # noticed_expectation had no reader.
    ((V + "second_painter",), "start", p(
        '''"You said it might show what the person looking expects," {n}she adds.{/n} "I have been testing that all morning. It expects me to be bored. Rude."''',
        requires=(V + "noticed_expectation",))),
    # trickster.cost.late (the week in Orrel Vask's crate) had no reader.
    ((T + "after.visit", T + "after.visit_quarters"), "unmirrored", p(
        '''"A week," {n}she adds.{/n} "A week in a cambion's crate at the rift camp, with straw against my face, while you decided whether I was worth his surcharge. I counted every hour of it. I shall be spending them on you."''',
        requires=(T + "cost.late",))),
    ((T + "after.visit", T + "after.visit_quarters"), "diminished", p(
        '''"And a week," {n}she adds,{/n} "face to the wall in a haulier's crate, while you haggled over a frame. I could hear you haggling. I shall be spending that week on you."''',
        requires=(T + "cost.late",))),
    # renewed_slow overload: the Trickster's "You." also sets trickster.courting; company_end must not forget it.
    ((V + "two_unremarkable_pleasures",), "company_end", p(
        '''"You told me in Drezen that it was me you wanted," {n}she remarks as you reach for the cover, without looking up from her bottles.{/n} "Not a debt, not a trick. And tonight you sorted papers. I remember both answers. I shall decide which one to punish."''',
        requires=(T + "courting",))),
    # ending_dead never read the native VellexiasSlavesFreed etude.
    ((V + "ending_dead",), "start", p(
        '''{n}Her death emptied the house of the guests she had kept; they walked out of it free. Some of them came afterwards to look at the place where she died. None of them sat down.{/n}''',
        requires=(V + "slaves_freed",))),
]


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(by_id, sid, node_id):
    scene = by_id.get(sid)
    if scene is None:
        raise ValueError("vellexia_cloud: missing scene " + sid)
    for node in scene["Nodes"]:
        if node["Id"] == node_id:
            return node
    raise ValueError(f"vellexia_cloud: missing node {sid}:{node_id}")


def integrate(payload):
    by_id = _scenes(payload)
    for sids, old, new, minimum in SUBS:
        hits = 0
        for sid in sids:
            if sid not in by_id:
                raise ValueError("vellexia_cloud: missing scene " + sid)
            for node in by_id[sid]["Nodes"]:
                if old in node.get("Text", "") and new not in node["Text"]:
                    node["Text"] = node["Text"].replace(old, new)
                    hits += 1
        if hits < minimum:
            raise ValueError(f"vellexia_cloud: {sids[0]}: expected {minimum} hits, got {hits}: {old[:60]!r}")
    for sids, node_id, guard, new in NODES:
        for sid in sids:
            node = _node(by_id, sid, node_id)
            if guard not in node["Text"]:
                raise ValueError(f"vellexia_cloud: {sid}:{node_id} no longer holds {guard!r}")
            node["Text"] = new.strip()
    for sids, node_id, index, old, new in CHOICES:
        for sid in sids:
            choices = _node(by_id, sid, node_id).get("Choices", [])
            if index >= len(choices) or choices[index].get("Text") != old:
                raise ValueError(f"vellexia_cloud: {sid}:{node_id}>{index} label changed: {old[:50]!r}")
            choices[index]["Text"] = new
    for sids, node_id, paragraph in PARAGRAPHS:
        for sid in sids:
            _node(by_id, sid, node_id).setdefault("Paragraphs", []).append(dict(paragraph))

    _player_answer_exchanges(by_id)


# VEL-A4-003: run after owned prose transformations so they cannot restore
# embedded Commander speech. Original choices remain in their saved positions.
PLAYER_ANSWER_EXCHANGES = [('unfinished_likeness', 'start', ['"Have you looked?"']),
 ('unfinished_likeness',
  'terms',
  ['"And you paid him?"',
   '"You want me to break that agreement for you."',
   '"What happens to him if I don\'t?"']),
 ('second_painter', 'start', ['"What did you say?"', '"You sound disappointed."']),
 ('second_painter',
  'ask',
  ['"I decline to damage something merely to avoid asking a question. He knows how he assembled '
   'it. Let him show us."',
   '"Then we can compare what he says with what he does."',
   '"Why?"']),
 ('two_observers', 'question', ['"I know you are dangerous."', '"You asked why I return."']),
 ('unadvertised_hour',
  'intent',
  ['"You have been watching me notice it."', '"Since when has that stopped you?"']),
 ('a_question_kept',
  'result',
  ['"Even if you helped find the answer?"', '"What would you most enjoy taking from me?"']),
 ('the_price_of_tomorrow',
  'offer',
  ['"Does she make the predictions?"',
   '"He could use those answers to arrange the result," {n}you say.{/n}']),
 ('the_cover_before_the_battle',
  'start',
  ['"You still can. I wanted to tell you that I am preparing to leave again. The next part may be '
   'difficult to come back from."',
   '"Enough for you to waste on me."']),
 ('the_cover_before_the_battle',
  'lovers',
  ['"I want to come back. I want to hear you complain about the singer."'])]


def _player_answer_exchanges(by_id):
    from copy import deepcopy

    for suffix, node_id, lines in PLAYER_ANSWER_EXCHANGES:
        sid = V + suffix
        scene = by_id[sid]
        node = _node(by_id, sid, node_id)
        text = node["Text"]
        offsets = []
        cursor = 0
        for line in lines:
            needle = "\n" + line + "\n"
            offset = text.find(needle, cursor)
            if offset < 0:
                raise ValueError(f"VEL-A4-003: missing embedded answer {sid}:{node_id}")
            offsets.append(offset)
            cursor = offset + len(needle)
        original_choices = deepcopy(node["Choices"])
        node["Text"] = text[:offsets[0]]
        current = node
        for index, _ in enumerate(lines, 1):
            reply_id = f"{node_id}_commander_reply_{index}"
            if any(item["Id"] == reply_id for item in scene["Nodes"]):
                raise ValueError(f"VEL-A4-003: duplicate reply {sid}:{reply_id}")
            beat = f"VEL-A4-003 {suffix}/{node_id} exchange {index}"
            current["Choices"].append({
                "Text": f"[PROSE PENDING: {beat} Commander answer]",
                "Next": reply_id, "Set": [], "Requires": [],
                "Forbids": [], "Abort": False,
            })
            reply = {
                "Id": reply_id, "Speaker": node["Speaker"],
                "Text": f"[PROSE PENDING: {beat} Vellexia reply and continuation]",
                "Choices": deepcopy(original_choices) if index == len(lines) else [],
            }
            if "Portrait" in node:
                reply["Portrait"] = node["Portrait"]
            scene["Nodes"].append(reply)
            current = reply
