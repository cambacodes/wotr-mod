"""Living Chapter 5 Gesmerha visits at her native post-resolution Wintersun contact.

Packing, survivors and later affection are authored developments.
Native chapter, quest, leadership and death state remain read-only.
"""
from story_format import c, n, scene
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
"I dislike losing the convenience. I accept the arrangement."
"Six days for a loan," Sella says. "Longer only if I agree before the carrier leaves. If you cannot promise the return, ask for a different time."
"And if you move farther away?"
"Then I will tell you where a message can reach me, if there is such a place. I cannot give you a road I have not traveled."
{n}Gesmerha rests her empty hands against each other.{/n}
"Then I shall teach the curve from what I know. I will tell them why it may differ from the old piece. There is work enough in that."
"You sound as though I have deprived you of something," Sella says.
"You have. Something I enjoyed using. You have also offered to lend it under terms I can understand. I can be disappointed without withdrawing my answer."
{n}Sella exhales, a small sound that seems to surprise Halvek more than the argument did.{/n}
"Good. I should like to take the box home without being congratulated for allowing everybody to become wiser."
"Then let us make the trip useful instead," Gesmerha says. "There are other things waiting with it."''', c('[Keep the limited-loan agreement.]', "loan_end")),
    *[n(id, "Gesmerha", '''{n}Sella and Halvek leave together after agreeing where the box will be taken. Gesmerha waits for their steps to pass beyond the doorway before reaching for her staff.{/n}
"Will you walk with me as far as the door? I know the way. I would like the company."
{n}You offer your arm where she asks for it. She takes it lightly, testing the floor ahead with her staff rather than letting you draw her around the stool.{/n}
"I wanted you to agree with me," she says as you reach the threshold. "At the beginning. I had a very satisfactory account prepared of why I ought to keep everything."
"You might have argued it."
"I still could. That is the irritating part. I have chosen an answer while the other arguments remain perfectly capable of waking me at night."
{n}Cool air reaches the hall. She turns her face toward it and loosens her grip on your arm.{/n}
"There are worse ways to spend an afternoon than discovering I can bear that. There are also more enjoyable ones. I should like to arrange one with you before I go."''',
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
"He began composing the request. I have asked to hear it only if he wants help. I am trying not to acquire another duty merely because I can perform it more quickly."
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
"The box is hers. If a loan becomes inconvenient, we shall ask for a different time. I have stopped planning my whole workshop around the expectation that somebody else must remain conveniently near it."''', c('[Ask what she wants her own workshop to become.]', "hers")),
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
    n("start", "Gesmerha", '''"Come in. Close the door, then tell me whether you have brought an audience small enough to hide in your pockets."
{n}Gesmerha sits on the edge of a low bed. Her boots stand beneath it, heels toward the wall. A lamp burns on a chest near the door; its light reaches the long hair she has loosened from its tie.{/n}
"No audience," you tell her.
"Good. There is a chair two steps to your left. If you want it closer, tell me before you move it."
{n}You describe where you put the chair. She turns toward the scrape, then settles with her feet resting on a folded blanket.{/n}
"I have been waiting for the last knock. Someone asked where we put the smallest pattern. I told him to ask the person who had put it away. Then he remembered that was himself."
"Did you forgive him?"
"I shall consider it tomorrow. Tonight I have closed the door."''',
      c('"May I sit beside you and kiss you?"', "lover", requires=("gesmerha.lover",)),
      c('"I still want to explore what might be between us."', "slow", requires=("gesmerha.campaign_slow",), forbids=("gesmerha.evening_as_friends",)),
      c('"I am glad we have kept an evening for our friendship."', "friends", requires=("gesmerha.campaign_friends",), forbids=("gesmerha.evening_as_friends",)),
      c('"I have come for the evening we agreed to spend as friends."', "friends", requires=("gesmerha.evening_as_friends",)),
      c('"I cannot keep the evening clear yet. May I return?"', abort=True)),
    n("lover", "Gesmerha", '''"Then come where I can reach you. I have thought about it too."
{n}You tell her when you stand and where you sit beside her. She offers her hand, follows your arm to your shoulder and laughs softly when her fingers encounter the fastener near your collar.{/n}
"That part is determined to be remembered."
"Shall I move it?"
"Please. I should like to touch you without acquiring a lesson in metalwork."
{n}You loosen it and set it on the chest, telling her where. When you return to her side, she lifts her hand to your cheek.{/n}
"May I kiss you?"
"Yes."
{n}She draws you close. The kiss begins gently and becomes less tentative when your hand settles where she guides it against her waist. When you part, she remains near enough that you feel her laugh before hearing it.{/n}
"There. An excellent use for the door."
{n}She asks what you want from the rest of the evening.{/n}''',
      c('"I want to stay close, and see where we both want the evening to go."', "night"),
      c('"Your company and a few more kisses. I would like to take the rest slowly tonight."', "gentle")),
    n("slow", "Gesmerha", '''{n}Gesmerha rests her hands on the blanket beside her.{/n}
"So do I. I have enjoyed these days, including the parts in which you did not agree with the answer I had hoped to give."
"I would like more than good afternoons."
"Then tell me what you mean. I have imagined several answers and would prefer to hear yours before becoming attached to the wrong one."
{n}You tell her about the closeness you want. She listens, asks one question about what you expect when the two of you are apart, and gives you time to answer.{/n}
"I cannot promise to remain wherever it is easiest to find me," she says. "There will be other people I care for, work I choose and days I want for myself. You have people of your own. I will not ask you to make their answers for them."
"I want us to choose our time together honestly."
"Good. I would also like to kiss you. I have managed to make that sound like the least difficult part of the discussion, and now I am discovering how much I want your answer."''',
      c('"Yes. I want to be your lover, with the freedom and care we have discussed."', "first_kiss"),
      c('"I still need time. I want this evening without promising romance."', "open"),
      c('"I want to keep knowing you as a friend."', "friends")),
    n("first_kiss", "Gesmerha", '''"Then sit beside me. Tell me where your hand is."
{n}You do. She takes it and draws it gently toward her shoulder, letting you know when you are near enough. Her other hand finds your cheek. She pauses until you lean toward her, then kisses you with a warmth that makes the carefully prepared first words disappear.{/n}
"Was that the answer you imagined?" you ask when she draws back.
"No. The imagined one had a very polished remark afterward. I have forgotten it entirely."
"You could take a moment."
"I would rather use the moment differently."
{n}She kisses you again. When she rests against you afterward, she asks you not to move the blanket under her feet; she has finally found a comfortable place for them.{/n}
{n}You remain together, learning how she likes to be held and telling her what you enjoy in return. She asks for another kiss before either of you begins speaking about tomorrow.{/n}''',
      c('[Keep the new relationship and an unhurried first evening.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers", "gesmerha.committed"))),
    n("night", "Gesmerha", '''"Then stay. Ask me when you want something different from what we are doing. I intend to ask you."
{n}She reaches back to move the pillow, tells you where she is putting it and draws you with her only after you answer. The narrow bed obliges you both to negotiate a comfortable place. At one point she begins laughing so hard that the kiss you were attempting becomes impossible.{/n}
"You sound surprised," she says.
"I had imagined more elegance."
"So had I. We can accuse the bed. It cannot defend itself."
{n}You try again with less concern for the imagined version. Her hand moves through your hair, then rests against the back of your neck. She tells you what feels good and what catches against a tender place, plainly enough that you can answer without guessing.{/n}
{n}The room grows quiet around the small sounds you make together. When she asks whether you want to stay for the night, you say yes. She draws the blanket nearer and asks you to describe which things you have put beside the bed so neither of you has to discover them with a bare foot.{/n}
{n}Later, with her head resting against you, she complains that the pillow has escaped again. You find it, and her thanks becomes another kiss.{/n}
"I wanted this," she says softly. "I am pleased we did not wait for a room without inconveniences."
{n}In the morning she wakes before you and tells you, with considerable satisfaction, that the door has successfully refused its first visitor.{/n}''',
      c('[Keep the night you freely chose together.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers"))),
    n("gentle", "Gesmerha", '''"Then sit close enough that I need not keep finding the distance."
{n}You settle beside her with your arm where she asks for it. She leans against you and begins describing the first sculpture she ever made without someone standing over her shoulder. It had an unfortunate resemblance to an irritated goat, although she had intended a dignified person.{/n}
"Who told you?"
"My aunt. She had an excellent eye and very little patience for a niece explaining what the wood ought to resemble."
{n}You ask whether the goat survived. Gesmerha says somebody bought it after she stopped insisting it was a person.{/n}
"I had forgotten that part," she admits. "There was a useful lesson in it, but I believe we can leave the lesson outside tonight."
{n}You kiss her. She answers slowly, then asks for a story of your own. You choose one that makes her laugh, with her hand resting in yours.{/n}
{n}When it is time to go, she draws you close once more and asks you to put the chair back where it stood before leaving. Her last remark through the closing door makes you laugh all the way across the hall.{/n}''',
      c('[Keep the gentle evening as lovers.]', flags=("gesmerha.private_evening_kept", "gesmerha.late_lovers"))),
    n("open", "Gesmerha", '''"Then no promise of romance. I would rather hear that here than carry away a warmer answer you were trying to make yourself believe."
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
"I want room in that life for you. I cannot name the house while I say it. I can still tell you what I am offering."''', c('[Ask her to say it.]', "offer")),
    n("shelter", "Gesmerha", '''"Yes. We can leave the houses without giving every part of this land to what has hurt us. I have not promised that we will return to these same rooms and find the old days waiting."
"What do you want to restore?"
"Places where people can work without wondering which alarm will interrupt the next hour. Songs they sing because they want to, not because somebody has demanded proof that Sarkoris remains alive. I want a workshop with a roof I know how to describe without beginning with the leaks."
{n}She laughs softly.{/n}
"I have begun with a box delivered to its owner and a lesson somebody else can teach. It is a small beginning for a person who has made several large speeches. I am pleased with it."
"And the days beyond that?"
"Will need work of their own. I want room in them for you. That is not a request that you become another duty I must carry to prove I deserve the people who trust me."''', c('[Ask what she wants your place to be.]', "offer")),
    n("unreported", "Gesmerha", '''"Where people will use it. I have spent too long imagining that if every tool leaves this hall, something essential will disappear between the door and the next place it is put down."
{n}She traces the seam of her bundle.{/n}
"I have not given you a plan for the whole clan. I will not make one out of this private conversation. There are people who have to speak for themselves, and questions that do not become settled because I am tired of hearing them."
"You can tell me what you want."
"A place to work. People willing to learn and willing to leave me alone when I ask. Some mornings I do not begin by counting what everyone needs from me."
{n}She tilts her face toward your voice.{/n}
"And time with you. I should like that wish to remain simple even when arranging it becomes inconvenient."''', c('[Ask her to say what she wants between you.]', "offer")),
    n("offer", "Gesmerha", '''"I want to keep choosing our time. To tell you when I miss you, and when I have work I would rather finish before being distracted. I want you to tell me the same."
{n}She offers her hand. You describe where yours waits before meeting it.{/n}
"I will leave word where a trustworthy carrier can find me when there is word worth sending. I will not send someone into danger merely to prove I have remembered you. If we choose a visit, I want it arranged between the people actually making the journey."
"That may mean waiting."
"Yes. I have discovered that waiting and being forgotten are different things. I dislike how often they feel alike before there is an answer."
{n}Her thumb moves once across your hand.{/n}
"What do you want to keep?"''',
      c('"I want our life as lovers, with our own work and people still part of it."', "lovers", requires=("gesmerha.late_lovers",)),
      c('"I want to keep our friendship, and make time to visit when we can."', "friends", requires=("gesmerha.late_friends",)),
      c('"I want to keep this closeness without a romantic promise."', "open", requires=("gesmerha.late_open",)),
      c('"I cannot promise another chapter together. I want to end this honestly here."', "part")),
    n("lovers", "Gesmerha", '''"Then that is what I choose too. I will not move every part of my life into the space left after yours is arranged. Nor would I like you to arrive with nothing of your own left to tell me about."
"We will have plenty to disagree over."
"Good. It would be inconvenient to discover I had fallen in love with somebody whose opinions disappeared when I kissed them."
{n}She smiles at the silence after her words.{/n}
"Yes," she says. "I meant that. You may take a breath before answering."
{n}You tell her what she means to you. She listens with your hand between hers, then asks you to come closer. You ask whether she wants a kiss; her answer is immediate.{/n}
{n}The kiss lasts until a sound at the distant doorway reminds you both where you are. Gesmerha laughs against your cheek, then rests her forehead near yours for one more quiet breath.{/n}
"I want another ordinary morning with you," she says. "Not merely a farewell worth remembering."
"So do I."
{n}When she lets go, you place her staff where she asks and tell her which way the doorway lies. She lifts her bundle herself. At the threshold she turns toward your last steps and tells you she will miss the sound.{/n}''',
      c('[Keep the love and the practical promise you made together.]', flags=("gesmerha.late_complete", "gesmerha.future_lovers", "gesmerha.committed"))),
    n("friends", "Gesmerha", '''"Then come with a story when you can. If you arrive with a useful question, I may still answer it, but I would prefer not to find that usefulness has become the whole reason we remember one another."
"I shall try to be an inconvenient guest."
"Moderation. I have known people with a natural gift for it, and I would not ask you to compete."
{n}She laughs, squeezes your hand and lets go. You tell her where her staff rests, then describe the clear way to the door.{/n}
"I am glad we finished the box," she says. "I am glad we had an evening afterward. Those are separate pleasures. I should like to keep remembering both."
{n}She lifts her bundle. You walk together as far as the doorway, where Halvek has come to ask whether she is ready. She tells him yes, then turns back toward your voice for the goodbye.{/n}''',
      c('[Keep the friendship and the visits you will try to arrange.]', flags=("gesmerha.late_complete", "gesmerha.future_friends"))),
    n("open", "Gesmerha", '''"Then we shall keep knowing one another. I will not explain your answer to the people who would enjoy predicting what it must become."
"Would they believe you?"
"Some. Others would decide that I had become mysterious. That might improve several meetings I would otherwise have to attend."
{n}Her laughter makes the parting easier without making it unimportant. She releases your hand and feels for the tie of her bundle.{/n}
"Ask for me when you can. If I am elsewhere, let the message wait somewhere safe. I will answer when I have an answer to give."
{n}You tell her where her staff lies. She stands, adjusts the bundle and waits while you describe the doorway. Before leaving she asks for another harmless story next time, including whatever unflattering detail you are tempted to leave out.{/n}
{n}You promise the detail. Neither of you promises what the relationship must become.{/n}''',
      c('[Keep the open relationship without inventing another answer.]', flags=("gesmerha.late_complete", "gesmerha.future_open"))),
    n("part", "Gesmerha", '''{n}Her hand loosens around yours. She draws it back and settles both hands on her bundle.{/n}
"Then I am glad you have said so before I began choosing the words for your next welcome."
"I did not want to make the work we shared seem like a mistake."
"It was not. Sella has her box. I have days I wanted to spend with you. You cannot return them, and I am not asking you to."
{n}She takes a breath, then asks where her staff lies.{/n}
"I will need time before I know whether I want another private visit. Do not send explanations until I have had it."
"I will respect that."
"Thank you."
{n}You tell her the way to the doorway. She lifts her bundle, waits until you say the path is clear and leaves the hall without asking you to make the parting easier by changing your answer.{/n}''',
      c('[Respect the ending and the time she requested.]', flags=("gesmerha.late_complete", "gesmerha.closed"))),
], "gesmerha.private_evening_kept")


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("gesmerha.late_ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Gesmerha")], Relationship="gesmerha", last=99,
        requires=("gesmerha.late_complete", *requires), forbids=forbids))


LIVING_BLOCK = ("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended", "sacrifice")
ending("lovers", "Ordinary mornings", '''{n}Gesmerha and the Commander kept the relationship they had chosen. It took messages, changed plans and an occasional argument about whether a person could reasonably call something a short visit when half a day had already passed. Neither arranged an entire life around waiting for the other to become available.{/n}
{n}When they met, there was work to hear about and company that did not have to justify itself by being useful. Gesmerha learned the sound of the Commander's arrival in more than one doorway. Sometimes she finished the cut beneath her hand before turning toward it. Sometimes she set the knife down at once, and the difference was a pleasure the Commander learned to recognize.{/n}
{n}They had ordinary mornings together. A misplaced cup, an interrupted kiss, a story told badly enough to be improved by laughter. Gesmerha remained blind, proud of her work and capable of being thoroughly inconvenient about the things she loved. The Commander was among them.{/n}''', requires=("gesmerha.future_lovers",), forbids=LIVING_BLOCK)
ending("friends", "A story worth bringing", '''{n}Gesmerha's friendship with the Commander survived the practical inconvenience of two lives that did not always lead toward the same door. Messages waited. Visits were arranged and sometimes rearranged. When they met, Gesmerha asked for the part of the story the Commander had considered too ordinary to include.{/n}
{n}The box remained Sella's. What the learners made from its lessons belonged to their own hands. Gesmerha could still be heard explaining why a particular curve should be cut differently, then laughing when somebody reminded her how much of its history had begun with a mistake.{/n}
{n}The Commander had a place among the people who knew when she wanted company and when she wanted to finish a difficult piece. It was a friendship with enough affection to make both answers easy to hear.{/n}''', requires=("gesmerha.future_friends",), forbids=LIVING_BLOCK)
ending("open", "The answer they kept", '''{n}Gesmerha and the Commander continued to make time for one another when the road permitted it. The relationship remained the open, unpromised closeness they had named. Neither treated another person's prediction as a debt the two of them must eventually pay.{/n}
{n}There were visits, stories and several arguments worth beginning again. Gesmerha asked about the places the Commander had seen and supplied her own account of people who had misunderstood an apparently simple commission. The visits mattered without becoming evidence for an answer neither had given.{/n}''', requires=("gesmerha.future_open",), forbids=LIVING_BLOCK)
ending("closed", "What had been finished", '''{n}The Commander and Gesmerha parted after settling the work they had shared. Sella's box had reached its owner. The private evenings had been wanted while they lasted. Their ending did not undo either fact.{/n}
{n}Gesmerha took the time she had asked for. She did not send a message merely to make the parting easier for the person receiving it. When she thought of the Commander, she remembered particular words and sounds, some with pleasure and some with a pain that did not require another explanation.{/n}''', requires=("gesmerha.closed",), forbids=("gesmerha.dead", "inhuman", "demon", "devil"))
ending("loss", "The work beyond her hands", '''{n}Gesmerha died. The people she had taught went on making things with their own hands. Their work was not an answer from her, but sometimes a familiar curve made someone stop to remember the exact impatience with which she had explained it.{/n}
{n}The Commander remembered more private things: a joke through a closing door, her hand waiting to be met, the pause before she said something she had decided mattered. She had given a misplaced stool an address, then made room on the chest for the Commander to sit. The complaint and the welcome returned together. There would be no next visit to hear them again.{/n}
{n}Sella kept the box. The loss did not make the inheritance belong to someone else.{/n}''', requires=("gesmerha.dead",))
ending("changed", "A familiar voice was not enough", '''{n}The Commander's transformation ended the welcome Gesmerha had been willing to offer. She had learned too much about comforting appearances to let a familiar voice decide what she must accept.{/n}
{n}She remembered the time they had chosen, including the moments she would still have been glad to live again. Remembering them did not oblige her to make the same invitation to the being the Commander had become. Her refusal was her own.{/n}''', requires=("inhuman",), forbids=("gesmerha.dead",))
ending("demon", "The invitation withdrawn", '''{n}Gesmerha would not let her affection for the Commander become a welcome for the Commander's demonic power. She had seen a clan teach itself to accept cruelty through a voice it wished to trust. She had no desire to repeat the lesson in a more private room.{/n}
{n}The evenings they had shared did not become false. She could miss them and still refuse another. When she gave that answer, she asked for it to be carried accurately, without an assurance that time would persuade her to change it.{/n}''', requires=("demon",), forbids=("gesmerha.dead", "inhuman"))
ending("devil", "No claim beyond the words", '''{n}The Commander's infernal path did not acquire Gesmerha through anything she had promised before. She had offered time and affection she could choose. She would not allow those words to become another person's authority over the life she meant to lead.{/n}
{n}She gave her refusal plainly. There was work she still wanted to finish, and people she still wanted to see. Explaining the refusal until a powerful listener approved of it was not among her obligations.{/n}''', requires=("devil",), forbids=("gesmerha.dead", "inhuman", "demon"))
ending("ascent", "News without a familiar answer", '''{n}News of the Commander's ascent reached Gesmerha through a messenger who seemed to expect her to know what a god would want from the people left behind. She told him she had known someone who could sit beside her and be corrected about the position of a chair. She would not invent the next answer merely because the question had become magnificent.{/n}
{n}She kept the memory of their farewell. Whatever place she might have in the new power's existence would need a new invitation. Until one came, she had work of her own and people who could still knock at the door.{/n}''', requires=("ascended",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil"))
ending("sacrifice", "The ordinary morning she wanted", '''{n}Gesmerha heard how the Commander had died. She asked the messenger to tell her the part he knew, then stopped him when he began explaining what she ought to find comforting about it.{/n}
{n}She wanted another ordinary morning. She remembered the pressure of the Commander's hand while they spoke, and the weight of her own bundle when she lifted it to go. Those small things returned to her more clearly than the messenger's account of the battle.{/n}
{n}For a time she found reasons not to tell one of the stories the Commander had liked. Later she told it again. Someone laughed at the right place, and the pleasure hurt enough that she had to stop before beginning another.{/n}''', requires=("sacrifice",), forbids=("gesmerha.dead", "gesmerha.closed", "inhuman", "demon", "devil", "ascended"))
ending("aeon", "A life without that visitor", '''{n}In the history remade without the Worldwound, the same Commander did not arrive to share Gesmerha's afternoons. The disputes, journeys and private answers that had followed that meeting did not survive unchanged as promises she owed to an absent traveler.{/n}
{n}Whatever work her hands found in that world belonged to the life she lived there. No erased farewell could decide its ending for her.{/n}''', owner="AeonEpilogue")


SCENES.append(scene("gesmerha.late_ending_unfinished", "The visit after the return", "Epilogue", 0, "", [
    n("start", "Narrator", '''{n}There had been another meeting in Wintersun. Gesmerha had sat behind a chest of things waiting to be sorted and asked the Commander to describe the stool someone had left in her path. After the long absence, the little complaint had made her presence wonderfully ordinary.{/n}
{n}The Commander remembered her moving the folded blanket to make room on the chest beside her. She had wanted company among the bundles and the arguments. When another journey failed to bring another afternoon, it was that ordinary welcome the Commander found themself wanting to hear again.{/n}''', portrait="Gesmerha")], Relationship="gesmerha", last=99,
    requires=("gesmerha.late_arrived",), forbids=(*LIVING_BLOCK, "gesmerha.late_complete")))


def integrate(payload):
    payload.setdefault("Etudes", {}).update(ETUDES)
    for item in payload["Scenes"]:
        if item["Id"] in ("gesmerha.ending_living_reunion", "gesmerha.ending_unmet_again", "gesmerha.the_voice_at_court"):
            flag = "gesmerha.late_arrived"
        else:
            flag = "gesmerha.late_complete" if item["Id"].startswith("gesmerha.ending_") else None
        if flag and flag not in item["Forbids"]:
            item["Forbids"].append(flag)
