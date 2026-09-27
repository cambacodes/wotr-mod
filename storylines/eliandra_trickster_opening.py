"""Unregistered Trickster opening for an authored Eliandra romance route.

The opening grows from Pulura's Fall's native dispute about love, duty, and
community safety. Every route, contact, and response flag here is a proposal;
none is registered or produced by the game integration.
"""

from story_format import c, n, scene


RELATIONSHIP = dict(
    Title="A star allowed to wander",
    Description="Eliandra decides whether duty leaves room for one private question.",
    Objective="Help without turning gratitude or Pulura's will into a claim",
    Guidance=(
        "Unregistered Trickster opening experiment. It requires verified Pulura's Fall "
        "contact, the community's romance-rule decision, Eliandra's survival and presence, "
        "and her explicit agreement to this private conversation. None of those producers "
        "exists. A conversation is not consent to romance. Other-path access and the full "
        "route remain unimplemented."
    ),
    StartedFlag="eliandra.trickster.opening_started",
    ClosedFlag="eliandra.trickster.opening_closed",
    CommittedFlag="eliandra.trickster.romance_committed",
    UnavailableFlags=["eliandra.trickster.native_conflict", "eliandra.trickster.contact_refused"],
    FailureFlags=[],
)


NATIVE = {
    "first_contact": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/ElyandraRanger_Intro/Cue_0001.jbp",
        "id": "0bd02c57a78fd7f4e8b5b379d29280ec",
        "fact": "Eliandra introduces herself as Pulura's high priestess and says the Commander is the first new face she has seen during the vigil.",
    },
    "katair_intro": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/ElyandraRanger_Intro/Cue_0002.jbp",
        "id": "3fcae78bc3948ab4c8c8de778013099c",
        "fact": "Katair calls himself leader of Pulura's holy guards and challenges the Hand's decision to reveal the temple.",
    },
    "relationship_rule": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/Elyandra_main/Cue_0002.jbp",
        "id": "c9f74d937a185d543a06273cdd21ca30",
        "fact": "Eliandra explains that isolation makes love, jealousy, discord, quarrels, and breakups a genuine danger to the community.",
    },
    "community_outcome": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/Elyandra_main/Cue_0010.jbp and Cue_0011.jbp",
        "id": "dde53ed7a465f5a4c8062f7e82cb1ead; 6692c6d1de7b1404cbd87079739a3a4e",
        "fact": "She may accept that the community should not thwart the heart's desires, or refuse because of old wounds and future chaos.",
    },
    "personal_history": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/HeraldPulura/Cue_0009.jbp",
        "id": "24d719b48b3195949b3d96a5afb5721b",
        "fact": "The Herald says Eliandra discovered her gift at thirteen, served as healer and guide ever since, and never married or had a family.",
    },
    "century_vigil": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/ElyandraRanger_Intro/Cue_0003.jbp",
        "id": "c0dd70f8eb05b8a4fb13342b5507958a",
        "fact": "The Hand says Eliandra, Katair, and their comrades have spent a hundred years in voluntary isolation.",
    },
    "chapter_3_actor": {
        "path": "World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/Chapter03_AreasDefault/PuluraFall/Pulura_NPC_DefaultActors/Pulura_NPC_Eliandra_DefaultActor.jbp",
        "id": "a048f51d45b5268488cb32c383465115",
        "fact": "The extracted Chapter 3 area etude includes a default actor record for Eliandra at Pulura's Fall.",
    },
    "abduction": {
        "path": "World/Dialogs/c3/Pulura_C3/Pulura_C3_main/HeraldChapel/Cue_0020.jbp",
        "id": "45876b95070de8a43b4e2eb88bf7381d",
        "fact": "The Hand reacts to the Echo of Deskari taking Eliandra and calls her the heart of Pulura's Fall.",
    },
    "rescue": {
        "path": "World/Dialogs/c4/Mythic_Angel/EliandraSaved/Cue_0001.jbp",
        "id": "75eca543e0150f74b927fbd6694a90cb",
        "fact": "In an Angel-specific rescue scene, Eliandra is pale but composed and thanks the Commander for saving her.",
    },
    "chapter_5_rescue": {
        "path": "World/Dialogs/c5/PuluraFallsC5/PuluraLeaderSaved/Answer_0028.jbp and Cue_0001.jbp",
        "id": "fd419afa29e9cf146807aa3d91c3332e; 860edc351f25b624296a572aa1f6c48f",
        "fact": "A Chapter 5 Pulura shrine scene says Eliandra is alive and rescued from the Echo, then presents her thanking the Commander for saving her shrine.",
    },
    "chapter_5_research": {
        "path": "World/Dialogs/c5/PuluraFallsC5/PuluraLeaderSaved/Cue_0025.jbp and Cue_0031.jbp",
        "id": "53d10d142f76b964cb7e14ee305a642b; c12de8773867e9d49a4fdfedd804b8a7",
        "fact": "Eliandra says the community's Worldwound research has been studied for a hundred years and explains the Echo's attempt to use it.",
    },
    "sacrifice": {
        "path": "World/Dialogs/c3/Mythic_Angel/Targona/Cue_0014.jbp",
        "id": "a528614125b07714db52d9004f36d448",
        "fact": "The Inheritor recognizes Eliandra and Katair's self-sacrifice as part of what protected Pulura's Fall.",
    },
}


# These are names for future source-bound producers, not existing game flags.
CONTRACT = {
    "status": "unregistered opening design; all custom flags and actor bindings are proposals",
    "availability": (
        "A native-history reader must verify that the Commander completed Pulura's Fall's "
        "relationship dispute, read Eliandra's resulting community decision, and confirmed "
        "she survived and is physically contactable in Chapter 3. The authoring proposal "
        "adds a separate, optional audience only after she explicitly invites the Commander. "
        "Chapter 3 has an extracted Pulura NPC default-actor etude for Eliandra. The "
        "later Echo abduction is also explicit. Chapter 4's EliandraSaved dialogue is "
        "Angel-specific, so it cannot supply universal post-capture contact. Chapter 5 "
        "has a separate PuluraLeaderSaved dialogue that reports her alive and rescued "
        "from the Echo and presents her at the shrine. That is a sound future contact "
        "point if its own actor and rescue-history requirements are verified. This "
        "opening is intentionally set in Chapter 3, before the abduction, and does not "
        "claim that an unregistered mod actor or future Chapter 5 continuation exists."
    ),
    "trickster_hook": (
        "The Commander has already witnessed the temple's argument about whether love "
        "endangers an isolated community. The proposed Trickster play is an honest "
        "procedural ruse: request a public, time-bounded test of the policy's actual "
        "consequences, then offer Eliandra a private conversation only after she sees "
        "evidence and separately chooses it. The wit is in proposing a reversible "
        "experiment and respecting its limits, not in magic that changes her feelings. "
        "The Trickster's specific edge is turning a supposed binary fate into a test "
        "that can expose both the harm of restriction and the cost of change. It remains "
        "possible for the experiment to preserve the rule or for Eliandra to refuse contact."
    ),
    "community_decision": {
        "permitted": "Native result equivalent to Eliandra agreeing that the community should not thwart the desires of the heart.",
        "refused": "Native result equivalent to Eliandra refusing reform because reopening old wounds and future chaos seem too costly.",
        "policy": "The Trickster opening can occur after either result. Reform is not consent to the Commander, and refusal is not a flirtation test. A refusal result changes the conversation's focus to the cost she carries; it cannot be bypassed with a skill check.",
        "future_verified_flags": {
            "eliandra.native.rule_reformed_verified": "A source-bound reader recognizes the affirmative native branch represented by Cue_0010 GUID dde53ed7a465f5a4c8062f7e82cb1ead.",
            "eliandra.native.rule_retained_verified": "A source-bound reader recognizes the refusal branch represented by Cue_0011 GUID 6692c6d1de7b1404cbd87079739a3a4e.",
            "mutual_exclusion": "The runtime reader must prove exactly one branch from dialogue history. Missing both or observing contradictory history blocks this scene; no synthetic default is allowed.",
        },
    },
    "romance_rule": "No choice in this opening commits Eliandra to romance. Only her authored, explicit welcome to another personal conversation sets private_conversation_welcomed. A refusal, withdrawal, hostile answer, or missing contact closes the opening without setting romantic interest.",
    "katair_and_duty": (
        "Katair remains her fellow leader and trusted protector, never a presumed spouse, "
        "obstacle, accomplice, or object of ridicule. Native text calls him devoted and "
        "describes their shared century, but does not establish a romantic relationship. "
        "The opening neither recruits him into a triangle nor demands Eliandra abandon "
        "Pulura's Fall. Later writing must show an explicit, credible division of duty "
        "before any travel or sustained courtship away from the community."
    ),
    "path_access": {
        "Trickster": "This opening proposes a quest-linked Trickster access route; no native contact invitation or integration exists yet.",
        "other_nine": "No route is implemented. Each path needs its own character-consistent introduction without reusing the Trickster's procedural ruse as a universal answer.",
    },
    "presence_boundary": (
        "The base game's Chapter 3 Pulura's Fall quest and later Echo captivity establish "
        "historical contact, not continuous physical availability. The Angel-specific "
        "Chapter 4 rescue cannot be treated as a universal return. Before registering "
        "this scene, implement a real Chapter 3 contact producer or an explicit "
        "path-independent actor delivery event. Until then this file is a manuscript, "
        "not a runnable campaign route."
    ),
}


def page(id, speaker, text, *choices):
    return n(id, speaker, text, *choices, portrait="Eliandra")


SCENE = scene(
    "eliandra.trickster.first_private_audience",
    "A star allowed to wander",
    "Eliandra",
    3,
    "invitation",
    [
        page("invitation", "Narrator", '''{n}The temple's public hall has thinned to the sound of the evening bell and the scratch of a quill. Eliandra waits beside the western arch, where the windows give the last light to Pulura's painted stars. She has dismissed the guards from earshot, though not from the hall. Katair is visible at the far door, speaking to a sentry with the same grave concentration he brings to everything that might keep his people alive.{/n}

{n}Eliandra wears no ceremonial veil. The light catches the silver at her temples and the fine lines at the corners of her eyes. They look like the marks of long attention, not age guessed from a face: she has spent more years than most people live listening to grief and asking what it needs.{/n}

"Commander. I asked you to stay because I owe you an answer about the temple's rule. I also wanted to speak without making the whole community listen. You may refuse either conversation. You have already done enough for us that I should not mistake your help for a promise."''',
            c("Tell her you came to hear her answer, not collect a debt.", "debt"),
            c("Ask whether this private audience is her choice or another duty she thinks she owes.", "choice"),
            c("Ask what she decided about the community's rule.", "reformed", requires=("eliandra.native.rule_reformed_verified",), forbids=("eliandra.native.rule_retained_verified",)),
            c("Ask what she still fears if the community loosens the rule.", "retained", requires=("eliandra.native.rule_retained_verified",), forbids=("eliandra.native.rule_reformed_verified",)),
            c("Say the temple's needs come first and offer to leave.", "withdraw", flags=("eliandra.trickster.opening_closed",))),
        page("reformed", "Eliandra", '''"I agreed that we should not thwart the desires of the heart. I did not decide that every relationship will be easy, or that I can tell the people here how to love. A rule can change overnight. Trust changes more slowly." {n}She studies your face to see whether you heard the distinction.{/n}

"Do not mistake this decision for an invitation to me. I made it because the community deserved a voice in its own life. I am still learning what freedom asks of a leader once the permission has been given."''',
            c("Ask what remains difficult about leading after the rule changed.", "experiment"),
            c("Tell her you are glad she chose for herself too.", "interest"),
            c("Call the decision proof she is ready to choose you.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("retained", "Eliandra", '''"I kept the rule. I could not look at the people who have already lost so much and tell them I knew how to prevent another wound. That answer gave me order. It did not give me peace." {n}She does not ask you to absolve her, and she does not frame the choice as a secret wish for someone to overrule it.{/n}

"If we discuss it again, I need you to understand that my caution is not a coy invitation. It may be the best judgment I can make with what I know. It may also have cost people more than I was willing to see. I am still accountable either way."''',
            c("Ask what evidence could help her understand the rule's cost without shaming anyone.", "experiment"),
            c("Respect her answer and ask whether she wants to speak about something else.", "service"),
            c("Promise the Trickster can make her change her mind.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("debt", "Commander", '''"You owe me no answer because I helped. If you want to discuss the rule, I'll listen. If you want to end the discussion, I will still help your people with whatever we agreed."''',
            c("Ask what changed her mind enough to invite a private conversation.", "experiment"),
            c("Ask about the work she has kept doing since she was thirteen.", "service"),
            c("Let her choose the subject.", "her_subject")),
        page("choice", "Eliandra", '''"It is my choice. I have made enough decisions in other people's names to know the difference. But I am choosing a conversation, not a new rule and not an answer about you." {n}Her gaze stays kind, but it is steady. There is no apology in it.{/n}

"The distinction matters. I would not ask you to pretend it doesn't."''',
            c("Agree that she can decide one question at a time.", "experiment"),
            c("Say that you are interested in the woman who made the choice, if she wants to be seen that way.", "interest"),
            c("Apologize for pressing and offer to go.", "withdraw", flags=("eliandra.trickster.opening_closed",))),
        page("experiment", "Commander", '''"I have a proposal, and it is less elegant than the one I would make if I were trying to win an argument. Do not change the rule tonight. Give the temple a trial instead: one week in which the people affected by it can speak openly, with a witness from each side and a clear right to stop. Then ask what the rule protected, what it cost, and whether anyone was safer because of it."''',
            c("Add that the trial must not pressure anyone to confess a love or name a partner.", "safeguards"),
            c("[Knowledge: World] Draft a neutral record that weighs safety, silence, and the costs of both rules. DC 25.", "protocol_success", check=dict(Skill="SkillKnowledgeWorld", DC=25, CommanderOnly=True, Success="protocol_success", Failure="protocol_failure")),
            c("Ask whether she wants the community to choose the witness or wants you to find one.", "witness"),
            c("Claim the trial proves she should abandon the rule now.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("protocol_success", "Commander", '''{n}The problem is not that the temple has no rules. It is that its current rule treats every private attachment as the same danger, while the people who carry the consequences have no safe way to describe which danger they actually face.{/n}

"I would record what the rule is meant to prevent, then ask each person whether it has prevented that harm in their life. We should record what people feared would happen if the rule changed, too. No names, no forced testimony, and no vote that can turn one person's confession into the price of everyone else's freedom."''',
            c("Offer the outline to Eliandra for correction before anyone else sees it.", "protocol_review"),
            c("Ask her to write her own questions and let the community reject yours.", "protocol_review"),
            c("Use your draft as proof that she should agree with you.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("protocol_failure", "Eliandra", '''{n}You begin the outline and find that every version assumes a conclusion. One protects the rule by treating all desire as a threat; another abolishes it by treating every consequence as a prejudice. Neither can listen to people who are frightened for reasons you do not yet understand.{/n}

"You did not solve this by thinking harder. That is useful information, Commander. Can you leave the question open long enough for the people here to answer it?"''',
            c("Admit the draft is incomplete and ask Eliandra to set the boundaries.", "safeguards"),
            c("Invite the community to design the trial without you directing it.", "witness"),
            c("Pretend the failed outline says exactly what you wanted.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("protocol_review", "Eliandra", '''"You found a way to make the exercise answerable. You did not find a way to make the answer yours." {n}She takes the page and reads each line twice. Her brow tightens at the mention of harm; it eases when she reaches the part that protects silence.{/n}

"I will change the wording. The first question should ask what people need to feel safe speaking, and the second should ask whether silence itself has become a cost. A person may answer neither. The choice to remain private must not become a confession by another name."''',
            c("Accept the edits and let her convene the meeting in her own voice.", "decision_open"),
            c("Ask if the question about silence is one she is asking herself, too.", "responsibility"),
            c("Tell her the revision was unnecessary because your wording was already fair.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("safeguards", "Eliandra", '''"You would permit people to remain silent? To say nothing about whom they love, and still have the rule reconsidered?" {n}The question comes quickly. Her fingers close around the quill until the feather bends, then loosen.{/n}

"That is not how most people ask for change. Usually they arrive with one couple in mind and call every cost an obstacle. You are proposing a test that may tell us to keep the rule. Is that really what you mean?" {n}She sets the quill down with care. Her hands are fine-boned, strong from years of work, and marked by tiny pale lines where old cuts healed. You notice them because she has stopped moving them. The silence gives you the chance to answer without being hurried.{/n}''',
            c("Yes. A trial that cannot return an inconvenient answer is only a speech with witnesses.", "evidence"),
            c("No. Admit you wanted to get your way and apologize for dressing it as fairness.", "repair"),
            c("Tell her she already knows the rule is wrong.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("witness", "Eliandra", '''"The people who live under the rule must choose their own witnesses. Katair should hear the proposal as a leader, but he should not be made its judge. Nor should you. If you become the face of the argument, half the temple will speak to please you and the other half will refuse simply to prove they can."''',
            c("Accept her terms and ask whether she will convene the meeting.", "evidence"),
            c("Offer to persuade Katair first, then let her decide.", "katair"),
            c("Say the trick is to keep both leaders busy while you change the rule.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("katair", "Eliandra", '''"You are welcome to tell Katair your proposal. I will not have him maneuvered into agreement, though. He is responsible for the guards and for the safety of this place. He has earned the right to say no without becoming a villain in your story." {n}She pauses, weighing how much of her frustration belongs in the room.{/n}

"We have disagreed before. We will disagree again. I do not need you to turn that into a weakness you can exploit."''',
            c("Agree to speak with him openly and accept whatever answer he gives.", "evidence"),
            c("Say you were looking for a crack between them and withdraw.", "withdraw", flags=("eliandra.trickster.opening_closed",)),
            c("Ask whether disagreement has left either of them alone with the cost.", "loneliness")),
        page("service", "Eliandra", '''"I discovered my gift when I was thirteen. I was young enough to think that being able to ease pain meant I ought to be able to ease all of it. Then a person I had helped would leave, and another would arrive, and the work would not be finished. I learned to guide before I learned how to rest."''',
            c("Ask what she learned about rest without asking her to justify the years she gave away.", "rest"),
            c("Tell her you admire how she has served everyone, then ask what she wants for herself.", "interest"),
            c("Say she should have chosen a life instead of a calling.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("her_subject", "Eliandra", '''"Then let us begin with the question I avoided in public. I have told this community that love can become a danger when a small, isolated people cannot escape its quarrels. I still believe that danger is real. But I have also seen the harm of treating every tenderness as the first step toward a disaster."''',
            c("Ask what evidence she would trust enough to change her mind.", "evidence"),
            c("Ask whether the fear is about the lovers, or about being responsible when the lovers hurt one another.", "responsibility"),
            c("Tell her that love is always worth any cost.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("evidence", "Eliandra", '''"The trial would need rules of its own. No one is compelled to speak. No one is punished for remaining together or for ending a relationship. If there is a quarrel, the people involved must not be made into a lesson for the rest of us. And if a person asks to stop, the gathering stops." {n}She looks past you toward the hall. The temple is small enough that a private grief can become communal property before the grieving person knows it has happened.{/n}

"Would you accept those limits if they meant the trial gave you nothing you wanted?"''',
            c("Accept the limits and ask her to invite the community herself.", "decision_open"),
            c("Ask to serve as an outside witness, with no authority over the outcome.", "decision_open"),
            c("Argue that discomfort is the price of progress.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("decision_open", "Eliandra", '''"Then I will speak to them. Not because you have found a clever way to make me yield, but because the rule should answer to the lives it governs. I may decide it remains necessary. I may decide that we can trust people with more freedom than I have given them. Either answer will belong to the community, and I will carry the part that is mine."''',
            c("Ask if she would like you to stay for the meeting or leave her to lead it.", "meeting"),
            c("Tell her you respect the decision and turn toward the door.", "close_respect", flags=("eliandra.trickster.opening_closed",)),
            c("Call her decision a victory for you.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("responsibility", "Eliandra", '''{n}Eliandra's expression changes. Her eyes lower, not in shame but in recognition of a question that has been waiting longer than this conversation.{/n}

"Both. I have watched people hurt one another and call the pain proof that they were wrong to love. I have also watched leaders use that pain to tighten every rule around the people who survived it. The temple cannot pretend its smallness makes it harmless. I have made decisions for others because I was afraid of what would happen if I did not."''',
            c("Tell her fear can be honest and still need to answer for what it takes away.", "honest_cost"),
            c("Ask whether she trusts herself to lead without deciding for everyone.", "trust"),
            c("Say a good priestess would never be afraid of desire.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("honest_cost", "Eliandra", '''"You make a dangerous distinction sound simple." {n}A small smile appears, then remains guarded. She has not mistaken a pleasing sentence for an answer.{/n}

"It is easier to keep order when I ask no one to risk anything. It is also easier to call that order compassion. I cannot promise I have not done so. If you want me to become a symbol of freedom, I will disappoint you. I have hurt people while trying to keep them safe, and I will not be absolved by changing one rule."''',
            c("Say you are not asking for a symbol, only a person able to disagree with you.", "interest"),
            c("Say that she should make the decision without using your approval as a measure.", "decision_open"),
            c("Tell her you can absolve her if she gives you a chance.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("trust", "Commander", '''"You have carried the temple for a century. You can trust yourself to lead and still let people disagree with you. Those things are not opposites."''',
            c("Add that a decision is not safe just because it is yours.", "evidence"),
            c("Ask what support she needs before convening the community.", "support"),
            c("Tell her you can take the burden from her if she trusts you.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("support", "Eliandra", '''"I need no one to take the burden from me. I need the people whose lives are affected to share the speaking, the listening, and the repair if we are wrong. Katair can guard the meeting without policing what anyone says. I can lead it without pretending I know the answer in advance. You can remain a guest instead of its clever author."''',
            c("Accept the guest's place, even if no one praises the idea.", "decision_open"),
            c("Ask whether she wants you to stay after the meeting for another conversation.", "interest"),
            c("Say the plan only works if you are allowed to direct it.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("rest", "Eliandra", '''"I still do not know. My days have been arranged around people who needed me, and that is not a complaint. I chose the work. But choice does not make a life limitless. There are evenings I have watched the stars from this window and wondered what I might have wanted if I had believed the calling would not vanish when I stepped away." {n}She looks toward the open window. The evening wind moves a strand of hair against her cheek. Her hand rises as if to tuck it back, but she leaves it there for a moment, feeling the air against her skin.{/n}

"Perhaps I would have wanted the ordinary things people speak of as though they were small: a room that belongs to me, a meal that is not interrupted, a hand I can take because I want to, not because someone needs help standing. I cannot tell you whether those things would have lasted. I only know I have spent a long time treating the question as selfish."''',
            c("Ask what she would choose for this evening, without asking for a lifetime answer.", "chosen_evening"),
            c("Tell her she may leave the question unanswered.", "close_respect", flags=("eliandra.trickster.opening_closed",)),
            c("Tell her the Trickster can return every lost evening to her.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("chosen_evening", "Eliandra", '''"Tonight? I would finish the work I promised to finish. Then I would sit at this window with someone who did not need me to make a decision for them. I would ask what they wanted before I asked what they thought I ought to want. I might even let them ask me something that has no useful answer." {n}She holds your gaze. The idea is plainly unfamiliar, but not unpleasant.{/n}

"I would like to learn what it is to be wanted without being treated as a solution. And I would like to find out whether I can want someone without immediately counting all the ways that might complicate my life. I am not offering you the answer. I am admitting that the question has begun to interest me."''',
            c("Ask what she wants to know about you, and answer without turning it into a performance.", "interest"),
            c("Offer to share the evening only if she still wants it after her work is done.", "evening_offer"),
            c("Tell her you can prove that wanting you will be worth the trouble.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("evening_offer", "Eliandra", '''"An hour. Here, after my duties are done, if the temple remains quiet and I still want company. Tea, the stars, and no questions about what either of us owes the other. If I am tired, I will say so. If you have somewhere else to be, you may say so. Neither of us should pretend an evening is a vow." {n}She glances toward the night sky, then back at you. The measured terms do not cool the invitation. They make it hers.{/n}

"And if we discover that the silence between questions feels better than the questions, I will decide what to do with that. You do not need to decide it for me."''',
            c("Accept the hour as offered and let her set the boundary if she changes her mind.", "interest"),
            c("Decline so she does not have to divide her attention tonight.", "close_respect", flags=("eliandra.trickster.opening_closed",)),
            c("Ask for more than an hour before she has chosen whether to offer it.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("loneliness", "Eliandra", '''"Sometimes. Katair and I have stood beside each other through an age of war. That does not mean we can stand in each other's place. He keeps the guards alive; I keep the temple's purpose visible. We trust one another with the lives entrusted to us. We do not always know what the other has set aside to do it."''',
            c("Ask what she has set aside, and leave her free not to answer.", "rest"),
            c("Say that a century beside him sounds like a marriage.", "bad_assumption", flags=("eliandra.trickster.opening_closed",)),
            c("Tell her she does not have to defend her bond with him to you.", "interest")),
        page("bad_assumption", "Eliandra", '''"It sounds like a century beside him. That is what it is. Do not make my closest ally into a husband because you want my history to arrive in a shape you understand." {n}Her voice is quiet. The rebuke is not.{/n}

"Katair is my fellow leader and a loyal friend. I have never called him my spouse. You do not need to put us in a romance to imagine one for yourself."''',
            c("Apologize without asking her to make the correction gentler.", "repair"),
            c("Insist you only meant that they are close.", "pressure", flags=("eliandra.trickster.opening_closed",)),
            c("Leave and accept that you have ended the audience.", "withdraw", flags=("eliandra.trickster.opening_closed",))),
        page("interest", "Commander", '''{n}You have spoken of rules and the people who must live beneath them. Now you let the silence settle before you say anything about yourself. Eliandra watches you with a different attention. There is enough space between you that neither has to pretend a step was unavoidable.{/n}

"I am interested in you as a woman, not as a reward for making the temple's life easier. I have noticed your voice when you disagree, and the way you listen before you decide what someone meant. I have wondered what that composure would become if you let yourself want something plainly. I also know this room is full of duties you did not invent and cannot abandon. You do not owe me a response tonight. I would like to know whether you want another private conversation, when there is no crisis to excuse it."''',
            c("Make clear that a no ends the question, not her place in the temple.", "invitation_answer"),
            c("Take back the question and leave her in peace.", "withdraw", flags=("eliandra.trickster.opening_closed",)),
            c("Ask whether the light on her face makes every other woman seem dim.", "bad_flattery", flags=("eliandra.trickster.opening_closed",))),
        page("meeting", "Eliandra", '''"You may stay as a guest, if the people here agree. I will not have the meeting become a hearing where the Commander waits to reward the answers he prefers." {n}She looks toward the hall, where the last conversation has ended and the guards are changing watches. The rule has not changed; neither has the memory behind it. The temple's lonely decades are not a ledger entry you can balance with a speech.{/n}

"The people will speak of jealousy, quarrels, and breakups. They will speak of the couple who cannot leave this place and the person who has already lost a family outside it. They may ask us to keep the rule. They may ask us to change it. A fair trial will not make either answer painless."''',
            c("Say you will sit where she places you and make no argument unless asked.", "interest"),
            c("Offer to leave so no one feels watched by the Commander.", "close_respect", flags=("eliandra.trickster.opening_closed",)),
            c("Insist that they need to hear your judgment first.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("repair", "Eliandra", '''"Thank you. An apology is not a door that obliges me to open another one. But the fact that you can hear a correction without asking me to soften it matters." {n}She returns the quill to the table. The bent feather does not straighten.{/n}''',
            c("Ask what she wants to do with the conversation now.", "her_subject"),
            c("Offer to end it here.", "withdraw", flags=("eliandra.trickster.opening_closed",))),
        page("invitation_answer", "Eliandra", '''{n}Eliandra is silent long enough for the last light to leave the painted stars. She studies you as though weighing not whether you are sincere, but what your sincerity might ask her to carry.{/n}

"I would like another conversation. I am curious about you, and that curiosity is mine. It is not gratitude. It is not a promise of romance, nor permission to treat my attention as a beginning I have already chosen. I have seen what happens when people decide another person's heart for them." {n}Her gaze catches on your mouth, holds there for a breath, then returns to your eyes. She does not pretend you failed to notice. The warmth that reaches her face is not a priestess blessing. It is a woman's response, tentative and alive.{/n}

"I have spent so long teaching myself that wanting something is less important than protecting everyone around me. I am not certain that lesson was false. I am certain it did not make the wanting disappear. If I look at you and wonder how it would feel to be kissed, that is a thought I can own without making it a promise you can collect."''',
            c("Thank her, and ask her to choose the time and place.", "welcome", flags=("eliandra.trickster.private_conversation_welcomed",)),
            c("Say you would rather not begin anything while she is unsure.", "close_respect", flags=("eliandra.trickster.opening_closed",)),
            c("Tell her curiosity is enough and press for a kiss.", "pressure", flags=("eliandra.trickster.opening_closed",))),
        page("bad_flattery", "Eliandra", '''"You speak as if a compliment becomes more intimate when you make it impossible to refuse. I am not a star in one of your tricks, Commander. I am a woman standing here, and I can tell when you are admiring me instead of listening."''',
            c("Apologize and ask whether she wants to continue the conversation.", "repair"),
            c("Tell her she is too serious to understand a joke.", "pressure", flags=("eliandra.trickster.opening_closed",)),
            c("Leave without demanding reassurance.", "withdraw", flags=("eliandra.trickster.opening_closed",))),
        page("pressure", "Eliandra", '''{n}The warmth leaves her face. She does not raise her voice or ask Katair to intervene. She does not need to.{/n}

"You have mistaken a willingness to speak for permission to manage me. This audience is over. The work we agreed to do for the people of Pulura's Fall remains separate from this. I will not punish them for your presumption, and I will not meet you privately again."''',
            c("Accept her answer and go.", "end", flags=("eliandra.trickster.opening_closed",))),
        page("withdraw", "Narrator", '''{n}You step away from the western arch. Eliandra does not call you back. Her duties remain, and so does her freedom to decide whether this conversation was enough.{/n}''',
            c("End the audience.", "end")),
        page("close_respect", "Eliandra", '''"Then I will leave the next choice where it belongs. The community will hear from me tomorrow. Tonight, I have said what I needed to say." {n}She offers you no promise and no dismissal. You leave the hall with the difference intact.{/n}''',
            c("End the audience.", "end")),
        page("welcome", "Narrator", '''{n}Eliandra asks you to return after the community has met and after the immediate work at Pulura's Fall permits it. She has not changed her calling, surrendered her judgment, or agreed to a romance. She has chosen one more conversation, and the choice is hers to renew or withdraw.{/n}

{n}At the far end of the hall, Katair finishes speaking with the sentry. He gives Eliandra a brief nod. She returns it with the ease of a trust built through a century, not a signal for you to interpret. The temple goes on around all three of you.{/n}

{n}When you turn to leave, Eliandra's hand brushes the back of yours. It might be an accident; it might be a question. She does not close her fingers around your wrist, and you do not turn it into an answer for her. She lets the moment remain a moment, then gives you a small, private smile.{/n}

"Next time," she says, "we can discover whether your cleverness survives a conversation that has nothing to do with a crisis." The suggestion carries more heat than her voice. It also carries a boundary: there will be a next time only if she still wants one when it arrives."''',
            c("Leave without asking for more than she offered.", "end")),
        page("end", "Narrator", '''{n}The stars painted above Pulura's altar do not arrange themselves into an omen. What happens next will depend on the temple's choices, Eliandra's duties, and whether she still wants you there when the next conversation becomes possible.{/n}'''),
    ],
    requires=("trickster", "eliandra.native_pulura_contact_verified", "eliandra.actor_alive_and_present", "eliandra.invited_private_audience"),
    RequiresAnyGroups=[("eliandra.native.rule_reformed_verified", "eliandra.native.rule_retained_verified")],
    forbids=("eliandra.trickster.opening_closed", "eliandra.trickster.private_conversation_welcomed", "eliandra.native_conflict"),
    delay=0,
    last=3,
    optional=True,
    Relationship="eliandra.trickster",
    ManualOnly=True,
    Remote=False,
    PhysicalPresenceRequired=True,
    ContactUnit="Eliandra",
)


SCENES = [SCENE]


if __name__ == "__main__":
    import json
    from collections import deque
    from pathlib import Path

    nodes = {node["Id"]: node for node in SCENE["Nodes"]}
    assert len(nodes) == len(SCENE["Nodes"]), "duplicate node IDs"
    assert SCENE["Entry"] in nodes
    terminals = {"end"}
    for node in SCENE["Nodes"]:
        for choice in node["Choices"]:
            assert choice.get("Next") in nodes or (node["Id"] == "end" and choice.get("Next") is None), (node["Id"], choice)
            assert not any(flag.startswith("eliandra.native.") for flag in choice.get("Set", ())), node["Id"]
    visited = set()
    queue = deque([SCENE["Entry"]])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for choice in nodes[current]["Choices"]:
            if choice.get("Next") is not None:
                queue.append(choice["Next"])
            check = choice.get("Check", {})
            queue.extend(target for target in (check.get("Success"), check.get("Failure")) if target)
    assert visited == set(nodes), f"unreachable nodes: {set(nodes) - visited}"
    assert terminals <= visited
    assert nodes["invitation_answer"]["Choices"][0]["Next"] == "welcome"
    assert nodes["invitation_answer"]["Choices"][0]["Set"] == ["eliandra.trickster.private_conversation_welcomed"]
    assert all("eliandra.trickster.private_conversation_welcomed" not in choice.get("Set", ()) for node in SCENE["Nodes"] for choice in node["Choices"] if node["Id"] != "invitation_answer")
    assert all("eliandra.trickster.romance_committed" not in choice.get("Set", ()) for node in SCENE["Nodes"] for choice in node["Choices"])
    assert nodes["pressure"]["Choices"][0]["Set"] == ["eliandra.trickster.opening_closed"]
    serialized = json.dumps(SCENE, ensure_ascii=False)
    assert serialized.count("{/n}") == serialized.count("{n}")
    assert all(source["id"] for source in NATIVE.values())
    print(f"Eliandra opening graph OK: {len(nodes)} nodes, {sum(len(n['Choices']) for n in nodes.values())} choices, {len(visited)} reachable nodes")
