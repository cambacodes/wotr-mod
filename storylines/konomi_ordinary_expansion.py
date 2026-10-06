"""Played retained-office Chapter 5 evenings; no native policy or career mutation."""
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ANSWERS = "0dc8b8604bb33c846a63f3eb62443674"
SCENES = []


def s(id, title, entry, nodes, after, delay=24):
    for page in nodes:
        page["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 5, entry, nodes,
        Relationship="konomi", Chapters=[5], Areas=[DREZEN], AnswerLists=[ANSWERS],
        requires=("konomi.present", "konomi.power", "konomi.committed", *after),
        forbids=("konomi.closed", "konomi.dismissed", "inhuman", "konomi.ordinary", "konomi.farewell"),
        ForbidOverrides={"konomi.ordinary": "konomi.ordinary_expansion_requested", "konomi.farewell": "konomi.ordinary_expansion_requested"},
        delay=delay, optional=True))


SCENES.append(scene("konomi.another_evening", "An invitation after the promise", "Konomi", 5, "", [
    n("start", "Narrator", """{n}Konomi sends a small folded invitation. The address is a merchant's supper room, and she has added a line below the hour.{/n}
"I have an argument to make and would enjoy your company. Those are separate inducements. I cannot promise you will find both equally attractive.
"We have made plans together. I would like to begin doing some of the things that will inconveniently fill them. Can you spare several evenings? The first involves a woman who thinks I have underestimated the usefulness of sleep."
{n}There is a second note about what will be served. She has underlined the less promising dish.{/n}""",
      c('[Accept the invitation and make time for the following evenings.]', flags=("konomi.ordinary_expansion_requested",)),
      c('[Leave the invitation until you can offer the time.]', abort=True), portrait="Konomi"),
], Relationship="konomi", Remote=True, ManualOnly=True, Chapters=[5], Areas=[DREZEN],
    requires=("konomi.present", "konomi.power", "konomi.committed", "konomi.ordinary"),
    forbids=("konomi.closed", "konomi.dismissed", "inhuman", "konomi.ordinary_expanded"), optional=True))


s("a_useful_supper", "The price of a quiet street", '"You mentioned an invitation."', [
    n("start", "Konomi", """{n}Konomi holds two gloves in one hand and a folded sheet in the other. When you enter, she looks from the sheet to your clothes.{/n}
"Good. You have come dressed as someone who intends to sit down. I had feared we would have to find another chair for your importance."
{n}She gives you the page. It contains an address, four names, and a sketch of two adjoining yards.{/n}
"Varine rents storage to civilian traders. She wants their wagons unloaded in the evening, after the street is less crowded. Oselda keeps the accounts for three of the tenants. She wants to know when the people above those yards are expected to sleep. They have asked me to help them agree on a trial."
"And you have already agreed with one of them."
"I have already thought about it. Those conditions are often confused."
{n}She puts on one glove, tugging each finger into place.{/n}
"The wagons currently wait half a day to turn into that street. Food sits beneath tarpaulins. Drivers charge for waiting. We could avoid some of it by unloading later."
"At what cost to the sleepers?"
"That is what Oselda asks. With rather less charm, though I suppose she has had practice."
{n}Konomi lays the second glove across her wrist.{/n}
"Come and hear her. You needn't agree with me because you came with me. I reserve the right to be annoyed if your reasons are poor.\"""",
      c('"Then make sure I hear hers before you tell me how to answer."', "walk"),
      c('"I intend to have supper with you. The argument will have to earn my attention."', "walk"),
      c('[Ask her to postpone until you can stay for the discussion.]', abort=True)),
    n("walk", "Konomi", """{n}On the way she tells you how she met Varine. The merchant once asked for an introduction to a family whose name she had spelled incorrectly on the request. Konomi returned it with the spelling corrected and no introduction.{/n}
"She sent another request. The name was right. The reasons were better. I found that encouraging."
"You like persistence."
"When it learns something. Otherwise it is simply noise that has acquired a schedule."
{n}You reach the narrow steps beside the storage doors. Konomi pauses to inspect a broken strip of plaster above them.{/n}
"There are people I would like Varine to introduce me to. She hears things before they become proposals. I would rather be useful to her than exchange compliments over a dead plant."
"Is this official work?"
"An evening's advice. No order from Drezen. No promise that anyone else must accept the result. She has offered supper, and her cook takes a sufficiently dim view of us to keep the obligation modest."
{n}Her fingers settle briefly at your elbow.{/n}
"I also wanted to spend the evening with you. I realize I have concealed that desire beneath a warehouse, but it is there."
"I shall look for it."
"Try the chair beside mine.\"""", c('[Follow her upstairs.]', "table")),
    n("table", "Narrator", """{n}Varine is a broad woman wearing a silver ring too tight for her hand. She turns it whenever anyone mentions the weather. Oselda, lean and neatly dressed, moves her chair before introductions are finished so the serving woman can get through with the bowls.{/n}
{n}The fourth place belongs to a driver named Hesset, whose coat has been brushed so fiercely that its seams look injured. He rises for you; Konomi points out that the soup is escaping his bowl. He sits down in time to save most of it.{/n}
"I have invited the Commander as my guest," {n}she says.{/n} "Our advice is still advice. Varine owns the lease. Hesset owns his wagon. Oselda appears to own the only spoon without a bent handle."
"I came early," {n}Oselda says.{/n}
{n}Konomi inspects her own spoon and acknowledges the advantage.{/n}
{n}Varine explains the proposal. Six wagons would enter after the neighboring shops shut. Each merchant would pay a porter for the evening rather than leave a driver waiting through the day. The entrance would be cleared before dawn.{/n}
"The rooms above are occupied," {n}Oselda says.{/n}
"I know. I collect the rent."
"Then you know the woman over the west gate begins work before sunrise. And that Hesset sometimes sleeps in his wagon. Which will be standing beside the other wagons."
{n}Hesset lowers his spoon.{/n}
"I hadn't got to that part."
{n}Varine looks toward Konomi. She does not immediately supply an answer.{/n}""", c('[Ask what it would take for each of them to agree.]', "needs")),
    n("needs", "Konomi", """"Hesset?"
"A time I can depend on. I can sleep somewhere else if I know before I get there. It is waiting that ruins me."
"Oselda?"
"A night somebody actually hears. No deciding from this room that the courtyard sounds tolerable. It always sounds tolerable from this room."
{n}Varine objects that she has stood in the yard herself. Oselda asks whether she stood there while six carts were being unloaded. Varine turns her ring and admits that she has not.{/n}
"One wagon," {n}Konomi says.{/n} "Tomorrow evening. One unloading, with the porter paid for his time. We listen downstairs and upstairs. Then we decide whether six are possible."
"Tomorrow?" {n}you ask.{/n}
"I have been accused of making an attractive guess. I should like to improve it before everyone learns to enjoy the accusation."
{n}Oselda studies her, then names a tenant who has agreed to let them into the upper passage. Hesset can bring empty barrels. Varine will provide the porter and a lamp.{/n}
"Nobody needs to lose a night's sleep to prove they would," {n}Oselda adds.{/n} "We stop when the people upstairs ask."
"Agreed," {n}Konomi says, before Varine can negotiate with the word stop.{/n}
{n}The serving woman brings a covered dish. Its smell answers the question Konomi underlined on your invitation. She moves it a little farther from your plate.{/n}
"There. I have saved you from one poor decision tonight. You may make the others yourself.\"""", c('[Agree to meet them for the trial.]', flags=("konomi.supper_trial",))),
], after=())

s("the_upper_passage", "What reaches the rooms above", '"Shall we see what the yard sounds like?"', [
    n("start", "Narrator", """{n}Hesset has arrived early, which makes him impatient before anyone else has had an opportunity to be late. His wagon carries four empty barrels and a crate of loose wooden pegs. Varine has paid a porter named Bel to move them into the store and back.{/n}
{n}Konomi wears a plain cloak over her good coat. Oselda leads you through the yard to a stair door, carrying the borrowed key.{/n}
"This is Sella's passage," {n}she says.{/n} "She has her sister's children tonight. If she comes out, we finish."
{n}Konomi nods. A child's voice behind the nearest door asks whether that was a horse. Another voice says it was certainly not a horse and therefore should be ignored.{/n}
"A promising beginning," {n}Konomi murmurs.{/n}
{n}Below, Hesset calls to Bel. The first barrel lands on a plank with a hollow crack. Sound seems to run up the wall beneath your hand.{/n}
{n}Oselda does not look at Konomi. Her restraint is almost impolite.{/n}
"Yes," {n}Konomi says.{/n} "I heard it."
"There are five more wagons in your proposal."
"I also remember arithmetic."
{n}She says it too sharply. After a moment she adds,{/n} "That was unnecessary. Shall we find out which part is making the worst of it?\"""",
      c('[Listen along the passage while the next barrel is moved.]', check=dict(Skill="SkillPerception", DC=26, Success="hear", Failure="miss", CommanderOnly=True)),
      c('"Let us ask them to repeat each movement separately. It will take longer, but we can compare them."', "slow"),
      c('[Ask them to pause while you attend to something else.]', abort=True)),
    n("hear", "Narrator", """{n}You hear the wheel creak and the barrel strike, but the loudest report comes a moment afterward. A loose end of the loading plank jumps against an iron bracket. You ask Bel to hold it down while Hesset moves the next barrel.{/n}
{n}The crack disappears. The wagon remains audible, and there is still the scrape of wood, but it no longer sounds as though someone has struck the wall with a mallet.{/n}
"There," {n}Konomi says.{/n} "We have at least found an expense worth naming."
{n}Oselda tests the wall herself. She nods, then points toward the closed door.{/n}
"Less noise is not silence."
"No. But I would rather offer a repair than a promise to be quiet."
{n}Konomi calls down to ask Varine what it would cost to secure the plank properly. Varine says very little, which Bel contradicts with the confidence of the person expected to do it.{/n}""", c('[Go down to hear Bel explain the repair.]', "repair")),
    n("miss", "Narrator", """{n}You name the wagon wheel. Hesset lifts its edge with a lever and has Bel move a barrel while it is clear of the stones. The crack returns, just as loud.{/n}
"The wheel is innocent," {n}Hesset calls.{/n} "It would like that entered somewhere."
{n}Konomi presses her lips together. For a moment you think she is trying not to be annoyed. Then she turns away, shoulders moving, and you realize she is laughing.{/n}
"I apologize," {n}she tells Oselda.{/n} "It has had a difficult evening."
{n}They lower the wagon and repeat the movements separately. The loose loading plank finally jumps against its iron bracket. Bel puts a foot on it, and the next barrel passes with a dull scrape.{/n}
{n}The repeated unloading has taken long enough that the door opens. Sella stands there with a child asleep against her shoulder. She need not say anything. Oselda signals below, and the yard falls quiet.{/n}
"We have finished," {n}Konomi tells her.{/n} "Thank you for the time."
{n}You go downstairs to settle the repair and the porter's extra work without another trial.{/n}""", c("[Listen to the porter explain what would be needed.]", "repair_late")),
    n("slow", "Narrator", """{n}Oselda repeats your request downstairs. Hesset moves the wagon a little. Bel lifts a barrel, sets it down, then rolls it slowly along the plank. Konomi tells him when to stop and asks you whether the sound changed.{/n}
{n}On the fourth attempt the end of the plank springs upward against its bracket. Bel holds it with his boot, and the next movement loses its sharp report.{/n}
"There," {n}Konomi says.{/n} "A repair, rather than an instruction to make less noise. I prefer problems that can be fastened to something."
{n}The door opens before you can try again. Sella has a sleepy child against her shoulder. Oselda apologizes and signals that the trial is over.{/n}
"We said we would stop," {n}Konomi tells Varine when the merchant looks up from below.{/n} "We have learned enough for tonight."
{n}You descend together. Bel has worked past the time he was hired for, and Varine begins counting the additional coins before Oselda can ask.{/n}""", c('[Ask Bel what a lasting repair would require.]', "repair_late")),
    n("repair", "Konomi", """{n}Bel wants two new supports and a carpenter who will fit them to the stone rather than nail another scrap over the old split. He names the cost. Varine turns her ring twice, then agrees to obtain an estimate.{/n}
"We have time to try carrying one barrel instead of rolling it," {n}Konomi says.{/n} "Only if Bel agrees, and only while the passage remains available."
{n}Bel agrees to one. The sound is gentler. His arms tremble before he has carried it back.{/n}
"And that," {n}Oselda says,{/n} "is why we shall not write that he can do it six times for the same wage."
{n}Konomi strikes a line from her page.{/n}
"I had written that three minutes ago. You may enjoy seeing it removed."
"I do."
{n}Konomi hands you the pencil. "If you intend to remember that, have the decency to help me measure the distance."{/n}""", c('[Measure the carrying distance with her.]', "early_end")),
    n("repair_late", "Konomi", """{n}Bel explains the loose supports. Fixing them would require a carpenter and proper fittings. Carrying barrels would be quieter, he admits, but nobody has paid him enough to pretend it would not hurt.{/n}
"Then I shall not write it as a saving," {n}Konomi says.{/n}
{n}She asks him to show her the route without a load. You walk beside them while Oselda measures the distance in paces. They stop twice to disagree about the easiest turn.{/n}
"We haven't tried the carrying," {n}Varine says.{/n}
"No," {n}Konomi answers.{/n} "We have tried the patience of the people upstairs. Tomorrow we can ask Bel what he would charge. We cannot ask his back to answer tonight."
{n}It is a useful answer. She still looks unhappy as she folds the page.{/n}
"I wanted a cleaner result," {n}she tells you, quietly enough that nobody else has to respond.{/n}""", c('"We learned where the costs are. That is a result."', "late_end")),
    n("early_end", "Konomi", """{n}When the others leave, you walk the length of the empty yard with Konomi. She checks her figures against yours, then asks to see your hands.{/n}
"A splinter. You acquired it while holding the rail."
{n}She removes it with the tip of a small pin, more carefully than she has treated any opinion tonight. Her fingers linger when she has finished.{/n}
"I had intended a rather more flattering evening. I would explain the proposal, you would admire its elegance, and nobody would strike the building with a barrel."
"You revised it. That was worth seeing."
"I hoped you might say that. I am trying not to arrange for you to say it twice."
{n}She turns your hand over and kisses the uninjured palm before releasing it.{/n}
"Come to the discussion. I should like you there even if the next version is imperfect too.\"""", c('[Agree to hear the revised proposal.]', flags=("konomi.yard_heard", "konomi.yard_precise"))),
    n("late_end", "Konomi", """"It is. I shall like it better after I have stopped wishing it were the result I brought with me."
{n}She looks toward the dark upper windows. The child has stopped asking about the horse.{/n}
"I was unfair to Oselda. She had done the work I thought I could improve in an evening. I dislike discovering that while wearing gloves I chose for being impressive."
{n}You offer your arm. She takes it, and after a few steps she begins to laugh at herself.{/n}
"Don't comfort me so efficiently. Give me a little time to enjoy being unreasonable."
"How much?"
"Until the corner. After that I should like to hear what you think we should propose."
{n}At the corner she stops, turns toward you and kisses you before you can begin.{/n}
"There. Now you may be useful.\"""", c('[Walk back with her and discuss the next meeting.]', flags=("konomi.yard_heard", "konomi.yard_slow"))),
], after=("konomi.supper_trial",))

s("two_bad_prices", "Who pays for the improvement", '"What will you propose to Varine?"', [
    n("start", "Konomi", """{n}The supper table has been cleared for Konomi's pages. Varine has supplied a better lamp. Oselda has brought a wooden ruler and a list of the upstairs tenants' working hours. Hesset brings nothing, which he describes as a deliberate professional choice.{/n}
"Two possible trials," {n}Konomi says.{/n} "Both smaller than the proposal we began with. I have decided not to call either inexpensive until someone else has paid for it."
{n}She places the pages side by side.{/n}
"One wagon in the first part of the evening, with the plank repaired and two porters. The upper rooms get a stated stopping time. Varine gets one wagon out of the street before the next day. Bel gets another pair of hands."
"Two wages," {n}Varine says.{/n}
"Yes. The alternative is a hired waiting space beyond the adjoining houses. The wagon waits there until morning. Oselda has found one. Varine pays for the space and a watch. Hesset does not charge a day's waiting because we agree his time in advance."
{n}Hesset lifts a finger. "A smaller waiting charge. I still have to eat while I know what time it is."{/n}
{n}Konomi corrects the page without disputing him.{/n}
"A smaller charge. Thank you. Those are the choices I can recommend on what we know."
"One costs money to move less," {n}Varine says,{/n} "and one costs money not to move."
"You have understood them perfectly.\"""",
      c('[Ask why Konomi prefers the evening trial.]', "preference"),
      c('[Ask why Oselda prefers the waiting space.]', "other"),
      c('[Ask them to wait until you can hear the discussion properly.]', abort=True)),
    n("preference", "Konomi", """"Because a narrow reliable opening can be enlarged later. If one wagon works, we can ask about two. Repairing the loading place is useful even if the trial ends. And Varine can see what her extra wages bought."
"You still want the proposal you began with," {n}Oselda says.{/n}
"I want a version of it that works. Do you think that is the same thing?"
"I think you can imagine the second wagon very easily. I want you to imagine the woman upstairs wondering whether she has agreed to the fifth."
{n}Konomi takes her hand away from the page.{/n}
"Then the agreement says that a larger trial needs a new answer. Hers as well as ours."
"It can say it. Will they ask?"
"Varine is sitting here. Ask her."
{n}The merchant looks irritated to have become the subject of her own discussion.{/n}
"For a week," {n}she says.{/n} "One wagon. If it does not work, I stop. If I want more, I ask."
{n}Oselda writes the words down. The small scratch of her pen gives the concession more weight than another exchange of assurances would have.{/n}""", c('[Ask what they would give up by choosing the other plan.]', "trade")),
    n("other", "Konomi", """{n}Oselda puts her ruler across the list of working hours.{/n}
"These people can arrange themselves around daylight. They have been doing it for years. Nobody has to watch a clock wondering when the noise will stop. The waiting space costs something, but it keeps the cost where we can count it."
"And leaves the road into the store crowded in the morning," {n}Konomi says.{/n}
"For one wagon, arriving at an agreed time. Your own smaller trial."
{n}Konomi looks at Hesset.{/n}
"Would that help?"
"It would. I don't need to be the first man through the gate. I need someone to mean it when they say when I can come."
{n}Konomi marks the waiting charge in the margin. She has been looking at the larger queue; Hesset has been looking at tomorrow's breakfast.{/n}
"Then I have been promising you a grander improvement than you asked for."
"I wouldn't refuse a grand one. I should like the small one while you arrange it."
{n}Oselda smiles without looking up. Konomi notices and allows it.{/n}""", c('[Ask what they would give up by choosing the evening trial.]', "trade")),
    n("trade", "Konomi", """{n}They work through the cost again. The evening plan could clear more deliveries eventually, but only if the noise and wages remain acceptable. The waiting yard gives up that immediate gain and pays a watch to keep the load safe. Neither will feed an idle driver for nothing.{/n}
{n}Varine asks for your opinion. Konomi leans back, leaving her pages where you can read them.{/n}
"You have stood upstairs," {n}she says.{/n} "You are entitled to disagree with me. I would prefer to hear why before everyone enjoys it too much."
"And if I agree?"
"Then I would still like reasons. I have had quite enough of people agreeing because it is cheaper than continuing the conversation."
{n}Oselda turns her ruler over. The white edge is worn smooth where her thumb rests. Hesset waits, looking from you to Varine rather than toward the door.{/n}""",
      c('"Try one evening wagon, with the repair, two paid porters and a firm stopping time. It is worth learning whether that opening can work."', "evening"),
      c('"Use the waiting yard. The predictable arrival helps Hesset now, and the neighbors keep their nights. I would pay for that certainty first."', "morning")),
    n("evening", "Konomi", """{n}Konomi nods once. She does not look at Oselda until the clerk has had time to put down her pen.{/n}
"I will draft the hours. Oselda, will you ask the people upstairs whether they will try them? You can show them the figures. There is no reason to make them guess what we hope to gain."
"And if they refuse?"
"Then we have learned that too. We still have your yard."
{n}Varine counts the proposed wages aloud. She dislikes them. She agrees to them. Hesset offers his next evening arrival, provided the carpenter has finished.{/n}
"The report should carry both our names," {n}Konomi tells Oselda.{/n} "Yours for the tenant hours and the alternative. Mine for the trial I have been so difficult about."
{n}Oselda looks up sharply.{/n}
"I was paid to keep the accounts."
"You have done something beyond them. I want a reader to know whom to ask about each part."
{n}Konomi gathers her gloves. Under the table, her foot touches yours and withdraws again before it becomes a claim on your attention.{/n}
"Now," {n}she says,{/n} "can we eat before Varine discovers a cheaper alternative?\"""", c('[Stay for supper after the agreement.]', flags=("konomi.trial_chosen", "konomi.evening_trial"))),
    n("morning", "Konomi", """{n}Konomi looks down at her proposal. For a moment she appears about to explain it again. Instead she asks Hesset what hour would keep his waiting charge small.{/n}
{n}They settle the arrival time. Varine will rent the space for the trial and pay the watch. Oselda will check that the route out of the yard is clear before accepting the first load.{/n}
"I would still repair the plank," {n}Konomi says.{/n}
"So would I," {n}Varine replies.{/n} "I have been hearing it ever since you made me listen."
{n}Oselda begins to gather the pages. Konomi keeps one back.{/n}
"Your name goes first on the recommendation. I will write why I changed mine."
"You needn't make a ceremony of it."
"I wasn't proposing one. I dislike an incomplete account even when it would be convenient for me."
{n}Her tone has an edge. Oselda hears it, but does not take the offered quarrel.{/n}
"Then I shall read your explanation before we send it."
"Naturally."
{n}Konomi finds your hand briefly beneath the table. She does not squeeze it, and she does not leave hers there. When the food arrives, she asks you to pass a dish instead of returning to the argument.{/n}""", c('[Stay with her through the less triumphant supper.]', flags=("konomi.trial_chosen", "konomi.morning_trial"))),
], after=("konomi.yard_heard",))


s("the_trial_day", "An improvement with a bill attached", '"How is the trial going?"', [
    n("start", "Konomi", """{n}Konomi has brought the two pages from supper, now folded into quarters and marked with a thumbprint that is plainly not hers.{/n}
"Varine touched them after checking the new supports. She has discovered that work becomes much more interesting when she can point to the part she paid for."
{n}She opens the pages along the old creases.{/n}
"We have a trial to watch. I have brought the original figures so that I cannot improve my memory of them afterward. You may consider yourself warned."
"Against what?"
"Allowing me to be vague. I can be very persuasive when nobody remembers what I actually proposed."
{n}She puts the pages away and offers her arm.{/n}
"Afterward, I would like to walk somewhere that does not need unloading.\"""",
      c('[Go with her to the evening unloading.]', "evening", requires=("konomi.evening_trial",)),
      c('[Go with her to the morning arrival.]', "morning", requires=("konomi.morning_trial",)),
      c('[Arrange to meet her at another time.]', abort=True)),
    n("evening", "Narrator", """{n}The people upstairs have agreed to the limited trial. Oselda has put the finishing hour on a board beside the gate. Bel works with another porter; neither appears particularly grateful for having been discovered to possess a back.{/n}
{n}The repaired plank still creaks. It no longer cracks against the wall. Hesset brings the wagon through, waits while the porters steady the load, and climbs down to help them release the first rope.{/n}
{n}Varine wants Konomi to see how quickly the entrance clears. Konomi asks Oselda whether the upper passage is available. It is not. Sella's sister has returned, and the room is full. They listen from the stair landing instead.{/n}
"We should say where we stood," {n}Konomi tells you.{/n} "The wall sounded different higher up."
{n}Bel calls that one of the casks has a damaged binding. The second porter fetches another rope. The extra care consumes the time Varine hoped to save. When the finishing hour arrives, two casks remain on the wagon.{/n}
"Ten minutes," {n}Varine says.{/n}
{n}Oselda turns toward her. Konomi closes her writing case.{/n}
"Tomorrow. We said when we would stop."
"They are already here."
"So are the people we asked to trust the hour."
{n}Hesset covers the remaining casks. He is displeased, but he has been paid for the agreed arrival and knows when the last part will be unloaded. The porters finish tying the cover and collect their wages.{/n}
{n}Varine watches them leave. "We paid two men to do less than one wagon."{/n}
"We did," {n}Konomi says.{/n} "Put that in the account beside the waiting charge we avoided. I would like to see both.\"""", c('[Stay while they compare the actual cost.]', "evening_cost")),
    n("morning", "Narrator", """{n}The waiting yard lies behind a small cooper's shop. Hesset's wagon occupies most of it. The watch has kept the gate clear and complains, with some pride, that there was nothing to do except remain awake.{/n}
{n}Konomi asks how he stayed warm. He shows her a brazier borrowed from the cooper, then names what he paid for the charcoal. Oselda adds it to the cost.{/n}
"We didn't allow for that," {n}Konomi says.{/n}
"Neither did I," {n}Oselda answers.{/n}
{n}Konomi gives her a look that might have become satisfaction on a less demanding morning. Then Hesset calls them to help open the gate.{/n}
{n}The wagon arrives at Varine's entrance at the agreed hour. A handcart stands across half the opening. Its owner has gone to buy bread. Varine sends a servant to find him, and the minutes begin accumulating exactly where nobody wished to see them.{/n}
"So much for certainty," {n}she says.{/n}
{n}Oselda's jaw tightens. Konomi walks the length of the handcart, sees that it can be shifted without touching the load, and asks Bel for help. They move it against the wall. Hesset turns carefully through the remaining space.{/n}
"A clear entrance has to belong to someone's morning," {n}Konomi says when she returns.{/n} "It won't happen because we put an hour on paper. Who will check it?"
{n}Varine names the servant who opens the store. Oselda writes it down and tells her to pay for the earlier start.{/n}
{n}The wagon is unloaded before the busiest part of the day. Hesset's waiting charge is smaller. The yard, watch, charcoal and earlier start consume most of the saving.{/n}
"Most," {n}Oselda says, checking the figures.{/n} "Not all."
{n}Konomi nods. "And the people upstairs had their night. We should include what we meant to buy."{/n}""", c('[Help compare the outcome with the original estimate.]', "morning_cost")),
    n("evening_cost", "Konomi", """{n}The remaining casks are small enough to unload the next morning without holding up another wagon. The evening trial saved some waiting and left a bill larger than Varine wanted. She agrees to finish the week, one wagon at a time, and asks for no expansion yet.{/n}
{n}Oselda writes the results beside Konomi's estimate. She does not offer to soften them.{/n}
"You were right to keep the hour," {n}she says.{/n}
"I would have liked to be right about something that made me appear cleverer."
"You can put that in the report too."
{n}Konomi actually considers it. Then she writes a plain account of the casks that remained on the wagon.{/n}
{n}On the way out, Bel stops her to ask who will read it. She tells him. He asks whether they will remember that the damaged binding cost time because he kept a cask from falling.{/n}
"I will put that beside the delay," {n}she says.{/n}
{n}He nods and goes back to the plank. Konomi watches him check the new supports with his heel.{/n}
"He wanted a sentence," {n}she says.{/n} "I nearly gave him a defense of the whole arrangement. You may rescue me if I begin doing that to you.\"""", c('[Walk with her away from the store.]', "walk")),
    n("morning_cost", "Konomi", """{n}Varine agrees to finish the week using the waiting yard. She wants the charcoal included in the next estimate and no more handcarts discovered at the last moment. Oselda says she can promise the first with more confidence than the second.{/n}
{n}Hesset leaves knowing where he will wait on his next visit. He shakes Oselda's hand, then thanks Konomi for moving the cart.{/n}
"There. I have finally made a contribution he can point to," {n}she tells you.{/n}
"You helped them agree."
"I know. I also held a wheel while Bel moved the other one. One of those things was harder to argue about."
{n}She flexes her fingers. Her glove has acquired a dark streak across the palm. She looks at it, then deliberately leaves it on.{/n}
"Oselda will write the recommendation. I shall write the comparison with the evening proposal. They should travel together."
"Are you disappointed?"
"In parts. I wanted them to choose my plan. I wanted a useful result. It is inconvenient that those wishes turned out to require separate answers."
{n}She takes your arm before you can offer it.{/n}
"I am less disappointed in the company. I am prepared to be quite definite about that.\"""", c('[Go somewhere quieter with her.]', "walk")),
    n("walk", "Konomi", """{n}You find shelter from the wind beside a closed stall. Konomi rests her gloved hands together and leans against the wall beside you, glad to have stopped moving.{/n}
"You were watching me at supper."
"You invited me to."
"I invited you to hear a proposal. I discovered afterward that I cared rather more about what you saw while I was defending it."
{n}She looks at you directly. The small composed smile has gone.{/n}
"In council I would have had that plank in my report and Oselda's name in a footnote. I nearly did it here. You watched me decide not to, and I found I wanted you to see it. That is a weakness, Commander, and I am telling you so you cannot sell it to anyone."
"Then sell it to me instead. What do you want, right now?"
"At present? Taking off this glove. And not having to draft the next part as a proposal. I have written enough proposals today."
{n}She begins working at the fastening. You wait until she has freed her hand, then take it.{/n}""",
      c('[Kiss her, and let the unhurried moment last.]', "kiss"),
      c('[Draw her beside you and stay with her in the shelter.]', "rest")),
    n("kiss", "Konomi", """{n}She steps into the kiss, one hand settling at your waist. When you draw back, she follows far enough to make you smile before remembering the open street.{/n}
"I had hoped that would be your answer. I was preparing something very composed in case it wasn't."
"Keep it. It may be useful another time."
"It was dreadful. You have spared us both."
{n}She draws off the other glove, folds them together and asks when you can see her again. The report will need an answer from Varine, but she is already thinking beyond it.{/n}""", c('[Arrange another evening.]', flags=("konomi.trial_lived", "konomi.trial_kissed"))),
    n("rest", "Konomi", """{n}She rests her shoulder against yours. For a while the quiet does more for her temper than another successful argument could have done.{/n}
"This is satisfactory," {n}she says eventually.{/n}
"Such enthusiasm."
"I thought you might enjoy a favorable finding without an argument attached."
{n}Her hand closes around yours. She stays until you have both stopped listening for someone to call you back, then asks when you can see her again. There will be an answer from Varine about the report. After that, she says, she would like an evening nobody has asked her to improve.{/n}""", c('[Make time to see her again.]', flags=("konomi.trial_lived", "konomi.trial_rested"))),
], after=("konomi.trial_chosen",), delay=48)

s("a_name_beside_hers", "The readers she wanted", '"Has Varine answered about the report?"', [
    n("start", "Konomi", """{n}Konomi has put Varine's reply beneath a heavy glass cup. She lifts the cup when you arrive, then decides to finish the water before speaking.{/n}
"She liked the report. She has sent it to two people who manage properties outside Drezen. One wants regular accounts of small arrangements like this. He says they are more useful than another splendid declaration about commerce."
"You wanted readers."
"I did. These are readers who can introduce me to others. I am attempting to enjoy that before I tell you the rest."
{n}She gives herself the length of one breath.{/n}
"He wants one voice. Mine. Oselda's figures attached beneath, but no separate correspondence with her. He calls it a matter of convenience."
"What does she call it?"
"An offer she has not yet answered. I thought it best to ask. We are meeting her here."
{n}Konomi shifts the glass to an empty patch of table.{/n}
"I know what you are about to say."
"Do you?"
"No. But I like you to believe I do. It saves us both time."
{n}A knock saves her from further practice. Oselda enters carrying the draft they sent together. She has made notes in a different color, leaving very little margin unused.{/n}""",
      c('[Make room for her draft.]', "offer"),
      c('[Ask to postpone the discussion until you can remain.]', abort=True)),
    n("offer", "Konomi", """"I could use the work," {n}Oselda says.{/n} "I could also use a reader who knows when to ask me a question. They are not necessarily the same employment."
"I would pass the questions on."
"Would you pass on the ones you thought you could answer?"
{n}Konomi's reply stops before she speaks it. Oselda places a finger on the trial account.{/n}
"You write more persuasively than I do. I know why they want you. But a tenant asking about a loading hour will tell me things she won't tell a letter signed Lady Konomi. If the reader never hears that, your next account will be worse."
"You would like your own access."
"Yes. I would also like the fee. I am not inviting you to admire me for refusing it."
{n}Konomi reads the offer again, more slowly.{/n}
"Then we offer two arrangements. Joint private reports, with both names and an address for each. I introduce you in the first letter. If they refuse that, a short public circular. Varine can send it to her tenants and acquaintances. Anyone who wants to ask us about it can write."
"No regular fee for the second," {n}Oselda says.{/n}
"No promised fee. We could charge for copies beyond the first distribution, if there is interest. It would begin modestly."
"And you would lose your private introduction."
"I would lose the guarantee of being the first person they ask. I haven't decided that I like either possibility."
{n}Oselda sits back. "Now we have something to discuss."{/n}""", c('[Ask what each arrangement would demand of their time.]', "time")),
    n("time", "Konomi", """{n}The private reports would require an answer on a fixed day. Each woman would write the parts she knew, then they would argue over the conclusions before sending them. The offered fee could pay for Oselda's time away from other accounts and a portion of Konomi's evenings.{/n}
{n}The circular could wait until they had something worth saying. It would travel farther through Varine's acquaintances, but neither writer would control which reader received it next. There would be no claim on an evening merely because a payment was due.{/n}
"My office comes first," {n}Konomi says.{/n} "What reaches me as the crown's envoy is the crown's stock, and I do not sell the crown's goods out of my own stall. It is the quickest way I know to be recalled. We write what the yard told us, and nothing else. If the two collide, this work waits."
"Then put that in the offer," {n}Oselda answers.{/n} "I would rather discover what waiting means before I depend on the fee."
{n}They write a limit on the number of reports. Konomi strikes out a phrase promising prompt answers and replaces it with the days she can actually offer.{/n}
"That is less flattering," {n}she says.{/n}
"It is easier to arrange my week around."
{n}Konomi turns toward you.{/n}
"These would be some of the evenings we discussed. I want the work. I want time with you. I could make an impressive speech about reconciling them and then cancel our next supper. I would prefer a less elegant beginning."
"What beginning?"
"Tell me which cost you think I am pretending not to mind. Then I shall decide whether you are right.\"""",
      c('"You want the private readers and the steady work. Ask for joint terms. I can arrange around a few definite evenings better than an ambition you keep setting aside for me."', "joint"),
      c('"You want room to choose your subjects. The circular gives you that, even if the first readers impress you less. Try it before you sell a regular evening."', "circular")),
    n("joint", "Konomi", """"I do want them. I have been trying to make that sound like a duty, which was dishonest of me."
{n}She turns the letter over and begins a new draft. Oselda watches until Konomi reaches the sentence inviting questions to both writers. Then she moves her chair closer and corrects the address.{/n}
"You can send it," {n}Oselda says when they have read it aloud.{/n} "If they answer only you, I expect to see what they asked."
"You will. And if you answer before I do, I expect not to discover it from the next question."
"Agreed."
{n}They decide which evening each will keep for writing if the offer is accepted. Oselda leaves with a copy. Konomi seals the other and puts it where her outgoing private letters wait.{/n}
"I have not won the work yet," {n}she says.{/n} "I dislike how much I want their answer."
"What would you like while you wait?"
"Something very unhelpful to my professional composure. Your undivided attention, for a start. After their answer comes, I shall send you an invitation. I shall obtain something better than Varine's supper."
{n}She touches your sleeve, then lets her hand slide down until your fingers meet.{/n}
"I would like that even if they refuse.\"""", c('[Agree on an evening that belongs to you both.]', flags=("konomi.readers_answered", "konomi.joint_offer"))),
    n("circular", "Konomi", """{n}Konomi reads the private offer once more. Then she lays it aside, carefully enough to show that doing so costs her something.{/n}
"I want to choose. I also want them to be impressed. You have identified an inconvenient disagreement."
{n}Oselda asks how long the circular would be. Konomi names a length. Oselda looks at the marked pages between them until she names a shorter one.{/n}
"We begin with what happened in the yard," {n}Konomi says.{/n} "Actual costs, the inconvenience we missed, and what we have not yet learned. Both names. Varine may distribute it with her own letter, provided she doesn't change ours."
"I can finish my part in two evenings."
"So can I. I shall have to resist improving it on the third."
{n}They divide the work. When Oselda leaves, Konomi opens her reply to the private offer and declines the regular arrangement. She offers to send the circular instead.{/n}
"That was a smaller answer than I imagined giving this morning. I am going to be dissatisfied with it until I have written something I prefer."
"Would company interfere?"
"While I write, yes. After the circular has gone out and the first answers are back, I hope it will. Quite thoroughly."
{n}She catches your hand before you can take that as a dismissal.{/n}
"I am asking you to supper. I shall send you a time when we can make a proper evening of it.\"""", c('[Promise to arrive for supper, and let her finish the draft.]', flags=("konomi.readers_answered", "konomi.circular_offer"))),
], after=("konomi.trial_lived",))

s("the_evening_she_kept", "After the answer arrived", '"You asked me to come to supper."', [
    n("start", "Konomi", """{n}Konomi opens the door before you knock a second time. The room smells of toasted bread and pepper. A covered dish waits on the table beside two cups that actually match.{/n}
"You are on time. I have spent the last five minutes finding that increasingly unreasonable of the clock."
{n}She takes your hand and leads you inside. Her coat hangs over a chair. Without it, the movement of her shoulders looks less guarded, as though she has finally set down something she had forgotten she was carrying.{/n}
"There is an answer about the writing. I want to tell you before supper. Then I intend to be interested in something else."
"You have scheduled your interests."
"I have ambitions. We shall see whether they survive the first cup.\"""",
      c('[Ask about the joint offer.]', "joint_reply", requires=("konomi.joint_offer",)),
      c('[Ask about the circular.]', "circular_reply", requires=("konomi.circular_offer",)),
      c('[Apologize and arrange another evening when you can stay.]', abort=True)),
    n("joint_reply", "Konomi", """"They agreed to two reports as a trial. Both names, separate replies, the limits we wrote. They reduced the fee."
"By how much?"
"Enough that Oselda was offended. Not enough that she refused. She sent them an extremely polite account of what the original work would have cost. I enjoyed reading it."
{n}Konomi brings the cups to the table.{/n}
"We have one evening to prepare each part, and one to disagree before we send it. Mine are here. Hers are wherever she can escape her other clients. We will exchange copies through Varine's carrier."
"Are you pleased?"
"Very. I would have liked to appear less pleased when I wrote back. I crossed out three unnecessary compliments and left one because it was true."
{n}She sits, looking for a moment exactly as pleased as she has admitted.{/n}
"They addressed their first question to Oselda. I have survived. I may become very tiresome about having survived."
"I shall prepare myself."
"Do. I have been looking forward to telling you.\"""", c('[Share her pleasure before the meal.]', "supper")),
    n("circular_reply", "Konomi", """"Varine had six copies made. One reader asked for the longer comparison. Another asked whether Oselda would look at an account for him. Nobody has asked me to lead a splendid new enterprise."
"An unforgivable delay."
"I am showing restraint."
{n}She sets the cups down and sits opposite you.{/n}
"The man who offered the private reports wrote that he was sorry. A short letter. No attempt to make me reconsider. I found that much more annoying than it deserved."
"You wanted him to ask again."
"I wanted him to reveal that I had been worth a better offer all along. It was a childish wish. I have allowed myself until the end of this sentence to enjoy it."
{n}She lifts her cup, drinks, and puts it down.{/n}
"I like what we wrote. Someone can read it without owing me an introduction. That has its own uses. I have begun a page on another small arrangement, and Oselda has already found the question I avoided."
"Will you answer it?"
"Tomorrow. I have a prior engagement tonight.\"""", c('[Ask whether the engagement includes the covered dish.]', "supper")),
    n("supper", "Konomi", """{n}The dish contains sliced mushrooms beneath a crisp covering. Konomi serves it without claiming to have made it. She did persuade the cook to use less salt, and considers that contribution worth mentioning.{/n}
"I have learned to distinguish doing a thing from obtaining it competently. This evening rests heavily on the second skill."
{n}You tell her something small from your day. She asks a question about the person involved, then another about what you said. When you reach the part where you were less certain of yourself, she stops eating to listen.{/n}
"Would you like an opinion?"
"You have one."
"Several. I am withholding them until you have finished, which you will recognise as a painful concession."
{n}You choose one detail to explain more carefully. She changes her first opinion, keeps the second, and admits the third was mainly an opportunity to say something clever. By then the covering has gone soft beneath the sauce. Neither of you complains.{/n}
{n}When you reach for the last slice, she lays her hand over yours.{/n}
"A negotiation. Half in exchange for your company while I clear the table."
"I was planning to stay."
"Then I have made an unnecessarily generous offer. Eat it before I reconsider."
{n}Her fingers slide away slowly. You catch them before she can return to her cup.{/n}
"I am glad you came," {n}she says, with no clever qualification waiting behind it.{/n}""", c('[Help her clear the table.]', "plans")),
    n("plans", "Konomi", """{n}The dishes take less time than the conversation about where they ought to go. Konomi has a strong opinion about a shelf you have never noticed. You discover that it is based on having dropped a cup from it last month, and suggest moving the cups.{/n}
"An excellent proposal. I should have invited you sooner."
{n}She puts the last one safely down. When she turns, you are close enough that she does not have to raise her voice.{/n}
"One evening a week, Commander, entered in both our books before the week begins. If the war takes it, the war owes us another, and I shall collect. I have collected from worse debtors than a crusade."
"Which evening?"
{n}She names two possibilities and tells you where her writing will fall. You choose a time you can offer. She asks what you would like to do and waits through your first, overly generous answer.{/n}
"Something you want. I have spent several evenings being extremely specific. It would be discourteous to let you remain mysterious."
{n}You suggest a meal away from her workroom, or a walk that has no destination anyone will wish to inspect. She prefers the walk, then admits she would like to choose the place for supper afterward.{/n}
"There. We have already disagreed and remained interested. A promising beginning."
{n}Her hand settles at the back of your neck. She draws you close enough to brush her lips against yours, then stays there, waiting for you to close the small remaining distance.{/n}""",
      c('[Kiss her and stay for the night.]', "night"),
      c('[Kiss her, then ask for a little air together before you leave.]', "air")),
    n("night", "Narrator", """{n}Konomi meets the kiss with a quick intake of breath. Her hand tightens at your neck. The next kiss is less careful, and she laughs when the edge of the table catches you both by surprise.{/n}
"We have discussed this room's furniture quite enough."
{n}She takes your hand and leads you past it. At the inner door she turns back and starts on your collar herself, briskly, as if she has been wanting to all evening. "I have been sitting across from you all evening pretending to care about mushrooms. Get this off."{/n}
{n}Her sash comes loose under your hands. She lets the silk fall, then catches your wrists and draws your hands back to her warm skin. She pushes you onto the bed by the shoulders and comes down over you, her hair falling around your faces.{/n}
"There," {n}she says against your mouth.{/n} "Now you have my attention."
{n}She kisses you again and pulls you close.{/n}
{n}Afterward, she lies beside you with one hand resting loosely against your chest. When you move, her fingers close for a moment, then relax.{/n}
"I had a better answer about the waiting yard," {n}she murmurs.{/n}
{n}You turn your head toward her.{/n}
"No. Tomorrow. I wished you to know that I was heroically withholding it."
{n}You laugh, and she lifts her head to kiss the laughter from your mouth. When she settles again, she draws your arm around her. Nothing more needs arranging before morning.{/n}""", c('[Stay beside her as the room grows quiet.]', flags=("konomi.ordinary_expanded", "konomi.ordinary_night"))),
    n("air", "Konomi", """{n}She kisses you again before reaching for her coat. Outside, the air is cool enough that you both discover you were more comfortable indoors. Konomi calls this useful information and refuses to turn back immediately.{/n}
{n}You walk to the end of the street. At each pool of lamplight she draws you close, once to say something quietly and once for no reason beyond wanting the contact. The second time she smiles when you notice.{/n}
"We have an evening arranged. I expect you to offer an opinion about the food, even if I choose it."
"You would become suspicious if I stopped."
"You have been listening. An alarming development."
{n}At her door she keeps hold of your hand while she finds the key. She opens it, then turns back to you instead of going inside.{/n}
"I enjoyed tonight. I would like there to be more of it. That is all I meant to say. I had prepared a much longer version."
{n}You kiss her goodbye. She stays in the doorway until you look back, raises her hand, then goes in to put out the lamp.{/n}""", c('[Keep the next evening you have arranged.]', flags=("konomi.ordinary_expanded", "konomi.ordinary_walk"))),
], after=("konomi.readers_answered",), delay=96)


def integrate(payload):
    """Extend new ordinary evenings while keeping completed older promises intact."""
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    for id in {s["Id"] for s in SCENES} | {"konomi.ordinary", "konomi.farewell"}:
        if id not in by_id:
            raise ValueError("Missing Konomi ordinary expansion scene: " + id)
    ordinary = by_id["konomi.ordinary"]
    existing = ordinary.get("RequiresAny", [])
    gates = ["konomi.ordinary_expanded", "inhuman"]
    if existing and existing != gates:
        raise ValueError("Unexpected ordinary Konomi alternative prerequisites")
    # Existing transformed companionship remains possible without the embodied outing.
    ordinary["RequiresAny"] = gates
