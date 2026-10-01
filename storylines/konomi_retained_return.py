"""Trickster return of Konomi's exact retained dead capital actor.

Authored alternate development, not a canonical death or change of native office.
The host owns recovery dispatch, positive verification and current contact evidence.
"""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
UNIT = "ca2d58c5c65723945857e04fb85d30ce"
DEAD = "konomi.retained_dead"
CONTACT = "konomi.return_contact_available"
CLOSED = ("konomi.closed", "konomi.farewell", "konomi.private_parted")
REVIVALS = {"konomi": dict(Relationship="konomi", Unit=UNIT, DeathFlag=DEAD)}
SCENES = []


def recovery(id, title, nodes, requires=()):
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
        Relationship="konomi", Remote=True, Recovery="konomi", Chapters=[3, 5], Areas=[DREZEN],
        requires=("trickster", DEAD, *requires), forbids=("konomi.retained_return_confirmed",), optional=True))


def visit(id, title, nodes, requires=(), delay=0):
    for page in nodes:
        page["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
        Relationship="konomi", Remote=True, AfterRecovery="konomi", ContactUnit=UNIT, Chapters=[3, 5], Areas=[DREZEN],
        requires=("konomi.retained_return_confirmed", CONTACT, *requires), forbids=(DEAD, "inhuman"),
        delay=delay, optional=True))


recovery("retained_inquiry", "An objection to the last line", [
    n("start", "Narrator", '''{n}The little map of Drezen has acquired an annotation you did not write. Lady Konomi's name stands beside a narrow black stroke. When you move the lamp, the stroke remains dark. When you turn the map over, it appears on the other side.{/n}
{n}Konomi is dead. Her body is still in Drezen. Beneath your hand, the map seems unusually determined to tell you that these two facts settle the matter.{/n}
{n}On the map, a line of smaller writing appears. NO FURTHER CORRESPONDENCE EXPECTED.{/n}
{n}It is an extravagant claim to fit in so little space.{/n}''',
      c('[Examine the claim before attempting to change anything.]', "examine"),
      c('[Leave the map open for now.]', abort=True)),
    n("examine", "Narrator", '''{n}The annotation gives no reason why an expectation should be binding. You trace its letters without touching the black stroke. A second line emerges: ALL REPLIES RECEIVED AFTER CLOSURE WILL BE RETURNED TO SENDER.{/n}
{n}You ask who signed for the closure. The map produces a smudge shaped like a signature. You ask for a legible copy. The smudge acquires a second smudge certifying the first.{/n}
{n}A clerk passing the doorway sees you arguing with a map and quietly takes her documents elsewhere. You cannot fault her judgment.{/n}''',
      c('[Find the distinction between closing an account and deciding every future entry. Knowledge (World), DC 22.]',
        check=dict(Skill="SkillKnowledgeWorld", DC=22, Success="distinction", Failure="read_again")),
      c('[Read every line aloud until the map is forced to hear what it claims.]', "read_again")),
    n("distinction", "Narrator", '''{n}You have seen merchants close a ledger and open another on the same afternoon. A completed account can be accurate without being the last account anyone will ever keep.{/n}
{n}The map tries to move its annotation beneath the legend. You pin it with the lamp.{/n}
{n}The black stroke remains. You have not disproved her death. You have found a place where a true sentence has been made to do more work than it can bear.{/n}''',
      c('[Separate what happened from what may happen next.]', "name", flags=("konomi.return_distinction",))),
    n("read_again", "Narrator", '''{n}The writing becomes smaller whenever you approach the end. You borrow a magnifying glass. The writing becomes faint. You move the lamp closer. At last, forced into the margin, the map supplies a qualification: EXPECTATION DOES NOT CONSTITUTE PROOF.{/n}
{n}It then attempts to fold itself. The magnifying glass holds one corner down and the lamp holds another.{/n}
{n}You have spent an irritating hour obtaining a sentence that should have appeared first. The black stroke remains. Her death happened. The claim that nothing can follow it is a separate matter.{/n}''',
      c('[Leave room for something after the black stroke.]', "name", flags=("konomi.return_patient_reading",))),
    n("name", "Narrator", '''{n}There is room now for one line beneath Konomi's name. You could fill it with a title, an account of her usefulness, or a list of things you wanted from her. None would identify the woman more precisely.{/n}
{n}You write her name again. The second inscription does not erase the first.{/n}''',
      c('[Remember the woman whose company you have shared as a lover.]', "lover", requires=("konomi.lovers",)),
      c('[Remember the private address she chose to give you.]', "address", requires=("konomi.missed_private_access",), forbids=("konomi.lovers",)),
      c('[Remember the private meeting she agreed to after her dismissal.]', "known", requires=("konomi.private_meeting",), forbids=("konomi.lovers", "konomi.missed_private_access")),
      c('[Remember the personal conversations you began with her.]', "known", requires=("konomi.margin",), forbids=("konomi.lovers", "konomi.missed_private_access", "konomi.private_meeting")),
      c('[Leave room for the woman you have yet to know privately.]', "unmet", forbids=("konomi.lovers", "konomi.missed_private_access", "konomi.private_meeting", "konomi.margin"))),
    n("lover", "Narrator", '''{n}You remember the pause before she lets herself smile. There were times when you wanted to hurry through it, to hear the answer you hoped was coming. Now you remember how much of her was in making you wait.{/n}
{n}The map offers the word BELOVED in elaborate lettering. You turn it down. You want Konomi back, including the parts of the next conversation you cannot predict.{/n}''',
      c('[Keep the memory without writing her next answer.]', "prepare", flags=("konomi.return_remembers_love",))),
    n("address", "Narrator", '''{n}She supplied her own address. You remember the practical instructions and the unmistakable pleasure beneath them. An impossible delivery had led to an ordinary place where she wanted to receive another letter.{/n}
{n}You copy no promise into the new line. The address belongs to a history already lived, and that history will still be there if she returns.{/n}''',
      c('[Keep the address among your own papers.]', "prepare", flags=("konomi.return_remembers_address",))),
    n("known", "Narrator", '''{n}You remember the care she took over an answer. Even a few words could leave very little room for you to hear only what suited you. It is a precision you would like to encounter again.{/n}
{n}You almost improve her answer in the recollection. Then you remember the raised eyebrow that would have greeted your version, and find yourself smiling at an empty chair.{/n}''',
      c('[Remember the beginning as it was.]', "prepare", flags=("konomi.return_remembers_talk",))),
    n("unmet", "Narrator", '''{n}You know her name. You write it carefully. For once, the map cannot offer you a form with the rest conveniently filled in.{/n}
{n}The map seems disappointed by the blank space. You leave it blank. If there is to be a private acquaintance, she will have to take part in it.{/n}''',
      c('[Prepare the attempt without inventing an acquaintance.]', "prepare", flags=("konomi.return_no_private_history",))),
    n("prepare", "Narrator", '''{n}You draw a small arrow past the black stroke. The ink disappears. You draw it again, beginning beneath the second name rather than over the first. This time it holds.{/n}
{n}The arrow pulls at your fingertip. There is something at its other end, something the little map has been trying to keep you from noticing. Following it will take more than another argument with stationery.{/n}
{n}You leave the map beneath the lamp. The final annotation has changed to FURTHER CORRESPONDENCE UNDETERMINED.{/n}''',
      c('[Keep the prepared path for a deliberate attempt.]', flags=("konomi.return_path_prepared",))),
])


recovery("retained_attempt", "The line after her name", [
    n("start", "Narrator", '''{n}The arrow beneath Konomi's name has not moved. Its point ends at the place where the map insists there should be no more writing.{/n}
{n}You set a clean sheet beside it. The map promptly stamps the sheet COPY. You turn it over and write ORIGINAL CONTINUES. The stamp lifts itself from the paper, offended.{/n}
{n}Nothing has happened to Konomi yet. This is the opening you prepared, not proof that your power has reached her.{/n}''',
      c('[Take up the prepared thread of fate.]', "attempt"),
      c('[Wait before committing your power.]', abort=True)),
    n("attempt", "Narrator", '''{n}You follow the arrow with one finger. The room seems to take a breath and hold it. Somewhere close, the map's absurd argument touches something that has never been made of ink.{/n}
{n}Her death remains on the map. Beneath her name, you begin another line. You think of breath catching in a throat, of someone opening her eyes and wanting to know who has left a lamp burning.{/n}
{n}The paper grows warm beneath your hand. At its edge, a tiny annotation begins to write CONDITIONS MAY APPLY. You put your thumb over it.{/n}''',
      c('[Use your Trickster power to attempt to bring Konomi back to life.]', revive="konomi", flags=("konomi.retained_return_confirmed",)),
      c('[Release the thread without making the attempt.]', abort=True)),
], requires=("konomi.return_path_prepared",))


visit("return_first_words", "The first unfinished answer", [
    n("start", "Konomi", '''{n}Konomi looks at you, then down at her own hand. She opens it once, slowly, as though testing an unfamiliar glove.{/n}
"I have been told the simplest version. I would like to hear what you actually did."
{n}Her voice is quiet. She chooses each word with care, then stops after the sentence to take another breath.{/n}
"Begin with the part you know. We can leave the embellishments until I am better equipped to dislike them."''',
      c('"I found a way to attempt your return. You are here. I cannot give you an account of everything between."', "account"),
      c('"There was an argument with a map. The map lost its certainty before I gained mine."', "map"),
      c('[Give her time before continuing.]', abort=True)),
    n("map", "Konomi", '''{n}Her eyes close briefly.{/n}
"Of course there was."
{n}You describe the repeated name and the arrow that would not cross out the black stroke. She listens without interrupting until you reach the annotation about further correspondence.{/n}
"That is a very poor filing system."
{n}Her mouth moves before the rest of her face does. It is almost a smile.{/n}
"I understand why you found it congenial. Tell me what remains uncertain."''',
      c('"The useful distinction was between a closed account and the last account anyone will ever keep."', "method_ledger", requires=("konomi.return_distinction",)),
      c('"I read the fine print aloud until it admitted that an expectation was not proof."', "method_patient", requires=("konomi.return_patient_reading",)),
      c('[Give her the plain account as well.]', "account")),
    n("method_ledger", "Konomi", '''"You persuaded a document to admit it had exceeded its authority."
{n}Her eyebrows rise a little.{/n}
"I know several people who would take that distinction as a personal insult. I hope the map was one of them."
{n}She looks down at her hand again. This time she leaves it still.{/n}
"I am glad you noticed."
{n}For once she does not add a qualification.{/n}''', c('[Continue with what you can tell her plainly.]', "account")),
    n("method_patient", "Konomi", '''"You outlasted it."
{n}She considers you with a small, tired smile.{/n}
"I had wondered whether patience would ever become one of your more dangerous qualities. I should have expected you to discover it while inconveniencing somebody."
"The map was very determined."
"Apparently it had met its equal."
{n}She draws a breath before continuing.{/n}
"Thank you for staying with the argument. I am rather pleased to be here to hear how irritating it was."''', c('[Tell her the rest without embellishing your victory.]', "account")),
    n("account", "Konomi", '''{n}You tell her what you can establish without supplying an explanation for every strange part of it. She asks two questions, considers the answers, and does not ask you to improve the second one.{/n}
"I have no useful recollection to contribute. There are people who would find that disappointing."
{n}She runs her thumb along the side of her forefinger.{/n}
"I would find their disappointment exhausting. For the moment I should prefer they direct their questions elsewhere."
{n}She looks up again.{/n}
"And you? What have you been waiting to say?"''',
      c('"What we ended stays ended. I did not do this to reopen it."', "boundary", requires=("konomi.closed",)),
      c('"Our farewell stands. I did not come to collect on it."', "boundary", requires=("konomi.farewell",), forbids=("konomi.closed",)),
      c('"We parted. I still wanted you to have another day."', "boundary", requires=("konomi.private_parted",), forbids=("konomi.closed", "konomi.farewell")),
      c('"I missed you."', "love", requires=("konomi.lovers",), forbids=CLOSED),
      c('"I hoped we would have another private afternoon."', "private", requires=("konomi.missed_private_access",), forbids=(*CLOSED, "konomi.lovers")),
      c('"I hoped we would meet privately again."', "private", requires=("konomi.private_meeting",), forbids=(*CLOSED, "konomi.lovers", "konomi.missed_private_access")),
      c('"I wanted another conversation with you."', "acquainted", requires=("konomi.margin",), forbids=(*CLOSED, "konomi.lovers", "konomi.missed_private_access", "konomi.private_meeting")),
      c('"I am glad we can have this conversation."', "introduction", forbids=(*CLOSED, "konomi.lovers", "konomi.missed_private_access", "konomi.private_meeting", "konomi.margin"))),
    n("boundary", "Konomi", '''"I remember. I did not imagine you had forgotten."
{n}She rests both hands on the chair arms.{/n}
"Good. Say it plainly and I can file it. I have had people at my bedside all day drafting the rest of my life for me, and they all write badly."
{n}The tension at the corner of her mouth eases.{/n}
"Thank you for coming, and for what you attempted. It does not buy a different answer to an older question, and I am relieved you have not tried to spend it that way."''',
      c('[Let the visit remain a visit of recovery.]', "water")),
    n("love", "Konomi", '''{n}She reaches for your hand, misses it by a little, and lets you bring it the rest of the way. Her fingers close firmly once they have found yours.{/n}
"That is the first answer today that has made sense immediately."
{n}For several breaths she says nothing. Her thumb rests against your knuckle.{/n}
"I cannot manage a grand reunion. I can manage being pleased that you are here. You may have to accept that for this afternoon."''',
      c('"I can stay for the afternoon."', "water"),
      c('[Kiss the back of her hand and remain beside her.]', "water", flags=("konomi.return_hand_kissed",))),
    n("private", "Konomi", '''"So did I."
{n}She seems surprised by the steadiness of the answer.{/n}
"I have been trying to decide which plans must be reconsidered. It is a relief to discover one I need not discard immediately."
{n}She adjusts her hand on the chair arm.{/n}
"An afternoon will have to be shorter than we might wish. I am discovering that answering one question can leave me with very little appetite for the next."''', c('"Then we need not use up the afternoon talking."', "water")),
    n("acquainted", "Konomi", '''"I remember our conversations. I should dislike having to begin by pretending they had made no impression."
{n}She pauses, measuring the effort it takes to continue.{/n}
"But there are things I cannot tell you today merely because I was able to discuss them before. I am still finding out what an ordinary hour feels like."
{n}Her glance moves toward the water within reach.{/n}
"That may be the most useful place to begin."''', c('[Offer the water.]', "water")),
    n("introduction", "Konomi", '''"As am I. Though I suspect neither of us expected to begin a personal conversation this way."
{n}She studies you more closely, then inclines her head.{/n}
"Lady Konomi. I believe you know that already. I should prefer to make the introduction myself in any case."
{n}You give her your name without a recital of titles. She accepts it with a faint movement of her eyebrows.{/n}
"I have opinions about you. We need not begin with all of them. It would give the wrong impression that I have made up my mind about everything."''', c('"We can leave something for the next conversation."', "water")),
    n("water", "Konomi", '''{n}She takes the cup herself and drinks. When she sets it down, she looks annoyed by how carefully she had to attend to the simple movement.{/n}
"I would like a second visit. Tomorrow would be unwise. I will spend it convincing myself that tomorrow exists without immediately filling it."
{n}She looks at you over the cup.{/n}
"The day after, perhaps. Bring the map, if it has finished arguing. I should like to see whether it has spelled my name correctly."
{n}She does not ask you to leave at once. You remain until she begins to tire, and go before she can dismiss you, which she notes with professional approval.{/n}''',
      c('[Agree to the later visit.]', flags=("konomi.return_first_words", "konomi.return_followup_invited"))),
])


visit("return_second_visit", "A day she has left partly empty", [
    n("start", "Konomi", '''{n}Konomi has placed a blank sheet beside the map. She has also brought a ruler.{/n}
"Your account suggested something much less legible."
{n}The map's annotation is ordinary ink now. She reads it twice, then measures the empty space beneath her second name.{/n}
"There is room for several lines. A little presumptuous to decide that none would ever be needed."
{n}She sets down the ruler. You notice that she has brought it as an excuse to occupy her hands rather than because the measurement tells her anything.{/n}''',
      c('"What would you put there?"', "plans"),
      c('"You seem stronger."', "stronger")),
    n("stronger", "Konomi", '''"I am. I am also becoming better at recognizing the point before I cease to be."
{n}She leans back rather than proving the claim by sitting straighter.{/n}
"A woman stopped me this morning to say how wonderful it must be to receive a second chance. She meant kindly. I wanted to ask whether the first chance had come with instructions that I had somehow misplaced."
{n}The irritation fades into amusement.{/n}
"I thanked her. Then I came here and left two appointments unmade."''', c('[Ask what she wants from the time she has kept.]', "plans")),
    n("plans", "Konomi", '''"A meal I finish while it is warm. A walk whose length is decided before I begin it. A chance to hear an argument without everyone stopping to ask whether it has upset me."
{n}She glances at the blank sheet.{/n}
"I am not going to become a different woman merely because other people would find the story tidier. There are things I still believe. There are people I still find foolish. I intend to discover whether that list has grown."
{n}Her eyes return to you.{/n}
"You will hear about it if you are included."''',
      c('"I assumed I had a reserved place."', "laugh"),
      c('"I would rather hear your opinion than a version prepared to thank me."', "laugh")),
    n("laugh", "Konomi", '''"You have earned a hearing. Do not confuse that with a favorable judgment."
{n}She laughs, briefly and without preparing for it. Afterward she looks down as though the sound had surprised her into remembering something pleasant.{/n}
"There. That was useful."
{n}She folds the blank sheet once, then opens it again.{/n}
"We should also be accurate about what has not changed."''',
      c('[Speak about her continuing official position.]', "office", requires=("konomi.present",)),
      c('[Speak about the dismissal that already happened.]', "dismissed", requires=("konomi.dismissed",), forbids=("konomi.present",)),
      c('[Keep official appointments separate from this visit.]', "unappointed", forbids=("konomi.present", "konomi.dismissed"))),
    n("office", "Konomi", '''"My work has not become a love letter because you brought me back to it."
{n}The familiar firmness returns to her voice.{/n}
"I shall still advise you to do things you dislike, and I shall still report it to the capital when you refuse. Do not expect gratitude to soften the memoranda. Gratitude is not a line item."
{n}She presses the fold out of the paper with her palm.{/n}
"Outside the council room, you may call on me because you want to. That is a separate account, and I keep my accounts separate."''', c('[Let her official decisions remain her own.]', "next")),
    n("dismissed", "Konomi", '''"I remember being dismissed. I have had no difficulty retaining my opinion of it."
{n}Her expression permits you a small smile, though she does not join it immediately.{/n}
"This visit is not a return to that office. There would be decisions to make if either of us wished to discuss such a thing. We have not made them by discussing my health."
{n}She looks at the map again.{/n}
"An inaccurate account of this would be particularly irritating after all the effort you apparently spent distinguishing one line from the next."''', c('[Keep the old dismissal out of the new appointment.]', "next")),
    n("unappointed", "Konomi", '''"No appointment has been offered or accepted in this room. I would prefer that neither of us leave with the impression that it happened between the water and the map."
{n}She says it lightly, but waits until you answer.{/n}
"Good. That leaves us with the question I actually meant to ask. Whether there is another conversation we would enjoy, once I have stopped treating an afternoon as a considerable expedition."''', c('[Ask what kind of invitation she would welcome.]', "next")),
    n("next", "Konomi", '''{n}She folds the paper again and places it beneath the map.{/n}
"Keep that. You may eventually need a sheet that has not already expressed an opinion about my future."
{n}You slide it free. She has written only her name in the corner, in her own hand this time.{/n}
"I should like the next account of my life to contain something I have decided for myself. A modest ambition. Apparently it requires considerable persistence."''',
      c('[End the visit without reopening the relationship she has left.]', "closed", requires=("konomi.closed",)),
      c('[Keep your farewell intact while wishing her well.]', "closed", requires=("konomi.farewell",), forbids=("konomi.closed",)),
      c('[Let your parting remain a parting.]', "closed", requires=("konomi.private_parted",), forbids=("konomi.closed", "konomi.farewell")),
      c('[Ask about the next afternoon you can spend together.]', "familiar", requires=("konomi.lovers",), forbids=CLOSED),
      c('[Use the private address she already gave you.]', "address", requires=("konomi.missed_private_access",), forbids=(*CLOSED, "konomi.lovers")),
      c('[Ask about the next private visit you had already begun arranging.]', "familiar", requires=("konomi.private_meeting",), forbids=(*CLOSED, "konomi.lovers", "konomi.missed_private_access")),
      c('[Ask whether she would welcome a personal letter.]', "begin", forbids=(*CLOSED, "konomi.lovers", "konomi.missed_private_access", "konomi.private_meeting"))),
    n("closed", "Konomi", '''"Thank you."
{n}The answer is short, and she leaves it that way.{/n}
"I mean to take the walk I mentioned. A short one, before I decide that good weather is an instruction to prove something."
{n}She puts the ruler away and leaves the map with you. You tuck her signed sheet beside it.{/n}
"I hope you find a better use for that than arguing with it again. Though I suspect it knows where to find you."
{n}She leaves with plans for her own afternoon. Your earlier parting stands where you both left it.{/n}''',
      c('[Let the next afternoon belong to her.]', flags=("konomi.return_aftercare_complete",))),
    n("familiar", "Konomi", '''"You may also write something shorter than an account of the future."
{n}She watches you put away the sheet.{/n}
"For example, that you would like to see me on a particular afternoon. Or that you have thought of something I would find amusing. You need not wait until the subject is important enough for a report."
{n}She lets her hand rest beside yours before drawing it back.{/n}
"I should like something ordinary to look forward to."''', c('[Keep her request for the next invitation.]', flags=("konomi.return_conversation_resumed",))),
    n("address", "Konomi", '''"The address was given for that purpose. I should be annoyed to discover you had begun treating it as a relic."
{n}She smiles at the word, then reaches to straighten the map's curling edge.{/n}
"Ask me about the plans we made. Some may need to wait. I would rather tell you that than have you decide on my behalf that I have abandoned them."''', c('[Keep the next invitation practical and personal.]', flags=("konomi.return_conversation_resumed",))),
    n("begin", "Konomi", '''"A letter is manageable. I can put it down when I tire and return to it without making its author worry that the silence means something terrible."
{n}Her expression warms.{/n}
"I am not promising the answer you may want. I am telling you that I would like to read the question. There is a difference, and you have recently shown an unusual talent for finding those."''', c('[Let any new invitation earn its own answer.]', flags=("konomi.return_invitation_welcome",))),
], requires=("konomi.return_followup_invited",), delay=48)
