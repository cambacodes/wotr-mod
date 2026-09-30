"""Unregistered authored bridge to a future history-aware harbor variant.

The hosted dream and named political limits are authored developments, not native
Gift effects or a completed Worldwound bargain. Existing harbor exports remain
untouched and cannot consume this draft without the separately documented edits.
"""
from story_format import c, n, scene
from storylines.nocticula_trickster_acquisition import DREZEN, allowed


def f(*names):
    return tuple("noct.join." + name for name in names)


def p(key, speaker, text, *choices):
    return n(key, speaker, text, *choices, portrait="Nocticula")


SCENES = []


def add(key, title, prior, nodes):
    SCENES.append(scene("noct.join." + key, title, "Memory", 5, title, nodes,
        requires=("trickster", "noct.acq.renewed_agreement", "noct.acq.an_answer_of_her_own_done", *prior),
        forbids=("noct.dead", "noct.acq.council_fight", "noct.acq.closed", "noct.closed", *f("closed", key + "_done")),
        delay=24, optional=True, Remote=True, Relationship="nocticula.acquisition",
        Areas=[DREZEN], Chapters=[5]))


add("an_unfinished_map", "The coast beyond the letter", (), [
    p("start", "Narrator", '''{n}Nocticula sends a drawing of a coastline with the water omitted. You recognize the deliberate blank: she wants you to notice what she has chosen not to supply.
Across the margin she has written, "There are people making money from this. I am not among them."
You write that it must be a very unusual coast.
"An intolerable one. I am considering whether to show you why."
The drawing changes beneath her answering stroke. A row of mooring posts appears, then stops before reaching the edge. She has supplied enough to make you want the rest. You set the sheet beside the reports you meant to finish.{/n}
"You will ruin an evening's work with half a harbor."
"Then I shall save the other half for an occasion when you are less vulnerable."
{n}Her next line asks whether you would consider meeting somewhere she can show you the problem without describing every rope. You remind her that the agreement concerned letters and chosen invitations.{/n}
"I remember. I am making one."''',
      c('Before accepting a different sort of meeting, name the promises that actually exist between you.', "history"),
      c('Keep the correspondence as it is. Decline dream meetings and the harbor proposal.', "letters", flags=f("closed", "letters_retained"))),
    p("history", "Nocticula", '''"I had expected a question about the harbor. You have chosen the more awkward shore."
{n}She waits for your answer. No unfinished sentence appears to help you give it.{/n}''',
      c('We never made the earlier personal bargain. There is nothing here to resume except the correspondence we chose.', "missed", forbids=("noct.parent_active", "noct.parent_rejected")),
      c('I refused your earlier offer. These letters did not turn that refusal into an acceptance.', "rejected", requires=("noct.parent_rejected",)),
      c('Our earlier agreement exists. A new means of meeting must not conceal what still stands between us.', "prior", requires=("noct.parent_active",), forbids=("noct.parent_rejected",))),
    p("missed", "Nocticula", '''"You are determined not to receive anything by accident."
"I have seen what happens to people who accept the favorable half of a story and let somebody else write the price."
"You have also seen what happens to people who make every conversation begin with their cleverness. Shall we risk a different opening?"
You tell her you want to see her, and that you will still ask the inconvenient question when she is there.
"Better. I was beginning to think you wanted an exceptionally well-annotated absence."
She draws a small mark beside the empty water. It is not a signature.
"I have offered you no accommodation and no solution to the Worldwound. Keep those spaces empty until we actually discuss them."''', c('Ask what the larger disagreement means for a smaller undertaking.', "politics", flags=f("history_new"))),
    p("rejected", "Nocticula", '''"I remember what you refused. You need not make a monument of it on every available page."
"Would you prefer I let you describe this as reconsideration?"
"I would prefer you discover an answer worth the trouble of hearing twice."
You put a line beneath your original sentence. It stays legible. Beneath it you write that you accepted her company, and will consider work worth doing together, without accepting an offer merely because she has repeated it attractively.
"A useful distinction," she answers. "I shall enjoy watching you maintain it when the work and the company want different answers."
The empty coast acquires one sharp rock. You ask whether it represents you.
"Do not be vain. There is room for several."''', c('Keep the refusal in history and discuss the new proposal.', "politics", flags=f("history_refused"))),
    p("prior", "Nocticula", '''"You recall that an interrupted convenience is not a canceled obligation. How refreshing."
"I recall that we can disagree about what was convenient."
"Frequently. You possess an unfortunate gift for finding reasons to dislike a privilege after making use of it."
You ask whether this harbor is another installment of the older price.
"No. If I ask you for something concerning the Worldwound, I will not disguise it as a discussion of ropes. You are perfectly capable of disappointing me in more than one matter. I prefer to know which we are discussing."
You leave the earlier terms written in your own account. She neither tears them out nor offers to forget them for the pleasure of another evening.''', c('Preserve the existing terms and ask about the separate harbor work.', "politics", flags=f("history_prior"))),
    p("politics", "Commander", '''You ask what she expects when your ambitions reach beyond a private trade route.
"I expect you to remember that my city is not a convenient collection of pieces for you to rearrange."
"I could say the same of my world."
"You should. Then explain what you intend to do with it."
You have no map complete enough to make every consequence obedient. You can name the direction in which you mean to work. Nocticula will hear that before she shows you another shore.''',
      c('[Good] I intend to end the danger of the Worldwound. That does not make every life near it a price you may collect.', "closure", flags=f("closure_intent")),
      c('[Trickster] I may want a crossroads which serves my world. You would need a reason to prefer it to an invasion at your gates.', "crossroads", flags=f("crossroads_proposed")),
      c('[Evil] I will seek the outcome that leaves me strongest. Tell me what you would actually pay to make your preferred answer mine.', "power", flags=f("power_declared"))),
    p("closure", "Nocticula", '''"Every commander learns to call the people he spends a necessity. You wish to reserve the arithmetic for yourself."
"I wish you to hear an objection before you count it as permission."
"Then make it specific when the occasion comes. I have little patience for men who bring me a principle instead of an answer and expect the principle to finish their work."
She does not offer a new Worldwound contract. She acknowledges that you have named an intention she can work with, and a limit she may contest.
"For the harbor, you may ask what happened to the passengers. I shall ask what made the passage valuable. Try to provide answers useful to both questions."''', c('Accept that common work does not settle every disputed price.', "gift")),
    p("crossroads", "Nocticula", '''"A crossroads. How charmingly you describe an open approach to somebody else's throat."
"A road can be closed to an army."
"By whom? For how long? And what happens when the person at the gate discovers that an army can pay?"
You begin to answer. She stops you at the first assumption you cannot support. The silence afterward is not an invitation to make the assumption more eloquent.
"I have not agreed to that outcome," she writes. "Do not put my name on it. Do not use my mark to invite an ally to a road whose existence you have not proved you can control."
You concede that limit. You will not trade her supposed endorsement while asking her to examine the danger.
"There is the first useful thing your crossroads has produced. An invitation you have promised not to sell. We can discuss an actual harbor while your larger ambition learns some dimensions."''', c('Withhold her endorsement and keep the crossroads proposal unresolved.', "gift", flags=f("endorsement_withheld"))),
    p("power", "Nocticula", '''"You have confused naming your appetite with demonstrating your price."
"I thought you disliked modesty performed for an audience."
"I dislike bad performances. You have yet to tell me what power you would relinquish for mine."
You answer that you will not grant another party authority to speak for her while negotiating with her yourself. If she offers something worth the loss, you will discuss the larger sacrifice then.
"A restraint upon your own intermediaries. Small, but intelligible. I accept that as a limit on this conversation, not as payment for the Worldwound."
She draws a narrow line across the coast.
"Show me what you do with one profitable route before you ask me to value your ownership of every road."''', c('Keep her name out of other bargains and leave the larger price unagreed.', "gift", flags=f("endorsement_withheld"))),
    p("gift", "Nocticula", '''"There is also the question of how you propose to meet me. Do you intend to let an old source of power supply an answer you have not given?"''',
      c('Your renewed gift is present. It is not permission for this new meeting.', "gift_present", requires=("noct.acq.gift_renewed",)),
      c('Your original gift remains. I will still choose whether to receive this invitation.', "gift_present", requires=("noct.gift",), forbids=("noct.acq.gift_renewed",)),
      c('No current gift supplies the passage. I want to know what you are offering to do instead.', "gift_absent", forbids=("noct.gift", "noct.acq.gift_renewed"))),
    p("gift_present", "Nocticula", '''"I could simply take the evening; the gift would let me. Where is the pleasure in that? I would rather watch you walk in on your own feet, knowing exactly what I am."
"And I am capable of wanting you while objecting to the means of obtaining me."
"Then we have something to discuss when you arrive. I should hate to exhaust the conversation before making a room for it."
She offers to host a single meeting through her side of the responding mark. You will name the hour and receive an invitation before sleep. She wants your answer; she could have the evening without it, and you both know it.''', c('Propose the following evening for one trial meeting.', flags=f("an_unfinished_map_done", "trial_offered"))),
    p("gift_absent", "Nocticula", '''"My side of the mark. I will make the place and send the invitation. You will provide the inconvenient guest."
"You could have proposed that before."
"I could have proposed a great many things before deciding whether your company justified them. You should enjoy being expensive enough to require a decision."
She will prepare a single meeting, not repair the old aperture or supply a blessing under another name. You will have to stay within the place she makes rather than use it as a road into Alushinyrra.
"If you want a palace door," she adds, "ask for one. I would prefer to refuse the actual ambition."''', c('Propose the following evening for one trial meeting.', flags=f("an_unfinished_map_done", "trial_offered"))),
    p("letters", "Nocticula", '''"Then keep the coast unfinished. It appears you prefer me at a distance which fits on a desk."
"I prefer the agreement I made."
"For now. Send me something worth reading within it."
She takes back the drawing. The answering stroke remains on the wax. You have declined a larger meeting, not invented an acceptance by continuing to write.''', c('Keep the personal correspondence without entering the harbor work.')),
])


add("the_room_she_makes", "The room she makes", f("trial_offered", "an_unfinished_map_done"), [
    p("start", "Narrator", '''{n}At the chosen hour, a second stroke appears beside the old answering line. It describes a closed shape without crossing the split in your half of the wax.
Nocticula tells you to keep the old fold flat. You are not to enlarge it, mend it or repeat the construction which once promised a view through its edge. She has placed an invitation on her side, and is waiting for your answer.
You sit where the lamp illuminates your own hand. Beyond the window, a sentry strikes the last watch upon a rail. You count the blows before writing.{/n}''',
      c('The narrow fold is still mine to leave closed. Use only the invitation you have just made.', "prepare", requires=("noct.acq.channel_provisional",), forbids=("noct.acq.channel_letters_only",)),
      c('My ordinary letters remain closed. I am considering this separate hosted invitation.', "prepare", requires=("noct.acq.channel_letters_only",), forbids=("noct.acq.channel_exposed",)),
      c('The exposed aperture stays broken, and you keep its sketch. Do not mistake this for permission to restore it.', "exposure", requires=("noct.acq.channel_letters_only", "noct.acq.channel_exposed", "noct.acq.channel_repaired", "noct.acq.sketch_surrendered"))),
    p("exposure", "Nocticula", '''"I remember the sketch. It has not improved while in my possession."
"You have been looking at it?"
"You gave me an error with an attractive idea inside it. Did you expect me to preserve only the error?"
She keeps what you surrendered. The admission costs her nothing, and gives you a reason to remember that she does not stop being curious because you would prefer your mistake forgotten.
The new stroke has no branching path to test. It answers from her side of the mark, and will vanish when she withdraws it.
"You may refuse this as well," she writes. "I have not offered to make your former discretion look foolish."''', c('Keep the old exposure and surrendered sketch distinct from the invitation.', "prepare")),
    p("prepare", "Nocticula", '''"Write where you mean to wake."
You name your room in Drezen, the chair, and the lamp with a chipped blue foot. She asks for something the dream should not need to contain. You choose the sentry's watch signal.
"When you wish to leave, remember that sound. I will end the room when you ask. I should like you to know that I can keep you there, and that I choose not to. We will test it before we discuss anything else."
"You are promising to let me leave."
"Yes. Not to become incapable of mistreating you. If you wanted a harmless hostess, you chose badly."
You examine the words. The risk has a name and has not become smaller because she wrote it beautifully.
She has asked for one trial evening. Even a pleasant result will require a separate answer before future sleep becomes an invitation.''',
      c('Accept one trial meeting. Keep the lamp and the watch signal in mind.', "arrival", flags=f("trial_accepted")),
      c('Decline the trial. Keep the letters and give her no permission to enter your sleep.', "refuse", flags=f("closed", "letters_retained"))),
    p("arrival", "Narrator", '''{n}You leave the sheet beneath the lamp and close your eyes. Sleep brings a stone landing no larger than your room, with an open arch at one end. Beyond it hangs a red evening sky. There is no city beneath the sky, and no ground upon which to place one.
Nocticula stands beside the arch. The light follows the edges of her wings, then loses itself in their shadow. She looks at your boots before meeting your eyes.{/n}
"You brought those."
"I was uncertain about the floor."
"Practical. Disappointing, but practical."
{n}You can see the familiar ease with which she lets a silence become someone else's difficulty. Her attention is less comfortable than her handwriting. It also makes the absurdly small landing seem worth the wait.
You tell her so. She inclines her head, accepting the compliment without offering another in exchange.{/n}
"The sound," she says. "Before you decide the view has answered that question for you."''', c('Ask to wake and remember the sentry striking the rail.', "waking")),
    p("waking", "Narrator", '''{n}You hear one remembered blow. The arch loses its red light, and your chair presses against the back of your legs. The lamp is still burning. Nocticula's next words arrive on the sheet beneath it.{/n}
"You left a remarkably promising evening."
"You asked me to test the exit."
"I have never claimed to enjoy every successful instruction."
{n}You can put the wax away now. The new stroke is fading. She has ended the hosted place when asked; the room was not an entrance into her city, and waking has left no coast beneath your desk.
She asks whether you would like another evening in which the first subject is not your departure.{/n}''',
      c('Yes. Let us discuss a continuing invitation after both of us have had time to consider it.', flags=f("the_room_she_makes_done", "exit_demonstrated")),
      c('No. Keep the letters. I do not want further dream meetings.', flags=f("the_room_she_makes_done", "exit_demonstrated", "closed", "letters_retained"))),
    p("refuse", "Nocticula", '''"Then stay by your lamp."
The second stroke disappears. The old answering mark remains.
You ask whether she intends to withdraw her correspondence as well.
"Did you ask me to?"
"No."
"Then try not to refuse an evening and spend the rest of it demanding compensation for an offense I have not committed. Tell me what you meant to write before I drew the coast."
You turn to a clean page. Nothing asks you to sleep.''', c('Continue the existing correspondence.')),
])


add("a_chosen_shore", "A shore chosen twice", f("the_room_she_makes_done", "exit_demonstrated"), [
    p("start", "Narrator", '''{n}The letter waiting the following evening contains no picture. Nocticula asks what you remember.
You name the red sky and the absence of any city beneath it. Then the way she inspected your boots.
"You may blame the shoes for your disappointment," you write. "I will remember who invited them."
Her answer arrives before you can decide whether the sentence was wise.
"I invited their owner. There are matters upon which even I must accept an imperfect delivery."
You put the letter down, laughing. When you pick it up again she has added a question about the choice you made before the trial.{/n}''',
      c('I still intend to end the Worldwound\'s danger. The harbor will not buy your answer to every other question.', "closure", requires=f("closure_intent")),
      c('The crossroads is still a proposal. I have not sold your endorsement while waiting for this reply.', "unagreed", requires=f("crossroads_proposed", "endorsement_withheld")),
      c('I have kept your name out of other bargains. I still want to discover what makes this route valuable.', "unagreed", requires=f("power_declared", "endorsement_withheld"))),
    p("closure", "Nocticula", '''"Nor will your interest in the passengers purchase my indifference to what they found."
"I would find you less interesting if you were indifferent to a profitable mystery."
"Be careful. You are making it difficult for me to charge you for my patience."
She asks whether you want your first advice to concern the passengers' safety or the means of securing the passage. She has not offered enough of the case to make either answer a plan.
You tell her which question you intend to ask first. She will still decide what to reveal, and you will still have to hear the facts before proposing a solution.''', c('Choose the first question without pretending it settles the harbor.', "purpose")),
    p("unagreed", "Nocticula", '''"Good. I have declined far more impressive attempts to make an acquaintance sound like an alliance."
"You would dislike finding your name on something you had not examined."
"I would dislike finding it there unsuccessfully. Do not omit the more expensive possibility merely because you disapprove of it."
She has not endorsed a crossroads or named her price for your strongest possible future. You copy that answer beside the proposal, where neither of you can later describe the silence as agreement.
"The harbor," she writes. "Show me an ambition which can bear being questioned while it is still small enough to inspect."''', c('Choose what you would investigate first.', "purpose")),
    p("purpose", "Commander", '''You could begin by asking whom the trade leaves behind. You could begin by asking who is foolish enough to profit from a road under Nocticula's gaze without sharing it with her.
The two questions may lead to the same person. They will not flatter that person in the same way.
Nocticula has left space beneath her unfinished drawing. This time she means you to choose what belongs there.''',
      c('[Good] Begin with those who paid to travel and did not arrive. A route worth keeping must be worth surviving.', "people", flags=f("first_question_passengers")),
      c('[Evil] Begin with whoever collects the profit. If I help you find the road, I expect to discuss its value to me.', "profit", flags=f("first_question_profit"))),
    p("people", "Nocticula", '''"You have chosen the answer most likely to make me listen to an inconvenient witness."
"You have chosen the adviser most likely to find one."
"Yes. I am attempting to remember why I considered this an advantage."
She writes that she will retain the accounts of missing and returned travelers for the first discussion. She will not promise to regard every passenger as innocent, or every dangerous passage as something that ought to be destroyed.
You accept the distinction. She has agreed to bring the evidence, not to let your preferred conclusion sit in judgment before it arrives.''', c('Keep the request for the travelers\' accounts in the invitation.', "invitation")),
    p("profit", "Nocticula", '''"You expect to be paid before discovering whether your advice is worth taking?"
"I expect to be heard before you decide that my only reward should be proximity to you."
"An ambitious complaint from a man who requested precisely that."
You admit the difficulty. It does not make the two questions identical.
She agrees to discuss a specific return for a useful result when you know what the route can do. She promises neither ownership nor a share merely for appearing.
"Bring the appetite," she writes. "We shall see whether it develops manners when the thing it wants belongs to somebody who can refuse it."''', c('Keep payment open for an actual result rather than an invented entitlement.', "invitation")),
    p("invitation", "Nocticula", '''"Then I will show you the quay."
You ask whether she is offering further hosted meetings through the same mark.
"When you choose to sleep with the answering sheet beside you. Put it away when you want a night of your own. In the room, you may ask to leave as you did before. I will hear the answer even when I dislike its timing."
You will keep the old correspondence as well. She does not ask about your other lovers. She has never needed to ask about anything she could find out for herself.
"And if I decline the harbor after hearing the case?"
"Then I shall have spent an evening arranging a particularly elaborate disappointment. I do not recommend making a habit of it."
"That was almost an answer."
"You may decline the undertaking. I may remain annoyed. Your letters will have to become better company."
She has left you the clean final space again. No new stroke appears inside it.''',
      c('Accept recurring hosted invitations on those terms. Hear the harbor proposal before deciding whether to undertake it.', "yes", flags=f("recurring_dreams_accepted", "harbor_variant_ready")),
      c('Keep the letters and decline further dream invitations or harbor work.', "no", flags=f("closed", "letters_retained"))),
    p("yes", "Nocticula", '''"Wear whatever boots you believe the mystery deserves."
You ask whether there will be water this time.
"You have not yet seen the problem. Do not begin improving it."
The coast returns beneath her signature. She has finished one more mooring post. You could count the spaces left for the others, but instead you turn the sheet so its blank water faces the lamp.
You want to see what she makes of it. You also want to see her notice that you have returned.
For once you do not supply a more respectable reason.''', c('Keep the accepted invitation to hear a new undertaking.', flags=f("a_chosen_shore_done"))),
    p("no", "Nocticula", '''"Then the coast remains my concern."
She folds the drawing through the answering mark until only your own words remain. Beneath them she asks whether your missing broker has yet become foolish enough to use his old name.
You consult the latest report. The correspondence continues within the narrower choice you made.''', c('Keep the private correspondence without accepting the larger invitation.', flags=f("a_chosen_shore_done"))),
])


def validate():
    """Walk the draft's supported histories; do not simulate native acquisition."""
    import runpy
    from pathlib import Path
    from storylines.nocticula_trickster_concession import outcomes
    words = runpy.run_path(str(Path(__file__).resolve().parents[1] / "tools/measure-story-content.py"))["words"]
    from storylines import nocticula_trickster_acquisition as opening
    native = set(opening.ETUDES) | set(opening.COMPLETED_ETUDES) | set(opening.SEEN_CUES) | set(opening.SELECTED_ANSWERS)
    assert len({s["Id"] for s in SCENES}) == len(SCENES)
    for s in SCENES:
        nodes = {n["Id"]: n for n in s["Nodes"]}
        assert len(nodes) == len(s["Nodes"])
        seen = set()
        def visit(key, stack):
            assert key not in stack
            if key in seen:
                return
            seen.add(key)
            for choice in nodes[key]["Choices"]:
                assert all(flag.startswith("noct.join.") for flag in choice["Set"])
                assert not set(choice["Set"]) & native
                assert not choice.get("Check")
                if choice.get("Next"):
                    assert choice["Next"] in nodes
                    visit(choice["Next"], stack | {key})
        visit(s["Nodes"][0]["Id"], set())
        assert seen == set(nodes)
    histories = {"missed": set(), "rejected": {"noct.parent_rejected"}, "prior_lost": {"noct.parent_active", "noct.acq.original_gift_completed"}}
    gifts = {"none": set(), "original": {"noct.gift"}, "renewed": {"noct.acq.gift_renewed"}}
    channels = {"narrow": {"noct.acq.channel_provisional"}, "letters": {"noct.acq.channel_letters_only"}, "exposed": {"noct.acq.channel_letters_only", "noct.acq.channel_exposed", "noct.acq.channel_repaired", "noct.acq.sketch_surrendered"}}
    bounds = {}; closed = 0
    for hn, history in histories.items():
        for gn, gift in gifts.items():
            # Original Gift still playing is not the completed-original patronage fixture.
            if hn == "prior_lost" and gn == "original":
                continue
            for cn, channel in channels.items():
                base = {"trickster", "noct.acq.renewed_agreement", "noct.acq.an_answer_of_her_own_done", *history, *gift, *channel}
                assert allowed(SCENES[0], base)
                for blocked in ("noct.dead", "noct.acq.council_fight", "noct.acq.closed", "noct.closed"):
                    assert not allowed(SCENES[0], base | {blocked})
                assert not allowed(SCENES[0], base - {"noct.acq.renewed_agreement"})
                states = [(base, 0)]
                for s in SCENES:
                    next_states = []
                    for state, count in states:
                        assert allowed(s, state)
                        for updated, extra in outcomes(s, state, words):
                            if "noct.join.closed" in updated:
                                closed += 1
                                assert "noct.join.harbor_variant_ready" not in updated
                                assert "noct.acq.closed" not in updated
                                assert not any(allowed(later, updated) for later in SCENES)
                            else:
                                next_states.append((updated, count + extra))
                    states = next_states
                for state, count in states:
                    assert set(f("trial_accepted", "exit_demonstrated", "recurring_dreams_accepted", "harbor_variant_ready", "a_chosen_shore_done")) <= state
                    assert len(set(f("closure_intent", "crossroads_proposed", "power_declared")) & state) == 1
                    assert len(set(f("first_question_passengers", "first_question_profit")) & state) == 1
                    assert state & native == base & native
                    if state & set(f("crossroads_proposed", "power_declared")):
                        assert "noct.join.endorsement_withheld" in state
                bounds[hn + "/" + gn + "/" + cn] = dict(minimum=min(v for _, v in states), maximum=max(v for _, v in states), completed_paths=len(states))
    return dict(scenes=len(SCENES), nodes=sum(len(s["Nodes"]) for s in SCENES), fixtures=len(bounds),
                completed_paths=sum(v["completed_paths"] for v in bounds.values()), closure_paths=closed,
                minimum=min(v["minimum"] for v in bounds.values()), maximum=max(v["maximum"] for v in bounds.values()),
                selected_bridge_words=bounds, status="author draft; unregistered; existing harbor gates and prose unchanged")


if __name__ == "__main__":
    import hashlib
    import json
    from pathlib import Path
    result = validate()
    result["sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()
    print(json.dumps(result, indent=2))
