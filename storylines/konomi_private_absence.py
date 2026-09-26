'''Private Chapter 4 absence and optional Chapter 5 acknowledgement.

No courier crosses the Abyss and no mythic power or office is restored.
Existing reunion answers remain in place; the added answer and manual catch-up
both preserve a player's decision to leave the subject for another evening.
'''
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
BASE = ("konomi.dismissed", "konomi.office_completed", "konomi.private_departed", "konomi.private_address")
SCENES = []

SCENES.append(scene("konomi.private_absence", "The address in your keeping", "Konomi", 4, "", [
    n("start", "Narrator", '''{n}The fastening on a small pouch gives way while you are sorting your belongings. Nothing valuable falls far. You catch a folded sheet before it reaches the ground, recognize Konomi's handwriting on the outside, and remain crouched with it in your hand.{/n}
{n}The receiving agent's address is still perfectly legible. Knowing where a letter ought to go has become a different matter from being able to send one. There is no reason to believe that the impossible clerk who once accepted your invitation owes you another delivery, least of all from here.{/n}
{n}You gather the pouch's contents and set them beside you. Somebody else has the watch for now. You have time to mend a fastening, and nobody waiting to hear what your decision means for the crusade.{/n}''',
      c('[Sit down and repair the fastening.]', "repair"),
      c('[Keep the address safe. Leave the repair and the recollection for another time.]', abort=True)),
    n("repair", "Narrator", '''{n}The old cord has worn through at the knot. You pull the damaged length free and turn it between your fingers. It would be quicker to tie the two frayed ends together. You cut away the weakest part instead, leaving a shorter cord that must be threaded through the loops one at a time.{/n}
{n}Halfway through, your hands stop. You have been preparing an explanation of why Konomi has heard nothing. You imagine presenting it reasonably, in the correct order, until there can be no question of your having neglected her.{/n}
{n}In this imagined conversation she has not yet been allowed to say anything. You pull the last loop tight, then loosen it enough to open the pouch without tearing the seam.{/n}
{n}You could tell her about this, if you return: the fastening, the address, the argument you nearly won against someone who was not present. There is room in the pouch for an account. There is also room simply to keep the address.{/n}''',
      c('[Take out a blank sheet. Write an account for her to read only if you bring it home yourself.]', "page"),
      c('[Do not compose a letter. Recall the last departure carefully, without supplying her answer.]', "remember")),
    n("page", "Narrator", '''{n}You write her name. Beneath it you begin with the broken cord. It looks absurdly small on the page after everything you might have described, which is one reason you leave it there.{/n}
{n}"I kept the address you gave me. Today I repaired the thing I carry it in. I am telling you because, for a moment, I was angry with the cord for making me think about coming home."{/n}
{n}The next sentence begins as an apology for silence. You leave space beneath it. You can explain where you have been when she is there to ask questions. What would you want her to know that the explanation alone will miss?{/n}''',
      c('[Write that you miss being wanted without needing to be useful.]', "wanted_page"),
      c('[Write that you are afraid you will return expecting her life to have waited for yours.]', "waiting_page")),
    n("wanted_page", "Narrator", '''{n}"I miss being invited. Not summoned to something I can fix, not thanked for something I have already done. Invited because the person asking would rather have me there."{/n}
{n}You consider crossing out the distinction. Konomi has work of her own, and your evenings have included enough negotiations to make the sentence sound unfair. You add that. You do not want her to abandon the parts of her life she finds interesting in order to provide a refuge from yours.{/n}
{n}"I want to hear you enjoying an argument that does not depend on me winning a war. I would like to be allowed to interrupt because I want to kiss you. You may finish the argument first."{/n}
{n}That last concession takes longer to write than it should. You leave it. The page has begun to sound like a request she could actually answer, including an answer you did not prepare for her.{/n}''',
      c('[Keep the page with the address. Send neither through an untrusted bargain.]', flags=("konomi.private_absence_kept", "konomi.absence_page", "konomi.absence_wanted"))),
    n("waiting_page", "Narrator", '''{n}"I have been imagining that, if I reach you, we can continue from the last thing we said. I know that is not fair. You will have had days I have not even attempted to imagine."{/n}
{n}You begin a question about her work, then realize you are asking for a report you can put into order. What would be harder to hear? That she found something she preferred doing to waiting for news? That she had a good evening you were not part of? Or that she needed you once and learned how to manage without an answer?{/n}
{n}"Tell me one thing that changed while I was away. Something you chose, if there is one you want to tell me. I want to hear it without asking you to make it smaller so that I can fit back into the room."{/n}
{n}You read the question again before folding the page. For once, you have left most of the space beneath it empty.{/n}''',
      c('[Keep the page with the address. It will travel only when you do.]', flags=("konomi.private_absence_kept", "konomi.absence_page", "konomi.absence_changed"))),
    n("remember", "Narrator", '''{n}You smooth the fold of the address rather than write on it. Her directions deserve to remain legible.{/n}
{n}There was a wagon. There was a driver with work to do. Konomi had plans for Nerosyan that were neither an excuse to leave you nor a request to be persuaded to stay. You remember having to stand a little away from the horse when it stamped.{/n}
{n}The small movement is clearer than the words you have been rehearsing. Her touch on your sleeve, bringing you with her. For that moment, she had simply included you in the place she meant to stand.{/n}
{n}You try to keep the memory there, before it becomes a promise she never made. What do you most want to tell her about it?{/n}''',
      c('[Remember how much it meant to be wanted beside her, without a task to perform.]', "wanted_memory"),
      c('[Remember that she chose her journey. Resolve to ask what her own days became.]', "changed_memory")),
    n("wanted_memory", "Narrator", '''{n}You close your hand around the address and let yourself miss her. It is an inconvenient feeling. There is no order you can give that will turn it into a completed task.{/n}
{n}You remember what you would like to ask when you can speak again: an hour in which she wants your company, and the chance to believe her without looking for the service she needs in return. You would like to hear about her work in that hour. You would also like to kiss her before the account is over.{/n}
{n}She may have a very good reason to finish it first. Remembering that makes the imagined evening less obedient and more like something you want to live through.{/n}
{n}You put the address in the repaired pouch. The shortened cord is awkward to fasten, but it holds. When your turn comes to take the watch, you can do that without pretending this other desire has disappeared.{/n}''',
      c('[Keep the memory for a conversation she can answer.]', flags=("konomi.private_absence_kept", "konomi.absence_memory", "konomi.absence_wanted"))),
    n("changed_memory", "Narrator", '''{n}The wagon in your memory does not remain at the gate. You let it leave.{/n}
{n}You know very little about the rooms Konomi might be living in now, the people who might be asking for her advice, the ordinary annoyances she would have put in a letter if letters could reach you. You resist filling the gaps with a patient woman looking down an empty road.{/n}
{n}She may be impatient. She may be frightened. She may also be pleased about something you have not heard of. None of those possibilities cancels the others.{/n}
{n}You decide on one question to take home: What did you choose while I was away? You will have to let her answer before you decide what her answer means for you.{/n}
{n}The address goes into the repaired pouch. You pull the shortened cord shut and test it once. It holds. The question needs no fastening; it returns to you while you put the rest of your belongings away.{/n}''',
      c('[Keep the question without pretending you have received an answer.]', flags=("konomi.private_absence_kept", "konomi.absence_memory", "konomi.absence_changed"))),
], Relationship="konomi", Remote=True, Chapters=[4], last=4,
    requires=BASE, forbids=("konomi.present", "inhuman", "konomi.farewell", "konomi.private_parted"), optional=True, delay=0))


def earlier_reply_choices():
    # Original return can persist its letter response before the enclosing scene finishes.
    return [
        c('"You have already answered my letter. I want to talk about our lives now."', "absence_already",
          requires=("konomi.wrote", "konomi.wonder_answered"),
          forbids=("konomi.private_absence_kept", "konomi.private_absence_answered", "konomi.return")),
        c('"You have already answered my letter. I want to talk about our lives now."', "absence_already",
          requires=("konomi.wrote", "konomi.fear_answered"),
          forbids=("konomi.private_absence_kept", "konomi.private_absence_answered", "konomi.return", "konomi.wonder_answered")),
    ]


def reply_nodes(final_flags=()):
    '''The same acknowledgement can be offered at reunion or through explicit old-save catch-up.'''
    return [
      n("absence_open", "Konomi", '''{n}Konomi gives you her attention. When you hesitate, she does not supply an opening for you.{/n}
"You do not have to begin at the beginning. Choose the part you wanted me to hear."
{n}There is something unfamiliar about saying it now that she can answer. The account you kept is no longer yours alone to arrange.{/n}''',
        c('[Give her the account you kept with her address.]', "absence_page", requires=("konomi.absence_page",)),
        c('[Tell her about repairing the pouch and remembering her departure.]', "absence_memory", requires=("konomi.absence_memory",)),
        c('[Give her the earlier unsent letter you brought out of the Abyss.]', "absence_oldletter", requires=("konomi.wrote",), forbids=("konomi.private_absence_kept", "konomi.return", "konomi.wonder_answered", "konomi.fear_answered")),
        c('"We have already spoken since I came home. I would like to understand what has changed since."', "absence_already", requires=("konomi.wrote", "konomi.return"), forbids=("konomi.private_absence_kept",)),
        *earlier_reply_choices(),
        c('"I did not keep an account for you. I would like to talk about what we want from these visits now."', "absence_unrecorded", forbids=("konomi.private_absence_kept", "konomi.wrote"))),
      n("absence_page", "Narrator", '''{n}You give her the sheet. Konomi reads it without commenting on the crossings-out. Once she reaches the bottom she turns back to the first lines, then rests the page beside her.{/n}
"You carried this yourself."
"Yes."
"Good. I did not want a bargain made in my name merely because someone offered to bring me news."
{n}She touches the fold with one finger.{/n}
"May I keep it?"
{n}You agree. She does not put it away yet.{/n}
"I can hear the part you have not read aloud. Tell me whether I have understood it."''',
        c('[Ask for her answer about being wanted.]', "absence_wanted", requires=("konomi.absence_wanted",)),
        c('[Ask what changed in her own life.]', "absence_changed", requires=("konomi.absence_changed",))),
      n("absence_memory", "Konomi", '''"I remember the horse. I was trying to finish a perfectly sensible farewell, and it kept breathing on my shoulder."
{n}She listens while you describe the cord and the argument you caught yourself preparing.{/n}
"What did I say in your version?"
"I had not reached that part."
{n}She laughs, then grows quiet.{/n}
"I did the same. I had an excellent explanation of why I had been right to expect a letter. Then somebody would bring news from Drezen, and I would realize that I was arguing with a person who might not be able to answer at all."
{n}Her fingers curl against her palm, then relax.{/n}
"I wanted you alive. I was still angry about the silence. I could not make either feeling wait its turn."''',
        c('[Tell her why the memory made you want an ordinary invitation.]', "absence_wanted", requires=("konomi.absence_wanted",)),
        c('[Ask the question you kept about her own choices.]', "absence_changed", requires=("konomi.absence_changed",))),
      n("absence_oldletter", "Konomi", '''{n}You give her the letter you wrote in the Abyss. Konomi follows the worn creases as she opens it, then reads until she reaches your question about the plant.{/n}
"I cannot offer you an encouraging account of my gardening. I can tell you I was pleased to find that question here. You remembered something I was doing badly and still wanted to ask how it went."
{n}She reads the rest again before putting the page beside her.{/n}
"I wish you had been able to give me this sooner. I am glad you are here to hear the answer."''',
        c('[Ask about the beautiful sight you tried to describe.]', "absence_oldwonder", requires=("konomi.letter_wonder",), forbids=("konomi.letter_fear",)),
        c('[Let her answer the fear you wrote down.]', "absence_oldfear", requires=("konomi.letter_fear",)),
        c('[Tell her what you most want to say now.]', "absence_unrecorded", forbids=("konomi.letter_wonder", "konomi.letter_fear",))),
      n("absence_oldwonder", "Konomi", '''"I would have wanted to see it. You need not persuade me to approve of the Abyss before I can want to have stood beside you for a moment."
{n}She asks you to describe the light again. This time you can show its direction with your hands, stop when she has misunderstood, and hear the question that makes you remember another detail.{/n}
"There," she says at last. "I have something I can imagine."
{n}She looks pleased, then rueful.{/n}
"I cannot give you a memory of my being there. I can listen when you bring the memory here. I wanted that too, when something happened to me and there was no useful address for you."''', c('[Ask what she wants you to understand about her life now.]', "absence_now")),
      n("absence_oldfear", "Konomi", '''"I have read what you were afraid of. I do not know whether I can tell, from one evening, how much of it came home with you."
{n}She holds the letter against her knee.{/n}
"I would rather ask when I do not understand than pretend to recognize every change because I knew you before. You may have to explain things I once guessed correctly. I may dislike some of the answers."
"I know."
"I wanted to say it while you were listening. It is easy to promise that nothing will be different when the person concerned cannot answer."
{n}She offers you her free hand.{/n}
"I would like to hear what helps now. I also have things to tell you that will not fit into the person you remember. Let us make room for both."''', c('[Listen to what changed for her.]', "absence_now")),
      n("absence_already", "Konomi", '''"I remember. You need not begin as though you had only just arrived to tell me there is more to say."
{n}She turns toward you, leaving the things between you alone.{/n}
"We spoke after you came back. We have also had the dismissal to discuss, and the business of deciding whether we wanted to meet without an office between us. The first conversation did not settle all the later ones."
"No."
"I am glad we are having this one. Ask me about the person you have invited here now."''', c('[Ask what she wants from these visits now.]', "absence_now")),
      n("absence_unrecorded", "Konomi", '''"Then we shall talk now. There need not be a page to prove you thought of me."
{n}She takes a moment before continuing.{/n}
"We have made arrangements and kept them. I am pleased about that. It does not mean I have found a graceful way to tell you everything I want from the visits."
{n}She looks directly at you.{/n}
"Sometimes I would like to come without having a particularly good account of my day. Sometimes I should like you to interrupt the account because you would rather kiss me. I do not want either of us spending an entire evening being an agreeable correspondent in person."''',
        c('"I would like an invitation that does not require us to have something impressive to tell one another."', "absence_present_wanted"),
        c('"Tell me what has been hardest to fit into the arrangements."', "absence_now")),
      n("absence_present_wanted", "Konomi", '''"Come anyway, then. Tell me you would like to see me. I may have to suggest a different evening. I do not need you to invent a better reason."
{n}She holds out her hand. When you take it, she draws you nearer.{/n}
"I have wanted to ask you the same thing. There are days when I am tired, or cross, and have not yet learned anything worth explaining from either condition. I would like some company before I become interesting again."
"I might find you interesting then."
"You may discover how repetitive my complaints become. I am prepared to risk it if you are."''', c('[Stay near and ask what she has been making room for.]', "absence_now")),
      n("absence_now", "Konomi", '''"I am still learning how much of my time to promise before I know what an assignment will require. There is always someone who wants an answer before telling me how much work the question contains. I find it particularly difficult to refuse when the question interests me."
{n}She looks briefly exasperated, then returns her attention to you.{/n}
"This is part of the life I am making after the dismissal. You have seen some of it. I still want influence. Having something worth doing makes it tempting to give it the next evening as well, and the one after that. I can make a very persuasive case for each evening separately."
"Including this one?"
"I kept this one for you. I want to keep doing that. I would rather tell you what it competes with than arrive pretending I never wanted anything else."
{n}She rests her hand beside yours.{/n}
"And what should I understand about the future you want now?"''',
        c('"I gave up the power that once found a door for my invitation. I chose to become Legend."', "absence_legend", requires=("legend",)),
        c('"I can still bend a rule. I cannot turn the days we missed into days we spent together."', "absence_trickster", requires=("trickster",), forbids=("legend",)),
        c('"I want to make the next invitation without pretending I can promise every part of the future."', "absence_mortal", forbids=("legend", "trickster"))),
      n("absence_wanted", "Konomi", '''"I want you here."
{n}The answer comes before she has had time to make it elegant.{/n}
"I wanted you here when I was furious with a client. I wanted you here when I had done something well and could not bear to explain it to one more person who thought I ought to be grateful for the opportunity. I particularly wanted you here when there was nothing to report."
{n}She leans forward.{/n}
"I cannot promise never to ask you for anything. There will be things you can do that I cannot, and I will sometimes think you should do them. You already know how pleasant I am when I think that."
"I am not asking you to stop."
"Then believe the invitation as well. Do not make me disguise every difficulty in my life so that you can be certain I invited you for yourself."
{n}She waits for you to answer. This is the part you could not finish alone.{/n}''',
        c('"Tell me when you want help. I will try not to hear a task in every invitation."', "absence_her_days"),
        c('"Tonight I want to be wanted. Tomorrow you may bring me the most inconvenient question you have."', "absence_tonight")),
      n("absence_tonight", "Konomi", '''{n}Konomi studies you, then nods.{/n}
"Tonight, then. I can ask a question another day."
{n}She reaches for your hand and leaves her palm open between you.{/n}
"Come closer if you wish. You need not earn the place."
{n}You take her hand. Her fingers tighten around yours before she lets them rest. For a little while she seems as relieved as you are not to be explaining something.{/n}
"I have missed touching you," she says. "Even when the conversation I imagined was a quarrel. That was annoying."
{n}The admission makes her smile, but she does not use the smile to withdraw it.{/n}''', c('[Stay near and ask how she spent the days you could not hear about.]', "absence_her_days")),
      n("absence_changed", "Konomi", '''"I stopped leaving an evening empty every time somebody said there might be news."
{n}She watches your face as she says it.{/n}
"At first I arranged my work around the possibility. Then I went to a reception I would have missed, because a woman there could introduce me to people who commission negotiations. I wanted the introduction. I stayed long enough to obtain it."
"And the news?"
"There was none. That did not make my decision brave or wise. It meant I had spent an evening asking for something that might happen instead of sitting in my room waiting for something I could not arrange."
{n}She looks down at her hands.{/n}
"I enjoyed it. Someone asked for my opinion and wrote down the answer. For a while I was not the person who ought to know whether you were coming back. I do not want to apologize for being relieved."''',
        c('"I am glad you went. I wanted your life to have room for things I could not give you."', "absence_her_days"),
        c('"Part of me wishes you had missed me every moment. I know that is unfair. I am glad you did not have to."', "absence_honest")),
      n("absence_honest", "Konomi", '''"Thank you for telling me which part you know is unfair."
{n}There is affection in her voice, and a limit to it.{/n}
"I will not offer to have been more miserable. I was miserable often enough. I also wanted work, and company, and an evening when I did not have to be tactful about somebody else's consoling remark."
{n}She shifts nearer, without taking your hand for you.{/n}
"I am pleased to be here now. I would like that to be allowed to matter on its own."
"It does."
"Then stay for what I actually have to tell you. There is quite a lot of it. Some of it may even interest you."''', c('[Listen without asking her to revise the missing days.]', "absence_her_days")),
      n("absence_her_days", "Konomi", '''"That reception gave me two invitations to submit proposals. Neither was an offer of a position. I wrote both proposals. One received an answer. I remember trying to decide how often to remind the other woman that she had asked. It occupied much more of my attention than I should like to admit."
{n}Her expression brightens at the professional problem before she notices your attention and returns to the more difficult subject.{/n}
"That is what I mean. Those days were not an interval in which nothing happened. I was sometimes afraid you would never hear about them. Then I was afraid you would come back and be too changed to care."
"You might have changed too."
"I did. I am still finding out where."
{n}She draws a breath.{/n}
"Tell me what you want me to understand about the person who came back."''',
        c('"I gave up the power that once found a door for my invitation. I chose to become Legend."', "absence_legend", requires=("legend",)),
        c('"I can still bend a rule. I cannot turn the days we missed into days we spent together."', "absence_trickster", requires=("trickster",), forbids=("legend",)),
        c('"I want to make the next invitation without pretending I can promise every part of the future."', "absence_mortal", forbids=("legend", "trickster"))),
      n("absence_legend", "Konomi", '''{n}Konomi looks at you for a long moment.{/n}
"Was it a relief?"
{n}You answer as well as you can. She lets you finish before giving her own.{/n}
"I will not pretend the power meant nothing to me. It frightened people I could not persuade, and made people listen who would have discarded a request from either of us. There were uses I would have liked to put it to. You can probably name several arguments we would have had."
{n}She turns your hand over and runs her thumb once across your palm.{/n}
"But the invitation had your name on it. The answer was mine. The clerk did not provide those."
"There may be no impossible door next time."
"There was never a promise of a second delivery. I gave you an address because I wanted you to use it. If it changes, I shall tell you."
{n}She holds your gaze.{/n}
"We shall have to make arrangements. I know how to do that. I would like to know whether you still want to make them with me."''', c('"I do. With the life I have now."', "absence_close")),
      n("absence_trickster", "Konomi", '''"Please do not try. I should like the days I spent without you to remain mine, including the ones I would have preferred to spend differently."
{n}Her mouth lifts, but she waits until you have heard the request beneath it.{/n}
"Your first invitation reached me in a way I could not have arranged. I chose to answer. After that, we used a woman who knew the road and expected to be paid for traveling it. I rather liked knowing what she wanted."
{n}She takes your hand.{/n}
"I may ask for your help again. You may offer something impossible. We can discuss it then. I do not want the evenings we choose now to depend on improving the ones we could not have."
"Nor do I."
"Good. There is something I should like to do with this one."''', c('[Ask her what she wants.]', "absence_close")),
      n("absence_mortal", "Konomi", '''"I would distrust the invitation if you could."
{n}She considers that, then shakes her head.{/n}
"No. I might find it very attractive. I would need to distrust it anyway."
{n}She places her hand beside yours.{/n}
"We have an address, and people who know how to carry a letter along an ordinary road. I have work to return to. You have demands I cannot make disappear by wanting more of your attention. That gives us something to arrange."
"You make it sound possible."
"It is possible. It is not already done. I would rather begin than ask you for a better description of the future."''', c('[Take her offered hand.]', "absence_close")),
      n("absence_close", "Konomi", '''{n}Konomi moves close enough that you can feel her breath when she speaks.{/n}
"I wanted to hear what you had kept for me. I am glad you told me."
{n}She glances at your mouth, then meets your eyes again.{/n}
"May I kiss you? I should like to stop finding new ways to describe missing you."
{n}She stays close, waiting, her hand warm against yours.{/n}''',
        c('"Yes. I have wanted that too."', "absence_kiss"),
        c('"Stay close. I would rather keep talking for a while."', "absence_quiet")),
      n("absence_kiss", "Narrator", '''{n}Her first kiss is careful. When you draw her nearer, that care becomes attention of a different kind: her hand at the back of your neck, the pause in which she lets you return the kiss, the small impatient breath when you move away too soon.{/n}
{n}"Again," she says, and this time you do not make her ask twice.{/n}
{n}Afterward she rests her forehead briefly against yours. She has a hand on your sleeve and you are both smiling, a little unsteadily, at how much more difficult it is to speak now that you no longer need to.{/n}
{n}When she finally leans back, she keeps your hand. There will be more to tell each other. You begin with the evening still available, and the things each of you would like to do before it ends.{/n}''',
        c('[Keep this part of the evening for one another.]', flags=(*final_flags, "konomi.private_absence_answered", "konomi.absence_reunion_kissed"))),
      n("absence_quiet", "Narrator", '''{n}She accepts the answer and settles beside you, close enough that your shoulders touch.{/n}
{n}"Then tell me something badly," she says. "I have had enough time to imagine polished explanations. I would like the version you find while I am listening."{/n}
{n}You begin with a small detail and lose the order of events halfway through. She asks a question. You correct the first part, then discover that the detail matters for a reason you had not thought to explain. Konomi listens with her head tilted toward you, occasionally disagreeing with your description and waiting for you to defend it.{/n}
{n}In time she begins an account of her own. You are allowed to ask questions too. The evening acquires the untidy shape of two people who are still learning what they have missed and intend to keep listening.{/n}''',
        c('[Stay close and hear her account as well.]', flags=(*final_flags, "konomi.private_absence_answered"))),
    ]


CATCHUP = scene("konomi.private_absence_catchup", "What we have not said yet", "Konomi", 5, "", [
    n("start", "Narrator", '''{n}You arrange a private conversation with Konomi during one of her visits to Drezen. You tell her beforehand that you want to speak about the things your renewed visits have left unsaid, rather than leave them to interrupt another discussion.{/n}
{n}She agrees. When you meet, she makes room beside her and waits for you to choose where to begin.{/n}''',
      c('[Tell her about the account or memory you kept in the Abyss.]', "absence_open", requires=("konomi.private_absence_kept",)),
      c('[Speak about what you want from your visits now, bringing an older letter only if it remains undiscussed.]', "absence_open", forbids=("konomi.private_absence_kept",)),
      c('[Leave the subject for another visit. Continue the existing relationship as before.]', abort=True)),
    *reply_nodes(),
], Relationship="konomi", Remote=True, ManualOnly=True, Areas=[DREZEN], Chapters=[5],
    requires=(*BASE, "konomi.private_returned"),
    forbids=("konomi.present", "inhuman", "konomi.private_parted", "konomi.private_absence_answered"), optional=True, delay=0)
# The manual conversation can be deferred until after every career visit.
# Append earned recollections without moving any original answer or replaying a decision.
def add_career_recollections(item):
    moments = [
        ("decision_now", "We chose to take the owner's work without waiting. I wanted it. I still do. That does not entitle me to the tenant's good opinion as part of the fee. You heard me admit both things. I am glad I did not have to pretend to want less before you would stay beside me.",
         ("konomi.career_decided", "konomi.career_accepts_now"), ("konomi.private_terms_sent",)),
        ("decision_wait", "We chose to give the tenant time to find another adviser. I agreed to a smaller fee, not to become someone who no longer notices money. I still want the owner's work. You know what waiting cost me, and you have not required me to sound delighted about the cost every time I mention it.",
         ("konomi.career_decided",), ("konomi.career_accepts_now", "konomi.private_terms_sent")),
        ("terms_exclusive", "I sent the seasonal terms we discussed. First sight of the applicants, a guaranteed payment, a limit on how long that claim lasts. I am waiting for the owner's answer to those terms. I am not waiting to discover whether I want the work. You were there while I decided how expensive I meant to be.",
         ("konomi.private_terms_sent", "konomi.private_career_exclusive"), ("konomi.private_hours_kept",)),
        ("terms_portfolio", "I sent the smaller guarantee we discussed, with the freedom to approach other owners. I am waiting for her answer. I still remember the larger figure. It has not grown less attractive merely because I crossed it out. I chose the room to maneuver, and I liked having you beside me while I chose it.",
         ("konomi.private_terms_sent", "konomi.private_career_portfolio"), ("konomi.private_hours_kept",)),
        ("paid_exclusive", "She accepted the seasonal arrangement and paid me. You heard what the applicant thought of losing my help, and what I thought of finally choosing which proposals the owner hears. Neither account has become false. I want to be able to tell you when I enjoy this work without first proving that everyone enjoyed my getting it.",
         ("konomi.private_hours_kept", "konomi.private_career_exclusive"), ("konomi.private_consequence_complete",)),
        ("paid_portfolio", "The smaller guarantee was accepted. It keeps my room in Nerosyan paid for, and leaves me free to approach another landlord. It also leaves the owner free to ask another negotiator. You heard how much less appealing I found that part. I still want the independence. I am glad I can tell you when it is inconvenient.",
         ("konomi.private_hours_kept", "konomi.private_career_portfolio"), ("konomi.private_consequence_complete",)),
        ("settled_exclusive", "The tenant paid for her option. The seasonal agreement is signed, and I have been paid. You also heard about the applicant the owner listened to because I put her forward. I liked being able to do that. I have work worth returning to, and someone I want to tell about it. Our farewell did not make either thing smaller.",
         ("konomi.private_consequence_complete", "konomi.private_career_exclusive"), ()),
        ("settled_portfolio", "The tenant paid for her option. The other applicant chose the second place I found, and paid the agreed fee. The narrower terms held when the owner questioned them. You heard how pleased I was, even after paying for all those letters. Our farewell did not leave that business unfinished. I want more of that work, and more evenings in which to tell you about it.",
         ("konomi.private_consequence_complete", "konomi.private_career_portfolio"), ()),
    ]
    now = next(node for node in item["Nodes"] if node["Id"] == "absence_now")
    days = next(node for node in item["Nodes"] if node["Id"] == "absence_her_days")
    future_choices = deepcopy(now["Choices"])
    for suffix, words, requires, forbids in moments:
        identity = "absence_career_" + suffix
        for origin in (now, days):
            origin["Choices"].append(c('[Ask about the work she chose, and what she wants from it now.]', identity,
                requires=requires, forbids=forbids))
        item["Nodes"].append(n(identity, "Konomi", '"' + words + '"\n{n}She rests her hand beside yours, leaving you room to take it.{/n}',
            c('[Take her hand and tell her what you want her to understand about your own future.]', "absence_career_future")))
    item["Nodes"].append(n("absence_career_future", "Konomi", '"There. That is the woman you have invited. What should I understand about the person sitting beside her?"', *future_choices))


add_career_recollections(CATCHUP)
SCENES.append(CATCHUP)
for item in SCENES:
    for node in item["Nodes"]:
        node["Portrait"] = "Konomi"


def integrate(payload):
    reunion = next(s for s in payload["Scenes"] if s["Id"] == "konomi.private_reunion")
    if any(n["Id"] == "absence_open" for n in reunion["Nodes"]):
        return
    partners = next(n for n in reunion["Nodes"] if n["Id"] == "partners")
    partners["Choices"].append(c('[Tell her what you kept for her during the silence in the Abyss. The other answers leave this for another visit.]',
        "absence_open", requires=("konomi.private_absence_kept",), forbids=("konomi.private_absence_answered",)))
    partners["Choices"].append(c('[Give her the unsent letter from the Abyss that you have not discussed during this visit.]',
        "absence_oldletter", requires=("konomi.wrote",), forbids=("konomi.private_absence_kept", "konomi.private_absence_answered", "konomi.return", "konomi.wonder_answered", "konomi.fear_answered")))
    partners["Choices"].append(c('"We have already spoken since I came home. I would like to understand what has changed since."',
        "absence_already", requires=("konomi.wrote", "konomi.return"), forbids=("konomi.private_absence_kept", "konomi.private_absence_answered")))
    partners["Choices"].extend(earlier_reply_choices())
    nodes = reply_nodes(("konomi.private_returned", "konomi.reunion_kept"))
    for node in nodes:
        node["Portrait"] = "Konomi"
    reunion["Nodes"].extend(deepcopy(nodes))
