"""Post-finale path-specific contact branches for Targona's missed romance."""
from story_format import c, n, scene


RELATIONSHIP = dict(
    Title="A choice made again",
    Description="Targona's old answer stands. A new correspondence gives her room to decide whether she wants something more.",
    Objective="Answer Targona's letters and let her decide what follows",
    Guidance="After Targona's completed RanRomance finale and nonromantic ending; path-specific access requires verified survival and contact.",
    StartedFlag="targona.trickster_acq.started",
    ClosedFlag="targona.trickster_acq.closed",
    CommittedFlag="targona.trickster_acq.courtship",
    UnavailableFlags=["targona.dead_lab", "targona.dead_lair", "targona.condemned", "swarm"],
    FailureFlags=[],
)

ETUDES = {
    "targona.free": "720af1f72f413354db3f4d41f76d5af6",
    "targona.dead_lab": "3b8bd37108050a94b9be14e22501e090",
    "targona.dead_lair": "bc65b234df544a718afc4856eb7f33fc",
    "targona.condemned": "1aaee57d670b0494e9d8662bffbf4f6a",
    "targona.ran_none": "4774e38b267c47f2b5f6c0975ec486f0",
    "targona.ran_angel": "e1837a6b241f4095a4312e0115988721",
    "targona.ran_azata": "2660c0d29eaf4dce9de52b3994462df1",
    "targona.ran_aeon": "383cc2c9ea3f47c4a71982cb06535118",
    "targona.ran_trickster": "64e2b82829694b8fac652ea06f4dc8a7",
    "targona.ran_romance": "80cb9c6f466b4eaaaa9561ca56c5f348",
    "targona.ran_lich": "480fead956f24022930a83d4457a377c",
    "targona.ran_demon": "6ba14669a2a74dfbb308f66fecda8f6e",
    "targona.ran_devil": "df70df5cb6824ff5a9776a2478eee6c6",
    "targona.ran_legend": "94bc04d1ed474feaab54af2f77a94574",
    "targona.ran_dragon": "ecdddd77ad964561b38ad1848cb4553f",
    "targona.ran_late_change": "2edcb6e5a1c3439fa9b9e0b3b96a49fb",
}
COMPLETED_QUESTS = {"targona.ran_treatment_completed": "6ec03ce2f763460c8ac89f4c2064c5ad"}
SEEN_CUES = {"targona.ran_nonromance_seen": [
    "ad655c40be31401386b85287483b3841",
    "cfc5f3cb2cf94672a96cab742e62225d",
]}

HISTORY = (
    "targona.ran_none", "targona.ran_angel", "targona.ran_azata", "targona.ran_aeon",
    "targona.ran_trickster", "targona.ran_demon", "targona.ran_lich", "targona.ran_devil",
    "targona.ran_legend", "targona.ran_dragon", "targona.ran_late_change",
)
PATH_FLAGS = {
    "Angel": "angel", "Azata": "azata", "Aeon": "aeon", "Trickster": "trickster",
    "Demon": "demon", "Lich": "lich", "Devil": "devil", "Legend": "legend",
    "GoldDragon": "dragon", "Swarm": "swarm",
}
PATH_ENTRY_PLANS = {
    "Angel": "Use the established treatment and service bond; ask her directly after the finale.",
    "Azata": "Use shared defense of the living and her protection of others; do not presume she joins the court.",
    "Aeon": "Use an evidence-led judgment of the treatment's consequences, with Anograt's voice treated separately.",
    "Trickster": "Use the bounded courier-marker contradiction in this module after her nonromantic parent ending.",
    "Demon": "Require a costly restraint or protection choice that she can reject; do not erase hostile treatment history.",
    "Lich": "Require a credible non-necromantic refuge and her informed consent; reject histories where she died or was transformed incompatibly.",
    "Devil": "Make terms explicit and revocable, then let her challenge the Commander's leverage; no infernal coercion as courtship.",
    "Legend": "Build a mortal future around the completed treatment and verified survival, not a false claim of restored wings.",
    "GoldDragon": "Use mutual guardianship and the verified post-Dragon body/future; source and actor gates remain unverified.",
    "Swarm": "Only a separately authored survivor/escape intervention could qualify; if her death or identity loss is terminal, refuse acquisition. Native survival and contact proof are absent.",
}
BLOCKED = (
    "targona.trickster_acq.closed", "targona.dead_lab", "targona.dead_lair", "targona.condemned",
    "targona.ran_romance", "swarm",
)


def add(id, title, nodes, previous=None, delay=24):
    for page in nodes:
        page["Portrait"] = "TargonaCorrespondence"
    SCENES.append(scene(
        "targona.trickster_acq." + id, title, "Targona", 5,
        "Read Targona's letter", nodes,
        requires=("trickster", "targona.free", "targona.ran_treatment_completed",
                 "targona.ran_nonromance_seen", "targona.correspondence_opened") + ((previous,) if previous else ()),
        forbids=BLOCKED, delay=delay, optional=True,
        Relationship="targona.trickster_acq", Remote=True, ManualOnly=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY),
    ))


SCENES = []
add("the_second_letter", "The second letter", [
    n("start", "Narrator", '''{n}The next personal packet contains a page in Targona's hand, folded around a copy of your reply. The earlier decision remains plain: you did not begin the RanRomance courtship, and neither this letter nor the old ending rewrites it.{/n}
"I am writing because a courier report reached my desk with two dates that do not agree. I could ask the clerk to copy it again, but I would rather hear how you read it. I do not need you to change your answer to anything you said before. I would rather know what you think when no one is trying to turn my life into a lesson.
"A message from the Order has reached me by the ordinary dispatch road. It describes a damaged signal marker near a waystation, but the account contradicts itself about whether the marker is still active. I can ask someone else to look. I am asking you because you notice when a report is arranged to make its reader hurry.
"Will you examine the contradiction with me? A refusal is an answer I can use."''',
      c("Agree to inspect the report, without promising what follows.", "report", flags=("targona.trickster_acq.started",)),
      c("Decline the errand and keep the letters friendly.", "decline", flags=("targona.trickster_acq.closed",))),
    n("report", "Narrator", '''{n}The courier's duplicate carries two different dates and the same seal. Targona has circled one line: the marker's bell was heard after the report says the post had been abandoned.{/n}
She writes that the contradiction matters because the marker once warned travelers away from unstable ground. No one can tell whether the bell was an echo, a deliberate signal, or a clerk's mistake. She will not send a patrol into danger on the strength of a joke, and she will not dismiss the possibility merely because the report is ridiculous.
Your Trickster senses an opening in the contradiction, but it is not permission to invent whatever ending would amuse you. The practical task comes first: compare the seal and dates, then decide whether a bounded intervention can make the signal legible without moving anyone or changing the marker's location.
"If your answer is that the evidence is insufficient, say so. I would prefer an honest uncertainty to a miracle with hidden terms."''',
      c("[Perception] Compare the seal, ink, and duplicate date before answering.", check=dict(Skill="SkillPerception", DC=22, Success="careful", Failure="uncertain", CommanderOnly=True)),
      c("Use the Trickster's wit to reconstruct the courier's route from the contradictory dates.", "route", requires=("trickster",)),
      c("Tell Targona the evidence is too thin to justify an intervention.", "decline_task")),
    n("careful", "Narrator", '''{n}The seal is genuine, but the second date was copied from the return docket rather than the outbound sheet. The bell may have sounded after the waystation was empty; that still leaves open whether anyone is stranded nearby.{/n}
Targona thanks you for separating what the paper proves from what it only suggests. She will send a local runner to inspect the safe approach and will not ask you to open a gate or summon a person. Before the runner leaves, she asks whether your strange talent can make a false signal impossible to mistake for a true one.
It is a narrow request. You can make the next bell ring only if the marker is touched from its own side. The trick cannot identify who touches it, cannot draw anyone toward it, and will expire after one test. If that condition fails, the whole attempt ends.''',
      c("Accept the bounded test and write down exactly what it can and cannot do.", flags=("targona.trickster_acq.intervention_ready",)),
      c("Refuse the magic and let the runner inspect the marker by daylight.", "ordinary")),
    n("route", "Narrator", '''{n}The two dates map to a courier's return loop. Your reconstruction finds the error without changing either record: the report was copied from the wrong side of a folded dispatch sheet.{/n}
Targona's reply is not praise for having bent reality. It is a practical question about the danger the error concealed. You answer that the marker may still be useful, but nothing in the copied pages proves anyone is near it.
She authorizes a daylight inspection by a local runner and asks you for a second, narrower favor. Can your Trickster power make the marker distinguish an actual touch from a report claiming a sound? No signal to a person, no pulled thread across distance, and no chance to send someone through a doorway. Just one test from the marker's own side.''',
      c("Accept the bounded test and write down exactly what it can and cannot do.", flags=("targona.trickster_acq.intervention_ready",)),
      c("Refuse the magic and let the runner inspect the marker by daylight.", "ordinary")),
    n("uncertain", "Narrator", '''{n}The handwriting is too consistent to prove either date false. The seal is intact, and the sound could have been carried from elsewhere. You tell Targona precisely that.{/n}
She does not punish caution by withdrawing the correspondence. Instead, she asks the runner to inspect from the safe road and leaves the marker alone until there is better evidence. The report remains a report, not a summons.
"That is not the answer I hoped for," she writes. "It is a useful one. I am glad you knew the difference."
You can stop here and let the runner handle the matter. Or, without claiming that either date is false, you can trace the courier's ordinary return loop and narrow down where the copy may have gone wrong. That second method is slower and does not make the evidence more certain, but it gives Targona another useful lead.''',
      c("Let the daylight runner finish the inspection and leave the question open.", "ordinary"),
      c("Trace the courier's route from the two dates, without calling either one false.", "route")),
    n("decline_task", "Narrator", '''{n}You tell Targona that the contradiction does not justify risking a person or a power on the marker. She replies that she agrees with the limit, even if she had hoped for a sharper answer.{/n}
"Thank you for treating the danger as real. I can ask the runner to look in daylight. The letters need not become a bargain for your help."''',
      c("Send a friendly reply and leave the route here.", flags=("targona.trickster_acq.closed",))),
    n("decline", "Narrator", '''{n}You decline the errand. Targona accepts the answer without asking you to justify it.{/n}
"I am glad you answered plainly. The earlier decision remains yours, and the correspondence can stay what it is. I will ask the courier to take this as a friendly note, not an unfinished invitation."''',
      c("Keep the exchange friendly.", flags=("targona.trickster_acq.closed",))),
    n("ordinary", "Narrator", '''{n}The runner inspects the marker by daylight and confirms that no one is stranded. Targona's dispatch thanks you for declining an unnecessary risk.{/n}
The report's contradiction is corrected in the courier ledger. The marker is neither enchanted nor moved, and the runner returns by the same safe road. The correspondence continues without the Trickster intervention.''',
      c("Write back and continue as friends.", flags=("targona.trickster_acq.friendship",))),
], delay=24)

add("a_measured_impossibility", "A measured impossibility", [
    n("start", "Narrator", '''{n}You describe the Trickster intervention as a rule with edges. For one test, the marker's bell will sound only if someone touches the marker itself. It will not answer a voice, point toward a person, alter the ground, or carry anyone. If the effect becomes ambiguous, you will end it.{/n}
Targona sends the runner's safe approach and asks for the written terms before you begin. The test happens at the marker, under ordinary daylight, with the runner standing far enough away to leave the area at once. This is a newly authored side errand attached to Targona's established concern for warning others; it is not a recovered base-game quest.
The impossible part is brief. The bell rings once when the runner touches the marker, and remains silent when he repeats the sound from the road. The marker stays where it was. The runner returns by the same safe path.
Targona reads your account twice. "You made the absurdity answer one question. You did not ask it to answer the question you wanted."''',
      c("Tell her the boundary mattered more than the result.", "boundary"),
      c("Joke that fate behaved because it recognized your handwriting.", "wit"),
      c("Ask whether the runner found anyone in danger.", "result")),
    n("boundary", "Narrator", '''{n}Targona's answer comes by the next courier, with a note that the runner found no one stranded and the marker can now be repaired without guessing at its condition.{/n}
"I am glad the test had a limit you were willing to obey. Power is easiest to trust when the person holding it can say where it stops. I do not mean that as a compliment you must earn again. It is simply what I observed."
She asks if you will tell her how you chose the boundary. You explain that a trick meant to help should not demand that the person helped surrender control. She replies that this distinction is familiar to her, though it has not always been honored around her.
There is no request to turn the moment into a confession. She leaves a clean space at the bottom of the page for whatever you choose to write.''',
      c("Answer as a friend, without asking for romance.", "friend"),
      c("Tell her the work mattered because it was hers to direct.", "trust")),
    n("wit", "Narrator", '''{n}Targona's reply begins with a dry note about fate's famously poor penmanship.{/n}
"Do not flatter yourself. The runner's notes were legible, which is more than I can say for your last report. Still, the joke did not make the danger disappear, and you did not pretend it had. I appreciate both facts."
She adds that the marker is being repaired and that the runner found no one in danger. Then, almost as an afterthought, she writes that she misses having a conversation where the other person can be clever without insisting cleverness is the same as being right.
The line is warmer than her earlier account, but she does not call it a promise. You can answer with the same care.''',
      c("Keep the reply friendly and leave the old answer untouched.", "friend"),
      c("Say that you are glad she wants to keep talking to you.", "trust")),
    n("result", "Narrator", '''{n}The runner found no one stranded. Targona is relieved, then visibly annoyed at herself for having hoped the report meant there was someone she could still help.{/n}
"I know that hope is not evidence. I know it does not make me foolish to have felt it. Both things can be true." You agree. You do not manufacture a rescue to reward her concern.
She writes that your restraint made it easier to read the result. The repair crew can now replace the marker at the safe approach. What remains is a small, completed task and the knowledge that you could have made a more dramatic story, but chose not to.''',
      c("Tell her the honest result is enough.", "boundary")),
    n("friend", "Narrator", '''{n}You write that you are glad she asked, and that you do not expect the errand to revise the old RanRomance ending. Targona's answer is immediate and unmistakable.{/n}
"Good. I would not want to discover that helping me had become a clever way to argue against an answer I already gave. Keep writing to me if you want to. I will keep answering while I want to."
The courier carries the note with the next ordinary packet. Its route, delay, and seal are mundane. No Trickster power is needed to preserve a friendship she freely chooses.''',
      c("Reply with an ordinary detail from the citadel.", flags=("targona.trickster_acq.friendship",))),
    n("trust", "Narrator", '''{n}Your letter says that the task mattered because Targona set its terms, could stop it, and could judge the result without owing you a kinder interpretation.{/n}
Her reply takes longer. She says she has thought about the difference between the person who helped her and the person she first met. She does not say that the first no was mistaken. She says that she has changed, you have changed, and the old choice belonged to the two people you were then.
"I am not asking you to be less careful," she writes. "I am asking if you would like to meet me at the next safe courier stop, in public, with no spell and no expectation that I will stay. I would like to see the person who made that boundary. If you say no, the letters remain letters."''',
      c("Accept her invitation and let the public meeting be its own answer.", "accept", flags=("targona.trickster_acq.invited", "targona.path.trickster.meeting_pending")),
      c("Decline the meeting, while welcoming further letters.", "decline_meeting", flags=("targona.trickster_acq.friendship",))),
    n("decline_meeting", "Narrator", '''{n}You tell Targona you would rather keep writing. She accepts without turning the invitation into a test.{/n}
"Then we will keep writing. I am glad I asked, and I am glad you could answer honestly. The old ending stays what it was. This one stays what we choose now."''',
      c("Send an affectionate but friendly reply.", flags=("targona.trickster_acq.friendship",))),
    n("accept", "Narrator", '''{n}You accept the invitation without adding a condition. Targona names the safe courier stop and the hour, then sends a second note confirming that she can leave whenever she wishes.{/n}
She has initiated this meeting. It is a new choice, made after the parent ending and after a task in which you let her define the risk. It does not undo the earlier no, and it does not obligate her to begin a romance. The next scene can only be staged after integration verifies a real meeting location and actor availability.''',
      c("Keep the invitation and wait for a verified meeting scene.", flags=("targona.trickster_acq.started", "targona.trickster_acq.meeting_pending", "targona.path.trickster.meeting_pending"))),
], previous="targona.trickster_acq.intervention_ready", delay=48)


# These authored letters model character-appropriate recontact. Their exact
# flags still need native contact producers and independent runtime review.
PATH_FRAMES = {
    "Angel": ("Targona crosses out a line calling the delay a test of faith. She writes 'unknown ground' instead. Her changed wing remains part of her body, not a flaw for you to mend. She wants your judgment on the patrol route, not a sign from Heaven.", "The Angel's certainty cannot fill the gaps in the report. The marker failed, but no witness says why. Targona will not send a patrol beyond known safe ground just because the risk sounds righteous."),
    "Azata": ("Targona's letter has a rough road sketch and a sun she has crossed out. She welcomes humor, but not in place of a safe route. She asks if you can make room for joy without asking someone else to pay for the surprise.", "The map marks unstable ground. Targona can laugh with you, but will not confuse an adventure with a safe plan."),
    "Aeon": ("The dispatch, repair ledger, and patrol route arrive together. Targona writes: 'Records are not a verdict.' Anograt adds a note in a different hand, which she has kept separate from her own.", "The ledger proves the marker failed. It does not establish who damaged it, whether anyone remains nearby, or which repair would last."),
    "Demon": ("Targona's letter does not call your restraint kindness. She asks what you would do if no one praised you. She knows what your path can make of anger, but does not pretend that knowledge makes her safe beside you.", "The patrol needs protection, but Targona will not accept it at the price of someone else's fear. Her answer to you is not part of the payment."),
    "Lich": ("Targona writes: 'I am alive, and I am not asking you to preserve me.' She asks you to handle the patrol report without invoking death, undeath, or a promise that makes her body answer for your choices.", "The patrol needs a safe route, not a dead observer or restored memory. Targona would rather delay the repair than make someone an experiment."),
    "Devil": ("Targona's letter contains a list of terms, all crossed out. 'I do not want a contract for this,' she writes. 'I want to know if a promise can remain a promise without binding the person who asked.' Her freedom is not negotiable.", "An agreement protects the road only if its limits are explicit and revocable. Targona will not accept a guarantee whose penalty falls on the people she means to protect."),
    "Legend": ("Targona writes after your mythic power has left you. She does not call you ordinary. She asks you to read the patrol report as someone who must live with tomorrow's consequences, when neither title nor legend can walk that road for you.", "Reputation cannot repair a warning marker. Targona would rather wait for a trained crew than let a celebrated name stand in for knowledge."),
    "GoldDragon": ("Targona's page sketches a warning marker beneath a dragon silhouette. She crosses out the silhouette and leaves the marker. 'Protection is not the same as being seen to protect,' she writes. Her injured wing remains visible, neither cured nor hidden.", "A guardian's presence cannot prove the ground is stable. Targona wants a plan that remains safe after the great figure has left."),
}


PATH_MEETING = {
    "Trickster": ("The courier stop is a small public wayhouse, its common room busy enough to make privacy optional. Targona arrives without a guard and keeps her travel cloak on. She checks the door before she sits, a habit rather than a signal that she wants you to ask about it.", "You tell her the paper contradiction was interesting, but not the reason you accepted her invitation. You wanted the chance to see her when neither of you was recovering from a battle or answering a command. She studies your face, looking for the joke that might turn the sentence into a trick."),
    "Angel": ("The meeting is arranged at a public wayhouse on the ordinary road. Targona comes in travel clothes, the altered wing visible where the cloak falls open. She asks you not to turn the evening into a discussion about Heaven, forgiveness, or what her body means. She chose to come as a woman who wanted to see you.", "You answer that you did not come to ask whether she is healed enough to be desired. You wanted to meet the person who can disagree with an angel's interpretation of her own life and still make you feel watched when she holds your gaze."),
    "Azata": ("Targona arrives at the public wayhouse a few minutes early and claims she meant to inspect the road. A half-finished sketch of the marker is folded in her pocket. She asks if you can have an evening that does not need to become a memorable story for someone else.", "You say that you wanted to see her when neither of you had to turn danger into a joke. She laughs once, quietly, and admits she was hoping you would say something more personal than that the courier arrived on time."),
    "Aeon": ("Targona waits at a public wayhouse with the dispatch ledger closed beside her cup. She says Anograt's perspective remains hers to share, but it is not a substitute for Targona's answer. If Anograt wants to join any future evening, she will be asked separately and can refuse. Tonight's invitation belongs to Targona.", "You tell her that what drew you here was not a verdict or a contradiction. You wanted to know what she chooses when no record can tell either of you what the answer is supposed to be."),
    "Demon": ("Targona chose a public wayhouse with a clear road to the door. She does not hide that calculation. She also does not leave. Her wing is uncovered, her posture unbowed, and her attention follows your hands before it reaches your face.", "You say that you want her, but you will not use her fear of you as proof that she wants you back. Targona holds your gaze. She says the distinction matters, and asks whether you can still hear her if her answer makes you angry."),
    "Lich": ("Targona arrives in a public wayhouse, alive and unmistakably herself. She has asked that the evening involve no spell, preservation, promise against death, or discussion of what your power could do to her. She wants to find out whether you can desire a living woman without turning her into something you must keep.", "You tell her that you want to know the person who is here tonight, not a future body, an echo, or a proof that your path has not taken too much. Her shoulders ease slightly, though her eyes keep testing the words."),
    "Devil": ("Targona chooses a public wayhouse and pays for her own room. No contract, favor, or protection clause appears between you. She tells you this is a date only if both of you keep choosing it after every sentence that might change the terms.", "You admit you want her. You do not attach a condition, bargain, or promise that would make the desire difficult to refuse. She studies the empty table between you and says she wants to see if you can keep the space empty."),
    "Legend": ("Targona chooses a public wayhouse away from the citadel's reception rooms. She asks for no report about the famous Commander and offers no account of herself for a collection. The ordinary table and unremarkable hour are deliberate.", "You say that you wanted her company after the mythic power left, when neither reputation nor a miracle could answer a personal question for you. She asks whether the answer would survive an ordinary disagreement."),
    "GoldDragon": ("Targona chooses the public wayhouse and asks that you arrive in a shape that fits through its door without breaking the lintel. The joke is dry, and her eyes linger on your face after she says it. She wants the evening to belong to two people, not a guardian and a rescued angel.", "You say you want the woman across the table, including the wing she has chosen to keep and the judgment that comes with it. She asks if you can mean that without making her a symbol of your restraint."),
}

PATH_MEETING_MOMENTS = {
    "Trickster": ("Drop the joke and tell her why you wanted a night without a trick.", "Targona waits through the silence. You tell her that wit is easier than being seen, and you do not want to win her by making her laugh when you are afraid of what she might answer. Her smile arrives slowly. She says she had wondered whether the Commander knew how to leave the mask on the table."),
    "Angel": ("Ask her not to reassure you about Heaven or her wing.", "Targona looks relieved to have the subject named without being asked to forgive it. You tell her you will not use your faith as a cure or a verdict. She says she can be angry at what happened and still want the life she has now. She asks whether you can want her without needing to settle that contradiction."),
    "Azata": ("Ask if she wants to dance before the courier leaves.", "Targona laughs at the timing and says there is no music. You offer the rhythm of boots on a floor. She chooses a slow turn, then an abrupt change of direction that nearly makes you collide. She steadies you by the wrist, amused, and asks if you can enjoy a surprise that she chose."),
    "Aeon": ("Ask whether Anograt wants to add a thought in her own voice.", "Targona gives the invitation separately, without answering for her. Anograt's shadow lifts its hand. 'Silver wanted you to ask me, not solve what I meant before I could say it.' Targona smiles at the correction. Anograt does not join the date by default; she says she may want a separate conversation later and leaves the answer open."),
    "Demon": ("Set your weapon down and ask her to tell you if your temper enters the room.", "Targona studies the weapon before she studies you. She says she can be attracted to power and still refuse to be governed by it. You answer that she does not have to manage your anger for you. She touches the scarred hilt once, then meets your eyes and says she will remember that answer if you stop keeping it."),
    "Lich": ("Leave every spell uncast and offer to share an ordinary meal.", "Targona asks whether you can enjoy a mortal evening without weighing how long it will last. You say you can let the hour be real without making it permanent. She breaks bread and slides the larger piece to you, then takes it back with a grin when you accept too quickly."),
    "Devil": ("Ask her to choose one thing she wants from the evening, with no terms attached.", "Targona asks for honesty about attraction and no promise of forever. You agree without adding a penalty for either answer. She tests the space by telling you one thing she dislikes about your reputation. You let the criticism stand long enough for her to believe you heard it."),
    "Legend": ("Ask what she noticed when the mythic power left you.", "Targona says you looked smaller for a day, then more like yourself. You admit there are parts of the power you miss and parts you are relieved to set down. She answers with her own mixed feelings about the future, then lets the conversation turn toward what each of you wants tonight."),
    "GoldDragon": ("Ask if she wants you to change shape so you can share the table comfortably.", "Targona says the change must be your choice. You settle into a smaller form because you want to sit beside her, not because you think she could not love a dragon. Her gaze stays on your eyes. She says she likes seeing the person who makes the choice."),
}

PATH_SPAR = {
    "Trickster": "Targona chooses a practice bout after you tease that a courier's report is easier to disarm than its writer. She makes you repeat the joke while she checks the straps on her blunted sword.",
    "Angel": "Targona asks you to practice without treating her as a test of your virtue. She will call the bout herself and does not need an angelic lesson about mercy.",
    "Azata": "Targona suggests a bout after an unplanned detour makes you both late for the courier. She grins at the inconvenience, then reminds you that a surprise in the ring still needs a safe stop.",
    "Aeon": "Targona marks a circle in the dirt and defines its limits before she draws her practice blade. Anograt has supplied commentary from the margin, but Targona says the match belongs to her.",
    "Demon": "Targona proposes a controlled bout and names the stop word before either of you takes a stance. She wants to see whether your anger can remain yours when you are losing.",
    "Lich": "Targona asks for a bout with ordinary practice steel, no spells, summons, or resistance to injury. She needs the person in front of her to be the one who answers when she calls stop.",
    "Devil": "Targona proposes a bout with simple rules: no wager, no penalty, no advantage hidden in the wording. She wants to know whether you can accept terms that grant her no leverage over you.",
    "Legend": "Targona asks to spar after you describe how strange it feels to be a person after leaving the mythic path. She says a practice bout cannot tell either of you who you are, but it can show how you respond when you are outmatched.",
    "GoldDragon": "Targona asks you to meet her in a form that fits inside the practice yard. She does not want to train against a guardian large enough to end the bout by accident; tonight she wants a partner she can disarm.",
}

PATH_FUTURES = {
    "Trickster": "Targona asks what you intend to do when a relationship and a promise to rewrite fate pull in different directions. She wants a future that is chosen in ordinary moments, not one she has been told will happen because you made it possible.",
    "Angel": "Targona wants to decide for herself whether her service to Heaven or her life on Golarion comes next. She asks if your devotion can survive a future in which she has obligations that do not belong to you.",
    "Azata": "Targona wants to keep protecting people, but she does not want every quiet evening turned into another rescue. She asks you to plan space for rest without making rest a restriction.",
    "Aeon": "Targona and Anograt do not always want the same future. Targona asks you to treat their disagreement as real, rather than selecting whichever voice best supports your decision.",
    "Demon": "Targona wants to know whether the anger she finds compelling will be safe to stand beside when the crusade is over. She asks you to name a boundary you will respect even when you are furious.",
    "Lich": "Targona asks what future you can offer while she remains alive and mortal to harm. She will not be kept by a spell, turned into an experiment, or asked to approve a path by outliving it.",
    "Devil": "Targona wants to make plans without a contract, a penalty, or a protection clause that gives one of you authority over the other. She asks whether you can promise a date without trying to own the calendar.",
    "Legend": "Targona asks what you want now that power and prophecy no longer decide your itinerary. She has her own service and people she wants to see; a shared future has to fit two mortal lives.",
    "GoldDragon": "Targona wants a future in which she can guard people without becoming the companion who stands beneath your shadow. She asks how you will make room for her judgment when the two of you see danger differently.",
}

PATH_FOLLOWUPS = {
    "Trickster": (
        "A week later, Targona sends a dispatch with two versions of the same order. In one, she has agreed to let your power rewrite a failed evacuation so the missing wagon reached the safe road. In the other, she refused. Both are possible futures, but only one happened. She asks you to read the order she signed, not the one fate might have supplied. The surviving page records her refusal. The wagon was delayed, and the people aboard arrived alive after a harder road.",
        "She does not ask you to make the loss of time disappear. She asks whether you can stay beside her when the honest ending is slower and less clever.",
        "You leave the order unchanged. Targona folds it and keeps it as proof that your power can stand beside an answer it did not choose."
    ),
    "Angel": (
        "The next dispatch comes from an infirmary where two soldiers argue about whether Targona should be the one to tell a wounded scout that he cannot return to the field. She has already given the healer the facts. She asks you to come only as someone she trusts, not as Heaven's voice, the Commander, or a judge of what sacrifice ought to mean. The scout asks if she would still have chosen the same life after seeing what it cost.",
        "Targona will answer him herself. She asks you to stay close enough that she can find your hand, and far enough away that her words remain hers.",
        "She tells the scout that she would choose the life again, but not every injury or command that came with it. You let the answer stand without turning it into a sermon."
    ),
    "Azata": (
        "A celebration for the repaired marker spills into a wayhouse yard. Someone has painted a bright sun on the post, and the patrol captain wants it removed before the next inspection. Targona likes the harmless joke, but a traveler mistakes the paint for an official signal and starts down the wrong track. No one is hurt. The captain wants the whole party punished; the painter wants the sign kept. Targona asks you to help settle it without making joy itself the culprit.",
        "She is willing to defend the joke and admit its cost in the same breath. She wants you to do likewise.",
        "You help replace the paint with a clear warning and leave a smaller sun on the safe side, where it cannot be mistaken for an order. Targona laughs, then checks the marker herself."
    ),
    "Aeon": (
        "Anograt returns to the dispatch ledger with a correction in a hand that is not Targona's. The correction changes the official repair time by one day, but not the lived fact that the patrol chose to wait. Targona says the ledger should show both accounts. Anograt says a single record with two authors will be read as one voice. Targona looks to you, not to ask for a verdict, but to see whether you will collapse their disagreement into a neat answer.",
        "Anograt speaks for herself. Targona can answer for herself. Your task is to keep their words distinct even when a single version would be easier to publish.",
        "The archive keeps both accounts and identifies each hand. Neither woman has to adopt the other's wording to remain part of the same history."
    ),
    "Demon": (
        "A patrolman who once served under Targona refuses to take orders from a demon-blooded officer. He has not attacked anyone, but he is making the rest of the patrol choose sides. Targona wants the road kept safe and the man judged for what he does, not for the fear his face provokes. She asks you to speak with him while she watches. The question between you is not whether you can frighten him into silence. It is what you do when anger would make that easy.",
        "She will intervene if he threatens anyone. She will not ask you to conceal your temper, and she will not manage it for you.",
        "You remove the officer from the patrol until a fair hearing can happen. Targona approves the protection, not the force you could have used to obtain it."
    ),
    "Lich": (
        "A courier carries news that the patrol's old guide has died during the winter. The route is still safe, but the marker crew has lost the one person who remembered how the ground shifted after heavy rain. Your first thought is that a dead guide could answer questions no living scout knows. Targona sees the thought arrive before you speak. She asks you to help rebuild the route from living witnesses and weather marks, even if the answer takes longer.",
        "She knows what your power can offer. She wants to know what you choose when the dead could be useful and the living are tired.",
        "You send the crew back at daylight with two living guides. The repair waits. Targona shares the watch with you until the road is ready."
    ),
    "Devil": (
        "A local reeve offers to fund the marker's upkeep in return for a binding promise that no patrol will ever leave the road. The condition sounds safe until Targona points out that an emergency might make the road itself the danger. The reeve wants a signature today. She asks you to negotiate without turning her freedom or the patrol's safety into a clause you can enforce against them later.",
        "Targona is willing to promise what she can control. She will not promise that the world will never change or accept a penalty paid by someone else.",
        "You replace the absolute promise with a review date, a public record, and a right to withdraw if the ground changes. The reeve accepts. Targona keeps the page because its terms can end."
    ),
    "Legend": (
        "The marker crew's new recruit recognizes you from the crusade and assumes you can settle a dispute by reputation alone. Two workers disagree about where to place the replacement post. One remembers the flood line; the other has measured the current bank. Targona does not want your name used as a shortcut around the evidence. She asks you to carry tools, listen, and accept that neither worker needs to be impressed by a legend.",
        "The decision belongs to the people who will maintain the road after you leave. Targona wants to know if you can remain useful without being the answer.",
        "The crew places the marker where the measurements and the old flood line agree. You spend the afternoon helping them set it. No one asks you to make the work grand."
    ),
    "GoldDragon": (
        "A storm breaks the signal tower's upper brace. The repair crew can reach it only from the narrow platform, where a great dragon cannot fit. Targona has the relevant training but cannot safely brace the beam alone. You can change to a smaller form, but the crew still needs to trust the person giving directions rather than the shape above them. Targona asks whether you can share the work without turning the rescue into a display of guardianship.",
        "She will call each movement. You may lend your strength, but the repair is not yours to command.",
        "You take the lower brace in a form that fits the scaffold. Targona calls the lift, the crew secures the beam, and the tower stands because each person did the part they chose."
    ),
}


def add_meeting(path, lines):
    key = path.lower()
    opening, answer = lines
    personal_choice, personal_moment = PATH_MEETING_MOMENTS[path]
    nodes = [
        n("start", "Narrator", opening + "\nShe has chosen a public table and a clear way out. Before the first drink is finished, she asks what you wanted from this meeting. The letter said you would let it be its own answer. Now she wants to hear yours.",
          c("[Diplomacy] Listen for what she is asking beneath the composure.", "read", check=dict(Skill="SkillDiplomacy", DC=24, Success="read", Failure="misread", CommanderOnly=True)),
          c("Ask whether she wants the evening to stay friendly.", "friend"), c("Tell her plainly that you are attracted to her.", "desire"), c(personal_choice, "personal")),
        n("read", "Narrator", answer + "\nYou do not mistake her attention for permission. You ask what she wants to do with the evening. Targona says she wants to finish her drink, take a walk along the public road, and find out whether you can be present without steering her answer.", c("Walk beside her and let her set the pace.", "walk", flags=(f"targona.path.{key}.honest",))),
        n("misread", "Narrator", "You take a pause for agreement and begin to explain your own intentions again. Targona interrupts. 'That was not an answer to what I asked.' The rebuke is cool and direct. You can defend yourself or let the mistake stand as yours.", c("Apologize without explaining the apology away.", "walk", flags=(f"targona.path.{key}.careful",)), c("Defend your reading and end the meeting.", "leave")),
        n("friend", "Narrator", "Targona nods. 'I do want the evening to stay ours, whatever name we give it later.' You agree to keep the flirtation where she can see it and the question open. She tells you about the first time she broke formation to help another soldier, then asks what kind of person you were before anyone entrusted you with an army.", c("Answer honestly, including the part you would usually make into a joke.", "walk", flags=(f"targona.path.{key}.honest",)), c("Keep the evening friendly and talk about the road.", "leave")),
        n("desire", "Narrator", "Targona holds your eyes for a long second. 'Attraction is not a claim,' she says. 'Tell me what you find attractive, and leave me room to disagree with what you think you see.' Her expression warms when you speak of her dry humor, her commander's voice, and the way she chooses a dangerous task with her eyes open.", c("Tell her the truth without asking for an answer tonight.", "walk", flags=(f"targona.path.{key}.honest",)), c("Ask if she wants to stop the personal conversation.", "friend")),
        n("personal", "Targona", personal_moment, c("Continue the evening on the terms she chose.", "walk", flags=(f"targona.path.{key}.honest",)), c("End the date kindly.", "leave")),
        n("walk", "Targona", "She leads you down the public road, choosing the side with the better view of the wayhouse entrance. The conversation turns from the courier report to the people she served beside, then to the quieter question of what she likes when she is not standing watch. She admits she enjoys being surprised, as long as the surprise does not remove her choices. At the bridge she takes your hand, then releases it to point out the first star appearing above the ridge. 'I wanted to do that,' she says. 'Do not make it mean more than I have said.'", c("Tell her you like the meaning she gave it, and ask if she would spar with you tomorrow.", "spar_invite", flags=(f"targona.path.{key}.date_accepted", f"targona.path.{key}.spar_pending")), c("Thank her for the evening and let this be the whole answer.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship"))),
        n("spar_invite", "Targona", "She smiles and says yes, but makes the terms clear: blunted steel, no magic, no audience that might turn the result into a story about either of you. She decides when the bout ends. You agree. She releases your hand and walks you back to the wayhouse at the pace she chose.", c("Accept the terms and return for the practice bout.", flags=(f"targona.path.{key}.spar_pending",))),
        n("leave", "Targona", "She sees you back to the common room. The evening ends without a second invitation. The courier continues to carry ordinary letters, but she has not offered another date.", c("Leave with her answer respected.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship"))),
    ]
    SCENES.append(scene(f"targona.trickster_acq.meeting_{key}", f"The meeting Targona chose: {path}", "Targona", 5,
        "Meet Targona at the verified public stop", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.meeting_pending", "targona.path_meeting_actor_verified"),
        # Actor binding is intentionally omitted until a valid spawn/contact
        # producer is authored. "Targona" is not a native ContactUnit GUID.
        forbids=BLOCKED, delay=24, optional=True, Relationship="targona.trickster_acq",
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_intimate_invitation(path):
    key = path.lower()
    nodes = [
        n("start", "Targona", "The next letter arrives on the day she promised, without a second courier or a symbolic seal. 'I meant what I said about wanting another evening. There is one thing I want to ask before we meet. I have spent too many years being looked at as a warning, an instrument, or a miracle. When you look at me, I want to know what you want from the woman who is actually here.'\nThe question has no correct answer hidden in it.", c("Tell her you desire her, and ask what she wants you to notice.", "desire"), c("Say you care for her, but want to go slowly.", "slow"), c("Decline the romance and keep the friendship.", "friend")),
        n("desire", "Narrator", "Your reply names her voice, her certainty, her impatience with being turned into an example, and the beautiful force with which she occupies a room. You say you find the altered wing striking because it is hers, not because it needs a story attached. You do not call the captivity beautiful or claim the wound was worth it. You ask before describing the way you remember her looking at you.", c("Send the letter and leave the answer in her hands.", "meet", flags=(f"targona.path.{key}.intimacy_invited",))),
        n("slow", "Narrator", "You tell her that desire is present, but trust will matter more if it takes time. You will not turn patience into a performance she must reward. Targona writes back that this answer makes her want the next meeting more, not less. She is not ready to promise what she will want after it.", c("Accept another meeting with no promised physical step.", "meet", flags=(f"targona.path.{key}.intimacy_invited",))),
        n("meet", "Narrator", "At the next verified visit, Targona has chosen a quiet room near the public hall and left the door unlatched. She asks you to sit beside her, not behind her. After a few minutes she sets her hand palm-up on the table. The old damage crosses the white of her wing; the dark feathers catch the lamplight. She watches to see whether you will ask before making the gesture about her body.", c("Ask if she wants you to touch her hand.", "ask"), c("Leave your own hand beside hers and let her close the distance.", "wait"), c("Ask if she would rather talk instead.", "talk")),
        n("ask", "Targona", "'My hand, yes. The wing, not tonight.' She gives you her fingers. Her grip is warm and firm, a soldier's handshake becoming something more only because she chooses not to let go. Then she draws you closer and kisses you once, slowly enough that you can answer or stop. When she breaks the kiss, she asks, 'Do you want another?'", c("Say yes, and kiss her again while she keeps your hand in hers.", "commit", flags=("targona.trickster_acq.started", f"targona.path.{key}.committed")), c("Say not yet, and stay close without asking for more.", "slow_end")),
        n("wait", "Targona", "She closes the distance herself and rests her palm over your knuckles. 'This is not a test,' she says. 'I wanted to know if you could wait without making restraint another argument for why I should choose you.' You tell her that the wanting remains, and the waiting belongs to you. She kisses you, then asks before drawing you nearer.", c("Meet her kiss and let the relationship remain a choice for another day.", "commit", flags=("targona.trickster_acq.started", f"targona.path.{key}.committed")), c("Ask to leave the evening at a kiss.", "slow_end")),
        n("talk", "Targona", "You ask to talk. Targona's shoulders drop a fraction. She tells you how she has been thinking about the wing, not as a problem to solve but as a part of her that can be private, visible, or simply unmentioned depending on her mood. She asks what makes you feel desired rather than merely admired. You answer without turning the question back into an audition.", c("Tell her the truth and invite her to decide whether to kiss you.", "wait"), c("End the evening warmly, without physical intimacy.", "slow_end")),
        n("slow_end", "Narrator", "The evening ends with Targona's hand in yours, if she has chosen to hold it, and no demand that she turn patience into a promise. She says she wants to write again. A relationship may grow from that, or stop there if either of you changes your mind.", c("Keep the correspondence open and leave the choice mutual.", flags=(f"targona.path.{key}.slow",))),
        n("commit", "Narrator", "The second kiss is longer. Targona's thumb traces your knuckles, then stops where her hand meets the edge of her sleeve. She keeps the rest of her body at the distance she chose. 'I want you,' she says. 'Not because you helped me, and not because I need to prove that I am whole. I want you because I am alive, I am a woman, and I like the way you look at me when you remember I can say no.' The desire is direct; the next step remains hers to choose with you.", c("Ask if she wants to continue somewhere private, with each of you free to stop.", "future", flags=(f"targona.path.{key}.private_invited",)), c("Stay here and let the evening end after the kiss.", "slow_end")),
        n("future", "Targona", "She says yes to a private evening, then names her limits: the wing stays untouched tonight, she will not be praised for surviving, and either of you can stop without explaining. You tell her your boundaries too. She listens, then kisses you once more, long enough to leave no doubt about her desire and slow enough to let you answer. She asks if you want to go with her.", c("Accept the private evening she proposed.", "private", flags=(f"targona.path.{key}.private_evening",)), c("Choose another night and keep the boundary in place.", "slow_end")),
        n("private", "Narrator", "The room is quiet, and Targona leaves the door unlatched. She takes off her travel cloak, then unpins her hair and lets both wings settle at their own weight. The dark feathers catch the lamplight beside the clean line of her throat. She is not asking you to admire a wound. She is letting you see the woman who chose this room and chose you to enter it.\nHer palm rests on your chest. She asks you to say what you want. You answer with the truth and ask what she wants next. Targona kisses you, then guides your hand to her waist. The heat between you is unmistakable; so is the way she pauses to check your face before moving closer. The wing remains private, exactly as she asked.", c("Tell her you want more, and ask her to keep guiding the pace.", "night", flags=(f"targona.path.{key}.private_consented",)), c("Stay with kissing and stop there tonight.", "slow_end")),
        n("night", "Narrator", "Targona pulls you into another kiss, smiling against your mouth when you answer her touch. She sets the pace, you tell her what you want, and the two of you keep checking that the answer is still yes. Her clothes fall by choice, never as proof of healing; yours follow when she asks. The rest belongs to the closed room, the warmth of her body against yours, and the quiet permission to pause whenever either of you needs to speak.\nIn the morning, her hair is loose and one wing spills across the blanket. She turns toward you before the light reaches the window. 'I wanted that,' she says, then watches you answer. She is not embarrassed to have wanted it, and she does not ask you to make it mean forever.", c("Tell her you wanted it too, and ask for another night when she wants one.", flags=(f"targona.path.{key}.private_complete",)), c("Say the night was good, but you do not want a continuing romance.", "private_end", flags=(f"targona.path.{key}.private_complete", f"targona.path.{key}.ending_unfinished", "targona.trickster_acq.closed"))),
        n("private_end", "Targona", "She accepts the end of the romance without calling the night a mistake. You part with a kiss she initiates, then agree whether ordinary friendship is something both of you still want. The past answer remains hers; this ending belongs to the two adults who chose the night and then chose to stop.", c("Keep a friendship if she wants it too.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship")), c("Close the letters kindly.", flags=("targona.trickster_acq.closed",))),
        n("friend", "Narrator", "You decline the romance. Targona thanks you for saying it cleanly. She does not ask whether you might change your mind or use the patrol work to reopen the question. The friendship ends this invitation without revising the answer either of you gave before.", c("Close the romantic inquiry and keep only the friendship she wants.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship"))),
    ]
    SCENES.append(scene(f"targona.trickster_acq.intimacy_{key}", f"The question of wanting: {path}", "Targona", 5,
        "Read Targona's personal letter", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.date_accepted", f"targona.path.{key}.spar_complete", "targona.path_meeting_actor_verified"),
        forbids=(*BLOCKED, f"targona.path.{key}.friendship"), delay=48, optional=True, Relationship="targona.trickster_acq", Remote=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_spar(path, text):
    key = path.lower()
    nodes = [
        n("start", "Narrator", text + "\nTargona gives you a blunted sword and checks your grip. She has left her wing uncovered. It shifts slightly when she settles into her stance, no longer a secret she must guard from your eyes. 'This is practice,' she says. 'If I say stop, you stop. If you want to stop, say it. A win is not permission to follow me out of the ring.'", c("Take a careful stance and let her set the first pace.", "bout", flags=(f"targona.path.{key}.spar_ready",)), c("Ask her to demonstrate the first move.", "lesson", flags=(f"targona.path.{key}.spar_ready",)), c("Decline the bout and ask to talk instead.", "decline")),
        n("bout", "Narrator", "She attacks with the quick, economical movement of a trained warrior. You can read the line of her shoulder and choose to yield ground or meet the strike. Your answer changes the bout, not her opinion of whether you deserve affection.", c("[Athletics] Meet the strike without overcommitting.", check=dict(Skill="SkillAthletics", DC=25, Success="even", Failure="disarmed", CommanderOnly=True)), c("Give ground and keep your guard high.", "even")),
        n("even", "Narrator", "You catch her blade at the flat and turn it aside. Targona's next step comes close enough that you smell the clean leather of her glove. You do not chase the opening. She breaks contact first, smiling at your restraint without calling it a favor owed.", c("Accept the point and let her call the bout.", "win", flags=(f"targona.path.{key}.spar_win",)), c("Call the bout while the choice is still yours.", "draw", flags=(f"targona.path.{key}.spar_draw",))),
        n("disarmed", "Targona", "Your grip fails; the practice blade spins into the dirt. Targona stops at once and offers her hand to help you up, not to pull you into a hold. 'You were late on the turn,' she says. 'It happens.' Her amusement is real, but she waits for you to decide whether to continue.", c("Accept the loss and ask her to call the bout.", "loss", flags=(f"targona.path.{key}.spar_loss",)), c("Call the bout and thank her for the lesson.", "draw", flags=(f"targona.path.{key}.spar_draw",))),
        n("lesson", "Targona", "She shows you the turn slowly, then places the practice sword back in your hand. Her fingers rest against yours for one breath. 'This is the part where you watch me,' she says. 'Not the part where you decide what I mean by letting you close.' She steps away before the moment can become an assumption.", c("Repeat the movement and ask for one live pass.", "bout"), c("Say the lesson was enough.", "draw", flags=(f"targona.path.{key}.spar_draw",))),
        n("win", "Targona", "You earn a clean point. Targona is pleased, but tells you that you started to press the advantage after the whistle. She asks whether you noticed her hand go up. When you acknowledge it, she accepts the point and the apology as two separate answers.", c("Ask whether she wants another date.", "yes"), c("Say you would rather remain friends.", "no")),
        n("loss", "Targona", "You lose the exchange. Targona gives you a hand up and makes a joke about your timing, not your worth. The joke lands because she leaves room for you to laugh first. She asks whether you want to keep practicing another day, and you can say no without being called a coward.", c("Ask whether she wants another date.", "yes"), c("Say you would rather remain friends.", "no")),
        n("draw", "Targona", "You call the bout before either of you can turn it into a performance. Targona wipes the blades and thanks you for taking the stop seriously. She likes a capable opponent, she says; she likes a person who can stop even more.", c("Ask whether she wants another date.", "yes"), c("Say you would rather remain friends.", "no")),
        n("yes", "Targona", "She says yes. Her smile is no longer the one she wears for a soldier who has done well; it is private and unmistakably meant for you. She touches the back of your hand with two fingers, then asks if you noticed that she had wanted to do it before the bout. She will not accept a claim that winning earned it.", c("Tell her you noticed, and ask what else she wants you to know.", flags=(f"targona.path.{key}.spar_complete",))),
        n("no", "Narrator", "You say the bout has made friendship feel right. Targona accepts the boundary with a nod. She asks whether you are comfortable continuing letters as friends; you both get to choose that separately from the training.", c("Keep the letters friendly.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship", f"targona.path.{key}.spar_complete"))),
        n("decline", "Targona", "You decline the bout. Targona puts the practice sword away without disappointment. She asks whether you want to keep the date as conversation or go back to the wayhouse. Either answer leaves her in control of the evening.", c("Talk together without turning it physical.", "draw", flags=(f"targona.path.{key}.spar_complete",))),
    ]
    SCENES.append(scene(f"targona.trickster_acq.spar_{key}", f"The bout Targona chose: {path}", "Targona", 5,
        "Meet Targona for practice", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.spar_pending", "targona.path_meeting_actor_verified"),
        # Actor binding is intentionally omitted until a valid spawn/contact
        # producer is authored. "Targona" is not a native ContactUnit GUID.
        forbids=BLOCKED, delay=24, optional=True, Relationship="targona.trickster_acq",
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_path_ending(path):
    key = path.lower()
    nodes = [
        n("start", "Narrator", "Targona does not treat the evening as a cure for the past or proof that a relationship has succeeded. The next morning she sends a short note asking if the night felt good to you, and if anything should change before she invites you again. She writes about the future as a question she can revise, not a vow she must keep.", c("Tell her the truth and ask to build a continuing relationship.", "together"), c("Say the night mattered, but do not promise a future.", "apart"), c("Ask her to choose what she wants next.", "choice")),
        n("together", "Narrator", "You answer that the desire was real, the tenderness was welcome, and you want another evening. You do not claim exclusive rights to her or ask her to prove this choice by leaving anyone else. Targona writes back that she wants to keep choosing you, and that any future conversation about other partners will be separate, honest, and hers to enter or refuse.", c("Begin the relationship with that understanding.", flags=(f"targona.path.{key}.ending_together", "targona.trickster_acq.courtship")), c("Ask for one more slow meeting before naming it.", "slow")),
        n("apart", "Narrator", "You tell Targona that you wanted the night and are glad you shared it, but you cannot offer a continuing romance. She answers that she would rather receive this truth than a promise made from gratitude. She decides whether the correspondence remains friendly; no one uses the intimacy to claim the other person.", c("End the romance without erasing the affection.", flags=(f"targona.path.{key}.ending_unfinished", "targona.trickster_acq.closed"))),
        n("choice", "Targona", "Targona says that she wants another date. She also wants you to understand that wanting a relationship today does not give either of you control over tomorrow. You agree. Then she asks you what you want, without letting your answer substitute for hers.", c("Say you want to continue, and let her keep the right to change her mind.", "together"), c("Say you want to remain lovers without promising permanence.", "together"), c("Say you cannot offer what she wants.", "apart")),
        n("slow", "Narrator", "You agree not to name the relationship yet. Targona keeps the letter and proposes another public evening, where either of you can revise the answer. This route ends with possibility, not a committed state.", c("Leave the relationship undecided together.", flags=(f"targona.path.{key}.ending_unfinished",))),
    ]
    SCENES.append(scene(f"targona.trickster_acq.ending_{key}", f"An answer that can change: {path}", "Targona", 5,
        "Read Targona's next-morning reply", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.committed"),
        forbids=BLOCKED, delay=48, optional=True, Relationship="targona.trickster_acq", Remote=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_future(path, conflict):
    key = path.lower()
    nodes = [
        n("start", "Targona", conflict + "\nShe asks you to answer before either of you turns a hope into a promise. You can make a plan, ask for another conversation, or tell her what you want as an order. The last option is not a joke. She will treat it as an answer about the relationship.", c("[Diplomacy] Turn your wish into a plan that leaves her room to choose.", "plan", check=dict(Skill="SkillDiplomacy", DC=24, Success="plan", Failure="missed", CommanderOnly=True)), c("Ask what future she wants, then listen.", "listen"), c("Order her to follow your plans.", "order")),
        n("plan", "Narrator", "You suggest a schedule that leaves room for Targona's service, her own travel, and time together. You make the days concrete without claiming to decide the places she may go. She says the plan is workable, and then asks what happens when an emergency breaks it.", c("Agree that either of you can revise the plan when life changes.", "shared", flags=(f"targona.path.{key}.future_negotiated",)), c("Ask her to promise not to leave you waiting.", "listen")),
        n("missed", "Targona", "You offer a schedule that assumes she will change her service to fit yours. Targona points to the assumption before it becomes a fight. 'You asked me for a future, then filled it in before I answered.' She is not ending the relationship yet. She wants to know if you can revise the plan instead of defending it.", c("Apologize and ask what she wants to preserve.", "listen", flags=(f"targona.path.{key}.future_revised",)), c("Insist that your plan is safer.", "order")),
        n("listen", "Narrator", "Targona tells you what she wants: to keep serving, to spend time with you because she desires it, and to remain free to change the balance if her work or your life changes. The answer is not a promise to stay forever. It is a clear invitation to make the next decision together.", c("Propose shared time and separate duties.", "shared", flags=(f"targona.path.{key}.future_negotiated",)), c("Ask to continue without a schedule and check in honestly.", "open", flags=(f"targona.path.{key}.future_open",))),
        n("order", "Targona", "You tell her that she will go where you decide. Targona's expression closes. 'I chose to love you. I did not put my life under your command.' She takes her key and leaves the meeting. The route does not reward an order with romance. She writes once afterward to say that she is safe and wants no further private contact.", c("Accept the end and do not pursue her.", flags=(f"targona.path.{key}.future_ended", "targona.trickster_acq.closed"))),
        n("shared", "Targona", "You agree that the plan can change, and that neither of you owes the other permanent access to her time. Targona reaches for your hand. She says she wants to keep choosing you, including on the days that are not exciting enough to become a story. The relationship continues with separate duties and shared time, not a vow that erases either person's life.", c("Keep building the relationship on those terms.", flags=(f"targona.path.{key}.future_shared", f"targona.path.{key}.future_continuing", "targona.trickster_acq.courtship")), c("Leave the relationship open and decide each visit together.", "open", flags=(f"targona.path.{key}.future_open",))),
        n("open", "Targona", "You decide not to set a schedule yet. Targona likes the freedom and asks that neither of you use it to hide a change in feeling. She wants another date, not a contract. You agree that either person can say when the arrangement stops working.", c("Continue without a fixed plan and revisit it together.", flags=(f"targona.path.{key}.future_open", f"targona.path.{key}.future_continuing", "targona.trickster_acq.courtship")), c("Say you need a defined future and end the relationship kindly.", flags=(f"targona.path.{key}.future_ended", "targona.trickster_acq.closed"))),
    ]
    SCENES.append(scene(f"targona.trickster_acq.future_{key}", f"Two lives, one chosen plan: {path}", "Targona", 5,
        "Read Targona's letter about the future", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.ending_together"),
        forbids=BLOCKED, delay=168, optional=True, Relationship="targona.trickster_acq", Remote=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_path_followup(path, lines):
    key = path.lower()
    situation, Targona_says, outcome = lines
    nodes = [
        n("start", "Narrator", situation + "\nTargona has asked you to stand with her through the decision. She is not asking you to decide what she feels. The people involved will live with the outcome after the two of you leave, and she wants their stake named before either of you chooses.", c("Help her carry out the response she proposed.", "together"), c("Ask what she wants to do, then support her answer.", "her_choice"), c("Use your authority to settle it for her.", "overreach")),
        n("together", "Targona", Targona_says + "\nYou take the part she offers and leave the rest in her hands. The work is not romantic proof. It is a decision with a result other people can see.", c("Finish the work and ask how she feels about the result.", "after"), c("Stop if she wants you to step back.", "her_choice")),
        n("her_choice", "Targona", "Targona gives the answer herself. She chooses who speaks, what gets recorded, and which risks she accepts. You support that answer in the way she requests, then keep quiet where your title would make silence more useful than another order. The decision takes longer than a command and belongs more fully to the people who must live with it.", c("Stay beside her while the decision takes effect.", "after"), c("Leave the remaining work to her and the people involved.", "apart")),
        n("overreach", "Targona", "Your order makes the room go quiet. Targona does not raise her voice. 'You asked to share a life with me, then used its authority to take this choice away.' She asks you to reverse the order if it is still possible. If you cannot, she will decide whether she can remain with someone who mistook protection for permission.", c("Withdraw the order and apologize without asking her to soothe you.", "repair"), c("Defend the order as necessary and end the relationship.", "apart")),
        n("repair", "Narrator", "You withdraw the order where you can and name the harm without asking Targona to call it a misunderstanding. She does not forgive you on the spot. She asks for time to see whether your next choice matches the apology.", c("Give her the time and accept that she may leave.", "apart"), c("Stay available without pressing for an answer.", "after")),
        n("after", "Narrator", outcome + "\nThe two of you speak afterward about the choice, including the part that was difficult. Targona does not turn agreement into a promise that you will never disagree. She says she wants to keep the relationship, while leaving both of you free to revisit that answer when the circumstances change.", c("Continue, with this decision remembered honestly.", flags=(f"targona.path.{key}.followup_continues", "targona.trickster_acq.courtship")), c("Take more time before deciding what continues.", flags=(f"targona.path.{key}.followup_open",))),
        n("apart", "Narrator", "Targona accepts that you have chosen to leave or that she needs distance after your decision. She will not ask you to turn your shared history into a reason she owes you another chance. The correspondence can close here, or remain an ordinary friendship if both of you want it later.", c("End the romance and do not pursue her.", flags=(f"targona.path.{key}.followup_ended", "targona.trickster_acq.closed")), c("Leave the future unanswered and wait for her to write.", flags=(f"targona.path.{key}.followup_open",))),
    ]
    for page in nodes:
        page["Portrait"] = "TargonaCorrespondence"
    SCENES.append(scene(f"targona.trickster_acq.followup_{key}", f"After the choice: {path}", "Targona", 5,
        "Read Targona's next letter", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path], f"targona.path.{key}.future_continuing"),
        forbids=BLOCKED, delay=168, optional=True, Relationship="targona.trickster_acq", Remote=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


def add_path_frame(path, lines):
    key = path.lower()
    opening, conflict = lines
    nodes = [
        n("start", "Narrator", opening + "\n\"My answer at the end of the treatment stands as the answer I gave then. This is a different question. You may answer, ask for time, or decline. Silence will not become permission.\"",
          c("Answer the question she asked.", "report"), c("Ask for a day to think.", "time"), c("Decline the inquiry.", "decline")),
        n("report", "Narrator", conflict + "\nThe marker is damaged. The patrol can use the marked safe road, wait for another report, or delay repair until a trained crew arrives. Targona will not make romance payment for help. The choice affects ordinary people who walk there tomorrow.",
          c("[Knowledge: World] Separate evidence from assumptions.", "evidence", check=dict(Skill="SkillKnowledgeWorld", DC=22, Success="evidence", Failure="uncertain", CommanderOnly=True)), c("Ask Targona what risk she accepts.", "direct"), c("Refuse to act before the route is verified.", "decline")),
        n("evidence", "Narrator", "The dispatch proves the marker failed. It does not prove anyone caused it or that ground beyond it is safe. Targona accepts the limited finding. The patrol stays on the known road; repair waits for daylight. She asks if you can let an ordinary answer stand without turning it into a sign about either of you.",
          c("Let the patrol follow the safe route and record the limits.", "invite", flags=(f"targona.path.{key}.measured",)), c("Wait for a second report.", "uncertain")),
        n("uncertain", "Narrator", "Your evidence is incomplete. Targona sends the patrol by the safe road and delays repair. The marker remains imperfect overnight, but no one is sent past the line they can verify. The delay has a cost, and she accepts it rather than make the patrol absorb a risk she would not take.", c("Wait for the second report.", "invite", flags=(f"targona.path.{key}.measured",)), c("End the inquiry here.", "decline")),
        n("direct", "Narrator", "Targona answers plainly: she accepts a delayed repair, not a patrol sent past safe ground. She is not asking you to judge whether she is brave. The limit is hers. The patrol follows it, returns without incident, and a trained crew later repairs the marker.", c("Honor the limit she set.", "invite", flags=(f"targona.path.{key}.measured",)), c("Leave the operation to her.", "decline")),
        n("time", "Narrator", "Targona agrees to a day's pause. The courier does not return before then. The time lets you decide without making her question a deadline.", c("Send a considered answer after reviewing the report.", "evidence"), c("Let the inquiry pass.", "decline")),
        n("invite", "Narrator", "Targona's next letter is personal. She writes that she likes the way you let a limited answer remain limited. It does not make her first answer wrong; it makes this one new. She asks if you would meet at the next confirmed courier stop, in public. No rescue, treatment, or promise is attached. She will choose whether to stay, and you can still say no.", c("Accept the meeting without deciding what it means yet.", flags=("targona.trickster_acq.started", f"targona.path.{key}.meeting_pending", "targona.trickster_acq.invited")), c("Decline the meeting and keep the correspondence friendly.", flags=(f"targona.path.{key}.friendship", "targona.trickster_acq.friendship"))),
        n("decline", "Narrator", "You decline. Targona replies: 'Thank you for answering. I will not make you prove that answer with another favor. The old choice remains; this question ends here.'", c("Close the inquiry without hostility.", flags=(f"targona.path.{key}.declined", "targona.trickster_acq.closed"))),
    ]
    for page in nodes:
        page["Portrait"] = "TargonaCorrespondence"
    SCENES.append(scene(f"targona.trickster_acq.path_{key}", f"A letter on the {path} path", "Targona", 5,
        "Read Targona's letter", nodes,
        requires=("targona.free", "targona.ran_treatment_completed", "targona.ran_nonromance_seen", PATH_FLAGS[path]),
        forbids=BLOCKED, delay=24, optional=True, Relationship="targona.trickster_acq", Remote=True, ManualOnly=True,
        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5], RequiresAny=list(HISTORY)))


for _path, _lines in PATH_FRAMES.items():
    add_path_frame(_path, _lines)


for _path, _lines in PATH_MEETING.items():
    add_meeting(_path, _lines)
    add_spar(_path, PATH_SPAR[_path])
    add_intimate_invitation(_path)
    add_path_ending(_path)
    add_future(_path, PATH_FUTURES[_path])
    add_path_followup(_path, PATH_FOLLOWUPS[_path])


assert set(PATH_FLAGS) == set(PATH_ENTRY_PLANS)
assert set(PATH_FOLLOWUPS) == set(PATH_MEETING)
assert {book["Id"].rsplit("_", 1)[-1] for book in SCENES if ".path_" in book["Id"]} == {"angel", "azata", "aeon", "demon", "lich", "devil", "legend", "golddragon"}
assert all(f"targona.trickster_acq.meeting_{path.lower()}" in {book["Id"] for book in SCENES} for path in PATH_MEETING)


def validate_graphs():
    for book in SCENES:
        nodes = {page["Id"]: page for page in book["Nodes"]}
        assert len(nodes) == len(book["Nodes"]), book["Id"]
        graph = {node_id: set() for node_id in nodes}
        for page in nodes.values():
            for option in page["Choices"]:
                check = option.get("Check", {})
                targets = (option.get("Next"), check.get("Success"), check.get("Failure"))
                for target in targets:
                    if target:
                        assert target in nodes, (book["Id"], page["Id"], target)
                        graph[page["Id"]].add(target)
        visited = set()
        active = set()

        def visit(node_id):
            assert node_id not in active, (book["Id"], "cycle", node_id)
            if node_id in visited:
                return
            active.add(node_id)
            for target in graph[node_id]:
                visit(target)
            active.remove(node_id)
            visited.add(node_id)

        visit("start")
        assert visited == set(nodes), (book["Id"], "unreachable", set(nodes) - visited)


validate_graphs()


def validate_cross_scene_transitions():
    """Simulate authored flag handoffs without inventing game-side entry state."""
    by_id = {book["Id"]: book for book in SCENES}
    assert len(by_id) == len(SCENES)

    def play(book_id, steps):
        book = by_id[book_id]
        pages = {page["Id"]: page for page in book["Nodes"]}
        state = set()
        for node_id, outcome in steps:
            matches = []
            for option in pages[node_id]["Choices"]:
                check = option.get("Check") or {}
                targets = {option.get("Next"), check.get("Success"), check.get("Failure")}
                if outcome in targets or outcome in option.get("Set", []):
                    matches.append(option)
            assert matches, (book_id, node_id, outcome)
            state.update(matches[0].get("Set", []))
        return state

    for path in PATH_FLAGS:
        key = path.lower()
        if path == "Swarm":
            assert "swarm" in BLOCKED
            assert not any("swarm" in book["Id"].lower() for book in SCENES)
            continue
        meeting = by_id[f"targona.trickster_acq.meeting_{key}"]
        spar = by_id[f"targona.trickster_acq.spar_{key}"]
        intimacy = by_id[f"targona.trickster_acq.intimacy_{key}"]
        ending = by_id[f"targona.trickster_acq.ending_{key}"]
        future = by_id[f"targona.trickster_acq.future_{key}"]
        followup = by_id[f"targona.trickster_acq.followup_{key}"]
        # Entry state is a contract to be supplied by native integration, not
        # something this simulation pretends to create.
        assert "targona.free" in meeting["Requires"]
        assert "targona.path_meeting_actor_verified" in meeting["Requires"]
        assert PATH_FLAGS[path] in meeting["Requires"]
        assert f"targona.path.{key}.meeting_pending" in meeting["Requires"]
        assert f"targona.path.{key}.spar_pending" in spar["Requires"]
        assert f"targona.path.{key}.date_accepted" in intimacy["Requires"]
        assert f"targona.path.{key}.spar_complete" in intimacy["Requires"]
        assert f"targona.path.{key}.committed" in ending["Requires"]
        assert f"targona.path.{key}.ending_together" in future["Requires"]
        assert f"targona.path.{key}.future_continuing" in followup["Requires"]

        producers = set()
        for book in SCENES:
            for page in book["Nodes"]:
                for option in page["Choices"]:
                    producers.update(option.get("Set", []))
        assert f"targona.path.{key}.meeting_pending" in producers
        assert f"targona.path.{key}.spar_pending" in producers
        assert f"targona.path.{key}.date_accepted" in producers
        assert f"targona.path.{key}.spar_complete" in producers
        assert f"targona.path.{key}.committed" in producers
        assert f"targona.path.{key}.ending_together" in producers
        assert f"targona.path.{key}.friendship" in producers
        if path != "Trickster":
            assert f"targona.path.{key}.declined" in producers
        assert f"targona.path.{key}.ending_unfinished" in producers
        assert f"targona.path.{key}.future_continuing" in producers

        continued = play(f"targona.trickster_acq.future_{key}", [
            ("start", "listen"), ("listen", "shared"),
            ("shared", f"targona.path.{key}.future_continuing")])
        assert f"targona.path.{key}.future_continuing" in continued
        open_continuing = play(f"targona.trickster_acq.future_{key}", [
            ("start", "listen"), ("listen", "open"),
            ("open", f"targona.path.{key}.future_continuing")])
        assert f"targona.path.{key}.future_open" in open_continuing
        followthrough = play(f"targona.trickster_acq.followup_{key}", [
            ("start", "together"), ("together", "after"),
            ("after", f"targona.path.{key}.followup_continues")])
        assert f"targona.trickster_acq.courtship" in followthrough
        followup_breakup = play(f"targona.trickster_acq.followup_{key}", [
            ("start", "overreach"), ("overreach", "apart"),
            ("apart", "targona.trickster_acq.closed")])
        assert f"targona.path.{key}.followup_ended" in followup_breakup

        # This dry run follows authored options only. Native freedom, treatment,
        # parent ending, mythic-path, survival, and actor flags remain unseeded.
        if path == "Trickster":
            marker = play("targona.trickster_acq.the_second_letter", [
                ("start", "report"), ("report", "route"),
                ("route", "targona.trickster_acq.intervention_ready")])
            assert "targona.trickster_acq.intervention_ready" in marker
            entry = play("targona.trickster_acq.a_measured_impossibility", [
                ("start", "boundary"), ("boundary", "trust"),
                ("trust", "targona.path.trickster.meeting_pending")])
            assert "targona.trickster_acq.invited" in entry
        else:
            entry = play(f"targona.trickster_acq.path_{key}", [
                ("start", "report"), ("report", "direct"), ("direct", "invite"),
                ("invite", f"targona.path.{key}.meeting_pending")])
        assert f"targona.path.{key}.meeting_pending" in entry
        if path != "Trickster":
            friend_entry = play(f"targona.trickster_acq.path_{key}", [
                ("start", "report"), ("report", "direct"), ("direct", "invite"),
                ("invite", "targona.trickster_acq.friendship")])
            assert f"targona.path.{key}.friendship" in friend_entry

        date = play(f"targona.trickster_acq.meeting_{key}", [
            ("start", "friend"), ("friend", "walk"),
            ("walk", f"targona.path.{key}.date_accepted")])
        assert f"targona.path.{key}.spar_pending" in date
        meeting_friend = play(f"targona.trickster_acq.meeting_{key}", [
            ("start", "friend"), ("friend", "leave"),
            ("leave", "targona.trickster_acq.friendship")])
        assert f"targona.path.{key}.friendship" in meeting_friend
        spar = play(f"targona.trickster_acq.spar_{key}", [
            ("start", "bout"), ("bout", "even"), ("even", "win"),
            ("win", "yes"), ("yes", f"targona.path.{key}.spar_complete")])
        spar_refusal = play(f"targona.trickster_acq.spar_{key}", [
            ("start", "bout"), ("bout", "disarmed"), ("disarmed", "loss"),
            ("loss", "no"), ("no", "targona.trickster_acq.friendship")])
        assert f"targona.path.{key}.spar_complete" in spar_refusal
        assert f"targona.path.{key}.friendship" in spar_refusal
        intimate = play(f"targona.trickster_acq.intimacy_{key}", [
            ("start", "desire"), ("desire", "meet"), ("meet", "ask"),
            ("ask", "commit"), ("commit", "future"), ("future", "private"),
            ("private", "night"), ("night", f"targona.path.{key}.private_complete")])
        assert f"targona.path.{key}.committed" in intimate
        intimate_decline = play(f"targona.trickster_acq.intimacy_{key}", [
            ("start", "friend"), ("friend", "targona.path." + key + ".friendship")])
        assert f"targona.trickster_acq.friendship" in intimate_decline
        separated = play(f"targona.trickster_acq.intimacy_{key}", [
            ("start", "desire"), ("desire", "meet"), ("meet", "ask"),
            ("ask", "commit"), ("commit", "future"), ("future", "private"),
            ("private", "night"), ("night", "private_end"),
            ("private_end", "targona.trickster_acq.friendship")])
        assert f"targona.path.{key}.ending_unfinished" in separated
        together = play(f"targona.trickster_acq.ending_{key}", [
            ("start", "together"), ("together", f"targona.path.{key}.ending_together")])
        assert f"targona.trickster_acq.courtship" in together
        separation = play(f"targona.trickster_acq.intimacy_{key}", [
            ("start", "friend"), ("friend", f"targona.path.{key}.friendship")])
        assert f"targona.trickster_acq.friendship" in separation
        apart = play(f"targona.trickster_acq.ending_{key}", [
            ("start", "apart"), ("apart", f"targona.path.{key}.ending_unfinished")])
        assert "targona.trickster_acq.closed" in apart

    assert not any("ContactUnit" in book for book in SCENES)
    all_flags = [flag for book in SCENES for flag in book["Requires"] + book["Forbids"]]
    all_flags.extend(flag for book in SCENES for page in book["Nodes"]
                     for option in page["Choices"] for flag in option.get("Set", []))
    assert not any("{" in flag or "}" in flag for flag in all_flags)
    assert not any("targona.path_meeting_actor_verified" in option.get("Set", [])
                   for book in SCENES for page in book["Nodes"] for option in page["Choices"])
    assert "swarm" in BLOCKED
    assert PATH_FLAGS["Swarm"] == "swarm"


validate_cross_scene_transitions()
