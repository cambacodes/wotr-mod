"""Played private career consequences and a voluntary Chapter 5 farewell."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
BASE = ("konomi.dismissed", "konomi.office_completed", "konomi.private_returned",
        "konomi.private_evening_kept", "konomi.career_decided", "konomi.private_future")


def s(id, title, nodes, requires=(), delay=24, manual=False):
    for node in nodes:
        node["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 5, "", nodes,
        Relationship="konomi", Remote=True, ManualOnly=manual, Areas=[DREZEN], Chapters=[5],
        requires=(*BASE, *requires), forbids=("konomi.present", "inhuman", "konomi.closed",
        "konomi.private_parted", "konomi.farewell", "konomi.private_last_visit"),
        delay=delay, optional=True))


s("private_return_terms", "The price of being asked first", [
    n("start", "Narrator", '''{n}Konomi's letter proposes another visit to Drezen. This time she has an appointment with the owner whose leases she now negotiates, and an answer to the invitations she carried back to Nerosyan. She asks whether you can meet during the visit before she books her passage.{/n}
{n}You confirm a date through the ordinary post. When the agreed day comes, she arrives at your meeting place with dust on the hem of her traveling clothes and a narrow wooden box beneath her arm.{/n}
"Samples," {n}she says before you ask.{/n} "A prospective tenant makes fittings for furniture. I thought it would help the owner understand what she proposes to store. I have spent the journey explaining that I am not selling hinges."
{n}She puts the box down and comes close enough to touch your cheek.{/n}
"I am pleased to see you. That was the other thing I meant to say first."''',
      c('[Welcome her and ask what became of the introductions.]', "offer"),
      c('[Tell her you need to postpone this conversation.]', abort=True)),
    n("offer", "Konomi", '''"One of them produced the woman who makes these. She wants more rooms than the owner currently has free. She can wait until the end of the season, and she can pay for an answer now."
{n}Konomi lifts the lid. A row of small brass fittings catches the light. One is shaped like a leaf; she touches it before closing the box.{/n}
"Unfortunately for everybody's convenience, the first tenant has exercised her option. The rooms are hers if she pays on the agreed date. I wrote back confirming that."
"And the owner?"
"Would prefer the new applicant. So would I, if the rooms were ours to offer. A reliable larger account is worth more than several people who need reminding that payment was part of the agreement."
{n}She draws the box toward her.{/n}
"They are not ours to offer. That has made the next conversation rather interesting."''',
      c('[Ask how the tenant answered after Konomi accepted the work immediately.]', "tenant_now", requires=("konomi.career_accepts_now",)),
      c('[Ask how the tenant and her new adviser answered after Konomi delayed her start.]', "tenant_wait", forbids=("konomi.career_accepts_now",))),
    n("tenant_now", "Konomi", '''"Through her adviser. She found one without my introductions, as she said she would. Every letter arrives with both their names beneath it."
{n}Konomi removes a short note from the box and shows you the date.{/n}
"She met the deadline. She also asked that I stop sending messages beginning with 'as we discussed.' She wants the written agreement cited, not the conversations in which I represented her."
"Will you?"
"I already have. I dislike being addressed as though I were searching for a way to cheat her. I also accepted employment from the person who benefits if she makes a mistake. She need not give me the benefit of remembering how agreeable I used to be."
{n}She puts the note away.{/n}
"The owner has noticed that I can obtain an answer even from someone who would rather not speak to me. That is one reason for the offer I want to discuss."''', c('[Hear the new terms.]', "terms")),
    n("tenant_wait", "Konomi", '''"Her adviser sent the notice early, with the payment date copied underneath. Waiting gave them time to arrange the money. I would like you to know that before I complain about it."
{n}She settles the little box squarely between you.{/n}
"The owner has pointed out that the introductions I made during the delay were excellent. She has also pointed out that I accepted a smaller fee for that period. She sees no reason to pay me twice for work I chose to do then."
"Do you think she should?"
"I think I should have negotiated the introduction fee before making the introductions. She is entirely entitled to enjoy that error. I intend to correct the next agreement."
{n}Konomi's expression brightens at the prospect.{/n}
"She wants me enough to discuss it. The tenant has her adviser and her rooms. I am quite prepared to spend the next conversation obtaining something for myself."''', c('[Hear the new terms.]', "terms")),
    n("terms", "Konomi", '''"A fixed payment for representing the owner's buildings, with an additional fee for each new agreement. I would bring proposals to her before approaching another landlord in Drezen. In return, she would pay me even in a month when nobody signs."
{n}Konomi lets you consider that.{/n}
"It would give her the first look at good applicants. It would give me an income I can plan around. People with smaller businesses would have one fewer person willing to take their side of a lease. Some of them will dislike me for it."
"What happens to the woman who needs the rooms?"
"I can offer her the owner's smaller space and a later expansion, with no claim on the first tenant's option. She may refuse. If she does, someone else can introduce her to another landlord. I would no longer be paid to find the best building for everybody."
{n}Her gaze holds yours.{/n}
"That is the work I want. I have been useful to people who would never permit me to decide whom they should hear. This woman will."''',
      c('"You would become a gatekeeper. I understand wanting the security and the influence."', "ambition"),
      c('"I would dislike losing an adviser because the wealthier side could buy her time."', "disagree")),
    n("ambition", "Konomi", '''"Yes. A gatekeeper with a fee and a name people must remember."
{n}She smiles without making the admission gentler.{/n}
"I can recommend that an applicant be heard before she has the money to be impressive. I can also recommend somebody who already has it. I will not promise that every choice I make will be the one you would have made for the person standing outside."
{n}Her hand rests on the lid of the box.{/n}
"I shall be insufferably pleased about it for at least a month. You may dislike half my reasons. You will still be expected at supper, and you will still be expected to pour."''', c('"What is the alternative you would actually accept?"', "alternative")),
    n("disagree", "Konomi", '''"So would I, if I were that client. I would look for another adviser. I might be very angry while doing it."
{n}She does not look away.{/n}
"There are only so many hours I can sell. At present I spend some of them persuading people that asking for payment does not diminish our friendship. A guaranteed fee would buy me freedom from that particular conversation. It would also buy my employer something she wants."
"I do understand the attraction."
"Then disagree with it. Loudly, if you like; I argue better against a live opponent. I want the work. And I want you across the table when it goes well, so that somebody sees me win who is not paying me."
{n}The last words come more quietly than the rest.{/n}''', c('"What terms would give you enough without accepting the whole offer?"', "alternative")),
    n("alternative", "Konomi", '''"I could represent these buildings without promising first sight of every applicant I meet. A smaller guaranteed payment, separate fees for the introductions she accepts. I would keep the right to act for other owners, never for both sides of the same agreement."
{n}She opens the box and turns the leaf-shaped fitting over.{/n}
"I would have to go on finding clients. There would be no agreeable fiction that I had kept every freedom and obtained the same security. She has already named the lower figure. I have already calculated what it leaves after travel."
"And what do you want from me?"
"Your opinion. Then company while I decide what to send. You are not signing this. I may remind you of that if it goes badly."
{n}She offers you the small brass leaf to examine. Its underside is plain and practical, ready to be fixed to something larger.{/n}''',
      c('"Take the first-refusal arrangement. Set a clear limit on it and be paid for the influence you bring."', "exclusive"),
      c('"Take the smaller guarantee. I think you would value being able to take a good proposal elsewhere."', "portfolio")),
    n("exclusive", "Konomi", '''"For this season, then. No promise that she owns every introduction I may ever make."
{n}She listens while you return the fitting to its place. Then she writes the term beside the figure and reads it aloud, testing the sound of an agreement she intends to live with.{/n}
"I shall lose some invitations. I may receive better ones. I am tired of treating the second possibility as something I must mention apologetically."
{n}She closes the box and catches your hand before you take it away.{/n}
"There. You have spent an afternoon in the company of a woman who intends to be expensive. I hope you were not expecting me to become easier to arrange."
{n}You settle the next visit before she sends the answer. She writes its date in a different place, where it will not be mistaken for a term offered to her employer.{/n}''',
      c('[Keep the visit you have arranged and let her send her terms.]', flags=("konomi.private_career_exclusive", "konomi.private_terms_sent"))),
    n("portfolio", "Konomi", '''"I would. I can name two people I particularly want the freedom to disappoint by choosing somebody else. That is not the noblest reason, but it has survived the arithmetic."
{n}She writes the smaller figure and the limit on the owner's claim. Before folding the answer, she looks at the larger figure once more.{/n}
"I shall miss that. If I complain later, you need not recite my reasons back to me. I have written them down."
{n}She takes the fitting from you, closes it into the box, and keeps your hand.{/n}
"You argued the other side of it very ably. I may hire you, if the war ever releases you. My rates for you would be ruinous."
{n}You settle the next visit before she sends the answer. She writes its date in a different place, where it will not be mistaken for a term offered to her employer.{/n}''',
      c('[Keep the visit you have arranged and let her send her terms.]', flags=("konomi.private_career_portfolio", "konomi.private_terms_sent"))),
], delay=168, manual=True)

s("private_kept_hours", "An hour she could have sold", [
    n("start", "Narrator", '''{n}On the morning of your promised visit, Konomi sends a runner with a question: can you come to the lease office before meeting her elsewhere? The runner has been told to wait, and plainly paid to look at the door until you answer.{/n}
{n}You agree. At the office, the owner has already left. Konomi is replacing the fittings in their box while the prospective tenant fastens a traveling cloak. The woman thanks her for the answer, not warmly, and goes out past you.{/n}
"She dislikes the space I could offer," {n}Konomi says.{/n} "She was quite right to refuse it. I wish she had reached the decision before I finished the explanation."
{n}She lifts the box from the desk.{/n}
"The first tenant's option stands. There will be no little miracle in which everyone gets the same rooms. Come in. I have an answer about my agreement, and a less pleasant question about our afternoon."''',
      c('[Ask whether the owner accepted the exclusive seasonal arrangement.]', "exclusive", requires=("konomi.private_career_exclusive",)),
      c('[Ask whether the owner accepted the smaller guarantee.]', "portfolio", requires=("konomi.private_career_portfolio",)),
      c('[Leave the visit for another day.]', abort=True)),
    n("exclusive", "Konomi", '''"She accepted. I have my first payment. The applicant now needs another adviser, and I have told her why I cannot accompany her to another landlord. She said it was convenient that my new principles began just when she needed me."
{n}Konomi sets the box by the door.{/n}
"She will take her samples away. She will probably advise someone else not to hire me. My employer, meanwhile, has asked me to choose which of three proposals she should hear next. I intend to enjoy that part."
"Even after this morning?"
"Especially after this morning. Otherwise I shall have paid for the agreement and declined to use what I bought."
{n}She pulls a chair away from the desk for you.{/n}
"I have not changed my mind. I did want to tell you what happened before I became excellent at describing it as an unqualified success."''', c('[Ask what she needs to decide about the afternoon.]', "hour")),
    n("portfolio", "Konomi", '''"She accepted the smaller guarantee. She has also sent two proposals to another negotiator. I am not entitled to be the only person with alternatives. I find that considerably less attractive in practice."
{n}Konomi sets the box by the door.{/n}
"The woman who was here has asked me to approach another landlord. I can do that under the terms we agreed. She wants to pay only if she signs a lease. I have offered a fee for the search and another for a signed agreement. She is considering whether my independence is worth paying for."
{n}She pulls a chair away from the desk.{/n}
"I have enough guaranteed work to keep the room in Nerosyan. Not enough to stop caring about the next answer. That is what I chose."
"Do you regret it?"
"Ask me after she answers. No, that is unfair. I want the chance to ask another landlord. I dislike having to sell the chance before I can use it."''', c('[Ask what she needs to decide about the afternoon.]', "hour")),
    n("hour", "Konomi", '''"The owner wants to meet the three applicants before she leaves tomorrow. She would pay an additional attendance fee. I told her I had promised the afternoon to you."
{n}Konomi looks toward the open door, then shuts it herself.{/n}
"She offered the same fee for written recommendations delivered tomorrow morning. I can finish those today, if I remain here for another hour. We would still have part of our visit. Or I can decline the extra work and leave with you now. My guaranteed payment stays mine either way."
"Which would you prefer?"
"Both the fee and the afternoon. I have checked; there is still only one afternoon."
{n}She comes back to the desk, but does not sit.{/n}
"So. An hour of my time has a price this afternoon, and I know it to the copper. What does it cost you? Do not tell me 'nothing'. I have never once believed a counterpart who said 'nothing'."''',
      c('"Keep the work. I can give you an hour, then I want the rest of our visit."', "work"),
      c('"I made room for this afternoon. I want us to keep it as we promised."', "leave")),
    n("work", "Narrator", '''{n}Konomi checks the time before opening the proposals. She offers you the comfortable chair and asks whether you want a task. You decline; you came to see her, and there is a book on the shelf you would rather examine than a lease.{/n}
{n}For a while the room contains the scratch of her pen and your occasional turning of a page. Once she asks whether a sentence sounds insulting. You tell her it sounds deliberate. She leaves it unchanged.{/n}
{n}When the hour is almost spent, she puts the completed recommendation beneath a weight. The last applicant has received a refusal instead of a request for further figures. Konomi reads that line again, changes one word, and stands.{/n}
"I could spend another hour making the refusal kinder. It would still be a refusal."
{n}She takes the book from your hands, keeping your place with a scrap of blank paper, and puts it aside.{/n}
"Now come with me. I have been looking at you across that desk long enough."''', c('[Leave with her for the remaining time.]', "short_walk")),
    n("leave", "Narrator", '''{n}Konomi opens the door and calls to the clerk in the passage. She asks him to tell the owner that she cannot provide the additional recommendations by tomorrow. He offers to bring the proposals to her lodging. She declines.{/n}
{n}When he has gone, she takes a moment to put her things away. The decision has not made her suddenly indifferent to the fee.{/n}
"I shall be drafting that answer in my head halfway through whatever you say next," {n}she says.{/n} "When you catch me at it, pinch me."
"I might ask you to tell me about it."
"That would be generous. Begin with something else. I want to discover whether I remember how to leave a room before the work in it is finished."
{n}She closes the box, leaves it for the applicant to collect, and offers you her arm. At the street she turns her face into the wind as though she has only just remembered the weather.{/n}''', c('[Take the whole afternoon you kept for one another.]', "long_walk")),
    n("short_walk", "Konomi", '''{n}You take a short route along the quieter streets. Konomi tells you which applicant she recommended and why the most persuasive proposal was not the most reliable. You interrupt when she begins quoting the figures.{/n}
"I know. The hour is over."
{n}She draws you into the shelter of a closed doorway, out of the passing wind.{/n}
"I am trying to decide whether you have been patient or whether you enjoyed watching me enough to consider it a fair use of the time."
"A little of both."
"Then I am fortunate. I should not like to depend entirely on your patience."
{n}Her hand settles at your waist. She tilts her head, looking from your eyes to your mouth with an interest that has nothing reserved about it.{/n}''',
      c('[Kiss her, and keep the remainder of the walk for yourselves.]', "short_kiss"),
      c('[Take her hand. Tell her what you wanted to share before the visit ends.]', "short_talk")),
    n("long_walk", "Konomi", '''{n}With the whole afternoon free, you reach the quiet end of the street and keep going. Konomi notices a patch of pale flowers growing through a broken wall. She stops to examine them, then admits she has no idea what they are.{/n}
"I have been wrong about enough plants. You may identify these if you like."
{n}You leave them unnamed. A loose stone makes an adequate seat. She settles beside you, tests whether it rocks, and leaves you the steadier end.{/n}
"I am still pleased about the work," {n}she says.{/n} "And I walked out on a fee to sit on a wobbling stone with you. My mother would call that a very poor bargain. She would be wrong."
{n}She reaches for your hand and watches you bring it to your lips. Her fingers curl against your cheek.{/n}
"There. That is an excellent beginning. What did you want to do with the afternoon you defended so firmly?"''',
      c('[Draw her close and kiss her.]', "long_kiss"),
      c('[Stay beside her and tell her the thing you wanted time to explain.]', "long_talk")),
    n("short_kiss", "Narrator", '''{n}She answers the kiss immediately. When somebody passes the doorway, she waits with her mouth close to yours until the footsteps have gone, then finishes what she began.{/n}
{n}Afterward you walk until the time you agreed to part. She keeps hold of your arm. The afternoon was shorter than either of you wanted; neither has to pretend it vanished entirely.{/n}''', c('[Part at the agreed time.]', flags=("konomi.private_extra_fee", "konomi.private_visit_kissed", "konomi.private_hours_kept"))),
    n("short_talk", "Narrator", '''{n}You tell her about something you have been putting off because it will disappoint a person whose good opinion matters to you. Her advice is assembling before you finish the first sentence; you can watch it happen. You tell her you do not want it.{/n}
{n}Konomi takes this like a tariff she disapproves of and pays it anyway, biting back two better arguments in plain view. At the turning where you must part, she squeezes your hand.{/n}
"Write and tell me how it goes. I shall have drafted three better replies for you by then, and I shall burn every one of them unread. You may admire the sacrifice."
{n}She looks ruefully back toward the street you walked together.{/n}
"We did manage some of it."''', c('[Part at the agreed time.]', flags=("konomi.private_extra_fee", "konomi.private_hours_kept"))),
    n("long_kiss", "Narrator", '''{n}She draws you nearer by your sleeve. There is time to kiss her without listening for the next summons, time to laugh when the stone shifts beneath you, and time to settle together on the steadier part before beginning again.{/n}
{n}When you finally stand, Konomi straightens your collar. Her own is not quite straight. You attend to that while she pretends to find the attention unnecessary.{/n}
{n}You take the longer way back. She does not calculate what the afternoon would have paid.{/n}''', c('[Walk back together before your other appointments.]', flags=("konomi.private_full_afternoon", "konomi.private_visit_kissed", "konomi.private_hours_kept"))),
    n("long_talk", "Narrator", '''{n}You tell her about something you have been putting off because it will disappoint a person whose good opinion matters to you. Her advice is assembling before you finish the first sentence; you can watch it happen. You tell her you do not want it.{/n}
{n}Konomi leans against your shoulder while you explain. Once she gets as far as "If I were you," and stops herself with an audible click of the teeth. You reach the end without an easy answer. She does not move from your side.{/n}
"You brought that to me instead of to your council. I shall take it as the compliment it is. I also held my tongue for a full quarter of an hour, which no ambassador has ever managed to make me do."
{n}You laugh, and she nudges you with her shoulder. There is still time to sit before you need to walk back.{/n}''', c('[Keep the rest of the afternoon, then return together.]', flags=("konomi.private_full_afternoon", "konomi.private_hours_kept"))),
], requires=("konomi.private_terms_sent",), delay=48)

s("private_last_visit", "The visit before you leave", [
    n("start", "Narrator", '''{n}You send Konomi a request to see her before the final fighting. She answers with a time during her stay in Drezen and asks you to come without work you expect to finish in her company.{/n}
{n}Her room looks lived in now. The traveling case is under the bed, not beside the door. A book lies open on the windowsill, a strip of cloth marking her place. She sees you notice it.{/n}
"I borrowed it from the lease office. I wanted something to read in which I was permitted to dislike both parties without finding terms they would accept."
{n}She closes the door and rests against it for a moment.{/n}
"There is something practical to tell you. Then I should like to be as impractical as the remaining time allows."''',
      c('[Hear what became of the agreement before saying goodbye.]', "business"),
      c('[Put off the farewell for another day.]', abort=True)),
    n("business", "Konomi", '''"The first tenant paid for her option. Her adviser sent the receipt. The owner and I have signed the arrangement we discussed, and I have been paid under it. I will keep working from both cities."
{n}Konomi sits on the edge of the bed, leaving space beside her.{/n}
"There. That is done, and I did not have to be dismissed for it this time. There will always be another applicant. I refuse to spend tonight on any of them."
{n}She looks toward the book, then back at you.{/n}''',
      c('[Ask about the applicants whose first hearing she now controls.]', "exclusive", requires=("konomi.private_career_exclusive",)),
      c('[Ask whether the applicant paid for an independent search.]', "portfolio", requires=("konomi.private_career_portfolio",))),
    n("exclusive", "Konomi", '''"One accepted a smaller space. One withdrew. One has asked me to explain the refusal to her partner, who apparently thinks a second audience will cause the rooms to enlarge. I have declined the second audience."
{n}Her smile is sharp and pleased.{/n}
"I have also put forward an applicant the owner had overlooked. She listened because choosing who reaches her table is now part of what she pays me to do. I liked that very much."
"And the people who no longer ask you?"
"Have found other people. Some of them will obtain excellent advice. I need not be delighted about it."
{n}She reaches for your hand.{/n}
"You watched me take the uglier half of that bargain and you are still sitting on my bed. I note it for the record."''', c('[Sit beside her.]', "time")),
    n("portfolio", "Konomi", '''"She did. I found two places she could examine, charged for the search, and left the choice with her. She took the second. I received the agreed additional fee when she signed."
{n}Konomi looks satisfied, though not triumphant.{/n}
"It required more letters than I wanted. I spent part of the fee paying someone else to carry them. The owner of the first buildings asked why I had not brought the applicant back to her. I reminded her that the applicant had refused the available space. We then discussed the next agreement."
"So the narrower terms held."
"They held. I have more than one person to disappoint and more than one person who may pay me. I still want influence. I shall have to acquire it a little less comfortably."
{n}She takes your hand.{/n}
"It is a life I recognize. I wanted you to see that before you went."''', c('[Sit beside her.]', "time")),
    n("time", "Narrator", '''{n}Konomi holds your hand between both of hers. Outside the room somebody carries a heavy object down the stairs, stopping at each landing. Neither of you volunteers to help.{/n}''',
      c('"We kept part of our visit even when you took the extra work."', "short", requires=("konomi.private_extra_fee",)),
      c('"I am glad we kept the whole afternoon."', "whole", requires=("konomi.private_full_afternoon",))),
    n("short", "Konomi", '''"We did. I received the attendance fee for the written recommendations. I remember that because I wanted it. I remember the walk because I wanted you."
{n}She turns your hand palm upward and brushes her thumb over it.{/n}
"Next time I may refuse the fee. Next time you may be the one selling me an hour. We shall haggle each time, openly, like honest merchants. It is the only arrangement I have ever trusted."
{n}She looks directly at you.{/n}
"Today I have kept the time. There is no proposal waiting for you to finish reading while I work."''', c('[Make her an offer before you go.]', "future")),
    n("whole", "Konomi", '''"So am I. I also remember the fee. I have a very good memory for both sorts of thing."
{n}She lifts your hand to her cheek.{/n}
"You told me outright the afternoon was yours and you would not sell it back. I have met two people in my life who would say that to my face. The other one was my grandmother."
{n}She leans into your touch.{/n}
"Today is kept too. Nobody is buying it."''', c('[Make her an offer before you go.]', "future")),
    n("future", "Konomi", '''"I have been wondering what people expect to hear at a farewell like this. Something they could repeat afterward without explaining who we were on an ordinary afternoon."
{n}She shakes her head.{/n}
"I want the ordinary afternoons. I am frightened that I will not have them. There is no elegant form of that request, and I have drafted eleven."
{n}Her grip tightens once, then loosens.{/n}
"So say what you mean, and not a word more. I negotiate for a living. I know what a promise inflated by fear is worth the morning after."''',
      c('"I still want the life we promised. Keep a place for my next invitation among your plans."', "committed", requires=("konomi.committed",)),
      c('"I want to go on seeing you. I will not turn that into a promise of a shared life just because I am leaving."', "open", forbids=("konomi.committed",))),
    n("committed", "Konomi", '''"I will. It will not be the only place in either of our lives. I knew that when I said yes."
{n}She moves nearer until her knee touches yours.{/n}
"When you can write, tell me where you expect to be. If you cannot come, write that too, and I shall be furious and believe you."
"That is what I want."
"Good. Then come back. That is the whole treaty. Come back scarred and short-tempered and late, I do not care, only come back. I have not finished collecting from you."
{n}Her smile falters. She does not turn away before you see it.{/n}
"Come nearer. I am finished being sensible."''', c('[Move close enough to hold her.]', "close")),
    n("open", "Konomi", '''"A smaller offer than I wanted. Still, it is honest paper, and I have been sold worse by kings."
{n}She moves nearer until her knee touches yours.{/n}
"I want the next visit. I may raise the stakes someday. You may meet them, or not. That is a negotiation for another season."
"You still want this one?"
"Very much."
{n}She puts her arm around you and lets her forehead rest briefly against your shoulder.{/n}
"I was trying to make that sound dignified. I am tired of it. Stay close. I want this one."''', c('[Hold her.]', "close")),
    n("close", "Konomi", '''{n}For a while you hold each other without finding another subject. Konomi's fingers move against the back of your neck. When she lifts her face, her eyes are bright and her expression impatient with the distance still between you.{/n}
"Enough talking. I have described how much I shall miss you in four drafts and burned them all. Kiss me."
{n}She touches your mouth once with her thumb, and pulls you down to her by the collar before you have finished moving.{/n}''',
      c('[Kiss her and stay together for the night.]', "night"),
      c('[Keep holding her. Spend the evening close, and part before your next duty.]', "quiet")),
    n("night", "Narrator", '''{n}She kisses you hard, as if the war might come through the door before she has finished. Her hand closes in your collar and does not let go until she needs both hands for your belt.{/n}
"The lamp stays lit," {n}she says against your mouth.{/n} "I intend to remember this properly."
{n}Her robe slides from her shoulders onto the floor beside the travelling case. She pushes you back across the bed and follows, her hair falling loose around your face as she pulls your hands to her hips and bends to kiss you.{/n}
{n}The lamp throws her shadow huge up the wall. She is bare and lit and does not hide in it, and she watches your eyes travel over her as if reading a document she drafted herself.{/n}
"Look," {n}she says.{/n} "I mean to be remembered in detail." {n}Her mouth travels along your jaw to your throat, teeth and then tongue, unhurried, as if the war she has declared to be on the other side of the door had been told to wait its turn.{/n}
{n}Much later, when the lamp is out, she asks whether you are awake. You are. In a precise, level voice she tells you which of the war's likely outcomes she has been costing out since supper. You do not promise her any of them. You find her hand beneath the cover and hold it until the figures run out.{/n}
{n}In the morning she walks you to the door. The book remains on the windowsill.{/n}
"Go carefully," {n}she says.{/n} "I want another inconvenient afternoon."
{n}You kiss her once more before you leave.{/n}''', c('[Leave with the farewell and the affection you chose.]', flags=("konomi.private_consequence_complete", "konomi.private_farewell_night"))),
    n("quiet", "Narrator", '''{n}She settles against you. You remain together while the room grows darker, speaking when something occurs to either of you and letting the rest of the time pass without an account of how well you used it.{/n}
{n}Before you must leave, she lights the lamp. You help her find a place for the borrowed book where she can reach it from the bed. She tells you which part she intends to argue with when you have both read it.{/n}
{n}At the door she holds you once more.{/n}
"Go carefully," {n}she says.{/n} "I want another inconvenient afternoon."
{n}She keeps your hand until the bells force the matter.{/n}''', c('[Leave with the farewell and the affection you chose.]', flags=("konomi.private_consequence_complete",))),
], requires=("konomi.private_hours_kept",), delay=24, manual=True)


for committed in (True, False):
    identity = "distance_lived" if committed else "distance_open_lived"
    text = ('''{n}Konomi and the Commander kept the life they had begun between two cities. There were journeys neither wanted to postpone, letters received too late, and afternoons one of them defended against a profitable interruption. Konomi kept a ledger of the broken appointments on both sides and presented it at intervals, with interest. Neither of them ever paid it off.{/n}'''
            if committed else '''{n}Konomi and the Commander continued their courtship on the terms they had actually signed, not on the ones fear had tempted them to draft. They arranged visits, broke some, and haggled over the rest. Konomi raised the stakes twice. The Commander met them once.{/n}''')
    SCENES.append(scene("konomi.ending_" + identity, "The hours they kept", "Epilogue", 5, "", [
        n("start", "Narrator", text,
          c('[Recall the influence she chose to build.]', "exclusive", requires=("konomi.private_career_exclusive",)),
          c('[Recall the independent work she chose to keep.]', "portfolio", requires=("konomi.private_career_portfolio",))),
        n("exclusive", "Narrator", '''{n}Her seasonal agreement grew into a reputation for selecting proposals worth hearing, and for charging enough to make the hearing valuable. Some former clients took their business elsewhere. Konomi wished them success with varying degrees of sincerity. When she told the Commander about a decision she was proud of, she no longer omitted the people it had disappointed.{/n}
{n}Her private invitations were still addressed by hand. The Commander came when possible, answered honestly when not, and knew which parts of her pleasure could be heard in a letter and which required being there.{/n}''', c(), portrait="Konomi"),
        n("portfolio", "Narrator", '''{n}Konomi kept several clients and the freedom to take a good proposal beyond the first unpromising answer. The freedom required work. She acquired influence through people who had watched her obtain a useful agreement and remembered what she charged for it. She enjoyed becoming someone whose refusal mattered.{/n}
{n}Her private invitations were still addressed by hand. The Commander came when possible, answered honestly when not, and knew which parts of her pleasure could be heard in a letter and which required being there.{/n}''', c(), portrait="Konomi"),
    ], Relationship="konomi", last=99,
        requires=("konomi.private_future", "konomi.private_consequence_complete", "konomi.committed" if committed else "konomi.private_future_open"),
        forbids=("konomi.closed", "inhuman", "ascended", *(() if committed else ("konomi.committed",)))))
    SCENES[-1]["Nodes"][0]["Portrait"] = "Konomi"


def integrate(payload):
    """Preserve old ending IDs and answers; suppress only their earned replacement."""
    for item in payload["Scenes"]:
        if item["Id"] in ("konomi.ending_distance", "konomi.ending_distance_open"):
            if "konomi.private_consequence_complete" not in item["Forbids"]:
                item["Forbids"].append("konomi.private_consequence_complete")
