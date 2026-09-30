"""Unregistered living-history continuation of the authored trial correspondence.

All new people, papers, concessions and seal behavior below are authored additions.
The final agreement concerns personal correspondence, not a native parent pact,
Worldwound outcome, ProfaneGift, Shamira transaction or entry into the harbor.
"""
from story_format import c, n, scene
from storylines.nocticula_trickster_acquisition import DREZEN, allowed, f


SCENES = []


def page(key, speaker, text, *choices):
    return n(key, speaker, text, *choices, portrait="Nocticula")


def add(key, title, previous, nodes):
    SCENES.append(scene(
        "noct.acq." + key, title, "Nocticula", 5, title, nodes,
        requires=("trickster", *f("correspondence_trial", previous)),
        forbids=("noct.dead", "noct.acq.council_fight", *f("closed", key + "_done")),
        delay=24, optional=True, Relationship="nocticula.acquisition", Remote=True,
        Areas=[DREZEN], Chapters=[5],
        RequiresAnyGroups=[list(f("channel_provisional", "channel_letters_only"))]))


add("borrowed_signature", "A signature for sale", "her_hand_done", [
    page("start", "Narrator", '''{n}The next paper to arrive at your desk bears your title twice. Once in the address, once beneath a promise you did not make.
An itinerant broker named Salven offers safe passage for letters to the Lady in Shadow. He has sent a sample of his guarantee to Drezen's clerks, hoping to sell the privilege to people with more money than sense. The sample promises that the Commander will intercede if a message displeases its recipient. Beneath that promise he claims the protection of the Council whose business brought you to her.
Your clerk Neris has held it back from the incoming petitioners. She asks whether the seal is yours.
It resembles the outward face of the divided wax. The central line is wrong. Somebody has seen enough of a request to sell an imitation, and too little to make one answer.
You lay the false guarantee beside your own half. When Nocticula's answering stroke appears, you copy Salven's wording onto the permitted sheet. You do not place the unfamiliar seal against hers.{/n}
"If you are selling introductions," she writes, "I expect a better description. This makes me sound like an office with inconvenient hours."
"Would you prefer expensive ones?"
"I would prefer the money. Why have you sent me an advertisement instead?"
"Because he is selling your brother's promise of access with my name underneath it. I want to discover who buys it before somebody takes a false invitation seriously."
"My brother's actual invitations have been quite troublesome enough. Show me this improvement."''',
         c('Explain how the guarantee reached Neris, and show the false central line.', "channel"),
         c('End the private correspondence. Deal with the forgery through your own officers.', "withdraw", flags=f("closed"))),
    page("channel", "Nocticula", '''"Tell me exactly which part he could have seen. Guess afterward."
{n}You have kept the original wrapping. You spread it flat and compare the folds with the broker's impression.{/n}''',
         c('The narrow fold has remained closed except for your answering mark.', "narrow", requires=f("channel_provisional"), forbids=f("channel_letters_only")),
         c('The letter travelled as a closed packet. The outside could have been copied.', "letters", requires=f("channel_letters_only"), forbids=f("channel_exposed")),
         c('The failed aperture exposed more. You already hold the sketch and the marked shavings.', "exposed", requires=f("channel_letters_only", "channel_exposed", "channel_repaired", "sketch_surrendered"))),
    page("narrow", "Nocticula", '''"Then do not flatter the counterfeit by making it a successful intrusion. Your half has an outside. You have carried it through a fortress full of people who can remember a shape."
You ask whether she thinks the broker knows anything useful.
"He knows somebody will pay before asking whether he does. That is usually enough to begin a career."
"And end one?"
"You are asking me to become optimistic about your clerks. Show me the paper."''', c('Copy the guarantee without supplying the missing line.', "offer")),
    page("letters", "Nocticula", '''"A closed letter is an excellent precaution against somebody reading its contents. Against somebody selling its existence, it is less distinguished."
"He still cannot reach you."
"He does not need to. He needs his customer to fear that he can. A remarkably economical use of me."
Her next instruction is brief: keep the wrapping. Someone who copies only a seal may be a liar; someone who copies the fold has handled the packet.
You ask whether she wants the original.
"I want you to discover which before you help him improve his work."''', c('Compare the wrapper and copy the guarantee.', "offer")),
    page("exposed", "Nocticula", '''"The opening you spoiled is still closed. Do not reopen it to reassure yourself."
"I have not."
"Good. I dislike paying twice for the same stupidity, particularly when I paid in attention."
You describe the second light again, then stop. It had no face, voice or mark that identifies this broker.
"That is the useful part of your answer," she writes. "You have an enemy small enough to investigate. Do not improve him into an unknowable one."
She retains the surrendered sketch. You cannot test a copy of its inner stroke against the counterfeit without asking her to perform that comparison.
You ask. Her answer arrives after a long enough pause to remind you who now possesses the original construction.
"It is not that stroke. Keep looking."''', c('Keep the old exposure on record without claiming it identifies Salven.', "offer")),
    page("offer", "Commander", '''You propose sending a reply that appears to accept one purchased introduction. Salven will have to name where he expects a petition to be delivered. Neris can attend his advertised collection point in Drezen with a closed packet, soldiers close enough to hear her call.
Nocticula wants to know what is in the packet.
"A request from a man who thinks you will enjoy hearing how easily he purchased your attention."
"You have a model close at hand."
"I was going to sign it."
The next line forms more slowly.
"Then he will learn that you are investigating him."
"After he has supplied the delivery instructions. Before that, I offer a seller the possibility of a better customer."
"Better in which sense?"
"More expensive to disappoint."
You offer a further concession. If she supplies an outer mark which her actual servants recognize as false, you will let her keep a signed undertaking naming your part in the investigation. It will prove your involvement if the affair later becomes inconvenient. Anyone selling Council protection will have to account for your recorded cooperation with the woman his guarantee claims to reach.
She will gain a record you cannot dismiss as an anonymous forgery. You will gain a way to distinguish a bought promise from a reply she actually chose to send.''',
         c('[Good] Use the bait once, then publish a denial and destroy the reusable pattern. People who bought protection should hear the truth.', "public", flags=f("concession_public")),
         c('[Evil] Keep the buyers out of the proclamation. Take control of the forwarding arrangement and share its reports with you.', "network", flags=f("concession_network")),
         c('I will not put my name in your keeping for this. End our private correspondence.', "withdraw", flags=f("closed"))),
    page("public", "Nocticula", '''"You would rather embarrass the purchasers than own them."
"I would rather stop selling them a danger they cannot recognize."
"There is no need to make that sound unprofitable. Some will be grateful. Some will insist you have destroyed an excellent investment. You may enjoy learning which are richer."
She draws an outer flourish around a blank space. It resembles a careless hand imitating her patience.
"Copy this. Once. I shall recognize it, and so will the servants to whom I choose to show it. It gives you no audience with anyone else."
You copy it onto the bait letter. She asks you to send the signed undertaking through your own answering mark first. Its lines fade from your sheet one after another, leaving their pressure in the paper.
You have not been promised another evening in return.''', c('Let her retain the undertaking and prepare the single bait letter.', flags=f("borrowed_signature_done", "undertaking_held"))),
    page("network", "Nocticula", '''"You propose to become a more reliable version of the man you are investigating."
"Reliability is a neglected advantage in his trade."
"What would you forward?"
"An address and an offer. No seal would guarantee your answer. People could still pay me to make certain you received the question."
"And I should thank you for appointing yourself between me and people who might interest me?"
You revise the proposal. Every forwarded petition gets copied to her mark before you decide whether to answer its sender. You cannot quietly keep the profitable ones for yourself.
She leaves the page blank until you write that limitation in your own hand.
"There. Now you have offered something. Keep a copy of your greed. It will help us identify it when you later give it a more diplomatic name."
Her false flourish arrives beneath your signature. She takes the undertaking through the answering mark and leaves you the pattern for the bait.''', c('Accept the copied-report obligation and prepare the bait.', flags=f("borrowed_signature_done", "undertaking_held", "reports_owed"))),
    page("withdraw", "Narrator", '''{n}You write that she will receive no further private requests. The answering line pulls free of the wax. It leaves the old break visible beneath it.
Neris still needs instructions about Salven. You send for her and put the false guarantee where an ordinary clerk can read it. Nothing about ending the correspondence makes the forgery disappear.{/n}''', c('Take the forgery back to your officers.')),
])


add("the_paid_address", "The address he sold", "borrowed_signature_done", [
    page("start", "Narrator", '''{n}Neris returns from the broker's collection point with your packet unopened and a narrow strip of paper. Salven would not take the packet without an advance; she would not pay without knowing where a failed delivery could be disputed. He gave her an address and called the question provincial.
Two soldiers saw him hand it over. Neither touched him. Neris reports that he was packing his display case before she reached the door.
Salven tore the strip from an acceptance counterfoil while she watched. Neris asked for the discarded half too, saying a receipt needed its number. It records three pending deliveries to the merchant whose room is named in the address. She has not seen the letters.
The address is above a bathhouse in Drezen. On the counterfoil, the receiving merchant's initials stand beneath a date earlier than the gate book's record of his arrival. Another date has been crowded into the margin and scratched through. Neris has brought the gate clerk's copy of his entry; both papers are on your desk.
You can send your officers there immediately. You can also compare the dates with the gate clerk's arrival book before Salven learns what Neris noticed.
Nocticula's mark waits in a sheet beside the papers. You have copied the address to her; no answer has arrived.{/n}''',
         c('[Knowledge: World 35] Separate the copied date from the merchant\'s own hand before anyone questions him.', flags=f("address_check_tried"), forbids=f("address_check_tried"), check=dict(Skill="SkillKnowledgeWorld", DC=35, Success="read", Failure="mistake", CommanderOnly=True)),
         c('Have the gate clerk compare his own entry and send the officers with Neris. Let the inquiry be visible.', "open", flags=f("inquiry_visible")),
         c('Close the private channel and let the officers finish the investigation without her.', "withdraw", flags=f("closed"))),
    page("read", "Commander", '''The old date belongs to the form beneath the signature. The merchant added the day of arrival in the margin, then scratched it out when it contradicted the guarantee he was copying.
You send the officers to hold the room while Neris asks the bathhouse keeper for that day's rental account. The keeper produces it before the merchant can send his assistant away. The three letters lie beside a brazier, their wrappers marked with the counterfoil's delivery numbers.
The assistant has a list of three buyers sewn inside his sleeve. He agrees to unpick it after Neris asks whether he prefers a seamstress or a soldier to perform the operation.
Salven is gone. The merchant is still here, with the payments and the letters he promised to forward. Your officers seal the room while its owner counts the money in their presence.
Nocticula's reply appears as you finish recording the names.
"An address which leads to a person. You should send my brother the method. He has always preferred the reverse."''', c('Account for the held letters and identified buyers.', "decision", flags=f("buyers_identified", "merchant_held"))),
    page("mistake", "Narrator", '''{n}You take the copied date for the day of sale and send an inquiry naming the wrong day. Neris carries both papers back to the gate clerk to challenge the discrepancy. He checks his original book, then points out that the crossed-out margin belongs to a different hand. By the time she returns with the correction, your inquiry has reached the bathhouse.
The merchant tries to leave with the payments. Your officers catch him at the back stair. His assistant gets away with the list of buyers, and the three letters burn in a brazier before Neris can put out the coals.
She saves one torn wrapper. Its writer will need to be found through the public noticeboard, which will also tell Salven that the investigation has followed his delivery address.
You send Nocticula the corrected date and the burned wrapper's description. Her answer leaves the error where you put it.{/n}
"You may keep the ingenious explanation. I shall keep the fact that he had time to burn the names. What will you offer the people you can no longer warn privately?"''', c('Post a notice for the missing buyers and record the lost names.', "decision", flags=f("buyers_unknown", "merchant_held", "inquiry_visible", "salven_warned", "wrapper_recovered"))),
    page("open", "Commander", '''The clerk recognizes his own abbreviated date. He is less interested in proving that you could have recognized it than in finding the person who has copied his office's hand.
He goes with Neris. The merchant hears the inquiry coming and reaches the stairs with his money; the soldiers there turn him back. His assistant escapes from a window onto the bathhouse roof. By the time the room is opened, the letters and buyers' list are burning. Neris pulls one torn wrapper out with a fire iron before its edges collapse. The address has burned away, but a red knot and part of a delivery number survive.
You have the merchant and his payments. You do not have a private means to warn every buyer. Neris writes a notice describing the guarantee without reproducing its seal.
Nocticula reads your account and asks whether the visible inquiry was deliberate.
"I preferred the clerk who knew his own book to a guess which sounded clever."
"He seems to have been worth consulting. Ask him whom the merchant paid for the room. Men often remember an unpaid week more accurately than a face."''', c('Post the notice and record that the assistant escaped with warning.', "decision", flags=f("buyers_unknown", "merchant_held", "salven_warned", "wrapper_recovered"))),
    page("decision", "Nocticula", '''"Now decide what your signature was worth."
{n}Her flourish still lies on your unused bait letter. The broker supplied enough of an address without taking it; the pattern can be destroyed or put to the limited use you promised.
The merchant admits selling reassurance. He claims never to have believed that any letter reached Nocticula. Neris writes that admission beside the payments, then makes him read it aloud.
You copy it through the answering mark. Nocticula underlines the word believed.{/n}
"He will discover a belief which suits the next person who questions him. Keep the first account."''',
         c('Publish the denial, reserve the recovered payments for claimants and burn the pattern.', "public", requires=f("concession_public")),
         c('Make the merchant supply his forwarding contacts. Establish the copied-report arrangement you promised.', "network", requires=f("concession_network", "reports_owed"))),
    page("public", "Narrator", '''{n}Neris places the seized payments in the clerk's strongbox and writes the sum on the posted denial. Claimants must describe what they bought; the notice does not promise that every claim can be paid.
You hold the unused bait letter over the lamp. The false flourish curls inward first. Nocticula's answering mark remains on the other sheet, beside the copy of your undertaking which she has returned for you to sign as fulfilled.
She has not returned her original.
"An expensive performance of honesty," she writes. "You have lost a useful imitation."
"I kept the address that answers."
"For the moment."
You leave her qualification where it is and sign. The copy darkens beneath your hand. Somewhere beyond the paper, she receives the proof that you surrendered the instrument instead of using it a second time.{/n}''', c('Keep the restitution account and relinquish the reusable pattern.', flags=f("the_paid_address_done", "concession_delivered", "pattern_destroyed", "restitution_reserved"))),
    page("network", "Commander", '''The merchant supplies two forwarding contacts. One address is empty when your officers reach it; the other belongs to a woman who copies advertisements and has kept his unpaid bill. She gives Neris the original wording for her claim against his seized funds.
Your new arrangement begins with a creditor, a room and a man who will lie when it becomes profitable. You write those limitations into the first report to Nocticula.
"You omitted the most troublesome proprietor," she answers.
You add your own name.
"Better."
Neris prepares a different notice: an office that receives requests, and a keeper who copies every one before she refuses it. Nocticula reads the copies. Nobody who writes to that office is told so.
Nocticula receives the first ledger page before you close the room for the night. It contains the merchant's account and your correction of it. She now knows which contacts you obtained and which escaped.
The false flourish stays in a sealed drawer. Using it outside this one forwarding arrangement would contradict the signed undertaking she holds.''', c('Retain the limited pattern and give her the first required report.', flags=f("the_paid_address_done", "concession_delivered", "pattern_retained", "first_report_delivered"))),
    page("withdraw", "Narrator", '''{n}You tell Nocticula that the remaining inquiries will go through your officers. Her answering mark lifts from the paper.
"Keep your undertaking," she writes before the last line vanishes. "I have mine."
The correspondence ends. The signature you gave her does not follow it out of the world.{/n}''', c('Close the channel. She keeps your signature.')),
])


add("the_retained_copy", "The copy she keeps", "the_paid_address_done", [
    page("start", "Nocticula", '''"Your clerk has better handwriting."
{n}The remark appears above the account you sent. Nocticula has circled a crowded line where you corrected a sum. Beneath it she has copied the figure correctly without improving your signature.{/n}
"You found the mistake."
"Neris found it. You admitted it. I am beginning to distinguish the services I receive from Drezen."
"Should I send her the compliment?"
"Send her an accurate account. She appears to prefer them."
{n}There is no outline of Nocticula in the wax, only the patient motion of the answering stroke. You find yourself watching it between sentences. A line curves beneath the last word.{/n}
"Read the rest before you decide I have praised you."''',
         c('Read her answer about the buyers whose names you recovered.', "known", requires=f("buyers_identified")),
         c('Read her answer about the buyers who must identify themselves publicly.', "unknown", requires=f("buyers_unknown", "wrapper_recovered"))),
    page("known", "Nocticula", '''"The first buyer wanted his daughter's letter delivered. He did not ask what she had written. The second wanted a rival denounced. The third wanted to learn which answer the second would receive."
These are the accounts Neris obtained from the three people on the saved list. Nocticula has reordered them.
"You have put the most innocent first," you write.
"I have put the man who knows least first. You may decide whether that improves him."
Neris has warned them individually. The daughter keeps her letter. The two rivals must conduct the next stage of their dispute without claiming that a demon lord has already selected a favorite.
Nocticula asks whether you regret losing their expectations before discovering what they would pay to keep them.
You tell her she received your answer in the report.
"I received what you did. I was asking whether you enjoyed doing it."''', c('Answer her about the bargain you actually carried out.', "bargain")),
    page("unknown", "Nocticula", '''"Two people have answered the notice. The merchant claims he recognizes one. She claims he never saw her face. An unfortunate distinction for the people holding the money."
Neris has not paid either claim yet. She is comparing the torn wrapper with the descriptions they supplied. The assistant remains missing, and Salven will have heard which address you found.
"You are not going to tell me that all the money returned to its owners," Nocticula writes.
"Not until it does."
"Then keep sending that account. A finished story would be less useful than this unfinished one."
You had expected mockery. The instruction is worse in a more practical way: she will know if a later report quietly forgets the people you could not find.
You leave their claims open in the ledger. The clerk has work for another morning, whether or not tonight's letter becomes pleasant.''', c('Keep the missing buyers and escaped assistant in the account.', "bargain")),
    page("bargain", "Commander", '''You turn her question back on her. She could have denounced a copied flourish through any servant able to hold a pen. Why ask you to spend days pursuing a broker?
"Because you asked for my company and offered your ingenuity. I wished to discover whether either survived an inconvenient task."
"And because you now possess a signed undertaking that links my name to yours."
"You did read it before signing."
"I am trying to discover whether you enjoyed receiving it."
The answering stroke pauses halfway through a curve.
"A little. You made an excellent show of noticing the price before paying it."
You can almost hear the smile. It is irritating how readily your memory supplies what the sheet withholds.''',
         c('I chose to end the fraud. You can use my signature to embarrass me, but you cannot make that choice yours.', "honesty", requires=f("pattern_destroyed", "restitution_reserved")),
         c('I kept a useful trade and gave you a view into it. We can both want the advantage without pretending the other is harmless.', "profit", requires=f("pattern_retained", "first_report_delivered"))),
    page("honesty", "Nocticula", '''"You imagine I need to own a choice to enjoy what it costs you."
"I imagine you enjoy letting people wonder."
"Often. You have deprived me of several agreeable minutes by saying it so promptly."
She encloses a copy of the false guarantee with its central line struck through. You had sent her the wording; she has returned it with your title replaced by Salven's own name.
"For your noticeboard. Let the guarantee promise that he will intercede with himself. It may finally describe a service he can provide."
You laugh before finishing the page. Her next line is already forming.
"There. Your gratitude has become less laborious. Keep it that way."
You set the corrected advertisement beside Neris's ledger. The pattern is gone, and the joke does not require you to recover it.''', c('Send the corrected advertisement to Neris and return to the private letter.', "history")),
    page("profit", "Nocticula", '''"Harmless would be a poor recommendation for either of us. I prefer to know which appetites can be given useful employment."
"You have employed mine for the price of reading a ledger."
"You have acquired a business for the price of admitting I may read it. We can quarrel about who was cheated after it produces something worth stealing."
She asks for one amendment. Neris is to mark blank reports as blank, not omit them. Otherwise a silence could conceal a profitable refusal.
You write the instruction while the answering stroke waits.
"You are very pleased with that," you tell her.
"With the amendment? Moderately. With your expression, considerably more."
"You cannot see it."
"Then you have no reason to change it."''', c('Record that even an empty reporting period needs an answer.', "history", flags=f("blank_reports_owed"))),
    page("history", "Nocticula", '''"Now that we have established what you will give away, tell me what you are still asking to receive."
{n}You set the business papers aside. The half-seal rests in its wrapping, at the same small distance from your hand.{/n}''',
         c('I refused an earlier offer. I want to ask for your company on terms I can actually choose.', "rejected", requires=("noct.parent_rejected",)),
         c('We already made promises. I want a personal invitation which does not pretend the lost means of contact has returned.', "patronage", requires=("noct.parent_active",), forbids=("noct.parent_rejected",)),
         c('There was no agreement to resume. I want an evening that begins with what we have actually done.', "missed", forbids=("noct.parent_active", "noct.parent_rejected"))),
    page("rejected", "Nocticula", '''"You were allowed to refuse the first offer. You seem determined to make me admire the exercise."
"I want you to understand why this answer would be different."
"Then give a different answer. Rehearsing the refusal has not made it more fascinating."
You cross out the next sentence, which had begun with an explanation she has already heard. Beneath it you write that you enjoy wanting something from her which she has not yet decided to give.
"A dangerous taste," she replies. "You will find me exceedingly accomplished at prolonging it."
"I have noticed."
She leaves those words unanswered for several breaths before adding a small correction to your canceled sentence. Even your discarded defense, apparently, could have been better.''', c('Leave the old refusal intact and ask for a new invitation.', "end")),
    page("patronage", "Nocticula", '''"I have not misplaced our earlier terms. Neither should you."
"This would not settle them."
"No. Nor purchase another gift, nor make my patience with your experiments inexhaustible."
You write that you are asking for her attention, not a favorable entry in an account. If she wants an answer about your ambition, she will have to hear something she may dislike.
"I have heard you before. That danger is not new."
"Then you should know whether you miss it."
The answering stroke goes still. When it moves again, it crosses out the word should.
"You may ask," she writes. "Try to remember how that differs from supplying my reply."
You rewrite the question. She keeps both versions.''', c('Keep the earlier bargain separate and let her answer the personal question.', "end")),
    page("missed", "Nocticula", '''"You have no shared night to invoke, so you invoke a broker and a clerk. An original courtship."
"Would an invented night improve it?"
"It would improve my opinion of your imagination. Briefly."
You tell her you would like to discover which of her silences mean she is bored and which mean she is deciding how to make your next sentence expensive.
"And what will you do with that distinction?"
"Risk a better sentence."
She writes nothing for long enough that you start considering several. Then a single line arrives.
"Keep one. I may ask to hear it."''', c('Wait for an actual invitation.', "end")),
    page("end", "Narrator", '''{n}The last page carries a time: after the following evening's reports. Nocticula asks you to put aside a clean sheet and leave the business ledger closed unless you have something urgent to tell her.
You write that the city may provide something urgent without asking either of you.
"Then it will have to compete," she answers. "I dislike a dull interruption more than an important one."
Her mark darkens. You put the clean sheet beneath the wax before returning to the work you have delayed. It makes an absurdly conspicuous patch of white on the desk.{/n}''', c('Keep the offered time and finish the remaining work.', flags=f("the_retained_copy_done", "personal_answer_invited"))),
])


add("an_answer_of_her_own", "An answer of her own", "the_retained_copy_done", [
    page("start", "Narrator", '''{n}By the time the answering stroke moves, you have read the same paragraph of a supply report three times. You finish it before turning the sheet. Nocticula has written a question where your hand will rest.{/n}
"Did you choose the sentence?"
"I chose several. Most became less impressive while I waited."
"Good. I have been spared the first draft."
{n}You tell her that you wanted to stop imagining the answer in her voice long enough to hear the one she actually gives. The mark draws a slow curve beneath your words.{/n}
"You could have asked whether I wanted this evening."
"Do you?"
"Yes. I have found you troublesome in a manner which survives my having something else to do. I would like to discover how long that remains entertaining."
{n}The next line is smaller, as though she has brought the pen closer rather than raised her voice.{/n}
"You may call that an invitation. Do not spend it all congratulating yourself."''',
         c('I want continued private company with you, and I want us to know exactly what we are agreeing to.', "terms"),
         c('I want the political exchange, but I will decline the personal invitation.', "decline", flags=f("personal_declined", "closed"))),
    page("terms", "Nocticula", '''"You may send a personal request through the mark. I may answer it. Either of us may end an evening without turning the silence into permission to enter the other's room."
"And other company?"
"Keep it interesting enough that you do not arrive here to complain about it. I am not offering to become the occupation of every hour you possess."
You ask whether she expects names.
"When somebody is involved in the business you bring me, accuracy is useful. When you wish to make me jealous, I suggest choosing a less predictable amusement."
"I was considering whether you would insist on exclusivity."
"I insist that an invitation intended for me should interest me. You will discover that this is work enough."
Her next line returns to the seal. You have permission for chosen exchanges, no standing permission for sleep or possession, and no right to counterfeit her answer if she refuses one.
She retains the signed undertaking. Closing the private channel later will not erase the concession already made or prevent either of you speaking about an actual political dispute.''',
         c('Ask what the narrow fold permits now.', "narrow", requires=f("channel_provisional"), forbids=f("channel_letters_only")),
         c('Keep the repaired or written channel limited to the letters already agreed.', "letters", requires=f("channel_letters_only"))),
    page("narrow", "Nocticula", '''"It permits you to ask before turning it."
{n}You leave the edge flat.{/n}
"May I?"
"Not tonight."
{n}The answer is prompt enough to make you laugh. You tell her she could have saved the explanation.{/n}
"I wanted to hear whether you would ask after receiving it. Now I have."
"And you enjoyed refusing."
"A little. You may decide whether the prospect of another evening survives that terrible injury."
{n}You have still seen no part of her room. The paper remains a sheet of paper with a hand moving on its other side. Her last sentence leaves a broad blank beneath it.{/n}''', c('Continue negotiating without opening the fold.', "risk")),
    page("letters", "Nocticula", '''"Letters, then. No window because an evening has become personal."
"You will have to imagine my expression."
"I have been doing quite well. You will have to become less predictable if you wish to keep that privilege."
You ask whether she dislikes being imagined.
"I dislike being corrected. People are generous with the improvements they believe a woman has been waiting to receive."
"And what would you correct about me?"
"The confidence with which you asked that question. I shall leave the rest until it inconveniences me."
You fold down the corner of the sheet before it can brush the lamp. The mark waits while you move it. Her answer has followed the wax; nothing has entered the room.''', c('Keep the written limit and ask about the price she still retains.', "risk")),
    page("risk", "Commander", '''You ask whether the undertaking will remain private.
"While keeping it private suits me. You gave it because it was worth something. Do not now ask me to make it worthless as proof of affection."
"I could be asked why I placed my name in your keeping."
"You might answer. I should be interested to hear which part you omit."
You put your palm flat beside the wax. The mark on the paper stops moving, as if it had felt the weight of your hand and is deciding whether to bite.
You tell her that the same applies to you. An enemy might one day make it useful to say that she answered.
"Then give an accurate account," she writes. "Inaccurate ones attract tedious corrections."
Beneath her last line she has left a blank the width of a signature, and the wax beside it has gone warm, the way skin goes warm.''',
         c('I accept. The letters, the danger that comes with them, and you. Mostly you.', "accept", flags=f("renewed_agreement", "personal_risk_accepted")),
         c('I will keep the concession, but I do not want this personal arrangement. Close the private channel.', "decline", flags=f("personal_declined", "closed"))),
    page("accept", "Nocticula", '''"An ambitious evening. We shall see how much of it you can sustain."
{n}Below your answer she writes her own name. The answering mark crosses its last letter and returns to the broken edge of the wax. It has sealed this page, not joined the two halves.{/n}
"For the record," she adds. "You seem to enjoy acquiring them."
"This one has better handwriting."
"This one has an excellent reason to be legible. I may wish to quote you."
{n}You ask her to stay while you tell her the discarded first sentence. She declines. Then she asks for the second.
It is worse than you remembered. Halfway through writing it, you stop and cross out a word. Nocticula supplies a more dangerous one beneath it.
You spend the next few minutes arguing about the difference. Neither of you opens a ledger. The lamp burns lower while the mark moves between your unfinished lines.{/n}''', c('Keep the agreed correspondence and spend the rest of this evening in it.', flags=f("an_answer_of_her_own_done"))),
    page("decline", "Nocticula", '''"Then you have your answer. So have I."
{n}You ask whether she intends to treat the refusal as another debt. Her reply is precise.{/n}
"You offered an undertaking for the work we did. I still hold it. I offered you company, and you have declined. Do not make the first transaction an excuse to misunderstand the second."
{n}The answering stroke draws itself out of the wax. No figure replaces it and no hand reaches through the sheet. You wait until the paper is still, then place it beside the business account.
There may be political business to conduct again. You have not retained a personal channel through which to pretend this answer was unfinished.{/n}''', c('Leave the personal invitation declined.', flags=f("an_answer_of_her_own_done"))),
])


def outcomes(current, initial, words):
    """Enumerate selected acyclic paths, including their terminal consequences."""
    nodes = {node["Id"]: node for node in current["Nodes"]}
    def walk(key, flags, count, visited):
        assert key not in visited, (current["Id"], key)
        node = nodes[key]
        choices = [choice for choice in node["Choices"] if allowed(choice, flags)]
        assert choices, (current["Id"], key, "no eligible answer")
        for choice in choices:
            if choice["Abort"]:
                continue
            state = flags | set(choice["Set"])
            total = count + words(node["Text"]) + words(choice["Text"])
            check = choice.get("Check")
            for target in (check["Success"], check["Failure"]) if check else (choice.get("Next"),):
                if target:
                    yield from walk(target, state, total, visited | {key})
                else:
                    yield state, total
    return walk(current["Nodes"][0]["Id"], set(initial), 0, set())


def validate():
    """Check this draft's graphs and exact supported continuation fixtures."""
    import runpy
    from pathlib import Path
    from storylines import nocticula_trickster_acquisition as opening
    words = runpy.run_path(str(Path(__file__).resolve().parents[1] / "tools/measure-story-content.py"))["words"]
    native_aliases = set(opening.ETUDES) | set(opening.COMPLETED_ETUDES) | set(opening.SEEN_CUES) | set(opening.SELECTED_ANSWERS)
    assert len({s["Id"] for s in SCENES}) == len(SCENES)
    all_nodes = 0
    for s in SCENES:
        nodes = {node["Id"]: node for node in s["Nodes"]}
        assert len(nodes) == len(s["Nodes"])
        all_nodes += len(nodes)
        seen = set()
        def visit(key, stack):
            assert key not in stack
            if key in seen:
                return
            seen.add(key)
            for choice in nodes[key]["Choices"]:
                assert all(flag.startswith("noct.acq.") for flag in choice["Set"])
                assert not set(choice["Set"]) & native_aliases
                assert not set(choice["Set"]) & {"noct.acq.gift_renewed", "noct.acq.council_fight", "noct.acq.conflict_resolved_verified", "noct.acq.postconflict_reply_verified"}
                check = choice.get("Check")
                assert not check or (not choice.get("Next") and not choice["Abort"])
                for target in (check["Success"], check["Failure"]) if check else (choice.get("Next"),):
                    if target:
                        assert target in nodes
                        visit(target, stack | {key})
        visit(s["Nodes"][0]["Id"], set())
        assert seen == set(nodes)
    histories = {"missed": set(), "rejected": {"noct.parent_rejected"}, "lost_patronage": {"noct.parent_active", "noct.acq.original_gift_completed"}}
    channels = {"narrow": set(f("channel_provisional")), "letters": set(f("channel_letters_only")), "exposed": set(f("channel_letters_only", "channel_exposed", "channel_repaired", "sketch_surrendered"))}
    result = {}
    closed = 0
    completed = 0
    for history, h in histories.items():
        for channel, ch in channels.items():
            base = {"trickster", *f("correspondence_trial", "her_hand_done"), *h, *ch}
            for block in ("noct.dead", "noct.acq.council_fight", "noct.acq.closed"):
                assert not allowed(SCENES[0], base | {block})
            assert not allowed(SCENES[0], base - {"noct.acq.correspondence_trial"})
            states = [(base, 0)]
            for s in SCENES:
                next_states = []
                for state, count in states:
                    assert allowed(s, state)
                    for updated, addition in outcomes(s, state, words):
                        if "noct.acq.closed" in updated:
                            closed += 1
                            assert "noct.acq.renewed_agreement" not in updated
                            assert not any(allowed(later, updated) for later in SCENES)
                            continue
                        next_states.append((updated, count + addition))
                states = next_states
            assert states
            for state, count in states:
                assert set(f("concession_delivered", "undertaking_held", "personal_risk_accepted", "renewed_agreement", "an_answer_of_her_own_done")) <= state
                assert len(set(f("pattern_destroyed", "pattern_retained")) & state) == 1
                assert len(set(f("buyers_identified", "buyers_unknown")) & state) == 1
                if "noct.acq.pattern_retained" in state:
                    assert set(f("first_report_delivered", "blank_reports_owed")) <= state
                if "noct.acq.buyers_unknown" in state:
                    assert set(f("salven_warned", "wrapper_recovered")) <= state
            completed += len(states)
            result[history + "/" + channel] = dict(minimum=min(n for _, n in states), maximum=max(n for _, n in states), completed_paths=len(states))
    tried = {"noct.acq.address_check_tried"}
    answers = [c for c in SCENES[1]["Nodes"][0]["Choices"] if allowed(c, tried)]
    assert not any(c.get("Check") for c in answers)
    assert any(c.get("Next") == "open" for c in answers)
    evidence = {node["Id"]: node for node in SCENES[1]["Nodes"]}
    assert "counterfoil" in evidence["start"]["Text"] and "both papers are on your desk" in evidence["start"]["Text"]
    for method in ("mistake", "open"):
        assert "wrapper" in evidence[method]["Text"].lower()
        assert all("noct.acq.wrapper_recovered" in choice["Set"] for choice in evidence[method]["Choices"])
    joined = {}
    fixtures = (
        ("missed", set()), ("missed_gift", {"noct.gift"}),
        ("rejected", {"noct.parent_rejected"}),
        ("rejected_gift", {"noct.parent_rejected", "noct.gift"}),
        ("lost", {"noct.parent_active", "noct.acq.original_gift_completed"}),
        ("renewed_gift", {"noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed"}),
    )
    for name, history in fixtures:
        base = {"trickster", "noct.acq.audience_question", *history}
        entries = [s for s in opening.SCENES[:3] if allowed(s, base)]
        assert len(entries) == 1
        states = list(outcomes(entries[0], base, words))
        # These two native witnesses are fixture inputs, not produced by this draft.
        states = [(state | {"noct.acq.council_disclosed", "noct.socoth_plan_exposed"}, count)
                  for state, count in states if "noct.acq.closed" not in state]
        for s in [*opening.SCENES[3:5], *SCENES]:
            next_states = []
            for state, count in states:
                assert allowed(s, state)
                for updated, addition in outcomes(s, state, words):
                    if "noct.acq.closed" not in updated:
                        next_states.append((updated, count + addition))
            states = next_states
        assert states and all("noct.acq.renewed_agreement" in state for state, _ in states)
        joined[name] = dict(minimum=min(n for _, n in states), maximum=max(n for _, n in states), completed_paths=len(states))
    return dict(scenes=len(SCENES), nodes=all_nodes, completed_paths=completed, closure_paths=closed,
                selected_concession_words=result, selected_opening_plus_concession_words=joined,
                status="unregistered author draft; no review approval or harbor join")


if __name__ == "__main__":
    import hashlib
    import json
    from pathlib import Path
    result = validate()
    result["sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
    print(json.dumps(result, indent=2))
