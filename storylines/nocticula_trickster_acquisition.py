"""Development-only beginning of an authored Chapter 5 Trickster contact quest.

Native audience and history bindings are read-only.  The seal is authored magic,
not an inventory item, a Gift replacement, parent acceptance or a resurrection.
The post-conflict preparation deliberately awaits an unimplemented lifecycle
producer; no death etude is treated as an observed corpse.
"""
from copy import deepcopy

from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
AUDIENCE_ANSWERS = "2729c49e2bf20c64caa4f54b352e03f6"
ETUDES = {
    "noct.parent_active": "18affced672d4c56a52bf6ffc00601b9",
    "noct.parent_rejected": "761ca3572c1145ebb755032d613bff46",
    "noct.gift": "0c1695f4a362f0243a4afcfd1957eb0d",
    "noct.acq.gift_renewed": "f5be7095af9d43779ce79a52ec27425d",
    "noct.acq.gift_refused": "0383369136fadc247b7d6ff99110fa55",
    "noct.acq.gift_broken": "61b07b3511bb71646a717c2b3c0f3bf6",
    "noct.dead": "e581f609dc0f44a481e7e88824ac39da",
    "noct.acq.council_fight": "ed5d1dfa2402bed4cb7a59a21c14a1a4",
}
COMPLETED_ETUDES = {
    "noct.acq.original_gift_completed": "0c1695f4a362f0243a4afcfd1957eb0d",
}
SEEN_CUES = {
    "noct.acq.audience_question": ["20451daada07f744b9d7f3e14a37a864"],
    "noct.socoth_plan_exposed": ["bb552fe4e21cb874fa3c98c2cc328186"],
    "noct.acq.threshold_projection_answer": ["77216dc2c3770794f93b010659f4aa64"],
}
SELECTED_ANSWERS = {
    "noct.acq.council_disclosed": "fd4f6c1d6397fa94db7aaf08de7dfeca",
}
RELATIONSHIP = dict(
    Title="An address she has not given you",
    Description="Nocticula has heard a request for another conversation. Her answer will have a price of its own.",
    Objective="Prepare the narrow channel she permitted",
    Guidance="Finish your Council audience, then prepare the correspondence Nocticula permitted. The divided seal grants a chance to speak, not a renewal of your old bargain.",
    StartedFlag="noct.acq.requested", ClosedFlag="noct.acq.closed",
    CommittedFlag="noct.acq.renewed_agreement",
    UnavailableFlags=["swarm", "legend", "dragon"], FailureFlags=[],
)
CONTRACT = {
    "status": "living opening in development export; post-conflict draft unregistered; native gameplay unverified",
    "native_hook": "AnswersList_0007, before Cue_0016's reward and Cue_0019's teleport; never a reusable post-departure actor",
    "authored_objects": "The divided wax impression, keyed answering mark and dream aperture are story objects, not granted inventory or stat facts.",
    "incomplete_producers": {
        "noct.acq.conflict_resolved_verified": "Requires a reviewed actual Council resolution producer; FightAgaintsNoctaCouncilAllied and NocticulaDead alone are insufficient.",
        "noct.acq.postconflict_reply_verified": "Future identity-checked Chapter 5 reply mechanism; no scene here writes this flag or asserts that Threshold occurred early.",
    },
    "not_implemented": ["missed audience after departure", "living Shamira essence transaction", "post-conflict verified response", "body or government restoration", "Worldwound/crossroads pact", "romance acceptance", "parent continuation join", "native Gift grants", "inventory or gold effects"],
}


def f(*names):
    return tuple("noct.acq." + name for name in names)


def page(id, speaker, text, *choices):
    return n(id, speaker, text, *choices, portrait="Nocticula")


COMMON_REQUEST = [
    page("request", "Commander", '''"I want a way to ask you a question after I leave. One which your brother has not supplied."
{n}Nocticula looks toward the place through which you entered. The glance is brief enough to make you wish you had phrased the request less conveniently.{/n}
"You have discovered the disadvantage of arriving through another person's ingenuity. He may consider the return journey part of his entertainment."
"I thought you might prefer to choose who knocks."
"I prefer to choose whom I admit. People who confuse the two are a considerable expense."
{n}She holds out her hand. When you do not immediately put anything in it, her mouth curves.{/n}
"A useful hesitation. Most petitioners invent a gift at this point. What are you actually offering?"''',
         c('"An account of the part of your brother\'s scheme that concerns you. Hear it here, where I must answer questions."', "price"),
         c('"I wanted private access without another bargain. That was an unreasonable request."', "decline")),
    page("price", "Nocticula", '''"Then give the account to me before you leave. I shall decide whether it deserves another conversation."
"You have not heard it yet."
"You have not yet received the thing you asked for. We have both been spared a disappointment."
{n}She presses a thumb into the wax pooled beside a lamp. The wax darkens without burning her. She draws it out in a thin disc, turns it, and breaks it across the center. One half remains between her fingers. She places the other on the table within your reach.{/n}
"If I accept what you bring me, fold your request around this. Write your own name. Not a title, not the name my brother found amusing, and not somebody else's hand hired to make yours look better."
"Will it reach you?"
"It will ask whether I wish to receive it. If I do not, you will still own half an ugly seal."
{n}The two halves have different edges. You can see where yours might be made to resemble hers. It would be a remarkably small alteration for a remarkably large intrusion.
Nocticula turns her half over before you finish studying it.{/n}
"There. You noticed the attractive mistake. What will you do with it?"''',
         c('"Give you the possibility of refusing. I want an answer worth hearing."', "bounded", flags=f("petition_candid")),
         c('"Keep the shape in mind. If someone else copies it, I would rather recognize the attempt before you blame me."', "leverage", flags=f("petition_watchful")),
         c('"Nothing. Keep both halves. I will speak about the Council and leave the private question alone."', "decline")),
    page("bounded", "Nocticula", '''"You say that while you are still hopeful. We shall discover whether it remains true when I am occupied."
{n}She touches the broken edge to your open palm. A small warmth runs along your fingers and fades. When you lift the wax, its reflection in the table's polish is incomplete: a line is missing from the center.{/n}
"My half supplies that line. If you draw it yourself, you will have a handsome impression of your own expectations. I recommend keeping it. Many men require a shrine before they recognize the object they have been worshipping."
"And women?"
"Usually better craftsmen. No less persistent."
{n}You wrap the half in a blank sheet. She waits until you have put it away.{/n}
"Now earn the trouble you have asked me to consider. Tell me what my brother has been doing."''',
         c('[Return to the audience and give your own account of the Council.]', flags=f("requested", "seal_received"))),
    page("leverage", "Nocticula", '''"You would like a little knowledge which obliges me to hear you."
"I would like to know whether the voice answering me is yours."
"Both can be true. Your second answer was better dressed."
{n}She touches the broken edge to your palm, then scores one shallow line across the back of the wax. You have not seen her make the matching stroke on her own half.{/n}
"Keep your curiosity. Do not improve my reply before I have made it. If you counterfeit the missing line, I will know what sort of conversation you preferred."
"You sound almost interested in the attempt."
"I am often interested in things I intend to punish. Try to remain capable of distinguishing that from an invitation."
{n}She leaves the wax in your hand and withdraws her fingers. It is cooler than your skin.{/n}
"The Council," {n}she says.{/n} "Before your private ambitions acquire another chapter."''',
         c('[Keep the marked half and return to the Council conversation.]', flags=f("requested", "seal_received"))),
    page("decline", "Nocticula", '''{n}Nocticula lowers her hand and waits until you have finished speaking.{/n}
"Then we have finished that question. You may yet have something interesting to say about the business which brought you here."
{n}She turns back to the audience as if you had already left it, and lifts two fingers. A servant who was not there a moment ago steps out of the shadow by her couch with her cup.{/n}''',
         c('[Leave the request unmade.]', flags=f("closed"))),
]

SCENES = []


def request_variant(history, text, requires=(), forbids=(), groups=()):
    nodes = [page("history", "Nocticula", text, c('"Then hear what I am asking now."', "request")), *deepcopy(COMMON_REQUEST)]
    SCENES.append(scene(
        "noct.acq.audience_" + history, "A request before departure", "Nocticula", 5,
        '"Before I leave, there is another question."', nodes,
        requires=("trickster", "noct.acq.audience_question", *requires),
        forbids=("noct.dead", "noct.acq.council_fight", *f("closed", "requested"), *forbids),
        optional=True, Relationship="nocticula.acquisition", Remote=False,
        NativeReturnCue="20451daada07f744b9d7f3e14a37a864",
        AnswerLists=[AUDIENCE_ANSWERS], Chapters=[5], RequiresAnyGroups=[list(g) for g in groups]))


request_variant("missed", '''"Another question? You have arrived with a generous estimate of my patience."
{n}Nocticula waits, one nail tapping the arm of her couch, and lets the silence grow expensive.{/n}
"I would like to know you when neither of us is performing for your brother."
"You believe I have stopped performing because he cannot hear me?"
"I believe you might enjoy a different audience."
{n}Her smile acknowledges the answer without rewarding it.{/n}
"Possibly. You have not told me why it should be you."''',
    forbids=("noct.parent_active", "noct.parent_rejected"))
request_variant("rejected", '''"You were more certain when you refused me. I remember finding the certainty tedious."
"I am not asking you to forget it."
"How economical. You ask me to supply a second opportunity and propose that I keep the first expense myself."
{n}She turns toward you fully. The attention is less comfortable than the smile with which she began.{/n}
"What has changed?"
"I want to ask for something smaller, and answer for wanting it. You may dislike the answer again."
"I may dislike it more accurately. Continue."''', requires=("noct.parent_rejected",))
request_variant("patronage", '''"You have discovered that refusing a means of access can make access inconvenient."
"I am asking for a conversation."
"Yes. You have become wonderfully particular about the word."
{n}Nocticula studies you as though comparing the request with an earlier answer she remembers too well.{/n}
"Our history does not disappear because you want a different door. Nor does a familiar door prove that you have come willingly. Tell me what you want this one to admit."''',
    requires=("noct.parent_active",), forbids=("noct.parent_rejected", "noct.gift"),
    groups=(("noct.acq.original_gift_completed", "noct.acq.gift_broken", "noct.acq.gift_refused", "noct.acq.gift_renewed"),))


def add_remote(id, title, nodes, previous, delay=12):
    SCENES.append(scene("noct.acq." + id, title, "Memory", 5, title, nodes,
        requires=tuple(dict.fromkeys(("trickster", "noct.acq.council_disclosed", "noct.socoth_plan_exposed", *f("requested", "seal_received", previous)))),
        forbids=("noct.dead", "noct.acq.council_fight", *f("closed", id + "_done")),
        delay=delay, optional=True, Relationship="nocticula.acquisition", Remote=True,
        Areas=[DREZEN], Chapters=[5]))


add_remote("the_missing_line", "The missing line", [
    page("start", "Narrator", '''{n}In Drezen, the half-seal leaves a cold mark on the sheet beneath it. You have written Nocticula's name twice and crossed it out twice. The instructions required your own.
Her answer about the Council returns to you, and the look that came with it: the look she gives a debt she has not yet decided how to collect.
You write your name. Nothing happens.
When you fold the paper around the wax, the crossed-out letters become visible through its back. They do not shine. They cast a small shadow toward a light which is not in your room.
The opening is narrow enough to examine without sleeping. Something could follow the reflection back if you gave it the rest of the room. You draw the lamp closer and move the papers bearing your officers' names out of its light.{/n}''',
         c('[Knowledge: Arcana 34] Bind the reply to the missing stroke and keep the room outside the reflection.', flags=f("channel_attempted"), forbids=f("channel_attempted"), check=dict(Skill="SkillKnowledgeArcana", DC=34, Success="fine", Failure="torn", CommanderOnly=True)),
         c('Use the seal as a sealed question. Give up the possibility of hearing her answer tonight.', "slow", flags=f("channel_slow")),
         c('Put it away. You are not ready to offer even this much access.', abort=True)),
    page("fine", "Commander", '''{n}You trace the folded edge instead of the line Nocticula withheld. The difference catches under your fingers: an unanswered question may be carried without pretending to contain its own answer.{/n}
{n}You turn the fold inward. The shadow ends at the crease. Beyond it there is darkness, but no glimpse of your desk, door or sleeping city.{/n}
{n}For a moment you can feel how easily the fold could be widened. Your gift for making an exception is waiting for a larger proposition. You leave it waiting.{/n}
{n}Three small impressions appear in the wax. None matches the movement of your hands.{/n}
{n}You tap the paper twice. There is a pause. Then a single answering tap comes from the wrong side of the table.{/n}
{n}You have attracted someone's attention. The unanswered part is whose.{/n}''',
         c('Keep the narrow opening and ask her to complete the mark you never saw.', "question", flags=f("channel_narrow"))),
    page("torn", "Narrator", '''{n}The fold catches a reflection of the lamp. It begins repeating down a corridor which should not fit inside the sheet. On the third repetition, another light appears.
You flatten the paper. The corridor closes, leaving a scorched crease and a sound like somebody drawing breath on the far side of a locked door.
The wax is intact. Its warm edge has impressed part of your name into the tabletop.
You cannot tell whether the other light belonged to Nocticula. Opening the same fold again would give whoever waited there a better view of the room.{/n}
"No," {n}you say, to the empty chair.{/n}
{n}You scrape the marked wood into a bowl and move your work to an inner room. The mark travels with the shavings; a fleck on the floor turns toward the bowl until you pick it up.
The wax will have to carry a closed question now. You will also have to tell Nocticula what nearly answered it.{/n}''',
         c('Seal the shavings with the request and disclose the failed opening.', "slow", flags=f("channel_exposed", "channel_slow"))),
    page("slow", "Narrator", '''{n}You wrap the wax so no light reaches its broken edge. The packet grows heavier for a moment, as though someone has laid a finger on the far end of it. Then the weight is only paper again.
This way offers no view into her room, and no voice to interrupt. You must write what you want her to answer, then endure the possibility that she will choose a different question.
There is space for a few lines. You leave the rest blank.{/n}''',
         c('Ask for her half of the authentication, and offer to account for your own.', "question")),
    page("question", "Commander", '''{n}You describe the incomplete reflection and ask her to add the part she withheld. You do not draw what you think it ought to be.{/n}
{n}Below that, you write the real request: an evening with her, on her side of the wax, with no brother in the room, no Council waiting and no report due at the end of it.{/n}
{n}The last sentence is less restrained. You tell her that you expect her to be difficult and would rather find out whether you can be interesting.{/n}
{n}You consider crossing it out. The line remains.{/n}
{n}The folded sheet goes dark from the center outward. When the shadow reaches the edge, it stops. Nothing in the room beyond it changes.{/n}''',
         c('Leave the request closed and wait for an answer.', flags=f("the_missing_line_done", "question_sent"))),
], "seal_received")

add_remote("her_hand", "The other hand", [
    page("start", "Narrator", '''{n}The packet opens while you are reading something else. A curl of dark wax rises from its center and forms a line you did not draw. It traces the old break, then turns beneath the wax in a direction you cannot see without lifting the paper.
You keep your hands where they are. The line finishes anyway.
"You may stop looking so pleased," Nocticula says. "I have corrected a piece of wax."
Her voice comes from the small completed mark. No figure occupies the chair.{/n}
"I asked you to answer."
"You asked several things. The last was better than the first. I dislike receiving instructions before I have decided to enjoy a visit."
{n}The answering stroke cannot be lifted from the original half. When you turn the sheet, her voice follows the mark rather than your reflection.{/n}
"Now tell me which opening you made."''',
         c('Describe the narrow reflection and the edge you kept closed.', "narrow_account", requires=f("channel_narrow")),
         c('Describe the closed packet and the answer you chose not to demand immediately.', "slow_account", requires=f("channel_slow"), forbids=f("channel_exposed")),
         c('Tell her about the second light and the marked shavings.', "exposed_account", requires=f("channel_exposed"))),
    page("narrow_account", "Nocticula", '''"You left a tempting amount unfinished. Was that discipline, or did something frighten you?"
"You may enjoy the result without choosing the flattering explanation for me."
"May I? How generous you become when I cannot see your face."
{n}The mark sharpens. You feel the edge of the opening, no wider than the paper, waiting for her to say something else.{/n}
"Keep that fold. A room is an unnecessarily large introduction. I shall send an invitation through it when I want one answered. If you pull at the other side, I shall stop answering."
"You would notice."
"I have noticed considerably less gifted people trying considerably more ingenious things. Your advantage is that I have not yet found yours tiresome."''',
         c('Ask what she requires before another invitation.', "history", flags=f("channel_provisional"))),
    page("slow_account", "Nocticula", '''"A letter. You came through my brother's mischief and have invented correspondence."
"I thought you might value the opportunity to leave me waiting."
"I have been enjoying it. The difficulty was deciding when you had enjoyed it enough."
{n}Something touches the opposite side of the sheet. There is a faint sound of a nail traveling around the completed mark.{/n}
"You will receive words first. No window, no body, no visit while you sleep. We can discover whether you possess a second interesting question before I lend you a room in which to ask it."
"Lend?"
"Do not begin negotiating the furniture. I have seen your sort make a kingdom out of an invitation to sit down."''',
         c('Accept written invitations while the trust remains narrow.', "history", flags=f("channel_letters_only"))),
    page("exposed_account", "Nocticula", '''{n}For several breaths there is no reply. Then the wax turns cold enough to sting through the paper.{/n}
"Put the bowl where you can see it. Do not open it."
"You recognize the second light?"
"I recognize an aperture pretending that being empty makes it safe. It may have attracted nothing capable of remembering you. You should prefer that possibility without conducting your affairs as though it has been proved."
{n}The shavings lift inside the sealed packet. You hear one strike the paper and fall.{/n}
"Bring me the shape you used. All of it. You will not keep a second route around the one I decide to close."
"That gives you my mistake."
"You offered me your ingenuity. I am discovering the cost of receiving it in installments."''',
         c('Surrender the working sketch and let her close the exposed route.', "repair", flags=f("sketch_surrendered")),
         c('Refuse to give her that leverage. End this attempt at private contact.', "close", flags=f("closed"))),
    page("repair", "Narrator", '''{n}You lay the sketch beneath the packet. You leave no copy beneath the blotter. Nocticula asks you to name the point at which the second light appeared, and stops you when you try to describe the whole attempt before answering that question.
One line chars. The shavings settle. A thin streak of ash runs into the wax and disappears.
You try the old fold without opening it. It no longer catches a reflection.{/n}
"There," {n}she says.{/n} "You may keep the paper. The clever part of it has become mine."
"And the conversation?"
"May continue as a letter. If I discover that you kept a useful omission, it will become a very short one."
{n}You have lost the private opening and given her the construction which failed. Her answering mark remains, small and legible beside your name.{/n}''',
         c('Keep the written channel and the cost of having it repaired.', "history", flags=f("channel_repaired", "channel_letters_only"))),
    page("history", "Nocticula", '''"Before you compose another request, there is an answer you have already given me."
{n}She lets the phrase hang. The sheet supplies no expression with which to soften it.{/n}''',
         c('"I refused you. I will not pretend this letter makes that refusal disappear."', "old_refusal", requires=("noct.parent_rejected",)),
         c('"We have an earlier understanding. I am asking for a different means of speaking, not a counterfeit of it."', "old_bargain", requires=("noct.parent_active",), forbids=("noct.parent_rejected",)),
         c('"There was no agreement between us to resume. I am asking you to consider a new one."', "no_bargain", forbids=("noct.parent_active", "noct.parent_rejected"))),
    page("old_refusal", "Nocticula", '''"Good. I disliked the answer. I would dislike being told I imagined it more."
"What would make you willing to hear another?"
"Something you are willing to lose before discovering whether I admire the gesture. I have admirers who mistake payment for a mechanism which operates me. They are frequently disappointed with the workmanship."
{n}You ask what she wants. She says that is the question for the next letter, and that you should decide first whether you are asking for power, company, or a chance to revise how she remembers you.{/n}''',
         c('Agree to answer that question without calling it reconciliation.', "patronage")),
    page("old_bargain", "Nocticula", '''"Then keep its terms available when they inconvenience you. People have an extraordinary memory for an agreement's privileges and a delicate forgetfulness about its price."
"You have not always made the distinction comfortable."
"No. I should be suspicious if that were the reason you remembered me."
{n}She will hear a proposal about another channel. She has not returned a blessing, canceled an earlier demand or agreed that the Worldwound can wait upon your private experiments.{/n}''',
         c('Keep the old terms separate from this trial correspondence.', "patronage")),
    page("no_bargain", "Nocticula", '''"You do possess an attractive capacity to arrive late and describe the empty chair as an opportunity."
"Is it occupied?"
"Not by an invitation I have made to you."
{n}The answer leaves you no graceful fiction of a relationship resumed. It also leaves her listening.{/n}
"Write what you want," {n}she says.{/n} "If your proposal begins with my becoming less difficult, spare us both the paper."''',
         c('Prepare to ask for her actual company rather than a gentler imitation.', "patronage")),
    page("patronage", "Nocticula", '''"And the gift? Are you hoping a better-mannered question will make it unnecessary to discuss that?"''',
         c('"Your renewed gift is a fact between us. It is not my answer to this invitation."', "terms", requires=("noct.acq.gift_renewed",)),
         c('"I retain your gift. I still want you to hear an answer I give while awake."', "terms", requires=("noct.gift",), forbids=("noct.acq.gift_renewed",)),
         c('"I will discuss patronage separately. This channel must carry words before it carries any promise of obedience."', "terms", forbids=("noct.gift", "noct.acq.gift_renewed"))),
    page("terms", "Nocticula", '''"Words can be expensive enough. We shall begin with those."
{n}The mark turns slowly on the page. You have the impression that she has lifted her half to look at it from another angle.{/n}
"Write me one proposal about the Council business which does not require pretending my enemies have stopped wanting what they want. If you intend to preserve somebody I was promised an answer about, say it plainly. I would prefer your scheme to its flattering summary."
"And after that?"
"You have already spent one letter asking me to promise the second. Try not to spend the second asking for the third."
{n}You smile despite yourself. She cannot see it, but her next words arrive with uncomfortable accuracy.{/n}
"There is the advantage of making you wait. You have had time to consider how much you wanted an answer."
{n}The wax cools. Its completed stroke remains. She has ended this conversation herself.{/n}''',
         c('Keep the trial correspondence. Prepare an actual concession before asking for more.', flags=f("her_hand_done", "correspondence_trial"))),
    page("close", "Narrator", '''{n}You tell her you will keep the sketch. The answering stroke lifts from the wax like a thread being pulled through cloth.{/n}
"Then keep it without my address," {n}she says.{/n}
{n}You flatten the packet. It reflects only the light in your room. There is still work to do about the place you exposed, but no reply waiting inside it.{/n}''', c('[End the attempt; the earlier history remains.]')),
], "question_sent")

# A separate preparation, never admitted by NocticulaDead alone.  Its actual
# resolution producer and identity-checked response remain root-owned work.
SCENES.append(scene("noct.acq.after_the_council", "An unanswered address", "Memory", 5,
    "Consider a message after the Council conflict", [
        page("start", "Narrator", '''{n}You put the account of the Council aside. It contains enough conflicting descriptions of Nocticula's departure to make a careless magician choose the one most useful to an experiment.
You have decided not to be that magician tonight.
There is a distinction between reaching someone who may answer and constructing the voice you remember. Your recollection could supply her contempt with distressing accuracy. It could not supply her decision.
You sketch an empty frame and leave its center untouched. Around it you place the questions a real reply would have to settle: what she remembers of your opposition, what she believes you owe, and what she would refuse even if you offered it beautifully.
None is an apology on your behalf. None is proof that she cannot answer.
The proposed message must admit what you did before it asks what she might do next.{/n}''',
             c('Write that you opposed her and want to negotiate with the person who remembers it.', "message", flags=f("conflict_admitted")),
             c('Put the frame away. Do not send a likeness in place of a question.', abort=True)),
        page("message", "Commander", '''You write her name outside the frame, where it addresses rather than describes her.
Then your own.
The first draft explains why you were right. You set it aside. The second asks what it would cost to speak and admits that she may choose not to name a price.
You keep the first draft beside it. If she answers, you will still have to account for the reasons you have not renounced. It would be a poor beginning to offer her a repentance made only of omitted sentences.
You leave the center empty. No red eyes appear there. No remembered voice praises your restraint.
A real channel will need a sign you did not supply, and a way to distinguish its bearer from anybody who finds your request profitable. Until you can obtain those, the message stays in your hands.''',
             c('Keep the unsent request and seek an independently answered sign.', flags=f("postconflict_probe_prepared"))),
    ], requires=("trickster", "noct.acq.council_fight", *f("conflict_resolved_verified")),
    forbids=f("closed", "postconflict_probe_prepared"), optional=True,
    Relationship="nocticula.acquisition", Remote=True, ManualOnly=True, Areas=[DREZEN], Chapters=[5]))


def validate():
    """Check source contracts without claiming native acquisition or delivery."""
    ids = [s["Id"] for s in SCENES]
    assert len(ids) == len(set(ids))
    native = set(ETUDES) | set(COMPLETED_ETUDES) | set(SEEN_CUES) | set(SELECTED_ANSWERS)
    for s in SCENES:
        nodes = {node["Id"]: node for node in s["Nodes"]}
        assert len(nodes) == len(s["Nodes"])
        reached, active = set(), set()
        def visit(key):
            assert key not in active, (s["Id"], key)
            if key in reached:
                return
            active.add(key)
            for choice in nodes[key]["Choices"]:
                assert not (set(choice["Set"]) & native)
                assert all(flag.startswith("noct.acq.") for flag in choice["Set"])
                check = choice.get("Check")
                assert not check or (not choice.get("Next") and not choice.get("Abort"))
                for target in ((check["Success"], check["Failure"]) if check else (choice.get("Next"),)):
                    if target:
                        assert target in nodes
                        visit(target)
            active.remove(key)
            reached.add(key)
        visit(s["Nodes"][0]["Id"])
        assert reached == set(nodes)
    return {"scenes": len(SCENES), "nodes": sum(len(s["Nodes"]) for s in SCENES), "status": CONTRACT["status"]}


def allowed(item, flags):
    return (set(item.get("Requires", ())) <= flags
            and not set(item.get("Forbids", ())) & flags
            and all(set(group) & flags for group in item.get("RequiresAnyGroups", ())))


def validate_paths():
    """Exercise finite contact outcomes and native-history boundaries locally."""
    def outcomes(current, initial):
        nodes = {node["Id"]: node for node in current["Nodes"]}
        def walk(key, flags, visited):
            assert key not in visited
            choices = [choice for choice in nodes[key]["Choices"] if allowed(choice, flags)]
            assert choices, (current["Id"], key, "dead end")
            for choice in choices:
                if choice["Abort"]:
                    continue
                updated = flags | set(choice["Set"])
                check = choice.get("Check")
                targets = (check["Success"], check["Failure"]) if check else (choice.get("Next"),)
                for target in targets:
                    if target:
                        yield from walk(target, updated, visited | {key})
                    else:
                        yield updated
        return walk(current["Nodes"][0]["Id"], set(initial), set())

    base = {"trickster", "noct.acq.audience_question"}
    fixtures = (
        base, base | {"noct.gift"}, base | {"noct.parent_rejected"},
        base | {"noct.parent_rejected", "noct.gift"},
        base | {"noct.parent_active", "noct.acq.original_gift_completed"},
        base | {"noct.parent_active", "noct.acq.original_gift_completed", "noct.acq.gift_renewed"},
    )
    complete = 0
    for flags in fixtures:
        entries = [s for s in SCENES[:3] if allowed(s, flags)]
        assert len(entries) == 1
        kinds = set()
        for requested in outcomes(entries[0], flags):
            assert not allowed(SCENES[3], requested)
            if "noct.acq.closed" in requested:
                continue
            earned = requested | {"noct.acq.council_disclosed", "noct.socoth_plan_exposed"}
            assert allowed(SCENES[3], earned)
            for sent in outcomes(SCENES[3], earned):
                assert allowed(SCENES[4], sent)
                for final in outcomes(SCENES[4], sent):
                    if "noct.acq.closed" in final:
                        assert "noct.acq.correspondence_trial" not in final
                        continue
                    assert "noct.acq.correspondence_trial" in final
                    assert ("noct.acq.channel_provisional" in final) != ("noct.acq.channel_letters_only" in final)
                    if "noct.acq.channel_exposed" in final:
                        assert set(f("sketch_surrendered", "channel_repaired")) <= final
                        kinds.add("repaired")
                    else:
                        kinds.add("narrow" if "noct.acq.channel_provisional" in final else "letters")
                    complete += 1
        assert kinds == {"narrow", "letters", "repaired"}
    for blocked in (base | {"noct.parent_active", "noct.gift"}, base | {"noct.dead"},
                    base | {"noct.acq.council_fight"}, base - {"trickster"}):
        assert not any(allowed(s, blocked) for s in SCENES[:3])
    assert not allowed(SCENES[-1], base | {"noct.dead", "noct.acq.council_fight"})
    writes = {flag for s in SCENES for node in s["Nodes"] for choice in node["Choices"] for flag in choice["Set"]}
    assert not writes & {"noct.acq.conflict_resolved_verified", "noct.acq.postconflict_reply_verified", "noct.renewed_agreement", "noct.complete"}
    return {"fixture_histories": len(fixtures), "completed_trial_outcomes": complete}


if __name__ == "__main__":
    import json
    print(json.dumps({**validate(), **validate_paths()}, indent=2))
