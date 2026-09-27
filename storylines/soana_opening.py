"""Development Soana introduction gated by native outcomes and live local contact.

Unity contact behavior and the complete route still require verification.
"""
from story_format import c, n, scene

SCENES = []
RELATIONSHIP = dict(
    Title="At the edge of her forest",
    Description="Soana has allowed me another visit. She expects useful hands and a legible argument. I would like to discover what else she might welcome.",
    Objective="Return to Soana",
    Guidance="Speak to Soana at her cave after resolving the bear quest while she remains alive and willing to talk. Allow time between visits.",
    StartedFlag="soana.started", ClosedFlag="soana.closed", CommittedFlag="soana.committed",
    UnavailableFlags=["soana.dead", "soana.killed_by_camellia", "soana.forest_dead"], FailureFlags=[],
)


def s(id, title, entry, nodes, requires=(), delay=24):
    for page in nodes:
        page["Portrait"] = "SoanaForest" if id == "water_carrier" and page["Id"] in {
            "start", "promised", "work", "hands", "own_work"
        } else "Soana"
    SCENES.append(scene(
        "soana." + id, title, "Soana", 3, entry, nodes,
        Relationship="soana", Chapters=[3], last=3,
        AnswerLists=["2b1776f3e398685479ff6b16290b4cc2"],
        ContactUnit="64805abb52739e44280a758f850b300c",
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", *requires),
        forbids=("soana.dead", "soana.killed_by_camellia", "soana.forest_dead", "soana.closed", "inhuman"),
        delay=delay, optional=True))


s("threshold", "A way out of the basket", '"Is there something here you would accept help with?"', [
    n("start", "Soana", '''{n}Soana looks past you toward the cave mouth. Something scrapes against the stone there, stops, and scrapes again.{/n}
"You could begin by moving out of the light."
{n}When you step aside, you see a fox pressed behind an overturned basket. A loop from the basket's broken carrying strap has caught around one hind leg. Each time the animal pulls away, the basket knocks against a stone and the loop tightens.{/n}
{n}Soana has set a folded cloth beside it. She reaches for the cloth, and the fox bares its teeth.{/n}
"It came for a scrap of hide. Now it intends to take my fingers instead. Hold the basket still. I will cut the strap."
{n}Her own hands are small and dry, the knuckles swollen. She closes them deliberately before reaching for the basket again.{/n}''',
      c('[Kneel beside the basket, leaving the cave mouth clear.]', "look"),
      c('"I cannot stay. I will leave the entrance clear."', abort=True)),
    n("look", "Narrator", '''{n}The fox jerks its trapped leg. Soana stops with the cloth suspended between her hands. The edge of the loop has rubbed a narrow raw line through the fur.{/n}
"Not a spirit," she says. "An ordinary hungry thief. You may spare me an exorcism."
"Can you reach the strap without holding it down?"
"If it stops trying to flee through a space too small for its bones."
{n}You can see a way to move the basket around the stone, opening a wider gap. It would take time to do without frightening the fox further. Soana's knife lies on a flat stone beside her, within reach.{/n}''',
      c('"Move the basket a little at a time. Let it find the larger gap before you reach for the strap."', "wait", flags=("soana.fox_waited",)),
      c('"Cover its eyes. I will hold the basket while you cut. We should end this quickly."', "hold", flags=("soana.fox_held",))),
    n("wait", "Soana", '''"And if it spends the remaining daylight learning nothing?"
"Then we will still have the cloth."
{n}She glances toward the trees outside, measuring the light, then lowers the cloth to her lap. You ease the basket away from the stone. The fox lunges at the movement. Both of you stop.{/n}
"Smaller," she says.
{n}You move it less. This time the animal stays still. A gap opens between wicker and rock. For a while nothing follows except the sound of the fox's breathing.{/n}
{n}Soana begins to reach for the knife. You shake your head. She gives you a look that would sour milk, but leaves it where it is.{/n}
{n}At last the fox turns toward the gap. It lowers its nose, takes one short step, and discovers that the strap no longer draws tight. Soana slips the knife beneath the loose loop and cuts outward, away from the leg.{/n}
{n}The animal scrambles through the opening. Its injured foot touches the ground gingerly, but it can put weight on it. It disappears beneath the bracken.{/n}''',
      c('[Release the basket and sit back on your heels.]', "wait_cost")),
    n("wait_cost", "Soana", '''{n}She retrieves the severed strap and lays it across her knee.{/n}
"There goes my thief. With the hide, unless I am mistaken."
{n}She is not mistaken. The scrap has vanished too.{/n}
"You gave it a long time to choose a short journey."
"It took the journey."
"Yes."
{n}She examines the raw edge of the strap, then looks outside. The strip of sunlight has left the cave floor.{/n}
"And now I will not gather the dry reeds before dusk. I needed them for a carrier."
"I can bring a bundle when I return."
"Dry reeds. Not green stalks pulled out by somebody who thinks enthusiasm makes a basket."
{n}She shows you the clean, pale length she needs. You turn it between your fingers while she corrects your estimate of its thickness.{/n}''',
      c('"Show me where you gather them. I will return tomorrow with what you actually asked for."', "end_wait", flags=("soana.reeds_promised",)),
      c('"I cannot promise tomorrow. Keep the sample until I can offer you a day."', "end_wait")),
    n("hold", "Soana", '''{n}You steady the basket. Soana lowers the cloth over the fox's head and shoulders. Beneath it the animal twists hard enough to knock her hand against the stone.{/n}
"Hold that corner. The basket, not the leg."
{n}You press the wicker down. Her knife severs the strap on the second attempt. She lifts the cloth at once, but the fox has already dragged its leg across the broken edge of the basket. A thin smear of blood marks the wicker.{/n}
{n}It bolts through the cave mouth and disappears under the bracken. Soana stays kneeling. A bead of blood is forming on the back of her hand where the stone scraped it.{/n}
"Done," she says.
{n}You look at the blood on the wicker. She follows your gaze.{/n}
"Yes. I saw. It would not keep still."
"Neither of us expected it to."
{n}She folds the cloth over the stain before answering.{/n}
"No. We did not."''',
      c('"Next time, I want to try making room before we hold anything down."', "hold_room", flags=("soana.fox_reconsidered",)),
      c('"The strap had to come off. I would still choose to cut it quickly, but we should have padded that edge."', "hold_pad", flags=("soana.fox_expedience",))),
    n("hold_room", "Soana", '''"You had a hand on that basket too."
"I know. That is why I am saying what I would do differently."
{n}She opens the cloth again, inspects the stain, and lays it where she will have to see it when she next reaches for the knife.{/n}
"There is your reminder. Do not appoint yourself my conscience merely because yours has found its voice."
"Will you try it?"
"Ask me when there is an animal in front of us. I will not swear how to treat an empty floor."
{n}She gets up slowly, favoring the scraped hand. You hold the basket while she removes the broken strap altogether.{/n}''', c('[Help her put the basket aside.]', "end_held")),
    n("hold_pad", "Soana", '''"Then fetch the scrap under that pot. Fold it twice."
{n}You bring her a piece of worn felt. She binds it over the broken wicker with the remaining strap, then pulls against it until the rough edge no longer shows.{/n}
"This one will not catch another leg. As for the next one, perhaps you will have found a gentler pair of hands by then."
"I can make these hands more careful."
{n}She looks at them before turning away.{/n}
"See that you do."
{n}There is daylight left. She takes a small sickle from beside the cave wall and tells you where she gathers reeds. You carry the repaired basket while she chooses the dry stalks. She leaves the green ones standing.{/n}''', c('[Bring the reeds back with her.]', "end_held")),
    n("end_wait", "Soana", '''{n}Soana picks up the damaged basket. The cut strap hangs loose from its side.{/n}
"I shall remove the other loop before something else discovers it. You may tell your soldiers that you defeated a piece of wicker."
"Would you corroborate my account?"
"Not if they bring trumpets."
{n}The reply comes so quickly that you smile before she can turn away.{/n}
"Come during daylight if you come again. I have a water pot whose carrier needs mending. You can learn whether your patience survives being useful."''',
      c('"I would like to come again."', flags=("soana.threshold_kept",)),
      c('"For the work, then. Do not expect an audience for everything else."', flags=("soana.threshold_kept", "soana.work_first"))),
    n("end_held", "Soana", '''{n}Back beside the cave mouth, Soana sets the basket beyond the narrow animal track. She flexes her scraped hand once, then tucks it into her sleeve.{/n}
"There is a water pot I cannot carry safely until I repair its cradle. Return during daylight if you want another task. This one will not bite."
"An improvement."
"It will spill on your boots if you do it badly. Do not rejoice too soon."
{n}For a moment her mouth draws into a crooked smile. The deep lines beside it remain when the smile is gone.{/n}''',
      c('"I would like to come again."', flags=("soana.threshold_kept",)),
      c('"For the work, then. Do not expect an audience for everything else."', flags=("soana.threshold_kept", "soana.work_first"))),
], delay=0)


s("water_carrier", "The weight of water", '"You said the water pot needed a carrier."', [
    n("start", "Narrator", '''{n}Soana has brought an empty clay pot into the daylight. Its sides are sound; the wicker cradle beneath it has split at one handle. She has arranged an awl, a shallow dish of water and several lengths of reed beside it.{/n}
"The vessel is older than that handle. I am not throwing it away because somebody wove in a hurry."
"Who wove it?"
"Somebody in a hurry. Sit there. Keep your shadow off my hands."''',
      c('[Set down the promised dry reeds and take the place she indicates.]', "promised", requires=("soana.reeds_promised",)),
      c('[Sit beside the pot and examine the broken handle.]', "work", forbids=("soana.reeds_promised",))),
    n("promised", "Soana", '''{n}She sorts through your bundle. Two stalks go aside. The rest she lays within reach.{/n}
"These will do."
"Only those?"
"Those will do well. Must I praise every reed separately?"
{n}She puts the rejected pair across the dish to keep the soaking lengths from rising out of the water. Nothing is thrown away.{/n}''', c('[Hold the cradle while she loosens the broken weave.]', "work")),
    n("work", "Soana", '''{n}She works the awl beneath a stubborn crossing, turns it, and draws the broken strip free. You hold the cradle so its weight does not pull against her hand.{/n}
"Here. Under this one. Over the next. Leave enough length to return."
{n}Your first attempt cuts diagonally across the old pattern. Soana makes you pull it out. On the second attempt the reed bends without splitting.{/n}
"Better. You are not building a cage. The pot must come out when it needs washing."
{n}The dry warmth of her fingers brushes yours as she moves the loose end. She does not hurry to apologize for the contact. Neither does she repeat it without a reason.{/n}''',
      c('[Ask her to guide the next crossing while you hold the reed.]', "hands", flags=("soana.accepted_guidance",)),
      c('"Let me make the next crossing myself. Tell me if I miss it."', "own_work", flags=("soana.tried_weave",))),
    n("hands", "Soana", '''{n}She places two fingers over yours and turns the reed edgewise.{/n}
"Like this. Strength is useful after you have put it in the right place."
{n}You follow the pressure. The reed slides into the weave. She removes her hand and waits while you make the next crossing unaided.{/n}
"Now you have it."
{n}Her praise is quiet and exact. You find yourself wanting to earn another word of it.{/n}''', c('[Finish the row.]', "flowers")),
    n("own_work", "Soana", '''{n}She watches without reaching across you. You stop at the last crossing, uncertain which strip should pass beneath the other.{/n}
"Look where it returns," she says.
{n}You trace it backward with a finger and find the answer. She presses her thumb against the finished row, testing its tension.{/n}
"That will hold."
"You let me hesitate."
"It was a reed. We could afford the delay."''', c('[Finish the handle.]', "flowers")),
    n("flowers", "Soana", '''{n}The new handle is paler than the rest. Soana rubs her thumb across the join, then turns the pot to hide the repair. After a moment she turns it back.{/n}
"There. No reason to pretend it never broke."
{n}A small white flower has caught in the reeds you are using. You lift it clear before it is crushed into the weave.{/n}''',
      c('"Would you like this?" [Offer her the flower.]', "flower", flags=("soana.flower_offered",)),
      c('[Lay the flower beside the water dish and ask how she learned this work.]', "learned")),
    n("flower", "Soana", '''{n}She takes the flower by its stem. Her wrinkled lips tighten, then soften.{/n}
"There were flowers enough to carpet the paths when Orso walked them. Corven made a wreath for me. I wore it when I became his wife."
{n}She looks at you directly.{/n}
"A woman does not arrive empty merely because you have only just met her."
"I was offering one flower. I would like to know the woman receiving it."
"Then do not hurry to decide what she has lost."
{n}She lays the stem across the rim of the water dish. The blossom rests clear of the water.{/n}''',
      c('"I will ask what you want to tell me. I will not make an opening for myself out of what you have not said."', "marriage", flags=("soana.marriage_acknowledged",)),
      c('"Keep it as thanks for the lesson. I meant nothing more."', "thanks", flags=("soana.flower_thanks", "soana.marriage_acknowledged"))),
    n("learned", "Soana", '''"A handle breaks. A vessel must still be carried. That is an excellent teacher."
{n}She looks at the little flower beside the dish.{/n}
"There were gentler lessons. Corven wove a wreath for me from the flowers that followed Orso. I became his wife wearing it. Later I washed our children in the holy spring."
{n}Her eyes return to the repaired handle.{/n}
"You are looking at more years than your questions can conveniently hold."
"Then I can leave room for answers I have not heard."
"See that you do. I have no wish to have my life tidied into a story that pleases you."''',
      c('[Acknowledge what she has chosen to tell you without deciding what became of her marriage.]', "marriage", flags=("soana.marriage_acknowledged",))),
    n("marriage", "Soana", '''{n}She draws the last reed through the handle and trims the end. For a little while you hear only the scrape of her knife and water dripping from the soaking strips.{/n}
"You need not pull every memory out of me in one afternoon," she says. "I have work left. So have you, unless your army has become unusually patient."
{n}She settles the pot into its cradle and holds the handle out to you.{/n}
"Carry it as far as the stream. Empty first. I will walk beside you and watch the join."''', c('[Take the carrier and walk beside her.]', "stream")),
    n("thanks", "Soana", '''"Then I accept your thanks. You need not look as if I have confiscated something."
"I was wondering whether the handle would hold."
"A tactful recovery. Let us discover whether you also did competent work."
{n}She settles the pot into its cradle and gives you the handle. The flower remains beside the dish as you leave for the stream.{/n}''', c('[Carry the empty pot while she watches the join.]', "stream")),
    n("stream", "Narrator", '''{n}The path ends at a shallow run of water between stones. Soana steadies herself against a tree before stepping down. You wait rather than pull her after you.{/n}
{n}She lowers the pot into the water herself. When she gives it back, the repaired handle takes the full weight. The weave creaks once and holds.{/n}
"Slowly uphill," she says. "Unless you want to do the filling twice."
{n}On the return, she stops to catch her breath. There is no coyness in it. Her age is in the effort, in the care with which she places each foot, and in the impatient glance she gives you when you look ready to speak.{/n}''',
      c('"I like being here with you. I am not asking you to become somebody younger to make that easier to say."', "attraction", forbids=("soana.flower_thanks",), flags=("soana.attraction_named",)),
      c('"The work was worth doing. I would help again."', "company", flags=("soana.practical_company",))),
    n("attraction", "Soana", '''"Then say the first part next time. I know how old I am."
{n}She regards you with a searching, unsentimental attention.{/n}
"You like being here with me? With this temper? These hands?"
"Yes. And I have heard what you said about Corven. I am not asking you to answer anything you have not chosen to discuss."
{n}She looks down at the hand resting on the tree. A smile touches one corner of her mouth.{/n}
"You have not heard the worst of the temper."
"I suspected that."
"Good. Suspicion may keep you from becoming tedious."
{n}She lifts her hand from the tree and resumes the walk. She makes no promise about where your interest may lead.{/n}''', c('[Match her pace and carry the water back.]', "finish")),
    n("company", "Soana", '''"You may. I will find something heavy enough to discourage a careless offer."
"This seems a reasonable beginning."
{n}She tests the firmness of the ground with her foot, then leaves the tree.{/n}
"It is. Walk beside me. I want to see whether that handle pulls unevenly when you carry it."''', c('[Match her pace and carry the water back.]', "finish")),
    n("finish", "Soana", '''{n}At the cave you lower the pot onto level stone. Soana runs a finger beneath the repaired join. It is damp from the filling, but has not shifted.{/n}
"Next time, bring the question you have been carrying around my forest. You can scarcely put it down long enough to lift a pot."
"About Orso?"
"Did you think I had failed to notice?"
{n}She sets the knife beside the awl. Both lie beyond the rim of the full vessel.{/n}
"Come to speak, then. We will see whether either of us can hear an answer we dislike."''', c('[Accept another conversation without treating it as an answer to your interest.]', flags=("soana.water_kept",))),
], requires=("soana.threshold_kept",))


s("guardian_question", "What a protector may demand", '"You asked me to bring my question about Orso."', [
    n("start", "Narrator", '''{n}Soana sits beside the repaired water carrier. Its new handle has begun to darken where her fingers grip it. She has left a place on the stone beside her, with enough space between you for the pot.{/n}
"There is water. Take some if you want it. Then ask."
{n}No animal is waiting to be examined, no spirit summoned to settle the argument for you. She has agreed to a conversation, and watches to see what you will do with it.{/n}''',
      c('"Orso still protects this forest. What choice does he have in continuing?"', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead",)),
      c('"Orso is dead. You spoke of finding another guardian. What would you do differently?"', "dead", requires=("soana.bear_dead",))),
    n("bound", "Soana", '''"The deer have no choice about needing grass. The trees cannot take their roots somewhere kinder. You have seen what comes out of the Wound."
"Those are reasons to protect them. I asked about the one you bound."
{n}Her shoulders stiffen beneath the worn cloth.{/n}
"And if I loosen what holds him? Will you stand here through every night that follows? Will your soldiers leave their walls and guard every hollow?"
"I cannot promise that."
"At least you have brought one honest answer."
{n}She takes the cup from the pot, drinks, and replaces it carefully.{/n}
"I knew the good Orso. I knew the paths that bloomed beneath him. You think I needed a stranger to teach me that something terrible happened to my friend?"
"Knowing did not stop you."
"No. It did not."''', c('[Let that admission stand before answering her challenge.]', "position", flags=("soana.orso_bound_discussed",))),
    n("dead", "Soana", '''"I would need a spirit strong enough to endure the work and a creature strong enough to contain it. Such things are not found by wishing them into a clearing."
"You have described a way to repeat it."
{n}She turns toward you, furious.{/n}
"And you have described nothing! You come with the luxury of a question after the thing that guarded us is gone. Must I let the forest die politely so that no visitor will reproach me?"
{n}The carrier shifts when her knee strikes it. She catches the pot before water spills, and holds it until her breathing slows.{/n}
"Orso was my friend," she says. "Before all this. I remember him without needing you to draw the shape of a bear in the dirt."
"Then the next creature cannot simply take his place."
"Nothing will take his place. That does not make the forest cease to need a guardian."''', c('[Answer the need without pretending it settles the means.]', "position", flags=("soana.orso_dead_discussed",))),
    n("position", "Soana", '''"Tell me what you came here to demand."
{n}She waits with both hands resting on the pot, as if keeping something small and whole between them is helping her remain seated.{/n}''',
      c('"A different method. I will help look for one, but I will not praise another binding merely because you call it protection."', "alternative", flags=("soana.seeks_alternative",)),
      c('"I understand choosing a terrible measure when every answer costs lives. I want you to admit who pays for yours, and to look for a way to stop charging them."', "command", flags=("soana.accepts_hardship",)),
      c('"I cannot make this part of a closer relationship. I will leave your water and your work in peace."', "leave", flags=("soana.closed",))),
    n("alternative", "Soana", '''"Look where? You cannot gather an answer in the reeds."
"You know this forest. I can bring accounts of what others have tried, if you will read something that did not originate in your own hands."
"Accounts written by mages, I suppose. Those who dig into darkness and act surprised when it opens beneath their cities."
"Some may be. You can dispute a method. You cannot decide its failure before hearing it because you dislike the person who wrote it."
{n}She gives a harsh little laugh.{/n}
"I certainly can."
"Then you will be choosing not to look."
{n}She takes her hands off the pot. For a moment you think she is about to order you away.{/n}
"Bring one account. One. Something you have read yourself. I will tell you exactly why it is foolish."
"And if it is not?"
"Do not borrow tomorrow's victory. We have not reached tomorrow."''', c('[Agree to bring a proposal for examination, not a promised cure.]', "memory")),
    n("command", "Soana", '''"You sound like someone who has sent others to die."
{n}She rubs a thumb across the water carrier's handle.{/n}
"Do they have the liberty to refuse you? Or is that a kindness you recommend only when another person must endure it?"''',
      c('"They must be able to refuse. I would have to decide what to do without them."', "command_refusal"),
      c('"I give orders. I expect obedience. I also need to know when a method is destroying what it was meant to preserve."', "command_orders"),
      c('"I have made decisions I cannot defend by pointing to yours. We still need a better answer here."', "command_regret")),
    n("command_refusal", "Soana", '''"A costly conviction. I wonder whether those who rely on your protection would agree."
"You asked what I would permit. That is my answer."
{n}She looks down at her swollen knuckles.{/n}
"Then bring me an answer for the forest as well. I cannot guard it with your good opinion."''', c('[Ask whether she will examine a different method.]', "cost")),
    n("command_orders", "Soana", '''"There. I thought there might be someone giving orders beneath all that concern."
"You asked. I answered."
"Yes. And you would like me to believe you know the difference between a necessary cost and a convenient one."
"I want us to examine this one."
{n}She lets the silence stretch before giving a grudging nod.{/n}
"Examine it, then. I shall be interested to see what you call necessary when the proposal is yours."''', c('[Ask whether she will examine a different method.]', "cost")),
    n("command_regret", "Soana", '''"I did not ask you for a confession."
"I am not offering one. I am saying your question applies to me too."
{n}Her thumb stops moving along the handle.{/n}
"Then you know how little comfort there is in finding fault after the choice has been made."
"Enough to look for another choice before we repeat it."
"Perhaps. Show me something worth looking at."''', c('[Ask whether she will examine a different method.]', "cost")),
    n("cost", "Soana", '''"I will examine it. Do not mistake that for agreement before you have brought me anything."
{n}She looks toward the cave mouth.{/n}
"Bring me something other than a verdict next time. A method, a record, an account from someone who endured this land. I will hear it. I do not promise to like its author."
"You can begin by hearing it."
"Yes. I can begin there."''', c('[Agree to look without promising a result you cannot yet deliver.]', "memory")),
    n("memory", "Narrator", '''{n}Soana draws the pot nearer and pours water into the cup. Before passing it to you, she checks that the rim is clean.{/n}''',
      c('[Remember the fox finding its own way out.]', "fox_wait", requires=("soana.fox_waited",)),
      c('[Remember the blood on the wicker and the room you wanted to make next time.]', "fox_change", requires=("soana.fox_reconsidered",)),
      c('[Remember the padded edge and the cost of choosing speed.]', "fox_speed", requires=("soana.fox_expedience",))),
    n("fox_wait", "Soana", '''"Do not say it," she tells you.
"What?"
"That we should move the whole forest a finger's width and wait for the Abyss to notice the gap."
"I was remembering that you waited."
{n}Her answer takes longer this time.{/n}
"I had a knife ready if waiting failed."
"Yes. You still waited."
{n}She makes an impatient noise, but takes the cup back only after you have finished drinking.{/n}''', c('[Settle what the next visit will actually involve.]', "terms")),
    n("fox_change", "Soana", '''"I left that cloth where I would see it," she says. "The one from the fox."
"I remember."
"I moved it this morning. It needed washing. Remorse is a poor reason to keep a dirty cloth."
"Did moving it change what you remembered?"
"No."
{n}She holds out her scraped hand. The little wound has dried.{/n}
"I have this as well. There is no shortage of reminders. What I lack is an answer I can use."''', c('[Settle what the next visit will actually involve.]', "terms")),
    n("fox_speed", "Soana", '''"You helped hold the basket," she says. "I remember that when you speak so carefully about what another creature may be made to bear."
"I remember it too. Padding the edge mattered. It did not make the blood disappear."
"No."
{n}She studies you over the rim of the cup.{/n}
"At least you have not come here wearing an innocence you did not possess when you left. Bring your account. We will see what work it survives."''', c('[Settle what the next visit will actually involve.]', "terms")),
    n("terms", "Soana", '''"You will bring something for us to examine," she says. "I will hear it before I dismiss it. That is the agreement."
"And if it offers no answer?"
"Then it offers no answer. We will have spent an afternoon finding that out."
{n}She sets the empty cup down. Her hands remain free beside it.{/n}''',
      c('"I would still like the afternoon in your company."', "warm", requires=("soana.attraction_named",)),
      c('"For now, that is enough reason to return."', "practical")),
    n("warm", "Soana", '''{n}She looks at your face for a long time. The wary attention does not entirely conceal her pleasure.{/n}
"You have a peculiar idea of a pleasant afternoon."
"You have given me fair warning."
"And I have given you no answer about anything beyond another visit. Remember both."
"I will."
{n}Her smile is brief, crooked and entirely her own.{/n}
"Good. Bring a legible account. I do not intend to spend your affection deciphering somebody else's handwriting."''', c('[Leave with the invitation she actually offered.]', flags=("soana.inquiry_invited", "soana.opening_kept"))),
    n("practical", "Soana", '''"Then we understand each other on at least one small matter."
{n}She rises, lifts the carrier and places it in the shade. The new handle holds without a sound.{/n}
"Bring a legible account. If you arrive with a scroll written to impress other scholars, I will make you read every word aloud until you hear how foolish it sounds."
"That may be a long afternoon."
"You may leave before you finish. I expect you will want to."
{n}She watches you go, and does not call you back to improve the terms.{/n}''', c('[Leave with a specific question to investigate.]', flags=("soana.inquiry_invited", "soana.opening_kept"))),
    n("leave", "Soana", '''{n}She takes her hands off the pot.{/n}
"Then go. You have done useful work here. I will not pretend you did not because you refuse to stay."
"The handle should last."
"I know. I tested it."
{n}She turns the cup upside down on the stone. You leave without taking back the water, the repairs or the time you offered. She makes no promise to change in exchange for your return.{/n}''', c('[End these private visits.]')),
], requires=("soana.water_kept",))
