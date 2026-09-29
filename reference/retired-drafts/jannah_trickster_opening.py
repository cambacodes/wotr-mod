"""A Trickster-only opening for a new, post-Sunhammer Jannah route."""
from story_format import c, n, scene


RELATIONSHIP = dict(
    Title="A second chance chosen",
    Description="Jannah's return to the Crusade is her choice. So is anything between her and the Commander.",
    Objective="Answer Jannah's invitation on terms she chooses",
    Guidance="Unregistered prototype. Requires the successful native Seelah soul-return quest and Jannah's return.",
    StartedFlag="jannah.trickster.started",
    ClosedFlag="jannah.trickster.closed",
    CommittedFlag="jannah.trickster.courtship",
    UnavailableFlags=["jannah.dead_known", "jannah.dead_unknown"],
    FailureFlags=[],
)

ETUDES = {
    "jannah.prison_history": "59632e1775b2f7240af0f6d0db28e35b",
    "jannah.condemned_history": "46f4524cec981c544964229e3e08c847",
    "jannah.dead_unknown": "f8129442feebb7c49b209c83b8ee6267",
    "jannah.dead_known": "699b1ad898227c943b2ee9e0cfd355aa",
    "jannah.free_history": "d99770b13ebc47447881d33763209b03",
}

COMPLETED_QUESTS = {
    "jannah.souls_returned": "5a5a533c9ce630a48b877f9a194840cb",
}

SEEN_CUES = {
    "jannah.joined_mission": ["651ecf0cde0e1a54dbc93761d1751b43"],
}

PATH_ENTRY_PLANS = {
    "angel": "Build from her Eagle Watch service and her independent choice to return after the native soul mission.",
    "aeon": "Use evidence and accountable judgment, while separating justice from punishment and romance.",
    "azata": "Use the successful mission and her choice to help people, without treating flight as a moral failing.",
    "trickster": "Offer an optional, bounded delivery trick after Jannah has already chosen to write; the ordinary courier remains available and her answer is unchanged.",
    "demon": "Requires a costly, observable restraint after the native campaign; she can reject the Commander without reprisal.",
    "devil": "Requires terms she can refuse outside the Commander's authority; parole and service cannot become leverage.",
    "gold_dragon": "Use protection and accountability without claiming that compassion erases her choices.",
    "legend": "Build a future after the war from her own service decision and verify that she remains alive and reachable.",
    "lich": "Requires a credible living future and her informed choice; a reanimated body cannot consent.",
    "swarm": "Unavailable unless a script-backed intervention proves Jannah survives as herself and can answer freely.",
}

BLOCKED = (
    "jannah.dead_known", "jannah.dead_unknown", "jannah.trickster.closed",
    "jannah.trickster.friendship", "jannah.trickster.courtship",
    "jannah.trickster.courtship_started", "jannah.trickster.met",
)


def add(id, title, nodes, previous=None, delay=24, forbids=BLOCKED):
    for page in nodes:
        page["Portrait"] = "JannahCorrespondence"
    SCENES.append(scene(
        "jannah.trickster." + id, title, "Jannah Aldori", 5,
        "Read Jannah's letter", nodes,
        requires=("trickster", "jannah.souls_returned", "jannah.joined_mission")
                 + ((previous,) if previous else ()),
        forbids=forbids, delay=delay, optional=True,
        Relationship="jannah.trickster", Remote=True, ManualOnly=True,
    ))


SCENES = []
add("the_misdelivered_hour", "The misdelivered hour", [
    n("start", "Jannah Aldori", '''{n}The after-action report is correctly addressed to Jannah's unit commander and remains sealed. A separate letter is addressed to you in Jannah's hand, its seal unbroken. The courier has placed the two envelopes together by mistake; you open only the one bearing your name.{/n}
Jannah writes that the battle is over and the stolen souls are home. She has not forgotten what she did before the Molten Scar, or the scar it left above her temple. She also has not forgotten that you gave her a choice after she came back and asked to serve again.
"I was going to ask whether the mission changes what you think of me. That is a ridiculous question. A mission can't decide that for you. So I'll ask the useful one instead: if you have an hour when you aren't issuing orders, would you spend it talking to me? You can say no. I won't mistake a no for another sentence."''',
      c("Write that the hour is hers to use or cancel. Do not mention her parole.", "plain", flags=("jannah.trickster.started",)),
      c("Tell her that a completed mission is not a debt paid, and invite her to choose a time.", "debt", flags=("jannah.trickster.started",)),
      c("Tell her she owes you a private meeting for returning to the Crusade.", "boundary", flags=("jannah.trickster.closed",))),
    n("plain", "Commander", '''You answer with a time and a place that leave her free to refuse. You do not mention her sentence, her service, or the mission. The choice to meet belongs to her, and so does the choice to walk away.''',
      c("Send the letter and wait for her answer.", "reply", flags=("jannah.trickster.invited",))),
    n("debt", "Commander", '''You write that the victory belongs to the people who returned the souls, and that none of it buys her time or affection. If she wants to meet, you would like to hear what she wants next, not what she thinks you want her to say.''',
      c("Send the invitation without setting a deadline.", "reply", flags=("jannah.trickster.invited",))),
    n("boundary", "Jannah Aldori", '''Jannah's answer arrives before the next dispatch. "No. I came back because I wanted to do something useful. I did not put myself on a private roster. If that is what you think I agreed to, we should stop here." The letter ends there. Her command and her parole remain untouched.''',
      c("Accept the refusal and close the correspondence.", flags=("jannah.trickster.closed",))),
    n("reply", "Commander", '''Jannah's sealed answer is logged for delivery tomorrow. The courier has not left yet. You can let the ordinary route carry it, or use a small Trickster fold to bring the same sealed letter to your desk now. Either way, you will not change its words, her decision, or the time she chose.''',
      c("Leave the letter to the ordinary courier.", "ordinary_reply"),
      c("[Trickster] Fold the route and bring her sealed answer here now.", "trickster_reply", flags=("jannah.trickster.delivery_trick_used",))),
    n("ordinary_reply", "Jannah Aldori", '''Her letter arrives the next day by the ordinary route. "I chose the old practice yard after my shift. If you are late, I will leave. If I decide I am done, I will leave then too. That is the whole invitation; don't turn it into an order."''',
      c("Read her invitation and decide whether to meet.", "decision"),
      c("Decline the meeting but leave future letters to her choice.", "decline_meeting")),
    n("trickster_reply", "Jannah Aldori", '''Her sealed answer appears on your desk before the courier has left the barracks. The fold changes only the route, not the letter or Jannah's choice. She has named the old practice yard after her shift. In the margin she adds: "I know a Trickster did this. The time is still mine to offer, and still yours to refuse."''',
      c("Read her invitation and decide whether to meet.", "decision"),
      c("Decline the meeting but leave future letters to her choice.", "decline_meeting")),
    n("decision", "Narrator", '''The invitation is hers, and the answer is yours. If you meet, it will be at the old practice yard after her shift, on terms she set. The strange delivery has changed nothing else.''',
      c("Accept the place and time she chose.", flags=("jannah.trickster.meeting_set",)),
      c("Decline the meeting but leave future letters to her choice.", "decline_meeting")),
    n("decline_meeting", "Commander", '''You write that the practice yard is hers. If she wants to write again, you will read the letter. If she does not, you will not ask the Trickster to send it back.''',
      c("Close the invitation and keep the correspondence friendly.", flags=("jannah.trickster.friendship",))),
], delay=24, forbids=BLOCKED + ("jannah.trickster.invited", "jannah.trickster.meeting_set"))

add("the_practice_yard", "The practice yard", [
    n("start", "Narrator", '''{n}The appointment is after her duty shift, at a practice yard where she can leave by the gate without asking anyone's permission. Jannah has unfastened her armor but kept her sword. The fresh scar on her temple is clean and pale. She catches you looking at it.{/n}
"The scar is staying. I could hide it, but I don't feel like pretending the fight never happened. That isn't an invitation to ask how I got it. You know the story well enough." She rests one hand on the sword hilt. "I wanted to see whether we can talk when there isn't a mission between us. I also wanted to know whether you look at me and see the woman who ran, or the one who came back. Maybe both. I haven't decided which answer I want."''',
      c("Ask what she wants you to see now, and accept that she may not know yet.", "now", flags=("jannah.trickster.met",)),
      c("Offer a short sparring bout, with no audience and no score kept.", "spar", flags=("jannah.trickster.met",)),
      c("Say that her return makes the old mistake irrelevant.", "erase", flags=("jannah.trickster.met",))),
    n("now", "Jannah Aldori", '''"That's better than asking me to choose a flattering version." Her expression loosens, but only a little. "I was afraid of dying. I left people in danger, and I have to own that. I also came back when I had every reason to stay away. Those can both be true. I don't need you to call me brave so I can stand here."''',
      c("Tell her you respect the decision she made to return, without making it a pardon.", "respect"),
      c("Ask what she would change if she could make that decision again.", "regret")),
    n("spar", "Narrator", '''Jannah accepts the bout, sets the rules, and makes you repeat them back. First clean touch wins. No mythic power, no audience, and no wound that needs tending after. She wants the test because she chose it, not because she owes you proof.''',
      c("[Athletics] Match her footwork and let the first opening pass.", check=dict(Skill="SkillAthletics", DC=24, Success="even", Failure="stumble", CommanderOnly=True)),
      c("[Mobility] Keep the distance she set and wait for her opening.", check=dict(Skill="SkillMobility", DC=24, Success="steady", Failure="stumble", CommanderOnly=True)),
      c("Stop the bout and ask whether she would rather talk.", "stop")),
    n("even", "Jannah Aldori", '''You meet the line of her blade without trying to turn a practice bout into a contest of rank. She calls the point a draw. "You can follow directions when they don't flatter you. That is rarer than it should be." The corner of her mouth lifts. "I wondered if you would be as careful with me when I wasn't asking for help."''',
      c("Say you find her attractive and ask if she wants to talk about that.", "attraction"),
      c("Leave the feeling unspoken and ask what she wants from the next meeting.", "next")),
    n("steady", "Jannah Aldori", '''You keep to the space she marked and wait. Jannah taps your shoulder with the flat of her blade, then steps back. "You gave me room to choose the finish. That was the point." Her gaze stays on yours a little longer than the bout requires. "I was curious whether you were that deliberate with everyone, or only when you wanted something."''',
      c("Say the interest is real, but she owes you no answer tonight.", "attraction"),
      c("Ask whether she wants another meeting, without naming it a date.", "next")),
    n("stumble", "Jannah Aldori", '''Your foot catches in the dust. Jannah stops at once and lowers her sword. She does not laugh. "Are you hurt?" When you say no, she nods and puts her blade away. "Then let's stop. I don't want a mistake in a spar to become a lesson you have to accept."''',
      c("Thank her and end the evening here.", "end_friendly"),
      c("Ask if she still wants to talk without the swords.", "talk")),
    n("stop", "Jannah Aldori", '''She lowers the point immediately. "Yes. Thank you for saying so." She sets her sword aside and chooses the bench nearest the gate. The offer to spar is over; she does not treat stopping as a failure.''',
      c("Sit beside her, leaving the space between you open.", "talk")),
    n("erase", "Jannah Aldori", '''"No. It still matters." Her voice hardens. "If I let the good ending erase the bad choice, I learn nothing from either. I came here because I wanted to talk to you. I won't do it if you need me to be a story about redemption."''',
      c("Apologize and let her end the evening.", "end_friendly"),
      c("Say you were trying to reassure her, then ask what you missed.", "now")),
    n("respect", "Jannah Aldori", '''"That is what I wanted to hear. Not forgiveness on demand. Just that the choice counts because I made it." She studies your face, then adds, more quietly, "And I am glad you were there when I came back. That's separate from the mission. I don't know what it means yet."''',
      c("Tell her you want another meeting if she does.", "next"),
      c("Tell her you are attracted to her, and that the answer is hers.", "attraction")),
    n("regret", "Jannah Aldori", '''She looks down at the practice-yard dust. "I would ask for help before I ran. That isn't the same as promising I would never be afraid again. I can't make that promise. If you're looking for a soldier who never breaks, you should find someone else."''',
      c("Say you want the woman who can name her limits, not a perfect soldier.", "attraction"),
      c("Agree that neither of you has to decide what this is tonight.", "next")),
    n("talk", "Jannah Aldori", '''You sit on the bench. Jannah keeps her sword where she can reach it and does not apologize for that. The conversation moves to the unit she served with after prison, the people she helped evacuate, and the way trust returned in small pieces. She does not claim her sentence was unfair. She does not pretend the sentence told her everything she could become.''',
      c("Ask about the work she chose after release.", "respect"),
      c("Ask whether she misses the road more than the army.", "next")),
    n("attraction", "Jannah Aldori", '''She listens without looking away. "I wondered if you would say it." Her thumb traces the worn leather at her sword hilt. "I like your nerve. I like that you can make an impossible thing happen and still tell me exactly where the trick ends. And, yes, I like the way you look at me when you aren't trying to turn my face into an answer." She takes one measured breath. "I am attracted to you. That doesn't settle what I want, and it doesn't give you the right to decide for me."''',
      c("Ask if she wants a kiss, and accept either answer.", "kiss_offer"),
      c("Say you would rather let the attraction grow at her pace.", "next"),
      c("Tell her you are glad she said it, then end the evening without asking for more.", "end_friendly")),
    n("kiss_offer", "Jannah Aldori", '''"I do." She closes the distance herself, pauses close enough for you to answer with your own movement, and kisses you once. It is brief, warm, and unmistakably chosen. She pulls back first. "One kiss. I want another meeting before I decide whether I want more than this."''',
      c("Tell her you want that next meeting too.", "next", flags=("jannah.trickster.courtship",)),
      c("Thank her and keep this as one good evening.", "end_friendly")),
    n("next", "Jannah Aldori", '''Jannah names a day when she is not on duty and makes you promise not to turn it into an appointment in her service record. "I want to see you again. I don't want a private chain of command, or a story where you save me and I owe you the rest of my life. If we do this, we do it because I keep choosing it."''',
      c("Agree, and ask what she wants the next evening to be.", "courtship", flags=("jannah.trickster.courtship",)),
      c("Leave the choice open and tell her you will wait for her to write.", "end_friendly")),
    n("courtship", "Narrator", '''She suggests dinner in a crowded inn and refuses to let you pay for her with crusade funds. You agree on the hour, then let her leave first. Neither of you calls it a promise beyond the next meeting.''',
      c("Wait for Jannah's next letter.", flags=("jannah.trickster.courtship_started",))),
    n("end_friendly", "Narrator", '''You thank her for the evening. She accepts the answer and asks that future meetings remain her choice. The friendship can continue if both of you want it. No service record, sentence, or Trickster coincidence will ask her again on your behalf.''',
      c("Close the meeting with a friendly goodbye.", flags=("jannah.trickster.friendship",))),
], previous="jannah.trickster.meeting_set", delay=48)

add("the_hour_after", "The hour after", [
    n("start", "Jannah Aldori", '''{n}Two mornings after the practice-yard meeting, Jannah writes that she reached the unit on time. She has already arranged her next off-duty hour herself.{/n}
"I keep thinking about our conversation. I don't want to turn the evening into a promise I didn't make. I also don't want to pretend I only came because I was curious. I want another evening with you, and I want it to be one where I can say what I want without wondering whether you'll hear an order in my voice."''',
      c("Tell her you want that too, and agree that rank stays outside the room.", "yes", flags=("jannah.trickster.second_evening",)),
      c("Thank her for being direct, but ask to keep the relationship at its current pace.", "slow", flags=("jannah.trickster.friendship",))),
    n("slow", "Jannah Aldori", '''"That's a good answer. I would rather have one honest evening than a month of guessing what you think I agreed to." She says she is glad you met and closes the door on romance for now. The friendship remains possible on ordinary terms.''',
      c("Keep the correspondence friendly and let her choose whether to write again.", flags=("jannah.trickster.friendship",))),
    n("yes", "Commander", '''You tell her that you want another evening too. You make one thing plain. Her duties and parole belong to the military chain of command; your attraction does not give you the right to use either as leverage. If either of you wants to stop, the evening ends without a report or penalty.''',
      c("Send the answer and let her name the place.", "place")),
    n("place", "Jannah Aldori", '''She chooses a small inn beyond the barracks, with a public room and a private table near the door. She confirms that she has leave, that no one expects her there, and that she can return to the unit without asking you. The plan is hers. The impossible part is the courier's timing: the invitation reaches you between two dispatches that were never meant to travel together.
"I know you made the route do that. I don't mind the joke. I mind being tricked into a meeting, and that isn't what happened. I had already asked. Next time, ask before the world starts helping."''',
      c("Promise the Trickster will wait for her word before bending the route again.", "terms"),
      c("Admit you thought the surprise would impress her, then apologize.", "apology")),
    n("terms", "Jannah Aldori", '''"Good. I can enjoy a trick when I know where it ends." She meets you at the inn after her shift. She wears a dark green dress under a short traveling cloak, with the temple scar uncovered. When she catches you looking, her smile is quick and a little crooked. "You can say you like the dress. You don't have to make a speech about the scar."''',
      c("Tell her she looks beautiful, then let her decide whether to take your hand.", "dinner"),
      c("Tell her the scar suits the way she carries herself now.", "dinner")),
    n("apology", "Jannah Aldori", '''She reads the apology twice. "I believe you meant to impress me. That isn't the same as it being all right." She accepts the apology because you named what you did and did not ask her to comfort you about it. The meeting stays on the agreed terms. She does not owe you a warmer reaction.''',
      c("Keep the magic out of the evening and meet her at the inn.", "dinner"),
      c("Offer to cancel, leaving the choice to her.", "cancel")),
    n("cancel", "Jannah Aldori", '''"Let's cancel tonight. I am not ending this forever. I am telling you what I want tonight." She thanks you for leaving the choice with her and returns to her unit. The next letter, if there is one, will come from her.''',
      c("Accept the answer and end this branch without penalty.", flags=("jannah.trickster.friendship",))),
    n("dinner", "Narrator", '''The two of you talk about the people she served beside, the soldiers who still distrust her, and the work of being trusted one ordinary day at a time. She tells you that the sentence did not teach her courage. The people in her unit did, by asking her to stand watch and then standing it with her.
When you ask what she wants from you, she sets down her glass. "I want to be wanted, not reassigned. I want to know what you are like when you don't need me for a battle, a rescue, or a good story. I want to find out whether this heat between us survives a quiet room." She lets the silence stay until you answer.''',
      c("Tell her what you want, then ask whether she wants to leave together.", "desire"),
      c("Tell her you want to keep dating and let tonight end here.", "slow_evening"),
      c("Ask what would make the room feel safe enough for her to stay.", "safe")),
    n("safe", "Jannah Aldori", '''"The door stays unlocked. My sword stays where I can reach it. And you ask before you touch me." She says it without embarrassment or apology. "That isn't me being afraid of you. It's how I want to be able to say yes." You agree, and she chooses to finish dinner before deciding anything else.''',
      c("Ask whether she wants to go somewhere private together.", "desire"),
      c("Say goodnight and wait for her next invitation.", "slow_evening")),
    n("desire", "Jannah Aldori", '''"I want to go with you." She takes your hand first. At the rented room, she closes the door but leaves the latch open, sets her sword on the chair she chose, and waits for you to meet her eyes before she kisses you.
The kiss deepens by degrees. Her fingers find your collar, then stop there until you nod. When your hand rises toward the scar at her temple, she catches your wrist gently. "Not yet." You stop and draw your hand back. "Would you like me to keep holding your hand, or should I stop?" She considers, then takes your hand and places it at her waist. "Here is good." She pulls you closer and lets her mouth answer before she does.
The rest belongs to the two of you. She asks for what she wants, changes her mind once, and asks again when she is ready. You listen. Later, with her cheek against your shoulder and the unlocked door still in view, she says the night was hers by choice. You tell her it was yours too.''',
      c("Ask if she wants to see you again when neither of you is on a clock.", "morning"),
      c("Let the night end here and leave future meetings to her.", "slow_evening")),
    n("slow_evening", "Jannah Aldori", '''Jannah walks with you back toward the barracks. At the gate, she kisses your cheek and tells you not to interpret it as a promise she has not made. The warmth between you is still there. So is her right to decide when it becomes anything more.''',
      c("Wish her good night and let her choose the next meeting.", flags=("jannah.trickster.courtship_started",))),
    n("morning", "Jannah Aldori", '''She turns her face toward you, close enough that the reply warms your mouth. "Yes. I want to see you again. And I want to be the one who asks sometimes." The morning does not erase her service, her sentence, or her choice to return. It adds one thing she chose after them.''',
      c("Agree to keep choosing each other without making promises for her.", flags=("jannah.trickster.courtship_started",))),
], previous="jannah.trickster.courtship_started", delay=48,
   forbids=("jannah.dead_known", "jannah.dead_unknown", "jannah.trickster.closed", "jannah.trickster.friendship"))

add("the_line_on_the_order", "The line on the order", [
    n("start", "Jannah Aldori", '''{n}Jannah asks to meet in the Defender's Heart, at a table where the door stays in view and anyone can join you. She has a folded duty schedule in front of her, marked with a request for an independent parole officer, a different reporting captain, and a separate field-order evaluator with a written complaint channel.{/n}
"I wrote it before I knew what you would say. I don't want my assignment to depend on whether you like me this week. I also don't want to pretend this is only an assignment now." Her eyes stay on yours. "If we keep seeing each other, the chain has to be clear to everyone, including us."''',
      c("Support the independent review she requested, without choosing its answer for her.", "support", flags=("jannah.trickster.separate_review",)),
      c("Ask what she wants the soldiers in her unit to know, and let her set the timing.", "privacy"),
      c("Offer to erase the request and keep her assignments under your direct control.", "pressure")),
    n("support", "Commander", '''You agree to send her request through the ordinary personnel office and to take no part in deciding her parole conditions or daily evaluations. You can confirm that the relationship exists if the process requires it, but you will not use your rank to keep her close or to punish her for leaving.''',
      c("[Knowledge: World] Draft a clean separation of reporting duties before the request goes forward.", "terms_ready", check=dict(Skill="SkillKnowledgeWorld", DC=24, Success="terms_ready", Failure="terms_rough", CommanderOnly=True)),
      c("Ask the personnel officer to propose the safeguards, then review them with Jannah.", "terms_rough")),
    n("terms_ready", "Jannah Aldori", '''You separate the parole review from combat assignment and put both under officers who do not report to you. Jannah reads each line and crosses out the clause that would have let a captain transfer her without asking. "That part stays mine. The rest is workable." She signs the request herself.''',
      c("Ask whether she wants to tell Seelah herself before the rumor reaches her.", "friend"),
      c("Leave the news private until she chooses otherwise.", "private", flags=("jannah.trickster.private_by_choice",))),
    n("terms_rough", "Jannah Aldori", '''The personnel officer returns a draft that separates her evaluations from your office but leaves the parole check-in with the same captain. Jannah spots it before you do. "The plan is decent. This line is not." She writes a correction in the margin and asks for it to be sent back. She does not ask you to fix it for her.''',
      c("Back the correction and return the form unsigned until it is accurate.", "friend"),
      c("Let Jannah decide when the form is ready, without asking her to report back to you.", "private", flags=("jannah.trickster.private_by_choice",))),
    n("privacy", "Jannah Aldori", '''"I want Seelah to hear it from me. Not because I need her permission. She was my friend before either of us knew you, and I don't want her to learn it from a barracks joke." Jannah folds the schedule. "The unit can know that my assignments are changing. They don't get the rest of my life because they share a watch with me."''',
      c("Agree, and offer to tell Seelah nothing unless Jannah asks.", "private", flags=("jannah.trickster.separate_review", "jannah.trickster.private_by_choice")),
      c("Ask if she would like you to be present when she tells Seelah.", "friend", flags=("jannah.trickster.separate_review",))),
    n("friend", "Jannah Aldori", '''She decides to speak to Seelah after the next duty rotation. You are invited to be there only if Jannah asks again that day. It is a small distinction, and she watches to see whether you understand it. When you do not turn the invitation into a standing claim, she reaches across the table and rests her fingers over yours.''',
      c("Ask whether she wants to keep holding hands here.", "hand", flags=("jannah.trickster.trust_earned",)),
      c("Let her choose how long her hand stays there.", "hand", flags=("jannah.trickster.trust_earned",))),
    n("private", "Jannah Aldori", '''She appreciates the discretion, then reminds you that privacy is not the same as secrecy you control. "I decide who hears it and when. If I want your help, I will ask." She sends the request to the Queen's designated parole authority and asks that Irabeth receive a copy as the advocate who supported her earlier appeal. The decision arrives in writing from the delegated officer a week later: a separate parole review, reporting captain, field-order evaluator, and complaint channel are approved. You had no signature on that decision. Jannah gives you a brief kiss before returning to her unit, then leaves first.''',
      c("Respect the privacy she chose and wait for her next invitation.", flags=("jannah.trickster.trust_earned", "jannah.trickster.independent_chain"))),
    n("hand", "Jannah Aldori", '''"For now, yes." Her thumb moves once across your knuckles. "I want this. I also want the work to stay fair when we disagree, and I want either of us to be able to leave without the other turning it into a campaign problem." You tell her the independent line will remain even if the romance ends. Her smile comes slowly, with more relief than triumph.''',
      c("Ask if she wants another evening together after the next rotation.", "next", flags=("jannah.trickster.trust_earned",)),
      c("Say nothing and let the quiet be enough for tonight.", "next", flags=("jannah.trickster.trust_earned",))),
    n("next", "Jannah Aldori", '''A week later, a letter from the Queen's delegated parole officer confirms the independent review, reporting captain, field-order evaluator, and complaint channel. Irabeth receives a copy as the advocate who supported Jannah's earlier appeal, but the decision belongs to the authorized parole office. You did not sign it or choose the result. Jannah then chooses the day and the place herself: a walk beyond the city wall, where neither of you will be mistaken for an officer inspecting a soldier. "Don't call it a reward for doing the right thing. I asked for this before we talked about the paperwork." She stands, kisses you once, and leaves for her shift with the written approval in her own hand.''',
      c("Agree to meet on her terms and keep the separate reporting line in place.", flags=("jannah.trickster.independent_chain",))),
    n("pressure", "Jannah Aldori", '''Her face closes. "No. The request is mine. You don't get to erase it because you want me nearby." She takes the schedule and stands. "If you need my work under your control to keep wanting me, then you don't want me. You want an order you can give." She will not stay for an apology made only to keep the evening alive.''',
      c("Accept that she is ending the romance and let her leave without interference.", flags=("jannah.trickster.closed",))),
], previous="jannah.trickster.courtship_started", delay=72,
   forbids=("jannah.dead_known", "jannah.dead_unknown", "jannah.trickster.closed", "jannah.trickster.friendship"))

add("the_question_in_the_yard", "The question in the yard", [
    n("start", "Jannah Aldori", '''{n}The next letter asks you to come to the practice yard as a guest, not an officer. Jannah has already finished a training rotation with a handful of new recruits. One of them has stayed behind, arms crossed, while the others pack their gear.{/n}
"He thinks the new reporting line means you pulled strings for me. I told him the request was mine and the review was independent. He wants to know whether he can challenge my decisions in the field without getting punished for embarrassing me." She looks toward the gate, then back at you. "I can answer. I want to know whether you'll let me."''',
      c("Stay quiet and give her the floor.", "her_answer"),
      c("Tell her she can answer, and speak only if she asks you to clarify the written procedure.", "clarify"),
      c("Use your rank to order the recruit to apologize to her.", "rank")),
    n("her_answer", "Jannah Aldori", '''She turns to the recruit. "Question the order if you have a reason and there is time to do it before anyone is in danger. Tell me what you think I missed. If you are right, I change the plan. If an immediate field order stands, you follow it and file your concern afterward through the evaluator. I won't punish you for using that channel." He asks whether she will remember who questioned her. "I will remember the question. I won't punish you for asking it." The recruit nods, not convinced, but no longer looking at you for the answer.''',
      c("Ask Jannah what she wants to do now that the yard is empty.", "quiet"),
      c("Tell her that you admire the way she made room for the question.", "admire")),
    n("clarify", "Commander", '''You wait until she looks to you. The written order names the independent evaluator and gives every soldier the same complaint channel. You explain only that process, then stop. The recruit reads the lines himself. Any immediate field order remains binding; he can question a plan before action when time permits or raise a concern afterward through the evaluator.''',
      c("[Diplomacy] Make the procedure clear without making a promise about the outcome.", check=dict(Skill="SkillDiplomacy", DC=25, Success="clear", Failure="blunt", CommanderOnly=True)),
      c("Let the paper speak for itself and leave the judgment to the evaluator.", "her_answer")),
    n("clear", "Jannah Aldori", '''Your explanation keeps the boundary between a complaint and insubordination intact. Jannah notices that you do not claim the evaluator will agree with her. "Good. I want to be judged by the work, not by who you are to me." The recruit asks his remaining question directly to her. She answers it herself.''',
      c("Wait until the others leave before asking for her answer.", "quiet"),
      c("Tell her she handled the challenge on her own terms.", "admire")),
    n("blunt", "Jannah Aldori", '''The words come out too much like an order. Jannah cuts in before the recruit can mistake your tone for a threat. "The evaluator decides the complaint. The Commander just explained the channel." She sends him to put the question in writing and thanks you for stopping there. Her expression says she noticed the difference.''',
      c("Ask what she wants from you before you speak again.", "quiet"),
      c("Acknowledge that you nearly made the room about your rank.", "admire")),
    n("quiet", "Jannah Aldori", '''Once the others are gone, she rests her sword against the practice rack. "I used to think a command sounded strong only if nobody questioned it. I don't believe that anymore. Some days I still miss the certainty." She asks if you can want her and still let her be difficult, especially when she is wrong.''',
      c("Say that wanting her does not make disagreement a betrayal.", "desire"),
      c("Admit that you are still learning how not to turn worry into control.", "honest"),
      c("Tell her a soldier who questions her cannot be trusted.", "distrust")),
    n("admire", "Jannah Aldori", '''"I did not do it for you to admire me." She watches your face, then lets out a quiet breath. "But I am glad you waited. It felt good to answer without you deciding what the answer should prove." She asks whether you can want her and still let her be difficult, especially when she is wrong.''',
      c("Say that wanting her does not make disagreement a betrayal.", "desire"),
      c("Admit that you are still learning how not to turn worry into control.", "honest"),
      c("Tell her a soldier who questions her cannot be trusted.", "distrust")),
    n("honest", "Jannah Aldori", '''She appreciates the honesty without rewarding it as if it were a confession that fixes everything. "Then keep practicing. I can be patient with someone who listens. I won't be patient with someone who keeps testing whether my no means try again." The last light catches the pale line of her scar. She offers her hand, palm up, and waits.''',
      c("Take her hand only after she offers it, then ask if she wants to kiss.", "kiss"),
      c("Leave her hand where it is and ask for another walk instead.", "walk")),
    n("desire", "Jannah Aldori", '''"Good. Then don't take disagreement away from me just because the feeling is inconvenient." She offers her hand, palm up, and waits. The pause is long enough to be a choice. "You can take it. I want you to."''',
      c("Take her hand and ask if she wants to kiss.", "kiss"),
      c("Take her hand, but leave the kiss for another evening.", "walk")),
    n("kiss", "Jannah Aldori", '''"I do." She draws you in and kisses you with the edge of a smile, her fingers firm around yours. There is heat in it now, but no hurry to turn the empty yard into a room. When she breaks away, she keeps your hand. "I want this because I can disagree with you and still choose you. I need both things to stay true."''',
      c("Tell her the reporting line stays independent even if you argue tomorrow.", "continue", flags=("jannah.trickster.independent_chain",)),
      c("Ask whether she would rather stop here and leave the rest for later.", "continue", flags=("jannah.trickster.independent_chain",))),
    n("walk", "Jannah Aldori", '''She accepts the slower evening and chooses the path along the outer wall. At the gate she kisses you once, then asks you not to turn a kiss into a vote on whether her boundaries have changed. You say you understand. She says she will tell you if they do.''',
      c("Let her choose when the next meeting happens.", "continue", flags=("jannah.trickster.independent_chain",))),
    n("continue", "Narrator", '''The training yard closes. The written request stays in the independent review, and Jannah's answer to the recruit remains hers. Neither result depends on the two of you kissing. She sends a note after her next shift with a day for another walk and a warning that she plans to beat you at cards this time.''',
      c("Answer that you will bring a deck and let her choose the stakes.", flags=("jannah.trickster.yard_trust",))),
    n("rank", "Jannah Aldori", '''She turns on you before the recruit can move. "No. He can challenge an order through the process we just wrote down. You don't get to make him apologize for doubting me." Her voice stays level, but the warmth is gone. She asks him to leave, then tells you she will not let rank speak for her in her own yard.''',
      c("Accept the correction and end the evening without asking her to soothe you.", "rank_accept"),
      c("Order her to let you handle it.", "rank_double")),
    n("rank_accept", "Jannah Aldori", '''"Thank you for stopping." She does not take your hand. "I am going to finish the review with the evaluator and then decide whether I want another meeting. You do not get an answer tonight." She leaves by the gate. The route pauses until she chooses to write again.''',
      c("Wait without sending a second invitation.", flags=("jannah.trickster.waiting_for_her",))),
    n("rank_double", "Jannah Aldori", '''She takes the signed request from the rack. "Then we are done. I will not be your soldier and your lover on the same order." She returns to her unit through the gate and files the request without your office's help.''',
      c("Let her leave and close the romance.", flags=("jannah.trickster.closed",))),
    n("distrust", "Jannah Aldori", '''Her hand drops to her side. "Then you want obedience, not me." She will not stay to make the answer gentler. The training continues without your presence, and the independent evaluator receives the report. Jannah does not ask you to come back.''',
      c("Accept the end of the romance and leave without using your authority.", flags=("jannah.trickster.closed",))),
], previous="jannah.trickster.independent_chain", delay=72,
   forbids=("jannah.dead_known", "jannah.dead_unknown", "jannah.trickster.closed", "jannah.trickster.friendship"))


def validate_graph():
    """Check that every authored choice target names a node in its scene."""
    for authored_scene in SCENES:
        nodes = authored_scene["Nodes"]
        ids = {node["Id"] for node in nodes}
        assert len(ids) == len(nodes)
        by_id = {node["Id"]: node for node in nodes}
        for node in nodes:
            for choice in node["Choices"]:
                target = choice.get("Next")
                assert target is None or target in ids, (authored_scene["Id"], node["Id"], target)
                check = choice.get("Check")
                if check:
                    assert check["Success"] in ids and check["Failure"] in ids
        reached = set()
        pending = ["start"]
        while pending:
            current = pending.pop()
            if current in reached:
                continue
            reached.add(current)
            for choice in by_id[current]["Choices"]:
                target = choice.get("Next")
                check = choice.get("Check")
                if target is not None:
                    pending.append(target)
                if check:
                    pending.extend((check["Success"], check["Failure"]))
        assert reached == ids, (authored_scene["Id"], ids - reached)

    def written_flags(authored_scene):
        return {
            flag
            for node in authored_scene["Nodes"]
            for choice in node["Choices"]
            for flag in choice.get("Set", ())
        }

    assert "jannah.trickster.meeting_set" in written_flags(SCENES[0])
    assert "jannah.trickster.meeting_set" in SCENES[1]["Requires"]
    assert "jannah.trickster.courtship_started" in written_flags(SCENES[1])
    assert "jannah.trickster.courtship_started" in SCENES[2]["Requires"]
    assert "jannah.trickster.independent_chain" in written_flags(SCENES[3])
    assert "jannah.trickster.trust_earned" in written_flags(SCENES[3])
    assert "jannah.trickster.yard_trust" in written_flags(SCENES[4])
    for authored_scene in SCENES:
        assert {"jannah.dead_known", "jannah.dead_unknown"}.issubset(authored_scene["Forbids"])
        assert not (set(authored_scene["Requires"]) & set(authored_scene["Forbids"]))

    def eligible(authored_scene, flags):
        return set(authored_scene["Requires"]).issubset(flags) and not (
            set(authored_scene["Forbids"]) & flags
        )

    native_entry = {"trickster", "jannah.souls_returned", "jannah.joined_mission"}
    assert eligible(SCENES[0], native_entry)
    assert not eligible(SCENES[0], native_entry - {"trickster"})
    assert not eligible(SCENES[0], native_entry | {"jannah.trickster.invited"})
    assert eligible(SCENES[1], native_entry | {"jannah.trickster.meeting_set"})
    assert not eligible(SCENES[1], native_entry | {"jannah.trickster.meeting_set", "jannah.trickster.met"})
    assert eligible(SCENES[2], native_entry | {"jannah.trickster.courtship_started"})
    assert not eligible(SCENES[2], native_entry | {"jannah.trickster.courtship_started", "jannah.trickster.friendship"})
    assert eligible(SCENES[3], native_entry | {"jannah.trickster.courtship_started"})
    assert not eligible(SCENES[3], native_entry | {"jannah.trickster.courtship_started", "jannah.trickster.friendship"})
    assert not eligible(SCENES[4], native_entry | {"jannah.trickster.trust_earned", "jannah.trickster.closed"})
    assert eligible(SCENES[4], native_entry | {"jannah.trickster.independent_chain"})
    assert not eligible(SCENES[4], native_entry | {"jannah.trickster.trust_earned"})


if __name__ == "__main__":
    validate_graph()
