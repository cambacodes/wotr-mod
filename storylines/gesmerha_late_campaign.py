"""Living Chapter 5 Gesmerha visits at her native post-resolution Wintersun contact.

Packing, survivors and later affection are authored developments.
Native chapter, quest, leadership and death state remain read-only.
"""
from story_format import c, n, reaction, scene
from storylines.gesmerha_opening import UNIT, AREA, ANSWER_LIST

ETUDES = {"gesmerha.post_resolution_contact": "24505150d0cf493c936f2c50b1c94468"}
SCENES = []
BLOCKERS = ("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil")


def s(id, title, entry, nodes, previous, delay=24):
    for page in nodes:
        page["Portrait"] = "Gesmerha"
    SCENES.append(scene("gesmerha." + id, title, "Gesmerha", 5, entry, nodes,
        Relationship="gesmerha", Chapters=[5], last=5, ContactUnit=UNIT,
        Areas=[AREA], AnswerLists=[ANSWER_LIST], optional=True, delay=delay,
        requires=("gesmerha.wintersun_resolved", "gesmerha.post_resolution_contact", previous),
        RequiresAny=["gesmerha.truth", "gesmerha.illusions"], forbids=BLOCKERS))


s("the_things_still_here", "The things left to carry", '"Gesmerha? May I come closer?"', [
    n("start", "Gesmerha", '''{n}Gesmerha answers from behind a chest in the hall. Two bundles rest against its side. A third has been opened across her knees, revealing a rolled cloth and several pieces of dark carved wood.{/n}
"Yes. Speak as you come. Someone has left a stool where there was a clear floor this morning, and I have already given it enough of my attention."
{n}You tell her where it stands. She taps its nearest leg with the end of her staff, then sets the staff within reach against the chest.{/n}
"There. It has acquired an address."
{n}Her hand waits on the open bundle while she listens to your last steps.{/n}''',
      c('"I hoped there would be time after your visit to Drezen."', "after_court", requires=("gesmerha.reunion_kept",)),
      c('"It has been too long since our last afternoon."', "without_court", forbids=("gesmerha.reunion_kept",)),
      c('"I will return when you have finished this part."', abort=True)),
    n("after_court", "Gesmerha", '''"So did I. I was not certain where we would find it."
{n}She puts the loose pieces back into the cloth without tying it.{/n}
"I have come back for work that will not finish merely because I have explained our troubles to a Commander. These things were left in three different houses. I asked for them here so nobody would have to guess which roof I was under."
"You are not staying?"
"Not to begin the old days again. A few of us are sorting what people want to carry, and what someone ought to be responsible for leaving. The second question produces longer arguments."
{n}She makes room on the chest beside her by moving a folded blanket. She tells you where she has put it before asking you to sit.{/n}
"I am glad you came while the arguments still have pauses. I have been saving several complaints for someone who was not present to cause them."''', c('[Sit where she has made room.]', "work")),
    n("without_court", "Gesmerha", '''{n}Her fingers become still against the wood.{/n}
"Yes. Long enough for people to begin telling me what your silence meant. I preferred waiting until there was someone here who might actually know."
"I cannot make the time shorter by describing it."
"No. You can tell me some of it when you want to. I would like that better than another explanation supplied by a helpful neighbor."
{n}She moves a folded blanket from the chest and tells you where to sit.{/n}
"I have not resumed the old afternoons. We have brought things here to sort before deciding who carries them away. I want the work finished without letting every bundle become a reason to argue about the whole history of Wintersun. So far, I have been ambitious."
"Have Dera and the others returned?"
"Some. Runa died while you were gone. Dera has been teaching one of her songs with the pause Runa always insisted was too short. I have not corrected it. I can already hear exactly what Runa would say, without making Dera listen to me say it for her."
{n}Gesmerha lets the silence rest before asking whether you are comfortably seated.{/n}''', c('[Tell her you are, and listen to the work she came to finish.]', "work")),
    n("work", "Narrator", '''{n}Someone enters the hall carrying a load that knocks against the doorframe. Gesmerha turns toward the sound.{/n}
"Set it down, Halvek. If that is the long box, it will not fit beside me."
"It is the long box."
"Then we have saved ourselves one attempt. Beside the door, with the lid toward the wall."
{n}The man obeys. You hear the small grunt with which he straightens. Gesmerha asks whether he has eaten; he replies that his sister has made the question unnecessary twice already.{/n}
"Good. Fetch her before we begin. I want the owner of the argument present."
{n}His steps leave the hall. Gesmerha tilts her head toward you again.{/n}''',
      c('"What have you come back to settle as chief?"', "chief", forbids=("gesmerha.marhevok_rules",)),
      c('"What can you decide while Marhevok still holds authority?"', "marhevok", requires=("gesmerha.marhevok_rules",))),
    n("chief", "Gesmerha", '''"What is ours, and what people only became accustomed to borrowing. I had hoped the distinction would be simple when I was not the person asked to make it."
{n}She finds the end of the rolled cloth and lifts it from the bundle.{/n}
"The long box holds carving patterns. Some were made for families. Some for the clan. Some were made by a woman who accepted payment in food and died before anyone thought to ask whether she considered that a sale."
"And now someone wants them?"
"Her granddaughter wants the box. The woodshapers want the patterns. I want both of them to stop describing the other as a thief before we have opened the lid."
{n}Her thumb traces a raised ridge through the cloth.{/n}
"I also want the patterns. You should know that before I make a speech about hearing everyone fairly. I learned from two of them. I would dislike being told that the lessons may leave when I still have people to teach."''', c('[Ask about the woman who wants the box.]', "claim")),
    n("marhevok", "Gesmerha", '''"The things people have actually brought to me. I am not the chief, and I will not become one merely because it would make this conversation easier."
{n}Her voice is level, but her hand tightens around the cloth.{/n}
"Marhevok has followers. He also has people who will carry their own bundles without asking him to name what belongs inside. I have agreed to hear a dispute between some of them. They can reject my answer."
"Will he allow it?"
"He has not settled who owns this box. I will not give him credit for allowing every conversation he has not thought to forbid. Nor will I promise you that he will approve when he hears it."
{n}She releases her grip, smoothing the creased cloth against her knee.{/n}
"The box contains carving patterns. The woman who made them is dead. Her granddaughter wants them. Other woodshapers say they belong to the clan. I learned from them, and I want to keep teaching from them. That is my interest. It does not make my answer a decree."''', c('[Ask about the granddaughter\'s claim.]', "claim")),
    n("claim", "Gesmerha", '''"Sella. Halvek's sister. She has a sharper tongue and better reasons for using it than he would prefer."
"Does she carve?"
"No. That is what some people keep saying as though they had finished the discussion. Her grandmother also taught her how to mend a torn sleeve. I have not heard anyone insist the needles must go to a more promising tailor."
{n}Gesmerha smiles briefly, then shakes her head.{/n}
"But a pattern copied once may teach people for years. If every family puts its best work beyond another person's reach, something will be lost. I am not willing to pretend that is nothing because Sella has a reasonable claim."
"What does she intend to do with it?"
"I asked her to tell us herself. You may stay if you want to listen. I would like someone here who has not spent the morning preparing an answer."
{n}She reaches toward the space between you and stops with her palm open.{/n}''',
      c('[Take her hand briefly before the others return.]', "hand", requires=("gesmerha.lover",)),
      c('"I will listen. You can introduce me when they arrive."', "waiting")),
    n("hand", "Gesmerha", '''{n}You tell her where your hand is and meet hers. Her fingers close around it with a warmth that changes the small space between you.{/n}
"There you are," she says softly.
"I am here."
"I know. I wanted to say it anyway."
{n}She turns your hand between hers, finding a callus with her thumb. You tell her how it came there. Her reply is a quiet laugh, followed by a question about whether it still hurts.{/n}
"Only when someone investigates it thoroughly."
"Then I shall save the rest of my investigation for a less public occasion."
{n}She lets go before the footsteps return, smiling without having to explain the smile to anyone.{/n}''', c('[Stay to hear the claim.]', flags=("gesmerha.late_arrived",))),
    n("waiting", "Gesmerha", '''"Thank you. Tell me if I begin answering before they finish. I have heard the complaint often enough that I may mistake my impatience for knowledge."
"You could tell them that."
"I intend to. I was hoping to practice on someone who might be amused before being offended."
{n}Her smile lasts until the returning footsteps reach the hall. Then she asks Halvek to bring a stool for Sella and describes where you are sitting.{/n}
"We have company," she says. "Company with an invitation to listen, not a new owner for the box."
{n}Sella's answer comes from the doorway.{/n}
"Good. I have brought enough relatives to disagree with already."''', c('[Let Gesmerha make the introductions.]', flags=("gesmerha.late_arrived",))),
], "gesmerha.campaign_kept", delay=0)

s("the_box_with_two_names", "The name beneath the clan's", '"Let us hear Sella before we decide what the box contains."', [
    n("start", "Gesmerha", '''{n}Sella pulls her stool near the long box. Halvek turns it so the lid can open without striking the wall. Gesmerha asks each of them to say where they have put their feet, then stands and crosses the short distance with her staff.{/n}
"I want to touch the first pattern," she says. "May I?"
"Yes," Sella replies. "I would have said yes this morning too, if anyone had asked before telling me what I must leave behind."
{n}The lid opens with a low creak. Sella puts a flat piece of wood into Gesmerha's waiting hands. One edge has been cut into a series of shallow curves; the other bears marks too close together to read at a glance.{/n}
"My grandmother made that after she hurt her wrist," Sella says. "She could still draw the curves. She asked her sister to cut them. People point at it and tell me how skilled my grandmother was, as though her having needed help would spoil the lesson."
{n}Gesmerha traces the cut edge.{/n}
"I learned that curve from this piece. Nobody told me who held the knife."
"I know. That is one reason I want the box."''',
      c('"You want her remembered as a person, including the work she shared."', "person"),
      c('"Could the pattern travel without the history being lost?"', "travel"),
      c('[Ask to pause before the discussion continues.]', abort=True)),
    n("person", "Sella", '''"I want to keep what she left us. I should not have to give a speech about remembering her properly before anyone believes that is enough."
{n}Gesmerha sets the pattern across her knees.{/n}
"You should not. But I will ask what happens to the people who learned from it. Some have nothing of their teachers except the work they were shown."
"Then they should make something of their own."
"They are trying. A useful pattern makes trying less wasteful. I have thrown away enough good wood to dislike telling an apprentice that waste is the proper tribute to someone else's ownership."
{n}Sella's stool scrapes as she shifts forward.{/n}
"And I have spent enough years being told that the box will be more useful with somebody else. It always seems to become useful just when I want to take it home."
{n}Neither woman raises her voice. Halvek looks from one to the other, then sits on the floor rather than offer an opinion.{/n}''', c('[Ask what arrangements have actually been proposed.]', "offers")),
    n("travel", "Sella", '''"It could. If somebody wanted to hear the history before offering to improve it."
"I want to hear it," Gesmerha says. "I also want to keep the pattern where it can be used. Those wishes are going to interfere with one another unless we are careful."
"You could make copies."
"Of some pieces. This edge is easy to measure. The marks beside it may have been a note to someone who already knew what they meant. Copying every scratch would not teach me their meaning."
{n}Sella leans close enough to indicate the marks aloud.{/n}
"They are not instructions. They record what her sister said when she cut the third curve too deep. Grandmother thought the complaint deserved to last as long as the mistake."
{n}Gesmerha laughs before she can stop herself. Then she asks to feel the third curve again.{/n}
"I have been teaching people to reproduce that depth," she admits. "I thought it deliberate."
"It became deliberate once you taught it. You can keep doing it. I am asking to keep the piece that began it."
{n}Gesmerha turns the pattern carefully between her hands.{/n}
"That is a better argument than several we have had this morning."''', c('[Ask what arrangements could preserve both uses.]', "offers")),
    n("offers", "Gesmerha", '''"We can copy the three patterns the apprentices use most. Sella can take the originals and the rest of the box. It will take work, and the copies will be teaching tools with their makers named, not little relics pretending to have belonged to her grandmother."
"Who pays?" Halvek asks from the floor.
"The people asking for copies," Gesmerha replies. "I have put aside wood and money for tools. I can use part of it. The apprentices can give time if they choose."
"You delayed your tools once already," you say.
"I remember. This does not make the second delay free."
{n}She rests the pattern against the rim of the box.{/n}
"Or we leave the originals with Sella and borrow them for a set period when she is somewhere we can reach. She names the carrier and decides which pieces travel. We teach from what we already know until then."
"No demand that I live near the workshop," Sella says.
"None. That would be a different bargain, and one I do not think you want."
{n}Gesmerha turns toward your voice.{/n}
"You have heard us. Which cost would you be willing to help with? I will not ask you to announce that one of us has been the reasonable person all along."''',
      c('"I can help make and deliver the three teaching copies. Let Sella keep the originals."', "copies"),
      c('"Arrange a limited loan when Sella chooses. I can help return this box to her now."', "loan")),
    n("copies", "Gesmerha", '''"Then I will pay for the wood. Not the Commander's treasury. I want the teaching pieces, and I have been allowed to decide what I spend on them."
{n}Sella takes the pattern when Gesmerha offers it back.{/n}
"Three," she says. "No quiet decision to copy the rest while the lid is open."
"Three. You can sit with us while we work, if you want to."
"I would rather finish packing my mother's things. Ask me when a mark is unclear. I may know. If I do not, leave it unclear until someone does."
{n}Gesmerha nods, then remembers to answer aloud.{/n}
"Agreed. We will name your grandmother and her sister on the first copy. The depth of the third curve can keep its complaint."
{n}Halvek laughs. Sella tells him he has been forgiven neither for bringing the box without asking nor for carrying it badly.{/n}
"But you can carry it back," she adds. "After the three pieces are finished."
{n}Gesmerha feels for the edge of the lid and asks Halvek to lower it only when she has moved her hand.{/n}''', c('[Keep the three-copy agreement.]', "copies_end")),
    n("loan", "Gesmerha", '''{n}Gesmerha runs her thumb once more along the pattern before giving it back.{/n}
"I will miss having it to hand. Still. Agreed."
"Six days for a loan," Sella says. "Longer only if I agree before the carrier leaves. If you cannot promise the return, ask for a different time."
"And if you move farther away?"
"Then I will tell you where a message can reach me, if there is such a place. I cannot give you a road I have not traveled."
{n}Gesmerha rests her empty hands against each other.{/n}
"Then I shall teach the curve from what I know. I will tell them why it may differ from the old piece. There is work enough in that."
"You sound as though I have deprived you of something," Sella says.
"You have. Something I liked to use. You have also offered to lend it on terms any carver could follow. I can grumble and still keep my word."
{n}Sella exhales, a small sound that seems to surprise Halvek more than the argument did.{/n}
"Good. I should like to take the box home without being congratulated for allowing everybody to become wiser."
"Then let us make the trip useful instead," Gesmerha says. "There are other things waiting with it."''', c('[Keep the limited-loan agreement.]', "loan_end")),
    *[n(id, "Gesmerha", '''{n}Sella and Halvek leave together after agreeing where the box will be taken. Gesmerha waits for their steps to pass beyond the doorway before reaching for her staff.{/n}
"Will you walk with me as far as the door? I know the way. I would like the company."
{n}You offer your arm where she asks for it. She takes it lightly, testing the floor ahead with her staff rather than letting you draw her around the stool.{/n}
"I wanted you to agree with me," she says as you reach the threshold. "At the beginning. I had a very satisfactory account prepared of why I ought to keep everything."
"You might have argued it."
"I still could. That is what galls me. I have given my answer, and the other arguments are still perfectly able to wake me at night."
{n}Cool air reaches the hall. She turns her face toward it and loosens her grip on your arm.{/n}
"My grandmother used to say that a chief who never loses an argument has stopped listening to her clan. She said a great many things. I would like a better afternoon than this one with you, before I go."''',
      c('[Agree to help with the carrying, and keep time for an afternoon of your own.]', flags=("gesmerha.patterns_agreed", flag)))
      for id, flag in (("copies_end", "gesmerha.teaching_copies"), ("loan_end", "gesmerha.family_loan"))],
], "gesmerha.late_arrived", delay=0)

s("the_long_way_with_company", "The weight on the road", '"Are the things ready to be carried?"', [
    n("start", "Gesmerha", '''{n}The long box stands shut beside the hall door. Halvek has fastened carrying loops around it. Gesmerha is checking the knot nearest her, following each turn with a fingertip.{/n}
"I would like it to remain one box," she says. "Sella was very particular about receiving the lid along with everything beneath it."
"I heard her," Halvek replies.
"Yes. So did the people outside."
{n}He tests the second loop with a short lift, then lowers the box again. Gesmerha finds the handle of her own small tool roll and puts it over her shoulder.{/n}''',
      c('[Ask how the three copies came out.]', "copies", requires=("gesmerha.teaching_copies",)),
      c('[Ask whether she has told the apprentices about the loan arrangement.]', "loan", requires=("gesmerha.family_loan",)),
      c('[Postpone until you can help with the journey.]', abort=True)),
    n("copies", "Gesmerha", '''"Two are ready. The third is nearly ready. I cut the familiar curve too confidently and had to begin again. Sella was delighted to discover that her grandmother was not alone in producing the wrong depth."
"You could have kept it as another version."
"I could. I wanted this one to teach the agreed curve. I am allowed to dislike a mistake without discovering a philosophy that makes it excellent."
{n}She pats her tool roll.{/n}
"We are taking the originals back before she begins to wonder whether 'nearly ready' is a way of keeping the box. I measured what I need. I can finish my own piece without borrowing another day."
"And the tools you meant to buy?"
"Will wait. I have told the seller, and he has told me what he intends to charge if I wait too long. Nobody has become saintly about the arrangement. I find that reassuring."''', c('[Take the carrying loop Halvek offers.]', "road")),
    n("loan", "Gesmerha", '''"Yes. One asked whether Sella would permit a loan next month. I told him to ask her, with a date for returning it. He looked remarkably surprised by the simplicity of a thing he had hoped I would do for him."
"Did he ask?"
"He began composing the request. I told him to bring it to me only if he wants help. A chief who does every small thing herself because she is quicker ends with a clan that cannot tie its own boots."
{n}She checks the strap of her tool roll.{/n}
"Today we take the box back. No lesson secretly arranged at the destination. I am bringing tools because Sella asked me to look at a split in the handle of her grandmother's knife. I may be able to mend it. If not, I shall tell her."
"You would like to mend it."
"Very much. It would be pleasant to finish one useful thing without an audience debating what it means."''', c('[Take the carrying loop Halvek offers.]', "road")),
    n("road", "Narrator", '''{n}You and Halvek carry the box between you. Gesmerha walks beside the load, keeping one hand on the loop near Halvek while her staff tests the uneven ground. She tells him when his pace begins to lengthen beyond hers; he shortens it without making a ceremony of the correction.{/n}
{n}Near the crossing, the water has risen over the stones usually used as a path. A branch turns slowly against the nearest one. Gesmerha hears it scrape.{/n}
"That was not there yesterday," she says. "Set the box down on dry ground before anyone decides how brave to be."
{n}Halvek points toward the higher path. It follows the bank before crossing farther upstream; the detour would bring you to Sella after the people gathering for a lesson have left.{/n}
"They asked me to hear their first attempts," Gesmerha says. "I said I would. I would still prefer to arrive late with a dry box."
{n}She asks you to describe the stones and the direction of the current. You do, including the gap concealed by cloudy water.{/n}''',
      c('[Examine the current and the bank before choosing a crossing.]', check=dict(Skill="SkillLoreNature", DC=26, CommanderOnly=True, Success="read_water", Failure="mistaken")),
      c('"Take the higher path. We can explain why the lesson had to wait."', "higher")),
    n("read_water", "Gesmerha", '''{n}The branch is caught against a broken stake, not the stone beneath it. Downstream, water spreads thinly over a bed of gravel. You describe a route that keeps the load above the deepest channel and lets each carrier test a step before shifting the weight.{/n}
"Show Halvek first," Gesmerha says. "Then he can tell me when his feet move. I would rather hear one account at a time."
{n}You cross without the box to test the gravel, then return. Halvek follows your directions with the load while Gesmerha keeps the staff ahead of her and one hand at his elbow. At the far bank she pauses until both carriers have put the box down.{/n}
"All of it?" she asks.
"Lid included," Halvek answers.
"Excellent. We have exceeded Sella's lowest expectations."
{n}She checks her tool roll, then offers you the strip of cloth she keeps for drying the handles. You finish the walk before the lesson begins. Sella receives the intact box, and Gesmerha hears the learners gathering as Halvek sets it down.{/n}''',
      c('[Carry the box the rest of the way without hurrying her.]', flags=("gesmerha.delivery_kept", "gesmerha.crossing_read"))),
    n("mistaken", "Narrator", '''{n}The surface near the familiar stones looks calmer than it is. You step onto the first one to test it. It shifts, and the sudden scrape of your boot makes Gesmerha turn toward you.{/n}
{n}Halvek reaches for the carrying loop before the box can slide down the bank. Gesmerha catches his sleeve, releases it when he says he is steady, and puts both hands on the dry end of the lid. Nobody has entered the water with the load.{/n}
"Leave it there," she says. "Tell me where you are."
{n}You answer from the bank. One boot is full of cold water. It takes time to recover your balance, check the gravel under the box and explain exactly which stone moved.{/n}
"The higher path," Halvek says.
"Yes," Gesmerha answers. "After we have rested enough that nobody is carrying Sella's inheritance while your boot is full of water."
{n}Your attempted shortcut has used the time that might have saved the appointment. Gesmerha unrolls her cloth for your wet boot. She asks you not to call the delay nothing; people did make time to hear her.{/n}''', c('[Acknowledge the mistake and take the safer way.]', "late")),
    n("higher", "Gesmerha", '''"Then the higher path. I shall be disappointed about the lesson while remaining pleased that none of us has to fish for the box."
{n}She asks Halvek to describe the first climb. He tells her about the roots and where the bank narrows. She shifts her tool roll to keep it from catching on the carrying loop.{/n}
"We can send word if we meet anyone coming the other way," she says. "If not, I will apologize when we arrive. They can decide whether they want to give me another afternoon."
"You dislike missing it."
"Yes. I wanted to hear what they had done. I also wanted them to be glad I had come. That part is less useful to explain in the apology."
{n}She waits until you and Halvek have the load balanced before setting out.{/n}''', c('[Take the longer path together.]', "late")),
    n("late", "Narrator", '''{n}The detour is slow. When you stop to change hands on the carrying loops, Gesmerha asks to sit for a moment. She chooses a patch of dry ground after you describe it, rests her staff across her knees and tilts her face toward the air moving above the bank.{/n}
"I should have brought something to eat," she says.
{n}Halvek produces a parcel his sister gave him. Gesmerha laughs when he admits she supplied it because she expected him to choose an inconvenient route.{/n}
"I shall ask her whether she wishes to take over the planning. I may even mean it."
{n}You share the food before lifting the box again. By the time Sella receives it, the learners have gone. One has left a message: he showed the others his work without waiting, and would like Gesmerha to hear about it tomorrow.{/n}
{n}She asks Sella to read the message once more. Then she says, with a care you recognize, that tomorrow will suit her very well.{/n}''',
      c('[Leave the intact box with its owner and keep the changed appointment.]', flags=("gesmerha.delivery_kept", "gesmerha.crossing_delayed"))),
], "gesmerha.patterns_agreed")

s("a_lesson_without_her", "The work someone else began", '"What did the learners make of the patterns?"', [
    n("start", "Gesmerha", '''{n}Gesmerha has arranged three small carvings on the chest. Each rests on its own scrap of cloth. She asks you to sit, then tells you which one has an edge that catches a careless finger.{/n}
"I have stopped touching that side first," she says. "A valuable lesson. I hope its maker intended it."
{n}She lifts the middle piece and follows its broad curve with her thumb.{/n}
"Elun brought these. His own, his cousin's and one made by a woman who insisted she was only watching until someone lent her a knife."
"Did you hear their explanations?"
"More than once. I am trying to decide which questions I asked because I wanted to know, and which because I wanted them to discover how much I knew already."''',
      c('"We reached them before the lesson. What did you keep thinking about afterward?"', "present", requires=("gesmerha.crossing_read",)),
      c('"Did Elun tell you how the lesson went without you?"', "absent", requires=("gesmerha.crossing_delayed",)),
      c('[Return when she has finished examining them.]', abort=True)),
    n("present", "Gesmerha", '''"The woman who had meant only to watch. She would not ask me where to put the cut. She asked whether the shape had to turn inward at all."
"Did it?"
"Not for the thing she wanted to make. I had been preparing to explain how to turn it more neatly. She had already chosen something else."
{n}Gesmerha puts the piece back on its cloth.{/n}
"I enjoyed being there. I also spoke long enough that Elun had to ask whether there would still be time for everybody to work. He was polite. I managed to be polite in return before deciding how much I resented the interruption."
"And afterward?"
"I asked him to keep the time at the next lesson. He named a price in lessons of his own. Apparently he can learn administration from me without becoming unable to negotiate."
{n}Her smile is fond and exasperated.{/n}
"He will do well, if he stops trying to make every handle impressive enough for a feast."''', c('[Ask how their next lessons will work.]', "patterns")),
    n("absent", "Gesmerha", '''"In great detail. They began by waiting for me. Then someone asked whether the wood would become easier to cut if they stared at it longer. I suspect Elun supplied that part of the story after discovering I could bear it."
"They worked without you."
"Yes. They made several mistakes I could have prevented. They also tried something I would have discouraged because I had failed at it years ago. It worked well enough to annoy me."
{n}She turns the broad piece between her hands.{/n}
"I apologized for not arriving when I said I would. He told me where they needed help now. I had expected to begin with the lesson I had prepared. The work had gone on without waiting for my explanation."
"Was that difficult?"
"For several embarrassing breaths. Then I had something interesting to do. I can survive being late to a discovery. I should prefer not to practice on every occasion."
{n}She sets the piece down in its proper place.{/n}
"Elun will begin the next lesson. I have asked him to leave me the difficult questions, rather than every question. He looked pleased until I told him I meant it."''', c('[Ask how their next lessons will work.]', "patterns")),
    n("patterns", "Narrator", '''{n}Gesmerha asks you to move the untouched cup away from the three pieces and say where you set it. She waits for your answer before spreading a clean cloth across her knees.{/n}''',
      c('[Ask whether the third teaching copy is finished.]', "copies", requires=("gesmerha.teaching_copies",)),
      c('[Ask whether Sella agreed to the requested loan.]', "loan", requires=("gesmerha.family_loan",))),
    n("copies", "Gesmerha", '''"Finished. Elun checked the edge against my measurements, and Sella told us which names belonged beneath it. I asked her to say them slowly while I cut. She corrected my first attempt at her great-aunt's name. I would rather be corrected before the wood becomes difficult."
"Will the copies stay with you?"
"One with me, two with the others. If I keep every useful piece beside my own chair, I shall have paid for a less honest version of taking the box."
{n}She gives a small, unwilling laugh.{/n}
"I wanted all three. I still want to know where they are. The owners of the work have agreed to tell me. That will have to serve."
"And Sella?"
"Has the originals and the box. She sent a strip of cloth for wrapping the most delicate copy. Her grandmother's sewing, apparently. I have been warned that the stitches are not clan property."
{n}Gesmerha's laughter returns, less guarded this time.{/n}''', c('[Ask what remains for her own hands.]', "hers")),
    n("loan", "Gesmerha", '''"She agreed to one piece, for six days, when the carrier can make both journeys. It is not here now. I made Elun repeat that part after he began planning a lesson around something he had not yet received."
"What will he teach instead?"
"The shape he has already made. I will help him explain the parts he learned by accident. There are enough of those to fill the first afternoon."
{n}She lifts the broad carving once more, then puts it down.{/n}
"Sella let me mend her grandmother's knife handle. The split was shallow. I told her what would make it open again, and she asked me to explain how she could bind it herself."
"Did you?"
"Yes. I enjoyed it. No argument about who ought to own the lesson afterward."
{n}Her hand rests on the clean cloth.{/n}
"The box is hers. If a loan comes at a bad time, we ask for another. I will not build my workshop around a box that lives under somebody else's roof."''', c('[Ask what she wants her own workshop to become.]', "hers")),
    n("hers", "Gesmerha", '''"Smaller, for a while. That was not the answer I expected to want."
{n}She folds the cloth into a narrower strip.{/n}
"I want to teach people who will carry something away without requiring me to carry every tool after them. I want a morning when I can choose one piece of work and remain with it until I understand why it displeases me."
"Would you miss being needed?"
"Yes. I expect to become inconvenient about it. You may remind me of this conversation if you first allow me to complain for a reasonable length of time."
"How long is reasonable?"
"We shall discover where we disagree."
{n}Her smile lingers as she lays the folded strip aside.{/n}
"The box has reached its owner. The work I promised is settled. There will be other questions, but I do not intend to borrow them merely because this one has finished."
{n}She turns toward your voice.{/n}
"I would like an evening with you. An evening nobody has requested for the benefit of the clan. Would you come?"''',
      c('"Yes. Tell me where you would like to meet."', "invitation"),
      c('"I would like to spend it as friends."', "friend_invitation", forbids=("gesmerha.lover",))),
    n("invitation", "Gesmerha", '''"Here, after the last person has finished looking for something they put away themselves. I have a room for the nights we spend sorting. There is a door. I find that an underrated piece of workmanship."
"Should I bring anything?"
"Yourself. A story, if you want to tell it. Nothing you think I must admire before accepting the company."
{n}She reaches toward you, and you tell her where your hand waits. Her fingers touch yours briefly.{/n}
"Ask before moving anything when you arrive. I have learned the room by the arrangement I made this morning. If someone has improved it for me, I shall need time to tell them what I think."
"I will leave the improvements to you."
"Then we have made an excellent beginning."''', c('[Keep the private invitation.]', flags=("gesmerha.work_settled",))),
    n("friend_invitation", "Gesmerha", '''"Then as friends. I did not intend to invite an answer you had already told me you did not want."
{n}She gathers the three carvings into their cloths, describing where each will go before standing.{/n}
"The room I am using has a door. We can close it against the people who believe a question becomes urgent merely because they have noticed someone else enjoying an evening."
"And if they knock?"
"They can tell me which roof is falling. If no roof is falling, they can return tomorrow."
{n}She laughs at your reply, then asks you to repeat it so she can decide whether she wants to use it herself.{/n}''', c('[Keep the evening as friends.]', flags=("gesmerha.work_settled", "gesmerha.evening_as_friends"))),
], "gesmerha.delivery_kept")

s("the_room_she_chose", "After the last knock", '"It is me. May I come in?"', [
    n("start", "Gesmerha", '''"Come in. Bar the door behind you."
{n}Gesmerha sits on the edge of the bed. Her boots stand beneath it, heels to the wall. A lamp burns on the chest by the door for your sake; its light finds the long hair she has loosened from its tie.{/n}
"There is a chair two steps to your left. Leave it where it is, or I will fall over it at dawn."
{n}You sit. She turns her face toward the creak of it and settles her bare feet on a folded blanket.{/n}
"I have been waiting for the last knock. Someone wanted to know where we put the smallest pattern. I told him to ask whoever put it away. Then he remembered that was himself."
"Did you forgive him?"
"Tomorrow, perhaps. Tonight the door is barred."''',
      c('[Sit beside her on the bed.]', "lover", requires=("gesmerha.lover",)),
      c('"I have been thinking about what might be between us."', "slow", requires=("gesmerha.campaign_slow",), forbids=("gesmerha.evening_as_friends",)),
      c('"I am glad we have kept an evening for our friendship."', "friends", requires=("gesmerha.campaign_friends",), forbids=("gesmerha.evening_as_friends",)),
      c('"I have come for the evening we agreed to spend as friends."', "friends", requires=("gesmerha.evening_as_friends",)),
      c('"I cannot keep the evening clear yet. May I return?"', abort=True)),
    n("lover", "Gesmerha", '''"Good. I have thought about it too. All day, with a mallet in my hand, which is not safe."
{n}She reaches for you as you sit and finds your arm, then your shoulder, then the fastener at your collar, and laughs low when it resists her.{/n}
"This thing again. Take it off before I take it off with my teeth."
{n}You unclasp it and drop it on the chest. When you turn back she already has a hand at your cheek, and she pulls you down into a kiss that begins gently and does not stay that way. She takes your hand and sets it at her waist, and holds it there.{/n}
"There. A better use for a door than keeping out clansmen."
{n}Her mouth is still close to yours.{/n}
"Now. Do you want me tonight, or do you want to sit and talk and kiss me like two youngsters at a harvest dance? I can bear either. One I would like better."''',
      c('"I want you tonight."', "night"),
      c('"Talk and kisses tonight. The rest another night."', "gentle")),
    n("slow", "Gesmerha", '''{n}Gesmerha rests her hands on the blanket either side of her.{/n}
"So have I. Even on the days you argued with me over the box, I liked having you there to argue."
"I want more than good afternoons."
"Then say what more. I have imagined three answers already, and I want the true one before I grow fond of a wrong one."
{n}You tell her. She listens with her head tilted, the way she listens for a crack in a block, and asks one question: what becomes of this when you are on your road and she is on hers.{/n}
"I will not sit wherever it is easiest for you to find me," she says, when you have answered. "I have a clan to see settled, and work I want, and days I mean to keep for myself. You have your own people. I will not speak for them, and you will not speak for mine."
"Agreed."
"Good. Then I want to kiss you. That was meant to be the easy part, and now I find I want your answer more than I wanted the other one."''',
      c('"Yes. Be my lover."', "first_kiss"),
      c('"Not tonight. Let this evening be only an evening."', "open"),
      c('"I want to keep knowing you as a friend."', "friends")),
    n("first_kiss", "Gesmerha", '''"Then come here."
{n}She finds your hand and draws it to her shoulder. Her other hand finds your face. She waits there a breath, until you lean to her, and then kisses you with a warmth that wipes out whatever she had meant to say after it.{/n}
"Was that the answer you imagined?" you ask when she draws back.
"No. The one I imagined had a clever remark after it. I have lost the remark."
"You could look for it."
"I would rather spend the time on this."
{n}She kisses you again. When she settles against you afterward, she warns you off the blanket under her feet; she has finally got them warm. You stay like that, learning how she likes to be held, and she asks for another kiss before either of you says a word about tomorrow.{/n}''',
      c('[Keep the new relationship and an unhurried first evening.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers", "gesmerha.committed")),
      c('"Don\'t send me back to the chair. Let me stay the night."', "first_night")),
    n("night", "Gesmerha", '''"Then stay."
{n}She says it the way she says *hold it* over the mallet. She is already pulling the tie from the end of her braid. Then she stands, takes the hem of her shift in both hands, draws it over her head and drops it, and stands there in the lamplight with her chin up, letting you look, because she knows you are looking.{/n}
"I cannot see you. You will have to come here so I can find out what I am getting."
{n}You come. She reads you the way she reads a block she means to cut: shoulders, the scars the war has left, the belt, which she deals with herself. Her hands are rough from the chisels and quite sure of what they want. When she has you as bare as she is, she pushes you down onto the bed, which was built for one sleeping woman and says so, and she laughs into your mouth at the creak of it and does not care.{/n}
"Too small," she says. "Good. Nowhere for you to go."
{n}She pulls the blanket over both your shoulders, slides her knee across you, and draws your hips hard up against hers.{/n}''',
      c('[Continue]', "after_night")),
    n("gentle", "Gesmerha", '''"Then sit close enough that I need not keep finding the distance."
{n}You settle beside her with your arm where she asks for it. She leans against you and begins describing the first sculpture she ever made without someone standing over her shoulder. It had an unfortunate resemblance to an irritated goat, although she had intended a dignified person.{/n}
"Who told you?"
"My aunt. She had an excellent eye and very little patience for a niece explaining what the wood ought to resemble."
{n}You ask whether the goat survived. Gesmerha says somebody bought it after she stopped insisting it was a person.{/n}
"I had forgotten that part," she admits. "There was a useful lesson in it, but I believe we can leave the lesson outside tonight."
{n}You kiss her. She answers slowly, then asks for a story of your own. You choose one that makes her laugh, with her hand resting in yours.{/n}
{n}When it is time to go, she draws you close once more and asks you to put the chair back where it stood before leaving. Her last remark through the closing door makes you laugh all the way across the hall.{/n}''',
      c('[Keep the gentle evening as lovers.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers"))),
    n("open", "Gesmerha", '''"Then no promises. Better a cold answer I can trust than a warm one you talked yourself into."
{n}She pats the place beside her, then asks whether you would prefer to keep the chair.{/n}
"Beside you is comfortable."
"Then sit. I can enjoy the company without demanding that the furniture decide what we call it."
{n}You tell her when you move. She asks about a place you would visit without an army waiting behind you, and listens while you choose an answer. Her own is a workshop belonging to a woman she once quarreled with over a carving neither of them owned.{/n}
"You want to see her again?"
"I want to hear whether she still believes she was right. Then I would like to discover whether I can bear agreeing with her now."
{n}The conversation wanders into travel, bad meals and the strange things remembered from otherwise unpleasant days. When you leave, there is no unfinished declaration waiting to ambush the goodbye. She says she enjoyed the evening and asks you to return before she goes.{/n}''',
      c('[Keep the closeness without a romantic promise.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_open"))),
    n("friends", "Gesmerha", '''"Then you may begin by telling me something entirely useless. I have been given useful information since dawn."
{n}You offer an account of a disagreement about a meal that neither participant had tasted. Gesmerha listens gravely until you reach the explanation for why nobody was willing to taste it first.{/n}
"That is not useless," she protests. "I know at least three people who would benefit from hearing it."
"We can change their names before telling them."
"They would recognize the sensible person immediately and fail to notice the resemblance to anyone else. I shall save myself the trouble."
{n}Her own story concerns a visiting trader who tried to sell a musical instrument by insisting it was easier to admire before hearing it played. She imitates his offended reply when somebody took him at his word and asked him not to demonstrate.{/n}
{n}You spend the evening laughing often enough that one knock at the door becomes a tentative apology from someone who decides his question can wait. Gesmerha tells you who it was after his steps have retreated; she recognized his voice in the apology.{/n}
"A promising development," she says. "Perhaps he has found it himself."
{n}When you leave, she asks for another such evening if the road permits it. You are pleased to have one worth remembering already.{/n}''',
      c('[Keep the friendship and the private evening.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_friends"))),
    # The aftermath of the night, its own beat after the cut (Sol 2026-09-30, Directive 12).
    n("after_night", "Gesmerha", '''{n}Later, with her head on your chest, she complains that the pillow has escaped again. You find it on the floor. Her thanks turns into another kiss, slower than the first ones.{/n}
"I wanted this," she says quietly. "Since the box. Since before the box. I stopped pretending otherwise somewhere on the road back from Sella's."
{n}In the morning she is up before you, dressed, sitting on the chest by the door with her staff across her knees. She tells you, with great satisfaction, that the door has turned away its first visitor of the day, that it was Halvek, and that he will never ask her about the smallest pattern again.{/n}''',
      c('[Stay for breakfast.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers", "gesmerha.night_shared"))),
    # The same morning for the slower lover's first night: its terminal choice records the commit.
    n("after_first_night", "Gesmerha", '''{n}Later, with her head on your chest, she complains that the pillow has escaped again. You find it on the floor. Her thanks turns into another kiss, slower than the first ones.{/n}
"I wanted this," she says quietly. "Since the box. Since before the box. I stopped pretending otherwise somewhere on the road back from Sella's."
{n}In the morning she is up before you, dressed, sitting on the chest by the door with her staff across her knees. She tells you, with great satisfaction, that the door has turned away its first visitor of the day, that it was Halvek, and that he will never ask her about the smallest pattern again.{/n}''',
      c('[Stay for breakfast.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers", "gesmerha.committed", "gesmerha.night_shared"))),
    # The late commit's own threshold: the slower lover who asks to stay after the first kiss (Sol 2026-09-30, pattern 3).
    n("first_night", "Gesmerha", '''{n}She goes still. Then she laughs, low, and does not let go of your hand.{/n}
"The chair was never going to hold you. I put it there so I would have something to refuse."
{n}She pulls you down beside her, and then beneath her. Her shift comes off over her head in one motion; your shirt takes longer, because she will not let you help and her fingers keep stopping to read what they find. The bed was built for one sleeping woman and says so. She tells it to be quiet.{/n}
"There," she says, when there is nothing left between you but the blanket. "Now I know what I am getting."
{n}She settles astride you with the blanket around both your shoulders, bends to take your mouth, and reaches down between you.{/n}''',
      c('[Continue]', "after_first_night")),
], "gesmerha.work_settled")

s("the_work_left_finished", "A place in the days ahead", '"Is everything ready for you to leave?"', [
    n("start", "Gesmerha", '''{n}The chest is shut. Gesmerha sits beside it with her staff across her knees and a small bundle at her feet. The three carvings have gone to their makers. The long box has not returned.{/n}
"Everything I have agreed to carry," she says. "Someone will remember another indispensable object once I stand up. I have decided to be selective about believing them."
{n}She asks you to describe the doorway. When you tell her it is clear, she smiles.{/n}
"A fine achievement. We ought to have celebrated it while everybody was still here."
"Are you glad the work is finished?"
"Yes. I am also waiting for someone to tell me I have forgotten an obligation. A tiresome habit. I should like it to arrive late enough that I am already enjoying the road."
{n}She feels for the tie on her bundle and checks it once.{/n}
"Before we go, I want to speak about where our own days belong in all this."''',
      c('[Sit beside her for the conversation.]', "future"),
      c('[Ask to return before she sets out, when you can give the answer time.]', abort=True)),
    n("future", "Narrator", '''{n}Gesmerha shifts her staff so there is room beside her. When you sit, she turns toward the sound rather than reaching across the space unannounced.{/n}''',
      c('"You said at court that you would seek another home."', "migration", requires=("gesmerha.heard_migration",)),
      c('"You spoke of sheltering in the forests and mountain trails."', "shelter", requires=("gesmerha.heard_staying",), forbids=("gesmerha.heard_migration",)),
      c('"Where do you want your own work to go next?"', "unreported", forbids=("gesmerha.heard_migration", "gesmerha.heard_staying"))),
    n("migration", "Gesmerha", '''"Yes. Sorting these things has not changed that. We did not come back here to discover that the old place had become easy to live in."
"Have you chosen where to go?"
"Not a new home for everyone. I know which people are traveling with me for the first stretch. I know what they have chosen to carry. After that we will have to ask questions of people who do not owe us comforting answers."
{n}She rests her palm on the lid beside her.{/n}
"I shall miss things I was tired of tending. I expect to complain about a new place by comparing it with something I disliked here. If you hear me doing that, ask for the rest of the comparison."
"Will you tell me?"
"After defending myself for a little while. I am trying to make the warning accurate."
{n}Her smile fades gently.{/n}
"I want you in that life. I cannot tell you which roof it will be under. I can tell you what I offer."''', c('[Ask her to say it.]', "offer")),
    n("shelter", "Gesmerha", '''"Yes. We can leave the houses without giving every part of this land to what has hurt us. I have not promised that we will return to these same rooms and find the old days waiting."
"What do you want to restore?"
"Places where people can work without wondering which alarm will interrupt the next hour. Songs they sing because they want to, not because somebody has demanded proof that Sarkoris remains alive. I want a workshop with a roof I know how to describe without beginning with the leaks."
{n}She laughs softly.{/n}
"I have begun with a box delivered to its owner and a lesson somebody else can teach. It is a small beginning for a person who has made several large speeches. I am pleased with it."
"And the days beyond that?"
"Will need work of their own. I want you in them. Not as one more duty to carry for the clan. As the reason I set the duties down, some evenings."''', c('[Ask what she wants your place to be.]', "offer")),
    n("unreported", "Gesmerha", '''"Where people will use it. I have spent too long imagining that if every tool leaves this hall, something essential will disappear between the door and the next place it is put down."
{n}She traces the seam of her bundle.{/n}
"I have not given you a plan for the whole clan. I will not make one out of this private conversation. There are people who have to speak for themselves, and questions that do not become settled because I am tired of hearing them."
"You can tell me what you want."
"A place to work. People willing to learn and willing to leave me alone when I ask. Some mornings I do not begin by counting what everyone needs from me."
{n}She tilts her face toward your voice.{/n}
"And time with you. As simple as that. The arranging will be hard enough without my making the wish hard too."''', c('[Ask her to say what she wants between you.]', "offer")),
    n("offer", "Gesmerha", '''"I want to keep having you. I want to tell you when I miss you, and to throw you out when I have work I mean to finish first. And I want the same from you, or I will know you are being polite, and I hate polite."
{n}She holds out her hand, and you put yours into it.{/n}
"When there is word worth sending, I will leave it where a carrier I trust can find it. I will not send a boy into demon country to prove I remember your face. When we meet, it will be because the two of us made the road, not because somebody else arranged it."
"That may mean waiting."
"Yes. Waiting and being forgotten feel the same until the answer comes. I have learned the difference. It did not come cheap."
{n}Her thumb moves once across the back of your hand.{/n}
"What will you keep?"''',
      c('"You. As my lover, wherever the roads go."', "lovers", requires=("gesmerha.late_lovers",)),
      c('"Our friendship, and every visit the road allows."', "friends", requires=("gesmerha.late_friends",)),
      c('"This, as it is. No promises made of it."', "open", requires=("gesmerha.late_open",)),
      c('"I can\'t promise you anything more. Better to end it here, cleanly."', "part")),
    n("lovers", "Gesmerha", '''"Then that is what I choose too. I will not pour my life into whatever space is left once yours is arranged. And do not come to me with nothing of your own left to tell."
"We will have plenty to argue over."
"Good. It would be a disgrace to find I had fallen in love with someone whose opinions melted when I kissed them."
{n}She hears the silence after her words and smiles into it.{/n}
"Yes," she says. "I meant that. Breathe before you answer."
{n}You tell her what she is to you. She listens with your hand between hers, then pulls you in by it and kisses you until a sound at the far doorway reminds you both where you are. She laughs against your cheek and rests her forehead near yours for one more breath.{/n}
"I want another ordinary morning with you. Not a farewell worth singing about. A morning."
"So do I."
{n}When she lets go, you set her staff in her hand and turn her toward the doorway. She lifts her bundle herself. At the threshold she turns back toward your last steps and tells you she will miss the sound of them.{/n}''',
      c('[Keep the love and the practical promise you made together.]', flags=("gesmerha.late_complete", "gesmerha.future_lovers", "gesmerha.committed"))),
    n("friends", "Gesmerha", '''"Then come with a story when you can. If you arrive with a useful question, I may even answer it. But I would rather not find, some year, that usefulness was all we had left."
"I shall try to be an inconvenient guest."
"Moderation. I have known people with a natural gift for it, and I would not ask you to compete."
{n}She laughs, squeezes your hand and lets go. You tell her where her staff rests, then describe the clear way to the door.{/n}
"I am glad we finished the box," she says. "I am glad we had an evening afterward. Two different pleasures. I mean to keep both."
{n}She lifts her bundle. You walk together as far as the doorway, where Halvek has come to ask whether she is ready. She tells him yes, then turns back toward your voice for the goodbye.{/n}''',
      c('[Keep the friendship and the visits you will try to arrange.]', flags=("gesmerha.late_complete", "gesmerha.future_friends"))),
    n("open", "Gesmerha", '''"Then we shall keep knowing one another. I will not explain your answer to the people who would enjoy predicting what it must become."
"Would they believe you?"
"Some. Others would decide that I had become mysterious. That might improve several meetings I would otherwise have to attend."
{n}Her laughter makes the parting easier without making it unimportant. She releases your hand and feels for the tie of her bundle.{/n}
"Ask for me when you can. If I am elsewhere, let the message wait somewhere safe. I will answer when I have an answer to give."
{n}You tell her where her staff lies. She stands, adjusts the bundle and waits while you describe the doorway. Before leaving she asks for another harmless story next time, including whatever unflattering detail you are tempted to leave out.{/n}
{n}You promise the detail. Neither of you promises what it must become.{/n}''',
      c('[Keep the open relationship without inventing another answer.]', flags=("gesmerha.late_complete", "gesmerha.future_open"))),
    n("part", "Gesmerha", '''{n}Her hand loosens around yours. She draws it back and settles both hands on her bundle.{/n}
"Then I am glad you have said so before I began choosing the words for your next welcome."
"I did not want to make the work we shared seem like a mistake."
"It was not. Sella has her box. I have days I wanted to spend with you. You cannot return them, and I am not asking you to."
{n}She takes a breath, then asks where her staff lies.{/n}
"I will not want another private visit for a long while. Do not send me explanations. I will know where to find you if I want one."
"I understand."
"Good."
{n}You tell her the way to the doorway. She lifts her bundle, waits until you say the path is clear and leaves the hall without asking you to make the parting easier by changing your answer.{/n}''',
      c('[Respect the ending and the time she requested.]', flags=("gesmerha.late_complete", "gesmerha.closed"))),
], "gesmerha.private_evening_kept")


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue", **extra):
    SCENES.append(scene("gesmerha.late_ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Gesmerha")], Relationship="gesmerha", last=99,
        requires=("gesmerha.late_complete", *requires), forbids=forbids,
        **{k: dict(v) if isinstance(v, dict) else v for k, v in extra.items()}))


LIVING_BLOCK = ("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice")
# A native Trickster ending after the sacrifice brings the Commander back (trickster.commander_back, trickster_world): the
# living endings stand and the mourning page yields (Sol 2026-09-30, INT; ledger row 16).
SURVIVED = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})
ending("lovers", "Ordinary mornings", '''{n}Gesmerha and the Commander kept each other, across messages that came late, plans that changed and a standing quarrel about whether half a day can honestly be called a short visit. Neither built a life around waiting for the other to be free.{/n}
{n}When they met, there was work to hear about and company that did not have to earn its place by being useful. Gesmerha learned the Commander's step in more than one doorway. Some days she finished the cut under her hand before she turned toward it. Some days she put the knife down at once, and the Commander learned what the difference meant.{/n}
{n}They had ordinary mornings: a cup mislaid, a kiss interrupted, a story told badly enough that laughter improved it. Gesmerha stayed blind, proud of her work and thoroughly inconvenient about the things she loved. The Commander was among them.{/n}''', requires=("gesmerha.future_lovers",), forbids=LIVING_BLOCK, **SURVIVED)
ending("friends", "A story worth bringing", '''{n}Gesmerha's friendship with the Commander outlasted two lives that did not often lead to the same door. Messages waited. Visits were fixed and unfixed. When they met, she always asked for the part of the story the Commander had thought too ordinary to tell.{/n}
{n}The box stayed Sella's. What the learners made from its lessons belonged to their own hands. Gesmerha could still be heard explaining why a certain curve should be cut deeper, and laughing when somebody reminded her that the curve had begun as a mistake.{/n}
{n}The Commander knew when she wanted company and when she wanted to be left alone with a hard piece of wood. She never had to explain which.{/n}''', requires=("gesmerha.future_friends",), forbids=LIVING_BLOCK, **SURVIVED)
ending("open", "The answer they kept", '''{n}Gesmerha and the Commander went on finding each other when the road allowed it, and made no promise of it. When people in the clan told her what it would come to in the end, she told them to go and carve their own futures and leave hers on the bench.{/n}
{n}There were visits, stories and several quarrels worth starting again. She asked about the places the Commander had seen, and in return told of people who had misunderstood a simple commission in ways no one could have foreseen.{/n}''', requires=("gesmerha.future_open",), forbids=LIVING_BLOCK, **SURVIVED)
ending("closed", "What had been finished", '''{n}The Commander and Gesmerha parted once the work they had shared was done. Sella's box had reached its owner. The evenings had been wanted while they lasted, and the parting did not unmake them.{/n}
{n}Gesmerha kept the distance she had asked for. She sent no message to make the parting easier on the one who would read it. When she thought of the Commander, she remembered certain words and a certain step, some with pleasure and some with an ache she did not care to explain to anyone.{/n}''', requires=("gesmerha.closed",), forbids=("gesmerha.dead", "inhuman", "demon", "devil"))
ending("loss", "The work beyond her hands", '''{n}Gesmerha died. The people she had taught went on making things with their own hands. Their work was not an answer from her, but sometimes a familiar curve made someone stop and remember the exact impatience with which she had explained it.{/n}
{n}The Commander remembered other things: a joke through a closing door, her hand held out to be met, the pause before she said something she had decided mattered. She had given a misplaced stool an address and then cleared the chest so the Commander could sit. The complaint and the welcome came back together. There would be no next visit to hear them again.{/n}
{n}Sella kept the box. The death did not make the inheritance anyone else's.{/n}''', requires=("gesmerha.dead",))
ending("changed", "A familiar voice was not enough", '''{n}What the Commander became ended the welcome Gesmerha had offered. Wintersun had knelt for a generation to a pleasing voice, and she would not let a familiar one tell her what to accept.{/n}
{n}She remembered the evenings, some of which she would still have lived again. Remembering them did not oblige her to open the door to what now stood behind it.{/n}''', requires=("inhuman",), forbids=("gesmerha.dead",))
ending("demon", "The invitation withdrawn", '''{n}Gesmerha would not let her love for the Commander become a welcome for the Commander's demonic power. She had watched a clan teach itself to smile at cruelty because it came in a voice they wished to trust. She would not learn that lesson a second time in her own bed.{/n}
{n}The evenings they had shared did not become false. She could miss them and still refuse another. She sent her answer word for word, with no promise that time would soften it.{/n}''', requires=("demon",), forbids=("gesmerha.dead", "inhuman"))
ending("devil", "No claim beyond the words", '''{n}The Commander's infernal path did not acquire Gesmerha through anything she had said before. She had given her time and her affection, not her name to a contract, and she would not have her own words turned into somebody else's title to her life.{/n}
{n}She gave her refusal plainly. There was work she meant to finish and people she meant to see, and arguing the point until a devil agreed with her was not among her duties.{/n}''', requires=("devil",), forbids=("gesmerha.dead", "inhuman", "demon"))
ending("ascent", "News without a familiar answer", '''{n}News of the Commander's ascent came to Gesmerha by a messenger who seemed to expect her to know what a god would want from the people left behind. She told him she had known someone who could sit beside her and be corrected about where the chair went. She would not make up the next answer for him because the question had grown grand.{/n}
{n}She kept the farewell as it had been. Whatever place she might have in the new power's existence would need a new knock at the door. Until one came, she had work of her own, and people who could still knock.{/n}''', requires=("ascended",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil"))
ending("sacrifice", "The ordinary morning she wanted", '''{n}Gesmerha heard how the Commander had died. She let the messenger tell the part he knew, and stopped him when he began explaining what she ought to find comforting in it.{/n}
{n}She had wanted another ordinary morning. What came back to her was small: the pressure of the Commander's hand while they talked, the weight of her own bundle when she lifted it to go. Those came back more clearly than anything the messenger said about the battle.{/n}
{n}For a time she would not tell the stories the Commander had liked. Later she told one again. Someone laughed at the right place, and it hurt enough that she had to stop before she began another. That night she said the Commander's name into the fire in the old way, so that the ancestors would know the step.{/n}''', requires=("sacrifice",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "trickster.commander_back"))
ending("aeon", "A life without that visitor", '''{n}In the history remade without the Worldwound, that Commander never came to share Gesmerha's afternoons. The disputes, the journeys and the private answers that followed that meeting were not left behind as promises she owed an absent traveler.{/n}
{n}Whatever work her hands found in that world belonged to the life she lived there. No erased farewell decided its ending for her.{/n}''', owner="AeonEpilogue")


SCENES.append(scene("gesmerha.late_ending_unfinished", "The visit after the return", "Epilogue", 0, "", [
    n("start", "Narrator", '''{n}There had been another meeting in Wintersun. Gesmerha had sat behind a chest of things waiting to be sorted and asked the Commander to describe the stool someone had left in her path. After the long absence, the little complaint had made her presence wonderfully ordinary.{/n}
{n}The Commander remembered her moving the folded blanket to make room on the chest beside her. She had wanted company among the bundles and the arguments. When another journey failed to bring another afternoon, it was that ordinary welcome the Commander found themself wanting to hear again.{/n}''', portrait="Gesmerha")], Relationship="gesmerha", last=99,
    requires=("gesmerha.late_arrived",), forbids=(*LIVING_BLOCK, "gesmerha.late_complete"),
    ForbidOverrides=dict(SURVIVED["ForbidOverrides"])))


# The companion who reacts to the night (Sol 2026-09-30, BEL): Ulbrig, a Sarkorian, on a Sarkorian carver.
SCENES.append(reaction("Ulbrig", "gesmerha.react.ulbrig_night", ("gesmerha.night_shared", "ulbrig.in_party"),
    '''"The Wintersun woodshaper barred her door on you, they're saying, and half the hall heard her bed complain about it." {n}Ulbrig turns his mug a full circle on the table before he goes on.{/n} "My grandmother used to say a carver takes your measure before she takes you to bed, the way she'd measure a trunk before the first cut. So she's decided what's in you, warchief. Try not to make a liar of her."''',
    answer_list="0a50c9c878844ed4a69b8d6131304c5e", forbids=("ulbrig.dead", "ulbrig.kicked_out"), chapter=5, last=5, delay=24,
    entry='"About the woodshaper from Wintersun..."'))


def integrate(payload):
    payload.setdefault("Etudes", {}).update(ETUDES)
    for item in payload["Scenes"]:
        if item["Id"] in ("gesmerha.ending_living_reunion", "gesmerha.ending_unmet_again", "gesmerha.the_voice_at_court"):
            flag = "gesmerha.late_arrived"
        else:
            flag = "gesmerha.late_complete" if item["Id"].startswith("gesmerha.ending_") else None
        if flag and flag not in item["Forbids"]:
            item["Forbids"].append(flag)
