"""A retained officer's authored correspondence decision with native report memories."""
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "ca2d58c5c65723945857e04fb85d30ce"
ANSWERS = "0dc8b8604bb33c846a63f3eb62443674"
SEEN_CUES = {
    "konomi.foreign_report_seen": ["9980a1ecf3ca24e42ab3b22f858677b5"],
    "konomi.domestic_report_seen": ["60585f7319a294147a54f440865b21a2"],
    "konomi.crisis_report_seen": ["07459f4d09fa81e4b99beea351fb0434"],
}
SCENES = []


def s(id, title, entry, nodes, after, delay):
    for node in nodes:
        node["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 5, entry, nodes,
        Relationship="konomi", Chapters=[5], Areas=[DREZEN], AnswerLists=[ANSWERS], ContactUnit=CONTACT,
        requires=("konomi.present", "konomi.political_account", *after),
        forbids=("konomi.dismissed", "konomi.closed", "konomi.farewell", "inhuman"),
        delay=delay, optional=True))


s("the_names_admitted", "The names admitted to the room", '"Did you receive the political reply you wanted to show me?"', [
    n("start", "Konomi", '''{n}Konomi has opened a letter beside a list of names. Some names have titles beside them; others have been struck through. She turns both pages toward you.{/n}
"Veyra keeps correspondence for a small circle in Nerosyan. They compare accounts supplied by people who have held public responsibilities. No authority to issue orders. Considerable influence over which account of an order becomes accepted."
{n}She rests a finger beside her own name.{/n}
"She has invited me to review their next collection. I asked what I could show you. These terms, the disputed admission and the examples in her reply. Nothing from the restricted papers."
"A difficult answer?"
"An attractive one. Those require rather more care."''',
      c('[Read the terms with her.]', "context"),
      c('[Return when you can give the reply your attention.]', abort=True)),
    n("context", "Konomi", '''"They want to compare who gave an instruction, who carried it out, and who later claimed the credit. A modest beginning. Several correspondents have already objected to the second column."
{n}Her smile lasts only a moment.{/n}
"You have heard why I care about that. What we can say about Mendev now must still depend on the account we actually have."''',
      c('[Recall her report of foreign garrisons taking over administration.]', "foreign", requires=("konomi.rank_eight_started", "konomi.foreign_help_playing", "konomi.foreign_report_seen")),
      c('"What can these letters establish?"', "unconfirmed", requires=("konomi.rank_eight_started", "konomi.foreign_help_playing"), forbids=("konomi.foreign_report_seen",)),
      c('[Recall her report of Mendev resolving the crisis without outside intervention.]', "domestic", requires=("konomi.rank_eight_started", "konomi.domestic_report_seen"), forbids=("konomi.foreign_help_playing",)),
      c('"What is the circle willing to show you?"', "unconfirmed", requires=("konomi.rank_eight_started",), forbids=("konomi.foreign_help_playing", "konomi.domestic_report_seen")),
      c('[Recall her account of failing services and divided authority.]', "crisis", requires=("konomi.rank_six_started", "konomi.crisis_report_seen"), forbids=("konomi.rank_eight_started",)),
      c('[Ask what this limited collection can establish.]', "unconfirmed", requires=("konomi.rank_six_started",), forbids=("konomi.rank_eight_started", "konomi.crisis_report_seen")),
      c('"What do you expect to learn from this collection?"', "unconfirmed", forbids=("konomi.rank_six_started", "konomi.rank_eight_started",))),
    n("foreign", "Konomi", '''"Order improved. Administration passed to foreign soldiers. I told you both, and I still want an account that preserves both. Otherwise gratitude becomes a remarkably convenient substitute for asking who can answer an instruction."
{n}She draws the list closer.{/n}
"This collection will not make a garrison leave. It can preserve the names of the people who knew the work before somebody else began commanding it. I want those names available when somebody claims that Mendev has nobody capable of taking it back."''', c('[Ask what the circle requires of her.]', "terms")),
    n("domestic", "Konomi", '''"The cities and the capital acted together again. I was glad to tell you so. I do not want every account written afterward to begin with the claim that this was inevitable."
{n}She touches one of the crossed-out names.{/n}
"Institutions survived because people did things, not because the correct names remained on the doors. I want the record kept by people who understand those institutions. That is also how I might keep their most comfortable explanations from going unchallenged."''', c('[Ask what the circle requires of her.]', "terms")),
    n("crisis", "Konomi", '''"When services fail, a person who can still obtain an answer matters more than a title. It does not follow that we should accept every account that arrives with a persuasive description of its author's usefulness."
{n}Her finger follows the list down to a name without a title.{/n}
"I would like reliable records while they can still be made. Not a victory announcement, and not another demand that somebody else solve the country before we decide which letter to believe."''', c('[Ask what the circle requires of her.]', "terms")),
    n("unconfirmed", "Konomi", '''"An account of the letters its members handled. Who sent them, who answered, and what the writers are willing to have examined. That is enough to begin without declaring the country saved or lost."
{n}She leaves the folded correspondence where you can see its extent.{/n}
"I have wanted better answers. Here are people willing to supply some, on terms I have not yet accepted. I would rather decide what those terms cost than improve the account beyond what they sent."''', c('[Read the proposed terms.]', "terms")),
    n("terms", "Konomi", '''"They admit people whose service can be confirmed through an office already represented. Members have agreed to share certain extracts with that group. Veyra has obtained their permission for me to read them if I accept."
"And the crossed-out names?"
"People without that confirmation. Marenne kept a district office's correspondence while its appointed secretary was absent. She can show the work. The secretary will not confirm her place in it. He says assistance does not constitute appointment."
{n}Konomi's expression is cool.{/n}
"He is correct about the appointment. I suspect he is less interested in accuracy than in being the only person who can explain his absence."
"Would you admit her?"
"I would like to hear her. I also want an institution capable of saying who may read a letter entrusted to it. I have no intention of treating access to private papers as a reward for being the most sympathetic person excluded."''', c('[Ask what arrangements she would accept.]', "choice")),
    n("choice", "Konomi", '''"I can accept the existing rules. Marenne may submit an account, but she will not see the restricted replies. I would have access and a place among people who can answer my questions without asking a second intermediary. I want that place."
{n}She turns the page.{/n}
"Or I can sponsor her for this one comparison. Veyra allows a member to take responsibility for an unconfirmed correspondent. We would work from a smaller set of extracts whose authors permit that arrangement. I would give up the broader reading and put my name beside hers when errors are corrected."
"A cost to your own access."
"And perhaps my reputation. She may remember something incorrectly. So may the secretary. The difference is that nobody asks me to guarantee his entire character before hearing him."
{n}She looks at you with open impatience, not all of it directed at the circle.{/n}
"Those are the two arrangements I can defend. I would prefer not to be told that wanting the larger reading makes the first indefensible."''',
      c('"Take the established place. Make them answer the record you can actually examine, including what Marenne submits."', "recognized"),
      c('"Sponsor her for the limited comparison. Giving her a chance to answer may be worth losing the broader reading."', "sponsor")),
    n("recognized", "Konomi", '''"Yes. I want to know what they say to one another when they believe the reader understands why the institution matters. I might learn more than I could by standing outside and objecting to the invitation."
{n}She writes her acceptance, then a separate request for Marenne's account. She specifies that the account may be considered without giving its author access to the other papers.{/n}
"She may refuse. I would dislike being asked to trust a discussion I could not hear. I am choosing it anyway."
{n}Konomi puts down the pen.{/n}
"Stay while I read this once more. Then I should like to walk with you somewhere that does not contain the word credentials."''',
      c('[Stay for the rereading, then leave together.]', flags=("konomi.political_recognized", "konomi.political_terms_sent"))),
    n("sponsor", "Konomi", '''"For the comparison, then. I shall not certify an appointment she did not hold, or promise that I agree with everything she remembers."
{n}She writes the offer carefully, including the reduced reading and her responsibility for answering corrections. Beside it she puts a request for Marenne's own agreement to those terms.{/n}
"The secretary will call this patronage. He will be right. He might find it harder to enjoy that observation if it occurred to him how he obtained his own audience."
{n}Her mouth curves, sharp and pleased.{/n}
"I rather like choosing whom they must hear with me. Stay while I make that sound less provocative. Not much less."''',
      c('[Stay until the answer is ready, then leave the work together.]', flags=("konomi.political_sponsored", "konomi.political_terms_sent"))),
], after=(), delay=24)

s("the_answer_on_record", "The answer she puts her name to", '"What did the circle send back?"', [
    n("start", "Konomi", '''{n}Konomi has set aside two sheets. The rest of the packet is secured inside her case.{/n}
"The answer, and the correction they have agreed I may show you. I have not brought you here to admire a successful request for more correspondence. We reached a result."
{n}She moves the empty chair nearer with her foot.{/n}
"One I wanted, though I have had to practice saying which part."''',
      c('[Ask what she found through the recognized circle.]', "recognized", requires=("konomi.political_recognized",)),
      c('[Ask what the sponsored comparison established.]', "sponsor", requires=("konomi.political_sponsored",)),
      c('[Arrange to hear the answer another day.]', abort=True)),
    n("recognized", "Konomi", '''"Marenne sent her account. She declined further questions unless they came in writing. Veyra found that unnecessarily suspicious. I found it quite intelligible."
{n}Konomi puts the first sheet before you.{/n}
"The secretary claimed to have authorized a disputed instruction before leaving. His own covering letter shows that he received it afterward. I could compare the dates because I had the broader reading. The circle has corrected its summary and sent the correction to everyone who received the first version."
"Does Marenne get to see it?"
"Her own contribution and the corrected conclusion. Not the private replies. She wrote that she would have preferred to answer them herself. I believe her. I have not obtained her gratitude."
{n}Konomi folds the sheet along its existing crease.{/n}
"I have obtained a correction people inside the circle will actually read. Veyra wants me to review another set. The secretary has stopped answering my personal letters. I shall manage without those."''', c('[Ask what she takes from the result.]', "role")),
    n("sponsor", "Konomi", '''"Marenne accepted. The narrower extracts showed that her first date was wrong. She had copied the day she received the instruction where the form asked when it was issued. I sent the correction under both our names."
{n}Konomi slides the second sheet toward you.{/n}
"It did not establish the secretary's account either. He could not supply the authorization he claimed to have given. The circle amended its summary: the chain of instruction remains unproven. Both versions attached. No invented certainty."
"And your place?"
"Limited to this comparison, as agreed. I was not invited into the broader reading. Marenne was allowed to answer the questions about her account herself. She disputed my wording twice. The second objection was good."
{n}Konomi looks pleased despite the lost invitation.{/n}
"Veyra says I have made the next sponsorship more troublesome. People will expect their answers to be included. I told her that was one of the purposes of asking a question. I enjoyed writing it."''', c('[Ask what she takes from the result.]', "role")),
    n("role", "Narrator", '''{n}She returns the shared pages to their wrapper. Nothing from the restricted packet has been left on your side of the table.{/n}''',
      c('"You said the Diplomatic Council had served its purpose. This is a different kind of influence."', "concluded", requires=("konomi.council_conclusion_seen",)),
      c('"You found work you wanted without waiting for another council instruction."', "ongoing", forbids=("konomi.council_conclusion_seen",))),
    n("concluded", "Konomi", '''"It is. I meant what I said about that council. I did not resign every interest I have in whose account is believed."
{n}She secures the packet in her case.{/n}
"My appointment still has its duties. This correspondence does not entitle me to issue a new order in its name. It gives me a place in an argument I wanted to enter. I am glad of the distinction. It means I can admit how much I wanted the place."''', c('[Let her close the case.]', "respect")),
    n("ongoing", "Konomi", '''"I did. The appointment gives me responsibilities. It need not provide every reason I have for writing a letter."
{n}She secures the packet in her case.{/n}
"I am not presenting this as a council decision. It is an account I helped correct and a circle of people who now know what it is like to receive my questions. Some of them will be less eager next time. I have survived worse introductions."''', c('[Let her close the case.]', "respect")),
    n("respect", "Konomi", '''"You heard what I wanted before you knew whether the answer would flatter me. I liked that."
{n}She moves her chair away from the desk and turns toward you.{/n}''',
      c('"You once acknowledged my political judgment. I liked being asked for it without being promised agreement."', "earned", requires=("konomi.political_respect_seen",)),
      c('"I liked being asked. I did not expect that to make your judgment mine."', "unearned", forbids=("konomi.political_respect_seen",))),
    n("earned", "Konomi", '''"I remember the acknowledgment. I have not misplaced it merely because I might dislike your next recommendation."
{n}She reaches for your hand.{/n}
"Nor have I mistaken this for another occasion to bestow it. I wanted your company while deciding something I cared about. You gave me an answer I could use, and stayed to hear what happened. That mattered in a rather less official way."''', c('[Stay near.]', "close")),
    n("unearned", "Konomi", '''"A sensible expectation. I shall endeavor not to disappoint it by becoming too easily persuaded."
{n}She reaches for your hand, smiling at the effort that would require.{/n}
"I wanted your company while deciding something I cared about. I also wanted to be able to show you an answer without first making myself appear blameless in it. That is more difficult than inviting somebody to agree with me."''', c('[Stay near.]', "close")),
    n("close", "Konomi", '''{n}She draws your hand into her lap and rests both of hers around it.{/n}
"Enough. The correction has been sent. The invitations have been accepted or lost. There is no remaining person you must impress before I can enjoy the rest of our evening."
{n}Her thumb moves slowly across your knuckles.{/n}
"I have been looking at you while explaining all this. You may have noticed that my attention was not entirely on the chronology."''',
      c('[Kiss her, and stay after the case is put away.]', "kiss"),
      c('[Keep her hand and ask for a quiet walk together.]', "walk")),
    n("kiss", "Narrator", '''{n}Konomi meets you halfway. Her other hand comes to the back of your neck, and the careful pause after the first kiss lasts only until you draw her closer.{/n}
{n}When she finally lets you move back, she is smiling without trying to make it look like a favorable assessment.{/n}
"Yes," she says, though you have asked no question.
{n}She puts the case beneath the desk, well away from the chair beside her. You remain with her while the light changes at the window.{/n}''', c('[Keep the rest of the visit for each other.]', flags=("konomi.political_reply_kept", "konomi.political_reply_kissed"))),
    n("walk", "Narrator", '''{n}She agrees at once, then spends a moment looking for the gloves she put inside her own case. You wait while she finds them. She gives you a look that discourages the most obvious remark and invites a better one.{/n}
{n}Outside, she takes your arm. You choose the first turning; she chooses the next. Neither has an appointment at the end of the street.{/n}
"There," she says. "We have found a use for two people who insist on choosing."
{n}You continue walking until one of you wants to turn back, and say so.{/n}''', c('[Enjoy the walk and return together.]', flags=("konomi.political_reply_kept",))),
], after=("konomi.political_terms_sent",), delay=168)


def integrate(payload):
    """Add observed report memories and optional closing recollections only."""
    bindings = payload.setdefault("SeenCues", {})
    for flag, value in SEEN_CUES.items():
        if flag in bindings and bindings[flag] != value:
            raise ValueError("Conflicting native Konomi report cue: " + flag)
        bindings[flag] = list(value)
    ordinary = next(s for s in payload["Scenes"] if s["Id"] == "konomi.ordinary")
    if any(n["Id"] == "work_remembered" for n in ordinary["Nodes"]):
        return
    start = ordinary["Nodes"][0]
    original = deepcopy(start["Choices"])
    start["Choices"].append(c('"Those papers have an afternoon of ours in them. I have been thinking about the trial and what you chose to write."',
        "work_remembered", requires=("konomi.ordinary_expanded", "konomi.trial_lived", "konomi.readers_answered")))
    ordinary["Nodes"].extend([
        n("work_remembered", "Konomi", '''"Then tell me which part stayed with you. I remember several things I would have preferred to discover more elegantly. I also remember being glad you were there."''',
          c('[Recall keeping the evening stopping time even with casks left to unload.]', "work_evening", requires=("konomi.evening_trial",)),
          c('[Recall the morning arrival, including the watch, charcoal and blocked entrance.]', "work_morning", requires=("konomi.morning_trial",)), portrait="Konomi"),
        n("work_evening", "Konomi", '''"Two casks, and Varine looking at me as though ten minutes had never hurt anyone. I had made the attractive proposal. I am glad you also saw the part where we stopped."
{n}She sets the papers farther from the plant.{/n}
"Oselda wrote down the cost. I resisted making the account more flattering. We both contributed."''',
          c('[Ask about the private reports they agreed to write together.]', "work_joint", requires=("konomi.joint_offer",)),
          c('[Ask about the circular they sent to readers of their own choosing.]', "work_circular", requires=("konomi.circular_offer",)), portrait="Konomi"),
        n("work_morning", "Konomi", '''"And the handcart. I remember what my glove looked like afterward. Oselda's arrangement worked, though neither of us had allowed for everything it would cost."
{n}She sets the papers farther from the plant.{/n}
"I wanted my proposal chosen. I am glad I was there to see hers work. I can still find both things true without needing another trial to reconcile them."''',
          c('[Ask about the private reports they agreed to write together.]', "work_joint", requires=("konomi.joint_offer",)),
          c('[Ask about the circular they sent to readers of their own choosing.]', "work_circular", requires=("konomi.circular_offer",)), portrait="Konomi"),
        n("work_joint", "Konomi", '''"Two reports, both names and a reduced fee. Their first question went to Oselda. I have not ceased wanting to be asked first, but it was useful to discover that being asked second did not prevent me from enjoying the work."
{n}She turns back toward you.{/n}
"Those are the papers. They can still wait. I have been looking forward to this evening."''', *deepcopy(original), portrait="Konomi"),
        n("work_circular", "Konomi", '''"Six copies, then answers we had not known to expect. I wanted a more impressive beginning. I liked the account we actually wrote enough to let it leave the room."
{n}She turns back toward you.{/n}
"Those are the papers. They can still wait. I have been looking forward to this evening."''', *deepcopy(original), portrait="Konomi"),
    ])
