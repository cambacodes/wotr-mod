from copy import deepcopy
from story_format import c, n, scene

"""Terendelev continuation manuscript draft.

This authored continuation requires an accepted RanRomance romance terminal.
The live-person continuation and Trickster scale-prison escape are separate branches.
No scene grants arrival, restores a body, or changes native quest state.
"""

DREZEN = "2570015799edf594daf2f076f2f975d8"
TERENDELEV_CONTACT = "9e8401e7703907e4d94189d5992dd13e"
PARENT_ROMANCE = "terendelev.parent_romance"
PARENT_BOUND = "terendelev.parent_bound"
PARENT_LICH_BIND = "terendelev.parent_lich_bind"
PARENT_RAVENER = "terendelev.parent_ravener"
PARENT_QUEST = "terendelev.parent_quest"
PARENT_BOUND_FRIENDSHIP = "0e09ddffd8fb40e7b1a0b147906b57cd"
PARENT_BOUND_REJECTION = "f0233d7ac79b4557b0f8f5f18a077940"
PARENT_BOUND_SEPARATION = "1a10b8880b054837b2bb2802d11020b7"
ETUDES = {
    "terendelev.parent_romance": "00a4899cba2c46038f9309d12525262b",
    "terendelev.parent_bound": "e9e0e0efcdf74f6480915983a4a19704",
    "terendelev.parent_ravener": "274d1b1f473344b3a741614bd1910514",
    "terendelev.parent_lich_bind": "bbe7d7dbb92a4923a1ca4433e626a5ec",
    "native.terendelev.ravener_dead": "42e220d5dadc4dfd8bb3ef23cae832eb",
}
COMPLETED_QUESTS = {PARENT_QUEST: "a1d66e27b73d4d819d138868d681280b"}
SEEN_CUES = {
    "terendelev.continuation.returned_finale_seen": ["8bf0fdc74bae4ef79dcfe04036e813ab", "4791f49d19624dafa2ea1ae6dd18c588", "30b3341acced4fa793dcc92dfe3587a9", "10fe0c7bd80d441c8688c37babc19f66"],
    "terendelev.continuation.bound_finale_seen": ["0e09ddffd8fb40e7b1a0b147906b57cd", "f0233d7ac79b4557b0f8f5f18a077940", "2ef521fa2e8d468db335980dc2166174", "1a10b8880b054837b2bb2802d11020b7", "48a730e870d94c73bc61afecaf1c8540"],
    "terendelev.continuation.bound_nonromance_seen": ["0e09ddffd8fb40e7b1a0b147906b57cd", "f0233d7ac79b4557b0f8f5f18a077940", "1a10b8880b054837b2bb2802d11020b7"],
    "terendelev.continuation.bound_friendship_seen": ["0e09ddffd8fb40e7b1a0b147906b57cd"],
    "terendelev.continuation.bound_separation_seen": ["1a10b8880b054837b2bb2802d11020b7"],
    "terendelev.continuation.bound_rejection_seen": ["f0233d7ac79b4557b0f8f5f18a077940"],
}
SCENES = []

RELATIONSHIP = dict(
    Title="A promise under an open sky",
    Description="Terendelev has asked what the Commander will do with a promise that survived her death.",
    Objective="Answer Terendelev's invitation",
    Guidance="The returned-person branch requires a confirmed delivered living actor and the returned terminal history. The scale-confined branch requires a verified scale-channel history. A no-parent Trickster contact is a future authored route design only; it remains unavailable until its native evidence reader, one-way invitation producer, voluntary response handler, registration, and tests exist.",
    StartedFlag="terendelev.continuation.started",
    ClosedFlag="terendelev.continuation.closed",
    CommittedFlag="terendelev.continuation.complete",
    UnavailableFlags=["terendelev.continuation.dead", "inhuman"],
    FailureFlags=[])


def f(*names):
    return tuple("terendelev.continuation." + name for name in names)


def add(id, title, owner, nodes, requires, forbids=(), delay=12, remote=False, **extra):
    for page in nodes:
        page["Portrait"] = "Terendelev"
    if "Remote" in extra:
        raise TypeError("Use lowercase remote= when defining continuation contact mode")
    contact_requirements = tuple(requires)
    if not remote:
        contact_requirements += (RETURNED_ACTOR_CONFIRMED,)
    SCENES.append(scene("terendelev.continuation." + id, title, owner, 5, title, nodes,
        requires=contact_requirements, forbids=tuple(forbids) + ("terendelev.continuation.closed",),
        delay=delay, optional=True, Relationship="terendelev", Remote=remote,
        ContactUnit=None if remote else TERENDELEV_CONTACT,
        Areas=[DREZEN], Chapters=[5], **extra))


RETURNED = f("returned")
BOUND = f("bound")

# Contracts for future runtime producers, not flags set by this manuscript.
NATIVE_CONTACT_CONTRACT = {
    "eligibility": ["chapter_5", "trickster", "native_quest_verified", "native_original_clue_verified", "native_ravener_outcome_verified"],
    "states": ["unavailable", "prepared", "sent", "answered", "declined", "expired"],
    "mechanism": "A one-use Trickster memory-signal is assembled with the Storyteller at the preserved cave site, at the cost of surrendering the native claw if it is still possessed, or a permanent one-time Storyteller favor if the claw is absent. It carries one message: Terendelev may answer, refuse, or remain silent. The claw is never consumed as a soul vessel, and the Storyteller does not claim to know whether a soul can answer.",
    "answer_authority": "Only the registered response handler may set native_contact_answered after an explicit in-world affirmative reply. Silence, refusal, expiry, missing evidence, and conflicting histories never set it.",
    "status": "design only; no producer, scene registration, cost action, or runtime test exists",
}
NATIVE_CONTACT_ANSWERED = "terendelev.continuation.native_contact_answered"
BOUNDARY_RESULT_CONTRACT = {
    "producer": "A registered observer compares the actual replica state before and after the dated-fact test and writes exactly one persistent result.",
    "results": ["terendelev.continuation.boundary.result.changed", "terendelev.continuation.boundary.result.unchanged", "terendelev.continuation.boundary.result.unsafe"],
    "invariant": "Mutually exclusive, save-safe outcomes; changed never authorizes crossing, unchanged records a null result, unsafe closes further tests and contact escalation.",
    "status": "design only; no observer, writer, or runtime test exists",
}
PATH_AVAILABILITY_CONTRACT = {
    "paths": ["Angel", "Aeon", "Azata", "Trickster", "Lich", "Demon", "Devil", "Gold Dragon", "Swarm", "Legend"],
    "goal": "Each route family must have an attainable, character-consistent authored resolution on every mythic path, including difficult or costly outcomes where appropriate.",
    "current_status": "none of the ten path-specific no-parent contact or bound-escape adapters is registered or tested",
    "rule": "Mythic path changes the intervention and consequences, not Terendelev's consent; no path may bypass voluntary contact, native encounter outcomes, or confirmed delivery.",
}
NATIVE_RAVENER_ALIVE = "terendelev.continuation.native_ravener_alive_verified"
NATIVE_RAVENER_DEAD = "terendelev.continuation.native_ravener_dead_verified"
RETURNED_ACTOR_CONFIRMED = "terendelev.continuation.returned_actor_confirmed"
RETURNED_ACTOR_CONTRACT = {
    "proof": ["returned terminal cue history", "compatible parent/native identity history", "exact intended actor delivered", "actor alive, usable, and present in the expected destination"],
    "producer": "Only the registered delivery service may set returned_actor_confirmed after the exact entity and scene-state postconditions pass; dialogue must not set it.",
    "status": "design gate only; actor blueprint registration, delivery caller, live confirmation, and tests remain absent",
}

add("returned_letter", "An invitation without an audience", "Memory", [
    n("start", "Narrator", '''{n}The letter is delivered without a seal. Its paper smells faintly of cold air and woodsmoke, and the handwriting is patient enough to make each line look as though it had been considered twice.

"I have been told that the Commander is difficult to surprise. This is not a challenge. It is a request that you come to the lower garden after the evening bell, without an escort and without bringing an answer prepared for me.

"I would like to walk somewhere the walls do not pretend to be a mountain. I would like to decide whether we have anything to say to one another when no one is asking me to remember who I was.

"If you would rather not, burn this. If you come, I will be there because I chose to be. Do not make that sound smaller by calling it fate."{/n}

{n}The paper carries a silver trace at its edge, like the shadow of a scale. You recognize the careful hand from the last time she asked for a private evening. Whatever brought her back, this request is new.{/n}''',
      c('[Go to the garden at the appointed hour.]', "garden", flags=f("started", "returned", "invitation.accepted")),
      c('[Keep the letter, but do not accept tonight.]', "later", flags=f("started", "returned", "invitation.deferred")),
      c('[Decline the invitation and leave the existing ending intact.]', "decline", flags=f("closed"))),
    n("garden", "Terendelev", '''"You came without an escort. I had expected you might."

{n}Terendelev stands beneath the bare branches, wearing a human shape that fits the garden without making her seem smaller. Her hair is gathered back from her face. The old cut of her clothes remains recognizable; the new silver clasp at her throat is the only ornament she has chosen for tonight.{/n}

"I asked for no prepared answer. That does not mean I want silence. It means I would like to hear what you think before you decide what I should think."

"I thought you wanted to walk."

"I do. I also wanted to know whether you would treat a quiet request as an order to prove yourself." Her mouth bends, almost a smile. "You have managed to disappoint me in both directions before."

{n}She offers her arm without ceremony. When you take it, her fingers settle over your sleeve rather than closing around your wrist.{/n}

"The oath we made still matters to me. It is not a chain that obliges me to feel the same every hour. I wanted to say that before either of us mistook memory for permission."

"And tonight?"

"Tonight I wanted your company. I wanted to see whether being returned to a living body had made you any less insufferable. The early evidence is mixed."{/n}''',
      c('"Then let us walk until one of us improves the evidence."', "walk", flags=f("walk.accepted")),
      c('"I will not ask your body to settle a question you have not answered."', "walk", flags=f("walk.accepted")),
      c('"You owe me no private evening because I helped bring you back."', "walk", flags=f("walk.accepted"))),
    n("walk", "Terendelev", '''{n}The garden path turns around a dry fountain. Terendelev chooses the longer side without explaining why. Her arm remains in yours, light enough that she could withdraw it without resistance.{/n}

"I remember the end of the ritual," she says. "I remember the stars. I remember choosing to meet you there. That memory is mine. But I do not want you to spend the rest of our lives presenting it whenever you wish to make me agree with something."

"I would rather hear what you choose now."

"Good. I dislike being made into an argument."

{n}At the fountain, she releases your arm and turns to face you. The distance is deliberate, but not cold.{/n}

"There are people in Kenabres who have begun using my return in speeches. Some say I chose their plans. Others say the dragon who died would have blessed them. I have not yet decided what I owe them, if anything."

"You want help?"

"I want a second pair of eyes and a person who can tell a crowd that I am not a relic they have reclaimed. I may ask for more later. I will not promise that asking makes you right." Her gaze holds on yours. "Would you come with me to hear them?"{/n}''',
      c('"I will come as your partner, not your spokesman."', "invitation", flags=f("civic.accepted")),
      c('"Only if you choose the place and the terms."', "invitation", flags=f("civic.accepted")),
      c('"I can come as your commander, but I will not put your name on my orders."', "invitation", flags=f("civic.accepted"))),
    n("invitation", "Terendelev", '''"Those terms are acceptable. I will choose the place."

{n}She takes your hand, turning it palm upward as if checking for an old injury. Her thumb traces the line below your fingers. The touch is warm, careful, and unmistakably chosen.{/n}

"You look very serious when you are trying not to be pleased," she says.

"I thought restraint was what you wanted."

"Restraint is not the same as pretending not to want anything. I wanted you to understand that I can stop. I would also like you to understand that I can begin."

{n}Her hand closes around yours. She leans in, leaving the last space for you to cross or keep.{/n}

"Would you like to kiss me?"{/n}''',
      c('[Kiss her, and let her set the pace.]', "kiss", flags=f("kiss.chosen")),
      c('[Tell her you want to, then wait for her to close the distance.]', "kiss", flags=f("kiss.chosen")),
      c('[Decline the kiss without ending the relationship.]', "deferred", flags=f("intimacy.deferred"))),
    n("kiss", "Terendelev", '''{n}The kiss begins slowly. Terendelev watches your face before she gives it more weight, then makes a small sound against your mouth when you answer her with the same certainty. One hand rests at your shoulder; the other finds the back of your neck, its touch warmer than the cold air.{/n}

{n}When she draws away, she does not apologize for wanting it. She rests her brow against yours for a moment, breathing evenly.{/n}

"That was a better use of the evening than another speech about my return."

"I had a speech prepared."

"Burn it."

{n}You both laugh. Her fingers remain at your collar, testing the clasp there. She asks before she loosens it, and the question earns her a look that makes her laugh again.{/n}

"Not tonight," she says, still close. "I want the first thing we do together after this to be something neither of us has to explain afterward. Walk me to the gate. Tomorrow, we can decide what to say to Kenabres."

{n}She takes your hand for the way back. The invitation has not made her yours, and the kiss has not made her a symbol. They are two choices she has made this evening, both still hers.{/n}''', c('[Walk her to the gate, and agree to hear the Kenabres petition together.]', flags=f("returned.chapter1", "romance.confirmed"))),
    n("later", "Narrator", '''{n}You fold the letter and set it aside. No appointment is made, and no answer is sent in your name. The lower garden remains quiet after the evening bell.{/n}

{n}The silver mark at the edge of the paper catches the light when you pass it. You leave it where it is. A living person's invitation can wait for an answer; it does not become a debt while it waits.{/n}''', c('[Leave the invitation open.]', abort=True)),
    n("deferred", "Terendelev", '''"Thank you," Terendelev says. "I wanted to ask. I did not want the answer to become a test."

{n}She keeps your hand in hers, but lets the evening remain quiet. The petition can wait until tomorrow, and so can the kiss.{/n}''', c('[Walk her to the gate and agree to hear the petition together.]', flags=f("returned.chapter1", "romance.confirmed"))),
    n("decline", "Narrator", '''{n}You return no answer. Terendelev has not made the invitation a test, and you will not turn a silence into a new injury by pretending it was one.{/n}

{n}The letter goes into the fire. The existing RanRomance ending remains the last word between you for now.{/n}''', c('[Close this continuation.]', flags=f("closed"), abort=True)),
], requires=("terendelev.parent_romance", PARENT_QUEST, "terendelev.continuation.returned_finale_seen", RETURNED_ACTOR_CONFIRMED), forbids=("terendelev.parent_bound", "terendelev.parent_lich_bind", "terendelev.continuation.romance.refused"))

add("kenabres_petition", "A name used as a seal", "Terendelev", [
    n("start", "Terendelev", '''"The meeting is in a storehouse by the eastern wall," Terendelev says. "It belongs to a group of builders preparing a list of houses to clear before winter. They have used my name in their petition to the queen."

{n}She sets three documents on the table. The first is a public copy, polished and persuasive. The second is an inventory of households marked for removal. The third is a rough list of volunteers promised work after the clearances.{/n}

"I did not approve this. I did tell the organizers I would hear their proposal. That is not the same thing, but the petition has been written as if it were."

"What do you want from the meeting?"

"A chance to hear why they believe this is necessary. I want the families to know that my name is not an order. I want you to help me keep the disagreement about their plan, rather than about whether a dragon has the right to change her mind."{/n}''',
      c('[Compare the household list with the building assessments.]', "compare", check=dict(Skill="SkillKnowledgeWorld", DC=25, CommanderOnly=True, Success="compare", Failure="gap")),
      c('[Ask which households have already received notice.]', "notices"),
      c('[Ask Terendelev what she believes is at risk.]', "terms")),
    n("compare", "Narrator", '''{n}You compare the list of households against the building assessments. Three entries describe occupied homes as empty. One has a repair estimate copied from a neighboring property, and two addresses have been reversed. The pattern is not random enough to be a simple copying error.{/n}

{n}Terendelev reads the discrepancies without triumph. Her expression tightens when she reaches the name of a family whose roof she remembers seeing from the air. She does not mistake your discovery for proof of a conspiracy; she marks the entries to verify them with the residents.{/n}

"A useful question," she says. "Now we need to ask who benefits from the answer before we decide what it means."{/n}''', c('[Bring the discrepancies to the meeting and ask for the original records.]', "meeting", flags=f("evidence.records"))),
    n("gap", "Narrator", '''{n}The addresses do not align cleanly. One household has moved since the census, and the repair notes use a numbering system that has changed twice. You cannot call the entries false without inventing certainty.{/n}

{n}Terendelev does not punish you for the miss. She asks you to mark what is unknown, not what you would like the paper to say. A clerk who helped deliver notices has agreed to attend the meeting and explain how the lists were made.{/n}''', c('[Hear the clerk before drawing a conclusion.]', "meeting", flags=f("evidence.clerk"))),
    n("notices", "Terendelev", '''"Some have received notices. They were told an inspection would follow, not that they had to leave. Others heard the rumor in the market and have already begun packing."

{n}Terendelev folds the paper with care, keeping the names inside. She has memorized the street and household numbers, but does not recite them aloud.{/n}

"There is a difference between an official order and a threat delivered in the shape of one. We must not make that difference meaningless by treating every frightened person as if they should have read the law first."{/n}''', c('[Ask who wrote the notices and who delivered them.]', "meeting", flags=f("evidence.delivery"))),
    n("terms", "Terendelev", '''"The plan may be right about the danger and still wrong about who must bear it," she says. "The wall is unstable. The winter is near. A failed roof can kill a family as easily as a demon can. But I will not tell a mother that her home is expendable because the alternative is inconvenient to a committee."

{n}She looks at you directly.{/n}

"I want you to challenge me if I begin treating a remembered street as though it were unchanged. You were there during the attack. Your memory is not mine, and mine is not a map of every life that has continued without me."{/n}''', c('[Go to the meeting and listen before either of you argues.]', "meeting", flags=f("evidence.context"))),
    n("meeting", "Narrator", '''{n}The storehouse is crowded with people who came to dispute different things. Builders sit beside residents whose homes have been marked. A clerk guards a locked case of original assessments. At the far end, an organizer named Venn has arranged the chairs so that the petition's supporters face the door.{/n}

{n}Terendelev does not sit at the head of the room. She waits until the residents have found places and then stands beside you, not behind a lectern.{/n}

"I was told my name would persuade you to accept this plan," she says. "It cannot. I have not approved it. I am here to hear what danger you see and to learn what evidence you used."

{n}A resident interrupts Venn: her roof was listed as collapsed when she has been sleeping beneath it for three years. The room turns toward the two of you.{/n}''',
      c('[Let the resident explain before questioning Venn.]', "resident", flags=f("meeting.resident_first")),
      c('[Ask Venn to produce the original assessments now.]', "records", requires=f("evidence.records")),
      c('[Ask the clerk how notices became eviction rumors.]', "clerk", requires=f("evidence.clerk")),
      c('[Ask Terendelev to open with the limits of her own authority.]', "opening", flags=f("meeting.limits"))),
    n("resident", "Narrator", '''{n}The woman gives her name as Asla. She describes the roof, the repair she made with her brother, and the winter she spent sleeping in the back room because the front was unsafe. She does not ask for charity. She wants the inspection repeated by someone who understands the difference between a patched roof and an empty house.{/n}

{n}Terendelev listens without interrupting. When Asla finishes, the dragon asks what she would need to make the home safe before the first snow. The answer is lumber, two days of labor, and a stove pipe that does not leak.{/n}

"That is a plan we can assess," Terendelev says. "It is not the same as a promise that every house can remain."{/n}''', c('[Ask the committee to fund a second inspection and a repair estimate.]', "decision", flags=f("resident.heard"))),
    n("records", "Narrator", '''{n}Venn opens the case. The originals are not a single report, but a stack of notes from three inspections. One uses an obsolete street grid. Another records a dangerous foundation without stating that the house is empty. The third is missing the inspector's signature.{/n}

{n}No single page proves that Venn forged anything. Together they show that the petition's confident totals were assembled from records that cannot bear the weight put on them.{/n}

Terendelev asks Venn whether he knew the gaps were there. He admits that he did. He thought the danger of delay was greater than the harm of a few mistaken notices.{/n}''', c('[Require a public correction and a fresh inspection before any clearance.]', "decision", flags=f("records.opened"))),
    n("clerk", "Narrator", '''{n}The clerk says the notice was written to invite inspections. The courier who carried it told residents that inspectors would return with guards. He had been promised a paid position on the clearance crews if the petition passed.{/n}

{n}The clerk cannot say whether the courier invented the threat or repeated what he had heard from Venn. The evidence establishes a financial interest and a false rumor, not who first ordered it.{/n}

Terendelev asks for the courier's name and the dates of the deliveries. She will not call it a deliberate plot until residents can be questioned without the organizer present.{/n}''', c('[Separate the paid courier from the inspection plan and investigate both.]', "decision", flags=f("delivery.traced"))),
    n("opening", "Terendelev", '''"My name is not an order," Terendelev says. "I have not inspected these homes. I have not approved the numbers in this petition. I have agreed to hear the people who live here and the people who fear the wall will fail."

{n}She glances at the residents rather than the committee.{/n}

"If I am wrong about the danger, show me. If you are wrong about a home being empty, correct the list. We will not settle either question by asking which of us has the more impressive title."{/n}''', c('[Let the residents speak, then move to a documented decision.]', "decision", flags=f("meeting.limits"))),
    n("decision", "Terendelev", '''The room breaks into smaller arguments. Terendelev lets them run until the residents begin speaking to one another rather than waiting for a verdict from her.

"We have a choice," she says to you. "We can suspend the petition, repair the most urgent homes, and pay for new inspections. That costs time and money. We can authorize a smaller evacuation for houses independently found at immediate risk, with temporary lodging and a right to return. Or we can let the current committee proceed and promise that we will correct its mistakes later."

{n}She does not conceal which option she favors. She asks you to say what the evidence supports, not what will make her grateful.{/n}''',
      c('[Suspend the petition, fund repairs, and demand a fresh inspection.]', "pause", flags=f("decision.pause")),
      c('[Authorize verified immediate evacuations with lodging and return rights.]', "narrow", flags=f("decision.narrow")),
      c('[Let the committee proceed, but publish the errors and promise later review.]', "proceed", flags=f("decision.proceed"))),
    n("pause", "Narrator", '''{n}The petition is suspended pending a new inspection. The cost will come from funds reserved for the rebuilding committee, and the builders complain that delay could leave unstable homes in place.{/n}

{n}Terendelev does not call the decision righteous simply because it resembles her preference. She asks for a schedule, a named inspector, and a public list of what will count as immediate danger. The residents choose two observers to accompany the review.{/n}

{n}When the room empties, she turns to you.{/n}

"You did not rescue them for me. You made the plan answerable to them. I am glad you came."{/n}''', c('[Leave the repair plan in their hands and walk Terendelev home.]', flags=f("civic.resolved", "civic.pause"))),
    n("narrow", "Narrator", '''{n}The committee agrees to inspect each house again. Two buildings with visibly failing supports will be evacuated that night; their residents receive rooms nearby and written permission to return after repairs. The other homes remain occupied until their inspection is complete.{/n}

{n}Terendelev makes the limits plain. If the second inspection finds another immediate danger, there may be another evacuation. No one is promised that a loved home is safe simply because leaving it would hurt.{/n}

{n}She waits while the residents read the terms aloud and correct the location of the temporary rooms.{/n}

"It is not a perfect answer," she says after the meeting. "It is an answer people can challenge while there is still time to change it."{/n}''', c('[Walk her home without calling the compromise a victory.]', flags=f("civic.resolved", "civic.narrow"))),
    n("proceed", "Narrator", '''{n}The committee continues with its original schedule. Your promise of later review is entered into the minutes, but the residents leave without a date for that review. Terendelev does not argue in the room. She waits until the door has shut.{/n}

"You have left the burden with the people who have the least power to force us to keep our promise," she says. Her voice is quiet, not forgiving.

"You may be right that delay is dangerous. But do not ask me to call an unkept promise a compromise."{/n}''', c('[Accept her judgment and commit to securing a dated review.]', "repair", flags=f("civic.proceed")), c('[Defend the decision and let the disagreement stand.]', "repair", flags=f("civic.proceed"))),
    n("repair", "Terendelev", '''{n}You do not erase the decision by regretting it. Terendelev asks the committee to name a review date and give the residents copies of the inspection records. Some support her. Others say a public challenge will scare workers away.{/n}

She looks to you once, giving you the chance to speak. If you accept responsibility, she asks you to say what you will do and when. If you defend the choice, she tells the room she disagrees and will not use her return to lend it authority.

{n}The work continues with less trust than it might have had. Terendelev walks back to the keep beside you, but the silence between you takes effort to cross.{/n}''', c('[Ask what she needs from you now, then listen without demanding reassurance.]', flags=f("civic.resolved", "civic.cost"))),
], requires=RETURNED + f("returned.chapter1", "civic.accepted"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=36)

add("private_oath", "An oath with room to breathe", "Terendelev", [
    n("start", "Terendelev", '''{n}Terendelev asks you to meet her in the lower garden after the day's work is done. The builders have accepted the new inspection terms; the residents have not yet decided whether they trust them.{/n}

"I have been thinking about our old oath," she says. "It was made while I was divided between a voice in the dark and a creature built from my own remains. I do not regret it. I do want a promise that belongs to the people we are now."

She has brought a narrow silver cord. It is plain, without a crest or prayer. She sets it between you on the stone bench.{/n}

"No vows of obedience. No promise that desire will outlast disagreement. I want us to tell one another when we are choosing this, and to leave one another able to choose again tomorrow."{/n}''',
      c('[Ask what she wants the cord to mean before agreeing.]', "meaning"),
      c('[Offer a promise to make space for her duty to Kenabres.]', "duty"),
      c('[Tell her you want her, but will not turn an oath into ownership.]', "desire")),
    n("meaning", "Terendelev", '''"A reminder," she says. "Not a proof. If one of us keeps it, the other can ask what it means. The answer can change."

{n}She loops the cord around her fingers, then offers you one end.{/n}

"I want to be able to remember the promises I make without having to obey the person who remembers them for me."{/n}''', c('[Take the other end and agree that either may untie it.]', "oath", flags=f("oath.considered"))),
    n("duty", "Terendelev", '''"Kenabres is not a rival for your affection," she says. "It is a place with people who kept living while I was gone. I will sometimes choose their need over an evening with you. I do not want you to praise me for it or punish me for it."

{n}Her expression softens.{/n}

"And I will not ask you to pretend that it costs nothing. I want you to tell me when you miss me. I can answer honestly without giving up the choice."{/n}''', c('[Promise to tell her the truth without demanding she change her duty.]', "oath", flags=f("oath.considered"))),
    n("desire", "Terendelev", '''"Good," she says. "I want to be wanted. I do not want to be necessary in the way a key is necessary to a lock."

{n}Her fingertips close over yours.{/n}

"There is a difference between surrender and being taken. Sometimes I may want to give you the lead. Sometimes I will want to take it back. If that sounds less romantic than a perfect vow, you have not been listening to me."{/n}''', c('[Tell her that the changing choice is part of what you want.]', "oath", flags=f("oath.considered"))),
    n("oath", "Terendelev", '''{n}You each tie one end of the cord around a wrist. Neither knot is tight. Terendelev checks yours, then lets you check hers.{/n}

"Now say something true that you can keep," she says.

You tell her that you love her and cannot promise to make every future choice painless. She says she loves you, and will not use your failures as proof that the feeling was a mistake.

{n}The words are not a cure for grief, memory, or work. They are a way to find each other again when those things have made the path difficult.{/n}

She kisses you, then waits until you answer with your hands at her waist. When you do, her breath catches. The next kiss is hers to deepen, and she does. The quiet confidence of the gesture is more intimate than any ceremony could make it.{/n}''', c('[Stay with her for the evening, letting the rest of the night remain private.]', flags=f("oath.made", "returned.chapter2", "romance.confirmed"))),
], requires=RETURNED + f("civic.resolved", "romance.confirmed"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=48)

add("inspection_day", "The second inspection", "Terendelev", [
    n("start", "Terendelev", '''{n}The inspection takes place over two days. Terendelev asks you to come for the second, when the residents' observers will be present and the builders can no longer claim the earlier mistakes were only clerical.{/n}

{n}A mason taps the lintel of Asla's house and listens. The sound is hollow in one corner. The roof is not collapsed, but the beam has split where an old repair concealed water damage.{/n}

"The list was wrong about the house being empty," Terendelev says. "It was not wrong to call it dangerous. Both facts matter."{/n}

{n}Asla looks from the beam to the room she has lived in. She asks how long she will be expected to leave, who will pay for the repair, and whether anyone can promise she will be allowed back.{/n}

Terendelev does not answer before the builders do.{/n}''',
      c('[Ask for a temporary room near the house and a written right of return.]', "lodging", flags=f("inspection.lodging")),
      c('[Ask the residents to choose which repair should be funded first.]', "residents", flags=f("inspection.residents")),
      c('[Insist that the builders state what they know and what is still uncertain.]', "uncertainty", flags=f("inspection.uncertainty"))),
    n("lodging", "Narrator", '''{n}The nearest available lodging is across the market square. Asla says she can manage it if her brother can carry the furniture and if the stove is moved before the roof is opened.{/n}

{n}The builders agree to put the return date in writing after the repair inspection. They cannot promise the work will be finished before the next storm, but they can promise to keep the rooms available and to tell the family when the plan changes.{/n}

Terendelev asks Asla to read the written terms back to the builders. The phrasing is plain enough to expose what the committee has not agreed to pay.{/n}''', c('[Make the missing labor and lodging cost part of the public schedule.]', flags=f("inspection.outcome.lodging"))),
    n("residents", "Narrator", '''{n}The residents choose two repairs to fund first. A widow with a leaking roof votes for the foundation work because the house beside hers leans toward her wall. She has been waiting for someone to call her concern more than a private inconvenience.{/n}

{n}The committee's builders object that their own order is safer. Terendelev asks them to show the load calculations. She does not announce that the residents are right before she has read them.{/n}

The figures explain why the foundation should be stabilized before new roofing begins. The first schedule was written for speed, not safety.{/n}''', c('[Reorder the work and let the residents monitor the schedule.]', flags=f("inspection.outcome.residents"))),
    n("uncertainty", "Narrator", '''{n}The builders admit that they have not opened the wall. Until they do, no one can say whether the beam can be reinforced or whether the roof must be removed entirely.{/n}

{n}Terendelev asks them to record that uncertainty. She is willing to evacuate a household for a night if the exposed beam gives way. She will not tell the family the house is safe because a confident answer would be easier to hear.{/n}

The residents ask for an observer to remain through the first cut. The builders accept after the committee agrees to pay for the extra day.{/n}''', c('[Approve the inspection with a named observer and a stop-work rule.]', flags=f("inspection.outcome.uncertain"))),
    n("end", "Terendelev", '''{n}By dusk, the residents have copies of the revised schedule. It names who will pay for lodging, what work begins first, and when the next inspection will occur.{/n}

Terendelev watches the last family carry a small stove across the square. She does not call the outcome a victory. One home may still need to be rebuilt, and the people who have left it do not know when they will return.

"I wanted to save them from the order," she says. "We have instead made the order answerable. That is less beautiful and more useful."{/n}

{n}She looks at you with a tired smile.{/n}

"I am glad you did not make me thank you for agreeing with me. I want to thank you for staying when the answer became inconvenient."{/n}''', c('[Walk with her through the market before returning to the keep.]', flags=f("inspection.complete", "romance.confirmed"))),
], requires=RETURNED + f("civic.resolved", "returned.chapter1"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=48)

add("windward_evening", "The height she chooses", "Terendelev", [
    n("start", "Terendelev", '''{n}Terendelev asks you to meet her in a book-event room with an open roof and no audience. She has chosen a memory of the hill beyond Kenabres, before the city was rebuilt, when the wind came cleanly over the stone.{/n}

"This is not a promise that we will fly," she says. "It is a place where I can remember the feeling without having to explain it to anyone watching."

{n}The night sky is clear above the low wall. Terendelev wears the familiar human form. Her clothes carry the same practical lines as the parent portrait, loosened at the throat for the warmth of the evening. She has left her hair unbound.{/n}

"I used to think the sky was something I could return to whenever I wished. After I died, I began to understand it as something I could lose."{/n}''',
      c('[Ask her what she misses about flight, and let her lead the memory.]', "memory"),
      c('[Tell her what you remember from the first time she flew beside you.]', "shared"),
      c('[Tell her you want to touch her, then wait for her answer.]', "touch")),
    n("memory", "Terendelev", '''"The pressure changes before the wind does," she says. "You feel the air decide whether it will hold you. The ground stops being a list of things that can be lost and becomes a shape you can choose to approach."{/n}

{n}She stands close enough for your sleeves to brush. Her fingers move over the stone wall, following a line that would be invisible from below.{/n}

"I miss knowing exactly what my body can do. I do not miss being told that because I could survive a fall, I should accept every risk someone else finds dramatic."{/n}''', c('[Tell her that you miss it with her, but want her to set the height.]', "height", flags=f("flight.shared"))),
    n("shared", "Terendelev", '''"You remember the first time I let you ride with me?"{/n}

{n}You remember the wind, the sudden lift, and the city falling away beneath you. You remember holding on more tightly than you admitted afterward.{/n}

"You were frightened," she says. "You were also trying to look as though you had planned it. I could feel your fingers through the saddle straps."{/n}

"You could have warned me."

"I did. You told me that you were ready."{/n}

{n}She smiles at the memory and then lets it pass without asking it to prove what you should do now.{/n}''', c('[Ask whether remembering the flight feels comforting or painful tonight.]', "height", flags=f("flight.shared"))),
    n("touch", "Terendelev", '''{n}Terendelev watches you for a moment, then takes your hand and places it against the side of her waist.{/n}

"There," she says. "You asked. I have answered."

{n}The contact is simple and warm. Under the fabric, her body shifts as she breathes. Her fingers trace your wrist, then turn your hand so that she can kiss the inside of it.{/n}

"I like the way you look at me when you remember I am more than a voice or a promise. I like being desired. I do not want you to turn that into a demand for the dragon shape because you believe it would make the scene more impressive."{/n}''', c('[Tell her the choice of shape is hers, and ask what she wants tonight.]', "height", flags=f("touch.chosen"))),
    n("height", "Terendelev", '''"Tonight I want the wind and your hands," she says. "The wind is available here. The rest depends on whether you can keep listening."{/n}

{n}She steps past you and opens the memory of the hill. The stone wall becomes a ridge, the city lights a low scatter in the distance. No body has been transformed. It is a place made from recollection, and both of you know it.{/n}

Terendelev offers you her hand. When you accept, she draws you into a slow turn, the movement more like dancing than flight. Her body presses close; her mouth brushes your cheek and then the corner of your lips.

"You may ask me to show you the sky," she whispers. "You may not decide that I owe it to you."{/n}''',
      c('[Ask, and accept that she may choose not to transform.]', "ask", flags=f("flight.requested")),
      c('[Stay in the human shape and let the evening remain close and private.]', "human", flags=f("flight.deferred"))),
    n("ask", "Terendelev", '''{n}She studies you. The question has not made the answer inevitable.{/n}

"Not tonight," she says. "I want to remember the height without asking my body to perform it."

{n}She watches to see whether you will hide your disappointment or try to argue it away. When you nod, she kisses you with the slow confidence of someone who has chosen the next thing herself.{/n}

Her hands settle at your shoulders. Yours rest at her waist. The kiss deepens until the wind is only a cool edge against your skin and the city below is only a pattern of lights.

She breaks away before the moment becomes a promise you did not discuss. Her forehead rests against yours.{/n}

"I wanted to see whether you could want something and still let me keep my answer. I am pleased with you. I also want to make clear that I was not testing you for a reward."{/n}''', c('[Tell her you want the evening because you want her, not because of what she refused.]', "close", flags=f("flight.trust"))),
    n("human", "Terendelev", '''{n}You leave the transformation unasked. Terendelev's shoulders ease.{/n}

"Thank you," she says. "I may want to fly with you again. I would rather decide that on a day when the sky itself is not carrying half the conversation."{/n}

{n}She pulls you close and kisses you. There is no ceremony in the way her hand moves along your back. She pauses when she feels you tense, waits for your answer, and continues only when you draw her closer.{/n}

The warmth between you becomes less tentative. Her mouth finds your throat. When she looks up, her eyes are bright and amused.

"You may tell me if you want to stop," she says. "I will believe you the first time."{/n}''', c('[Stay with her and let the remaining night be private.]', "close", flags=f("flight.trust"))),
    n("close", "Terendelev", '''{n}Terendelev takes your hand and rests it over her heart. Her pulse is quick. She watches you understand what that means to her: not proof of resurrection, not a repayment, but the living body she has chosen to share with you tonight.{/n}

"I thought death had made me into a thing people remembered," she says. "This is better. It is messy, warm, and rather inconveniently alive."{/n}

{n}She kisses you once more before the book-event memory fades. The scene ends with the two of you still choosing to stay, while the next morning remains ordinary and unresolved.{/n}''', c('[Leave the hill together and agree to meet again after her next duty.]', flags=f("intimacy.adult", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=72)

add("kenabres_vigil", "The names that survived her", "Terendelev", [
    n("start", "Narrator", '''{n}The petition's work has slowed long enough for the residents to invite Terendelev to a small vigil. They plan to read the names of people lost in the attack, then the names of people who returned to rebuild.{/n}

{n}The invitation asks her to speak. It does not ask what she can do for the city. She reads it twice before accepting.{/n}

"I know some of these names," she says. "I do not know the people they became while I was gone. I will not pretend that memory gives me the right to speak for them."{/n}

{n}She asks you to attend beside her, but not to stand between her and the families. The event is a narrated book memory of a later evening in Kenabres; the scene does not teleport either of you or create a native city-state change.{/n}''',
      c('[Ask whether she would rather speak briefly or read names with the residents.]', "choice"),
      c('[Offer to tell the organizers she will not speak for anyone who has not asked.]', "terms"),
      c('[Ask what she wants you to do if someone blames her for surviving.]', "blame")),
    n("choice", "Terendelev", '''"I want to read the names with them," she says. "A speech would make the evening about my return. Reading together lets me be one of the people who remembers, and one of the people who has to listen."{/n}

{n}She chooses a place in the second row. When a family asks whether she remembers their son, she says she remembers the street, but not the boy. She does not invent a comforting detail to close the silence.{/n}

The mother thanks her for answering honestly and continues with the next name.{/n}''', c('[Stay beside her without answering for her.]', flags=f("vigil.honest"))),
    n("terms", "Terendelev", '''"Tell them I will come as myself," she says. "If they want a speaker, they can ask someone who knows what happened after I died. I will not make the word survivor carry more than it can."{/n}

{n}The organizer accepts the limit. One committee member complains that a quiet vigil cannot become a public statement. Terendelev tells him that remembrance is not a petition and does not need to produce a decision.{/n}

She looks to you, checking that you will not use the moment to endorse the rebuilding plan.{/n}''', c('[Agree that the vigil should remain separate from the petition.]', flags=f("vigil.separate"))),
    n("blame", "Terendelev", '''"You will let me answer for myself," she says. "If I ask you to stay, stay. If I ask you to leave, leave. I do not want you to defend my survival as if it were an argument I have to win."{/n}

{n}She squeezes your hand once, then lets go before anyone can read it as a public declaration.{/n}

At the vigil, an old man says she should have died with the others. Terendelev does not answer immediately. When she does, she says she knows why he wants a reason that fits the loss. She cannot give him one.{/n}''', c('[Let the silence remain before the next family reads.]', flags=f("vigil.silence"))),
    n("end", "Terendelev", '''{n}After the last name, Terendelev stays to help fold the chairs. No one makes a speech about her courage. No one asks her to bless a plan.{/n}

She walks with you through the square, where the lamps have been lit in a line that leaves no one in darkness. Her shoulder brushes yours once; she does not take your hand until the crowd has thinned.

"That was difficult," she says.

"Do you want to do it again?"

"I want to remember that I can choose it. I do not yet know when I will want to."{/n}

{n}She leans against you for a moment, then stands straight again.{/n}''', c('[Offer comfort without asking her to turn the vigil into a promise.]', flags=f("vigil.complete", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=96)

add("private_aftercare", "The morning after choosing", "Terendelev", [
    n("start", "Terendelev", '''{n}Morning enters the room before either of you is ready for it. The night has left the curtains half open and the silver cord loose on the table.{/n}

{n}Terendelev is awake, turned toward you. She studies your face with the frankness of someone who knows you have already seen her at less flattering hours.{/n}

"I would like to talk before either of us pretends this was a dream," she says. "I wanted you last night. I still want you this morning. Both answers are mine. Neither one means I have become easy to understand."{/n}

{n}She draws a finger along your shoulder, then stops before the touch becomes a question you have to interpret.{/n}''',
      c('[Tell her what you wanted and ask what she would like now.]', "desire"),
      c('[Ask whether anything from last night made her uncomfortable.]', "checkin"),
      c('[Say you want more time with her but will not treat that as a claim.]', "time")),
    n("desire", "Terendelev", '''You tell her that you wanted her confidence as much as you wanted her body, and that you want the chance to keep discovering what she likes.{/n}

{n}She raises one eyebrow.{/n}

"That is a very polished answer. Is it true?"

You admit that you also wanted to make the night last because the future feels uncertain. She nods, taking the truth without accepting it as a reason to hurry.{/n}

"I want to be touched again," she says. "I also want breakfast before the kitchen closes. If we can manage both without turning one into proof of the other, I will be impressed."{/n}''', c('[Kiss her, then help her find something to eat.]', flags=f("aftercare.desire"))),
    n("checkin", "Terendelev", '''"Nothing I have not already told you," she says. "I liked the questions. I liked that you waited when I paused. I did not like being watched for a sign that you had passed a test."{/n}

{n}You tell her that you sometimes looked for that sign because you feared getting it wrong. She says she understands the fear and does not want to be responsible for soothing it every time you touch her.{/n}

"I can tell you what I want. You can ask. We can both change our minds. That is not a test with a secret correct answer."{/n}''', c('[Thank her, and ask what would feel good now.]', flags=f("aftercare.checkin"))),
    n("time", "Terendelev", '''"Good," she says. "I would like more mornings. I cannot promise that the ones we get will be ordinary, and I do not want you to fill the uncertainty with a vow neither of us can keep."{/n}

{n}She takes your hand and turns the silver cord around your wrist. The knot has slipped loose during the night.{/n}

"We can tie it again. Or leave it loose. I would rather have you ask than guess what the old promise demands."{/n}''', c('[Ask whether she wants to tie it again or leave it loose.]', flags=f("aftercare.time"))),
    n("end", "Terendelev", '''{n}Terendelev chooses breakfast first. She pulls on the familiar clothes she wore the evening before, then pauses when she notices the silver cord in your hand.{/n}

"Leave it loose," she says. "I want to remember that it can come undone without either of us disappearing."{/n}

{n}At the door, she kisses you once, without audience or oath. The kiss is more urgent than the one in the garden and more certain than the one on the hill. When it ends, she keeps her hand on your chest for a heartbeat.{/n}

"I am going to check the inspection schedule," she says. "If you are coming, bring your own breakfast. The builders have learned that I will notice if they skip it."{/n}''', c('[Go with her, as her partner and not her keeper.]', flags=f("aftercare.complete", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made", "intimacy.adult"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=24)

# Trickster route: investigation and consent, not an automatic escape or resurrection.
add("scale_invitation", "The copy that remembers the wrong sky", "Memory", [
    n("start", "Narrator", '''{n}The scale grows cold in your palm. The voice comes through with the familiar restraint of someone who has learned that being heard is not the same thing as being safe.{/n}

"I have found something wrong with this place. Not with the memory inside it. With the edge between that memory and the rest of the world."

{n}Terendelev describes the replica Kenabres. Its buildings are drawn from remembered streets, but the sky does not move. She has counted the shadow of the bell tower for what feels like three afternoons; it remains fixed at the same angle.{/n}

"I know what you did when fate insisted there was only one ending. That is not why I am asking you to come. I am asking because you know how to look for the seam in a rule. If you find one, you will tell me what crossing it costs before you ask me to choose."{/n}''',
      c('[Accept the investigation, with no promise of escape or romance.]', "accept", flags=f("started", "bound", "escape.accepted")),
      c('[Help only if the plan leaves her able to refuse.]', "accept", flags=f("started", "bound", "escape.accepted", "escape.consent")),
      c('[Decline to interfere with the scale prison.]', "decline", flags=f("bound", "escape.declined"))),
    n("accept", "Narrator", '''{n}The scale warms enough for the voice to continue.{/n}

"Then we begin with what is outside this place," Terendelev says. "I do not need a speech about how powerful you are. I need a fact that this copy cannot have invented for itself."

{n}You agree to bring her two independent observations: one tied to her remains, and one recorded by a living witness in the city. The first is available only if the claw was preserved. The second can come from a resident's dated account or the Storyteller's witnessed report. Neither by itself proves that her soul can be returned.{/n}

"If the evidence does not fit," she says, "we stop. I will not have you making a door out of my longing."{/n}''',
      c('[Begin with the claw, if it remains in your possession.]', "claw", requires=f("claw.possessed")),
      c('[Begin with a dated account from a living Kenabres witness.]', "witness", flags=f("evidence.witness")),
      c('[Ask the Storyteller to repeat the account already given about her soul.]', "storyteller", flags=f("evidence.storyteller"))),
    n("claw", "Narrator", '''{n}The claw is colder than the scale. You do not take it to an altar or ask it to answer a question it cannot understand. The Storyteller identifies the place from which it came and confirms that he once believed her soul might be found in the darkness beyond death.{/n}

{n}That account is evidence of a search and a belief. It is not proof that the same path remains open now, or that the fragment in the scale will survive a crossing.{/n}

Terendelev is silent for a long while.

"Thank you for not improving the answer."{/n}''', c('[Record this as one clue, not a guarantee.]', "compare", flags=f("evidence.claw"))),
    n("witness", "Narrator", '''{n}The witness is a bell keeper who survived the first night of the attack. Her ledger records the bells she rang and the shadows that crossed the square. She remembers the tower's broken west face, now rebuilt with a different stone.{/n}

{n}You ask for the present description, not a story of Terendelev. The witness describes the new roof, the repairs, and the names of the people who replaced it. This gives you a fact that the old replica city could not have witnessed when it was made.{/n}

The memory within the scale has the same tower, the old stone, and the same unchanging shadow. It does not answer whether a boundary can carry a person.{/n}''', c('[Carry the dated observation to the scale and record both versions.]', "compare", flags=f("evidence.witness"))),
    n("storyteller", "Narrator", '''{n}The Storyteller repeats that he followed the soul's trace after the attack and found only a question he could not answer. He speaks carefully, without pretending that his old search can be repeated on command.{/n}

{n}His account gives you an independent point of comparison, not a map. Terendelev listens without interrupting.{/n}

"I remember the darkness," she says at last. "I do not remember what he saw. Do not use his hope as a location."{/n}''', c('[Write down the limit as carefully as the clue.]', "compare", flags=f("evidence.storyteller"))),
    n("compare", "Narrator", '''{n}You compare the details: a real bell, a current repair, the old tower preserved in the copy, and the still shadow. The contradictions are precise enough to test. They do not prove that the prison has a door, only that it may be keeping a world in place by refusing to admit new facts.{/n}

{n}Terendelev asks you to explain the difference between a contradiction and an opening. You tell her that a contradiction can reveal a rule; it cannot guarantee what happens when the rule is broken.{/n}

"Good," she says. "The trick is not to make the impossible sound ordinary. It is to discover which part of it is a claim no one has tested."{/n}''',
      c('[Use Knowledge: Arcana to identify the scale’s boundary rule.]', "rule", check=dict(Skill="SkillKnowledgeArcana", DC=28, CommanderOnly=True, Success="rule", Failure="uncertain")),
      c('[Use Knowledge: World to test the tower record against the altered city.]', "rule", check=dict(Skill="SkillKnowledgeWorld", DC=28, CommanderOnly=True, Success="rule", Failure="uncertain")),
      c('[Repeat the comparison with a second resident before making a theory.]', "second", flags=f("evidence.second"))),
    n("rule", "Narrator", '''{n}You identify the scale as an anchor for the copied memory, not a vessel that can simply be opened. The false sky and unchanging shadow suggest that the replica rejects information it cannot place within its remembered pattern.{/n}

{n}Terendelev does not call that a solution. She asks whether an outside fact could be introduced without tearing the memory apart. You explain that the hypothesis needs another observation and a controlled test. There is no safe way to infer that a soul will survive from a crack in a story.{/n}

"Then we do not test it on me," she says. "We test the memory. If the copy changes, we learn something. If it does not, we have lost an afternoon and not a person."{/n}''', c('[Propose a nonliving test and report the result before any crossing.]', flags=f("escape.theory", "escape.test.authorized"))),
    n("uncertain", "Narrator", '''{n}The evidence is not enough to identify the boundary. Your theory might explain the fixed sky, or it might merely give a name to a detail you do not yet understand.{/n}

{n}Terendelev rejects the temptation to reward confidence. She asks for another dated observation from a second witness and a fresh comparison with the scale. That costs time and another visit, but does not close the possibility.{/n}

"If your answer becomes true only because you have said it aloud," she says, "it is not an answer I can trust."{/n}''', c('[Gather a second independent account before continuing.]', flags=f("escape.more_evidence"))),
    n("second", "Narrator", '''{n}The second resident remembers the bell tower from a different street and gives a separate date for the rebuilding. The two accounts agree about the new stone and differ about the weather that day. That disagreement is useful: it shows where memory can vary without making the tower itself imaginary.{/n}

{n}The scale's city has no such variation. Its sky does not move and its people return to the same motions. The pattern is stronger evidence of a bounded reconstruction than either testimony alone.{/n}

Terendelev thanks you, then reminds you that knowledge of a prison is not permission to break it.{/n}''', c('[Ask her to choose whether to test the boundary further.]', flags=f("escape.theory", "escape.test.authorized"))),
    n("decline", "Narrator", '''{n}You do not ask the scale to answer. Terendelev's voice remains quiet.{/n}

"I am disappointed," she says. "I would have liked to know whether there was another way out. I am not angry that you declined to gamble with what remains of me."{/n}

{n}No escape has been attempted, and no new promise has been made. The scale stays what it was: a channel for contact, not proof that a living return is possible.{/n}''', c('[End the investigation without changing her confinement.]', flags=f("closed"), abort=True)),
], requires=(PARENT_QUEST, PARENT_BOUND, "trickster", "terendelev.continuation.bound_finale_seen"), forbids=(PARENT_LICH_BIND, "terendelev.continuation.escape.declined"), remote=True)

add("escape_boundary", "A rule that can be tested", "Memory", [
    n("start", "Narrator", '''{n}The next time you speak through the scale, Terendelev begins with the question you left unanswered: what can be tested without making her the test?{/n}

{n}You have arranged a small change to the replica: a dated description of the rebuilt tower, carried into the memory by the same channel used for ordinary contact. No spell will be cast on her. No demand will be made of the people in the copy. The experiment can be stopped if the city begins to distort.{/n}

"I want to see what happens when this place learns something new," she says. "I do not want to find out by watching someone else suffer for it."{/n}''',
      c('[Introduce the new description and ask her to compare it with the tower.]', "result_pending", flags=f("escape.test.requested"), requires=f("escape.theory", "escape.test.authorized")),
      c('[Delay until another witness can confirm the record.]', "wait", flags=f("escape.test.wait"))),
    n("result_pending", "Narrator", '''{n}You send the dated description through the channel and wait for the registered test observer to report what actually happened. The manuscript does not assume the memory changed just because the plan was attempted.{/n}

"No crossing while we do not know the result," Terendelev says. "If it changes, tell me exactly how. If nothing happens, say that. If it becomes unsafe, end the test and do not call the damage a door."{/n}''',
      c('[Review an observed boundary change, if the test handler confirms it.]', "changed", requires=f("boundary.result.changed")),
      c('[Review an observed unchanged result, if the test handler confirms it.]', "unchanged", requires=f("boundary.result.unchanged")),
      c('[Review an unsafe result, if the test handler confirms it.]', "unsafe", requires=f("boundary.result.unsafe"))),
    n("changed", "Narrator", '''{n}The registered observer confirms that the copy changed after the dated account arrived. You compare the recorded before-and-after details with Terendelev; the change is evidence that the boundary can register new information, not evidence of a traversable opening.{/n}

"A change is not a door," she says. "Now we know that the place can answer. We still do not know what it would do to anyone who crossed."{/n}''', c('[Record the limited result and continue only with her agreement.]', flags=f("escape.test.observed", "boundary.result.recorded"))),
    n("unchanged", "Narrator", '''{n}The registered observer confirms that the tower, sky, and shadow remain as before. The test produced no visible change. You record the null result as carefully as a dramatic one.{/n}

"Then we have not found a seam," Terendelev says. "Do not make failure sound like hidden progress because you dislike the answer."{/n}''', c('[Record no change and ask whether she wants another evidence visit or to stop.]', flags=f("boundary.result.recorded", "escape.test.no_change"))),
    n("unsafe", "Narrator", '''{n}The registered observer reports instability in the copy. The test handler stopped the attempt and closed the channel without asking Terendelev to bear the effect. No crack or passage is treated as success.{/n}

"That is enough," she says. "I will not risk what remains of me for a result we cannot contain."{/n}''', c('[End the boundary experiment and preserve her refusal to continue.]', flags=f("boundary.result.recorded", "escape.test.unsafe_stop", "closed"), abort=True)),
    n("wait", "Narrator", '''{n}You wait for the second witness. The scale remains cool, its familiar voice absent for several days.{/n}

{n}When the account arrives, the dates agree and the descriptions do not. The second resident remembers rain against the eastern wall; the first remembers a clear sky. Both place the new stone after the attack.{/n}

{n}The evidence is stronger because it preserves a real disagreement. Terendelev can compare a fixed reconstruction with facts that do not depend on a single memory.{/n}''', c('[Return to the scale with the corroborated record.]', flags=f("escape.theory", "escape.test.authorized"))),
], requires=BOUND + f("escape.accepted"), forbids=(PARENT_LICH_BIND,), delay=48, remote=True)

# The parent-ending branches below offer investigation, not inherited romance.
add("trickster_friendship", "A conversation without courtship", "Memory", [
    n("start", "Terendelev", '''{n}The scale carries Terendelev's voice, but no warmth has been promised with it.{/n}

"I remember the end of our last conversation. We did not leave it in a courtship, and I do not want this investigation treated as a clever way to make that answer disappear."

{n}She waits for you to answer.{/n}

"I can still speak to you about what is happening here. I can decide that your evidence matters. That is not a new courtship, and it is not a promise that one will follow."{/n}''',
      c('[Tell her the refusal stands, and offer evidence without asking for anything else.]', "evidence", flags=f("friendship.respected")),
      c('[Ask whether she might change her mind if you succeed.]', "boundary"),
      c('[Withdraw the offer and leave the channel quiet.]', "withdraw", flags=f("friendship.withdrawn"))),
    n("evidence", "Terendelev", '''"Thank you," Terendelev says. "Then tell me what the witness actually saw."

{n}You give her the date, the rebuilt western face of the bell tower, and the two accounts that disagree about the weather. You do not say this must mean that she can escape. You say only that her copy has no record of the rebuilding.{/n}

"That is a fact," she says. "Not a promise. It is enough to investigate."

{n}She asks what happened when the shadow moved. You explain that she asked you to stop the test, and that you stopped.{/n}

"You listened. I am glad. Do not turn that into a reason I owe you trust. It is simply what should have happened."{/n}''', c('[Continue only with the investigation she chooses.]', flags=f("friendship.investigation"))),
    n("boundary", "Terendelev", '''"Then I will not answer your question," she says. "You have made my feelings into a bargain whose price is your success. I will not let the quality of your work decide what I owe you."{/n}

{n}The scale cools. Several days pass before the next message. When it comes, she asks only whether you have new evidence about the tower. She does not mention romance or the question you asked.{/n}''', c('[Apologize, present the new facts, and do not ask again.]', "evidence", flags=f("friendship.repaired")), c('[End the investigation without another message.]', "withdraw", flags=f("friendship.withdrawn"))),
    n("withdraw", "Narrator", '''{n}You set the scale down. No answer follows, and none is owed.{/n}

{n}The Trickster's plan ends here. You keep the evidence, but do not use it to force contact. Terendelev remains where the last verified ending left her.{/n}''', c('[Close this approach.]', flags=f("closed"), abort=True)),
], requires=BOUND + f("escape.accepted") + ("trickster", "terendelev.continuation.bound_nonromance_seen"), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_native_lead", "A name without a scale", "Memory", [
    n("start", "Narrator", '''{n}You have never spoken with Terendelev through the silver scale. The Trickster's investigation begins with two records instead: the Storyteller's account of searching for her after Kenabres fell, and the claw the native quest placed in the Swarm cave.{/n}

{n}The claw is a remnant, not a person, a soul-vessel, or permission to summon her. The Storyteller's memory describes a search and a hope, not proof that the same path remains open.{/n}

You can revisit the cave only if the original native collectible and its action are still available. If it has already been collected, the actual inventory must establish whether the item remains. The story must not grant a replacement claw because the investigation needs one.{/n}

"If you mean to change a fate," the Storyteller says, "begin by learning which pieces of it you still possess."{/n}''',
      c('[Ask the Storyteller to prepare the signal and send one invitation.]', "prepare", requires=("terendelev.continuation.native_quest_verified", "terendelev.continuation.native_original_clue_verified", "terendelev.continuation.native_ravener_outcome_verified")),
      c('[Decline to spend the clue or favor and leave contact unopened.]', "wait", flags=f("native.pending"))),
    n("prepare", "Narrator", '''{n}The Storyteller sets the verified clue beside a page of his notes. The memory-signal will carry only an invitation: Terendelev may answer, refuse, or remain silent. It does not claim that the claw contains her soul, that the Storyteller can find her, or that the Trickster can restore her.{/n}

{n}The signal costs the claw if it is still held. If it is absent, the Storyteller instead spends a unique favor he cannot offer again. This authored cost, the signal, and its response are not implemented by this manuscript.{/n}

{n}The registered caller must verify the cost, persist the one-use attempt, and wait for an explicit voluntary answer. Until that caller and response handler exist, this page cannot appear in game.{/n}''', c('[Send the single invitation only after the registered handler is installed.]', flags=f("native.invitation.requested"))),
    n("wait", "Narrator", '''{n}You do not guess. The scale may have been consumed, and the claw may have been collected, lost, or never touched. Each possibility means something different.{/n}

{n}The native quest record remains intact while the investigation waits for a live inventory and cave-state check.{/n}''', c('[Leave the lead unresolved until the game can verify the evidence.]', flags=f("native.pending"))),
], requires=("trickster", "terendelev.continuation.native_quest_verified", "terendelev.continuation.native_original_clue_verified", "terendelev.continuation.native_ravener_outcome_verified"), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_identity_review", "The part of her the scale cannot prove", "Memory", [
    n("start", "Terendelev", '''"I want to ask you something before we try another test," Terendelev says. "What exactly do you believe the voice in this scale proves?"

{n}You tell her that it proves only that a voice can answer through the scale. She asks you to bring a detail from a witness who knew her before the scale, and separately to establish what happened to the remains at Iz.{/n}

"Do not make me prove that I am myself by guessing what you want me to remember. Ask questions whose answers you can check without me."{/n}''',
      c("[Compare the bell keeper's dated record with the native account.]", "witness", flags=f("identity.witness_selected")),
      c('[Check the claw history against the independently recorded Iz outcome.]', "remains", flags=f("identity.remains_selected"))),
    n("witness", "Narrator", '''{n}The bell keeper's dated ledger confirms the rebuilt western face of the tower. Terendelev corrects the date from her own memory, and the public record supports her correction.{/n}

{n}This verifies continuity between the voice and a remembered detail checked outside the signal. It says nothing about the condition of the missing half.{/n}''', c('[Record this witness evidence, then check the remains history.]', "remains", flags=f("identity.witness_verified")), c('[Close with witness evidence only after the remains history was separately checked.]', "identity_summary", flags=f("identity.witness_verified"), requires=f("identity.remains_verified"))),
    n("remains", "Narrator", '''{n}The verified native clue history places the claw in the cave, and the verified encounter result records whether the Ravener died. These facts document the history of the divided remains; they do not prove that the voice contains every part of Terendelev.{/n}

"That tells us what happened to the fragments we can still document," Terendelev says. "It does not tell you that I am ready to become something else."{/n}''', c('[Record this remains evidence, then check the witness record.]', "witness", flags=f("identity.remains_verified")), c('[Close with remains evidence only after the witness record was separately checked.]', "identity_summary", flags=f("identity.remains_verified"), requires=f("identity.witness_verified"))),
    n("identity_summary", "Narrator", '''{n}You compare the two distinct records: a dated witness fact that supports continuity of identity, and a separately verified clue and encounter history about the remains. Neither substitutes for the other. Together, they still do not establish that her soul is complete or that a living return is possible.{/n}''', c('[Record the limited combined findings without claiming restoration.]', flags=f("identity.context.reviewed"), requires=f("identity.witness_verified", "identity.remains_verified"))),
], requires=BOUND + f("escape.accepted", "escape.test.observed") + ("trickster",), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_other_half_living", "The part of her still in the world", "Memory", [
    n("start", "Narrator", '''{n}The story's records point toward the Ravener at Iz. Terendelev's voice changes when you say its name.{/n}

"That is not just a monster carrying part of me," she says. "It is the part of me that was made to suffer and to hurt others. If it is still there, do not turn the Trickster's plan into an excuse to skip what Iz requires."

{n}You agree not to interrupt the native encounter, change its reward, or call an unfinished death a completed reunion. The people endangered by the Ravener remain part of the decision.{/n}

"If I am ever to meet the person I was before, I will have to face what that creature remembers. You cannot prepare me by hiding it."{/n}''',
      c('[Wait for the actual Iz encounter to resolve through its native rules.]', "wait", flags=f("other_half.waiting")),
      c('[Tell her the Trickster should force the boundary open before the Ravener can act.]', "danger", flags=f("other_half.proposed_override"))),
    n("wait", "Terendelev", '''"Thank you," she says. "Not for waiting. For understanding that waiting is the work right now."

{n}The message ends without a promise of reunion. Her voice is quieter than before, but not distant.{/n}

The investigation remains available after the native Iz encounter has a verified result. It will not change the encounter, its combat, or Galfrey's recorded history.{/n}''', c('[Close this conversation until the Iz result is known.]', flags=f("other_half.waiting"), abort=True)),
    n("danger", "Terendelev", '''"No," she says. "You are trying to solve my fear by making another choice for me, and the risk would fall on everyone near it. The Ravener is not a lock on a door I asked you to open."{/n}

{n}She will not continue the discussion that night. The scale stays where it is, but the boundary test is suspended until the Commander can present a plan that leaves the native encounter intact.{/n}''', c('[Withdraw the proposal and wait for the real encounter to resolve.]', "wait", flags=f("other_half.corrected"))),
], requires=(NATIVE_RAVENER_ALIVE, "trickster", "terendelev.continuation.identity.context.reviewed"), forbids=(PARENT_LICH_BIND, NATIVE_RAVENER_DEAD), remote=True)

add("trickster_other_half_dead", "What Iz does not return", "Memory", [
    n("start", "Terendelev", '''{n}The native record now marks the Ravener dead. You do not claim the victory as yours. The encounter has resolved through its own event and actions.{/n}

"I remember the anger," Terendelev says. "I do not know whether the death returned everything that was taken from me. A dead Ravener is not the same as a restored soul. A body is not the same as the person who lived in it."

{n}The record gives you an answer about the encounter, not about the afterlife. The surviving scale voice still needs to choose what she wants to do with the fact.{/n}''',
      c('[Ask her whether she wants to investigate the missing memories before any crossing.]', "memories", flags=f("other_half.native_death_known")),
      c('[Offer to leave the missing part unanswered if she chooses not to pursue it.]', "choice", flags=f("other_half.choice")),
      c("[Tell her the Ravener's death proves she can be whole now.]", "overclaim")),
    n("memories", "Terendelev", '''"I do," she says. "I also want the investigation to stop if it begins using the people that creature hurt as scenery for my recovery."

{n}You agree to keep the record of the Iz encounter and Galfrey's part in it intact. Any attempt to interpret the Ravener's memories must use a source that actually survives the battle. No collected scale, claw, oath, or parent ending can stand in for that evidence.{/n}

"I want to learn what is missing," she says. "I do not want to be told that someone else has already found it for me."{/n}''', c('[Record a new investigation objective without marking her soul reunited.]', flags=f("other_half.investigation", "other_half.reviewed"))),
    n("choice", "Terendelev", '''"Thank you," she says. "I do not know that I want to become whole in the way you mean. I want the choice to remain mine while I find out what happened."{/n}

{n}The Trickster can make that choice possible to ask. It cannot answer for her.{/n}''', c('[Leave the question open and preserve her separate identity.]', flags=f("other_half.reviewed"))),
    n("overclaim", "Terendelev", '''"It proves that the creature died," Terendelev says. "It does not prove that I have returned to a complete life."{/n}

{n}She asks you to correct the record before you continue. The other half may be gone, released, or changed. None of those possibilities is the same as being restored.{/n}''', c('[Retract the claim and keep the outcome unresolved.]', flags=f("other_half.corrected"))),
], requires=(NATIVE_RAVENER_DEAD, "trickster", "terendelev.continuation.identity.context.reviewed"), forbids=(PARENT_LICH_BIND, NATIVE_RAVENER_ALIVE), remote=True)

add("trickster_new_courtship", "A question she chooses to ask", "Memory", [
    n("start", "Terendelev", '''{n}The investigation has not produced an escape. It has established that the copied sky can change, and that the Commander stopped when Terendelev asked.{/n}

"I have been thinking about how we left things," she says. "I am not pretending the past answer did not happen. I am telling you that I have begun to wonder what I would choose now, with the memory of that conversation but none of its promises."{/n}

{n}She is careful not to call your investigation a payment.{/n}

"You did not earn this by succeeding. You could have done everything right and still heard no. I am asking because I want to ask."{/n}''',
      c('[Tell her you would like to begin again, slowly, without claiming the old relationship.]', "begin", flags=f("new.courtship.accepted")),
      c('[Ask for time to consider, and let her know the answer can be no.]', "later", flags=f("new.courtship.deferred")),
      c('[Decline and keep the investigation non-romantic.]', "friendship", flags=f("new.courtship.declined"))),
    n("begin", "Terendelev", '''"Then we begin with a question, not a vow," she says. "Would you like to tell me something true about yourself that you would not put in a proclamation? I will answer in kind."

{n}You speak about a decision you regret and the person who paid for it. Terendelev listens without absolving or condemning you. She says she is afraid of being remembered only as a sacrifice people have learned to use.{/n}

Neither confession buys the other's affection. They give you a reason to be honest when honesty becomes inconvenient.{/n}''', c('[Agree to meet again for a second conversation before either promises more.]', flags=f("new.courtship.open", "romance.confirmed"))),
    n("later", "Terendelev", '''"Of course," she says. "I have spent too long with choices other people called obvious. I will not ask you to make one quickly for my sake."

{n}She asks you to return to the investigation when you are ready and leaves the question of romance where she placed it: open, but unanswered.{/n}''', c('[Continue the investigation without treating delay as consent.]', flags=f("new.courtship.deferred"))),
    n("friendship", "Terendelev", '''"Thank you for telling me clearly," she says. "I am glad we can speak without turning every kindness into a test of desire."

{n}She does not sound wounded or relieved. The relationship remains a friendship, chosen by both of you. The investigation continues on its own terms.{/n}''', c('[Continue the investigation as friends.]', flags=f("new.courtship.declined"))),
], requires=BOUND + f("escape.accepted", "friendship.investigation", "identity.context.reviewed") + ("trickster",), forbids=(PARENT_LICH_BIND,), RequiresAny=["terendelev.continuation.bound_friendship_seen", "terendelev.continuation.bound_rejection_seen", "terendelev.continuation.bound_separation_seen"], remote=True)

add("escape_choice", "The cost of a possible door", "Memory", [
    n("start", "Narrator", '''{n}Terendelev has studied the crack in the replica's tower. She has also had time to decide that she does not want to be hurried by the possibility of escape.{/n}

"There may be a way through," she says. "The boundary moved when it encountered a fact it could not place. I do not know whether the opening leads outward or deeper into something else. I do not know whether I can cross it whole."

{n}She is quiet. The scale carries the sound of her breathing, not the wind around her.{/n}

"If I choose to try, I need you to hear the risks without turning them into a challenge. I might lose this fragment. I might meet the rest of myself and find that she does not want what I want. I might come out altered. I might not come out at all."{/n}''',
      c('[Proceed only after identifying the other soul fragment and a recoverable destination.]', "prerequisite", flags=f("escape.cautious")),
      c('[Support a crossing if she chooses it, even without certainty.]', "choice", flags=f("escape.open")),
      c('[Tell her the evidence is not yet enough and ask her to wait.]', "wait", flags=f("escape.wait"))),
    n("prerequisite", "Terendelev", '''"Yes," she says. "The Ravener is not a metaphor for my missing half. It is what happened to the rest of me. If it remains, we need to know where it is and what would happen if we brought the two halves together."

{n}She will not let the Trickster's cleverness erase the people harmed by the Ravener or the native quest that ended it. If the encounter is still available, she wants it resolved by its actual rules. If the remains are gone or the route can no longer be reached, the investigation must find a real witness and an implemented way to establish the soul's condition.{/n}

"I will not ask you to create a whole person from a convenient flag," she says. "Neither will I let you pretend the first step is the last."{/n}''', c('[Record that no crossing is authorized until the other half is accounted for.]', flags=f("escape.prerequisite.pending"))),
    n("choice", "Terendelev", '''"That is not an answer yet," she says. "I asked what you would support. I am asking whether you think I should do it."

{n}You tell her that the possibility matters, but the evidence is not a promise of safety. You can help her test the boundary and gather what is missing. You cannot make the risk disappear by calling it a trick.{/n}

"Good. I do not need you to be certain. I need you to be honest about where your certainty ends."{/n}''', c('[Leave the decision with her and continue only if she asks again.]', flags=f("escape.decision.her"))),
    n("wait", "Terendelev", '''"I agree," she says. "The crack is evidence, not an invitation."

{n}She is disappointed, and she does not hide it. She also does not punish you for refusing to rename uncertainty as courage.{/n}

"Bring me the information about the other half. Then I will decide again. Until then, I want to speak to you about something other than the door."{/n}''', c('[Continue the relationship through ordinary scale contact while the investigation waits.]', flags=f("escape.prerequisite.pending"))),
], requires=BOUND + f("escape.test.observed"), forbids=(PARENT_LICH_BIND,), delay=72, remote=True)

add("scale_evening", "A voice across the dark", "Memory", [
    n("start", "Terendelev", '''{n}The scale rests between you on the table. Terendelev's voice reaches you after a long pause.{/n}

"You have spent the last several meetings asking what I remember. Tonight I would like to ask what you miss."{/n}

{n}She does not ask for a performance of grief or a report of your sins. She wants to hear the answer because she still wants to know you, even from the other side of a boundary neither of you has solved.{/n}

"Do not give me the answer you think a hero ought to say," she adds. "I have heard enough of those to last several lives."{/n}''',
      c('[Tell her you miss the ordinary weight of her arm beside yours.]', "ordinary"),
      c('[Tell her you miss arguing when neither of you is trying to win.]', "argument"),
      c('[Tell her you miss the possibility of a future and fear what it costs her.]', "future")),
    n("ordinary", "Terendelev", '''"That is a small thing," she says. "It is also exactly the sort of thing I would miss."

{n}She asks you to describe the garden after rain. You describe the smell of stone and the cold metal of the fountain. She corrects you about the tree nearest the wall: it was a pear tree, not an apple. She says the fruit was terrible.{/n}

"When I return, if I return, I want to stand somewhere ordinary. I want to be annoyed by a bad meal and tired after a walk. I do not want every moment to become a ceremony because it might be the last one."{/n}''', c('[Promise to make room for ordinary days, without promising they will arrive.]', flags=f("intimacy.shared"))),
    n("argument", "Terendelev", '''"You miss losing arguments to me?" she asks.

{n}You tell her that you miss the moments when disagreement did not threaten the whole relationship. She laughs softly.{/n}

"We have never been as calm as you make us sound. But I understand. I do not want you to agree with me to protect the memory you have of me. If we ever meet again, you may tell me that I am wrong."{/n}

"You say that now."

"I am sure you will remind me later."{/n}''', c('[Tell her you want the real disagreement, not its remembered shape.]', flags=f("intimacy.shared"))),
    n("future", "Terendelev", '''"I fear it too," she says. "I will not tell you that love makes the danger noble. I am not a lesson about hope. I am a person in a place I did not choose, and I would like to leave it if I can do so without losing what remains of me."

{n}Her voice catches once, then steadies.{/n}

"There is still something I want. That does not make the risk worth any price. It means I want to be included when we decide what the price is."{/n}''', c('[Agree that her desire belongs in the decision alongside her fear.]', flags=f("intimacy.shared"))),
    n("end", "Terendelev", '''{n}The scale warms in your hand. Terendelev asks you to keep it beside you for a little longer. The dark between you does not close, but her voice no longer sounds quite so far away.{/n}

"I want to kiss you," she says, with a wry edge to her voice. "It is inconvenient that I cannot reach you. You may tell the Storyteller I am holding that against the laws of the world, not against you."{/n}

{n}You press your mouth to the scale. She laughs, and the sound travels through it like a breath against your lips.{/n}''', c('[End the call with the next investigation agreed, not the escape promised.]', flags=f("remote.chapter", "romance.confirmed"))),
 ], requires=BOUND + f("escape.accepted", "romance.confirmed", "new.courtship.open"), forbids=(PARENT_LICH_BIND,), delay=24, remote=True)

# Fail closed if any scale or memory scene is accidentally authored as physical contact.
REMOTE_SCENE_NAMES = {
    "scale_invitation", "escape_boundary", "trickster_friendship", "trickster_native_lead",
    "trickster_identity_review", "trickster_other_half_living", "trickster_other_half_dead",
    "trickster_new_courtship", "escape_choice", "scale_evening",
}
for _remote_name in REMOTE_SCENE_NAMES:
    _remote_scene = next(item for item in SCENES if item["Id"] == "terendelev.continuation." + _remote_name)
    if _remote_scene["Remote"] is not True or _remote_scene["ContactUnit"] is not None:
        raise ValueError("Scale/memory continuation must be remote without a physical contact unit: " + _remote_name)
_returned_scene = next(item for item in SCENES if item["Id"] == "terendelev.continuation.returned_letter")
if _returned_scene["Remote"] is not False or _returned_scene["ContactUnit"] != TERENDELEV_CONTACT or RETURNED_ACTOR_CONFIRMED not in _returned_scene["Requires"]:
    raise ValueError("Returned-person meeting requires the confirmed physical actor")
for _physical_scene in SCENES:
    if not _physical_scene["Remote"] and RETURNED_ACTOR_CONFIRMED not in _physical_scene["Requires"]:
        raise ValueError("Physical contact scene lacks confirmed actor delivery: " + _physical_scene["Id"])

# No escape or returned-contact scene is authored until the reviewed delivery service is integrated.
# Native living/dead encounter proofs, response state, and returned actor confirmation are unproduced contracts.


def integrate(payload):
    """Register reviewed-source candidates without registering their scenes in production."""
    for name, bindings in (("Etudes", ETUDES), ("CompletedQuests", COMPLETED_QUESTS), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(name, {})
        for key, value in bindings.items():
            if key in target and target[key] != value:
                raise ValueError("Conflicting Terendelev source binding: " + key)
            target[key] = deepcopy(value)
    relationships = payload.setdefault("Relationships", {})
    if "terendelev" in relationships and relationships["terendelev"] != RELATIONSHIP:
        raise ValueError("Conflicting Terendelev relationship registration")
    relationships["terendelev"] = deepcopy(RELATIONSHIP)
