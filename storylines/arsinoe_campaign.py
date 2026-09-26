"""Arsinoe's authored street repair, private commitment and later campaign visits.

Native contact remains the verified living capital vendor, not a replacement actor.
The mason, disputed passage and Trickster possibility are authored developments.
"""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "a609ed9b2205d034bb3bb04d2a255681"
ANSWERS = "ecaf5cfe8087a4f45a2269974f4885c9"


def s(id, title, entry, nodes, previous, delay=48, chapters=(3, 5), forbids=()):
    SCENES.append(scene(id, title, "Arsinoe", min(chapters), entry, nodes,
        requires=("arsinoe.capital", "arsinoe.continuation_kept", previous),
        forbids=("arsinoe.closed", *forbids), delay=delay, optional=True,
        Relationship="arsinoe", Areas=[DREZEN], Chapters=list(chapters),
        ContactUnit=CONTACT, AnswerLists=[ANSWERS]))


s("arsinoe_after_rain", "The water under the step",
  '"You look as though somebody has offended you before breakfast."', [
    n("start", "Arsinoe", '''"A staircase. I am considering the appropriate form of complaint."
{n}Arsinoe pulls a chair from beneath her table. Its seat holds a damp shoe, a folded stocking, and a little heap of grit. Her other foot is very firmly planted in a dry slipper.{/n}
"The passage beside the cooper's yard is the shortest way here. This morning I discovered that its third step has become a fountain. An unannounced improvement."
{n}She shakes the stocking once and hangs it over the chair back.{/n}
"I have asked the people on either side to close it until someone has looked beneath the paving. They both tell me that the passage belongs to the other. The cooper does, however, consider its ownership quite settled when somebody wishes to leave a cart there."
{n}She retrieves her outdoor cloak.{/n}
"I have found a mason willing to examine it. Would you come? I can promise an improvement on the smell of this stocking. I cannot promise a pleasant afternoon."''',
      c('"Show me the offended staircase."', "passage"),
      c('"Another time. Keep people off it until then."', abort=True)),
    n("passage", "Narrator", '''{n}Arsinoe changes into dry walking shoes before you leave. The passage is a narrow flight between two high walls. A rope has been stretched across each end. Somebody has hung an empty pail from the nearer one, making the warning difficult to overlook.{/n}
{n}The mason waits on the upper landing, outside the rope. She is a stocky adult woman with white dust in the seams of her hands. A measuring rod rests against her shoulder.{/n}
"Orvena," Arsinoe says. "The Commander has offered us an opinion. We are under no obligation to accept it."
"Good. I get enough opinions. What I need is somebody to keep the far end clear while I work."
{n}You take turns directing the few approaching pedestrians around the longer way. Orvena lowers a weighted cord through the open joint beneath the third tread. When she draws it out, the weight carries dark, wet silt.{/n}
"There used to be a drain through here. It has stopped going where it ought. I can open the step, but first I want to know whether that wall has moved with it."
{n}She indicates a pale streak near the base of the cooper's wall. From the landing it could be fresh mortar, or a deposit left by the water.{/n}''',
      c('[Perception] Compare the streak with the stone joints from the safe landing.',
        check=dict(Skill="SkillPerception", DC=24, Success="seam", Failure="glare", CommanderOnly=True)),
      c('"Let Orvena open the tread before we decide what it means."', "opened")),
    n("seam", "Arsinoe", '''{n}At the end of the pale streak, one stone has left a clean edge against its neighbor. The edge is sheltered from the water. You point it out without crossing the rope.{/n}
{n}Orvena bends to sight along the wall, then nods.{/n}
"That is movement. Now I know which joint is opening, I can support it directly. Otherwise I would have to prop the whole side before lifting anything. Thank you."
{n}Arsinoe follows your pointing hand.{/n}
"I thought the white meant someone had repaired it recently. A reassuring conclusion to reach from such an inconveniently placed crack."
{n}Orvena sends an apprentice for timber. The delay earns a complaint from a man carrying a basket, who falls silent when the mason asks which part of his body he wishes to put under the wall first.{/n}
"I like her," Arsinoe says, once he has taken the longer road. "Though I had hoped to spend the afternoon discussing a drain."''',
      c('"Stay until she has the supports in place."', "work_seen")),
    n("glare", "Arsinoe", '''{n}Water glints on the pale line. You change your angle twice, but the stone beneath remains difficult to distinguish. Orvena listens to your uncertainty and reaches for a wedge.{/n}
"Then I shore the whole side. That will use the timber I had hoped to keep for the upper landing, but timber costs less than a guess."
{n}Arsinoe takes the mason's bag while she sends for the supports. There is no ceremony to the help; the bag is in the way, and Arsinoe has two free hands.{/n}
"I would have liked a simpler answer," she says. "I usually do. That has not made them more plentiful."
{n}By the time the timber arrives, somebody has brought the cooper. He objects to having part of his doorway obstructed. Orvena shows him where the loosened stone would fall. He moves his stock himself.{/n}
"We shall know more when she opens it," Arsinoe says. "Until then, I believe we can afford to be disappointing."''',
      c('"Wait for the work to make the answer clear."', "work_uncertain")),
    n("opened", "Arsinoe", '''"Yes. With the side supported first. I dislike this enough to pay for some caution."
{n}Orvena accepts the instruction only after making her own inspection. She measures the gap, sends for timber, and asks the cooper to move the goods stacked against his doorway.{/n}
"If it is nothing, he will say we wasted his afternoon," she tells Arsinoe.
"Then he shall have an afternoon available in which to say it."
{n}You help keep the landing clear. The people who use this passage know several other ways around it, each of which turns out to be particularly unpleasant when carrying a full basket. Arsinoe listens to the complaints without offering to reopen the rope.{/n}
{n}A woman with a handcart describes how the water first appeared. Orvena stops working to ask her which side it came from. The woman points to an old outlet beneath the lower landing, hidden behind a pile of rubble. Orvena marks its position for clearing along with the broken channel.{/n}
"That saves me opening the wrong end to find it," the mason says. "Thank you. You can leave the cart there while you catch your breath."''',
      c('"Stay for the inspection."', "work_opened")),
    n("work_seen", "Narrator", '''{n}Behind the lifted tread, a length of old drainage stone has broken away. The earth beneath it has washed into a hollow. Orvena holds up a chipped fragment, then lays it on the landing where nobody can mistake it for sound paving.{/n}
"I can repair this. I cannot make either neighbor own it by looking at them. Someone must authorize the excavation and agree to pay me."
{n}Arsinoe looks from the broken stone to the two closed doors.{/n}
"We shall ask them together. I have already heard them separately, and it was a remarkably complete exercise in explaining nothing."
{n}She keeps the little fragment. Before leaving, she checks that both ropes are secure.{/n}''',
      c('"I will come to the discussion."', flags=("arsinoe.drain_examined", "arsinoe.wall_movement_seen"))),
    n("work_uncertain", "Narrator", '''{n}The lifted tread exposes a broken length of drainage stone and a hollow where the water has carried away the earth. Orvena shows you how the wall above has begun to settle toward it. The pale line was only part of the damage.{/n}
"Now we know. I can repair this, if someone authorizes the excavation and pays me. I cannot settle the ownership with a trowel."
{n}Arsinoe takes a small fragment of the drain as a sample. She means to ask both neighbors to a discussion, together this time.{/n}
"They have each given me an excellent account of the other's obligations. I should like to see how well the accounts agree in the same room."''',
      c('"I will come."', flags=("arsinoe.drain_examined", "arsinoe.wall_uncertain"))),
    n("work_opened", "Narrator", '''{n}The drain beneath the step has broken, carrying earth away from the foot of the wall. Orvena shows the hollow to you both from the landing. She has no doubt about the repair. Her doubts concern the people who must agree to let her do it.{/n}
"I want permission to open both edges, a price agreed before I begin, and somebody who will still admit knowing me when I ask for payment."
{n}Arsinoe takes a small piece of the broken drain.{/n}
"I shall invite our neighbors to discuss all three. Together. We have tried asking separately, with impressive results for the art of conversation and none for the stairs."
{n}She checks the ropes before you leave.{/n}''',
      c('"I will be there."', flags=("arsinoe.drain_examined", "arsinoe.wall_opened"))),
], "arsinoe_the_unprofitable_hour")


s("arsinoe_two_doors", "The people on either side",
  '"Have the neighbors agreed to speak?"', [
    n("start", "Arsinoe", '''"They have agreed to arrive. I thought it best to begin with something measurable."
{n}Arsinoe takes you to the cooper's empty workroom. Orvena has brought her estimate. The cooper, Senn, stands behind a stool as though it might protect him from the figure written on the page. Beside the open door waits Edris, who rents the rooms on the passage's other side.{/n}
"I did not build it," Senn begins.
"Nor did I," says Edris. "Nor, so far as I know, did she. Can we finish that part?"
{n}Orvena places the piece of drain between them. Arsinoe waits until both look at it.{/n}
"The passage will remain closed while it is unsafe. We are deciding how to repair it. We are not deciding whether to ask people to fall through it until ownership becomes less embarrassing."
{n}Edris takes the stool. Senn discovers that standing behind it now looks rather foolish, and fetches another.{/n}''',
      c('"Hear what each of them can actually offer."', "terms"),
      c('"I cannot stay for this discussion."', abort=True)),
    n("terms", "Arsinoe", '''{n}Senn produces an old agreement permitting access through the passage. It assigns cleaning to the occupants of both properties but says nothing about replacing the drain. Edris has already paid for clearing it twice. She brings the receipts, with grease stains where they have lain in her kitchen.{/n}
"My tenants carry water up there," she says. "I want it open. I cannot pay for a new drain out of their rent this month."
"And I cannot close my yard while you decide," Senn replies.
"Your wall may decide first," Orvena says.
{n}Arsinoe asks the mason to separate the urgent work from the later paving. Then she asks each neighbor what they can pay now, before anybody begins discussing what a good person would offer.{/n}
{n}The smaller sum is still too large. Senn can supply cartage and stone from a demolished shed. Edris can pay in installments. Neither contribution will feed Orvena's crew through the first week.{/n}
"I can advance the difference," Arsinoe says. "But I want an arrangement we can examine after the noise of today's meeting has gone away."''',
      c('"You would become their creditor. Do you want that?"', "creditor"),
      c('"Could the urgent part be done while the rest waits?"', "stages"),
      c('"Surely they will cooperate if I order it."', "order")),
    n("creditor", "Arsinoe", '''"Not especially. I would prefer to walk here without getting wet."
{n}Her glance at you is brief and appreciative.{/n}
"It would be a loan for the agreed work, with dates they can meet. No interest for this small sum, and no claim on their homes if they miss a payment. I have no wish to become a landlord by means of a broken pipe."
"Then why would we pay?" Senn asks, too quickly.
{n}Arsinoe turns to him.{/n}
"Because you would have agreed to. Because I shall ask. Because a city in which every promise requires a threat is expensive to live in. If these answers are inadequate, you need not accept my money."
{n}Senn looks at Edris. She does not rescue him.{/n}
"I asked badly," he says at last.
"You did. It was useful to hear before I lent it."''',
      c('"Compare that with doing the work in stages."', "comparison")),
    n("stages", "Arsinoe", '''{n}Orvena turns her estimate over and draws the passage. She can replace the broken drain and shore the side now. The upper paving can wait behind a narrower barrier. People on foot would regain the passage; carts would still take the long way.{/n}
"Two visits cost more than one," she says. "And I will not promise the second week until it is paid for."
{n}Senn dislikes losing the cart route. Edris dislikes another round of work outside her rooms, but neither pretends the proposal is impossible.{/n}
"I could pay a smaller share outright," Arsinoe says. "As a neighbor who uses the passage. Then no one owes me anything. It would leave less for other things I hoped to do."
"You need not pay at all," Edris says.
"I know. I am deciding whether I want to. That is considerably easier while you remember the distinction."''',
      c('"Compare the two arrangements."', "comparison")),
    n("order", "Arsinoe", '''"They may agree very quickly. I should then have to discover which parts they cannot possibly do."
{n}She draws the estimate toward her.{/n}
"There are matters in which you must give an order. This is a repair whose cost ought to be known by the people meeting it. Let them disagree while disagreement is still inexpensive."
{n}Senn opens his mouth, glances at you, and shuts it. Edris watches him rather than you.{/n}
"For example," Arsinoe says, "I believe we have just learned that he has another objection. I would rather hear it."
{n}Senn admits that a promised delivery has not been paid for. His available money is smaller than the figure he first gave. Arsinoe crosses out the larger sum without praising his honesty.{/n}
"There. We have improved the plan by making it less impressive."''',
      c('"Let us work with what they can do."', "comparison")),
    n("comparison", "Arsinoe", '''{n}The alternatives take shape. Arsinoe can advance enough to let the crew finish the whole repair, accepting the trouble of collecting two modest debts. Or she can contribute a smaller gift toward the urgent work, leaving the upper paving for a later paid visit.{/n}
{n}Both neighbors accept either arrangement. Orvena writes down what each includes, and what it leaves out. She refuses Senn's request to promise a completion date before she has lifted the rest of the stone.{/n}
"I will choose with you," Arsinoe says quietly, while the others compare the two pages. "You have listened to more than my complaint about a wet foot. I should like your judgment now."
"And if we disagree?"
"Then we shall have a smaller meeting afterward. I am willing to try either. I would not ask you to choose from a list containing an answer I secretly intend to punish."''',
      c('"Advance the repair cost. I will help you face the awkward conversations afterward."', "loan"),
      c('"Pay a neighbor\'s share and do the urgent work first. Leave the larger promise for later."', "staged")),
    n("loan", "Arsinoe", '''{n}Arsinoe names her maximum before the agreement is signed. Anything discovered beyond it will require another discussion. Orvena approves this more readily than the neighbors do.{/n}
"I would rather interrupt work than discover afterward that I was expected to donate it," the mason says.
{n}When everyone has gone, Arsinoe remains beside the empty stool. She looks tired, and pleased, and faintly apprehensive.{/n}
"I have managed to acquire two debtors and a reason to inspect a drain. You see the temptations to which I am subject."
{n}She folds her copy of the agreement.{/n}
"Do keep your promise about the awkward conversations. Not to make them agree with me. I am quite capable of frightening Senn now. To tell me if I have begun enjoying it."''',
      c('"I will tell you."', flags=("arsinoe.repair_loan", "arsinoe.repair_agreed"))),
    n("staged", "Arsinoe", '''{n}Arsinoe states her contribution. Orvena marks the limit of the first repair in charcoal, takes the agreed deposit, and leaves the two neighbors to arrange the remaining payments between themselves.{/n}
"The upper paving will still be ugly," Arsinoe says once you are alone.
"You knew that."
"I did. I am permitting myself to complain anyway."
{n}She smiles and folds the page. The expression eases as she considers the smaller commitment.{/n}
"I can live with an ugly upper landing for a while. I shall have to remember that when the first person congratulates me on getting the passage repaired and then asks why I stopped halfway."
{n}Outside, Orvena is already measuring timber. Arsinoe watches her, then turns back to you.{/n}
"I am glad you stayed. I wanted company after that meeting, and it is a pleasure not to have to explain the whole thing first."''',
      c('"Walk back together."', flags=("arsinoe.repair_staged", "arsinoe.repair_agreed"))),
], "arsinoe_after_rain")


s("arsinoe_a_stone_in_hand", "The mason's spoiled piece",
  '"How is Orvena getting on?"', [
    n("start", "Arsinoe", '''"The drain is going very well. Her afternoon is not. Come and look."
{n}At the passage, Orvena has left the crew securing a channel that now carries water cleanly away from the wall. She sits under an awning with a small stone block in her lap. One corner has broken off. The broken piece rests on the ground beside her boot.{/n}
"A practice piece," she explains. "For a buyer who wanted a carved border. I made the leaves too deep. He can buy something else."
{n}The surviving leaves curl around a shallow recess. A little face should have looked out between them. Its mouth is a rough notch, unfinished.{/n}
"You might finish it for yourself," Arsinoe says.
"I could eat it for myself too, if my teeth were better. I have paid work."
{n}There is no anger in the answer, which seems to trouble Arsinoe more than anger would. She asks the price of the spoiled piece. Orvena gives a very small figure, then objects when Arsinoe offers to pay it.{/n}
"Do not buy my mistakes because you feel sorry for me."
"Then tell me whether you want to sell a small stone I would like to own. I have not asked you to disguise the missing corner."''',
      c('"What would you do with it?"', "sill"),
      c('"Orvena may prefer to keep it."', "hers")),
    n("hers", "Arsinoe", '''{n}Arsinoe withdraws her hand from her purse.{/n}
"Quite right. I have bargained enthusiastically with a person who has not agreed to sell."
{n}Orvena rubs the unfinished face with her thumb.{/n}
"I was going to throw it in the rubble. If you truly want it, take it at the price I said. Only do not ask me to be grateful for getting it wrong."
"I am glad you told me. I can be rather quick to decide that something ought to be settled."
{n}Orvena puts the stone on a workbench. It looks less forlorn there than it did in her lap, although the missing corner has not become any smaller.{/n}''',
      c('"Where will you put it?"', "sill")),
    n("sill", "Arsinoe", '''"There is a recess by my window. It contains a perfectly serviceable pot that I have never liked. I might replace it with a face that seems to have an opinion."
{n}Orvena asks whether Arsinoe truly wants this damaged piece. When she says yes, the mason agrees to sell it at the stated price. Arsinoe asks her to finish the mouth as paid work, if she has time. Orvena names the additional cost and Arsinoe accepts.{/n}
{n}Orvena gives her the stone, unfinished mouth and all, to judge its weight. Arsinoe almost drops it. You steady its lower edge while she adjusts her grip.{/n}
"A strongly held opinion."
{n}The mason laughs. Then she takes it back and tells you to return when she has finished the paid repairs. She will not carve delicate leaves with people waiting for a safe passage.{/n}
{n}Walking away, Arsinoe looks at the buildings beside you as though she is measuring their empty corners.{/n}
"I see good work disappear into walls every day. I value it. I can also see why a woman might want to make something people notice before it fails."
"Is that what you wanted from her?"
"I wanted the small face. I should be careful about supplying her with a grander reason to sell it to me."''',
      c('"I would like to try carving something. Something very small."', "try"),
      c('"I would rather watch someone who knows what she is doing."', "watch"),
      c('[Trickster] "What if the spoiled corner could show her the cut she has not made yet?"', "possibility", requires=("trickster",))),
    n("try", "Arsinoe", '''{n}Arsinoe arranges a short lesson after Orvena's paid work. The mason gives you a soft offcut, a blunt point, and the repeated instruction to keep your other hand out of the way.{/n}
{n}Your proposed leaf develops a shape that Arsinoe politely declines to name. Her own attempt breaks along the stem. Orvena places both beside a clean example and shows where you pressed instead of guiding the tool.{/n}
"You are both accustomed to getting a result when you insist," she says. "Stone does not find that interesting."
{n}On the next attempt, you let the point travel more gently. The line remains shallow but continues where you intended. Arsinoe watches with the concentration of a rival student.{/n}
"I see. You have become unbearably accomplished."
{n}She keeps her broken leaf. You keep your crooked one. Orvena sweeps the dust away without promising either of you a future in the trade, then finishes the small face Arsinoe bought. Its skeptical mouth seems to have formed an opinion of both students.{/n}
{n}Arsinoe wraps the finished stone for the walk home.{/n}
"Thank you," Arsinoe tells her. "That was exactly the amount of encouragement I could safely bear."''',
      c('"Carry your unsuccessful leaves home."', flags=("arsinoe.stone_practiced", "arsinoe.stone_chosen"))),
    n("watch", "Arsinoe", '''{n}You return when Orvena has time for the little face. She wedges the stone on her bench and makes the first cut so lightly that it scarcely seems to touch the surface. Arsinoe leans closer, keeping clear of her working arm.{/n}
"I expected a much larger tool."
"For a mouth that size? You would give it a very loud opinion."
{n}The expression appears by degrees. It is less solemn than the ruined corner made it seem, and distinctly less handsome than a buyer seeking flawless ornament might desire. Arsinoe likes the slight skepticism around the eyes.{/n}
"It will look at me when I put off cleaning the window."
"Then turn it toward the street," Orvena says. "There is more to criticize there."
{n}You sit with Arsinoe while the mason finishes. Work continues in the passage behind you. Water strikes the repaired channel with a steady little sound, quite different from the dripping that first brought you here.{/n}
{n}When the stone is ready, Arsinoe wraps it in an old cloth. She lets you carry it while she looks for a comfortable way to hold its awkward weight.{/n}''',
      c('"Take it back with her."', flags=("arsinoe.stone_watched", "arsinoe.stone_chosen"))),
    n("possibility", "Arsinoe", '''{n}Arsinoe stops walking.{/n}
"Show her a possible cut, or make her remember learning one? Those are very different proposals."
{n}You describe a moment made to arrive out of order: the stone might briefly display a finished face, then return to its present shape. Orvena could examine it, reject it, or use what she saw. Her hands would still do the work.{/n}
"Ask her," Arsinoe says. "And tell her what you cannot promise. I will watch."
{n}Orvena listens without putting down her tools.{/n}
"If it starts talking, you take it away. If it merely shows me something, I will look. I am not agreeing to carve whatever it happens to show."
{n}You place the broken corner beside the block. For an instant its shadow falls toward the sun. The empty notch becomes a laughing mouth. A leaf curls across the fracture, making the absent corner part of the border instead of hiding it.{/n}
{n}Then the shadow turns back. The block is rough and broken again. Orvena has already reached for her marking chalk.{/n}''',
      c('"Let her decide what to keep."', "after_possibility")),
    n("after_possibility", "Arsinoe", '''"The leaf is useful," Orvena says. "The mouth is smug. I can improve that."
{n}She draws a line across the broken corner, then wipes half of it away and begins again. Arsinoe waits until the mason has returned to her own work before speaking.{/n}
"I expected to dislike that. I dislike being shown a finished thing as though the only task remaining were obedience. But she has already altered it."
"Does that make it acceptable?"
"For this willing woman and this stone, yes. Do not expand my answer into permission to rearrange everyone else's disappointments."
{n}She studies you with an interest that is warmer than her caution.{/n}
"I have spent much of my life asking people to imagine a better place. You made one small possibility visible. I can admire that without deciding that every surprise is wise."
{n}Later, Orvena finishes a face distinctly different from the glimpse. Its smile is crooked. The missing corner remains. She charges Arsinoe the agreed price and declines to provide a discount for assistance from the future.{/n}
"An entirely reasonable position," Arsinoe says, and laughs when you agree a little too solemnly.''',
      c('"Carry home the face Orvena actually chose to make."', flags=("arsinoe.stone_possibility", "arsinoe.stone_chosen"))),
], "arsinoe_two_doors")


s("arsinoe_the_first_cart", "What the repair leaves behind",
  '"Is the passage ready?"', [
    n("start", "Arsinoe", '''"Ready for the work we agreed to pay for. Orvena has been very precise about that."
{n}Arsinoe walks with you to the passage. A shallow stream runs from a bucket into the repaired channel. Orvena watches where it emerges below; the cooper watches the dry patch beside his wall with the anxious pride of a man who has decided the result was his idea.{/n}
"You can admire it later," the mason tells him. "Stand where I can see whether the tread shifts."
{n}He obeys. Nothing moves. Orvena repeats the test with two of her crew, then marks the date on the underside of a spare stone she is leaving for future repairs.{/n}
"If anyone opens it again, they will know what we did. Ask before you build over it. Water does not read complaints."
{n}Arsinoe waits until the crew has finished before stepping onto the landing herself. She takes the third tread with deliberate weight.{/n}
"Dry," she announces. "An excellent quality in a staircase."''',
      c('"Did finding the moving joint help?"', "targeted", requires=("arsinoe.wall_movement_seen",)),
      c('"Did you need all the supports?"', "supported", requires=("arsinoe.wall_uncertain",)),
      c('"Did you find the outlet the woman showed us?"', "outlet", requires=("arsinoe.wall_opened",))),
    n("targeted", "Arsinoe", '''{n}Orvena shows you a stack of unused timber beside the landing.{/n}
"That joint was the one. Supporting it directly left these spare. The people who paid for them can keep them for the next job. Dry, preferably."
{n}Arsinoe asks Senn where he can store the wood. Edris follows him to look at the place, unwilling to have their common materials disappear into an unrecorded corner of his yard.{/n}
"A useful observation," Arsinoe says to you. "I should like the next repair to begin with materials already here. We shall see whether they can agree on which shed is sufficiently dry."
{n}She waits until the timber has been carried in before asking about the rest of the account.{/n}''',
      c('"Discuss the full repair."', "loan", requires=("arsinoe.repair_loan",)),
      c('"Discuss what remains."', "staged", requires=("arsinoe.repair_staged",))),
    n("supported", "Arsinoe", '''"All of them," Orvena says. "The wall began shifting as I lifted the tread. The props held it until we could pack beneath. I have used the timber allowance; there is none left for another job."
{n}She shows Arsinoe the marks where the supports took the weight. The cost remains inside the agreed estimate, but Edris had hoped to keep something toward the later repairs.{/n}
"You paid for timber that held up a wall," Arsinoe tells her. "I believe we should resist the temptation to mourn its usefulness."
{n}Edris laughs reluctantly. Arsinoe touches the dry stone, then asks Orvena for the rest of the account.{/n}''',
      c('"Discuss the full repair."', "loan", requires=("arsinoe.repair_loan",)),
      c('"Discuss what remains."', "staged", requires=("arsinoe.repair_staged",))),
    n("outlet", "Arsinoe", '''{n}Orvena points beneath the lower landing. With the old outlet cleared, the repaired channel has a place to discharge before water can build against the wall.{/n}
"I would have found it by digging from the other side. This took less time and left the paving there alone. Tell the woman with the cart if you see her. I would rather she heard that we used her answer than assumed she had wasted her breath."
{n}Arsinoe looks for her along the street, then turns back.{/n}
"I know which way she usually comes. I shall tell her when I see her. And I shall try to remember to ask who has watched a problem before deciding who ought to understand it."
{n}She returns to the mason's final account.{/n}''',
      c('"Discuss the full repair."', "loan", requires=("arsinoe.repair_loan",)),
      c('"Discuss what remains."', "staged", requires=("arsinoe.repair_staged",))),
    n("loan", "Arsinoe", '''{n}The upper landing has been relaid. Senn brings a handcart through while Orvena watches the wheels. At the bottom he stops beside Arsinoe, takes out a folded paper, and begins explaining a delayed payment.{/n}
{n}Arsinoe lets him finish.{/n}
"You have missed a date we agreed. I will hear a new proposal. I will not pretend the first one was merely a suggestion."
{n}His new dates are smaller and closer together. She asks which delivery will pay the first. This time he gives a specific answer. Edris has paid her installment already, a fact Arsinoe carefully avoids using to humiliate him.{/n}
{n}When he has gone, she opens her hand. Her fingers have left little crescents in her palm.{/n}
"I was angry before he finished speaking. I wanted this to be the afternoon when the repair was finished and nobody needed another arrangement. He had scarcely opened his mouth before I resented the conversation."
{n}She looks up at you.{/n}
"I heard him. I am still annoyed. You may tell me if you noticed something else."''',
      c('"You gave him room to make a new promise. That mattered."', "heard"),
      c('"You sounded as though you expected him to disappoint you before he spoke."', "expected")),
    n("staged", "Arsinoe", '''{n}The repaired drain is sound. The upper landing remains uneven, behind the narrower barrier Orvena described. Pedestrians can use the passage again; carts still take the longer road.{/n}
{n}Edris brings the crew a jug of water. She has begun setting aside money for the second visit, but Senn will not give a date until another delivery has been paid for. He complains that the short route is still closed to his business.{/n}
"It is open to your feet," Edris says. "Try delivering a smaller barrel."
{n}Orvena intervenes before that becomes a discussion of each other's customers. She leaves them with a written price that will remain valid for a stated period, then gathers her tools.{/n}
{n}Arsinoe watches a woman lead two laden companions carefully past the barrier.{/n}
"This was the arrangement I accepted. I find myself wanting to apologize for the unfinished part. If I begin paying whenever I feel that way, our small gift will become a very different thing."
{n}She turns to you.{/n}
"How did it look from where you stood?"''',
      c('"People can use a safe passage again. Let that be an improvement."', "heard"),
      c('"You wanted the whole job finished. You chose a limit you find difficult."', "expected")),
    n("heard", "Arsinoe", '''"Yes. I should allow the afternoon to contain something besides the part I would improve."
{n}She looks back at the dry tread. A child being led through by an adult hops over it, expecting the familiar splash, and looks disappointed when none comes.{/n}
"There. We have ruined someone's entertainment."
{n}Her smile returns. She waits for the family to pass before moving closer to you.{/n}
"I wanted you here for more than an opinion on masonry. I do like being admired. It is pleasant, and I have never understood the virtue of pretending otherwise. But I would like to be known when I am difficult too."
{n}She brushes dust from her cuff.{/n}
"Perhaps with occasional admiration afterward. I would hate to discover that intimacy required giving it up entirely."''',
      c('"I can manage both."', "home")),
    n("expected", "Arsinoe", '''{n}Arsinoe is silent long enough that the sounds of the passage become conspicuous.{/n}
"Yes. I wanted the reasonable choice to feel more comfortable than it does. I may have made other people carry some of that disappointment."
{n}She looks toward the cooper's door, then back at you.{/n}
"I asked you because I hoped you would answer. That does not make the answer immediately pleasant. Give me a moment before you decide I regret asking."
{n}You walk to the lower end of the passage together. By the time you reach it, she has stopped brushing at a mark on her cuff that disappeared several steps earlier.{/n}
"I do want to go on being asked to supper after I have behaved foolishly," she says. "I am discovering that this is a rather personal ambition."
"You have not lost your invitation."
"Good. I was about to ask for one."''',
      c('"Go home with her."', "home")),
    n("home", "Arsinoe", '''{n}At her door, Arsinoe stops to free a length of thread caught in the fastening of her cloak. You wait while she pulls it loose. The small delay seems to settle the last of the day's irritation.{/n}
"Come another evening. I have something I would like to tell you without a broken wall listening."
{n}She gives the invitation plainly, then smiles at the expression it produces.{/n}
"You need not prepare a defense. I have no estimate and no witnesses. I want to speak about us. If you would rather not, say so when you come. I should still prefer your answer to a week of ingenious guesses."
{n}She names a time after closing. You agree before she turns inside.{/n}''',
      c('"I will come."', flags=("arsinoe.repair_seen",))),
], "arsinoe_a_stone_in_hand", delay=72)


s("arsinoe_what_she_asks", "A question after closing",
  '"You wanted to speak about us."', [
    n("start", "Arsinoe", '''{n}The little carved face occupies the recess by Arsinoe's window. She has set it on a folded cloth to protect the sill. It watches the room with an expression far too skeptical for a guest.{/n}
"I tried turning it toward the street," she says. "It looked as though it disapproved of everyone passing. In here, at least, it has evidence."
{n}She closes the outer door and sits near you. There are drinks within reach, but she does not busy herself pouring them.{/n}
"I have enjoyed these visits. I have also caught myself imagining the next one while I ought to be listening to somebody buying a scroll. That is a poor professional habit, and I suspect it will get worse."
{n}She rests her hands loosely together.{/n}
"I would like to know what you want from me now. We made an earlier choice about how to begin. I have not forgotten it. I would rather hear whether it still suits you than treat it as an answer to every future question."''',
      c('"I want a lasting courtship with you."', "lasting", forbids=("arsinoe.friendship",)),
      c('"I am ready to stop keeping our affection at a distance."', "lasting", requires=("arsinoe.slow",)),
      c('"I want affection, but I cannot promise a settled future."', "open", forbids=("arsinoe.friendship",)),
      c('"I still want to take our time. I am not ready to promise more."', "slow", requires=("arsinoe.slow",)),
      c('"Our friendship is what I want to keep."', "friend", requires=("arsinoe.friendship",)),
      c('"I would rather end the courtship kindly than promise what I do not want."', "part", forbids=("arsinoe.friendship",)),
      c('"I need time before I answer."', abort=True)),
    n("lasting", "Arsinoe", '''{n}Arsinoe's breath catches before she smiles. She takes a moment to enjoy your answer without immediately improving its terms.{/n}
"Then I will tell you what I want. I want you to visit because you miss me. I want to be able to miss you without making it sound like a failure of discipline. I want us to speak when the shape of our lives changes."
{n}She reaches for your hand, slowly enough to make the invitation clear.{/n}
"I have made a life by leaving one place for another. I do not want to pretend I have become a woman who will never look at a road again. If I go somewhere, I want to discuss how we remain in each other's lives. I would expect the same of you."
{n}Her fingers rest against yours.{/n}
"Nor do I mean to make an unspoken claim on all your affection. If there are other people, I want to know what promises I am joining. Tell me what you can honestly offer."''',
      c('"A lasting place in my life, with room for other freely chosen relationships."', "shared_terms"),
      c('"I want to build this as my sole romantic partnership. I will honor my existing promises when I make that choice."', "sole_terms")),
    n("shared_terms", "Arsinoe", '''"Then let us be precise enough to avoid being cruel by accident. I will not require you to discard someone else to prove that you want me. I will require you to make time that does not consist entirely of whatever remains after everyone else's invitations."
{n}She gives your hand a small squeeze.{/n}
"I shall make time for you as well. If either of us wants to change the arrangement, we speak. If somebody is being deceived, we do not call it a happy consequence of having so much affection."
{n}Her composure softens into a smile.{/n}
"That is what I can offer. It sounds rather severe until I add that I am already looking forward to the next evening, and would be disappointed if you ended this one early."
{n}She moves her chair closer. The clasp at her wrist catches the light as she lifts her free hand to your cheek.{/n}
"May I kiss you now? I have been admirably patient with my own explanation."''',
      c('"Yes."', "promise_kiss"),
      c('"Hold me instead. I want to be close to you."', "promise_hold")),
    n("sole_terms", "Arsinoe", '''"Then do that honestly. I will not make another person disappear from your life by treating this room as though it contains the whole of it."
{n}She keeps your hand while she considers her own answer.{/n}
"I can choose that kind of partnership with you. I will not demand that you prove it by handing me a list of people you have disappointed. Tell the truth where a truth is owed, and tell me if your intention changes."
{n}Her smile comes slowly.{/n}
"I find that I have become much more interested in what happens after we have finished defining it. That may be a good sign. I should like to kiss you. Or be held, if that is what you would prefer tonight."
{n}She moves her chair nearer, leaving you enough room to turn toward her without the table between you.{/n}''',
      c('"Kiss her."', "sole_kiss"),
      c('"Draw close and hold her."', "sole_hold")),
    n("promise_kiss", "Narrator", '''{n}Arsinoe meets you without haste. Her hand rests along your cheek; when you draw back, she follows for one brief kiss more. She looks pleased enough to laugh at herself.{/n}
"There. A very satisfactory beginning to a difficult promise."
{n}You remain close while the drinks go untouched. Later she remembers them and pours, then discovers that she has given you her preferred cup. She considers asking for it back before deciding that you are worth the sacrifice.{/n}
{n}The evening continues with smaller questions. When do you like to wake? What makes a room feel occupied by someone you want there? Arsinoe dislikes sleeping beneath a window that cannot be opened. She admits this as though it might be the most troublesome condition of all.{/n}''',
      c('"Stay until it is time to wish her good night."', flags=("arsinoe.committed", "arsinoe.campaign_lover", "arsinoe.shared_terms", "arsinoe.future_spoken"))),
    n("promise_hold", "Narrator", '''{n}Arsinoe leans into your embrace and rests there. At first she keeps one hand against your arm, as though deciding how much weight to let you take. Then her breath eases and the question seems to settle itself.{/n}
"This too," she says. "I want evenings like this too."
{n}You stay together without making the pause lead anywhere else. Eventually the chair becomes uncomfortable enough for her to complain. She shifts, laughs, and asks whether a better cushion would constitute an unreasonable investment in the future.{/n}
{n}By the time you leave, you have discussed the cushion in absurd detail. Arsinoe walks you to the door, still disagreeing with your proposed color. She keeps your hand until the disagreement runs out of words.{/n}''',
      c('"Wish her good night."', flags=("arsinoe.committed", "arsinoe.campaign_lover", "arsinoe.shared_terms", "arsinoe.future_spoken"))),
    n("sole_kiss", "Narrator", '''{n}Arsinoe turns into the kiss with a warmth she has stopped trying to make discreet. When you part, she remains near enough that your next words need scarcely carry at all.{/n}
"I should have asked sooner. No, that is untrue. I am glad we had the other evenings. I merely wish to have had this one as well."
{n}She laughs at the impossibility and kisses you again. Later, when you sit together, she tells you something quite ordinary about her room: the window sticks in damp weather, and she prefers to sleep with it open. It is a small thing to learn after a large promise. You find yourself wanting to remember it.{/n}
{n}At the door she touches your cheek once more before letting you go.{/n}''',
      c('"Leave with the promise you both chose."', flags=("arsinoe.committed", "arsinoe.campaign_lover", "arsinoe.sole_intention", "arsinoe.future_spoken"))),
    n("sole_hold", "Narrator", '''{n}She comes into your embrace willingly. The first few moments are quiet. Then she notices the carved face watching from the window and begins to laugh against you.{/n}
"I shall turn it around. Later. I am comfortable."
{n}You remain together until the lamp needs adjusting. Arsinoe does it with one hand, reluctant to surrender the closeness for so small a task. There is no expectation that the evening must go farther to make the promise count.{/n}
{n}When you finally rise, she asks you to come again soon. Her voice is composed; her hand, holding yours at the door, is less willing to behave sensibly.{/n}''',
      c('"Promise another visit and wish her good night."', flags=("arsinoe.committed", "arsinoe.campaign_lover", "arsinoe.sole_intention", "arsinoe.future_spoken"))),
    n("open", "Arsinoe", '''"I can enjoy affection without pretending that we have settled the rest of our lives. I cannot enjoy being kept hopeful by an answer you have already decided never to give."
{n}She watches you while you assure her that uncertainty is what you mean. Then she nods.{/n}
"Very well. Let us keep seeing each other because we choose it. If that stops being enough for either of us, we say so. I would rather lose a pleasant arrangement than make it unpleasant by refusing to notice."
{n}She pours the drinks at last and hands you one.{/n}
"Stay tonight for the company. We have spent a great deal of it discussing a future we agreed not to promise. I should like to enjoy the part that is actually here."
{n}You talk until the hour grows late. She listens when you speak about a place you would like to see, then names one of her own. Neither destination becomes an appointment.{/n}''',
      c('"Keep the affection you can honestly offer."', flags=("arsinoe.campaign_lover", "arsinoe.open_future", "arsinoe.future_spoken"))),
    n("slow", "Arsinoe", '''"Then we shall take our time. I asked because I wanted your answer, not because I have decided the answer is overdue."
{n}She pours for you and settles back, allowing the space between the chairs to remain as it is.{/n}
"I am still interested. I also enjoy the evenings we have actually kept. If I find myself spending all of them impatient for a different one, I shall tell you. I would prefer you to hear that from me than discover it by becoming very good at reading a silence."
{n}The conversation moves to her room and the things she has brought from other places. You ask about a small brass weight on the shelf. It belonged to a set she bought because she liked the case; the case broke almost immediately. She keeps the weight because it holds a page open very well.{/n}
"There. An object that became useful after disappointing me. I should like to prevent you from drawing any conclusions about our evening from it."
{n}You laugh together. The question has been answered, and there is still time to enjoy the company.{/n}''',
      c('"Keep seeing each other at the pace you chose."', flags=("arsinoe.campaign_slow", "arsinoe.future_spoken"))),
    n("friend", "Arsinoe", '''"Then we agree. I wanted to ask because people can make a friendship strangely difficult by behaving as though it is a question they failed to answer. I have enjoyed ours."
{n}She pours for you, then settles into her chair with visible ease.{/n}
"I shall still expect you to notice when I am becoming insufferable. You have had practice now. And I should like to be invited to things you enjoy, even if I am likely to complain about the chairs."
{n}You talk about the repaired passage. Arsinoe soon abandons its practical merits for a description of Senn trying to appear knowledgeable while Orvena measured his wall. You supply his expression; she objects that you have made him too dignified.{/n}
{n}The evening runs comfortably past the time she intended to stop. At the door she asks you to come again before the next broken drain provides an excuse.{/n}''',
      c('"Keep the friendship."', flags=("arsinoe.campaign_friend", "arsinoe.future_spoken"))),
    n("part", "Arsinoe", '''{n}Arsinoe draws her hands back into her lap. She looks disappointed, and does not disguise it by immediately assuring you that the answer has made everything easier.{/n}
"Thank you for telling me. I would have preferred another answer. I shall need a little time before I can be gracious about how fortunate we are to understand each other."
{n}She stands when you do. At the door she stops, as though deciding whether to add something, then speaks without looking away.{/n}
"I enjoyed the evenings. I will not call them foolish because we have reached this one. But do let me decide when I want casual company again. I would rather not be asked to make the goodbye comfortable for both of us at once."
{n}You leave her with the room she had prepared. She closes the door gently after you.{/n}''',
      c('"Say goodbye."', flags=("arsinoe.closed", "arsinoe.parted", "arsinoe.future_spoken"))),
], "arsinoe_the_first_cart")


s("arsinoe_before_the_road", "Something that travels well",
  '"I may be away for some time. I wanted to see you before I go."', [
    n("start", "Arsinoe", '''{n}Arsinoe sets down the cloth she was using to polish a cup.{/n}
"Then sit. Unless you are leaving this very moment, in which case I shall be annoyed that you have called this notice."
{n}You sit. She studies your face before asking whether you know where the road will take you. You tell her what you can. She listens without supplying an optimistic destination of her own.{/n}
"I will remain here while there is work I can do. That is what I know about my road. I would like to know when yours brings you within reach again."
{n}She rises to fetch a small, soft pouch from a drawer. Inside is a thin metal cup, plain except for a dent near the rim.{/n}
"I carried this for years. It does not improve what you drink from it, despite what I was told when I bought it. But it fits in a bag, and I have not yet managed to break it."
{n}She offers it to you.{/n}
"Take it if it will be useful. I have been trying to think of a gift that would not require you to protect it from your life."''',
      c('"I would like something of yours to carry."', "cup"),
      c('"Keep it. Tell me something I can remember instead."', "memory")),
    n("cup", "Arsinoe", '''{n}The dent catches beneath your thumb. Arsinoe notices.{/n}
"A wagon. I put it on the edge while I fastened my bag, and the driver quite reasonably assumed that a person standing beside a moving vehicle would retrieve her belongings. I was thinking about a sermon."
{n}She looks ruefully toward her good pottery.{/n}
"It was not even a particularly good sermon. Too long, and with an example I later discovered proved the opposite of what I intended. I remember the cup much more fondly."
{n}You put it away where it will not rattle against anything fragile. Arsinoe watches until your hands are free again.{/n}
"I would ask you to bring me an interesting account of your travels, but I suspect the difficulty will be persuading you to have any dull ones. So bring me one dull thing. Something you ate. A place where you slept badly for an ordinary reason. I should like to imagine you in a day that did not require a victory."''',
      c('"I will look for one."', "cup_parting")),
    n("memory", "Arsinoe", '''"Very well. There was a market in Absalom where a woman sold hot little cakes from a pan. I used to pass it on a route that was longer than the one I claimed to be taking."
{n}Arsinoe sits again, the cup between her hands.{/n}
"I had a reason prepared. A shop I needed to visit, or someone I hoped to meet. Eventually the seller began asking what important business brought me out of my way that morning. She would have the cake ready before I finished answering."
{n}Her smile has a younger impatience in it.{/n}
"I went back years later. She had sold the business, and the new owner used too much honey. I ate it anyway. Then I went looking for something else I liked instead of spending the rest of the visit insulting the present."
{n}She puts the cup back in its pouch.{/n}
"There. A very small history. Remember me being foolish on an entirely safe street. I have managed it in several cities."''',
      c('"I will remember that."', "memory_parting")),
    n("cup_parting", "Arsinoe", '''{n}At the door, Arsinoe asks whether you have everything you meant to take. Then she stops herself before the question can grow into a list.{/n}
"You have traveled before. I know. I am having difficulty letting this visit end."
{n}She stands with you a moment longer.{/n}
"Come back if you can. I have work, company, and opinions enough to keep myself occupied. I shall still miss you. I see no reason to make one of those statements contradict the other."
{n}You say goodbye with the closeness you have chosen together. She remains at the door until you turn the corner, then goes inside to finish her interrupted work.{/n}''',
      c('"Leave with the cup."', flags=("arsinoe.departure_kept", "arsinoe.travel_cup"))),
    n("memory_parting", "Arsinoe", '''{n}Arsinoe accompanies you to the door. She begins to remind you of something practical, considers it, and lets the sentence go unfinished.{/n}
"You know how to travel. I know how to remain here. We shall both have to do the things we know while wishing the circumstances were different."
{n}She smiles at the dissatisfaction on your face.{/n}
"Yes. It is a poor consolation. I would prefer another evening as well."
{n}You say goodbye in the manner the two of you have chosen. When you begin to leave, she calls after you.{/n}
"Find something you like, even there. You may tell me about it when you can."
{n}She waits until you turn the corner before closing the door.{/n}''',
      c('"Leave with her memory of Absalom."', flags=("arsinoe.departure_kept", "arsinoe.travel_memory"))),
], "arsinoe_what_she_asks", delay=0, chapters=(3,))


s("arsinoe_where_she_stays", "The road she has not taken",
  '"Have you time to walk with me?"', [
    n("start", "Arsinoe", '''"Yes. I have been sitting over a letter long enough to begin disliking the shape of the words. Walking should improve them."
{n}She folds it and puts it away before taking her cloak. Outside, the streets are noisy enough that you have to choose a quieter way around the market. Arsinoe leads you toward the passage you helped repair.{/n}
"An acquaintance has asked whether I would consider moving when I can be spared. A trading settlement needs a priest, someone to manage a small temple's business, and, from the sound of the letter, someone willing to argue with everybody who suggested combining the two jobs."
{n}She glances at you.{/n}
"I would be good at it. That is an inconvenient part of the invitation. I have also caught myself planning how to arrange the rooms before I have decided whether I want to live in them."
{n}At the landing she pauses, letting a laden pedestrian pass.{/n}
"I have not accepted. I wanted to speak to you before I wrote my answer."''',
      c('"Is it the work you want, or the chance to begin again?"', "begin"),
      c('"What would you miss here?"', "miss"),
      c('"You asked me to return when I could. I wanted to find you here."', "departure", requires=("arsinoe.departure_kept",))),
    n("departure", "Arsinoe", '''"And here I am. I have not arranged a farewell behind your back."
{n}She answers gently, but without treating your expectation as a command.{/n}
"I remember asking you to come back. I also remember saying that I had a life to keep while you were away. This invitation arrived in that life. I am showing it to you because you belong in the conversation."
{n}She rests a hand against the dry stone at the side of the passage.{/n}
"I do not want us to discover that a promise to return has become an instruction never to move. There may be times when I leave and you remain. I would want you to have something better to do than measure how faithfully I had kept you waiting."
{n}She looks at you again.{/n}
"Tell me what you want. I shall tell you what I want. We need not agree before either of us is allowed to speak."''',
      c('"Then tell me what attracts you to the invitation."', "begin")),
    n("begin", "Arsinoe", '''"Both. I know how to arrive somewhere, examine what is lacking, and begin making myself useful. There is pleasure in it, beyond the duty. People remember the first person who repaired something they had stopped expecting to work."
{n}She looks up the passage.{/n}
"Remaining is less flattering. A good drain disappears beneath people's feet. They bring you the next complaint. You discover whether you like the place when it no longer congratulates you for being there."
{n}Her smile is a little embarrassed.{/n}
"I do like this place. I like knowing whose door will open before I knock. I like being able to ask you for an evening without first introducing the woman who wants it. I am trying to decide whether I have mistaken familiarity for a warning to leave."
{n}She takes a few steps, then stops beside you.{/n}
"It would be easier if the new work were unworthy. It is not. Someone should do it. That does not necessarily mean that someone must be me."''',
      c('"What would you miss here?"', "miss")),
    n("miss", "Arsinoe", '''"The people. The view from a particular window. Neral's refusal to admire an idea before she knows who will carry the chairs."
{n}She smiles as she names them.{/n}
"You. In ways that are not conveniently replaced by having important work. I would miss knowing that an ordinary day might include your arrival."
{n}The answer costs her less composure than it once might have. She lets you hear it without immediately asking for reassurance.{/n}
"I would also miss the little face by my window. I could pack it, of course. I have packed plenty of things I hoped would make a strange room feel like mine. Sometimes they did. Sometimes I simply had a familiar cup in an unfamiliar silence."
{n}She turns toward the market again.{/n}
"I think I want to remain, at least for the life we can actually see ahead. But I would like to take journeys that do not require abandoning one city to earn the next. A visit. A holiday. Such a shockingly modest use of a road."''',
      c('"I would like to see a city with you when we can travel for pleasure."', "journey"),
      c('"I want somewhere to return to. Make a home here if you want it too."', "home")),
    n("journey", "Arsinoe", '''"Then let us make an ambition of it, without pretending we have an available week in our pockets."
{n}She names two places, rejects a third for being too far, then restores it to the list because wishing to go somewhere ought not require immediate arrangements.{/n}
"I would like to arrive somewhere with you and be asked whether we want supper. Not whether we have come to solve the city's oldest grievance. We may look at the grievance after breakfast, if it is particularly interesting."
{n}On the way back she tells you which acquaintance might take the temple work. The woman has wanted a new appointment for some time. Arsinoe will write an introduction, making it very clear that an introduction does not commit either party.{/n}
"I am going to remain," she says. "I wanted to see whether saying it made the road seem to close. It does not."
{n}She walks the rest of the way with an ease that has little to do with the repaired paving.{/n}''',
      c('"Keep the possibility of a journey together."', flags=("arsinoe.staying_chosen", "arsinoe.future_journey"))),
    n("home", "Arsinoe", '''"I do. A room I arrange because I intend to enjoy it, without asking whether that is a sufficient justification for taking up the space."
{n}She considers the idea as you walk.{/n}
"I should like you to feel welcome there. I do not mean that you must move your life into my room. I mean that I want there to be a place where your arrival can be a pleasure before it becomes an occasion."
{n}She has someone in mind for the distant temple work, an acquaintance who has been looking for a new appointment. She will write an introduction and let them discover whether they suit each other.{/n}
"Then I shall answer the first letter. I am remaining. I have work here, and I like my life here, and apparently I needed to hear myself say the second part without disguising it as the first."
{n}At the market she stops to examine a plain window latch. It would fit the troublesome one in her room. She buys it before she can turn the purchase into another decision about the rest of her life.{/n}''',
      c('"Walk back with her and the new latch."', flags=("arsinoe.staying_chosen", "arsinoe.future_home"))),
], "arsinoe_what_she_asks", delay=72, chapters=(5,))


s("arsinoe_the_window_opens", "An evening she intends to keep",
  '"Have you written your answer?"', [
    n("start", "Arsinoe", '''"Yes. It was a much shorter letter once I stopped trying to explain why every other choice would have been defensible."
{n}Arsinoe has finished her work. She leads you to her room, where the window is open and the little stone face stands safely inside its recess. The air carries the smell of supper from another house.{/n}
"The latch works now. I hired someone who understood it instead of giving the matter another evening of my valuable attention. I am trying to remember the principle for other occasions."
{n}She sets a clean cushion on the wider chair. There is room beside her if you choose it, and another chair close enough for easy conversation.{/n}
"I have been asked whether I mean to stay because of the Commander. I gave an answer far too long for the question. Next time I shall say that I am staying because I have chosen to, and allow people to be disappointed by the lack of a simpler explanation."
{n}She looks at you with unmistakable warmth.{/n}
"You are among my reasons. I hope you enjoy being one of them."''',
      c('"I would like a quiet evening with my friend."', "friend", requires=("arsinoe.campaign_friend",)),
      c('"Sit with her. You have kept an evening without needing to hurry it."', "slow", requires=("arsinoe.campaign_slow",)),
      c('"Sit close to her. Let the evening take its time."', "near", requires=("arsinoe.campaign_lover",)),
      c('"I want to spend the night with you, if you want that too."', "night", requires=("arsinoe.campaign_lover",)),
      c('"I must postpone our evening."', abort=True)),
    n("near", "Arsinoe", '''{n}Arsinoe makes room for you and settles against your side. For a while you watch the light change on the opposite wall. She points out a repaired shutter, catches herself beginning an account of the repair, and asks what you have wanted to tell her instead.{/n}
{n}You talk about something small that stayed with you during the day. She asks a question, then another. When you ask about hers, she admits that she spent an unreasonable amount of time choosing the cushion.{/n}
"I wanted it to be comfortable. Then I wanted it to look as though I had not thought about its comfort for quite so long. The second ambition is where the trouble began."
{n}She laughs when you test it with exaggerated care. Her hand finds yours. Later she kisses you, gently at first, then again because neither of you has anywhere else you wish to be.{/n}
{n}When the evening ends, she walks you to the door. The window remains open behind her.{/n}
"Come again. I have decided not to require a new excuse every time I want this."''',
      c('"Promise another ordinary evening."', flags=("arsinoe.campaign_developed", "arsinoe.last_evening_kept"))),
    n("night", "Arsinoe", '''"I do. I have wanted to ask, and kept finding reasons to improve the room first. I think the room has had enough consideration."
{n}She comes close and lets you see the pleasure in her face before kissing you. Her hand rests against your shoulder. When she draws back, it is to ask what would make you comfortable, and to tell you what she likes without requiring you to guess.{/n}
{n}The lamp burns lower while you speak. There are moments of laughter, an awkward fastening she refuses to let spoil the mood, and then an unhurried closeness with no audience beyond the little stone face, which she finally turns toward the wall.{/n}
{n}Later, with the room quiet around you, Arsinoe reaches for your hand beneath the cover.{/n}
"I am glad you asked."
{n}In the morning she is reluctant to rise until the street becomes too noisy to ignore. She finds something to eat, objects to your account of who took more than a fair share of the cushion, and kisses you in the middle of the argument.{/n}
"There. Now you may go and be impressive. I have a customer who will insist that the price of a scroll has offended him personally. I expect to be equally impressive."''',
      c('"Leave with a kiss and the promise of another visit."', flags=("arsinoe.campaign_developed", "arsinoe.last_evening_kept", "arsinoe.night_shared"))),
    n("slow", "Arsinoe", '''{n}Arsinoe sits beside the open window and asks about your day. You tell her something you have been meaning to say, and find yourself adding another detail because she has asked the right question.{/n}
{n}Later she tells you about the letter she wrote. She had expected refusing the distant appointment to feel like an ending. Instead, it has left her wanting to arrange things in the room she intends to keep. She asks your opinion of a shelf, and accepts your disagreement without immediately defending the wall against it.{/n}
"I shall think about it. A remarkable concession, if you knew how much thought I had already given the matter."
{n}You remain until the light fades. At the door she smiles, openly pleased with an evening that has not required either of you to pretend the affection is further along than it is.{/n}
"Come again. We have not exhausted the subjects on which you are wrong about my furniture."
{n}She waits for your answer, then laughs and lets you go.{/n}''',
      c('"Agree to another evening."', flags=("arsinoe.slow_developed", "arsinoe.last_evening_kept"))),
    n("friend", "Arsinoe", '''"So would I. Sit where you like. I have already spent more time thinking about the chairs than either of them deserves."
{n}You sit beside the window while she pours. The conversation begins with the letter and wanders through matters neither of you planned to discuss. Arsinoe tells you an unflattering story about a purchase she made in another city. You ask whether she has ever been persuaded by an honest description.{/n}
"Frequently. Those make poorer stories. I am selecting for your entertainment."
{n}When the light begins to fade, she admits that she has been worried about remaining somewhere after the novelty of being useful has passed. You remind her of the people who will happily find work for her. She throws a folded cloth at you, missing deliberately enough to preserve her dignity.{/n}
{n}At the door she asks you to return before you acquire another important reason to do so. There is affection in the request, and no hidden condition waiting to turn it into a different kind of invitation.{/n}''',
      c('"Agree to visit your friend again."', flags=("arsinoe.friendship_developed", "arsinoe.last_evening_kept"))),
], "arsinoe_where_she_stays", chapters=(5,))


def ending(id, title, text, requires, forbids=(), owner="Epilogue"):
    SCENES.append(scene(id, title, owner, 1, "",
        [n("end", "Narrator", text, portrait="Arsinoe")],
        requires=requires, forbids=forbids, last=6, Relationship="arsinoe"))


ORDINARY = ("arsinoe.closed", "swarm", "true_lich", "sacrifice", "ascended")
ending("arsinoe_ending_kept", "A city with an open window", '''{n}Arsinoe remained in Drezen by choice. The work was plentiful, and she continued to disagree with those who assumed a priest of Abadar would be satisfied merely because a sum balanced. Some transactions were foolish at any price. Some improvements were worth making before anyone knew how to profit from them.{/n}
{n}The Commander knew the room behind her working space, the little carved face, and the window Arsinoe preferred to leave open. There were invitations made with days to spare and visits that began with a knock when both happened to be free. Promises did not arrange those evenings for them. They arranged them, sometimes badly, and learned to say when they minded.{/n}
{n}Arsinoe still looked up when someone described a city she had never seen. She wanted journeys, and a life that did not have to be packed away every time she took one. The Commander had heard that desire before making a place beside her. When roads were discussed, she expected to participate in choosing them.{/n}
{n}The repaired passage became ordinary enough to go unnoticed. Arsinoe would occasionally pause on its third step and smile. When the Commander asked what had amused her, she sometimes answered with the whole story and sometimes with a kiss.{/n}''',
    ("arsinoe.committed", "arsinoe.campaign_developed"), ORDINARY)
ending("arsinoe_ending_open", "The invitation she renewed", '''{n}Arsinoe and the Commander kept the affection they had chosen without turning it into a promise neither had made. An invitation could be accepted, postponed, or honestly refused. Arsinoe disliked a refusal less than a week spent preparing for someone who had never intended to come.{/n}
{n}She remained in Drezen and made the room by the window increasingly her own. The Commander knew where to sit, which cup she preferred, and how quickly an innocent remark about a building could become an argument worth enjoying. Some visits ended at the door. Others lasted longer. She kept asking what they wanted, even after she had become good at guessing.{/n}
{n}There were possibilities beyond the arrangement. Arsinoe did not pretend otherwise. For the time being, she liked the pleasure of hearing a familiar arrival and finding that she still wanted to open the door.{/n}''',
    ("arsinoe.open_future", "arsinoe.campaign_developed"), (*ORDINARY, "arsinoe.committed"))
ending("arsinoe_ending_unfinished", "The evenings still to come", '''{n}Arsinoe and the Commander had chosen to keep seeing each other without promising a settled future. The campaign had left fewer opportunities than she wanted. She missed the company, and sometimes resented having to be reasonable about the reasons for another delay.{/n}
{n}One morning she began a note while waiting for a customer. She meant to offer an evening, but found herself describing something amusing that had happened in the street. By the time she reached the invitation, the page was nearly full.{/n}
{n}Arsinoe read it over, crossed out an unnecessary apology for its length, and sent it. There were still things she wanted to hear from the Commander. She hoped the answer would include a day when they could sit together.{/n}''',
    ("arsinoe.open_future",), (*ORDINARY, "arsinoe.campaign_developed", "arsinoe.committed"))
ending("arsinoe_ending_promised", "The promise before the next visit", '''{n}Arsinoe and the Commander had chosen a lasting courtship before the last campaign left them with arrangements still to make. She remembered the promise clearly. So, on difficult days, did the Commander. It did not provide a date for the next visit, but it gave the waiting a question they intended to answer together.{/n}
{n}Arsinoe kept the small stone face by her window. Once, while dusting beneath it, she caught herself rehearsing what she would say when the Commander arrived. The conversation went exceptionally well in the empty room. She laughed, put the cloth away, and wrote a note that left room for an answer she had not supplied.{/n}
{n}She wanted the next evening. She wanted the difficult conversations that would come after it, although she suspected she would occasionally need reminding of that ambition. For now she sent the invitation and went back to work, listening more closely than usual whenever someone approached.{/n}''',
    ("arsinoe.committed", "arsinoe.campaign_lover"), (*ORDINARY, "arsinoe.campaign_developed"))
ending("arsinoe_ending_friend_waiting", "A letter to a friend", '''{n}Arsinoe had enjoyed the Commander's friendship enough to want more of its ordinary visits. The campaign had not obliged her by providing all the time she requested. She complained about this in a letter, then supplied an account of the latest disagreement in the repaired passage.{/n}
{n}She had work to do and decisions of her own still to make. It pleased her to have someone she wanted to tell about them. At the end of the letter she asked what had been occupying the Commander, adding that accounts of quite unimportant matters would be especially welcome.{/n}''',
    ("arsinoe.campaign_friend",), (*ORDINARY, "arsinoe.friendship_developed"))
ending("arsinoe_ending_slow_waiting", "The question she left open", '''{n}Arsinoe had agreed to take her time with the Commander. The campaign made some of that patience harder than either had intended. She missed the evenings they had managed to keep, especially the pleasure of asking a question and listening as the answer became more interesting than she expected.{/n}
{n}She wrote when she had something to say. Sometimes it was a small piece of news; sometimes she admitted that she would rather be talking in person. She did not make each invitation carry a demand for greater intimacy. She wanted another visit, and left the Commander room to want it too.{/n}''',
    ("arsinoe.campaign_slow",), (*ORDINARY, "arsinoe.slow_developed"))
ending("arsinoe_ending_friend", "A friend who knew the long way", '''{n}The Commander became someone Arsinoe could invite without finding an important reason first. She had friends in many places, but this one knew how she had acquired the skeptical stone face by her window and why she sometimes tested a perfectly dry step with unnecessary care.{/n}
{n}Arsinoe enjoyed being able to tell an unflattering story about herself without having it treated as a surprising confession. She also enjoyed hearing the Commander's stories, especially the ones in which victory required less courage than admitting a mistake.{/n}
{n}There were more afternoons to arrange, and more opinions to dispute. She looked forward to both.{/n}''',
    ("arsinoe.friendship_developed",), ORDINARY)
ending("arsinoe_ending_slow", "Time they had chosen to take", '''{n}Arsinoe and the Commander had kept their affection at a pace they could honestly enjoy. There was warmth in the invitations, interest in the questions, and no promise that a later evening owed them an answer different from the one they had already given.{/n}
{n}Arsinoe made a life in Drezen with work she valued and company she wanted to keep. The Commander had a place among those invitations. She sometimes found herself planning a visit before asking whether it was possible, then laughed and began with the question.{/n}
{n}She still wanted to hear the answer. That was reason enough to send it.{/n}''',
    ("arsinoe.slow_developed",), ORDINARY)
ending("arsinoe_ending_parted", "The room after a goodbye", '''{n}Arsinoe let the courtship end. It took longer to stop expecting another private invitation than she would have liked, but she did not ask the Commander to supply one merely to make the disappointment easier.{/n}
{n}The repaired passage remained useful. The little face remained by her window. Neither required her to pretend that every memory attached to them was pleasant, or that a pleasant memory made the goodbye a mistake.{/n}
{n}In time she found herself wanting company for reasons that had nothing to do with proving she had recovered. She made an invitation of her own.{/n}''',
    ("arsinoe.parted",), ("swarm", "true_lich", "sacrifice", "ascended"))
ending("arsinoe_ending_sacrifice", "The cup left on the table", '''{n}The Commander's sacrifice left Arsinoe with questions that could no longer be answered in the room where she had meant to ask them. She could understand the value of what had been won and still resent being expected to find that understanding sufficient.{/n}
{n}She missed a particular arrival, a voice, the pleasure of explaining something and discovering that the Commander had noticed a detail she had missed. Her work continued. On some days it helped. On others she found herself setting out a second cup before remembering why there would be no visit.{/n}
{n}Arsinoe did not throw the cup away. Eventually she used it for another guest, then felt foolish for crying while she washed it afterward.{/n}''',
    ("arsinoe.campaign_lover", "sacrifice"), ("arsinoe.closed", "swarm", "true_lich", "ascended"))
ending("arsinoe_ending_ascended", "An invitation on a different scale", '''{n}The Commander's ascension did not settle Arsinoe's future by enlarging it without her consent. She had chosen affection for a person she could speak to, disagree with, and ask to return. She remembered that choice without mistaking it for a vow to follow wherever power might lead.{/n}
{n}There was still a priest of Abadar with work to do, a city to live in, and a room whose window she preferred open. If the Commander could reach her across the distance that now separated their lives, there would be questions before there were promises.{/n}
{n}She would want to know whether a visit was possible. She would also want to know whether the visitor still remembered how to spend an evening without improving the world.{/n}''',
    ("arsinoe.campaign_lover", "ascended"), ("arsinoe.closed", "swarm", "true_lich"))
ending("arsinoe_ending_changed", "A history power did not preserve", '''{n}The Commander's transformation carried their life beyond the terms of Arsinoe's courtship. Earlier affection did not supply an answer to what had come afterward. Her willingness to serve a city, or to continue duties she believed her god required, could not be counted as a renewed romantic invitation.{/n}
{n}There had been real evenings together. Remembering them could give the loss a shape. It could not make the woman who had chosen them agree to a different future without being asked.{/n}''',
    ("arsinoe.campaign_lover", "true_lich"))
ending("arsinoe_ending_swarm", "A service that was never a vow", '''{n}Whatever duties kept Arsinoe at her work under the Swarm, they were not the answer she had given during an ordinary evening of courtship. Service did not renew intimacy. The Commander could possess the circumstances around her without thereby possessing her consent.{/n}
{n}The affection that had once made another visit worth anticipating remained part of a different history. No remembered promise made the present arrangement its fulfillment.{/n}''',
    ("arsinoe.campaign_lover", "swarm"), ("true_lich",))
ending("arsinoe_ending_aeon", "A city outside their shared hours", '''{n}The rewritten world had no obligation to preserve the particular evenings in which Arsinoe and the Commander had learned to want each other's company. Their repair, their conversations, and the room they had known belonged to a history the change did not leave intact.{/n}
{n}Arsinoe's life beyond it was her own. A different meeting might have become many things, but none could be claimed by reciting an invitation she had never made in that world.{/n}''',
    ("arsinoe.campaign_lover",), owner="AeonEpilogue")
