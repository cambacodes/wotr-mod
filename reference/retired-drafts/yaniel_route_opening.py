"""A post-rescue Yaniel opening; authored prototype, not yet integrated."""

from story_format import c, n, scene


# These are authored contract names, not native game etudes or verified live flags.
# The first two native cues below are evidence for an integration design, not producers.
# Integration must set the identity witness only from the genuine Fane rescue branch;
# neither the earlier fake nor a name, portrait, or Radiance possession check is enough.
NATIVE_EVIDENCE = {
    "genuine_rescue_identity": {
        "path": "World/Dialogs/c3/MidnightFane/TrueYaniel/Cue_0001.jbp",
        "guid": "cedf416f4d873d0468b01270c7b8eb9e",
        "meaning": "Yaniel identifies herself after helping free the final victim.",
    },
    "radiance_recognition": {
        "path": "World/Dialogs/c3/MidnightFane/TrueYaniel/Cue_0008.jbp",
        "guid": "cbf1a11c8d3ce814595149a211502ad1",
        "meaning": "Yaniel recognizes and takes Radiance; later Fane dialogue returns it to the Commander.",
    },
    "false_impersonation": {
        "path_prefix": "World/Dialogs/c2_vs/DrezenSiege/FakeYaniel_First/",
        "meaning": "A separate earlier impostor branch; it must never set the genuine-rescue witness.",
    },
}

CONTRACT = {
    "requires": [
        "yaniel.genuine_midnight_fane_rescue_witness",
        "yaniel.radiance_recognition_witnessed",
        "yaniel.confirmed_alive_and_unbound_at_contact",
        "yaniel.contact_invitation_authored_by_yaniel",
    ],
    "forbids": [
        "yaniel.fake_yaniel_branch_without_genuine_rescue_witness",
        "yaniel.dead",
        "yaniel.contact_refused",
        "yaniel.identity_or_agency_lost",
    ],
    "path_access": {
        "Angel": "Unresolved. Build on shared duty only after Yaniel freely asks for contact.",
        "Aeon": "Unresolved. Evidence and temporal responsibility may open a meeting; no assumption that she forgives the past.",
        "Azata": "Unresolved. Shared defense can provide an invitation, not instant intimacy.",
        "Demon": "Unresolved. Require a costly, observed act of restraint; preserve her right to refuse a dangerous Commander.",
        "Devil": "Unresolved. Any terms must be explicit, revocable, and independently judged by Yaniel.",
        "Gold Dragon": "Unresolved. Shared protection is a possible authored bridge, pending actor and chapter verification.",
        "Legend": "Unresolved. A mortal future may matter, but must not be treated as the only acceptable life for her.",
        "Lich": "Unresolved. No route if she is dead, enslaved, or reduced to a trophy; a credible free-survivor state is required.",
        "Swarm-that-Walks": "Unresolved. A separate survival intervention would be required; refuse if Yaniel's identity or agency is lost.",
        "Trickster": "Unresolved. A later bounded fate intervention may reopen a missed or hostile opportunity only if Yaniel is alive and can independently choose contact.",
    },
}


def make_scene(id, title, nodes, *, previous=None, delay=4):
    return scene(
        "yaniel.opening." + id,
        title,
        "Yaniel",
        3,
        "Attend Yaniel's requested meeting",
        nodes,
        requires=tuple(CONTRACT["requires"]) + ((previous,) if previous else ()),
        forbids=tuple(CONTRACT["forbids"]),
        delay=delay,
        optional=True,
        PhysicalPresenceRequired=True,
        ActorContract="yaniel.genuine_surviving_unbound_actor_unverified",
        AreaContract="yaniel.post_fane_meeting_location_unverified",
        Relationship="yaniel.opening",
        ContactContract="yaniel.invitation_from_yaniel_unverified",
    )


SCENES = [
    make_scene("the_letter", "A letter without a debt", [
        n("opening", "Narrator", '''{n}The letter arrives after the Midnight Fane, once Yaniel has spoken with the Hand of the Inheritor and chosen to leave the place of her rescue. The exact interval and courier are authored for this proposed continuation; the game has not been checked for a native contact event.{/n}
{n}There is no office seal. The handwriting is firm, though the downstrokes tremble where the page has been folded and opened again.{/n}
"Commander,

"I held Radiance in the Fane. It knew me. Then I put it back in your hands, because the road ahead belonged to you. That is a fact I can hold without deciding what it means about you.

"People keep saying that I am free as though the word itself should settle everything. I am free of the chains in the fane. I am not suddenly well, young, unafraid, or ready to be made an example of. Some mornings I wake expecting Minagho to be standing where the light falls across the door. Other mornings I feel angry that my body learned to expect it.

"You helped get me out. I thank you for that, and I will not pretend the help was meaningless. It does not buy my confidence, my time, or any particular feeling. I am writing because I want one conversation in which I am not asked to testify to the meaning of my survival.

"If you are willing, meet me in a quiet place after the evening bell. I will choose the place when I know whether you are coming. Bring no guard unless you believe you need one. I can leave whenever I choose. If you decline, say so plainly. I will not have a courier pursue you for an answer."''',
            c("Accept, and let Yaniel set the terms of the meeting.", "meet", flags=("yaniel.opening.meeting_accepted",)),
            c("Decline the meeting, without asking her to explain herself.", "decline", flags=("yaniel.opening.contact_declined",)),
            c("Ask whether she would prefer a letter instead of a meeting.", "letter_option")),
        n("decline", "Narrator", '''{n}Your reply says no without decorating the answer as a noble sacrifice. Yaniel's acknowledgment comes two days later.{/n}
"Thank you for answering directly. I meant what I wrote: I will not pursue you. I may send a practical note if the sword or the crusade requires it, but I will not disguise courtship as duty. May your road be yours."''',
            c("Leave the exchange there.", flags=("yaniel.opening.closed_friendly",))),
        n("letter_option", "Narrator", '''{n}Yaniel's answer arrives in her own hand.{/n}
"A letter is easier to put down, but harder to read honestly. I have chosen a meeting because I want to see whether speaking to you feels like speaking to a person, rather than answering a symbol. I can change my mind when I arrive. You can too."''',
            c("Accept her stated choice and attend.", "meet", flags=("yaniel.opening.meeting_accepted",)),
            c("Decline after all.", "decline", flags=("yaniel.opening.contact_declined",))),
        n("meet", "Narrator", '''{n}Yaniel chose a quiet courtyard with two clear exits and no audience. The precise place is an authored placeholder, not a verified in-game location. Age has left its honest marks: fine lines at her eyes, silver in her hair, and a measured care in the way she shifts her weight. None of it diminishes her. She carries herself like a woman who has spent a lifetime deciding where to plant her feet.{/n}
She wears a simple dark-blue coat over a plain shirt. Radiance rests within reach, not in her hand. Her gaze flicks to the sword, then to you.
"I considered leaving it behind. Then I remembered I have spent enough of my life being told what I ought to carry. It can sit there without deciding this conversation for us."
She gestures to the second chair but does not sit until you do. When you mention the rescue, her jaw tightens.
"I am grateful you helped me out. I am also tired of gratitude being treated like a key. Those truths do not cancel each other. Tell me something about yourself that is not a campaign report. I have had enough years of other people explaining history to me."''',
            c("Ask what she wants from the days ahead, and listen before advising.", "living"),
            c("Tell her you are glad she survived, then let her choose the next subject.", "living"),
            c("Say you understand, though you cannot know what the fane cost her.", "honest"),
            c("Tell her the Commander can make the world repay what it took.", "challenge")),
        n("honest", "Yaniel", '''"Good. Do not borrow my pain to make yourself sound wise." The answer is sharp, but not cruel. She watches to see whether you defend yourself.
When you do not, some of the tension leaves her shoulders. "I spent years with people deciding what my captivity meant. Minagho wanted a husk. Areelu thought repairs could be made to a body as if the person inside were merely a stubborn part. I survived them both, but survival did not make me an object lesson."
She studies your face, measuring the silence instead of filling it for you. "You can still speak plainly. I am not asking you to be gentle at the cost of honesty."''',
            c("Ask what she wants now, rather than what the past made her.", "living"),
            c("Say you will leave the question alone unless she brings it back.", "living")),
        n("challenge", "Yaniel", '''Yaniel's chair scrapes once against the stone. "Do not promise vengeance in my name. I know how to choose my own enemies." Her hand has not gone to Radiance, but her expression has closed.
If you apologize without qualification, she stays long enough to hear it. "That is better. A person can offer help. She cannot appoint herself my champion and call that care."
The evening is not ruined, but the invitation has narrowed. She says she will write again if she wants another conversation. There is no flirtation in the promise, and no hidden request for you to persuade her otherwise.''',
            c("Apologize and leave the next contact to Yaniel.", "repair", flags=("yaniel.opening.boundary_heard",)),
            c("Insist you meant well and ask her to reconsider.", "end_hostile", flags=("yaniel.opening.contact_declined",))),
        n("repair", "Narrator", '''{n}You tell her that good intentions did not give you the right to speak for her. Yaniel accepts the apology without rewarding it with intimacy.{/n}
"Then we can finish the tea. We need not decide whether there will be another evening." The conversation returns to safer ground: the garden's neglected roses, the work of rebuilding, and the strange sensation of hearing the citadel's bells without wondering whether they mark an execution.
When you part, she thanks you for hearing the boundary. It is not an invitation to test it again.''',
            c("Part as allies, with no romance assumed.", flags=("yaniel.opening.allies",))),
        n("end_hostile", "Narrator", '''{n}Yaniel rises. "You have asked me to soften the consequence of a boundary you heard. I am not going to do that." She leaves by the nearer gate, with no guard summoned and no scene made of her departure.{/n}
No new contact is scheduled. The rescued paladin remains free to pursue her duties and her own recovery without the Commander in her private life.''',
            c("End the conversation.", flags=("yaniel.opening.closed_hostile",), abort=True)),
        n("living", "Narrator", '''{n}She listens, then tests your account with a question about a choice you made during the campaign. She catches the gap between the answer you give your council and the one you give her.{/n}
"A polished answer. I used to give those to commanders who mistook confidence for truth." A corner of her mouth lifts. "You are more interesting when you stop trying to sound inevitable."
She speaks of wanting to learn which names have survived the years, and which places are now only memorials. She refuses to call herself an old story, then laughs at her own indignation.{/n}
"I am old enough to know that a legend is useful to other people. It is a terrible substitute for a life. I would like to find out what I still enjoy when no one is watching for a lesson." She tells you that, before the siege, she liked late suppers and arguments that ended in laughter. Her memories are not a promise to recreate youth. "The woman I was is part of me. She is not the only person I am allowed to become."
She looks you over with an appraising frankness. "And I have not forgotten how to want company. I have simply become selective about whose company I want." Her smile is brief, almost challenging. "Do not look so pleased. I have not said it is yours."''',
            c("Tell her disagreement is welcome, then ask what she thinks of your choices so far.", "disagreement"),
            c("Admit you hoped the meeting might become courtship, and leave her room to refuse.", "desire"),
            c("Say friendship would be enough, and let her decide whether to write again.", "friendship"),
            c("Ask about the fane in detail, before she has offered it.", "intrusive")),
        n("intrusive", "Yaniel", '''"No." Her voice is quiet. It leaves no room for confusion. "I will tell you what I choose, when I choose. If you want to know me, you cannot make the worst thing that happened to me the price of admission."
She stands and offers you her hand, not as a reconciliation but as a civil end to the meeting. You can take it or simply bow. The contact remains closed unless she later chooses to reopen it.''',
            c("Apologize, accept the end of the meeting, and do not ask again.", flags=("yaniel.opening.closed_friendly",), abort=True),
            c("Defend the question as necessary for trust.", "end_hostile", flags=("yaniel.opening.closed_hostile",))),
        n("friendship", "Yaniel", '''"Friendship is a word I can answer without having to settle the rest." She gives a small, tired smile. "I would like to write again. If that changes, I will say so. Do not turn my kindness into a test I have to pass."''',
            c("Agree to let the friendship remain what she named it.", flags=("yaniel.opening.friendship",))),
        n("disagreement", "Narrator", '''Yaniel's opinion is not flattering, but it is careful. She thinks your first instinct is to turn uncertainty into a problem you can solve. You tell her that may be true. She asks whether you can bear to leave a problem unsolved when the person in it asks you to stop.
"That is where duty becomes dangerous," she says. "A paladin can hide a desire to control behind a fine word. So can a commander. So can a lover, if people let that word excuse too much."
You tell her that lovers can also tell one another when they are wrong. Yaniel's eyes sharpen. "Good. I dislike being agreed with just because someone hopes I will take off my coat." The answer lands with enough heat to make you both pause. Then she laughs, low and unguarded, before adding, "Though I admit the thought crossed my mind. I am not yet saying what I might do with it."
You do not agree on every example. The disagreement stays alive between you, with neither of you surrendering merely to make the evening easier. At the gate, Yaniel says she enjoyed parts of the conversation. The qualification is deliberate.
"I may ask you to supper another night. That would be my invitation, not your reward. Tonight I want to walk back alone."''',
            c("Say you would welcome the invitation and let her leave alone.", "later", flags=("yaniel.opening.future_invitation_possible",)),
            c("Say you hope she asks, but only if she wants to.", "later", flags=("yaniel.opening.future_invitation_possible",))),
        n("desire", "Yaniel", '''You tell her you are attracted to her and would be interested in courtship, but that she owes you neither a yes nor an explanation. Yaniel studies you for a long moment.
"You have a talent for making a dangerous question sound like a petition." She taps one finger against her cup. "I am not offended by desire. I am offended when people treat desire as proof that they understand me. You do not. Not yet."
Her gaze returns to your face. "Still, I have looked at you tonight and wondered what your mouth would do with an answer you did not control. That is mine to wonder about. It is not your permission to take anything."
She reaches across the table, stopping with her fingers a hand's breadth from yours. "May I touch your hand? I am asking because I want to, not because this evening requires a gesture."''',
            c("Accept the offered hand, and let her set the duration.", "touch", flags=("yaniel.opening.touch_consented",)),
            c("Say you would rather wait, and thank her for asking.", "wait", flags=("yaniel.opening.touch_declined",)),
            c("Ask whether she is certain, without urging her to decide now.", "certain")),
        n("certain", "Yaniel", '''"No. I am curious. That is not the same thing." She draws her hand back. "Thank you for making room for that answer." The honesty costs the possibility of a dramatic kiss; it makes the evening safer to remember.''',
            c("Leave the question open for another day, if she wants one.", "later", flags=("yaniel.opening.curiosity_only",)),
            c("Say you would prefer to remain friends.", "friendship", flags=("yaniel.opening.friendship",))),
        n("wait", "Yaniel", '''She nods and folds both hands around her cup. "That is a good answer. I wanted to ask, not to be applauded for asking." The air between you settles. No disappointment is put on your shoulders, and no physical affection follows without a new choice.''',
            c("Continue talking, with no touch assumed.", "later", flags=("yaniel.opening.touch_declined",))),
        n("touch", "Narrator", '''{n}Yaniel's hand is warm and steady. Her fingers are strong, the skin marked by age and years of sword practice. She lets the contact last for a few breaths, then withdraws first. You do not close the distance after she does.{/n}
"That was pleasant," she says, plainly surprised. "It does not settle the question. But it is a beginning I chose." She looks at you with a frankness that is neither girlish nor ceremonial. "If there is a next time, I want it to include food, an argument, and the chance to change my mind before either of us calls it a courtship."''',
            c("Agree, and let her decide whether to send the next invitation.", "later", flags=("yaniel.opening.future_invitation_possible",))),
        n("later", "Narrator", '''{n}Yaniel leaves by herself. No second meeting is scheduled by this prototype. If she chooses to write later, that contact must come from a verified, authored producer and not from an automatic assumption that the first conversation began a romance.{/n}
She has not forgiven Minagho, made peace with Areelu's actions, or traded her paladin's calling for the Commander. She has made one adult choice about one evening. Whether that choice grows into attraction is still hers to make.''',
            c("End the opening and await a freely authored follow-up.", flags=("yaniel.opening.complete",))),
    ]),
]
