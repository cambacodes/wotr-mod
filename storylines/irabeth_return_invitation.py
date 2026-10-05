"""Authored personal audience after a living departure, without restoring office."""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"
SCENES = []
# eng7-f6c: the outgoing inquiry is handled at the quartermaster's desk.
QUARTERMASTER = "8692bff6041c47a0b13158d5977f291b"
QUARTERMASTER_HUB = "fa57cf97ea01bf34e9a30f6ad444381e"


def s(id, title, nodes, requires=(), delay=0, physical=False):
    request = id == "return_request"  # eng7-f6c: physical inquiry, one remote reply.
    for page in nodes:
        page["Portrait"] = "Irabeth"
    SCENES.append(scene("irabeth." + id, title, "Irabeth", 5,
        '"About the requisition bearing Irabeth\'s name."' if request else
        '"You agreed to hear me. May we speak?"' if physical else "", nodes,
        Relationship="irabeth", AfterDeparture="irabeth", Remote=not (physical or request),
        Chapters=[5], Areas=[DREZEN],
        requires=("trickster", "irabeth_gone", *requires,
                  *(('irabeth.return_meeting_arrived', 'irabeth.return_meeting_accepted') if physical
                    else ('irabeth.return_correspondence_available',))),
        forbids=("irabeth_dead", "inhuman", "swarm", "true_lich", "closed", "irabeth.closed",
                 "irabeth.return_meeting_declined", *(("irabeth.return_meeting_accepted",) if id == "return_reply" else ())),
        delay=delay, optional=True,
        **({"ContactUnit": IRABETH, "AnswerLists": ["871af36f2ab2b1f40b5de77976c54276"]} if physical else
           {"ContactUnit": QUARTERMASTER, "AnswerLists": [QUARTERMASTER_HUB]} if request else {})))


s("return_request", "An order without an officer", [
    n("start", "Narrator", '''{n}The requisition bears Irabeth's name. Its date is later than her departure.{/n}
{n}You find it among papers awaiting a countersignature. A supplier wants payment for a shipment supposedly accepted by an officer who no longer answers to your command. The clerk suggests striking out the name and asking the quartermaster to sign instead.{/n}
{n}That would settle the account. It would also tell whoever submitted it precisely how much attention Drezen pays to its former officers.{/n}''',
        c('[Compare the delivery dates with the departure records.]', check=dict(
            Skill="SkillKnowledgeWorld", DC=28, Success="precise", Failure="uncertain", CommanderOnly=True),
            forbids=("irabeth.return_docket_precise", "irabeth.return_docket_uncertain")),
        c('[Use the discrepancy you have already established.]', "purpose", requires=("irabeth.return_docket_precise",)),
        c('[Continue the inquiry with its limits stated.]', "purpose", requires=("irabeth.return_docket_uncertain",),
            forbids=("irabeth.return_docket_precise",)),
        c('[Keep the account pending while you consider another approach.]', abort=True)),
    n("precise", "Narrator", '''{n}The supplier has copied the heading from an older receipt, including a correction in Irabeth's name. The handwriting changes halfway through the new date. It is enough to challenge the claim, though not enough to identify who altered it.{/n}
{n}You set aside the original. Whoever answers your inquiry will receive a copy with the disputed date clearly visible. Let them explain the convenient officer before you explain the inconvenient records.{/n}''',
        c('[Prepare the copies, keeping the original in Drezen.]', "purpose", flags=("irabeth.return_docket_precise",))),
    n("uncertain", "Narrator", '''{n}Two dates appear to contradict each other until you find the notation for goods received before an account was entered. The remaining discrepancy might be fraud or might be an exhausted clerk copying the wrong heading.{/n}
{n}You can ask a useful question without pretending to possess its answer. The original stays in Drezen. The copy goes out with the uncertainty intact.{/n}''',
        c('[Mark the discrepancy as an open question.]', "purpose", flags=("irabeth.return_docket_uncertain",))),
    n("purpose", "Narrator", '''{n}An inquiry could reach Irabeth through the same couriers who carried her last instructions. A military summons would be easy to write and easy for her to refuse.{/n}
{n}A useful problem is a better opening. You draft the account first, then leave room for the reason you want her to read it herself.{/n}''',
        c('[Ask her to help prevent someone from profiting by using her name.]', "public"),
        c('[Explain how questioning the supplier before showing the records could expose an accomplice.]', "trap"),
        c('[Put the letter aside without sending it.]', abort=True)),
    n("public", "Narrator", '''{n}You write that she owes Drezen no signature on this account. You would nevertheless value her judgment about the use of her name. She can answer by letter, name someone else to examine the papers, or meet you privately.{/n}
{n}The next line takes longer. You would like to speak to her, beyond the account. You have not forgotten that she left. You ask whether she will hear you. You do not pretend the argument is over.{/n}''',
        c('[Send the inquiry and personal request together.]', flags=("irabeth.return_request_sent", "irabeth.return_public_case"))),
    n("trap", "Narrator", '''{n}You outline the questions the supplier should receive, in order. First ask who witnessed the delivery. Let the reply acquire a signature. Only then produce the departure record.{/n}
{n}You offer Irabeth the copies and invite her to find the flaw in your plan. Beneath that, you admit the second purpose of the letter. You want a conversation with her. Giving her a problem worth your time is your way of asking for some of hers.{/n}
{n}You read the paragraph again. It is a calculated invitation. You leave the calculation visible.{/n}''',
        c('[Send the plan with the request to speak privately.]', flags=("irabeth.return_request_sent", "irabeth.return_supplier_trap"))),
])

s("return_reply", "The question she returns", [
    n("start", "Narrator", '''{n}The reply arrives with your copy enclosed. Irabeth has written in the margin beside the disputed signature.{/n}
{n}"That is not my hand. It does not tell us whose hand it is. Do not punish the clerk for being the easiest person to find."{/n}
{n}There is a second sheet. She has begun it with your name rather than your title.{/n}''',
        c('[Read her response to the evidence.]', "precise", requires=("irabeth.return_docket_precise",)),
        c('[Read her response to the uncertain account.]', "uncertain", forbids=("irabeth.return_docket_precise",))),
    n("precise", "Narrator", '''{n}"The copied correction is useful. Keep the original, and send no accusation ahead of your questions. An honest supplier should be able to identify a witness without being told which answer you expect."{/n}
{n}She has added a short list of details worth asking for. The last is a cart number you had overlooked.{/n}''', c('[Read the next paragraph.]', "motive")),
    n("uncertain", "Narrator", '''{n}"You were right to leave the discrepancy open. The receipt is a copy of an account, not proof that the goods arrived on the date someone entered them. Ask for the cart number and the name of the person who unloaded it."{/n}
{n}She has crossed out one of your proposed questions. Beside it she writes: "This tells them too much."{/n}''', c('[Read the next paragraph.]', "motive")),
    n("motive", "Narrator", '''{n}"I also read the other request. I assume you expected me to notice why the account came to me instead of remaining with the quartermaster."{/n}
{n}The next sentence begins below a small blot of ink.{/n}
{n}"I will hear you in Drezen. Once, for now. I will not return to duty by walking into a room, and I will not sign a request to put me back into uniform. If this is a conversation you still want, send word. I can arrange a private hour after the next courier has reached me."{/n}
{n}She has signed both sheets. The signatures are the same, though the second has no rank beneath it.{/n}''',
        c('[Accept the personal meeting on those terms.]', "accept"),
        c('[Decline the meeting and retain her written advice.]', "decline"),
        c('[Keep her reply while you consider it.]', abort=True)),
    n("accept", "Narrator", '''{n}You send a brief acceptance and arrange an hour without an audience of officers. The account remains with the quartermaster, under instructions to preserve the original and record the supplier's answer.{/n}
{n}Irabeth has agreed to a conversation. You still have to make it worth the trouble she is taking to attend.{/n}''',
        c('[Wait for the agreed private hour.]', flags=("irabeth.return_meeting_accepted",))),
    n("decline", "Narrator", '''{n}You thank her for the corrections and say that you will not ask her to make the visit. Her advice goes to the quartermaster. The personal letter stays with you.{/n}''',
        c('[Leave the meeting unarranged.]', flags=("irabeth.return_meeting_declined",))),
], requires=("irabeth.return_request", "irabeth.return_request_sent"), delay=48)

s("return_first_words", "An hour outside the chain of command", [
    n("start", "Irabeth", '''"You chose a real account. I checked."
{n}Irabeth carries the copies you sent. She has brought no report case, and she does not salute.{/n}
"I thought you might have found a convenient piece of unfinished business after deciding that you wanted to see me."
{n}She lays the papers between you.{/n}
"You did. But you also found a question worth answering. Which part would you like to discuss first?"''',
        c('"Your correction. I would rather begin with the part of my plan you improved."', "work"),
        c('"You saw the invitation inside the inquiry. I expected you to."', "strategy")),
    n("work", "Irabeth", '''"The cart. A clerk can copy an officer's name without ever seeing the goods. A carter must explain where the load went."
{n}She turns the page toward you, tapping the margin.{/n}
"If your supplier can name a real delivery, you have a bad record to correct. If not, you have a different question. Do not decide which you prefer before you hear the answer."
{n}You ask which detail she would withhold. She considers, then crosses out a line on your copy.{/n}
"That one. Let them supply it."
{n}For the first time since entering, she looks interested in what you will say next.{/n}''',
        c('"You have made the trap less comfortable. Good."', "personal"),
        c('"And less likely to catch the wrong person."', "personal")),
    n("strategy", "Irabeth", '''"Yes. An officer's unfinished work, carefully placed where she cannot fail to see it."
{n}Her tone is dry.{/n}
"I considered returning the papers with someone else's recommendation. I nearly did."
{n}She waits for your reaction before continuing.{/n}
"Then I read the part where you admitted what you wanted. I preferred that to a summons dressed up as a courtesy. I'm not here because you asked. I'm here because I want the rest of it."''',
        c('"Then I had better offer you something worth the hour."', "personal"),
        c('"I would have used your recommendation. I would also have tried to write a better letter."', "personal")),
    n("personal", "Irabeth", '''"What do you want from me?"
{n}The question is direct. Irabeth settles her hands beside the papers.{/n}
"You know how to make yourself difficult to ignore. That is not quite the same thing as being good company. I would like to know which you intend to be."''',
        c('"Good company, if you let me try. I miss hearing what you think when nobody is asking for orders."', "company"),
        c('"Someone who can surprise you. You may enjoy finding the flaws in my plans."', "challenge"),
        c('"I wanted to hear whether there could still be a conversation between us. This is enough for today."', "leave")),
    n("company", "Irabeth", '''"I might be very poor company."
{n}You glance at the corrections on the page. Irabeth follows your look, and one corner of her mouth moves.{/n}
"Criticism is not my only accomplishment."
{n}She sits back. The papers remain between you, but she stops consulting them.{/n}
"I have been trying to read a book which contains no military advice. So far I have found three passages that would get someone killed if taken seriously. Anevia would tell me that is not how I am supposed to read it."
{n}Her expression changes slightly at the name. She leaves you no opening to turn it into a question about her wife.{/n}
"There is one very good description of a forest. I may finish it for that."''',
        c('"Tell me about the forest. I will save the tactical objections for afterward."', "end")),
    n("challenge", "Irabeth", '''"I already enjoy finding the flaws."
{n}The answer comes before she has quite decided how much of a smile to allow it.{/n}
"You would like to make a habit of being interesting, I think. A dangerous ambition in a person who can usually afford the consequences."
{n}She looks at the papers again, then at you.{/n}
"Let me see what you do when the clever answer is the wrong one. That will tell me more than another ingenious invitation."
{n}There is a challenge in her expression now, and something warmer which she has no intention of explaining for you.{/n}''',
        c('"Keep watching. I intend to give you more than one answer to judge."', "end")),
    n("leave", "Irabeth", '''"It is more than we had before the letter."
{n}Irabeth gathers her copies, leaving your corrected plan on the table.{/n}
"Use the advice. I would dislike finding that the account ceased to interest you as soon as I agreed to come."
{n}She waits for your answer, then inclines her head.{/n}
"Good day, Commander."''',
        c('[Thank her for the conversation.]', flags=("irabeth.return_private_hour_kept",))),
    n("end", "Narrator", '''{n}The hour runs out while Irabeth is still speaking. She notices the light at the window, checks the time, and stops herself in the middle of a sentence.{/n}
"I should go."
{n}She takes her papers. Yours remain covered in her precise corrections.{/n}
"Do not write to me yet," {n}she says.{/n} "If there is something more to say, I would like to be the one who decides when it is said."
{n}There is enough of a smile in it to make it worth remembering. She leaves without asking anyone to return her to a post.{/n}''',
        c('[Let her go. Leave the account to the quartermaster.]', flags=("irabeth.return_private_hour_kept",))),
], requires=("irabeth.return_reply",), delay=12, physical=True)
