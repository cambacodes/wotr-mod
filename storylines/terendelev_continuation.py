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
# eng7-f6d begin: dormant physical delivery uses the exact existing parent actor.
# Reuse never materializes an actor or grants the outstanding confirmation proof.
HUB = "terendelev.continuation.presence"
PRESENCES = {HUB: dict(Unit=TERENDELEV_CONTACT, Area=DREZEN, Mode="reuse-native",
    Requires=["terendelev.continuation.returned_actor_confirmed"],
    Forbids=["terendelev.continuation.closed", "terendelev.trickster.returned"],
    MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub")}
# eng7-f6d end

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
        requires=contact_requirements, forbids=tuple(forbids) + ("terendelev.continuation.closed", TRICKSTER_RETURNED),
        delay=delay, optional=True, Relationship="terendelev", Remote=remote,
        ContactUnit=None if remote else TERENDELEV_CONTACT,
        **({} if remote else dict(InteractionHub=HUB)),
        Areas=[DREZEN], Chapters=[5], **extra))


RETURNED = f("returned")
# The Trickster route (terendelev_trickster) brings her back by its own device; the two never both run.
TRICKSTER_RETURNED = "terendelev.trickster.returned"
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
    n("start", "Narrator", '{n}Terendelev passes you an unsealed letter in her careful hand.{/n} "Come to the lower garden after the evening bell. I want a walk, and I want your company. Leave the escort at the gate. Terendelev." {n}A silver trace marks the edge of the paper.{/n}',
      c('[Go to the garden at the appointed hour.]', "garden", flags=f("started", "returned", "invitation.accepted")),
      c('[Keep the letter, but do not accept tonight.]', "later", flags=f("started", "returned", "invitation.deferred")),
      c('[Decline the invitation.]', "decline", flags=f("closed"))),
    n("garden", "Terendelev", '{n}Terendelev waits beneath the bare branches, silver clasp bright at her throat. The evening bell sounds beyond the garden wall.{/n} "My return has not made you any less insufferable. The early evidence is quite firm." {n}She offers her arm.{/n} "I remember what we said before. I also remember being shut away while the world went on without me. Tonight I asked for a walk. Let us have one."',
      c('"Then let us walk until one of us improves the evidence."', "walk", flags=f("walk.accepted")),
      c('[Flirt] "I had hoped you would miss that part of me."', "walk", flags=f("walk.accepted")),
      c('"Show me where you want to go."', "walk", flags=f("walk.accepted"))),
    n("walk", "Terendelev", '{n}She takes the longer path round the dry fountain, her arm warm against yours.{/n} "I remember the stars at the end of the ritual. I had thought I would never see them without that darkness between us." {n}She stops beside the wall and turns to look at the lights of Drezen below.{/n} "Tomorrow they will want answers. Tonight I should like to speak to you without a roomful of people listening."',
      c('"I will come as your partner, not your spokesman."', "invitation", flags=f("civic.accepted")),
      c('"Only if you choose the place and the terms."', "invitation", flags=f("civic.accepted")),
      c('"I can come as your commander, but I will not put your name on my orders."', "invitation", flags=f("civic.accepted"))),
    n("invitation", "Terendelev", '"I shall choose the place for the meeting." {n}She takes your hand and runs her thumb across your palm. Her fingers close; she draws you nearer.{/n} "You are looking very solemn for someone I invited into a garden." {n}Her eyes settle on your mouth.{/n} "Come here."',
      c('[Kiss her.]', "kiss", flags=f("kiss.chosen")),
      c('[Draw her close.]', "kiss", flags=f("kiss.chosen")),
      c('[Keep walking.]', "deferred", flags=f("intimacy.deferred"))),
    n("kiss", "Terendelev", '{n}Her mouth is warm in the cold evening. She draws you close by the back of the neck, and when she lifts her head her fingers remain at your collar.{/n} "Not tonight. I want you to walk me to the gate." {n}She straightens the collar she has crumpled.{/n} "Tomorrow, Kenabres. Tonight, a little more of this."', c('[Walk her to the gate, and agree to hear the Kenabres petition together.]', flags=f("returned.chapter1", "romance.confirmed"))),
    n("later", "Narrator", '{n}You fold the letter and set it beside the lamp. The evening bell sounds outside.{/n}', c('[Leave the invitation open.]', abort=True)),
    n("deferred", "Terendelev", '"Then walk with me." {n}She takes your arm and turns toward the gate.{/n} "You can tell me what the builders have been asking for. I suspect I shall regret giving them the evening to think."', c('[Walk her to the gate and agree to hear the petition together.]', flags=f("returned.chapter1", "romance.confirmed"))),
    n("decline", "Narrator", '{n}You put the letter into the fire. Terendelev receives no answer. The next evening the garden bench is empty.{/n}', c('[Leave the garden empty.]', flags=f("closed"), abort=True)),
], requires=("terendelev.parent_romance", PARENT_QUEST, "terendelev.continuation.returned_finale_seen", RETURNED_ACTOR_CONFIRMED), forbids=("terendelev.parent_bound", "terendelev.parent_lich_bind", "terendelev.continuation.romance.refused"))

add("kenabres_petition", "A name used as a seal", "Terendelev", [
    n("start", "Terendelev", '''"The meeting is in a storehouse by the eastern wall," Terendelev says. "It belongs to a group of builders preparing a list of houses to clear before winter. They have used my name in their petition to the queen."

{n}She sets three documents on the table. The first is a public copy, polished and persuasive. The second is an inventory of households marked for removal. The third is a rough list of volunteers promised work after the clearances.{/n}

"I did not approve this. I did tell the organizers I would hear their proposal. That is not the same thing, but the petition has been written as if it were."

"What do you want from the meeting?"

"A chance to hear why they believe this is necessary. I want the families to know that my name is not an order. I want you to help me keep the disagreement about their plan, rather than about whether a dragon has the right to change her mind."''',
      c('[Compare the household list with the building assessments.]', "compare", check=dict(Skill="SkillKnowledgeWorld", DC=25, CommanderOnly=True, Success="compare", Failure="gap")),
      c('[Ask which households have already received notice.]', "notices"),
      c('[Ask Terendelev what she believes is at risk.]', "terms")),
    n("compare", "Narrator", '''{n}You compare the list of households against the building assessments. Three entries describe occupied homes as empty. One has a repair estimate copied from a neighboring property, and two addresses have been reversed. The pattern is not random enough to be a simple copying error.{/n}

{n}Terendelev reads the discrepancies without triumph. Her expression tightens when she reaches the name of a family whose roof she remembers seeing from the air. She does not mistake your discovery for proof of a conspiracy; she marks the entries to verify them with the residents.{/n}

"A useful question," she says. "Now we need to ask who benefits from the answer before we decide what it means."''', c('[Bring the discrepancies to the meeting and ask for the original records.]', "meeting", flags=f("evidence.records"))),
    n("gap", "Narrator", '''{n}The addresses do not align cleanly. One household has moved since the census, and the repair notes use a numbering system that has changed twice. You cannot call the entries false without inventing certainty.{/n}

{n}Terendelev does not punish you for the miss. She asks you to mark what is unknown, not what you would like the paper to say. A clerk who helped deliver notices has agreed to attend the meeting and explain how the lists were made.{/n}''', c('[Hear the clerk before drawing a conclusion.]', "meeting", flags=f("evidence.clerk"))),
    n("notices", "Terendelev", '''"Some have received notices. They were told an inspection would follow, not that they had to leave. Others heard the rumor in the market and have already begun packing."

{n}Terendelev folds the paper with care, keeping the names inside. She has memorized the street and household numbers, but does not recite them aloud.{/n}

"There is a difference between an official order and a threat delivered in the shape of one. We must not make that difference meaningless by treating every frightened person as if they should have read the law first."''', c('[Ask who wrote the notices and who delivered them.]', "meeting", flags=f("evidence.delivery"))),
    n("terms", "Terendelev", '''"The plan may be right about the danger and still wrong about who must bear it," she says. "The wall is unstable. The winter is near. A failed roof can kill a family as easily as a demon can. But I will not tell a mother that her home is expendable because the alternative is inconvenient to a committee."

{n}She looks at you directly.{/n}

"I want you to challenge me if I begin treating a remembered street as though it were unchanged. You were there during the attack. Your memory is not mine, and mine is not a map of every life that has continued without me."''', c('[Go to the meeting and listen before either of you argues.]', "meeting", flags=f("evidence.context"))),
    n("meeting", "Narrator", '''{n}The storehouse is crowded with people who came to dispute different things. Builders sit beside residents whose homes have been marked. A clerk guards a locked case of original assessments. At the far end, an organizer named Vennorik has arranged the chairs so that the petition's supporters face the door.{/n}

{n}Terendelev does not sit at the head of the room. She waits until the residents have found places and then stands beside you, not behind a lectern.{/n}

"I was told my name would persuade you to accept this plan," she says. "It cannot. I have not approved it. I am here to hear what danger you see and to learn what evidence you used."

{n}A resident interrupts Vennorik: her roof was listed as collapsed when she has been sleeping beneath it for three years. The room turns toward the two of you.{/n}''',
      c('[Let the resident explain before questioning Vennorik.]', "resident", flags=f("meeting.resident_first")),
      c('[Ask Vennorik to produce the original assessments now.]', "records", requires=f("evidence.records")),
      c('[Ask the clerk how notices became eviction rumors.]', "clerk", requires=f("evidence.clerk")),
      c('[Ask Terendelev to open with the limits of her own authority.]', "opening", flags=f("meeting.limits"))),
    n("resident", "Narrator", '''{n}The woman gives her name as Asla. She describes the roof, the repair she made with her brother, and the winter she spent sleeping in the back room because the front was unsafe. She does not ask for charity. She wants the inspection repeated by someone who understands the difference between a patched roof and an empty house.{/n}

{n}Terendelev listens without interrupting. When Asla finishes, the dragon asks what she would need to make the home safe before the first snow. The answer is lumber, two days of labor, and a stove pipe that does not leak.{/n}

"That is a plan we can assess," Terendelev says. "It is not the same as a promise that every house can remain."''', c('[Ask the committee to fund a second inspection and a repair estimate.]', "decision", flags=f("resident.heard"))),
    n("records", "Narrator", '''{n}Vennorik opens the case. The originals are not a single report, but a stack of notes from three inspections. One uses an obsolete street grid. Another records a dangerous foundation without stating that the house is empty. The third is missing the inspector's signature.{/n}

{n}No single page proves that Vennorik forged anything. Together they show that the petition's confident totals were assembled from records that cannot bear the weight put on them.{/n}

Terendelev asks Vennorik whether he knew the gaps were there. He admits that he did. He thought the danger of delay was greater than the harm of a few mistaken notices.''', c('[Require a public correction and a fresh inspection before any clearance.]', "decision", flags=f("records.opened"))),
    n("clerk", "Narrator", '''{n}The clerk says the notice was written to invite inspections. The courier who carried it told residents that inspectors would return with guards. He had been promised a paid position on the clearance crews if the petition passed.{/n}

{n}The clerk cannot say whether the courier invented the threat or repeated what he had heard from Vennorik. The evidence establishes a financial interest and a false rumor, not who first ordered it.{/n}

Terendelev asks for the courier's name and the dates of the deliveries. She will not call it a deliberate plot until residents can be questioned without the organizer present.''', c('[Separate the paid courier from the inspection plan and investigate both.]', "decision", flags=f("delivery.traced"))),
    n("opening", "Terendelev", '''"My name is not an order," Terendelev says. "I have not inspected these homes. I have not approved the numbers in this petition. I have agreed to hear the people who live here and the people who fear the wall will fail."

{n}She glances at the residents rather than the committee.{/n}

"If I am wrong about the danger, show me. If you are wrong about a home being empty, correct the list. We will not settle either question by asking which of us has the more impressive title."''', c('[Let the residents speak, then move to a documented decision.]', "decision", flags=f("meeting.limits"))),
    n("decision", "Terendelev", '''The room breaks into smaller arguments. Terendelev lets them run until the residents begin speaking to one another rather than waiting for a verdict from her.

"We have a choice," she says to you. "We can suspend the petition, repair the most urgent homes, and pay for new inspections. That costs time and money. We can authorize a smaller evacuation for houses independently found at immediate risk, with temporary lodging and a right to return. Or we can let the current committee proceed and promise that we will correct its mistakes later."

{n}She does not conceal which option she favors. She asks you to say what the evidence supports, not what will make her grateful.{/n}''',
      c('[Suspend the petition, fund repairs, and demand a fresh inspection.]', "pause", flags=f("decision.pause")),
      c('[Authorize verified immediate evacuations with lodging and return rights.]', "narrow", flags=f("decision.narrow")),
      c('[Let the committee proceed, but publish the errors and promise later review.]', "proceed", flags=f("decision.proceed"))),
    n("pause", "Narrator", '''{n}The petition is suspended pending a new inspection. The cost will come from funds reserved for the rebuilding committee, and the builders complain that delay could leave unstable homes in place.{/n}

{n}Terendelev does not call the decision righteous simply because it resembles her preference. She asks for a schedule, a named inspector, and a public list of what will count as immediate danger. The residents choose two observers to accompany the review.{/n}

{n}When the room empties, she turns to you.{/n}

"You did not rescue them for me. You made the plan answerable to them. I am glad you came."''', c('[Leave the repair plan in their hands and walk Terendelev home.]', flags=f("civic.resolved", "civic.pause"))),
    n("narrow", "Narrator", '''{n}The committee agrees to inspect each house again. Two buildings with visibly failing supports will be evacuated that night; their residents receive rooms nearby and written permission to return after repairs. The other homes remain occupied until their inspection is complete.{/n}

{n}Terendelev makes the limits plain. If the second inspection finds another immediate danger, there may be another evacuation. No one is promised that a loved home is safe simply because leaving it would hurt.{/n}

{n}She waits while the residents read the terms aloud and correct the location of the temporary rooms.{/n}

"It is not a perfect answer," she says after the meeting. "It is an answer people can challenge while there is still time to change it."''', c('[Walk her home without calling the compromise a victory.]', flags=f("civic.resolved", "civic.narrow"))),
    n("proceed", "Narrator", '''{n}The committee continues with its original schedule. Your promise of later review is entered into the minutes, but the residents leave without a date for that review. Terendelev does not argue in the room. She waits until the door has shut.{/n}

"You have left the burden with the people who have the least power to force us to keep our promise," she says. Her voice is quiet, not forgiving.

"You may be right that delay is dangerous. But do not ask me to call an unkept promise a compromise."''', c('[Accept her judgment and commit to securing a dated review.]', "repair", flags=f("civic.proceed")), c('[Defend the decision and let the disagreement stand.]', "repair", flags=f("civic.proceed"))),
    n("repair", "Terendelev", '''{n}You do not erase the decision by regretting it. Terendelev asks the committee to name a review date and give the residents copies of the inspection records. Some support her. Others say a public challenge will scare workers away.{/n}

She looks to you once, giving you the chance to speak. If you accept responsibility, she asks you to say what you will do and when. If you defend the choice, she tells the room she disagrees and will not use her return to lend it authority.

{n}The work continues with less trust than it might have had. Terendelev walks back to the keep beside you, but the silence between you takes effort to cross.{/n}''', c('[Ask what she needs from you now, then listen without demanding reassurance.]', flags=f("civic.resolved", "civic.cost"))),
], requires=RETURNED + f("returned.chapter1", "civic.accepted"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=36)

add("private_oath", "An oath with room to breathe", "Terendelev", [
    n("start", "Terendelev", '{n}Terendelev lays a plain silver cord on the garden bench. Beyond the wall a sentry calls the watch.{/n} "I remember being a voice you could hear and a monster you could not reach. Now I can stand beside you. I want to swear this oath where you can see my face."',
      c('"What should I remember when I see it?"', "meaning"),
      c('"Kenabres will still need you."', "duty"),
      c('[Flirt] "I want you here tonight."', "desire")),
    n("meaning", "Terendelev", '"Tie it where you will see it." {n}She gives you one end of the cord.{/n} "If you find me difficult, remember that you heard the oath before you tied the knot."', c('[Take the cord.]', "oath", flags=f("oath.considered"))),
    n("duty", "Terendelev", '"Kenabres will call for me. I will go when it does. There are people there who were mine before I knew your name." {n}She touches your wrist.{/n} "I shall come back to you. That is the promise I can make."', c('"I shall watch for your return."', "oath", flags=f("oath.considered"))),
    n("desire", "Terendelev", '"I want you." {n}Her fingers tighten over yours.{/n} "I have spent enough nights being remembered. Tonight I should like to be touched."', c('[Kiss her.]', "oath", flags=f("oath.considered"))),
    n("oath", "Terendelev", '{n}She ties the cord round her wrist and places the other end in your hand.{/n} "I will not forget the people I guarded. I will not forget you when I go to them. So I swear, Terendelev of Kenabres." {n}She kisses you before the knot is finished. Her hand finds the fastening of your coat; she works it loose, then draws your shirt open and presses her mouth to the skin beneath. You lift her clasp. Silver falls into your palm, and her collar slips from her shoulder. She takes your hand under the loosened cloth and pulls you against her, breath hot at your ear.{/n} "Inside. I have had enough of the evening wind."', c('[Go inside with her.]', "threshold")),
    n("threshold", "Narrator", "{n}She sets the cord on the table without looking at it. Her clothes fall beside your coat. She turns back to you, bare shoulders silver in the lamp's light, and pulls you down onto the coverlet. Her thigh presses along yours; her kiss loses its measured pace. As she draws you over her, the lamp goes dark.{/n}", c("[Stay with her.]", "oath_dawn", flags=f("oath.made", "returned.chapter2", "romance.confirmed"))),
    n("oath_dawn", "Terendelev", '{n}The watch changes outside. Terendelev lies beside you, the silver cord loose round her wrist and a crease from the coverlet across her shoulder. She opens her eyes when you touch it.{/n} "You are awake. Good. I have no intention of facing breakfast alone after keeping the kitchen waiting." {n}She kisses you, then reaches reluctantly for her shirt.{/n}', c("[Rise with her.]")),
], requires=RETURNED + f("civic.resolved", "romance.confirmed"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=48)

add("inspection_day", "The second inspection", "Terendelev", [
    n("start", "Terendelev", '''{n}The inspection takes place over two days. Terendelev asks you to come for the second, when the residents' observers will be present and the builders can no longer claim the earlier mistakes were only clerical.{/n}

{n}A mason taps the lintel of Asla's house and listens. The sound is hollow in one corner. The roof is not collapsed, but the beam has split where an old repair concealed water damage.{/n}

"The list was wrong about the house being empty," Terendelev says. "It was not wrong to call it dangerous. Both facts matter."

{n}Asla looks from the beam to the room she has lived in. She asks how long she will be expected to leave, who will pay for the repair, and whether anyone can promise she will be allowed back.{/n}

Terendelev does not answer before the builders do.''',
      c('[Ask for a temporary room near the house and a written right of return.]', "lodging", flags=f("inspection.lodging")),
      c('[Ask the residents to choose which repair should be funded first.]', "residents", flags=f("inspection.residents")),
      c('[Insist that the builders state what they know and what is still uncertain.]', "uncertainty", flags=f("inspection.uncertainty"))),
    n("lodging", "Narrator", '''{n}The nearest available lodging is across the market square. Asla says she can manage it if her brother can carry the furniture and if the stove is moved before the roof is opened.{/n}

{n}The builders agree to put the return date in writing after the repair inspection. They cannot promise the work will be finished before the next storm, but they can promise to keep the rooms available and to tell the family when the plan changes.{/n}

Terendelev asks Asla to read the written terms back to the builders. The phrasing is plain enough to expose what the committee has not agreed to pay.''', c('[Make the missing labor and lodging cost part of the public schedule.]', "end", flags=f("inspection.outcome.lodging"))),
    n("residents", "Narrator", '''{n}The residents choose two repairs to fund first. A widow with a leaking roof votes for the foundation work because the house beside hers leans toward her wall. She has been waiting for someone to call her concern more than a private inconvenience.{/n}

{n}The committee's builders object that their own order is safer. Terendelev asks them to show the load calculations. She does not announce that the residents are right before she has read them.{/n}

The figures explain why the foundation should be stabilized before new roofing begins. The first schedule was written for speed, not safety.''', c('[Reorder the work and let the residents monitor the schedule.]', "end", flags=f("inspection.outcome.residents"))),
    n("uncertainty", "Narrator", '''{n}The builders admit that they have not opened the wall. Until they do, no one can say whether the beam can be reinforced or whether the roof must be removed entirely.{/n}

{n}Terendelev asks them to record that uncertainty. She is willing to evacuate a household for a night if the exposed beam gives way. She will not tell the family the house is safe because a confident answer would be easier to hear.{/n}

The residents ask for an observer to remain through the first cut. The builders accept after the committee agrees to pay for the extra day.''', c('[Approve the inspection with a named observer and a stop-work rule.]', "end", flags=f("inspection.outcome.uncertain"))),
    n("end", "Terendelev", '''{n}By dusk, the residents have copies of the revised schedule. It names who will pay for lodging, what work begins first, and when the next inspection will occur.{/n}

Terendelev watches the last family carry a small stove across the square. She does not call the outcome a victory. One home may still need to be rebuilt, and the people who have left it do not know when they will return.

"I wanted to save them from the order," she says. "We have instead made the order answerable. That is less beautiful and more useful."

{n}She looks at you with a tired smile.{/n}

"I am glad you did not make me thank you for agreeing with me. I want to thank you for staying when the answer became inconvenient."''', c('[Walk with her through the market before returning to the keep.]', flags=f("inspection.complete", "romance.confirmed"))),
], requires=RETURNED + f("civic.resolved", "returned.chapter1"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=48)

add("windward_evening", "The height she chooses", "Terendelev", [
    n("start", "Terendelev", '{n}The wind runs along Drezen\'s parapet. Terendelev stands by the low wall, hair loose, collar unfastened. The city\'s lights lie below.{/n} "There was a hill above Kenabres where I used to stand like this. I wanted the wind tonight. Stay here with me."',
      c('"What do you miss about flight?"', "memory"),
      c('"I wish I could have seen Kenabres from above."', "shared"),
      c('[Draw closer.]', "touch")),
    n("memory", "Terendelev", '"The air under my wings. The moment I could stop beating them and let it hold me." {n}She runs her fingers along the stone.{/n} "I miss knowing what my body can do. Tonight I am beginning to find out."', c('[Stand beside her.]', "height", flags=f("flight.shared"))),
    n("shared", "Terendelev", '"You would have seen roofs, crusader. Very small roofs, and smoke from the chimneys." {n}She smiles.{/n} "I liked it better when I landed and someone opened a door. I could smell the bread from the hill, but I could not eat it there."', c('[Stand beside her.]', "height", flags=f("flight.shared"))),
    n("touch", "Terendelev", '{n}She sets your hand at her waist and kisses the inside of your wrist.{/n} "You look at me as though I might vanish. I am here." {n}She draws your palm against her through the cloth.{/n} "I should like you to make rather more of that."', c('[Tell her the choice of shape is hers, and ask what she wants tonight.]', "height", flags=f("touch.chosen"))),
    n("height", "Terendelev", '{n}She takes your hand and leads you along the parapet. Wind pulls at her open collar. She stops close enough for her hip to touch yours.{/n} "I came up here to look at the city. It is difficult to keep looking at it with you standing there."',
      c('[Ask her to fly with you.]', "ask", flags=f("flight.requested")),
      c('[Draw her into your arms.]', "human", flags=f("flight.deferred"))),
    n("ask", "Terendelev", '"Not tonight. I am tired, and I do not want to spend this evening forcing a shape." {n}She slides both hands behind your neck and kisses you until the wind feels cold against your heated face.{/n} "I came here for your company. I am finding it very satisfactory."', c('[Stay with her.]', "close", flags=f("flight.trust"))),
    n("human", "Terendelev", '{n}She presses close, her hand firm at your back. Her mouth moves from your lips to your throat. When she lifts her head she is smiling.{/n} "There. You have found something to do without wings."', c('[Stay with her.]', "close", flags=f("flight.trust"))),
    n("close", "Terendelev", '{n}She takes your hand from her waist and puts it at the fastening of her collar. Her shirt slips from her shoulders. Your coat lies against the wall; she draws you down into its shelter and kisses you. The rest of the fastenings yield under impatient fingers. She presses her bare body against yours, the wind caught in her loose hair, and her breath quickens under your mouth. She folds a leg over yours and pulls you closer.{/n} "Stay." {n}The city lights disappear behind her shoulder as she draws you down.{/n}', c('[Stay until morning.]', flags=f("intimacy.adult", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=72)

add("kenabres_vigil", "The names that survived her", "Terendelev", [
    n("start", "Narrator", '''{n}The petition's work has slowed long enough for the residents to invite Terendelev to a small vigil. They plan to read the names of people lost in the attack, then the names of people who returned to rebuild.{/n}

{n}The invitation asks her to speak. It does not ask what she can do for the city. She reads it twice before accepting.{/n}

"I know some of these names," she says. "I do not know the people they became while I was gone. I will not pretend that memory gives me the right to speak for them."

{n}She asks you to attend beside her, but not to stand between her and the families. The event is a narrated book memory of a later evening in Kenabres; the scene does not teleport either of you or create a native city-state change.{/n}''',
      c('[Ask whether she would rather speak briefly or read names with the residents.]', "choice"),
      c('[Offer to tell the organizers she will not speak for anyone who has not asked.]', "terms"),
      c('[Ask what she wants you to do if someone blames her for surviving.]', "blame")),
    n("choice", "Terendelev", '''"I want to read the names with them," she says. "A speech would make the evening about my return. Reading together lets me be one of the people who remembers, and one of the people who has to listen."

{n}She chooses a place in the second row. When a family asks whether she remembers their son, she says she remembers the street, but not the boy. She does not invent a comforting detail to close the silence.{/n}

The mother thanks her for answering honestly and continues with the next name.''', c('[Stay beside her without answering for her.]', "end", flags=f("vigil.honest"))),
    n("terms", "Terendelev", '''"Tell them I will come as myself," she says. "If they want a speaker, they can ask someone who knows what happened after I died. I will not make the word survivor carry more than it can."

{n}The organizer accepts the limit. One committee member complains that a quiet vigil cannot become a public statement. Terendelev tells him that remembrance is not a petition and does not need to produce a decision.{/n}

She looks to you, checking that you will not use the moment to endorse the rebuilding plan.''', c('[Agree that the vigil should remain separate from the petition.]', "end", flags=f("vigil.separate"))),
    n("blame", "Terendelev", '''"You will let me answer for myself," she says. "If I ask you to stay, stay. If I ask you to leave, leave. I do not want you to defend my survival as if it were an argument I have to win."

{n}She squeezes your hand once, then lets go before anyone can read it as a public declaration.{/n}

At the vigil, an old man says she should have died with the others. Terendelev does not answer immediately. When she does, she says she knows why he wants a reason that fits the loss. She cannot give him one.''', c('[Let the silence remain before the next family reads.]', "end", flags=f("vigil.silence"))),
    n("end", "Terendelev", '''{n}After the last name, Terendelev stays to help fold the chairs. No one makes a speech about her courage. No one asks her to bless a plan.{/n}

She walks with you through the square, where the lamps have been lit in a line that leaves no one in darkness. Her shoulder brushes yours once; she does not take your hand until the crowd has thinned.

"That was difficult," she says.

"Do you want to do it again?"

"I want to remember that I can choose it. I do not yet know when I will want to."

{n}She leans against you for a moment, then stands straight again.{/n}''', c('[Offer comfort without asking her to turn the vigil into a promise.]', flags=f("vigil.complete", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=96)

add("private_aftercare", "The morning after choosing", "Terendelev", [
    n("start", "Terendelev", '{n}Terendelev is awake beside you. Her hair is tangled, and the collar of the shirt she has pulled on is uneven.{/n} "The kitchen bell. Again. I ignored it the first time." {n}She touches your bare shoulder.{/n} "I am considering ignoring it twice."',
      c('[Kiss her shoulder.]', "desire"),
      c('"Was the coat comfortable enough?"', "checkin"),
      c('"I want another morning with you."', "time")),
    n("desire", "Terendelev", '{n}She kisses your shoulder, then sits up with a reluctant sigh.{/n} "I wanted you last night. I still do. But if I keep those accounts waiting, the builders will decide I have died again and make free with the stone."', c('[Let her get dressed.]', "end", flags=f("aftercare.desire"))),
    n("checkin", "Terendelev", '"My shoulder aches. You put your coat over a stone, crusader, and then made me forget the stone." {n}She turns to show you the small bruise, then catches your hand at her waist.{/n} "Next time, fold it twice."', c('[Kiss the bruised shoulder.]', "end", flags=f("aftercare.checkin"))),
    n("time", "Terendelev", '{n}She takes the loose silver cord from the table and winds it round her fingers.{/n} "The inspection accounts are waiting. I should like another morning like this when I have finished with them."', c('"I shall watch for you."', "end", flags=f("aftercare.time"))),
    n("end", "Terendelev", '{n}She fastens her shirt and leaves the top clasp open. At the door she comes back to kiss you, one hand spread against your chest.{/n} "Bring breakfast if you come to read the accounts. I shall be in a foul temper on an empty stomach."', c('[Go with her, as her partner and not her keeper.]', flags=f("aftercare.complete", "romance.confirmed"))),
], requires=RETURNED + f("inspection.complete", "oath.made", "intimacy.adult"), forbids=(PARENT_BOUND, PARENT_LICH_BIND), delay=24)

# Trickster route: investigation and consent, not an automatic escape or resurrection.
add("scale_invitation", "The copy that remembers the wrong sky", "Memory", [
    n("start", "Narrator", '''{n}The scale grows cold in your palm. The voice comes through with the familiar restraint of someone who has learned that being heard is not the same thing as being safe.{/n}

"I have found something wrong with this place. Not with the memory inside it. With the edge between that memory and the rest of the world."

{n}Terendelev describes the replica Kenabres. Its buildings are drawn from remembered streets, but the sky does not move. She has counted the shadow of the bell tower for what feels like three afternoons; it remains fixed at the same angle.{/n}

"I know what you did when fate insisted there was only one ending. That is not why I am asking you to come. I am asking because you know how to look for the seam in a rule. If you find one, you will tell me what crossing it costs before you ask me to choose."''',
      c('[Accept the investigation, with no promise of escape or romance.]', "accept", flags=f("started", "bound", "escape.accepted")),
      c('[Help only if the plan leaves her able to refuse.]', "accept", flags=f("started", "bound", "escape.accepted", "escape.consent")),
      c('[Decline to interfere with the scale prison.]', "decline", flags=f("bound", "escape.declined"))),
    n("accept", "Narrator", "{n}You will compare a living resident's account of the tower with an older clue: the claw, if you still have it, or the Storyteller's account of the voice he heard. Neither account establishes a way out.{/n}",
      c('[Begin with the claw, if it remains in your possession.]', "claw", requires=f("claw.possessed")),
      c('[Begin with a dated account from a living Kenabres witness.]', "witness", flags=f("evidence.witness")),
      c("[Review the Storyteller's account of her voice.]", "storyteller", flags=f("evidence.storyteller"))),
    n("claw", "Narrator", '{n}You set the claw beside the scale. The record of its discovery names the cave at Leper\'s Smile. You compare it with the account of her burning remains at Iz. The claw says nothing about what may cross from the copy.{/n} "Keep that beside the witness\'s account," {n}Terendelev says.{/n} "I should like to hear both."', c('[Record this as one clue, not a guarantee.]', "witness", flags=f("evidence.claw"))),
    n("witness", "Narrator", '''{n}The witness is a bell keeper who survived the first night of the attack. Her ledger records the bells she rang and the shadows that crossed the square. She remembers the tower's broken west face, now rebuilt with a different stone.{/n}

{n}You ask for the present description, not a story of Terendelev. The witness describes the new roof, the repairs, and the names of the people who replaced it. This gives you a fact that the old replica city could not have witnessed when it was made.{/n}

{n}The memory within the scale has the same tower, the old stone, and the same unchanging shadow. It does not answer whether a boundary can carry a person.{/n}''', c('[Carry the dated observation to the scale and record both versions.]', "compare", flags=f("evidence.witness"), requires=f("evidence.claw")),
      c('[Carry the dated observation to the scale and record both versions.]', "compare", flags=f("evidence.witness"), requires=f("evidence.storyteller"), forbids=f("evidence.claw")),
      c('[Check the other account before comparing.]', "accept", flags=f("evidence.witness"), forbids=f("evidence.claw", "evidence.storyteller"))),
    n("storyteller", "Narrator", '{n}You go over the Storyteller\'s account: a voice in pain, in darkness it could not escape. He could not explain it. You write that beside the clue, without adding a location.{/n} "I remember the darkness," {n}Terendelev says.{/n} "He heard me. I did not know it."', c('[Write down the limit as carefully as the clue.]', "witness", flags=f("evidence.storyteller"))),
    n("compare", "Narrator", '{n}You set the bell keeper\'s account beside the description from the scale. New stone outside; old stone within. The fixed shadow has not changed. The difference can be tested without asking Terendelev to cross anything.{/n} "Send the account," {n}she says.{/n} "Then tell me what changed. Do not call it a door before we have seen one."',
      c('[Use Knowledge: Arcana to identify the scale’s boundary rule.]', "rule", check=dict(Skill="SkillKnowledgeArcana", DC=28, CommanderOnly=True, Success="rule", Failure="uncertain")),
      c('[Use Knowledge: World to test the tower record against the altered city.]', "rule", check=dict(Skill="SkillKnowledgeWorld", DC=28, CommanderOnly=True, Success="rule", Failure="uncertain")),
      c('[Repeat the comparison with a second resident before making a theory.]', "second", flags=f("evidence.second"))),
    n("rule", "Narrator", '{n}The fixed shadow and false sky suggest that the copy keeps repeating the same remembered day. You propose sending a dated account of the tower\'s repairs through the scale and watching whether anything changes.{/n} "Send the account," {n}Terendelev says.{/n} "I shall watch the tower. Do not attempt anything else yet."', c('[Propose a nonliving test and report the result before any crossing.]', flags=f("escape.theory", "escape.test.authorized"))),
    n("uncertain", "Narrator", '{n}You cannot tell what keeps the shadow fixed. Terendelev listens to your explanation, then asks for another account of the tower.{/n} "The second witness may have seen something the first missed. Bring me both accounts."', c('[Gather a second independent account before continuing.]', flags=f("escape.more_evidence"))),
    n("second", "Narrator", '{n}A second resident describes the tower\'s repairs from another street. Her account agrees with the bell keeper\'s about the new stone and differs about the weather. You record both, including the disagreement.{/n} "Now ask the place what it makes of them," {n}Terendelev says.{/n}', c('[Ask her to choose whether to test the boundary further.]', flags=f("escape.theory", "escape.test.authorized"))),
    n("decline", "Narrator", '''{n}You do not ask the scale to answer. Terendelev's voice remains quiet.{/n}

"I am disappointed," she says. "I would have liked to know whether there was another way out. I am not angry that you declined to gamble with what remains of me."

{n}No escape has been attempted, and no new promise has been made. The scale stays what it was: a channel for contact, not proof that a living return is possible.{/n}''', c('[End the investigation without changing her confinement.]', flags=f("closed"), abort=True)),
], requires=(PARENT_QUEST, PARENT_BOUND, "trickster", "terendelev.continuation.bound_finale_seen"), forbids=(PARENT_LICH_BIND, "terendelev.continuation.escape.declined"), remote=True)

add("escape_boundary", "A rule that can be tested", "Memory", [
    n("start", "Narrator", '''{n}The next time you speak through the scale, Terendelev begins with the question you left unanswered: what can be tested without making her the test?{/n}

{n}You have arranged a small change to the replica: a dated description of the rebuilt tower, carried into the memory by the same channel used for ordinary contact. No spell will be cast on her. No demand will be made of the people in the copy. The experiment can be stopped if the city begins to distort.{/n}

"I want to see what happens when this place learns something new," {n}she says.{/n} "I do not want to find out by watching someone else suffer for it."''',
      c('[Introduce the new description and ask her to compare it with the tower.]', "result_pending", flags=f("escape.test.requested"), requires=f("escape.theory", "escape.test.authorized"), forbids=f("escape.test.requested")),
      c('[Delay until another witness can confirm the record.]', "wait", flags=f("escape.test.wait")),
      # eng7-f6d: reopen the pending request without issuing a second test.
      c('[Check whether the test result has arrived.]', "result_pending", requires=f("escape.test.requested"))),
    n("result_pending", "Narrator", '{n}The dated account has been sent. You wait for word of what happened to the tower.{/n} "Nothing further yet," {n}Terendelev says through the scale.{/n} "Let us learn what the account did first."',
      c('[Read the report of a change.]', "changed", requires=f("boundary.result.changed")),
      c('[Read the unchanged report.]', "unchanged", requires=f("boundary.result.unchanged")),
      c('[Read the report of the failed attempt.]', "unsafe", requires=f("boundary.result.unsafe")),
      # eng7-f6d: absence of an observer result must leave a selectable wait.
      c('[Wait for word.]', abort=True)),
    n("changed", "Narrator", '{n}The report records a change in the copy after the account arrived. You compare its details with Terendelev\'s observations.{/n} "Something changed. I am still here," {n}she says.{/n} "Tell me what you think it means."', c('[Record the limited result and continue only with her agreement.]', flags=f("escape.test.observed", "boundary.result.recorded"))),
    n("unchanged", "Narrator", '{n}The report describes the same tower, sky and shadow. You read it twice. Terendelev is silent until you finish.{/n} "No change, then. I had hoped for better. Keep the account; we may need it again."', c('[Record no change and ask whether she wants another evidence visit or to stop.]', flags=f("boundary.result.recorded", "escape.test.no_change"))),
    n("unsafe", "Narrator", '{n}The report describes the copy losing its shape before the attempt was stopped. No further account is sent.{/n} "Not again," {n}Terendelev says through the scale.{/n} "Find out what happened before you send anything else."', c('[End the boundary experiment and preserve her refusal to continue.]', flags=f("boundary.result.recorded", "escape.test.unsafe_stop", "closed"), abort=True)),
    n("wait", "Narrator", "{n}You arrange another witness's account. Until it arrives you do not send the test. Terendelev asks you to bring the record when you next speak.{/n}", c('[Return to the scale with the corroborated record.]', abort=True, flags=f("escape.theory", "escape.test.authorized"))),
], requires=BOUND + f("escape.accepted"), forbids=(PARENT_LICH_BIND,), delay=48, remote=True)

# The parent-ending branches below offer investigation, not inherited romance.
add("trickster_friendship", "A conversation without courtship", "Memory", [
    n("start", "Terendelev", '"I remember my answer. It has not changed." {n}Her voice is steady through the scale.{/n} "I can still hear what you have learned about this place. If that is why you have come, tell me."',
      c('"I brought the investigation\'s records."', "evidence", flags=f("friendship.respected")),
      c('[Ask whether she might change her mind if you succeed.]', "boundary"),
      c('[Withdraw the offer and leave the channel quiet.]', "withdraw", flags=f("friendship.withdrawn"))),
    n("evidence", "Terendelev", '"Tell me what you have found." {n}You lay out the investigation\'s records, keeping observations apart from guesses. The question of escape remains unanswered.{/n} "Then keep looking. I can speak to you while you do. I have no wish to spend every conversation waiting for a door."', c('[Continue only with the investigation she chooses.]', flags=f("friendship.investigation"))),
    n("boundary", "Terendelev", '"No. I did not offer my affection as a prize." {n}The scale cools beneath your fingers.{/n} "Have you brought anything about the tower? I will hear that."', c('[Show her the records.]', "evidence", flags=f("friendship.repaired")), c('[End the investigation without another message.]', "withdraw", flags=f("friendship.withdrawn"))),
    n("withdraw", "Narrator", "{n}You set the scale down. Her voice falls silent. You put the investigation's records away beside it.{/n}", c('[Close this approach.]', flags=f("closed"), abort=True)),
], requires=BOUND + f("escape.accepted") + ("trickster", "terendelev.continuation.bound_nonromance_seen"), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_native_lead", "A name without a scale", "Memory", [
    n("start", "Narrator", '''{n}You have never spoken with Terendelev through the silver scale. The Trickster's investigation begins with two records instead: the Storyteller's account of searching for her after Kenabres fell, and the claw the native quest placed in the Swarm cave.{/n}

{n}The claw is a remnant, not a person, a soul-vessel, or permission to summon her. The Storyteller's memory describes a search and a hope, not proof that the same path remains open.{/n}

You can revisit the cave only if the original native collectible and its action are still available. If it has already been collected, the actual inventory must establish whether the item remains. The story must not grant a replacement claw because the investigation needs one.

"If you mean to change a fate," the Storyteller says, "begin by learning which pieces of it you still possess."''',
      c('[Ask the Storyteller to prepare the signal and send one invitation.]', "prepare", requires=("terendelev.continuation.native_quest_verified", "terendelev.continuation.native_original_clue_verified", "terendelev.continuation.native_ravener_outcome_verified")),
      c('[Decline to spend the clue or favor and leave contact unopened.]', "wait", flags=f("native.pending"))),
    n("prepare", "Narrator", '''{n}The Storyteller sets the verified clue beside a page of his notes. The memory-signal will carry only an invitation: Terendelev may answer, refuse, or remain silent. It does not claim that the claw contains her soul, that the Storyteller can find her, or that the Trickster can restore her.{/n}

{n}The signal costs the claw if it is still held. If it is absent, the Storyteller instead spends a unique favor he cannot offer again. This authored cost, the signal, and its response are not implemented by this manuscript.{/n}

{n}The registered caller must verify the cost, persist the one-use attempt, and wait for an explicit voluntary answer. Until that caller and response handler exist, this page cannot appear in game.{/n}''', c('[Send the single invitation only after the registered handler is installed.]', flags=f("native.invitation.requested"))),
    n("wait", "Narrator", '''{n}You do not guess. The scale may have been consumed, and the claw may have been collected, lost, or never touched. Each possibility means something different.{/n}

{n}The native quest record remains intact while the investigation waits for a live inventory and cave-state check.{/n}''', c('[Leave the lead unresolved until the game can verify the evidence.]', abort=True, flags=f("native.pending"))),
], requires=("trickster", "terendelev.continuation.native_quest_verified", "terendelev.continuation.native_original_clue_verified", "terendelev.continuation.native_ravener_outcome_verified"), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_identity_review", "The part of her the scale cannot prove", "Memory", [
    n("start", "Terendelev", '''"I want to ask you something before we try another test," Terendelev says. "What exactly do you believe the voice in this scale proves?"

{n}You tell her that it proves only that a voice can answer through the scale. She asks you to bring a detail from a witness who knew her before the scale, and separately to establish what happened to the remains at Iz.{/n}

"Do not make me prove that I am myself by guessing what you want me to remember. Ask questions whose answers you can check without me."''',
      c("[Compare her recollection with the bell keeper's old register.]", "witness", flags=f("identity.witness_selected")),
      c('[Check the claw history against the independently recorded Iz outcome.]', "remains", flags=f("identity.remains_selected"))),
    n("witness", "Narrator", '{n}You ask who hung the highest festival ribbon before reading the bell keeper\'s old register to her.{/n} "I did. Blue, every year. She always gave me the long end and charged for the short one. I never told her." {n}The pre-attack account records a blue ribbon raised by Terendelev herself. The rebuilding date sent during the experiment is not used in this comparison. The agreement supports one old recollection. It does not prove that the voice is whole.{/n}', c('[Record this witness evidence, then check the remains history.]', "remains", flags=f("identity.witness_verified")), c('[Close with witness evidence only after the remains history was separately checked.]', "identity_summary", flags=f("identity.witness_verified"), requires=f("identity.remains_verified"))),
    n("remains", "Narrator", '{n}You compare the recorded find at Leper\'s Smile with the reports of the ravener at Iz. The records concern her remains. The voice in the scale has not accounted for all that happened to them.{/n} "That is where the bones were," {n}Terendelev says.{/n} "I still do not know what became of the rest of me."', c('[Record this remains evidence, then check the witness record.]', "witness", flags=f("identity.remains_verified")), c('[Close with remains evidence only after the witness record was separately checked.]', "identity_summary", flags=f("identity.remains_verified"), requires=f("identity.witness_verified"))),
    n("identity_summary", "Narrator", '{n}One old recollection is corroborated. The remains have their own recorded history. Neither tells you whether a living return is possible.{/n}', c('[Record the limited combined findings without claiming restoration.]', flags=f("identity.context.reviewed"), requires=f("identity.witness_verified", "identity.remains_verified"))),
], requires=BOUND + f("escape.accepted", "escape.test.observed") + ("trickster",), forbids=(PARENT_LICH_BIND,), remote=True)

add("trickster_other_half_living", "The part of her still in the world", "Memory", [
    n("start", "Narrator", '''{n}The story's records point toward the Ravener at Iz. Terendelev's voice changes when you say its name.{/n}

"That is not just a monster carrying part of me," she says. "It is the part of me that was made to suffer and to hurt others. If it is still there, do not turn the Trickster's plan into an excuse to skip what Iz requires."

{n}You agree not to interrupt the native encounter, change its reward, or call an unfinished death a completed reunion. The people endangered by the Ravener remain part of the decision.{/n}

"If I am ever to meet the person I was before, I will have to face what that creature remembers. You cannot prepare me by hiding it."''',
      c('[Wait for the actual Iz encounter to resolve through its native rules.]', "wait", flags=f("other_half.waiting")),
      c('[Tell her the Trickster should force the boundary open before the Ravener can act.]', "danger", flags=f("other_half.proposed_override"))),
    n("wait", "Terendelev", '''"Thank you," she says. "Not for waiting. For understanding that waiting is the work right now."

{n}The message ends without a promise of reunion. Her voice is quieter than before, but not distant.{/n}

The investigation remains available after the native Iz encounter has a verified result. It will not change the encounter, its combat, or Galfrey's recorded history.''', c('[Close this conversation until the Iz result is known.]', flags=f("other_half.waiting"), abort=True)),
    n("danger", "Terendelev", '''"No," she says. "You are trying to solve my fear by making another choice for me, and the risk would fall on everyone near it. The Ravener is not a lock on a door I asked you to open."

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

"I want to learn what is missing," she says. "I do not want to be told that someone else has already found it for me."''', c('[Record a new investigation objective without marking her soul reunited.]', flags=f("other_half.investigation", "other_half.reviewed"))),
    n("choice", "Terendelev", '''"Thank you," she says. "I do not know that I want to become whole in the way you mean. I want the choice to remain mine while I find out what happened."

{n}The Trickster can make that choice possible to ask. It cannot answer for her.{/n}''', c('[Leave the question open and preserve her separate identity.]', flags=f("other_half.reviewed"))),
    n("overclaim", "Terendelev", '''"It proves that the creature died," Terendelev says. "It does not prove that I have returned to a complete life."

{n}She asks you to correct the record before you continue. The other half may be gone, released, or changed. None of those possibilities is the same as being restored.{/n}''', c('[Retract the claim and keep the outcome unresolved.]', flags=f("other_half.corrected"))),
], requires=(NATIVE_RAVENER_DEAD, "trickster", "terendelev.continuation.identity.context.reviewed"), forbids=(PARENT_LICH_BIND, NATIVE_RAVENER_ALIVE), remote=True)

add("trickster_new_courtship", "A question she chooses to ask", "Memory", [
    n("start", "Terendelev", '"I have been thinking about our last conversation. I have not forgotten my answer." {n}Her voice warms through the scale.{/n} "I should like to know what I would say now. Will you speak to me again, without the investigation spread between us?"',
      c('"I would like that."', "begin", flags=f("new.courtship.accepted")),
      c('"Give me time to answer."', "later", flags=f("new.courtship.deferred")),
      c('"I would rather remain your friend."', "friendship", flags=f("new.courtship.declined"))),
    n("begin", "Terendelev", '"Then tell me something I would not find in a proclamation." {n}Her laugh is low through the scale.{/n} "A foolish thing you did in Kenabres, perhaps. I know several of my own. I shall tell you one."', c('"Tell me yours first."', flags=f("new.courtship.open", "romance.confirmed"))),
    n("later", "Terendelev", '"Very well. I shall want an answer when you have one." {n}She pauses.{/n} "Meanwhile, bring the tower\'s account next time. I have not forgotten that either."', c('[Continue the investigation without treating delay as consent.]', flags=f("new.courtship.deferred"))),
    n("friendship", "Terendelev", '"Very well. I would still like your company." {n}Her voice quiets for a moment.{/n} "Tell me what they are doing in Kenabres. Something besides the tower, this time."', c('[Continue the investigation as friends.]', flags=f("new.courtship.declined"))),
], requires=BOUND + f("escape.accepted", "friendship.investigation", "identity.context.reviewed") + ("trickster",), forbids=(PARENT_LICH_BIND,), RequiresAny=["terendelev.continuation.bound_friendship_seen", "terendelev.continuation.bound_rejection_seen", "terendelev.continuation.bound_separation_seen"], remote=True)

add("escape_choice", "The cost of a possible door", "Memory", [
    n("start", "Narrator", '{n}Terendelev has studied the reported change in the copy.{/n} "It can admit something new. I do not know whether it can let me out. I might lose this fragment trying. I might find what remains of me and fail to join it. Before we attempt that, I want to know where I would be going."',
      c('[Proceed only after identifying the other soul fragment and a recoverable destination.]', "prerequisite", flags=f("escape.cautious")),
      c('[Support a crossing if she chooses it, even without certainty.]', "choice", flags=f("escape.open")),
      c('[Tell her the evidence is not yet enough and ask her to wait.]', "wait", flags=f("escape.wait"))),
    n("prerequisite", "Terendelev", '"Yes. Find out what became of my remains at Iz. If someone survived the battle, ask them what they saw. I will not attempt a crossing until I know what I may find on the other side." {n}The scale grows cold in your hand.{/n}', c('[Put the scale away.]', flags=f("escape.prerequisite.pending"))),
    n("choice", "Terendelev", '"I have heard what you would risk. I have not decided what I will risk." {n}Her voice lowers.{/n} "Bring me what you learn of the remains. We can speak again then."', c('[Leave the decision with her and continue only if she asks again.]', flags=f("escape.decision.her"))),
    n("wait", "Terendelev", '"I agree. We have seen a change, not a passage." {n}She sounds disappointed.{/n} "Find out what became of the rest of me. Until then I should like to speak about something besides this place."', c('[Continue the relationship through ordinary scale contact while the investigation waits.]', flags=f("escape.prerequisite.pending"))),
], requires=BOUND + f("escape.test.observed"), forbids=(PARENT_LICH_BIND,), delay=72, remote=True)

add("scale_evening", "A voice across the dark", "Memory", [
    n("start", "Terendelev", '''{n}The scale rests between you on the table. Terendelev's voice reaches you after a long pause.{/n}

"You have spent the last several meetings asking what I remember. Tonight I would like to ask what you miss."

{n}She does not ask for a performance of grief or a report of your sins. She wants to hear the answer because she still wants to know you, even from the other side of a boundary neither of you has solved.{/n}

"Do not give me the answer you think a hero ought to say," she adds. "I have heard enough of those to last several lives."''',
      c('[Tell her you miss the ordinary weight of her arm beside yours.]', "ordinary"),
      c('[Tell her you miss arguing when neither of you is trying to win.]', "argument"),
      c('[Tell her you miss the possibility of a future and fear what it costs her.]', "future")),
    n("ordinary", "Terendelev", '''"That is a small thing," she says. "It is also exactly the sort of thing I would miss."

{n}She asks you to describe the garden after rain. You describe the smell of stone and the cold metal of the fountain. She corrects you about the tree nearest the wall: it was a pear tree, not an apple. She says the fruit was terrible.{/n}

"When I return, if I return, I want to stand somewhere ordinary. I want to be annoyed by a bad meal and tired after a walk. I do not want every moment to become a ceremony because it might be the last one."''', c('[Promise to make room for ordinary days, without promising they will arrive.]', "end", flags=f("intimacy.shared"))),
    n("argument", "Terendelev", '''"You miss losing arguments to me?" she asks.

{n}You tell her that you miss the moments when disagreement did not threaten the whole relationship. She laughs softly.{/n}

"We have never been as calm as you make us sound. But I understand. I do not want you to agree with me to protect the memory you have of me. If we ever meet again, you may tell me that I am wrong."

"You say that now."

"I am sure you will remind me later."''', c('[Tell her you want the real disagreement, not its remembered shape.]', "end", flags=f("intimacy.shared"))),
    n("future", "Terendelev", '''"I fear it too," she says. "I will not tell you that love makes the danger noble. I am not a lesson about hope. I am a person in a place I did not choose, and I would like to leave it if I can do so without losing what remains of me."

{n}Her voice catches once, then steadies.{/n}

"There is still something I want. That does not make the risk worth any price. It means I want to be included when we decide what the price is."''', c('[Agree that her desire belongs in the decision alongside her fear.]', "end", flags=f("intimacy.shared"))),
    n("end", "Terendelev", '''{n}The scale warms in your hand. Terendelev asks you to keep it beside you for a little longer. The dark between you does not close, but her voice no longer sounds quite so far away.{/n}

"I want to kiss you," she says, with a wry edge to her voice. "It is inconvenient that I cannot reach you. You may tell the Storyteller I am holding that against the laws of the world, not against you."

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
    # eng7-f6d: continuation shares her identity; never overwrite the live route's
    # journal/closure metadata during isolated draft integration.
    relationships.setdefault("terendelev", deepcopy(RELATIONSHIP))
    payload.setdefault("Presences", {}).update(deepcopy(PRESENCES))
