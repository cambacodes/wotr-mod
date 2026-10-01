"""Carry ordinary-route consequences into restored private contact."""
from story_format import c, n, scene

SCENES = [scene("konomi.private_history", "What was left unanswered", "Konomi", 3, "", [
    n("arrival", "Narrator", '''{n}Konomi sends a time when the courtyard will be free. She asks you to come before you arrange the visit to the wagon yard.{/n}''',
      c('[Meet her to discuss what your earlier conversations left unfinished.]', "start", requires=("konomi.disagreement",)),
      c('[Meet her to arrange the next visit.]', "fresh", forbids=("konomi.disagreement",)),
      c('[Return to her note when you have time.]', abort=True)),
    n("fresh", "Konomi", '''"The carriers have agreed to show me the wagons. I would like you to come. They have agreed to that as well."
{n}She gives you the location and the time, and then the size of her fee, in case you require persuading.{/n}
"I shall be working. I hope you will find me interesting company even when I am asking somebody else an inconvenient question."
{n}She smiles as you settle the arrangement.{/n}
"Good. I would like to see you there."''', c('[Arrange to meet her at the yard.]', flags=("konomi.private_history_ready",))),
    n("start", "Konomi", '''{n}Konomi meets you in the courtyard again. This time a folded petition lies beneath a cup she has set out for you. Beside it is a narrow writing case, firmly shut.{/n}
"I enjoyed seeing you. Then I went through my papers and found how much we had managed not to discuss."
{n}She draws the petition clear of the cup.{/n}
"Before we make pleasant plans, we settle the old accounts. I do not open a new ledger on top of one that does not balance."''',
      c('[Sit down and hear her out.]', "petition"),
      c('[Ask to return when you can give the conversation time.]', abort=True)),
    n("petition", "Narrator", '''{n}The paper is the settlement's petition that once prompted an argument about a shipment assigned to Drezen. Konomi leaves it where you can read it.{/n}''',
      c('[Ask for the figures you never received.]', "figures", forbids=("konomi.petition_resolved",)),
      c('[Recall the delivery and the storehouse inspection she requested.]', "delivered", requires=("konomi.petition_resolved",))),
    n("figures", "Konomi", '''"Their reserve was spoiled. The figures we were given counted grain they could no longer eat. I should have asked somebody to inspect it before I treated the answer as reliable."
{n}She takes a receipt from inside the folded petition.{/n}
"I sent the corrected account to the charitable collection in Nerosyan. They purchased grain through their own suppliers. This confirms the first delivery. None of it came from the shipment reserved for Drezen."
{n}She lets you examine the receipt before continuing.{/n}
"I did not need my appointment to ask a correspondent whether a donation had arrived. It did take longer to obtain an answer addressed to me alone. People who replied promptly to the officer have discovered other demands on their time."
{n}She points to the storehouse named below the delivery.{/n}
"I have asked whether the roof has been repaired. Until somebody checks it, this receipt is evidence of one delivery, not a solution to the winter."''',
      c('"I wanted you to take their need seriously. Thank you for following it through."', "aid", requires=("konomi.aid_priority",)),
      c('"We protected Drezen. We still owe them an answer about the storehouse."', "reserve", requires=("konomi.reserve_priority",)),
      c('"We should have been able to finish this argument while we were still speaking."', "frank")),
    n("aid", "Konomi", '''"You were right about the urgency. I was wrong to make them bear the consequences of unreliable figures while I waited for a more convenient argument."
{n}She draws the receipt back toward her.{/n}
"Remember that I admitted it. I would prefer not to spend the next disagreement persuading you that I am capable of doing so."''', c('[Acknowledge the delivery without declaring the remaining work finished.]', "letter", flags=("konomi.petition_resolved",))),
    n("reserve", "Konomi", '''"Yes. Retaining the shipment was defensible. It would not have made the spoiled grain edible."
{n}She places the receipt beneath the petition.{/n}
"I shall keep asking about the roof. I would like somebody there to become sufficiently tired of my letters to send a proper answer."''', c('[Acknowledge the delivery without declaring the remaining work finished.]', "letter", flags=("konomi.petition_resolved",))),
    n("frank", "Konomi", '''"We should."
{n}She studies the annotations for a moment.{/n}
"I am still angry about the dismissal. The petitioners did not dismiss me. Leaving their account unanswered would have been an exceedingly petty way to prove that my absence mattered."
{n}She folds the receipt into the petition.{/n}
"I found another reason to write."''', c('[Acknowledge the delivery without declaring the remaining work finished.]', "letter", flags=("konomi.petition_resolved",))),
    n("delivered", "Konomi", '''"You remember. Good. I did not want our last disagreement to become the only thing either of us recalled doing together."
{n}She refolds the petition.{/n}
"The receipt did not stop being real when you dismissed me. Nor did the need to keep the next delivery dry. I have kept the address for that correspondence."''', c('[Ask what else she wants to discuss.]', "letter")),
    n("letter", "Narrator", '''{n}Konomi moves the petition aside and rests one hand on the writing case.{/n}''',
      c('[Ask what became of the stolen letter and your answer to it.]', "unanswered", requires=("konomi.leak",), forbids=("konomi.scandal_answered",)),
      c('[Ask what remains after the response she already described.]', "answered", requires=("konomi.scandal_answered",)),
      c('[Ask what she wants from your letters now.]', "new_letters", forbids=("konomi.leak", "konomi.scandal_answered",))),
    n("unanswered", "Konomi", '''"I did not withdraw our reply. Whatever happened afterward, I would not give its recipient the pleasure of deciding that I had been ashamed to write it."
{n}She opens the case and removes a folded answer.{/n}''',
      c('[Ask about the consequences of the public acknowledgment.]', "public", requires=("konomi.public",)),
      c('[Ask whether the discreet reply helped her find the channel.]', "discreet", forbids=("konomi.public",))),
    n("public", "Konomi", '''"A noble household offered to keep carrying my letters if I supplied copies of my recommendations. Its secretary also withdrew an invitation to a private policy dinner. He described neither request as a punishment."
{n}Her expression hardens.{/n}
"I told him he could read my published advice. I did not authorize him to inspect my private correspondence. Since then, I have used other carriers. That is an expense and an inconvenience. I do not intend to describe it as a triumph."
{n}She puts the answer beside the case.{/n}
"The dinner matters too. People decide whom to hear before they invite anybody to a formal meeting. Losing my appointment has not made me indifferent to that."''', c('[Ask about the source of the copied page.]', "source", flags=("konomi.public_cost",))),
    n("discreet", "Konomi", '''"I sent three dull accounts of a proposed inspection through three different channels. Each gave a different date. Somebody with no reason to have received any of them complained about the second date."
{n}She opens the answer just far enough to show you the line.{/n}
"He thought he was proving how well informed he was. It was generous of him to specify the channel."
{n}Her smile is brief and sharp.{/n}
"I still enjoy that part. Dismissal has not improved my character nearly as much as some people might hope."''', c('[Ask who supplied the copy.]', "source", flags=("konomi.traced_leak",))),
    n("source", "Konomi", '''"The copyist who handled my writing case sold the page to an intermediary seeking access to my correspondents. When I asked the copyist to account for the work, he named his buyer. He would rather share the blame than be left with all of it."
{n}She folds the answer away.{/n}
"He will not handle my correspondence again. I have requested a hearing through his association about the payment and the use of its members' services. Losing my officer's appointment does not prevent me from being a client whose letter was sold."
{n}She closes the writing case and leaves her hand on it.{/n}
"That is as far as it has gone. Finding the channel did not settle the complaint."''', c('[Acknowledge what her investigation established.]', "trust", flags=("konomi.scandal_answered",))),
    n("answered", "Konomi", '''"The investigation remains what it was. Our disagreement did not make the copyist trustworthy again, and I have not given him any more of my letters."
{n}Her fingers rest on the clasp of the writing case.{/n}
"There is something I want to ask before I put this away."''', c('[Listen.]', "trust")),
    n("trust", "Narrator", '''{n}She looks directly at you, leaving the closed case between her hands.{/n}''',
      c('[Acknowledge that you still owe her an apology for proposing to deny the letter.]', "apology", requires=("konomi.almost_denied",), forbids=("konomi.apologized",)),
      c('[Tell her you remember your apology and intend to live up to it.]', "remember", requires=("konomi.apologized",), forbids=("konomi.hearing_trust_repaired",)),
      c('[Tell her you still stand by the reply you made together.]', "stood", forbids=("konomi.almost_denied", "konomi.apologized",)),
      c('"After the hearing, you told me you believed me. I have not forgotten what it took to get there."', "repaired", requires=("konomi.apologized", "konomi.hearing_trust_repaired"))),
    n("apology", "Konomi", '''"Yes. You do."
{n}She does not soften the answer.{/n}
"You asked me to call the letter false. I refused, and you agreed to a discreet acknowledgment. I remember that you changed your answer. I also remember what you asked first."
{n}She takes her hands from the case.{/n}
"We have discussed the dismissal. This is another thing. I will not let the larger argument swallow it merely because we would both rather enjoy the afternoon."''',
      c('"I was frightened of what they would do with it. I asked you to make our relationship a lie instead of admitting that fear. I am sorry."', "accepted", flags=("konomi.apologized",)),
      c('"I will not give you the acknowledgment you want."', "part")),
    n("accepted", "Konomi", '''"There. That is the clause I was waiting for. Not a general sorrow; the specific item."
{n}She exhales slowly.{/n}
"The next time somebody waves a page of mine at you, I shall remember this afternoon, and I shall remember the other one too. I do not forget debts, paid or unpaid. It is a professional failing."
{n}She moves the case off the bench beside her.{/n}
"Sit. I have not decided what to do with you yet. You may as well be comfortable while I think."''', c('[Sit, and let her think.]', "hearing")),
    n("remember", "Konomi", '''"I remember it too. I do not need you to deliver it again as though I had mislaid the first version."
{n}She moves the case aside.{/n}
"I want to know that the next private letter will not become something you are prepared to disown when it is inconvenient. That will take more than one good answer from either of us."''', c('[Tell her to judge you by what you do next.]', "hearing")),
    n("stood", "Konomi", '''"So do I. I am glad we can still say that."
{n}She moves the case away from the space between you.{/n}
"I did not invite you back so that we could spend every afternoon defending the old ones. But I wanted to be certain we were not pretending they had belonged to somebody else."''', c('[Ask what remains to be done.]', "hearing")),
    n("repaired", "Konomi", '''"I did believe you. I still do."
{n}She moves the case onto her other side, clearing the space beside her.{/n}
"I am angry about losing my appointment. I can give you a lengthy account of why, if you have somehow misplaced the first one. But you did not disown that letter when we disagreed. I noticed."
{n}The corner of her mouth lifts.{/n}
"Come and sit here. You need not conduct this conversation from the far end of the bench."''', c('[Sit beside her and ask what remains of the complaint.]', "hearing")),
    n("hearing", "Narrator", '''{n}Before you leave the subject, she takes out the association's correspondence.{/n}''',
      c('[Acknowledge that the complaint still needs its hearing.]', "pending", forbids=("konomi.hearing_finished",)),
      c('[Keep the hearing outcome intact as you discuss what comes next.]', "heard", requires=("konomi.hearing_finished",))),
    n("pending", "Konomi", '''"I shall keep pursuing it. The buyer should not discover that selling a private page becomes harmless as soon as its owner changes her address."
{n}She secures the case.{/n}
"We have answered one another today. We have not obtained a decision from the association. Remember the difference when somebody tells you the matter is over."''', c('[Keep the unresolved complaint in mind.]', "finish", flags=("konomi.private_hearing_needed",))),
    n("heard", "Konomi", '''"The decision remains on record. I have not asked the association to reconsider it because our own circumstances changed."
{n}She secures the case.{/n}
"Nor will I make you defend our choice about the evidence all over again. We made it together. We can live with what it cost."''', c('[Leave the recorded outcome unchanged.]', "finish")),
    n("new_letters", "Konomi", '''"I want the letters we write now to be meant for one another. We have both had practice composing answers for a roomful of people who were not there."
{n}She puts the case aside without opening it.{/n}
"I would like something I can read without preparing a reply on Mendev's behalf. It need not be impressive. It does have to sound like you."''', c('[Promise to write to her as yourself.]', "finish")),
    n("finish", "Konomi", '''{n}Konomi gathers the petition and case, then leaves them on her side of the courtyard bench.{/n}
"Now tell me when you can come to the wagon yard. I have not finished earning that fee."
{n}The change of subject is deliberate. For the first time that afternoon, it does not feel hurried.{/n}''',
      c('[Arrange the next visit with the earlier history acknowledged.]', flags=("konomi.private_history_ready",))),
    n("part", "Konomi", '''{n}She takes up the case and stands.{/n}
"Then I cannot offer the return you hoped for. I will not begin by teaching myself to expect less honesty from you."
{n}At the passage she waits for you to leave before returning to the courtyard. The papers remain hers to pursue. You do not arrange another private meeting.{/n}''',
      c('[Accept that the courtship has ended.]', flags=("konomi.closed", "konomi.private_parted", "konomi.private_future"))),
], Relationship="konomi", Remote=True, Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[3, 5],
    requires=("konomi.dismissed", "konomi.office_completed", "konomi.private_meeting"),
    forbids=("konomi.present", "inhuman", "konomi.farewell", "konomi.private_departed", "konomi.private_history_ready", "konomi.carriers"), delay=24, optional=True)]

for page in SCENES[0]["Nodes"]:
    page["Portrait"] = "Konomi"
