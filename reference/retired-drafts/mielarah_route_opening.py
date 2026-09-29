"""Unregistered opening contribution for a new Mielarah route.

All contact and path-entry flags below are authored contracts, not native game
facts. A runtime producer must prove Mielarah is alive, reachable, and willing
to receive the contact before these scenes can be registered.
"""
from pathlib import Path

from story_format import c, n, scene


# Intended chronology is narrower than the current authored gate can prove.
INTEGRATION_PREMISE = {
    "before": "Native C4 AirAdventures voyage reaches the Colyphyr Tumberd conversation.",
    "attach_after": ("424cf61a022d8d34b9131e99bf360ebd", "e05a1a1f1bc27674fbd569208c28c739"),
    "required_live_actor": "Mielarah at that same Tumberd scene; no later placement is assumed.",
    "verified_parent_choice_chain": False,
    "verified_extension_hook": False,
    "implemented": False,
    "excluded_histories": ("Cue_0426 Ishiar crash without an audited survival intervention", "Cue_0482 fatal Vazglar raid", "Cue_0010 Aeon expulsion without an audited later location"),
}

# Route concepts are authored proposals. They do not set native path flags and
# none is an implemented, reachable route. Each record says what must be built
# and audited before anyone can claim availability.
PATH_ACCESS = {
    "angel": {
        "condition": "After a verified living Colyphyr arrival, choose to shelter the ship's crew from a danger without demanding Mielarah's praise or conversion.",
        "choice_and_consequence": "She inspects the protection herself, credits any cost honestly, and may reject the Commander if the offer came with a sermon or order.",
        "failure": "A refusal to be recruited closes this contact; she keeps command and the route ends.",
        "native_anchor": "AirAdventures/Cue_0006, Cue_0020 or Cue_0070 only establish native ship/captain portrayal and a Colyphyr service statement; no Angel-specific contact is evidenced.",
        "implemented": False,
    },
    "aeon": {
        "condition": "Before any later court outcome, bring the actual curse and ship record to the Aeon hearing and ask for a bounded judgment of conduct rather than a sentence based on predicted deaths.",
        "choice_and_consequence": "If the Commander authorizes expulsion, the romance contact closes. A future authored alternative may preserve a later meeting only if the native court permits it and Mielarah freely agrees.",
        "failure": "No post-expulsion contact unless a later location or voluntary message is independently verified.",
        "native_anchor": "C4Aeon_Tumberd_Court/Cue_0001, Cue_0002, Answer_0015 and Cue_0010; native Cue_0010 explicitly orders her to leave the realm.",
        "implemented": False,
    },
    "azata": {
        "condition": "After a verified living Colyphyr arrival, offer practical crew assistance and let Mielarah choose the task and limits; do not treat the ship as the Commander's rescue reward.",
        "choice_and_consequence": "A completed task opens another conversation only if her crew confirms the aid was welcome. She can keep the relationship professional.",
        "failure": "If aid disrupts her command or she declines it, withdraw and close this approach.",
        "native_anchor": "AirAdventures/Cue_0020 or Cue_0070 are the native Colyphyr service lines; an Azata producer or actor contact is not evidenced.",
        "implemented": False,
    },
    "demon": {
        "condition": "After a verified living arrival, condemn the captain's conduct to her face if the Commander chose a predatory course, then relinquish ship, crew, and passage as leverage.",
        "choice_and_consequence": "Mielarah decides whether to hear one private argument. Candor may deepen respect, while a coercive order or raid ends contact and may preserve her hostility.",
        "failure": "If she or her crew are dead, no living romance begins without a separately audited restoration authored for this path.",
        "native_anchor": "The raiding branch at AirAdventures/Cue_0482 records her protest and death; a Demon route cannot silently bypass it.",
        "implemented": False,
    },
    "devil": {
        "condition": "After verified survival, offer a written passage or protection contract with explicit termination, no control over Mielarah, and no sexual or romantic clause.",
        "choice_and_consequence": "She may call the terms an insult to the aeronaut's code, negotiate a strictly practical obligation, or decline. Only her freely chosen later meeting can continue courtship.",
        "failure": "Invoking legal or infernal force to obtain her service closes the romance and preserves the ship's refusal.",
        "native_anchor": "TavernBadLuck/Cue_0053 and Cue_0056 establish her stated code and ship reputation; no Devil contract or meeting is native.",
        "implemented": False,
    },
    "gold_dragon": {
        "condition": "After verified survival, choose a concrete act that protects a threatened crew without asking Mielarah to approve the Commander's transformed identity or morality.",
        "choice_and_consequence": "She judges the act by its effect on her people, not its mythic label. A costly but unwanted intervention can still earn anger rather than attraction.",
        "failure": "If the intervention takes command away from her, accept her rebuke and end the private approach.",
        "native_anchor": "The extracted C4 AirAdventures lines evidence her ship and curse, not Gold Dragon access or current actor placement.",
        "implemented": False,
    },
    "legend": {
        "condition": "After a verified living arrival and the Commander's departure from mythic power, establish an ordinary, auditable courier route that Mielarah can accept or ignore.",
        "choice_and_consequence": "She decides whether a mortal correspondence is worth her time; losing supernatural leverage does not create trust by itself.",
        "failure": "No letter is delivered to an unverified location and no response is inferred from silence.",
        "native_anchor": "No Legend-era location, courier, or Mielarah survival state is established by the inspected dialogue.",
        "implemented": False,
    },
    "lich": {
        "condition": "Only meet a living Mielarah who retained her own mind and chose an independent position; no undead copy, compelled servant, or resurrected body counts as consent.",
        "choice_and_consequence": "The Commander must offer a non-necromantic exit from any threat to the ship. Mielarah may reject an alliance and keep her captaincy apart from the romance.",
        "failure": "If she died or was raised under control, the route remains closed unless a distinct agency-restoration arc is authored and reviewed.",
        "native_anchor": "No Lich path actor/contact or noncoercive survival branch is proven by the extracted source set.",
        "implemented": False,
    },
    "swarm": {
        "condition": "Before the Swarm consumes the Commander's former allies, author and verify an evacuation Mielarah herself chooses, with an independent living crew and a later voluntary sender.",
        "choice_and_consequence": "She can escape the Commander and sever contact; continued romance requires a later choice from her, not pursuit by the swarm.",
        "failure": "If she or her crew are consumed, presumed dead, or unreachable, there is no route until a reviewed and mechanically evidenced survival intervention exists.",
        "native_anchor": "The inspected C4 dialogue does not establish Swarm survival, escape, or later identity/contact.",
        "implemented": False,
    },
    "trickster": {
        "condition": "Before the native Ishiar crash cue fires, the verified Answer_0351 branch is active under CaptainMielara etude, and Mielarah remains alive at the helm. A runtime producer must intercept that exact answer before Cue_0426; no such hook is verified.",
        "choice_and_consequence": "Proposed authored checks: Knowledge Arcana DC 26 to distinguish the curse's fatal conviction from the immediate wind vector, then Perception DC 24 to mark a narrow lee. Mielarah decides whether to authorize a one-minute visible false crosswind and keeps the helm. A successful hard landing leads to an explicitly alternate three-day repair passage, then a captain-chosen arrival at Tumberd before contact can be recorded. Neither event is native or implemented.",
        "failure": "Either failed check, Mielarah's refusal, or a boundary violation leaves the native crash outcome intact and cannot reach the authored survival or contact states. The Trickster cannot reverse Cue_0426 after it fires, conjure her from death, or compel her to board or accept romance.",
        "native_anchor": "Raw AirAdventures/Answer_0351 GUID b98a0a14e5741ea4c90ae015154bc861 is selected by Cue_0426 GUID 1b4e78245cb3a244588f9ec0fda54ea8 when CaptainMielara etude 8d0fcb697a43a464fa7119e274bf9d7b is active. Proposed checks and wind event remain wholly authored and unimplemented.",
        "implemented": False,
    },
}

# Fate audit from the local extracted dialogue. A cue proves only the depicted
# event in that native branch, not a persistent flag or a later actor location.
FATE_AUDIT = {
    "intro": {
        "evidence": "c4/AirAdventures/Cue_0006, GUID 8235006c1e10df244a3467c7b3900f2a",
        "native_result": "Starcatcher the Third is flying; Mielarah is introduced as captain.",
        "route_treatment": "Only proves she is present at this intro moment.",
    },
    "colyphyr_service": {
        "evidence": "c4/TavernBadLuck/Tumberd/Cue_0020 and Cue_0070; Farewell Cue_0040",
        "native_result": "In these dialogue results she places Starcatcher and its crew at the Commander's disposal; Cue_0020 is annotated FlyPrice3 / -100,000 gp and Cue_0070 FlyPrice1 / -150,000 gp. The farewell says the curse has not claimed her life.",
        "route_treatment": "Candidate living contact window at the Colyphyr dialogue moment only. Parent selection and persistent flags are not yet bound, and the repeated cue has no proof of a later location.",
    },
    "ishiar_crash": {
        "evidence": "c4/AirAdventures/Answer_0351 GUID b98a0a14e5741ea4c90ae015154bc861; Cue_0426 GUID 1b4e78245cb3a244588f9ec0fda54ea8; CaptainMielara etude GUID 8d0fcb697a43a464fa7119e274bf9d7b",
        "native_result": "The raw cue condition requires AnswerSelected for Answer_0351 plus the CaptainMielara etude playing. Answer_0351 text orders Mielarah to helm through the storm; Cue_0426 depicts Gravedragger panic, loss of the wheel, and the Ishiar crash.",
        "route_treatment": "The unregistered authored branch now models survival, a three-day repair passage, and a Mielarah-chosen arrival at Tumberd before setting contact or a delayed follow-up. This is an authored alternate timeline, not native evidence. The intervention remains unavailable until a producer binds Answer_0351 and the active etude, safely suppresses the native cue, and verifies campaign progression.",
    },
    "trickster_alternate_timeline": {
        "native_anchor": "Answer_0351 GUID b98a0a14e5741ea4c90ae015154bc861 and Cue_0426 GUID 1b4e78245cb3a244588f9ec0fda54ea8 establish the native storm order and crash cue.",
        "native_limit": "The base-game evidence shows the crash outcome. It does not establish survival, a repair route, Tumberd arrival after the crash, Colyphyr healers, or a mod interception window.",
        "authored_counterfactual": "On the proposed successful Trickster branch, Mielarah orders a hard landing, keeps command through three days of repairs, and chooses to take Starcatcher to the Tumberd berth. Only after that narrated arrival can the source contract set a living-contact state.",
        "runtime_dependency": "Unimplemented answer interception, cue suppression, campaign progression, survival persistence, and actor/contact availability.",
    },
    "vazglar_raid": {
        "evidence": "c4/AirAdventures/Answer_0404 GUID 1eececde9d7a70c44be526ea668f3ed4; Cue_0482 GUID dbec675b71e9d5f4d96055f4bb31762e; CaptainMielara etude GUID 8d0fcb697a43a464fa7119e274bf9d7b",
        "native_result": "The raw cue condition requires AnswerSelected for Answer_0404 plus the CaptainMielara etude playing. Answer_0404 text chooses piracy and a settlement raid; Cue_0482 depicts Mielarah's protest, attack, and death.",
        "route_treatment": "Confirmed dead state; no living-route entry without a separately authored and reviewed restoration arc.",
    },
    "coercive_magic": {
        "evidence": "c4/AirAdventures/Cue_0032 and Cue_0328",
        "native_result": "The first describes magically imposed apathy; the second describes amulets compelling mutineers and the leader falling to his death, after which Mielarah is distraught.",
        "route_treatment": "These are separate morally serious outcomes, not proof she repented, changed policy, or is available to romance.",
    },
    "aeon_expulsion": {
        "evidence": "c4/Mythic_Aeon/C4Aeon_Judgement/C4Aeon_Tumberd_Court/Cue_0010",
        "native_result": "Nocticula expels her from Alushinyrra because her curse endangers servants.",
        "route_treatment": "No later location or voluntary contact is proven. This route entry cannot use her after expulsion until that state is source-bound.",
    },
}


PRODUCER_CONTRACT = {
    "mielarah.opening.contact_verified": {
        "requires_native_survival_proof": True,
        "requires_native_c4_outcome_audit": True,
        "requires_exact_colyphyr_native_dialogue_hook": True,
        "requires_path_specific_contact_producer": True,
        "authored_trickster_source": "mielarah.trickster.arrived_colyphyr",
        "implemented": False,
        "notes": "Never infer survival from an unlocked route, a quest item, or the Commander's wish. The Trickster scene records a proposed authored survival observation; it has not been mapped to a verified game flag or runtime cue override.",
    },
    "mielarah.trickster.arrived_colyphyr": {
        "requires_authored_alternate_timeline": True,
        "requires_three_day_repair_passage": True,
        "requires_mielarah_chosen_destination": True,
        "implemented": False,
        "notes": "This authored route bridge is not native evidence and depends on a future integration that can preserve the campaign after Cue_0426 is suppressed.",
    },
}

DELIVERY_CONTRACT = {
    "ManualOnly": True,
    "Remote": True,
    "runtime_behavior": "The mod UI lists an available remote scene with a Read button; ManualOnly excludes it from automatic NextRemote delivery.",
    "validator_rule": "src/Story.cs rejects ManualOnly when Rules.IsRemote(scene) is false.",
    "location_limit": "Remote delivery is an authoring fallback, not evidence that Mielarah's actor is physically present at the narrated location.",
    "implemented_as_native_contact": False,
}

RELATIONSHIP = dict(
    Title="A course freely chosen",
    Description="A conditional opening about command, accountability, and the uncertain possibility of mutual attraction.",
    Objective="Meet Mielarah on terms she chooses and decide whether to continue the conversation",
    Guidance="Unregistered opening draft. Requires a verified living Mielarah and a voluntary contact producer. Rescue, ship access, gratitude, and intimacy are never romantic payment.",
    StartedFlag="mielarah.opening.started",
    ClosedFlag="mielarah.opening.closed",
    CommittedFlag="mielarah.route.courtship",
    UnavailableFlags=["mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"],
    FailureFlags=[],
)

SCENES = [
    scene(
        "mielarah.opening.the_invitation",
        "A course freely chosen",
        "Mielarah",
        4,
        "Speak with Mielarah about the wind chart",
        [
            n("start", "Narrator", '''{n}Starcatcher the Third has reached Colyphyr. You were a passenger for the voyage; the ship and crew have survived this leg, though nothing in that arrival proves the Gravedragger is gone.{/n}
Mielarah catches you before you leave the mooring. She has a brass-edged chart under one arm, her grin quick and a little sharp.
"Well. You heard me say the ship was at your disposal. That means passage on the route we agreed. It does not mean you get to stroll across my deck whenever inspiration strikes."
"I had not assumed?"
"Good. Ask. It saves us both a speech." She taps the chart against her palm. "I've a crosswind that won't stay put on paper. I want another pair of eyes. You can look from the quay. Touch nothing until I say. If that is too small an honor, the gangplank is behind you."''',
              c("Read the disputed bearing from the quay, as she offered.", "conditions", flags=("mielarah.opening.started",)),
              c("Decline the conversation and leave without another approach.", "decline", flags=("mielarah.opening.closed",)),
              c("Ask whether her offer includes permission to board Starcatcher.", "verify")),
            n("verify", "Narrator", '''"You can look from here," Mielarah says. "I am not giving you command of my ship because you know how to read a chart."
She holds the brass plate out, but keeps her fingers on it until you reach. When you do, she lets go at once.
"Good. You waited. I have had people call that trust. It was a test of whether you listen. Don't promote yourself because you passed one." Her mouth tips upward. "The plate is warped. I want your reading, not your hands on the rigging."
The limit is plain. The captain is not pretending the ship or its crew are hers to lend without their own say.''',
              c("Accept the limit and read the plate from the quay.", "conditions", flags=("mielarah.opening.started",)),
              c("Decline; you will not continue on these terms.", "decline", flags=("mielarah.opening.closed",))),
            n("conditions", "Narrator", '''{n}The crosswind on Mielarah's chart is drawn in three different inks. She corrects the first two with a blunt pencil and leaves the third untouched. A scuff of grease darkens her cheek; the short hair above it lifts in the breeze off the berth. Her eyes are tired, her smile alert.{/n}
"I told the clerk I wanted a second opinion. He brought me a commander. I suppose that is what happens when one makes a request in the Abyss."
"You can still send me away."
"I know. I am deciding whether I want to." She turns the chart around so you can read it. "First, show me which mark you distrust. If you point at the prettiest one, I will laugh at you. If you point at all three, I will throw you off my quay."
She says it with enough amusement that you can tell the threat is playful. The underlying boundary is not.''',
              c("[Perception DC 24] Read the crossed course marks without guessing from appearance.", check=dict(Skill="SkillPerception", DC=24, Success="command", Failure="bad_read", CommanderOnly=True)),
              c("Admit you cannot read the plate and ask her to explain it.", "humble"),
              c("Apologize for any danger your decisions brought to her crew.", "accountability")),
            n("bad_read", "Mielarah", '''"No. You picked the ink you liked, not the wind that made it." She takes the plate back before the guess can become an order.
Her laugh is brief and mean enough to sting. "You can try again after you learn which line marks pressure. Or you can admit you don't know. Those are both better than selling me confidence you haven't earned."''',
              c("Admit the guess and ask her to show you the reading.", "humble"),
              c("Defend your guess as an order she should obey.", "friction")),
            n("humble", "Mielarah", '''She turns the plate toward the sun and traces the faintest of the three lines with her thumbnail.
"This is the pressure edge. That one's the old course. This is where a careless reader puts us on the rocks." She watches your face as she explains it. "No shame in not knowing. There is shame in pretending and making the crew pay for it."
She is not gentle about the correction. She is pleased that you listened.
"Now, tell me what you would do with a shorter course that saves time but risks a rough landing. You may answer badly. I can take it."''',
              c("Give her an honest estimate, including the danger you would accept.", "truth", flags=("mielarah.opening.trust_seed",)),
              c("Refuse to pretend you can decide a captain's course for her.", "challenge")),
            n("command", "Narrator", '''"That mark," you say, indicating the paper, not the ship. "The pressure shifts before the current does."
"Maybe. Or the scribe copied the old bearing and got sentimental about it." Mielarah leans over your shoulder, close enough for you to catch salt, lamp oil, and the sharp herb worked into her hair. "Go on. Make the case."
You explain the change you noticed. She interrupts twice, first to correct the crosswind's direction, then to say you have confused a gust with a stable current. The second correction is right. You concede it.
"There. You can be taught. It's a charming quality in a commander." Her smile lasts long enough to make the compliment feel deliberate. Then she steps away and points at the disputed bearing. "I asked for your eyes, not your title. One right answer still doesn't get you my helm."''',
              c("Explain your reading and name the risk you think it carries.", "truth"),
              c("Tell her she is wrong about the pressure and defend your reading.", "friction"),
              c("Ask what she has learned from the voyage you just shared.", "challenge")),
            n("accountability", "Mielarah", '''Mielarah snorts. "An apology before I've even accused you. Efficient. I like efficient."
The smile does not last.
"You may have made the right call. You may have been lucky. The crew still had to live with whatever your decision set moving. So did I."
She puts one finger on the chart. "If you came here hoping I'd say it wasn't your fault, I won't. I don't know that. If you came to admit that your decisions carried risk, good. Now we can talk without one of us auditioning for sainthood."''',
              c("Continue only if she still wants to discuss command.", "truth"),
              c("End the meeting and make no later approach unless she initiates one.", "decline", flags=("mielarah.opening.closed",))),
            n("truth", "Narrator", '''{n}You answer without claiming that every decision was clean. Mielarah watches your face instead of the chart. She taps the fork in the route where a faster current cuts close to danger.{/n}
"This one, then. Would you take the short course?"
You say you would weigh the risk against the lives and time at stake, but you cannot promise she would like the answer.
"Good. I hate a polished answer. Makes me wonder what you threw overboard to get it so shiny." She folds the chart along its old crease. "You read the crosswind beside me instead of pretending you could command it. You didn't understand every gust, and you didn't pretend to. I noticed. That is more useful than a speech about how much you trust me."''',
              c("Ask what she would refuse, knowing her own history complicates the answer.", "her_history"),
              c("Tell her your answer is enough for today, and ask whether she wants to continue another time.", "pause")),
            n("her_history", "Mielarah", '''"The crew were ready to gut each other. I stopped them." Mielarah says it quickly, as though speed might settle the argument. Then she grimaces. "There. That's the story I used to tell myself."
She turns the brass amulet in her fingers. "I put it on. They went still. I called it disciplinary thought-correction because the other words sounded like a crime. The ringleader walked over the rail. He chose that step, if you insist on the detail. My spell made every other choice for him first."
For a moment she looks less ashamed than angry: at the mutineer, at herself, and at you for hearing it. "I cried. I also kept the rest of the crew alive. I will not pretend either fact cancels the other. Do not praise me for regretting it. Do not tell me the spell was harmless because it worked."''',
              c("Ask whether she has given the crew a way to refuse her magic now.", "repair"),
              c("Tell her that the danger she faced does not make control harmless.", "friction"),
              c("Acknowledge both the danger and the harm, without absolving her.", "repair")),
            n("friction", "Mielarah", '''Her eyes go hard. "Careful, Commander. I asked for an answer. I didn't ask for a lecture from a person who has never had to keep a mutinous crew alive."
The warning is not theatrical. She takes the chart back, pinning its corner under one palm.
"You may tell me I was wrong. You may even be right. But if you decide that makes you my judge, this talk is over. I can live with a person who disagrees. I cannot stand one who confuses disagreement with command."''',
              c("Leave without trying to win the last word.", "decline", flags=("mielarah.opening.closed",)),
              c("Let her finish. Tell her disagreement is not a command, either.", "repair")),
            n("challenge", "Mielarah", '''"Both," she says. "I wanted to know if you would lie to me. I also wanted to know if you could stand there while I disagreed with you and not reach for your rank."
Her mouth twitches. "Two useful things to learn about a passenger before I let them aboard."
She rolls the chart back toward herself. The breeze lifts a loose strand from her temple. "I don't need you to make me noble. I've managed quite well without that. And I don't need to be the villain in your story just because I made a brutal choice. If that's all you brought, the gangplank is still there."''',
              c("Tell her disagreement goes both ways; she need not take your conclusion, either.", "repair"),
              c("End the meeting rather than turn the challenge into a contest.", "decline", flags=("mielarah.opening.closed",))),
            n("repair", "Narrator", '''{n}Mielarah keeps one hand on the chart. She has not forgiven the Commander for disagreeing, and does not expect the Commander to absolve her. The conversation does not settle what she will do next time.{/n}
"My first officer thinks I should throw every amulet in the sea," she says. "I told him I would consider it. I haven't. There are times I still think the spell saved the ship. There are times I wake hearing that man hit the water."
"What will you do?"
"I don't know yet. If you need me to have learned the perfect lesson before you can respect me, save us both the trouble." Her gaze cuts to you. "And if you think my worst choice makes me easier to handle, try it. I do enjoy proving people wrong."''',
              c("Stay beside the chart and keep the discussion professional.", "pause", flags=("mielarah.opening.trust_seed",)),
              c("Thank her for the conversation and leave the quay.", "pause"),
              c("Tell her you want to kiss her. Let her decide what to do with that.", "attraction")),
            n("attraction", "Mielarah", '''Mielarah studies you, then gives a short, disbelieving laugh. "You pick a remarkable moment to tell me you want me. I have just told you I used magic to make grown sailors move like puppets."
"I know what you told me."
"And you still want to kiss me?"
"Yes. Not because I think you were right."
She looks at you for a long beat. The crosswind worries at her collar, shifting the fabric against her throat. Her attention follows your eyes and returns to your face.
"I wanted to know whether you'd keep your hands to yourself when I was angry," she says. "You did. I liked that more than I meant to. And when you took my correction without reaching for your rank, I stopped thinking of you as another captain who wants to borrow my ship and started wondering what your mouth would do when you weren't making a speech."
The smile she gives you now is unmistakably hungry, but not forgiving. "That's desire. It isn't pardon. Ask before you touch me."''',
              c("Ask whether you may kiss her hand; wait for a clear answer.", "touch_question"),
              c("Keep your hands to yourself and thank her for the honest answer.", "pause", flags=("mielarah.opening.trust_seed",)),
              c("Say that uncertainty is not a yes and end the meeting before she must manage your reaction.", "pause", flags=("mielarah.opening.trust_seed",))),
            n("touch_question", "Mielarah", '''"My hand," she says. "And if I change my mind, you let go."
She turns her palm upward in yours, then offers her knuckles. Her skin is warm from the sun on the quay. You bend and kiss the back of her hand. She inhales sharply, then draws it back before the kiss can travel farther.
"I did say ask," she murmurs. "I didn't promise to be shy about the answer."
She steps back to the chart. Her eyes stay on you a moment longer than the work requires. "You may come aboard when I invite you. I haven't done that yet. Don't look so hopeful; a captain is allowed to change course."''',
              c("Agree to wait for her invitation; do not claim a berth or promise.", "pause", flags=("mielarah.opening.trust_seed",)),
              c("Tell her you would rather not begin a courtship and leave the meeting kindly.", "pause", flags=("mielarah.opening.closed",))),
            n("pause", "Mielarah", '''{n}The optional Colyphyr conversation ends with Mielarah keeping the chart, the ship, and the next decision. If she asked you to kiss her hand, it was her choice; it does not make the next touch, voyage, or meeting automatic.{/n}
"I'll send for you if I want you aboard," she says. "If I don't, don't have a clerk, an angel, or a trickster deliver another invitation for me."
You say you understand.
"We'll see." She turns away with a grin that is nearly a dare. "And Commander? If I call, come without an escort. If you bring one, I will make you all wait on the quay."''',
              c("Leave the next step to Mielarah, and wait to see whether she sends for you.", flags=("mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.followup_pending"))),
            n("decline", "Narrator", '''{n}You decline the chart and step away from the berth. Mielarah does not follow or call after you. The absence of another invitation is not a coy test.{/n}
The airship remains her command. Her curse remains her burden. The possibility of romance ends here without changing the native record of her survival at Colyphyr or any later consequences.''',
              c("Close the correspondence respectfully.", flags=("mielarah.opening.closed",))),
        ],
        requires=("mielarah.opening.contact_verified",),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=0,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
]


TRICKSTER_PRECRASH_HOOK = "mielarah.native_answer_0351_before_cue0426"
FOLLOWUP_CONTACT_CONTRACT = {
    "mielarah.opening.followup_by_her": {
        "source": "The authored delayed follow-up scene delivers a message Mielarah chose to send; accepting it records her invitation, while refusal closes this approach.",
        "requires_native_actor_and_current_area": True,
        "source_scene": "mielarah.opening.followup_contact",
        "delay_hours": 24,
        "implemented": False,
        "native_source_verified": False,
    },
}

SCENES.extend([
    scene(
        "mielarah.trickster.ishiar_intervention",
        "A wind with no source",
        "Mielarah",
        4,
        "Trickster: hold the helm against the storm",
        [
            n("trickster_storm_start", "Narrator", '''{n}The order has left no room for another delay. Mielarah is at the helm, one hand locked on the wheel while the other searches for a wind she can still trust. The sails strain; the deck shudders beneath the crew's feet.{/n}
"Don't tell me the storm isn't real," she shouts over the rigging. "I can see the water. I can hear the mast. If this is a trick, make it one that changes the wind, not my head."''',
              c("[Knowledge: Arcana DC 26] Separate the curse's fatal certainty from the actual wind vector.", check=dict(Skill="SkillKnowledgeArcana", DC=26, Success="trickster_vector_read", Failure="trickster_failed_read", CommanderOnly=True)),
              c("Do not use Trickster power. Countermand your order and let Mielarah make the next call.", "trickster_native_course", flags=("mielarah.trickster.no_intervention",)),
              c("Tell Mielarah you will not alter wind or mind without her explicit agreement.", "trickster_offer")),
            n("trickster_failed_read", "Narrator", '''The spell does not separate fear from weather. The storm is real; the curse is real; your cleverness has given you no safe bearing. Mielarah is still at the wheel, and the native crash cue is still pending.
"Stop guessing," she barks. "If you have no course, say so. I can use the truth."''',
              c("Countermand your order and leave the wheel to her judgment.", "trickster_native_course", flags=("mielarah.trickster.failed_arcana",)),
              c("Keep forcing a trick you cannot read.", "trickster_forced_failure", flags=("mielarah.trickster.failed_arcana",))),
            n("trickster_vector_read", "Narrator", '''{n}The Arcana check does not dispel the Gravedragger or still the storm. It reveals two things at once: Mielarah's certainty that the ship must die is being sharpened by the curse, and the crosswind tearing the sail is a real, changing force. A narrow lee opens behind a broken shelf of black rock. It may hold long enough to turn the ship. It may also be a wall under the water.{/n}
You cannot make the decision for her. You can offer one false crosswind, visible to every sailor and lasting for less than a minute, to show whether the current bends toward the lee. It will not touch a living mind, stop the sea, or guarantee that the ship survives.''',
              c("Tell her the exact limit and risk, then let her decide whether to try it.", "trickster_offer"),
              c("Decline to spend the trick. Countermand your order and let Mielarah choose.", "trickster_native_course", flags=("mielarah.trickster.no_intervention",))),
            n("trickster_offer", "Mielarah", '''"A false wind?" Mielarah's teeth flash. "I don't need a ghost pushing me toward a reef."
You tell her the wind will be visible, brief, and limited to the air. It will not choose for her. The storm may still destroy Starcatcher.
"And no spell in my crew's heads?"
"No."
"Then I can judge what I see." Her voice cuts through the roar. "One minute. If the sail pulls the wrong way, I abandon the turn. If I say stop, you stop. Don't spend my people to prove your talent."''',
              c("Agree to her exact terms and attempt the Arcana intervention.", "trickster_wind_test", flags=("mielarah.trickster.consent_to_wind_only",)),
              c("Refuse to change the weather under these conditions; let her keep the helm.", "trickster_native_course", flags=("mielarah.trickster.no_intervention",)),
              c("Ignore the limits and force the wind toward the lee.", "trickster_forced_failure", flags=("mielarah.trickster.boundary_broken",))),
            n("trickster_wind_test", "Narrator", '''The trick catches the empty seam between one gust and the next. For a breath, the false crosswind stands beside the storm like a second answer to the same question. Every sailor can see the sail tug; no one moves as if commanded.
Mielarah keeps both hands on the helm. "Now tell me where the lee opens. If you can't see it, I won't turn."''',
              c("[Perception DC 24] Mark the lee between the rock shelf and the breaking water.", check=dict(Skill="SkillPerception", DC=24, Success="trickster_lee_found", Failure="trickster_missed_lee", CommanderOnly=True)),
              c("Admit you cannot mark a safe passage. Let the false wind fade.", "trickster_native_course", flags=("mielarah.trickster.no_safe_bearing",))),
            n("trickster_missed_lee", "Mielarah", '''You mistake a white crest for the lee. Mielarah catches the error before the false wind can carry the ship into it.
"No. That's surf. I asked for a course, not a reason to die with enthusiasm." She lets the wheel hold on its present angle. "Let the trick go. I'll take the course from here."''',
              c("Let the false wind fade and leave the next course to Mielarah.", "trickster_native_course", flags=("mielarah.trickster.failed_perception",))),
            n("trickster_lee_found", "Mielarah", '''"There." She sees the line you marked, then checks the water with her own eyes. "That is a terrible place to put a ship."
"It is the only lee."
"I know." Her knuckles are white on the wheel. "And you are still not going to steer it for me."
You shake your head.
"Good. Then watch the sail. When I turn, I want the false wind against the storm for three breaths. If it shifts early, I break off. If the shelf isn't clear, you kill the trick. I take us in on my call."''',
              c("Hold the false wind for exactly three breaths, then let Mielarah steer.", "trickster_hard_landing", flags=("mielarah.trickster.wind_intervention_attempted",)),
              c("Let the trick expire now. Mielarah keeps the helm and the native outcome.", "trickster_native_course", flags=("mielarah.trickster.no_intervention",))),
            n("trickster_hard_landing", "Narrator", '''The wind holds for three breaths. Mielarah turns hard. The ship's belly scrapes the black shelf; a yardarm breaks, a sail tears, and the impact knocks you against the rail. When the false gust fades, Starcatcher is still moving, but no longer sinking into the raging water.
Mielarah orders the crew to account for one another before she looks at you. Her face is furious with fear, not gratefulness.
"You changed the ending of that minute," she says. "You didn't cure what put me there. We have damaged rigging, hurt people, and a ship stranded on a shelf. Don't call that a rescue until my crew is safe."''',
              c("Help only where Mielarah assigns you; leave her in command.", "trickster_after_landing", flags=("mielarah.trickster.authored_landing",)),
              c("Claim you saved her and demand she trust your next decision.", "trickster_close", flags=("mielarah.trickster.authored_landing", "mielarah.trickster.trust_demanded"))),
            n("trickster_after_landing", "Narrator", '''{n}Mielarah runs the count herself. One sailor has a broken wrist; another is pinned beneath a spar. You move when she points, and stop when she orders you clear. The crew answer her by name, not yours. Only when the last injured sailor is carried below does she turn back to you.{/n}
"You held the trick when I told you to. That mattered. It doesn't make the choice harmless. I gave you one minute and you spent it on a ship full of people who never agreed to be your experiment." Her stare is hard, but not simple. "I would have made the turn. I did make it. Don't steal that from me by calling yourself my savior."
The surviving course has bought a chance to live, not pardon or affection. She will decide whether survival is followed by another conversation.''',
              c("Accept the account and ask what the injured crew need.", "trickster_respectful_reckoning", flags=("mielarah.trickster.accepted_account",)),
              c("Tell her the crew deserve the truth about the risk you chose.", "trickster_truth_reckoning", flags=("mielarah.trickster.truth_requested",)),
              c("Insist your success entitles you to her trust.", "trickster_close", flags=("mielarah.trickster.trust_demanded",))),
            n("trickster_respectful_reckoning", "Mielarah", '''At dawn, Mielarah meets you on the damaged quarterdeck. The repaired sail is still a patchwork of borrowed canvas. She has not slept; the line of salt at her temple catches the first light.
"I spent the night deciding whether I was angry because you took a risk, or because you made it work." Her mouth twists. "I hate that those are different questions."
You ask after the injured sailors. "They'll mend. One will complain about his wrist for the rest of his life, which is how I know he'll live." Her voice softens for a beat, then she looks back at you. "I would like another conversation once the crew are safe. I am not promising you anything. I am deciding whether I want to hear you again."''',
              c("Accept her terms and wait while she decides where to take Starcatcher.", flags=("mielarah.trickster.landing_survival_verified", "mielarah.trickster.journey_pending", "mielarah.opening.met", "mielarah.opening.trust_seed")),
              c("Offer to help with repairs under her orders, then leave the next meeting to her.", flags=("mielarah.trickster.landing_survival_verified", "mielarah.trickster.journey_pending", "mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.trickster.repair_help_offered")),
              c("Leave her to the crew and make no claim on another meeting.", flags=("mielarah.opening.closed",))),
            n("trickster_truth_reckoning", "Mielarah", '''"They do deserve it," Mielarah says. "That doesn't mean I want you telling it for me." She looks past you at the patched sail. "I can tell them what happened. I can also tell them the turn was mine. Both things are true, and I won't let you make me the only person who chose a risk today."
She studies you as though looking for the easy answer. "You can come hear what I tell them if I ask. Until then, wait. If you can't wait, there is the gangplank."''',
              c("Wait for her to decide what happens next; do not ask her to promise you anything.", flags=("mielarah.trickster.landing_survival_verified", "mielarah.trickster.journey_pending", "mielarah.opening.met", "mielarah.opening.trust_seed")),
              c("Tell her you will leave the crew's account to her and go now.", flags=("mielarah.opening.closed",))),
            n("trickster_close", "Mielarah", '''"No." Mielarah steps between you and the companionway, not to keep you there but to make sure you hear the answer. "The ship surviving does not put me in your debt. You asked for trust as if the danger were a wager you had won."
She points to the gangplank. "Leave. I'll tell the crew what happened. You don't get to turn their injuries into your courtship story."''',
              c("Leave without pressing her, and close this approach.", flags=("mielarah.opening.closed",))),
            n("trickster_forced_failure", "Mielarah", '''Mielarah's hands wrench against the helm. The false gust catches the canvas at the wrong angle; the sail snaps back and the turn collapses.
"You said you could hold it," she shouts. "You promised the limit!"
Mielarah sees the sail snap back toward the water. "Stop it!" she shouts. The crew cling to whatever they can reach as she fights to keep the ship from turning broadside.''',
              c("Stop the magic and let Mielarah make the next call.", "trickster_native_course", flags=("mielarah.trickster.boundary_broken",))),
            n("trickster_native_course", "Narrator", '''You end the trick and tell Mielarah the wheel is hers. The storm does not pause for either of you. She shouts an order; the crew answer, and Starcatcher pitches hard beneath the next gust. There is no safe bearing in your hands now. You can only stand clear and let the captain face the course she chose.''',
              c("Step back and accept Mielarah's order.")),
        ],
        requires=("trickster", TRICKSTER_PRECRASH_HOOK),
        forbids=("mielarah.native.cue0426_fired", "mielarah.dead", "mielarah.trickster.authored_landing"),
        delay=0,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.trickster.colyphyr_arrival",
        "Three days under her command",
        "Mielarah",
        4,
        "Arrive at Tumberd with Starcatcher",
        [
            n("journey_start", "Narrator", '''{n}Three days after the hard landing, Starcatcher limps into the Tumberd repair berth on Colyphyr. For three days Mielarah and her crew have replaced torn canvas, splinted the damaged spar, and decided which risks they can still accept. The ship made the passage because her crew worked and Mielarah chose the route; the false wind did not carry them here.{/n}
The captain is the first onto the quay. Her coat is salt-stiff, and one cuff is held together with sail thread.
"We made it to a place that can mend the mast. That is all I promised. Do not call the damage a miracle, and don't mistake my being alive for owing you a smile."''',
              c("Ask what the crew need, and leave the arrival and repair decisions to her.", "journey_crew", flags=("mielarah.opening.contact_verified", "mielarah.trickster.arrived_colyphyr")),
              c("Tell her you can erase the damage or force Starcatcher onward with another trick.", "journey_forced", flags=("mielarah.opening.contact_verified", "mielarah.trickster.arrived_colyphyr", "mielarah.trickster.boundary_broken")),
              c("Thank her for the passage and say you will leave when she asks.", "journey_crew", flags=("mielarah.opening.contact_verified", "mielarah.trickster.arrived_colyphyr"))),
            n("journey_crew", "Mielarah", '''"They need sleep, a proper spar, and fewer people asking whether the ship is cursed." She rolls the shoulder that took the worst of the landing. "I need the mast inspected by someone who isn't trying to impress me."
You ask what she needs from you.
"Nothing you can pay back in one sentence." She looks toward the crew carrying the torn sail ashore. "You can help unload the gear when I point. You can also leave and let them forget your face for a day. Either is useful."''',
              c("Help with the gear under her directions, then wait for her decision about further contact.", "journey_arrived", flags=("mielarah.trickster.helped_at_tumberd",)),
              c("Leave the crew to their captain and make no claim on a later conversation.", "journey_declined", flags=("mielarah.opening.closed",))),
            n("journey_arrived", "Mielarah", '''By evening, the rigging has been secured and the injured are in the hands of Colyphyr healers. Mielarah checks the work herself, twice. She does not invite you aboard; she does not order you away.
"The first service offer still stands. Passage, if the ship is ready and the crew agrees. It isn't an invitation to come and go as you please." She runs a thumb along the stitched cuff. "When I know whether I want another conversation, I'll send word from the berth. I have not decided yet."
She meets your eyes, blunt as a command and far less certain. "You can wait without turning that into a claim, or leave now. If you wait, you wait for my choice."''',
              c("Wait for her to choose whether to send for you; make no claim on the ship or her attention.", flags=("mielarah.opening.followup_pending",)),
              c("Thank her and leave Colyphyr without expecting another message.", "journey_declined", flags=("mielarah.opening.closed",))),
            n("journey_forced", "Mielarah", '''"No." Mielarah's voice cuts through the quay noise. "You don't get to make a second decision for my ship because the first one worked. We came here under my command. If you change the hull, the course, or the crew's minds without permission, you can leave Starcatcher now."''',
              c("End the trick and leave the repair choices to Mielarah.", "journey_declined", flags=("mielarah.opening.closed",))),
            n("journey_declined", "Narrator", '''{n}Mielarah remains with her crew and the repairs. She sends no second message, and you make no claim on her time or her ship.{/n}''',
              c("Leave Starcatcher and close this approach.", flags=("mielarah.opening.closed",))),
        ],
        requires=("trickster", TRICKSTER_PRECRASH_HOOK, "mielarah.trickster.landing_survival_verified", "mielarah.trickster.journey_pending", "mielarah.opening.met", "mielarah.opening.trust_seed"),
        forbids=("mielarah.native.cue0426_fired", "mielarah.dead", "mielarah.expelled", "mielarah.opening.closed", "mielarah.contact_unverified"),
        delay=72,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.opening.followup_contact",
        "The captain's note",
        "Mielarah",
        4,
        "Read Mielarah's message, if you choose",
        [
            n("followup_note", "Narrator", '''{n}A day passes. No clerk, Trickster, or rescued sailor speaks for Mielarah. A folded note arrives in her own hand, carried by one of Starcatcher's crew: berth seven, after the watch, and a request to hear her out about the amulets. The wording is brisk enough to sound like an order, but the last line says you may decline and she will not send twice.{/n}
The note does not say whether she has changed her mind about the spells, the crash, or you.''',
              c("Accept the meeting she has chosen and take the note to the berth.", "followup_accepted", flags=("mielarah.opening.followup_by_her",)),
              c("Decline without sending a counteroffer or explanation.", "followup_declined", flags=("mielarah.opening.closed",))),
            n("followup_accepted", "Narrator", '''Mielarah is waiting at the gangplank, not aboard the ship. She checks that you came alone, then steps aside so you can choose whether to follow her in. The invitation is hers; boarding is still your choice.''',
              c("Ask permission to come aboard for the amulet conversation.", flags=("mielarah.opening.case_ready",)),
              c("Thank her for the note and leave the meeting declined.", "followup_declined", flags=("mielarah.opening.closed",))),
            n("followup_declined", "Narrator", '''Mielarah receives the refusal and sends no second invitation. The silence after it is the answer; it is not a test, a penalty, or a hidden route condition.''',
              c("Close the approach respectfully.", flags=("mielarah.opening.closed",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.followup_pending"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.opening.the_case",
        "What she keeps under lock",
        "Mielarah",
        4,
        "[Answer Mielarah's own invitation to discuss the amulets]",
        [
            n("case_start", "Narrator", '''{n}Mielarah waits at the gangplank, not aboard the ship. She checks that you came alone, then steps aside so you can choose whether to follow her in.{/n}
"The subject is the amulets. Not the storm, not my feelings, and not whether I am a good woman underneath a bad decision. If you can stay with the subject, come in."''',
              c("Ask what she wants from the discussion before offering advice.", "case_terms"),
              c("Board after asking permission, and hear the case she wants to make.", "case_terms"),
              c("Decline the invitation; you will not discuss her crew without them.", "case_closed", flags=("mielarah.opening.closed",))),
            n("case_terms", "Mielarah", '''The chart room is close and smells of oil, dry paper, and the sharp herb in her hair. The door stays open. Mielarah puts a small leather case on the table but does not open it.
"I have not thrown them overboard," she says. "I told you I would consider it. That was true when I said it. It is still true. I have used them before, and I may use them again if I think the ship is about to be lost."
She puts her palm on the case. "There. That is the part people usually edit out when they tell a story about regret. I am not giving you the case or asking you to decide what happens to it. I want to know what you think my crew is owed, and whether you can answer without pretending the captain has no duty to keep them alive."''',
              c("Say that the crew must be told plainly when she uses a spell on them.", "plain_notice"),
              c("Argue that no emergency can justify taking their minds from them.", "no_control"),
              c("Tell her that in a mutiny you would use any power needed to keep the ship.", "power_answer")),
            n("plain_notice", "Mielarah", '''"Told plainly," she repeats. "Before or after?"
You say before, unless the danger gives her no time.
"That exception is large enough to sail Starcatcher through." Her smile is thin. "If I have time to explain, I have time to hear no. If I have no time, we are already in the worst part of the story. That isn't a rule. It's a weather report."
She opens the case just far enough for the amulets to catch the lamp light, then shuts it again.
"I can tell the crew what is in the case. I cannot promise never to use it. If that means they trust me less, that is their answer to give."''',
              c("Tell her she should ask each sailor whether they will remain under that risk.", "crew_choice"),
              c("Ask how she will account for the choice if someone refuses.", "accounting")),
            n("no_control", "Mielarah", '''"No emergency?" Her laugh has no humor in it. "A mutiny can be one person with a knife at a throat. It can be five people with knives and the rest waiting to see who wins. It can be a frightened crew about to make a mistake that kills all of them. You say no emergency can justify the spell because you are imagining an emergency with time to hold a vote."
"You still take their choice away."
"Yes." She does not soften the answer. "That is why I am not asking you to call it clean. I am asking whether you would rather I risk the whole ship than force one sailor's hand for a minute. I may do it again. If you cannot love me with that in the room, say so now."''',
              c("Tell her you can desire her and still refuse to call the spell right.", "crew_choice"),
              c("Say you will not romance someone who may use that power again.", "case_closed", flags=("mielarah.opening.closed",))),
            n("power_answer", "Mielarah", '''For a moment, she looks pleased. Then she catches herself and the pleasure hardens.
"Don't say that to get aboard my ship. If you mean it, you are more dangerous than I took you for. If you are flattering me, I will have you thrown off the gangplank and feel no regret at all."
You say that keeping the ship alive matters, but that it cannot make the spell harmless.
"Better. A captain must choose, and someone must remember the cost after the choice is over." She taps the leather case. "I won't hand you the reins to my conscience, Commander. You may stand beside it or walk away."''',
              c("Stand beside her without pretending that you would make the same call.", "accounting"),
              c("Tell her she has mistaken attraction for approval and leave.", "case_closed", flags=("mielarah.opening.closed",))),
            n("crew_choice", "Narrator", '''{n}Mielarah listens, then picks up the case. Her thumb rubs the clasp hard enough to whiten at the nail.{/n}
"I can tell them the truth and let each one choose whether to stay. I can keep the amulets sealed unless I believe we are at immediate risk. That still makes the final call mine."
She watches you closely. "You may dislike that. I dislike it too. I will not promise them a captain who has no authority when the hull is coming apart. I also will not tell myself that a sailor's silence is consent."
The case remains in her hand. She has not decided whether she will open it at the crew meeting.''',
              c("Ask her to hold the crew meeting before deciding what rule to adopt.", "accounting", flags=("mielarah.opening.crew_heard",)),
              c("Tell her it is her ship and leave the decision with her.", "accounting")),
            n("accounting", "Mielarah", '''"I will speak to them," Mielarah says. "I haven't decided what I will promise."
Her certainty is not complete. She sounds angry that it isn't, and more angry at anyone who might mistake the hesitation for weakness.
"If I make a rule that fails in the next crisis, I will have made a pretty rule, not a useful one. If I keep everything as it was, I may lose the crew before a crisis arrives. I don't know which danger I can live with."
She returns the case to the table and leaves it closed. "I wanted to know whether you would say something difficult and stay here while I disliked hearing it. You did. That does not mean I trust you with my ship. It does mean I want you back."''',
              c("Ask if she means another argument or something more private.", "private_invitation", flags=("mielarah.opening.second_meeting",)),
              c("Tell her you will come back only if she wants your company, not your judgment.", "private_invitation", flags=("mielarah.opening.second_meeting",)),
              c("End the conversation without converting her invitation into a promise.", "case_closed", flags=("mielarah.opening.closed",))),
            n("private_invitation", "Mielarah", '''Mielarah studies you. "I'm attracted to you. You haven't cured my curse or convinced me to throw out the amulets. You have made arguing with you more interesting than it ought to be."
Her gaze drops to your mouth, then rises. "I want one evening. Private. Don't take it for a berth or a promise about tomorrow. If I change my mind, I say so. You can leave whenever you like."
The case remains within reach. She does not move it.''',
              c("Accept the evening, and leave the hour and place to her.", "evening_invited", flags=("mielarah.opening.evening_invited",)),
              c("Decline the private evening but keep the conversation open.", "evening_declined", flags=("mielarah.opening.second_meeting",)),
              c("Ask for another day before deciding.", "evening_declined", flags=("mielarah.opening.second_meeting",))),
            n("evening_invited", "Narrator", '''Mielarah names the hour and keeps the invitation limited. She has not promised a romance, a berth, or a change in her judgment about the amulets. The open door remains behind you when you leave the chart room.''',
              c("Wait for Mielarah's chosen hour and invitation.", flags=("mielarah.opening.evening_pending",))),
            n("evening_declined", "Mielarah", '''"All right," she says. There is disappointment in the word, but no attempt to bargain it away.
"I asked because I wanted to. You answered because you wanted to. We can leave it there until one of us has another question."''',
              c("Leave the next step open without promising a romance.", flags=("mielarah.opening.second_meeting",))),
            n("case_closed", "Narrator", '''{n}Mielarah shuts the case and ends the discussion. The route can continue only if she chooses to contact the Commander again; disagreement is not a puzzle that unlocks her, and no later invitation is owed.{/n}''',
              c("Leave Starcatcher by the gangplank.", flags=("mielarah.opening.closed",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.case_ready", "mielarah.opening.followup_by_her", "mielarah.opening.met", "mielarah.opening.trust_seed"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=0,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.opening.the_captains_evening",
        "The hour she chose",
        "Mielarah",
        4,
        "Join Mielarah at the hour she chose",
        [
            n("evening_start", "Narrator", '''{n}Mielarah meets you at the named hour in the small chart room. She has left the case of amulets aboard the ship, locked away from the table. She wears her captain's coat open at the throat, and watches you notice.{/n}
"Tonight is not a hearing," she says. "If you want to argue about the case, you can come back tomorrow. If you want to kiss me, ask. If you want to leave, the door is behind you. I dislike guessing games when I am the one being guessed at."''',
              c("Tell her you want to kiss her, and ask what she wants from the evening.", "evening_terms"),
              c("Ask whether she wants to talk first, without assuming a kiss.", "evening_terms"),
              c("Leave the private evening; her invitation does not obligate either of you.", "evening_exit", flags=("mielarah.opening.closed",))),
            n("evening_terms", "Mielarah", '''"I want to see if the spark survives when neither of us is trying to win." She comes closer, but stops before touching you. "And I want to kiss you. Don't expect me to wake up agreeing with you about the amulets."
"I wouldn't ask."
"Good. Keep your hands where I can see them. I'll put them where I want them." Her laugh is warm, then gone.''',
              c("Keep your hands visible and let Mielarah set the pace.", "kiss", flags=("mielarah.opening.evening_consent",)),
              c("Tell her you would rather talk and keep the evening nonphysical.", "evening_talk"),
              c("Say no and end the evening without explanation.", "evening_exit", flags=("mielarah.opening.closed",))),
            n("kiss", "Mielarah", '''She takes your wrists, one at a time, and places your hands at her waist over the fine fabric of her coat. Then she kisses you with no trace of the cautious courtesy she used on the quay. Her mouth is warm; her grip is firm. She draws you close until the chart table presses lightly into your hip, then pauses just long enough to see whether you follow or hold still.
You follow when she asks with her eyes. Her breath catches against your cheek. She kisses you again, slower, and lets her thumb trace the edge of your collar before she pulls back.
"That was my choice," she says. "Don't turn it into a promise about tomorrow."
"I won't."
"Good. I may still want you tomorrow. I may wake up irritated with you and the entire concept of wanting anyone. Either way, I will tell you."''',
              c("Tell her you want another kiss, and wait for her answer.", "second_kiss"),
              c("Let the evening end with that kiss and no further touch.", "evening_after", flags=("mielarah.opening.evening_shared",)),
              c("Tell her you need to stop; release her hands and step back.", "evening_after", flags=("mielarah.opening.evening_stopped",))),
            n("second_kiss", "Mielarah", '''"Then ask me properly." Her eyes shine with the sort of amusement she uses when she has already decided what she wants but intends to make you speak it aloud.
You ask. She answers with a kiss that opens slowly, her fingers working into your hair while yours remain at her waist until she guides one hand to her back. The warmth of her body through her clothes is unmistakable. She presses her thigh between yours, then breaks the kiss herself, breathing unevenly.
"Enough for tonight," she says. Her voice is rougher than before. "I wanted you to know I could want more without promising all of it."
She straightens your collar with infuriating care, then lets her hand rest against your throat for one brief, deliberate beat.''',
              c("Accept the limit and stay beside her until she says goodnight.", "evening_after", flags=("mielarah.opening.evening_shared",)),
              c("Ask for more and accept a no without argument.", "evening_after", flags=("mielarah.opening.evening_stopped",))),
            n("evening_talk", "Mielarah", '''Mielarah nods and stays where she is. The discussion turns to the ship's uncertain repair schedule, the crew's answer about the amulets, and whether either of you can sit beside an unresolved choice without dressing it up as fate.
She is sharp when you disagree. She is sharper when you agree too quickly.
At one point she reaches across the table and taps your knuckles with hers. The contact is brief, light, and entirely separate from an invitation to touch more. She withdraws first.
"There," she says. "A pleasant evening that did not require anyone to prove anything. I may have to revise my opinion of you."''',
              c("Enjoy the conversation and leave the physical question for another evening.", "evening_after", flags=("mielarah.opening.evening_shared",)),
              c("End the evening kindly and let her decide whether to invite you again.", "evening_after", flags=("mielarah.opening.evening_stopped",))),
            n("evening_after", "Narrator", '''{n}The evening ends at the limit Mielarah chose. If you kissed, she initiated and directed the contact, then stopped it herself. If you did not, the invitation remains a conversation she chose to have. None of these answers settles the amulet case, the curse, or the future of Starcatcher the Third.{/n}
She walks you to the gangplank and keeps the next meeting hers to offer. Her smile is crooked, tired, and unmistakably interested.
"I haven't decided what you are to me," she says. "Don't make me regret leaving the question open."''',
              c("Thank her for the evening and wait for her next choice.", flags=("mielarah.opening.evening_complete", "mielarah.opening.crew_meeting_pending"))),
            n("evening_exit", "Narrator", '''{n}You end the evening without pressure. Mielarah lets you go. The route remains closed unless she chooses a new approach; there is no pursuit, guilt, or penalty for saying no.{/n}''',
              c("Leave Starcatcher and close this private invitation.", flags=("mielarah.opening.closed",))),
        ],
        requires=("mielarah.opening.evening_pending", "mielarah.opening.evening_invited", "mielarah.opening.contact_verified"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=0,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.opening.the_crews_answer",
        "What the crew will risk",
        "Mielarah",
        4,
        "Attend the meeting Mielarah requested you witness",
        [
            n("crew_meeting_start", "Narrator", '''{n}Two days after the evening together, a note in Mielarah's hand asks you to stand at the edge of a crew meeting. She specifies that you are there to witness, not to vote. A sailor has already refused to wear one of the amulets again. The rest of the crew have questions, and Mielarah has chosen to answer them herself.{/n}
The mess is crowded with damp coats and the smell of tar. No one makes room for you until Mielarah points to a place by the bulkhead.
"There. You can hear, and they can see you aren't taking notes for a tribunal. If anyone wants you gone, you go. That includes me."''',
              c("Take the place she indicates and let the crew speak first.", "crew_question"),
              c("Ask the sailors whether they want you present before sitting.", "crew_question"),
              c("Decline to witness a decision that belongs to the crew and their captain.", "crew_leave", flags=("mielarah.opening.crew_witness_declined",))),
            n("crew_question", "Crew", '''A sailor near the hatch keeps both hands wrapped around a tin cup. "If the captain can use the amulet on me when she thinks it's necessary, I need to know before I sign on for the next run. I don't want to wake up having agreed to something I never heard about."
Mielarah's jaw tightens. "You will hear about it from me."
"Before or after?" the sailor asks.
She looks at the amulet case on the table, then at the crew. "If there's time, before. If there isn't, I may still make the call. I won't lie and promise otherwise." Her voice has no flourish in it. "If you decide that's enough reason to leave, I'll pay your share and find another hand. I won't call you a coward."''',
              c("Tell the crew the same thing you told Mielarah: emergency use still has a cost they can refuse.", "crew_cost"),
              c("Support Mielarah's authority, but ask her to name a review after every use.", "crew_authority"),
              c("Say the amulets should be destroyed before anyone sails again.", "crew_destroy"),
              c("Stay silent and let Mielarah answer without your influence.", "crew_silence")),
            n("crew_cost", "Mielarah", '''"You make that sound clean," Mielarah says. "It isn't. A sailor can refuse a voyage. They can't always refuse the person holding the ship together when the deck is on fire."
The sailor sets down the cup. "Then say you may control us. Don't call it discipline."
Mielarah's nostrils flare. For an instant, she looks ready to throw the case overboard and the argument with it. Instead, she turns the clasp toward the crew. "I used that word because it made the choice sound smaller. It wasn't. I won't use it again." She does not promise the amulets are gone. "If you stay, you stay knowing what I may do. If you leave, I won't make a story about your loyalty."''',
              c("Ask Mielarah privately whether she can live with sailors leaving over this.", "crew_private", flags=("mielarah.opening.crew_truth_spoken",)),
              c("Tell her the naming matters, but the amulets still require a rule.", "crew_rule", flags=("mielarah.opening.crew_truth_spoken",))),
            n("crew_authority", "Mielarah", '''"A review after?" She repeats it without mockery. "You want the person I controlled to tell me whether I was entitled to do it."
"I want the rest of us to know what happened," the sailor says. "And I want the captain to hear what it cost."
Mielarah's gaze shifts between you. "I hate that this is a reasonable answer." Her fingers close around the case, not opening it. "I can tell them what happened. I can let them tell me what they think. I cannot promise they get to overrule me while the ship is in danger."''',
              c("Say the review is not forgiveness or permission to repeat it.", "crew_rule", flags=("mielarah.opening.crew_review_offered",)),
              c("Ask the crew whether that limit is enough for them to stay.", "crew_private", flags=("mielarah.opening.crew_review_offered",))),
            n("crew_destroy", "Mielarah", '''"You think I haven't considered it?" Mielarah says. Her laugh is short and sharp. "I could throw the case into the sea and feel righteous for an hour. Then the next mutiny comes, and I have to decide whether a principle matters more than the people trapped aboard with me."
The sailor says, "Maybe the decision should be ours too."
"Maybe." She hates the word as soon as she says it. "I have not decided to destroy them. I have decided I won't hide what they can do." The case stays under her palm. No one reaches for it.''',
              c("Tell her that refusing to destroy them means she must accept people leaving.", "crew_private", flags=("mielarah.opening.crew_refusal_named",)),
              c("Tell the crew you will not decide the case for them.", "crew_rule", flags=("mielarah.opening.crew_refusal_named",))),
            n("crew_silence", "Mielarah", '''You keep quiet. Mielarah answers each question without looking to you for support. She does not say the mutiny was justified, and she does not pretend the spell left the crew untouched. When a sailor asks whether she will use the amulet again, she answers, "I might. I hope I don't."
The simplicity of it unsettles the room more than a promise would. Someone near the hatch leaves before the meeting ends. Mielarah watches the door close and says nothing until the others have gone.''',
              c("Ask whether she wants company after the crew have left.", "crew_private", flags=("mielarah.opening.crew_silence_kept",)),
              c("Leave with the departing sailor and give her the rest of the evening.", "crew_leave", flags=("mielarah.opening.crew_silence_kept",))),
            n("crew_rule", "Mielarah", '''"A rule," she says, and looks at the case as though it has personally insulted her. "All right. The crew gets the truth before the next voyage. Anyone can leave. If I use the amulet without time to warn them, I tell them after and hear what they have to say before I ask them to sail with me again."
The sailor studies her. "And if you don't like what we say?"
"Then I don't like it." Mielarah's smile is humorless. "I can be angry and still listen. I am not promising to do what you want. I'm promising not to pretend I didn't hear you."''',
              c("Ask her to write the rule with the crew, not just announce it.", "crew_private", flags=("mielarah.opening.crew_rule_proposed",)),
              c("Accept that this is her rule to keep or break, and let the crew judge her by it.", "crew_private", flags=("mielarah.opening.crew_rule_proposed",))),
            n("crew_private", "Mielarah", '''The last sailor leaves. Mielarah closes the mess door but does not lock it. She stands by the table, shoulders squared, one hand resting beside the case.
"There. I said it in front of them. Now I have to live with hearing it repeated when I am tired and frightened and looking for the fastest answer." She gives you a hard look. "Don't tell me you are proud of me. I didn't do anything heroic. I told them the truth because it was overdue."
You say you won't congratulate her for admitting what she did. Her mouth twitches. "Good. I would have thrown you out if you tried." She steps closer, then stops, leaving you room to move away.
"When the ship is patched, I want another day ashore with you. Not because you stood beside me in there. Because you could have made yourself the clever judge and chose to let them speak. I noticed." The admission seems to irritate her. "Don't make me repeat it."''',
              c("Tell her you want that day, and ask what she would like to do ashore.", "crew_next_day", flags=("mielarah.opening.crew_day_invited",)),
              c("Say you need time before another private meeting, and leave kindly.", "crew_leave", flags=("mielarah.opening.crew_day_deferred",)),
              c("Ask whether the crew would be safe if she used the amulet again; accept that she may end the conversation.", "crew_private_again", flags=("mielarah.opening.crew_rule_questioned",))),
            n("crew_private_again", "Mielarah", '''"I don't know," she says. The answer lands harder than an excuse. "I can tell you what I want to believe. I can't tell you I won't reach for it if I think the ship is going down."
She takes her hand off the case. "If that's the answer that makes you leave, leave. If you stay, don't call my uncertainty a promise to change."''',
              c("End the private conversation without making her uncertainty your burden to solve.", "crew_leave", flags=("mielarah.opening.crew_day_deferred",)),
              c("Tell her you will return only if she asks, then leave the next step to her.", "crew_leave", flags=("mielarah.opening.crew_day_deferred",))),
            n("crew_next_day", "Mielarah", '''"Walk the quay," she says. "Somewhere I can see the ship and pretend this is just an inspection." Her grin comes back, crooked and tired. "I will probably argue with you about the rule before we get to the end. Don't take that as a sign the day is going badly."
She reaches for your sleeve, stops short, and waits until you nod before touching it. Her fingers squeeze once. "I want you there. I don't want a promise about who I'll be after the next storm."''',
              c("Agree to meet when she sends the hour, and leave her the final choice.", flags=("mielarah.opening.crew_day_pending",)),
              c("Ask to kiss her, then wait for a direct answer.", "crew_kiss_question")),
            n("crew_kiss_question", "Mielarah", '''She considers you with the same care she gave the crew's questions. "Yes. One kiss. And if I stop it, you let me stop it." Her hand comes up to your collar, thumb settling beneath your jaw. The kiss is brief but not tentative; she bites your lower lip just enough to make you inhale, then pulls away before either of you can turn it into a negotiation.
"There," she says, her voice lower. "That was because I wanted to. Tomorrow I may want to argue about the amulets. I contain multitudes, Commander. Most of them are inconvenient."''',
              c("Accept the limit and wait for her to send the time ashore.", flags=("mielarah.opening.crew_day_pending",)),
              c("Tell her you would rather leave the evening there.", "crew_leave", flags=("mielarah.opening.crew_day_deferred",))),
            n("crew_leave", "Narrator", '''{n}You leave the mess without turning the meeting into a claim on Mielarah. She stays with her crew and the decision they still have to live with. The invitation to another private day can remain unanswered; no affection or passage is owed.{/n}''',
              c("End this branch without a new appointment.", flags=("mielarah.opening.crew_day_deferred",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.followup_by_her", "mielarah.opening.evening_complete", "mielarah.opening.crew_meeting_pending"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=48,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
    scene(
        "mielarah.opening.the_quay_day",
        "A course without a destination",
        "Mielarah",
        4,
        "Meet Mielarah for the day she chose",
        [
            n("quay_day_start", "Narrator", '''{n}Mielarah sends the hour in a note that contains no apology for keeping you waiting. She meets you beside Starcatcher's patched hull, dressed for walking rather than command. The ship remains in view; the repairs are slower than either of you wanted.{/n}
"I said a day ashore. I didn't say a pleasant one." She offers her arm, then turns the gesture into a point at the quay. "We can walk. If I start talking about rigging, you are allowed to throw me into the water."
"Would you do that?"
"If you were annoying enough, I'd consider it." Her eyes flick to your mouth. "I said consider. Don't start planning a rescue."''',
              c("Take the walk and let her choose the direction.", "quay_route"),
              c("Ask if she wants your arm or simply your company.", "quay_route"),
              c("Tell her you are glad she asked, but prefer to keep this day unromantic.", "quay_day_exit", flags=("mielarah.opening.quay_day_nonromantic",))),
            n("quay_route", "Mielarah", '''She takes the narrow quay path that keeps Starcatcher in sight. At each mooring she points out some small flaw in the rigging: a knot tied backward, a pulley with a hairline crack, a pennant trimmed too short. She speaks with the ease of someone who knows every sound her ship makes.
You ask whether she ever gets tired of knowing what is wrong before anyone else sees it.
"Constantly. It is still better than learning it while the deck is tilting." She glances at you. "You do that, too. Find the crack, then decide whether to mend it or make a joke. I haven't worked out which is more dangerous."''',
              c("Say that a joke can keep fear from making the decision for you.", "course_talk"),
              c("Tell her you sometimes make the wrong call and have to live with the cost.", "course_talk"),
              c("Ask whether she invited you to talk about your flaws or hers.", "course_talk")),
            n("course_talk", "Mielarah", '''"Mine, mostly." She stops where the quay bends and looks back at Starcatcher. A repair crew is hauling canvas into place. "The crew meeting didn't change the past. One sailor still left. Two asked to stay. The rest are waiting to see whether I keep the rule when we hit trouble."
You ask if she will.
"I don't know." The words come quickly, defensive before they are honest. "I want to say yes. I can picture the next crisis, though, and hear myself deciding there's no time. If I break the rule, they will be right to leave. I won't ask you to tell me it will be different." She rubs at a stain on her cuff. "I don't know how to be a captain without keeping the final choice. I don't know if that's the same thing as keeping the ship alive."''',
              c("Tell her you cannot promise the crew will forgive her, but they deserve to see what she does next.", "course_response"),
              c("Say you understand why she keeps command, but won't call coercion harmless.", "course_response"),
              c("Tell her she is trying to make you answer for a decision only she can make.", "course_response")),
            n("course_response", "Mielarah", '''She turns toward you, eyebrows raised. "That's a fair complaint. I asked for a day with you and spent half of it asking you to hold the parts of me I don't like. I can manage my own ugly thoughts, thank you." The last words are barbed; she is embarrassed, and she wants you to notice without saying so.
You tell her you wanted the day. You also wanted to see the woman who can spend twenty minutes describing a cracked pulley without making it sound like a confession.
That gets a real laugh from her. "You make the strangest attempts at flattery."
"Did it work?"
"A little." She steps closer, shoulder brushing yours. "Don't look so pleased. I am still deciding what to do with you."''',
              c("Ask if you may kiss her, and wait for her answer.", "quay_kiss_question", flags=("mielarah.opening.quay_attraction_named",)),
              c("Let the shoulder touch be enough and keep walking.", "quay_walk_on", flags=("mielarah.opening.quay_attraction_named",)),
              c("Tell her you would rather stop here than turn affection into an expectation.", "quay_day_exit", flags=("mielarah.opening.quay_attraction_named",))),
            n("quay_kiss_question", "Mielarah", '''Mielarah studies your face, then the open strip of quay behind you. "Yes. Here. One kiss, and then we keep walking unless I say otherwise." She puts two fingers under your chin and lifts it, making the answer hers in both word and gesture.
Her mouth is warm and sure. She kisses you with a captain's decisiveness, then breaks away before you can pull her closer. For a moment she keeps her forehead against yours.
"You ask as if you expect a no," she says.
"I do."
"Good. Anyone who expects me to say yes because I said it once has no business on my deck." Her thumb catches the corner of your mouth. "There. Now we can argue about the pulley."''',
              c("Accept the limit and return to the walk.", "quay_walk_on", flags=("mielarah.opening.quay_kissed",)),
              c("Ask for another kiss and wait for her answer.", "quay_second_question", flags=("mielarah.opening.quay_kissed",)),
              c("Tell her you want to stop here, and give her room to step away.", "quay_walk_on", flags=("mielarah.opening.quay_stopped",))),
            n("quay_second_question", "Mielarah", '''"You may ask." The corner of her mouth rises. "Do not make me answer before I've decided." She lets you wait. The seconds stretch while the riggers shout over one another behind you. Then she takes your coat in both hands and draws you in.
This kiss is slower, and she keeps one hand at the back of your neck as if learning the shape of you by touch. You feel her smile against your mouth before she lets you go.
"That's enough." Her voice is rough and amused. "If I keep doing that, I'll miss the argument I planned to have with you."
"Which argument?"
"I'll invent one. I'm very good at it."''',
              c("Leave the second kiss where she left it and walk beside her.", "quay_walk_on", flags=("mielarah.opening.quay_second_kiss",)),
              c("Tell her you would like to stop touching and return to the ship.", "quay_walk_on", flags=("mielarah.opening.quay_stopped",))),
            n("quay_walk_on", "Narrator", '''{n}You walk the length of the quay with Starcatcher always in sight. Mielarah points out the repairs she would redo herself, and you let her be wrong about one small thing until she notices and makes you admit it. Neither of you asks the other to settle the amulet case, the curse, or the next voyage.{/n}
At the gangplank she doesn't invite you aboard. She brushes two fingers over your sleeve where she touched you earlier.
"I want to see you again," she says. "I haven't decided what that means. Don't make me regret being honest before I've had time to be difficult about it."''',
              c("Say you will wait for her next invitation, and leave the ship hers.", flags=("mielarah.opening.quay_day_complete", "mielarah.opening.following_day_pending")),
              c("Ask whether she wants another day or a proper courtship; let her defer the answer.", "quay_defer")),
            n("quay_defer", "Mielarah", '''"A proper courtship." She tastes the phrase as if it might be an unfamiliar wine. "That sounds like forms, flowers, and someone asking my first officer for permission. I have no use for the first two, and the third would end badly for all of us."
She lifts her chin, deciding. "Another day first. Let me find out whether I want the word before you start polishing it." Her grin returns, smaller now. "You can bring a chart. I reserve the right to tell you it is upside down."''',
              c("Agree to another day on her terms.", flags=("mielarah.opening.quay_day_complete", "mielarah.opening.following_day_pending")),
              c("Say you want a defined relationship and will wait while she decides if she wants the same.", "quay_day_exit", flags=("mielarah.opening.quay_day_deferred",))),
            n("quay_day_exit", "Narrator", '''{n}The day ends without a bargain. Mielarah accepts your answer without pursuit or reproach, and returns to the work waiting aboard Starcatcher. A future invitation remains hers to make.{/n}''',
              c("Leave without claiming another meeting.", flags=("mielarah.opening.quay_day_deferred",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.followup_by_her", "mielarah.opening.crew_day_pending"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24,
        last=4,
        optional=True,
        Relationship="mielarah.opening",
        ManualOnly=True,
        Remote=True,
    ),
])

SCENES.extend([
    scene(
        "mielarah.opening.the_repair_ledger", "A course freely chosen", "Mielarah", 4,
        "Review Starcatcher's repair ledger",
        [
            n("ledger_start", "Narrator", '''{n}The next note is folded around a splinter from a broken spar. It gives you a time and a counting room; the last line reads: Bring your own arithmetic. Mine has been insulted.{/n} Mielarah has spread three invoices across the table. "You wanted another day. I have a day. This is not a date. It is numbers." She pushes the pages over, then keeps one finger on the manifest. "That stays mine."''', c("Compare the invoices and ask before changing an entry.", "ledger_read"), c("Tell her to pay the yard first, then question the charge.", "ledger_order"), c("Decline without turning the invitation into a grievance.", flags=("mielarah.opening.following_day_declined",))),
            n("ledger_read", "Narrator", '''The first invoice bills for canvas by the bolt; the second charges for the same measure as a finished panel. Mielarah leans over your shoulder, hair brushing your temple. Neither of you comments. "The yard counted offcuts as whole panels." She checks the manifest, then stops. "No. That line is mine. I ordered the reserve canvas and forgot to mark it." Her jaw tightens. "Write that down. I made the error. Don't make it noble."''', c("Record her correction exactly.", "ledger_continue", flags=("mielarah.opening.ledger_honest",)), c("Quietly shift the charge to the yard so her crew keeps the reserve.", "ledger_cover")),
            n("ledger_order", "Mielarah", '''"No." She takes the invoice back. "I pay when I owe. I challenge a charge when I don't. If you want to order people around, buy a ship." Her voice rises, then she catches herself and studies the figures. "The yard can wait an hour. I cannot keep a ship honest by teaching it to swallow every bill."''', c("Ask her to show you the disputed measure.", "ledger_read", flags=("mielarah.opening.ledger_rebuked",)), c("Insist your rank makes the order sensible.", "ledger_end")),
            n("ledger_cover", "Mielarah", '''"That is a polished way to call it a lie." She slides the manifest out of reach. "I have paid for a lie before. I've made people wear one because I liked the result. You don't get to help me do it tidily." She writes her name beside the reserve canvas charge, too hard. "There. My mistake."''', c("Leave the yard's charge intact and record her name.", "ledger_continue", flags=("mielarah.opening.ledger_honest", "mielarah.opening.ledger_conflict"))),
            n("ledger_continue", "Narrator", '''One charge belongs to the yard, one to Mielarah, and the rest survive a second look. She catches you rounding a figure up and taps the column with her knife handle. "You were getting comfortable. Don't." At last she gets the clerk to sign the correction. "The sail trial is tomorrow. Passenger rail only. If I give an order, you do not improve it." Her eyes slip to your mouth, then away. "Come anyway, if you want."''', c("Accept her limits and the trial invitation.", flags=("mielarah.opening.sail_trial_pending", "mielarah.opening.following_day_complete")), c("Ask for a private meeting instead.", "ledger_private"), c("Thank her for the work and keep this professional.", "ledger_end")),
            n("ledger_private", "Mielarah", '''"No. Not because I don't want to. Because I do, and I won't let that make me careless with my crew." Her blush annoys her; you can see it in the quick scowl. "Trial first. You can decide you were only interested in me at close range, or you can wait until tomorrow."''', c("Accept the trial and leave the next invitation to her.", flags=("mielarah.opening.sail_trial_pending", "mielarah.opening.following_day_complete")), c("Say you won't wait for an answer she hasn't offered.", "ledger_end")),
            n("ledger_end", "Narrator", '''{n}The ledger closes. Mielarah does not ask you to reconsider or follow you out. Repaired canvas snaps once in the wind beyond the window.{/n}''', c("Leave without another meeting.", flags=("mielarah.opening.following_day_declined",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.following_day_pending", "mielarah.opening.quay_day_complete"),
        forbids=("mielarah.opening.closed", "mielarah.opening.following_day_declined", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_sail_trial", "A course freely chosen", "Mielarah", 4,
        "Observe Starcatcher's sail trial",
        [
            n("trial_start", "Narrator", '''{n}At the appointed hour, Starcatcher puts out beneath a patched forecourse. You stand behind the passenger rail, hands visible. A seam pulls sideways as a gust catches the sail. Mielarah keeps one hand at the wheel. "You are not steering. You are not advising the deck crew. Watch the leech line. If I ask, answer. Otherwise keep your opinions in your skull." The crew moves at her call, not yours. Then a loose line begins to whip against the mast.{/n}''', c("[Perception DC 22] Call out the seam before the line catches the spar.", check=dict(Skill="SkillPerception", DC=22, Success="trial_success", Failure="trial_failure", CommanderOnly=True)), c("Stay at the rail and let the captain handle her test.", "trial_silent"), c("Cross the rail and grab the line without permission.", "trial_overstep")),
            n("trial_success", "Narrator", '''You point to the seam. "That stitch is walking. The line will foul the spar if he hauls there." Mielarah glances once. "Ease the sheet. Jori, lower cleat. Now." The sailor moves. A second gust strikes before the line is secured; Mielarah turns into it with a curse and steadies the ship. "Good eye," she says when the canvas settles. "Bad timing on the shout. Say the danger first next time."''', c("Take the correction without defending yourself.", "trial_debrief", flags=("mielarah.opening.trial_helped",)), c("Point out that your warning gave her time.", "trial_friction")),
            n("trial_failure", "Mielarah", '''You call for the port line. The deckhand hauls. The seam pulls harder; the spar cracks and everyone ducks. "Wrong side! Let it go!" Mielarah cuts across your call. The line tears free over the water. She brings the ship around before the gust can turn damage into a fall. "You guessed. Say that." She is angry because the guess could have hurt someone, not because you embarrassed her.''', c("Admit it and ask what sign you missed.", "trial_debrief", flags=("mielarah.opening.trial_failed_honest",)), c("Say the deckhand should have waited for your rank.", "trial_friction")),
            n("trial_silent", "Mielarah", '''You keep to the rail. Mielarah and the deck crew spot the seam together; the line snaps free over the water. Afterward she asks, "You saw it?" You admit you were unsure. "Silence was fair, then. Next time ask me what to look at before we put canvas up." Her eyes search your face for a joke. You give her none. "You didn't help. You also didn't make it worse. I can work with that."''', c("Ask her to teach you the seam marks.", "trial_debrief", flags=("mielarah.opening.trial_observed",)), c("Thank her and leave this as a professional favor.", "trial_end")),
            n("trial_overstep", "Mielarah", '''You clear the rail before anyone can stop you. "Back. Now." A deckhand knocks your wrist aside with a belaying pin, hard enough to make the point. Mielarah leaves the wheel for one heartbeat, then takes it again. "You were told where to stand. You decided the order was decorative. Get off my ship."''', c("Leave at once; the trial and private invitation are over.", "trial_end", flags=("mielarah.opening.closed", "mielarah.opening.trial_overstepped")), c("Argue that the emergency excused you.", "trial_end", flags=("mielarah.opening.closed", "mielarah.opening.trial_overstepped"))),
            n("trial_friction", "Mielarah", '''"You helped, then wanted credit on the bridge. Or you guessed and wanted the crew to pay for your pride. Pick whichever sounds less flattering." She orders the spar inspected and sends the crew below before addressing you again. "You may stay for the inspection if you can listen. You don't get another chance to take command from my deck."''', c("Apologize for making rank the subject of her crew's risk.", "trial_debrief", flags=("mielarah.opening.trial_conflict_owned",)), c("Leave and accept that you damaged the trust she offered.", "trial_end", flags=("mielarah.opening.closed",))),
            n("trial_debrief", "Narrator", '''The sailmaker finds a bad seam and a sound spar. Mielarah asks three exact questions, then changes the plan without pretending the failure was anyone else's. When the crew disperses, she stays by the rail, a loose thread looped around one finger. "I dislike needing a second opinion. I dislike more when it is right." She looks at you, then looks away. "Storm warning tomorrow. The crew decides whether we fly. I want you there to see what my mistake looks like from the deck. Not to rescue me."''', c("Accept, with no claim on her time beyond the watch.", "trial_finish", flags=("mielarah.opening.weather_watch_pending", "mielarah.opening.trial_complete")), c("Ask whether she wants you as a companion or witness.", "trial_desire"), c("Say the trial is enough and close the professional favor.", "trial_end")),
            n("trial_desire", "Mielarah", '''She watches the crew tie down the spare line. "Both, if you can keep them separate. I want you near me. I also want someone who'll tell me when my judgment is bad." You ask what happens if you cannot. "I send you ashore." Her gaze fixes on yours. "I want you, Commander. That is not the same as trusting you with my ship. Don't confuse them because one feels better."''', c("Say you want her too and accept that trust is still being decided.", "trial_finish", flags=("mielarah.opening.weather_watch_pending", "mielarah.opening.trial_complete", "mielarah.opening.desire_named")), c("Say you want to keep this professional.", "trial_end", flags=("mielarah.opening.trial_complete",))),
            n("trial_finish", "Narrator", '''The storm warning brings a hard rain and a red line across the harbor chart. Mielarah marks the safe mooring, then scratches it out. "That channel's silted. I should have known." She looks embarrassed, then furious at being embarrassed. "Tomorrow, I take Starcatcher through the outer markers. If you come, you take orders. If I am wrong, say so once. Clearly. I will decide what to do with it."''', c("Agree to the watch and let her decide whether you stay near her.", "trial_end", flags=("mielarah.opening.weather_watch_pending", "mielarah.opening.trial_complete")), c("Decline the watch and leave the ship to her crew.", "trial_end", flags=("mielarah.opening.trial_complete",))),
            n("trial_end", "Narrator", '''{n}Starcatcher returns to its berth with the damaged sail furled. Mielarah gives no speech about what the day meant. The crew takes the ship back, and she goes with them.{/n}''', c("Leave the quay without pressing for another meeting.", flags=("mielarah.opening.trial_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.sail_trial_pending", "mielarah.opening.following_day_complete"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_weather_watch", "A course freely chosen", "Mielarah", 4,
        "Stand watch during the storm warning",
        [
            n("watch_start", "Narrator", '''{n}Rain needles the harbor. The crew has voted to take Starcatcher through the outer markers, and Mielarah has not tried to change the count. She stands in the companionway, arguing with a chart that cannot answer back. "The channel is clear if the silt report is wrong. The report is usually wrong." She looks at you. "That is not a request for reassurance."{/n}''', c("Ask what evidence she has and let her answer.", "watch_chart"), c("Tell her to trust herself.", "watch_reassure"), c("Tell her the crew has voted and she must follow.", "watch_order")),
            n("watch_chart", "Narrator", '''She points to the tidal mark and a harbor pilot's note. The figures are two hours old. You compare them with the rain line and find the wind turning faster than predicted. Mielarah follows your finger. "That gives me a narrow pass, not a safe one." She tells the crew both facts and lets them vote again. One sailor stays ashore; the rest choose the risk.''', c("Help her explain the risk plainly.", "watch_vote", flags=("mielarah.opening.watch_assisted",)), c("Leave the decision to her and the crew.", "watch_vote")),
            n("watch_reassure", "Mielarah", '''"Don't." The word cracks across the passage. She rubs her forehead, angry at the outburst. "Doubt is how I keep from running a ship onto a sandbar. I do want you here. I don't want your comfort bought with my crew's risk."''', c("Apologize, then ask to see the tide report.", "watch_chart", flags=("mielarah.opening.watch_friction",)), c("Say you meant it but won't pretend certainty.", "watch_vote", flags=("mielarah.opening.watch_friction",))),
            n("watch_order", "Mielarah", '''Her face goes still. "There. That's the sound I know." She calls the first officer up and orders the risk explained to the crew again. To you: "You don't get to spend their lives because the vote is inconvenient."''', c("Withdraw the order and stand with her.", "watch_vote", flags=("mielarah.opening.watch_rebuked",)), c("Insist she silence dissent.", "watch_end", flags=("mielarah.opening.closed",))),
            n("watch_vote", "Narrator", '''The crew votes again. Mielarah chooses the pass, with a turn-back point marked in red. The ship moves when the crew is ready. At the rail she checks every knot; one is badly tied. She curses, fixes it, then makes the sailor retie it. Not to punish him; to make sure he knows what failed. She catches your sleeve. "Stay close enough to hear me. Far enough that you can't decide to be useful without asking." Her thumb traces your cuff. "I keep thinking about your mouth. It's inconvenient."''', c("Tell her the feeling is mutual and ask before touching.", "watch_kiss", flags=("mielarah.opening.watch_desire",)), c("Say nothing and take your position.", "watch_silence"), c("Tell her she can have you whenever she wants.", "watch_boundary")),
            n("watch_kiss", "Mielarah", '''"Ask, then." You ask if you may kiss her. She answers by taking your face between both hands and kissing you hard enough to steal the next sentence. Her mouth is salt and warm breath; her fingers press your jaw as if checking a knot. Then she lets go. "That is all before we cast off." Her mouth curves. "You have a whole ship to distract you."''', c("Accept her answer and return to the rail.", "watch_sail", flags=("mielarah.opening.watch_kissed",)), c("Ask for more and accept her answer.", "watch_more")),
            n("watch_more", "Mielarah", '''"No. I said all." She steps back; her face returns to captain's focus. "You can be disappointed. You cannot make that my problem while the crew waits."''', c("Apologize and return to the rail.", "watch_sail", flags=("mielarah.opening.watch_stopped",)), c("Press her again.", "watch_end", flags=("mielarah.opening.closed",))),
            n("watch_boundary", "Mielarah", '''She pulls her sleeve free. "I am not a berth you can reserve." The sharpness arrives first, the hurt after it. "I said I was thinking about you. I did not hand you my choices."''', c("Take the correction and return to the rail.", "watch_sail", flags=("mielarah.opening.watch_repaired",)), c("Argue that she invited the attention.", "watch_end", flags=("mielarah.opening.closed",))),
            n("watch_silence", "Narrator", '''She studies you, then nods. "Good. I might have kissed you if you asked. I might have wanted to be left alone. Both can be true." She turns toward the deck before either of you can soften the words.''', c("Take your place and wait for her next word.", "watch_sail", flags=("mielarah.opening.watch_respected",))),
            n("watch_sail", "Narrator", '''The current pushes hard against the hull. Mielarah sees the shift late, swears, and cuts the sail. Starcatcher shudders but clears the shoal. She does not call it a victory. Back at the berth, she writes the actual depth in the pilot's ledger and signs her name beneath the correction. She looks tired, frightened, and annoyed that you saw both. "I want you in my cabin tonight. An hour. No crew, no chart. I may change my mind. You may too."''', c("Accept, and ask again once you are there.", "watch_private", flags=("mielarah.opening.cabin_invited",)), c("Decline the cabin and offer a quiet walk.", "watch_walk"), c("Ask for a commitment before intimacy.", "watch_defer")),
            n("watch_private", "Narrator", '''{n}Her cabin door stays unlatched. Mielarah pours two fingers of brandy and drinks hers without ceremony. "I don't want to discuss the storm until morning. Don't tell me I was brave. And I want you to touch me, if I still want it when you ask." She sets down the glass. "Ask."{/n}''', c("Ask to kiss her and wait.", "watch_intimate", flags=("mielarah.opening.intimacy_questioned",)), c("Change your mind and leave gently.", "watch_end", flags=("mielarah.opening.intimacy_declined",))),
            n("watch_intimate", "Mielarah", '''"Yes." She closes the distance herself. The first kiss is slow, almost cautious; the next has the impatient edge she puts into an order. She takes your hand and places it at her waist, then covers it with hers. "Here. Stay until I move it." Her skin is warm beneath damp cloth. The rain drums above the cabin roof. She draws you closer, laughs when your belt catches on the chair, and swears at the chair as if it planned the ambush. Her hands learn your shoulders; yours follow only where she guides them. When she kisses you again, her composure breaks and she grins against your mouth. "Don't look smug. This is a decision about tonight." She rests her forehead on yours. "Ask me in the morning. I may tell you to get out."{/n}''', c("Stay with her and let the scene fade with her permission.", "watch_end", flags=("mielarah.opening.intimate_night",)), c("Pause and ask whether she wants to stop.", "watch_stop")),
            n("watch_stop", "Mielarah", '''She stills. You ask whether she wants to stop. For a moment she looks almost angry, then the tension leaves her mouth. "Ask me that more often than you think necessary." She draws you back by your collar. "Now hush." The rest belongs to the two of you, not to any bargain about tomorrow.''', c("Continue only while she keeps choosing it.", "watch_end", flags=("mielarah.opening.intimate_night",))),
            n("watch_walk", "Narrator", '''Mielarah buttons her coat. You walk the quay in rain without touching. She tells you about a storm that took a mast and nearly a crew, then admits her own wrong calculation and the sailor who corrected it. She does not make herself the hero. At the berth she says, "Thank you for not turning a no into a negotiation." Then she leaves before you can decide whether it was an invitation.''', c("Leave the next meeting to her.", "watch_end", flags=("mielarah.opening.cabin_declined",))),
            n("watch_defer", "Mielarah", '''"Then no cabin tonight." Her voice cools. "I offered an hour, not a contract. If you need a promise before you can want me, say so plainly. I won't mock you. But don't make me trade one for the other."''', c("Accept her distinction and walk instead.", "watch_walk"), c("End the courtship here.", "watch_end", flags=("mielarah.opening.closed",))),
            n("watch_end", "Narrator", '''{n}The watch ends. Mielarah has not forgiven her past, cured her curse, or promised what she will choose next. At dawn she is back on deck, arguing with the quartermaster about a knot that is plainly tied correctly.{/n}''', c("Let morning begin without claiming an answer.", flags=("mielarah.opening.watch_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.weather_watch_pending", "mielarah.opening.trial_complete"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_departure_notice", "A course freely chosen", "Mielarah", 4,
        "Answer the crew's departure notice",
        [
            n("departure_start", "Narrator", '''{n}Two days after the storm, a folded notice waits beneath your door. Jori, Starcatcher's senior deckhand, and three others have asked to leave at the next port. No accusation is written. No reason is needed; the choice is theirs.{/n} Mielarah stands on the quay beside a coil of line, the notice creased in her fist. "I can order them to finish the voyage. I can pay them out. I can tell the truth and let them decide. I have a talent for finding the answer that costs somebody else."''', c("Ask to speak with Jori only if he wants it.", "crew_voice"), c("Ask Mielarah what she intends before advising her.", "captain_choice"), c("Tell her the ship needs experienced hands and she must keep them.", "crew_order")),
            n("crew_voice", "Narrator", '''Jori agrees to meet at the counting room, not aboard. Mielarah leaves you alone with him. "I knew about the amulets. I didn't know what it felt like when she used them. I'm leaving because I can." You ask whether better notice would change his mind. "No. Don't bargain for me. Tell her I won't take a bonus to stay."''', c("Carry his answer exactly.", "carry_answer", flags=("mielarah.opening.jori_answered",)), c("Ask whether he might stay if she promised never to use them.", "crew_order")),
            n("captain_choice", "Mielarah", '''"I intend to let them leave." She says it too quickly, then stops. "I also want to ask them to stay. Both are true." If she promises never to use the amulets, she may break that promise in a crisis. If she reserves the right to use them, she asks the crew to stay under a captain who can take their minds. "Have you got an answer that isn't just a prettier lie?"''', c("Say you have none; ask what they told her.", "crew_voice"), c("Suggest a written rule with a crew veto and emergency exception.", "rule_debate"), c("Tell her the crew's fear matters less than survival.", "crew_order")),
            n("crew_order", "Mielarah", '''"No." She steps closer, quiet and dangerous. "You don't get to enlist them for me." She orders the first officer to pay their wages through departure. Then to you: "You can stand beside me when you disagree. You cannot make my crew the price of keeping me."''', c("Withdraw the order and tell her you were wrong.", "crew_voice", flags=("mielarah.opening.commander_corrected",)), c("Defend your advice and lose the relationship.", "departure_end", flags=("mielarah.opening.closed", "mielarah.opening.crew_lost"))),
            n("carry_answer", "Mielarah", '''She listens, then unfolds the notice. "Good. I wanted you to find a loophole. I hate that I wanted it." She signs the wage release. "Jori told me to use the amulet last time. He was there when it worked. He can still leave." She gives the paper to her first officer, then asks whether you will attend the crew meeting.''', c("Ask if she wants you there.", "crew_meeting", flags=("mielarah.opening.crew_release_signed",)), c("Leave her to speak with them alone.", "crew_meeting", flags=("mielarah.opening.crew_release_signed", "mielarah.opening.commander_absent"))),
            n("rule_debate", "Mielarah", '''"A veto during a crisis is a vote held too late." She laughs harshly. "And the exception eats the rule the first time I get scared." She starts a new page. "I can tell them when I carry the case. Anyone can refuse a voyage before we cast off. I cannot promise never to use it. They can decide whether those terms are enough."''', c("Help her write the terms plainly.", "crew_meeting_unbriefed", flags=("mielarah.opening.rule_written",)), c("Tell her to keep the amulets sealed whatever happens.", "rule_debate_end")),
            n("rule_debate_end", "Mielarah", '''She reads your proposed promise and crosses it out. "No. That's a promise I might break." She folds the paper. "I won't ask them to sign a rule I don't trust myself to keep."''', c("Let the crew answer her real terms.", "crew_meeting_unbriefed", flags=("mielarah.opening.rule_refused",)), c("Call her weak for refusing a clean promise.", "departure_end", flags=("mielarah.opening.closed", "mielarah.opening.crew_lost"))),
            n("crew_meeting", "Narrator", '''The crew gathers on the quay, with Mielarah below the gangplank instead of above them on deck. She says what she used, why she used it, and what she cannot promise. Their wages are paid through departure. Jori takes the notice and puts it in his pocket. "I'm still going." Two others stay. One asks to inspect the amulets before the next voyage. Mielarah hands him the case key. Afterward she says, "I hated you in there for half a minute. Then I hated myself for wanting you to make this easy."''', c("Say you wanted it easy too, but it was their choice.", "consequence", flags=("mielarah.opening.crew_decision_witnessed",)), c("Tell her you should have stayed out of the meeting.", "consequence", flags=("mielarah.opening.crew_decision_witnessed",)), c("Say their choice proves she was right all along.", "crew_wrong")),
            n("crew_meeting_unbriefed", "Narrator", '''You did not speak with Jori alone, so you do not carry a private answer to Mielarah. At the quay meeting she explains the spell, the wages, and the terms she cannot promise. Jori listens, then says in front of the others, "I'm still going." Two sailors remain. One asks to inspect the amulets before the next voyage. Mielarah hands him the case key. She does not claim the room has forgiven her. Afterward she says, "I hated you in there for half a minute. Then I hated myself for wanting you to make this easy."''', c("Say you wanted it easy too, but it was their choice.", "consequence", flags=("mielarah.opening.crew_decision_witnessed",)), c("Tell her you should have stayed out of the meeting.", "consequence", flags=("mielarah.opening.crew_decision_witnessed",)), c("Say their choice proves she was right all along.", "crew_wrong")),
            n("crew_wrong", "Mielarah", '''"No. It proves they chose with more information." She takes back the case key and locks it herself. "Don't turn their decision into a verdict for me. I have enough trouble doing that on my own."''', c("Let the answer stand without a victory speech.", "consequence", flags=("mielarah.opening.crew_decision_witnessed",)), c("Insist she should take the win.", "departure_end", flags=("mielarah.opening.closed",))),
            n("consequence", "Mielarah", '''She rubs the notice until the paper softens. "I don't want another person who tells me I'm good underneath it all. I don't want someone who thinks I'm a monster and therefore predictable." You ask what she wants. "A person who can sit with the fact that I chose. And tell me when I'm about to choose badly again." She lets the paper go. "Come on the next short voyage. Not as commander or judge. I want you there because I want you, and because you notice when the current changes."''', c("Accept the voyage and its ordinary risks.", "voyage_invited", flags=("mielarah.opening.second_voyage_pending", "mielarah.opening.crew_arc_complete")), c("Accept as a friend, without romance.", "voyage_invited", flags=("mielarah.opening.second_voyage_pending", "mielarah.opening.crew_arc_complete", "mielarah.opening.friendship_only")), c("Decline and let her captain without you.", "departure_end", flags=("mielarah.opening.crew_arc_complete",))),
            n("voyage_invited", "Narrator", '''{n}The voyage is three days, with a harbor call before the outer shoals. Mielarah sends the route and leaves the passenger berth unassigned until you answer. The crew has made its own decision. She has made hers. Neither settles whether the amulets stay sealed next time.{/n}''', c("Confirm the berth and wait for departure day.", flags=("mielarah.opening.voyage_accepted",))),
            n("departure_end", "Narrator", '''{n}The crew keeps the wages Mielarah promised, whether they remain or leave. She returns to Starcatcher without asking you to follow. Her decision has cost her people and changed the next voyage; it has not made her answer smaller.{/n}''', c("Leave without claiming another invitation.", flags=("mielarah.opening.crew_arc_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.watch_complete"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=48, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_outer_shoals", "A course freely chosen", "Mielarah", 4,
        "Sail with Mielarah through the outer shoals",
        [
            n("shoals_start", "Narrator", '''{n}Starcatcher leaves at dawn. You are passenger, not officer; the berth notice says so in Mielarah's blocky hand. The crew is smaller now. Jori's station is filled by a young sailor who keeps checking the empty rail.{/n} At midday, fog closes across the water. The pilot's marks disappear, and a squall presses from the east. Mielarah calls for the amulet case. Two crew members go still. She notices. For one heartbeat she looks at you instead of the wheel.''', c("Tell her to ask the crew before opening the case.", "crew_vote"), c("Say the decision is hers, but the crew should see it.", "open_case"), c("Tell her to use it now and explain later.", "use_order"), c("Stay silent and watch what she chooses.", "captain_decides")),
            n("crew_vote", "Mielarah", '''She looks at the deckhands, not you. "The spell could make you obey a steering order. You would remember it. I don't know what else it would take." The young sailor swallows. Another asks whether they can refuse. "Yes. You can leave at the next port, and you can refuse now." The first sailor shakes his head. "I won't be compelled."''', c("Help her repeat the options without pressure.", "captain_decides", flags=("mielarah.opening.crew_refusal_heard",)), c("Tell the crew the captain knows best.", "use_order")),
            n("open_case", "Narrator", '''Mielarah unlocks the case and lays the amulets in plain view. She describes the spell without softening the memory loss or pretending she can predict every effect. The crew can refuse. One does. A second asks her to use it only on herself if she loses the wheel. Mielarah shuts the case. "No. I will not promise a spell I cannot direct that precisely."''', c("Leave the case closed and take the longer marked route.", "captain_decides", flags=("mielarah.opening.case_disclosed",)), c("Ask her to choose with the limits she actually has.", "captain_decides", flags=("mielarah.opening.case_disclosed",))),
            n("use_order", "Mielarah", '''Her eyes snap to you. "You don't command my crew." The young sailor steps away from the case. Mielarah looks at the compass, then at the fog. "I will not cast on someone who refused." She drops the amulets in the case and orders the ship onto the longer route. It will cost a day, perhaps two.''', c("Accept her decision and help mark the longer route.", "long_route", flags=("mielarah.opening.commander_overruled",)), c("Argue until the crew chooses a route.", "shoals_fracture", flags=("mielarah.opening.closed",))),
            n("captain_decides", "Narrator", '''Mielarah closes the case. "No spell." She calls the crew to the chart and sets the longer route. It carries a cost: one late delivery, two extra nights at sea, and lost payment. No one is forced to obey. She accepts the loss without turning it into a test of loyalty.''', c("Offer to share the lost passage cost.", "long_route", flags=("mielarah.opening.no_spell",)), c("Ask whether she is certain about the delay.", "long_route", flags=("mielarah.opening.no_spell",))),
            n("long_route", "Narrator", '''The squall pushes them wide of the shoals. Starcatcher's patched sail strains, but the crew takes each line in turn. Mielarah stays at the wheel through the first night, then lets the new sailor take it while she sleeps for an hour. She wakes irritated at the relief she feels and sends him back to his station before he can thank her. At harbor, the delay costs the contract. Mielarah reads the penalty aloud and signs it herself. "That's my call. Take it up with me, not the person who refused the spell." The young sailor does not apologize.''', c("Tell her she made the right choice.", "arrival"), c("Say you would have chosen differently but will stand by her call.", "arrival"), c("Ask whether she regrets losing the contract.", "arrival")),
            n("arrival", "Mielarah", '''"Of course I regret it." She folds the penalty notice. "I also regret what I might have done to keep it. Those aren't equal regrets." She pulls you aside. "You stayed with a choice that cost us. You didn't make me thank you for it." She puts a hand on your chest, then removes it before you can cover hers. "I want you beside me after this voyage. I want days this boring in my life."''', c("Say you want that life, with the amulets and arguments in it.", "shared_end", flags=("mielarah.opening.future_chosen",)), c("Ask for more time before calling it a life together.", "deferred_end", flags=("mielarah.opening.future_deferred",)), c("Say you cannot accept that she may use the spell again.", "separate_end", flags=("mielarah.opening.closed",))),
            n("shared_end", "Mielarah", '''She kisses you once, hard and brief, then checks the mooring line. "Good. Don't start writing our future before we unload the cargo." She takes your hand in full view of the crew and does not pretend the gesture makes them approve of her. "We have a week before the next voyage. Come to dinner. Leave your rank at the door. Bring an appetite."''', c("Accept the invitation and imperfect future she offered.", "ending", flags=("mielarah.opening.route_open_ending",))),
            n("deferred_end", "Mielarah", '''"Then we wait." Her smile is crooked, disappointed but not wounded. "I can want you without making the answer easy. I'll send another note when I know the departure date. If you still want to come, say so then."''', c("Keep the correspondence open and let time answer.", "ending", flags=("mielarah.opening.route_deferred_ending",))),
            n("separate_end", "Mielarah", '''"Then we stop here." She takes the penalty notice back to the crew. She does not ask you to change your mind or offer to become safer to love. You leave at the next port, knowing desire could not erase the difference in your judgment.''', c("End the courtship without denying what mattered.", "ending", flags=("mielarah.opening.route_closed_ending",))),
            n("shoals_fracture", "Narrator", '''{n}Mielarah orders the Commander ashore at the next safe port. The crew takes the longer route. The voyage continues without you, and the contact closes.{/n}''', c("Leave the ship and respect the ending.", flags=("mielarah.opening.route_closed_ending",))),
            n("ending", "Narrator", '''{n}Starcatcher clears the outer shoals. The crew keeps its disagreement, Mielarah keeps the key to the amulet case, and the Commander leaves with a future offered rather than won. The next voyage remains another decision.{/n}''', c("Let the route end with her invitation unanswered until you choose.", flags=("mielarah.opening.outer_shoals_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.voyage_accepted", "mielarah.opening.crew_arc_complete"),
        forbids=("mielarah.opening.closed", "mielarah.opening.friendship_only", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=72, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_outer_shoals_friendship", "A course freely chosen", "Mielarah", 4,
        "Join Starcatcher as a friend",
        [
            n("friend_shoals_start", "Narrator", '''{n}Mielarah leaves the berth notice on the table between you. "You said friend. I heard you." The ship still needs to make the outer passage, and the crew has agreed to take the longer route after the lost contract. "Come if you want to see the coast. No hidden test. I am not asking you to reconsider before we reach harbor."{/n}''', c("Join the passage as a friend and passenger.", "friend_crisis"), c("Stay ashore and let the friendship continue by letter.", "friend_letter", flags=("mielarah.opening.friendship_ashore",))),
            n("friend_crisis", "Narrator", '''Fog closes across the water, and the new sailor asks Mielarah to slow the ship until the marker can be seen. She does. The delivery will be late again. Nobody asks whether the Commander agrees. At the rail, Mielarah points out a break in the clouds where the coast is visible. "That is why I wanted you along. You notice the small things. It is useful in a friend."''', c("Help mark the coast and keep the exchange friendly.", "friend_arrival"), c("Tell her you are glad she asked you without another meaning attached.", "friend_arrival")),
            n("friend_arrival", "Mielarah", '''At harbor she asks you to carry a corrected chart to the pilot, then takes the ship's accounts below. When she comes back, she has ink on her thumb. "The captain's life is glamorous." She smiles, but does not linger over the joke. "Write when you like. I will answer when I can. No schedule, no promise beyond that."''', c("Agree to keep the letters friendly and ordinary.", "friend_letter", flags=("mielarah.opening.friendship_voyage_complete",))),
            n("friend_letter", "Narrator", '''{n}The next letter contains a sketch of the coast, two lines about the late delivery, and a question about the book you left in the counting room. Mielarah does not reopen the courtship question. The correspondence has room to continue because the answer you gave was allowed to stand.{/n}''', c("Reply with a story from the road, as her friend.", flags=("mielarah.opening.friendship_correspondence_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.voyage_accepted", "mielarah.opening.crew_arc_complete", "mielarah.opening.friendship_only"),
        forbids=("mielarah.opening.closed", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=72, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_week_on_shore", "A course freely chosen", "Mielarah", 4,
        "Share dinner with Mielarah after the voyage",
        [
            n("shore_start", "Narrator", '''{n}The dinner is in a cramped room above the sailmaker's shop. Mielarah chose it because no one aboard Starcatcher can interrupt, and because the owner does not care who commands a ship. She has changed into a dark red dress, cut for movement, with the burn on one knuckle and a smudge of tar still under her thumbnail. She catches you noticing. "If you say I look beautiful, I'll ask what you want."{/n}''', c("Say you like the dress and ask what she wants from tonight.", "her_answer"), c("Say she looks beautiful and accept that she may challenge it.", "beauty"), c("Keep it friendly and ask about the next voyage.", "voyage_talk")),
            n("beauty", "Mielarah", '''She leans back, considering. "I want to believe you. I also know how useful it is to call a woman beautiful when you want her to stop asking difficult questions." She takes your hand and turns it palm up, inspecting the callus at your thumb. "You have one. So you do some work yourself." Her thumb moves over it once. "That helps."''', c("Tell her the dress is striking, but you meant the woman wearing it.", "her_answer"), c("Laugh and ask her what she actually wants.", "her_answer")),
            n("voyage_talk", "Mielarah", '''"The next voyage can wait a week. Longer if the new crew needs it." She cuts the meat with a sailor's economy. "The late contract took most of the profit. I can pay the crew, but the new sail will have to wait." She says it without asking you to repair her finances. Then she looks up. "You could still go. You have people who need you elsewhere. I won't call it abandonment if you do."''', c("Say you want to stay for the week and see what ordinary life looks like.", "her_answer", flags=("mielarah.opening.shore_week_chosen",)), c("Say you will leave tomorrow, but want to write.", "departure_letter", flags=("mielarah.opening.shore_week_deferred",)), c("Offer to pay for the sail as a gift.", "gift_reaction")),
            n("gift_reaction", "Mielarah", '''"No." She sets down the knife. "I am not taking your money for my ship. If you want to help, lend it on paper at a rate I can refuse, or keep your purse closed. Do not buy yourself a place in my life." She lets the silence stretch. "Now tell me if you meant it as help or as an excuse to stay."''', c("Withdraw the offer and choose the week without a price.", "her_answer", flags=("mielarah.opening.shore_week_chosen",)), c("Ask her to name terms for a real loan.", "loan_terms"), c("Say you meant to purchase certainty and end the evening.", "shore_end", flags=("mielarah.opening.closed",))),
            n("loan_terms", "Mielarah", '''She takes a scrap of paper and writes an amount, a due date, and no interest. "There. You may lend this, or not. I can wait for the sail." She pushes the paper across. "If you accept, you get a receipt. No cabin key, no extra vote, no claim on my next free evening."''', c("Make the loan on those terms, then choose the week together.", "her_answer", flags=("mielarah.opening.sail_loaned", "mielarah.opening.shore_week_chosen")), c("Decline and leave her to arrange the sail herself.", "her_answer", flags=("mielarah.opening.shore_week_chosen",))),
            n("her_answer", "Mielarah", '''"I want to eat without discussing the ship for ten minutes." She takes a sip of wine. "Then I want to know whether the Commander is a person when no one needs saving." Her boot nudges yours beneath the table, deliberate enough that you notice, slight enough that you can pretend otherwise. "And I want you to stop looking as if every answer might be a trap."''', c("Tell her you are nervous because you want her, not because you expect a reward.", "desire_answer"), c("Ask what she does when no one is asking for her command.", "ordinary_answer"), c("Say you would rather keep the evening friendly.", "shore_end", flags=("mielarah.opening.shore_friendship",))),
            n("ordinary_answer", "Mielarah", '''"I sleep. Badly, lately." She looks toward the window. "The curse has been quiet for three days. That means nothing. I have learned to enjoy the quiet without pretending it is a cure." She catches your glance and scowls. "Do not make a face at me. I'm not asking you to solve it."''', c("Ask what she wants from you when the curse returns.", "curse_talk"), c("Tell her you can sit with the uncertainty if she wants company.", "desire_answer")),
            n("curse_talk", "Mielarah", '''"I want you not to decide what I need before I say it." She turns the wineglass by its stem. "Sometimes I want help. Sometimes I want the room to myself. Sometimes I want to be held and hate that I want it. The curse doesn't get to answer for me, even when it is the loudest thing in the room."''', c("Ask her what would help tonight.", "desire_answer", flags=("mielarah.opening.curse_terms_heard",)), c("Tell her you will keep your distance unless invited.", "desire_answer", flags=("mielarah.opening.curse_terms_heard",))),
            n("desire_answer", "Mielarah", '''She gives a small, tired smile. "Good. You're allowed to want something too. I don't need a saint. I need someone who can say what he wants and survive my answer." You tell her you want her, and that you want to keep learning the person who can be angry with you and still reach for your hand. Her expression goes still. Then she slides her boot along yours again. "I can work with that."''', c("Ask if she wants to come back to your room or hers.", "evening_choice"), c("Ask her to walk with you and leave the night open.", "walk_after_dinner"), c("Tell her the answer is enough for tonight.", "shore_end", flags=("mielarah.opening.desire_acknowledged",))),
            n("evening_choice", "Mielarah", '''"Mine." She stands and puts on her coat. "I want my bed, my door, and the option to throw you out of both." She says it lightly, but waits while you answer. The room above the shop is small; her chart bag occupies the chair and a pair of boots block the hearth. She kisses you before you can comment on the accommodations, then laughs when you nearly knock over the washbasin. The rest of the evening is private. When she asks you to stay, it is an invitation for that night, not a promise to repeat it.''', c("Stay, and let her decide when the night ends.", "shore_end", flags=("mielarah.opening.shore_intimate", "mielarah.opening.desire_acknowledged")), c("Kiss her goodnight and return to your own room.", "shore_end", flags=("mielarah.opening.desire_acknowledged",))),
            n("walk_after_dinner", "Narrator", '''{n}You walk beside the harbor. Mielarah tells you the name of each ship she once wanted to steal and the one she actually did steal, then admits the second was a mistake. When she stops beneath the lantern, she takes your hand and kisses the back of it, returning the small courtesy from the quay with a captain's amused precision. "Do not make a poem out of this. I will mock the meter."{/n}''', c("Tell her you will remember the walk without turning it into a promise.", "shore_end", flags=("mielarah.opening.desire_acknowledged",))),
            n("departure_letter", "Mielarah", '''"Then go tomorrow." She folds the route note and gives it back. "I will write when I have something to say, not because a schedule says I owe you a letter." She stands, then kisses your cheek, so briefly that you might have missed it if she had not watched you notice. "There. Something to remember on the road. Don't let it make you stupid."''', c("Leave at dawn and keep the correspondence open.", "short_visit_end", flags=("mielarah.opening.desire_deferred",))),
            n("short_visit_end", "Narrator", '''{n}You leave at dawn after one night ashore. Mielarah keeps the promise to write when she has something to say. The week continues without you; there is no shared week to mark complete.{/n}''', c("Continue the correspondence from the road.", flags=("mielarah.opening.short_visit_complete",))),
            n("shore_end", "Narrator", '''{n}The week on shore begins with dinner and ends without a cure, a contract, or a settled answer about the amulets. Mielarah has made room for you in her ordinary days, and kept the right to change her mind in them. The next voyage will test that choice in weather neither of you can command.{/n}''', c("Let the week unfold on the terms you chose together.", flags=("mielarah.opening.shore_week_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.outer_shoals_complete"),
        RequiresAny=["mielarah.opening.route_open_ending", "mielarah.opening.route_deferred_ending"],
        forbids=("mielarah.opening.closed", "mielarah.opening.friendship_only", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=168, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
    scene(
        "mielarah.opening.the_new_sail", "A course freely chosen", "Mielarah", 4,
        "Review the new sail contract with Mielarah",
        [
            n("sail_start", "Narrator", '''{n}A week later, Mielarah asks you to meet at the sailmaker's yard. The new canvas is spread across the floor in a pale sweep, its edges weighted with brass. She has the invoice in one hand and a pencil behind her ear. "I want a second reading. Don't be kind. The price is already insulting."{/n} The contract includes a rush charge for a sail that was not rushed, and a duplicate fee for the brass edging. Mielarah has marked both but has not crossed them out.''', c("Compare the invoice against the order and identify what is provable.", "invoice_check"), c("Tell her the sail is worth the asking price if it keeps Starcatcher flying.", "price_agree"), c("Ask whether she wants you to negotiate or only check the math.", "her_role")),
            n("invoice_check", "Narrator", '''The signed order lists a standard delivery and brass already included. The yard's invoice charges both twice. You show Mielarah the two lines. She stares at them, then turns the page over as if the answer might be written there. "That is not a mistake. It is a test of whether I need this sail badly enough to stop reading."''', c("Ask her to challenge the fee herself, with the signed order in hand.", "negotiation", flags=("mielarah.opening.sail_overcharge_found",)), c("Offer to make the argument while she checks the canvas.", "negotiation", flags=("mielarah.opening.sail_overcharge_found",))),
            n("price_agree", "Mielarah", '''"It may be." She folds the invoice. "But if I pay without asking, the next captain pays more. I'm not buying a sail for one voyage." She lays out the old order and the yard's measurements. "Help me see where the charge came from. If it is fair, I will pay it. If it isn't, I won't."''', c("Read the contract line by line with her.", "invoice_check"), c("Tell her you trust her judgment and let her handle it.", "her_role")),
            n("her_role", "Mielarah", '''"I want you to read it. I can speak for myself." Her tone makes the distinction sting. Then she adds, quieter, "I know you can do both. I am asking you to look, not take the argument away from me."''', c("Compare the invoice and leave the negotiation to her.", "invoice_check"), c("Decline the favor and wait for her decision.", "yard_wait")),
            n("negotiation", "Mielarah", '''She takes the signed order to the yardmaster. "This says standard delivery. Your invoice charges rush. The edging is included. Correct it." He points out that the old sail was damaged during the trial and claims the rush fee covers replacement canvas. Mielarah's jaw sets. "The trial damage is mine. The duplicate edging is yours. Separate them." She does not look at you for help; she looks at the contract.''', c("Point to the signed price and let her make the final demand.", "fee_decided", flags=("mielarah.opening.sail_terms_proved",)), c("Offer to pay the rush fee yourself.", "money_offer"), c("Threaten the yardmaster with the Commander's rank.", "rank_interferes")),
            n("money_offer", "Mielarah", '''"No." She does not take her eyes from the yardmaster. "You don't get to turn my bill into your generosity." She taps the agreed price. "Strike the duplicate fee. I'll pay for the damage I caused. We can settle the rest after I inspect the stitching." The yardmaster crosses out both charges and offers a reduced repair bill.''', c("Let her accept the written correction herself.", "fee_decided", flags=("mielarah.opening.sail_terms_proved", "mielarah.opening.sail_fee_refused")), c("Ask her whether she wants you to leave the negotiation.", "fee_decided", flags=("mielarah.opening.sail_terms_proved",))),
            n("rank_interferes", "Mielarah", '''"Stop." She looks at you now. "If he changes the invoice because you are commander, I haven't proved a thing." She sends you to check the sailcloth seams while she finishes the dispute. The yardmaster removes the duplicate fee but keeps the damage charge. Mielarah pays it from Starcatcher's account, not yours.''', c("Apologize and inspect the sail without intervening.", "fee_decided", flags=("mielarah.opening.sail_terms_proved", "mielarah.opening.rank_checked")), c("Insist your rank was the quickest tool.", "fee_decided", flags=("mielarah.opening.sail_terms_proved", "mielarah.opening.rank_checked"))),
            n("fee_decided", "Narrator", '''Mielarah signs the corrected contract. She pays for the trial damage and refuses the duplicate charge. The sailmaker complains about his margin; she replies that he has been paid for the work he actually did. On the way out she catches your sleeve. "You did not make the argument for me." Her smile comes late. "I liked that."''', c("Tell her you wanted her to win the terms she chose.", "partnership"), c("Tell her she would have won without you.", "partnership"), c("Ask if she wants to celebrate or go back to the ship.", "celebration")),
            n("yard_wait", "Narrator", '''Mielarah comes back with the corrected contract. She accepted the yard's original price after finding that the rush charge was an accounting error, not a deliberate fee. She is annoyed that the invoice was wrong and more annoyed that she wanted you to find it. "You trusted me to handle it. I did. I still wish you had looked."''', c("Tell her you can do better at reading what she asks for.", "partnership"), c("Ask whether she wants to share the relief or the irritation.", "celebration")),
            n("celebration", "Mielarah", '''"The ship needs the sail before either feeling gets a vote." She ties the contract to her belt and walks toward the berth. "Come inspect it with me. After, I want dinner. Somewhere with a better chair than last time." The invitation has the easy confidence of someone who has already decided she wants your company, but she waits for your answer.''', c("Go to the berth, then dinner.", "partnership", flags=("mielarah.opening.sail_inspected",)), c("Go only to inspect the sail and leave dinner for another time.", "partnership", flags=("mielarah.opening.sail_inspected",))),
            n("partnership", "Mielarah", '''On deck, Mielarah checks the stitching herself and asks the new sailor to do the same. She thanks the sailmaker in front of the crew, then complains privately that the man nearly charged her twice. "That is as close to forgiveness as he gets." She turns toward you. "You have seen me angry, afraid, and stubborn about an invoice. You have seen me want you. I don't want to make that into a grand confession. I want to know if you will keep choosing the ordinary parts with me."''', c("Tell her yes, and name one thing you need from her in return.", "answer_yes", flags=("mielarah.opening.ordinary_partnership_asked",)), c("Tell her you want her, but not a shared life yet.", "answer_slow", flags=("mielarah.opening.ordinary_partnership_asked",)), c("Say your paths are no longer compatible and end the romance.", "answer_end", flags=("mielarah.opening.closed",))),
            n("answer_yes", "Mielarah", '''She listens to what you need, then makes you repeat it when you try to soften the request. "Good. I can work with a real answer." She takes your hand and presses your knuckles to her lips, returning the gesture without making a joke of it. "I will try. I won't promise I will get it right every time." Her smile is small, direct. "That is the bargain I can actually offer."''', c("Accept the imperfect partnership she offers.", "partnership_end", flags=("mielarah.opening.partnership_chosen",))),
            n("answer_slow", "Mielarah", '''"Then not yet." She looks disappointed, but does not punish you for it. "I want more than a night, but I won't take a yes you haven't given." She asks you to stay for dinner anyway. The sail waits at the berth, and so does the next conversation.''', c("Keep dating and leave the future undecided.", "partnership_end", flags=("mielarah.opening.partnership_deferred",))),
            n("answer_end", "Narrator", '''{n}Mielarah's expression closes. She does not argue you into staying. The new sail is delivered, the crew takes its next voyage, and your correspondence ends with an honest goodbye.{/n}''', c("Leave the partnership question answered.", "partnership_end", flags=("mielarah.opening.partnership_ended",))),
            n("partnership_end", "Narrator", '''{n}Starcatcher takes the new sail to sea. Mielarah keeps the corrected invoice in her chart case and the amulets in their locked box. A partnership, if you chose it, will be tested in decisions neither of you can settle in one dinner. The route continues beyond this opening; this scene does not complete the full romance arc.{/n}''', c("Let the next voyage begin on the terms you both named.", flags=("mielarah.opening.new_sail_complete",))),
        ],
        requires=("mielarah.opening.contact_verified", "mielarah.opening.shore_week_complete"),
        forbids=("mielarah.opening.closed", "mielarah.opening.friendship_only", "mielarah.dead", "mielarah.expelled", "mielarah.contact_unverified"),
        delay=24, last=4, optional=True, Relationship="mielarah.opening", ManualOnly=True, Remote=True,
    ),
])


EXTERNAL_FLAGS = {
    "trickster",
    TRICKSTER_PRECRASH_HOOK,
}


def authored_scene_eligible(scene_id, flags, chapter=4, elapsed_hours=0):
    """Evaluate this author's scene contract, not the unimplemented runtime."""
    authored_scene = next(item for item in SCENES if item["Id"] == scene_id)
    return (
        authored_scene["MinChapter"] <= chapter <= authored_scene["MaxChapter"]
        and elapsed_hours >= authored_scene["DelayHours"]
        and set(authored_scene["Requires"]).issubset(flags)
        and (not authored_scene.get("RequiresAny") or set(authored_scene["RequiresAny"]).intersection(flags))
        and not set(authored_scene["Forbids"]).intersection(flags)
    )


def authored_terminal_states(authored_scene, initial_flags, start_node=None):
    """Explore choice and check branches while applying their authored flag rules."""
    nodes = {node["Id"]: node for node in authored_scene["Nodes"]}
    pending = [(start_node or authored_scene["Nodes"][0]["Id"], frozenset(initial_flags))]
    visited = set()
    terminals = []
    while pending:
        node_id, state = pending.pop()
        key = (node_id, state)
        if key in visited:
            continue
        visited.add(key)
        outgoing = []
        for choice in nodes[node_id]["Choices"]:
            if not set(choice.get("Requires", ())).issubset(state):
                continue
            if set(choice.get("Forbids", ())).intersection(state):
                continue
            next_state = frozenset(set(state).union(choice.get("Set", ())))
            check = choice.get("Check", {})
            targets = [choice.get("Next")]
            if check:
                targets.extend((check.get("Success"), check.get("Failure")))
            targets = [target for target in targets if target]
            if targets:
                outgoing.extend((target, next_state) for target in targets)
            else:
                terminals.append(next_state)
        pending.extend(outgoing)
        if not outgoing and not any(
            set(choice.get("Requires", ())).issubset(state)
            and not set(choice.get("Forbids", ())).intersection(state)
            for choice in nodes[node_id]["Choices"]
        ):
            terminals.append(state)
    return terminals


def authored_states_at(authored_scene, target_node, initial_flags):
    """Return flag states that can actually reach a node through authored choices."""
    nodes = {node["Id"]: node for node in authored_scene["Nodes"]}
    pending = [(authored_scene["Nodes"][0]["Id"], frozenset(initial_flags))]
    visited = set()
    arrivals = set()
    while pending:
        node_id, state = pending.pop()
        key = (node_id, state)
        if key in visited:
            continue
        visited.add(key)
        if node_id == target_node:
            arrivals.add(state)
        for choice in nodes[node_id]["Choices"]:
            if not set(choice.get("Requires", ())).issubset(state):
                continue
            if set(choice.get("Forbids", ())).intersection(state):
                continue
            next_state = frozenset(set(state).union(choice.get("Set", ())))
            check = choice.get("Check", {})
            targets = [choice.get("Next")]
            if check:
                targets.extend((check.get("Success"), check.get("Failure")))
            pending.extend((target, next_state) for target in targets if target)
    return arrivals


def verify_authoring_contracts():
    """Focused source checks for refusal, delayed invitation, and cross-scene state."""
    scenes = {item["Id"]: item for item in SCENES}
    produced = {flag for item in SCENES for node in item["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
    required = {flag for item in SCENES for flag in item["Requires"]}
    assert required - produced <= EXTERNAL_FLAGS, required - produced - EXTERNAL_FLAGS

    validator_text = (Path(__file__).resolve().parents[1] / "src" / "Story.cs").read_text(encoding="utf-8")
    validator_rule = "if (scene.ManualOnly && !IsRemote(scene))"
    assert validator_rule in validator_text
    assert DELIVERY_CONTRACT["ManualOnly"] and DELIVERY_CONTRACT["Remote"]
    assert all(not item.get("ManualOnly", False) or item.get("Remote", False) for item in SCENES)
    assert all(item.get("Remote", False) and item.get("ManualOnly", False) for item in SCENES)
    assert DELIVERY_CONTRACT["implemented_as_native_contact"] is False

    native_contact = {"mielarah.opening.contact_verified"}
    opening = authored_terminal_states(scenes["mielarah.opening.the_invitation"], native_contact)
    normal_waiting = next(state for state in opening if {"mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.followup_pending"} <= state)
    assert not authored_scene_eligible("mielarah.opening.followup_contact", normal_waiting, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.followup_contact", normal_waiting, elapsed_hours=24)
    refused_opening = next(state for state in opening if "mielarah.opening.closed" in state)
    assert not authored_scene_eligible("mielarah.opening.followup_contact", refused_opening | {"mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.followup_pending"}, elapsed_hours=48)

    trickster_seed = {"trickster", TRICKSTER_PRECRASH_HOOK}
    trickster_ends = authored_terminal_states(scenes["mielarah.trickster.ishiar_intervention"], trickster_seed)
    successful_landing = next(state for state in trickster_ends if "mielarah.trickster.journey_pending" in state)
    assert {"mielarah.trickster.landing_survival_verified", "mielarah.opening.met", "mielarah.opening.trust_seed"} <= successful_landing
    assert "mielarah.opening.contact_verified" not in successful_landing
    refused_or_failed = [state for state in trickster_ends if {"mielarah.trickster.no_intervention", "mielarah.trickster.failed_arcana", "mielarah.trickster.failed_perception", "mielarah.trickster.boundary_broken"}.intersection(state)]
    assert refused_or_failed and all("mielarah.opening.followup_pending" not in state for state in refused_or_failed)
    demanded = next(state for state in trickster_ends if "mielarah.trickster.trust_demanded" in state and "mielarah.opening.closed" in state)
    assert not authored_scene_eligible("mielarah.opening.followup_contact", demanded | {"mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.followup_pending"}, elapsed_hours=72)

    assert not authored_scene_eligible("mielarah.trickster.colyphyr_arrival", successful_landing | trickster_seed, elapsed_hours=71)
    assert authored_scene_eligible("mielarah.trickster.colyphyr_arrival", successful_landing | trickster_seed, elapsed_hours=72)
    journey_ends = authored_terminal_states(scenes["mielarah.trickster.colyphyr_arrival"], successful_landing | trickster_seed)
    journey_contact = next(state for state in journey_ends if {"mielarah.opening.contact_verified", "mielarah.opening.followup_pending", "mielarah.trickster.arrived_colyphyr"} <= state)
    assert not authored_scene_eligible("mielarah.opening.followup_contact", journey_contact, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.followup_contact", journey_contact, elapsed_hours=24)
    journey_refusal = next(state for state in journey_ends if "mielarah.opening.closed" in state)
    assert "mielarah.opening.contact_verified" in journey_refusal
    assert not authored_scene_eligible("mielarah.opening.followup_contact", journey_refusal | {"mielarah.opening.followup_pending"}, elapsed_hours=72)

    contact_flags = journey_contact
    assert authored_scene_eligible("mielarah.opening.followup_contact", contact_flags, elapsed_hours=24)
    followup_ends = authored_terminal_states(scenes["mielarah.opening.followup_contact"], contact_flags)
    accepted = next(state for state in followup_ends if {"mielarah.opening.followup_by_her", "mielarah.opening.case_ready"} <= state)
    assert authored_scene_eligible("mielarah.opening.the_case", accepted | {"mielarah.opening.contact_verified"})
    followup_refusal = next(state for state in followup_ends if "mielarah.opening.closed" in state)
    assert not authored_scene_eligible("mielarah.opening.the_case", followup_refusal | {"mielarah.opening.case_ready", "mielarah.opening.followup_by_her", "mielarah.opening.met", "mielarah.opening.trust_seed", "mielarah.opening.contact_verified"})

    contradictory = accepted | {"mielarah.opening.contact_verified", "mielarah.dead"}
    assert not authored_scene_eligible("mielarah.opening.the_case", contradictory)
    assert not authored_scene_eligible("mielarah.opening.the_case", contradictory - {"mielarah.dead"} | {"mielarah.expelled"})
    assert not authored_scene_eligible("mielarah.opening.the_case", contradictory - {"mielarah.dead"} | {"mielarah.contact_unverified"})
    for scene_id in ("mielarah.opening.followup_contact", "mielarah.opening.the_captains_evening", "mielarah.opening.the_crews_answer", "mielarah.opening.the_quay_day"):
        scene = scenes[scene_id]
        eligible_flags = set(scene["Requires"])
        assert not authored_scene_eligible(scene_id, eligible_flags | {"mielarah.contact_unverified"}, elapsed_hours=scene["DelayHours"])

    case_ends = authored_terminal_states(scenes["mielarah.opening.the_case"], accepted | {"mielarah.opening.contact_verified"})
    evening_flags = next(state for state in case_ends if {"mielarah.opening.evening_invited", "mielarah.opening.evening_pending"} <= state)
    evening_ends = authored_terminal_states(scenes["mielarah.opening.the_captains_evening"], evening_flags | {"mielarah.opening.contact_verified"})
    crew_flags = next(state for state in evening_ends if "mielarah.opening.crew_meeting_pending" in state)
    crew_access = crew_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"}
    assert not authored_scene_eligible("mielarah.opening.the_crews_answer", crew_access, elapsed_hours=47)
    assert authored_scene_eligible("mielarah.opening.the_crews_answer", crew_access, elapsed_hours=48)
    assert not authored_scene_eligible("mielarah.opening.the_crews_answer", crew_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her", "mielarah.opening.closed"}, elapsed_hours=72)
    crew_ends = authored_terminal_states(scenes["mielarah.opening.the_crews_answer"], crew_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"})
    quay_day_flags = next(state for state in crew_ends if "mielarah.opening.crew_day_pending" in state)
    assert not authored_scene_eligible("mielarah.opening.the_quay_day", quay_day_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"}, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.the_quay_day", quay_day_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"}, elapsed_hours=24)
    assert any("mielarah.opening.quay_day_complete" in state for state in authored_terminal_states(scenes["mielarah.opening.the_quay_day"], quay_day_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"}))

    quay_ends = authored_terminal_states(scenes["mielarah.opening.the_quay_day"], quay_day_flags | {"mielarah.opening.contact_verified", "mielarah.opening.followup_by_her"})
    next_day = next(state for state in quay_ends if {"mielarah.opening.quay_day_complete", "mielarah.opening.following_day_pending"} <= state)
    assert not authored_scene_eligible("mielarah.opening.the_repair_ledger", next_day | {"mielarah.opening.contact_verified"}, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.the_repair_ledger", next_day | {"mielarah.opening.contact_verified"}, elapsed_hours=24)
    ledger_ends = authored_terminal_states(scenes["mielarah.opening.the_repair_ledger"], next_day | {"mielarah.opening.contact_verified"})
    trial_access = next(state for state in ledger_ends if {"mielarah.opening.sail_trial_pending", "mielarah.opening.following_day_complete"} <= state)
    assert not authored_scene_eligible("mielarah.opening.the_sail_trial", trial_access | {"mielarah.opening.contact_verified"}, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.the_sail_trial", trial_access | {"mielarah.opening.contact_verified"}, elapsed_hours=24)
    trial_ends = authored_terminal_states(scenes["mielarah.opening.the_sail_trial"], trial_access | {"mielarah.opening.contact_verified"})
    watch_access = next(state for state in trial_ends if {"mielarah.opening.weather_watch_pending", "mielarah.opening.trial_complete"} <= state)
    assert not authored_scene_eligible("mielarah.opening.the_weather_watch", watch_access | {"mielarah.opening.contact_verified"}, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.the_weather_watch", watch_access | {"mielarah.opening.contact_verified"}, elapsed_hours=24)
    watch_ends = authored_terminal_states(scenes["mielarah.opening.the_weather_watch"], watch_access | {"mielarah.opening.contact_verified"})
    assert any("mielarah.opening.intimate_night" in state for state in watch_ends)
    assert any("mielarah.opening.closed" in state for state in watch_ends)
    assert any("mielarah.opening.cabin_declined" in state for state in watch_ends)
    watch_complete = next(state for state in watch_ends if "mielarah.opening.watch_complete" in state and "mielarah.opening.closed" not in state)
    assert not authored_scene_eligible("mielarah.opening.the_departure_notice", watch_complete | {"mielarah.opening.contact_verified"}, elapsed_hours=47)
    assert authored_scene_eligible("mielarah.opening.the_departure_notice", watch_complete | {"mielarah.opening.contact_verified"}, elapsed_hours=48)
    departure_ends = authored_terminal_states(scenes["mielarah.opening.the_departure_notice"], watch_complete | {"mielarah.opening.contact_verified"})
    departure_scene = scenes["mielarah.opening.the_departure_notice"]
    jori_flag = "mielarah.opening.jori_answered"
    assert authored_states_at(departure_scene, "carry_answer", watch_complete) and all(jori_flag in state for state in authored_states_at(departure_scene, "carry_answer", watch_complete))
    assert authored_states_at(departure_scene, "crew_meeting", watch_complete) and all(jori_flag in state for state in authored_states_at(departure_scene, "crew_meeting", watch_complete))
    no_private_exchange = authored_states_at(departure_scene, "crew_meeting_unbriefed", watch_complete)
    assert no_private_exchange and all(jori_flag not in state for state in no_private_exchange)
    voyage = next(state for state in departure_ends if {"mielarah.opening.voyage_accepted", "mielarah.opening.crew_arc_complete"} <= state and "mielarah.opening.friendship_only" not in state)
    friend_voyage = next(state for state in departure_ends if {"mielarah.opening.voyage_accepted", "mielarah.opening.crew_arc_complete", "mielarah.opening.friendship_only"} <= state)
    friend_access = friend_voyage | {"mielarah.opening.contact_verified"}
    assert not authored_scene_eligible("mielarah.opening.the_outer_shoals", friend_access, elapsed_hours=72)
    assert authored_scene_eligible("mielarah.opening.the_outer_shoals_friendship", friend_access, elapsed_hours=72)
    friend_ends = authored_terminal_states(scenes["mielarah.opening.the_outer_shoals_friendship"], friend_access)
    assert any("mielarah.opening.friendship_correspondence_complete" in state for state in friend_ends)
    assert all(not {"mielarah.opening.future_chosen", "mielarah.opening.future_deferred", "mielarah.opening.route_open_ending", "mielarah.opening.route_deferred_ending"}.intersection(state) for state in friend_ends)
    friendship_with_romance_flags = friend_access | {"mielarah.opening.outer_shoals_complete", "mielarah.opening.route_open_ending", "mielarah.opening.shore_week_complete"}
    assert not authored_scene_eligible("mielarah.opening.the_week_on_shore", friendship_with_romance_flags, elapsed_hours=1000)
    assert not authored_scene_eligible("mielarah.opening.the_new_sail", friendship_with_romance_flags, elapsed_hours=1000)
    assert not authored_scene_eligible("mielarah.opening.the_outer_shoals", voyage | {"mielarah.opening.contact_verified"}, elapsed_hours=71)
    assert authored_scene_eligible("mielarah.opening.the_outer_shoals", voyage | {"mielarah.opening.contact_verified"}, elapsed_hours=72)
    ending_states = authored_terminal_states(scenes["mielarah.opening.the_outer_shoals"], voyage | {"mielarah.opening.contact_verified"})
    assert any("mielarah.opening.route_open_ending" in state for state in ending_states)
    assert any("mielarah.opening.route_deferred_ending" in state for state in ending_states)
    assert any("mielarah.opening.route_closed_ending" in state for state in ending_states)
    shore_scene = scenes["mielarah.opening.the_week_on_shore"]
    for ending_flag in ("mielarah.opening.route_open_ending", "mielarah.opening.route_deferred_ending"):
        accepted_ending = next(state for state in ending_states if ending_flag in state)
        shore_access = accepted_ending | {"mielarah.opening.contact_verified", "mielarah.opening.outer_shoals_complete"}
        assert not authored_scene_eligible(shore_scene["Id"], shore_access, elapsed_hours=167)
        assert authored_scene_eligible(shore_scene["Id"], shore_access, elapsed_hours=168)
        shore_ends = authored_terminal_states(shore_scene, shore_access)
        assert any("mielarah.opening.shore_week_complete" in state for state in shore_ends)
    deferred_visit_start = next(state for state in authored_states_at(shore_scene, "departure_letter", {"mielarah.opening.contact_verified", "mielarah.opening.outer_shoals_complete", "mielarah.opening.route_deferred_ending"}))
    short_visit = authored_terminal_states(shore_scene, deferred_visit_start, start_node="departure_letter")
    assert any("mielarah.opening.short_visit_complete" in state for state in short_visit)
    assert all("mielarah.opening.shore_week_complete" not in state for state in short_visit)
    assert all("mielarah.opening.shore_week_complete" not in state for state in short_visit if "mielarah.opening.short_visit_complete" in state)
    assert not authored_scene_eligible("mielarah.opening.the_new_sail", short_visit[0] | {"mielarah.opening.contact_verified", "mielarah.opening.outer_shoals_complete"}, elapsed_hours=1000)
    completed_week = next(state for state in shore_ends if "mielarah.opening.shore_week_complete" in state and "mielarah.opening.closed" not in state)
    assert not authored_scene_eligible("mielarah.opening.the_new_sail", completed_week | {"mielarah.opening.contact_verified"}, elapsed_hours=23)
    assert authored_scene_eligible("mielarah.opening.the_new_sail", completed_week | {"mielarah.opening.contact_verified"}, elapsed_hours=24)
    sail_ends = authored_terminal_states(scenes["mielarah.opening.the_new_sail"], completed_week | {"mielarah.opening.contact_verified"})
    assert any("mielarah.opening.partnership_chosen" in state for state in sail_ends)
    assert any("mielarah.opening.partnership_deferred" in state for state in sail_ends)
    assert any("mielarah.opening.partnership_ended" in state for state in sail_ends)
    closed_ending = next(state for state in ending_states if "mielarah.opening.route_closed_ending" in state)
    assert not authored_scene_eligible(shore_scene["Id"], closed_ending | {"mielarah.opening.contact_verified", "mielarah.opening.outer_shoals_complete"}, elapsed_hours=240)
    overstep = next(state for state in trial_ends if "mielarah.opening.trial_overstepped" in state)
    assert "mielarah.opening.closed" in overstep
    assert not authored_scene_eligible("mielarah.opening.the_sail_trial", trial_access | {"mielarah.opening.contact_verified", "mielarah.dead"}, elapsed_hours=72)

    assert all(not authored_scene.get("ManualOnly", False) or authored_scene.get("Remote", False) for authored_scene in SCENES)


if __name__ == "__main__":
    expected_paths = {"angel", "aeon", "azata", "demon", "devil", "gold_dragon", "legend", "lich", "swarm", "trickster"}
    assert set(PATH_ACCESS) == expected_paths
    assert all(set(item) >= {"condition", "choice_and_consequence", "failure", "native_anchor", "implemented"} for item in PATH_ACCESS.values())
    assert all(item["implemented"] is False for item in PATH_ACCESS.values())
    assert {"intro", "colyphyr_service", "ishiar_crash", "trickster_alternate_timeline", "vazglar_raid", "coercive_magic", "aeon_expulsion"} == set(FATE_AUDIT)
    assert INTEGRATION_PREMISE["implemented"] is False
    assert INTEGRATION_PREMISE["verified_parent_choice_chain"] is False
    assert FOLLOWUP_CONTACT_CONTRACT["mielarah.opening.followup_by_her"]["implemented"] is False
    assert TRICKSTER_PRECRASH_HOOK == "mielarah.native_answer_0351_before_cue0426"
    assert PRODUCER_CONTRACT["mielarah.opening.contact_verified"]["implemented"] is False
    ids = [node["Id"] for authored_scene in SCENES for node in authored_scene["Nodes"]]
    assert len(ids) == len(set(ids))
    id_set = set(ids)
    for authored_scene in SCENES:
        for node in authored_scene["Nodes"]:
            for choice in node["Choices"]:
                check = choice.get("Check", {})
                targets = (choice.get("Next"), check.get("Success"), check.get("Failure"))
                assert all(target is None or target in id_set for target in targets), (node["Id"], targets)
    for authored_scene in SCENES:
        nodes = {node["Id"]: node for node in authored_scene["Nodes"]}
        reachable = set()
        pending = [authored_scene["Nodes"][0]["Id"]]
        while pending:
            current = pending.pop()
            if current in reachable:
                continue
            reachable.add(current)
            for choice in nodes[current]["Choices"]:
                check = choice.get("Check", {})
                pending.extend(target for target in (choice.get("Next"), check.get("Success"), check.get("Failure")) if target)
        assert reachable == set(nodes), (authored_scene["Id"], set(nodes) - reachable)
    verify_authoring_contracts()
    flags = {flag for authored_scene in SCENES for node in authored_scene["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
    assert "mielarah.opening.trust_seed" in flags
    assert RELATIONSHIP["CommittedFlag"] not in flags
    print(f"{len(SCENES)} unregistered scene(s); {len(ids)} nodes; topology and cross-scene state contracts valid; no courtship commit awarded")
