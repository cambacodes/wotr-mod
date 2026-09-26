"""An authored rival and counterfeit performance, conducted through the existing charm.

Guests remain on Jerribeth's side; she relays their words and the Commander's replies.
No native actor, inventory, victim, allegiance or relationship state is rewritten.
"""
from story_format import c, n, scene

SCENES = []


def s(id, title, nodes, requires=(), delay=24):
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Jerribeth"
    SCENES.append(scene(
        "jerribeth." + id, title, "Jerribeth", 3, "", nodes,
        Relationship="jerribeth", Remote=True, Chapters=[3, 4, 5],
        Areas=["2570015799edf594daf2f076f2f975d8", "7847c3e3537104f4694167af0b9fcd0e"],
        requires=("jerribeth.consequences_kept", "jerribeth.terms", "jerribeth.lovers", *requires),
        forbids=("jerribeth.closed", "jerribeth.unavailable", "jerribeth.farewell"),
        delay=delay, optional=True,
        ForbidOverrides={"jerribeth.farewell": "jerribeth.catchup_requested"}))


s("counterfeit_guest", "A Commander who always agrees", [
    n("start", "Narrator", '''{n}Jerribeth has put a little theater inside the frame. Its curtain rises on a figure in an absurd crown. The face is a guess at yours. The figure bows to an empty chair and holds the bow until it looks painful.{/n}
"May I be useful?" Jerribeth says in a dreadful imitation of a soldier's voice. "May I conquer something small enough to fit beneath your chair?"
{n}She stops moving the puppet. Its smile remains.{/n}
"Somebody has offered me this. He believes I shall be delighted."
{n}Beside the theater lies an open, shallow case. Its lining bears the pressed outline of the model. This is an object on her table, not another room she has made for the charm.{/n}''',
      c('"Who thinks he can sell you that version of me?"', "maker"),
      c('[Postpone the conversation before she begins the demonstration.]', abort=True),
      c('"We kept my name out of the purchaser\'s entertainment. Has she been talking anyway?"', "previous_buyer", requires=("jerribeth.sale_corrected",)),
      c('"We withdrew from the purchaser rather than sell her an association with me. Did she send him?"', "previous_buyer", requires=("jerribeth.sale_withdrawn",))),
    n("previous_buyer", "Jerribeth", '''"I have no evidence that she did. You need not give her credit for every piece of impudence we encounter."
{n}She looks at the little crowned figure.{/n}
"People notice whom I refuse to discuss. They notice how often I am unavailable. Then they congratulate themselves upon discovering a secret, and eventually one of them attempts to make it useful."
"So we accomplished very little."
"We decided what I would sell. I kept that agreement. Neither of us purchased silence from everyone who might invent a story afterward."
{n}She makes the puppet bow again, then pulls it upright by its ridiculous crown.{/n}
"Our new admirer has supplied his own story. I would like to discover how expensive he has made it."''', c('"Tell me who he is."', "maker")),
    n("maker", "Jerribeth", '''"Vardess. A cambion who buys other people's inventions and claims to have discovered their makers. He has wanted a performance from me for some time."
{n}She turns the case so you can see the accompanying card.{/n}
"He has heard that I spend evenings in the Commander's company. He offers a substitute for those evenings when my dangerous acquaintance is unavailable. Such solicitude."
"And what does he want?"
"To exhibit it with my approval. The Commander at my feet. Me at his table, acknowledging that he has supplied something I wanted. Everyone in the room beneath someone else. He will consider the arrangement elegant."
{n}She makes the crowned figure straighten. Its head turns toward her with the same fixed smile.{/n}
"The face is poor. The obedience is worse."''',
      c('"You could send it back with that assessment."', "return"),
      c('"He is inviting you to admit what he thinks you want. What will you show him instead?"', "appetite")),
    n("return", "Jerribeth", '''"And allow him to say I was too offended to look? He would give the performance himself, with a sorrowful explanation of my absence."
{n}She closes one wing against her back. The other catches the edge of the case and pushes it aside.{/n}
"I can refuse. That is the dull answer, and I have considered it. I have also considered returning something that makes him regret inviting an audience."
"He is relying on that."
"Yes. I would find this much easier if he were entirely stupid."
{n}She brings the case back. Beneath its velvet lining, a corner of stiff paper protrudes.{/n}
"His assistant has sent more than the finished toy. Careless, unless the assistant had a reason."''', c('[Ask to see what was packed underneath.]', "lining")),
    n("appetite", "Jerribeth", '''"His own face, perhaps. Begging someone to admire an invention he could not make."
{n}Her amusement buzzes against the last word. Then she stops, considering the puppet.{/n}
"Too obvious. He will have prepared for that. He might even enjoy seeing himself at the center of the evening."
"Then take the center away."
{n}Jerribeth looks up. The motion is quick enough to disturb the image around her antennae.{/n}
"Now you are being helpful."
{n}She lifts the theater out of its case. Beneath the velvet lining, a corner of stiff paper protrudes.{/n}
"His assistant packed the construction sheet with it. I doubt Vardess intended me to have that."''', c('[Ask her to lift the lining.]', "lining")),
    n("lining", "Narrator", '''{n}The sheet shows a miniature stage divided into three compartments. In one stands the crowned puppet. In another, an insectile silhouette. The last contains several rows of watching faces. A narrow line runs from each compartment into a little square beneath the stage.{/n}
"The audience he proposes is invited to his own house," Jerribeth says. "They are people who enjoy pretending their host has a secret that makes attendance valuable. This is the little demonstration he wishes me to approve first. I have invited neither him nor his guests yet."
{n}The silhouette bows when she touches a brass pin beneath it. Its movement is identical to the puppet's.{/n}
"There. He has made me obedient as well. He merely delayed the discovery."''',
      c('"Find out what the square holds before you invite him anywhere."', "square"),
      c('"I want to see his face when that second figure bows to him. He expects you not to notice."', "square", flags=("jerribeth.counter_relishes_trap",))),
    n("square", "Jerribeth", '''"A place for instructions. Or a place for what the instructions preserve. I shall take it apart before I let him see it moving."
{n}She holds the construction sheet near the frame. A second hand has corrected the first draught in darker ink. The corrections are cramped into every available margin.{/n}
"I know that handwriting. Serit. An adult tiefling who makes clever moving scenery and insists on being described as an artist. Vardess calls him his assistant, which is cheaper."
"Is he yours?"
"No. He has worked for me once. He stole a set of sketches afterward. I paid him anyway. He had left the good ones."
{n}She tilts the sheet toward the light.{/n}
"He remembered that I look underneath things. We shall find out whether he has remembered anything else."''',
      c('"Show me the mechanism when you have it open. I will help examine it."', "keep"),
      c('"I will help spoil his performance. Do not mistake that for admiring every use you have made of one."', "judgment", requires=("jerribeth.judges_actions",))),
    n("judgment", "Jerribeth", '''"I had not mistaken you for an admirer of every use I have made of anything. Your conversation has made that difficult."
{n}She leaves the paper turned toward you.{/n}
"You may dislike the work and still recognize a hand reaching for the frame. Tell me where this one is reaching. We can return to disliking each other afterward."
"You invited me."
"And you have become very pleased with the fact. I should never have taught you to notice."''', c('[Return to the construction sheet.]', "keep")),
    n("keep", "Jerribeth", '''{n}Jerribeth removes the crown from the puppet. Its carved head is unfinished underneath. She turns it over, inspecting the peg.{/n}
"Vardess could have asked what I enjoy about your company. It would have saved him the expense of this thing."
"Would you have told him?"
"Certainly not. But I could have enjoyed refusing."
{n}She puts the crown on the empty chair. It fits more convincingly there.{/n}
"Another evening. I will have the stage open. Bring whatever expression you use when you intend to make someone regret underestimating you. I have become rather fond of it."''', c('[Agree to examine the model together.]', flags=("jerribeth.counter_invited",))),
])


s("counterfeit_hinge", "Under the miniature stage", [
    n("start", "Narrator", '''{n}The theater lies on its side. Jerribeth has removed its painted floor and placed the little figures in a row, like guests expelled from a supper. Light runs through narrow channels underneath the boards whenever she moves a brass pin.{/n}
"The obvious trick is quite good," she says. "The figures borrow one another's movements. A bow to me becomes a bow from me. Our host can appear to command both without changing what the first audience sees."
{n}She moves two pins. The crowned figure inclines toward her; the insectile figure inclines toward the empty chair.{/n}
"The square is still sealed. Serit has varnished the catch into the same color as the wood. I can break it. I would prefer to know what I shall break."''',
      c('[Study the seams and reflected light for a concealed catch.]', check=dict(Skill="SkillPerception", DC=25, Success="found", Failure="missed", CommanderOnly=True)),
      c('"Work through the construction sheet with me. We can mark every moving piece before you break the seal."', "patient"),
      c('[Leave the disassembled theater for another evening.]', abort=True),
      c('"Turn it around as you did the unfinished village. Show me what the audience would never see."', "study", requires=("jerribeth.sun_exposed",))),
    n("study", "Narrator", '''{n}Jerribeth turns the whole stage away from the frame, then angles it until you can look into the compartment meant for the audience. From here the painted catch is plainly a reflection laid across the wood. Its varnish continues up the wrong side of a supporting post.{/n}
"The front supplies the explanation," she says. "And the audience helps it along. You remembered."
{n}She reaches around the post and finds the real hinge from behind. The square opens. A thin strip inside bears a row of repeated diagrams. Jerribeth removes it without tearing either end.{/n}
"A recorder. He intended to keep my movements and give them whatever meaning pleased him."
{n}She puts the intact strip beside the stage. When she restores the model's position, the false catch becomes convincing again.{/n}
"There is a use for leaving the back of an illusion visible. I shall try not to become famous for it."''', c('[Keep the strip as evidence.]', "result", flags=("jerribeth.counter_cache_intact", "jerribeth.counter_study_used",))),
    n("found", "Narrator", '''{n}A line of light travels beneath the square when Jerribeth lifts the left figure. It stops at a tiny notch that the inked diagram places on the opposite side. You ask her to tilt the stage. The notch remains dark while everything beside it brightens.{/n}
"A false reflection," she says. "He has painted the catch where someone impatient will pry."
{n}You guide her toward the real hinge. It opens without resistance. Inside is a thin strip marked with repeated little diagrams of the figures' positions. Jerribeth slides it free before touching another pin.{/n}
"It keeps the movements. He can repeat the bow after I leave. He could exhibit my disapproval as often as he liked and have it incline prettily to him every time."
{n}She holds the unbroken strip where you can see both ends.{/n}''', c('"Keep that intact. We have the thing he expected to own."', "result", flags=("jerribeth.counter_cache_intact",))),
    n("missed", "Narrator", '''{n}You follow the brightest line to a corner that seems to shift beneath the varnish. Jerribeth presses there. The square opens with a dry crack, and a strip of inscribed material tears against a hooked pin.{/n}
{n}For an instant the insectile figure repeats its bow without her touching it. Then it drops on its face.{/n}
"That was the wrong catch."
{n}She picks up the torn strip. The repeated markings are visible, but several have split across their centers.{/n}
"It preserved the movements. Now we have a damaged example and my word about what it would have done. Vardess will be delighted to call it an accident caused by my temper."
{n}She tries to fit the edges together, fails, and puts them down separately.{/n}''', c('"Then we will need testimony or another way to make him reveal it."', "result", flags=("jerribeth.counter_cache_broken",))),
    n("patient", "Jerribeth", '''"Every piece? There are forty-seven."
"Then begin with the one touching the square."
{n}She begins. You follow the drawing while she moves each accessible pin. By the time you reach the third compartment, you have found two connections omitted from the neat original and added in Serit's cramped hand.{/n}
{n}One returns the figures to a starting position. The other runs under the sealed square. Jerribeth wedges both before lifting the lid.{/n}
"I have jammed the catch. We will have to cut through it."
{n}She scores around the square, ruining the little stage to lift its underside whole. An inscribed strip remains inside the extracted piece.{/n}
"There is your patient answer. We keep the strip. We lose the theater. Now he cannot blame an embarrassing performance on our having tampered with his toy. We shall need to build something else."''', c('[Keep the extracted strip and the ruined stage separate.]', "result", flags=("jerribeth.counter_cache_intact", "jerribeth.counter_stage_cut",))),
    n("result", "Jerribeth", '''"He wanted me to supply the first movement myself. A little genuine irritation. A refusal. Then his machine would turn it into the exact answer he had paid to hear."
{n}She lifts the insectile figure between two fingers.{/n}
"He believes he has found a weakness. Apparently I have become someone who objects to being made ridiculous in front of a particular person."
"You objected to being made ridiculous before."
"Yes, but I could dispose of the audience afterward. You are difficult to replace."
{n}Her antennae move as she watches you consider the remark. She does not soften it.{/n}
"Serit wants an answer. There is a place and time written underneath the construction sheet. He can come to my table. You may watch through this frame while I ask him what he has sold twice."''',
      c('"Make him show us what he knows before you offer him anything."', "clerk", flags=("jerribeth.counter_wants_evidence",)),
      c('"He put the warning where you would find it. Find out what he wants to escape."', "clerk", flags=("jerribeth.counter_hears_clerk",))),
    n("clerk", "Jerribeth", '''"He wants to escape being paid as an assistant. I suspect he also wants to escape discovering what happens when his employer learns that he has sold the instructions. We need not invent a nobler predicament for him."
{n}She puts the crowned figure on its back beside the others.{/n}
"I shall invite him. He will see this charm. You will see whatever I keep within its image. If you have a question, tell me, and I will ask it. I am not extending the connection into his head."
"Can he hear me?"
"Only what I choose to repeat aloud. It will be an excellent opportunity to discover whether you trust my delivery."
{n}She gives the puppet a voice again, solemn and disastrous.{/n}
"I trust you implicitly, magnificent Jerribeth."
{n}The puppet falls off the table.{/n}''', c('"Keep your own voice. I know when that one is lying."', flags=("jerribeth.counter_mechanism_known",))),
], requires=("jerribeth.counter_invited",))


s("counterfeit_clerk", "The artist who signed underneath", [
    n("start", "Narrator", '''{n}Serit sits at Jerribeth's table on the far side of the charm. His horns have been filed short enough to fit beneath a fashionable cap. He keeps removing the cap, looking for somewhere to put it, and replacing it. He is old enough to have gone gray at the temples and vain enough to have dyed those patches badly.{/n}
{n}Jerribeth has told him who is watching. Now she turns toward the frame and repeats his opening request.{/n}
"He would like me to remember that a warning is worth more before the disaster."
{n}Serit says something you cannot hear. Jerribeth listens, then adds:{/n}
"And he would like me not to put it quite that way. A demanding guest."''',
      c('"Ask why he built the thing if he wanted to warn you."', "built"),
      c('"Ask him what Vardess promised for it."', "payment")),
    n("built", "Jerribeth", '''{n}Jerribeth repeats the question. Serit's eyes go toward the pieces laid out beside her. He answers without looking at the charm.{/n}
"He says he built a recorder for stage movements. Vardess supplied the figures and the intended scene afterward. A conveniently narrow occupation."
{n}She asks another question of her own. This time Serit looks at her.{/n}
"Yes, he still made the alteration after he saw the figures. He does not claim to have been horrified. He claims to have expected payment."
{n}Serit takes off his cap and finally puts it on the table.{/n}
"Then Vardess asked for the same arrangement in a larger room. The miniature was the demonstration. He wanted a mechanism he could use on visiting performers without telling them what it kept."''', c('"Ask where that larger mechanism is now."', "larger")),
    n("payment", "Jerribeth", '''{n}She puts the question to Serit. He answers at length. Jerribeth makes a small circling motion with one hand until he reaches the part she wants.{/n}
"A studio in Vardess's house. His name on the work. An advance, followed by a much larger sum when the full room was finished."
{n}Serit spreads his hands. The fingertips are stained with the same dark ink as the corrected drawing.{/n}
"The advance arrived. The room grew. His name became inconvenient to mention. Vardess now describes him as a clever servant who has been allowed to pursue a hobby."
"And the larger payment?"
{n}She repeats the question. Serit laughs once, without pleasure.{/n}
"I believe we can infer the answer. He built the concealed mechanism willingly. He has become less willing to remain in the house that contains it."''', c('"Ask where that larger mechanism is now."', "larger")),
    n("larger", "Jerribeth", '''"Unfinished. The moving figures were ready; the room's recorder never worked reliably. He brought the only finished miniature here. Vardess has his drawings, including a catalogue of the scenes he means to reproduce."
{n}She watches Serit while she speaks to you. Then she asks him something else. His hand stops halfway toward his cap.{/n}
"He wants us to believe the unfinished part is essential. It may be. He also wants someone to get him out of the arrangement before his patron tests it again."
{n}Serit draws a folded scrap from his sleeve and lays it on the table. Jerribeth smooths it so you can see a page number and three small diagrams of a horned figure entering, stopping, and turning toward its audience.{/n}
"Vardess's own entrance. Rehearsed three times. He made Serit keep each version because the first two did not make his guests look sufficiently impressed. There is a strip containing all three."''',
      c('"We have an intact example of the mechanism. Ask for his testimony about that page."', "witness", requires=("jerribeth.counter_cache_intact",)),
      c('"Our damaged strip will not prove enough. Ask whether he can bring his employer\'s rehearsal."', "rehearsal", requires=("jerribeth.counter_cache_broken",)),
      c('"Ask for the drawings. We can deny Vardess a finished room without exhibiting Serit."', "drawings")),
    n("witness", "Narrator", '''{n}Jerribeth makes the offer. Serit looks at the intact strip, then toward the frame. He speaks slowly enough that she does not interrupt him.{/n}
"He will explain the mechanism in front of Vardess. He wants the copy of his employment agreement afterward. The one Vardess keeps threatening to show other patrons."
"What is in it?"
{n}She asks. Serit takes a long breath.{/n}
"An advance he cannot repay. A promise to deliver more work than he has finished. His own signature beneath a claim that all the ideas were Vardess's. He accepted the humiliation because he expected to be rich."
{n}Jerribeth taps the little horned profile on the scrap.{/n}
"We could make that signature expensive for its owner instead. I would enjoy watching him price it."''', c('"Offer to recover the agreement in exchange for his testimony."', "bargain", flags=("jerribeth.counter_clerk_witness",))),
    n("rehearsal", "Narrator", '''{n}Serit winces when Jerribeth points to the broken strip. He examines the tear, then says something sharp enough to make her antennae lift.{/n}
"He says the false catch was meant for Vardess. How disappointing that we opened his employer's present first."
{n}She lets Serit finish the rest.{/n}
"He can bring the rehearsal. He has kept it in the lining of his cap. He wants his employment agreement before he gives it to me."
{n}Jerribeth looks at the cap, which Serit promptly moves closer to himself.{/n}
"No. He can keep it until Vardess arrives, and surrender it when we have the agreement. I will not pay for evidence he can still take back."
{n}Serit considers the arrangement, then nods once.{/n}''', c('[Accept the exchange of the rehearsal for his agreement.]', "bargain", flags=("jerribeth.counter_clerk_rehearsal",))),
    n("drawings", "Narrator", '''{n}Jerribeth repeats your proposal. Serit answers too quickly. She stops him with one raised hand and asks again.{/n}
"He can bring the final adjustments. The earlier drawings will remain in the house. Someone sufficiently capable could finish the room from them, given time."
"Then we have not stopped it."
"We have stopped him from completing it tomorrow. That may be all he can sell."
{n}She listens to his next request.{/n}
"His agreement in return. He will hand me the working adjustments and depart before Vardess arrives. He does not wish to be our witness."
{n}Serit waits with his hands flat on the table. Jerribeth looks at the frame.{/n}
"We shall have to make Vardess surrender something without Serit standing here to explain why he should."''', c('"Take the adjustments. Let Serit leave before we deal with Vardess."', "bargain", flags=("jerribeth.counter_clerk_hidden",))),
    n("bargain", "Jerribeth", '''{n}Jerribeth gives the answer aloud. Serit asks one final question. She goes very still before repeating it.{/n}
"He wants to know whether I intend to keep the agreement myself afterward."
{n}The little theater lies between them. Jerribeth moves a figure out of the way, making space for his cap.{/n}
"I might. It would make him less likely to steal from me next time."
{n}Serit says nothing. He has heard that answer without requiring a translation.{/n}''',
      c('"We offered to recover it for him. Give it to him when the work is done."', "release", flags=("jerribeth.counter_return_agreement",)),
      c('"Keep it as security until he has shown us every adjustment. Then destroy it."', "security", flags=("jerribeth.counter_hold_agreement",))),
    n("release", "Jerribeth", '''"Generous with my next inconvenience."
{n}She turns to Serit and speaks. He listens closely, then retrieves his cap and rises. Before leaving the image, he points to a mark beneath the stage. Jerribeth looks where he indicates.{/n}
"He signed it underneath. Every piece he has made. He wants the correct name spoken if we show anyone the mechanism."
"Will you?"
"I already knew where to look. I was waiting for him to ask."
{n}She moves the theater so you can see the small, crowded signature.{/n}''', c('[Remember whose work it is.]', "end")),
    n("security", "Jerribeth", '''"A postponement. He will dislike that less than I expected to enjoy it."
{n}She gives Serit the answer. He argues over the meaning of every adjustment until she turns the construction sheet toward him and makes him circle each section he still has to explain.{/n}
{n}Finally he signs beneath the circles. He leaves his cap on the table while he writes, as though he has forgotten why he was holding it.{/n}
"He has made the work countable," Jerribeth says. "Annoying. Sensible. I shall remember that when I am tempted to ask for one more demonstration."
{n}Serit takes the cap and leaves the image.{/n}''', c('[Keep the circled sheet visible beside the model.]', "end")),
    n("end", "Jerribeth", '''{n}Jerribeth waits until her guest has gone before addressing you again. The miniature chair still wears the absurd crown.{/n}
"Serit will deliver the working adjustments before our next meeting. He has agreed to that much. If he is staying to face Vardess, he can keep the rehearsal until we have the agreement."
"Vardess will come if I offer to consider his demonstration privately. He would prefer witnesses. I shall tell him I want to be convinced before I risk appearing foolish. He will find that believable."
"And if he refuses?"
"Then we have spoiled his miniature and delayed the room. I can bear that disappointment."
{n}She looks down at the crowned chair and gives it a small push.{/n}
"But I think he will come. He has spent a great deal to discover whether I can be made to kneel. People become foolish when they have already paid for an answer."''', c('[Agree to attend through the frame if he accepts.]', flags=("jerribeth.counter_clerk_dealt",))),
], requires=("jerribeth.counter_mechanism_known",))


s("counterfeit_audience", "The host in the empty chair", [
    n("start", "Narrator", '''{n}Vardess has accepted. When you open the connection, Jerribeth tells you he is waiting outside her room. Serit's working adjustments lie beside the model, delivered as promised. She admits Vardess while you watch. He arrives wearing a collar so high that he must turn his shoulders to look around the table.{/n}
{n}She points to the frame and explains who is watching. His smile stops, then returns slightly wider. Jerribeth waits through his greeting before relaying it.{/n}
"He says this is an unexpected honor. I have told him I prefer to show you things before purchasing them."
{n}Vardess removes a flat leather portfolio from inside his coat. Jerribeth indicates a place for it beside the model.{/n}
"He has brought the catalogue and Serit's agreement. Apparently he thought I might wish to buy the artist with the performance."
{n}She leaves her hands off both.{/n}''', c('"Ask him to show us his favorite entrance."', "entrance")),
    n("entrance", "Jerribeth", '''{n}She asks. Vardess touches his collar and gives an answer that takes much longer than the question. Jerribeth translates the useful part.{/n}
"He prefers to surprise his guests. A tall door opening into darkness. A voice that reaches them before they see him. Then the light comes from behind, so everyone must turn."
{n}Vardess makes a turning gesture. It is familiar. You have seen it in the three small diagrams on Serit's scrap.{/n}
"He says an audience wants to be commanded. They come to discover whose command they will enjoy."
{n}Jerribeth lets him finish. Then she looks toward you.{/n}
"He wishes to know whether a person accustomed to command agrees."''',
      c('"Tell him an audience can also enjoy discovering that the person giving orders has forgotten his lines."', "challenge"),
      c('"Tell him I am waiting to see whether he has earned this audience."', "challenge")),
    n("challenge", "Narrator", '''{n}Jerribeth repeats your answer with evident pleasure. Vardess's gaze moves from her to the miniature. He notices that its underside has been opened.{/n}
{n}He speaks sharply. Jerribeth replies before translating.{/n}
"He says I have damaged a valuable invention. I have asked him which part contained his own contribution."
{n}Vardess puts one hand on the portfolio. Jerribeth puts one finger on the table beside it. He leaves it where it is.{/n}
"Now," she tells you. "We can make him acknowledge the recorder in front of its maker, if Serit is staying. Or we can give him a reason to bargain while the room is still private."''',
      c('"Bring Serit in. Let him explain the intact strip."', "testimony", requires=("jerribeth.counter_clerk_witness",)),
      c('"Bring Serit in with the rehearsal. Offer Vardess a chance to hear himself."', "replay", requires=("jerribeth.counter_clerk_rehearsal",)),
      c('"Show him the working adjustments Serit left. Ask how soon his room will be finished without them."', "missing", requires=("jerribeth.counter_clerk_hidden",))),
    n("testimony", "Narrator", '''{n}Serit steps into view from outside the frame. Vardess rises halfway out of his chair. Jerribeth points him back toward it without looking away from Serit.{/n}
{n}The artist lifts the intact strip and shows how its marks correspond to the three figures. Jerribeth repeats enough of his explanation for you to follow. When Vardess interrupts, Serit turns the strip over and shows his signature.{/n}
"He says the movement you make can become whatever bow the owner chooses to display," Jerribeth relays. "And he says the owner specifically requested that I should not be told."
{n}Vardess answers. Serit takes off his cap and removes a second strip from the lining.{/n}
"Our host considers his employee unreliable. His employee offers three rehearsals of the host's entrance for comparison."
{n}For the first time, Vardess looks at the door.{/n}''', c('"Now he understands what can leave this room."', "leverage", flags=("jerribeth.counter_proof_shown",))),
    n("replay", "Narrator", '''{n}Serit enters with his cap in both hands. He keeps the strip beneath it until Jerribeth asks Vardess to open the portfolio. The agreement lies on top. Serit nods, then takes out the rehearsal.{/n}
{n}Jerribeth fits it into a plain demonstration frame. A little horned figure walks through a door, stops, and turns back. On the second attempt it raises its arms too soon. On the third, the door catches its collar.{/n}
{n}Vardess lunges toward the model. Jerribeth lifts it out of reach. No one laughs until she does.{/n}
"He is explaining that this was a rehearsal. Serit has pointed out that my refusal was also meant to become a performance without my approval."
{n}The little figure tries the door again. Vardess sits down.{/n}''', c('"Stop the repetition. Let him decide what the next performance costs."', "leverage", flags=("jerribeth.counter_rehearsal_shown",))),
    n("missing", "Narrator", '''{n}Jerribeth lays Serit's working adjustments beside the portfolio. Vardess begins to answer, then sees the last sheet. He reaches for it. She draws it back.{/n}
"He recognizes the part his own copy lacks. He is offering to pay Serit's remaining fee. How unfortunate that he did not remember it earlier."
{n}Vardess points toward the open model. Jerribeth answers him with a sharp buzz before turning to you.{/n}
"He says he can find another artist. I believe him. I have asked how many entertainments he has promised before that artist will be ready."
{n}She waits through the reply.{/n}
"Three. He began with none and became more truthful as he considered what I might already know. We have an inconvenience to sell him, and he is in a hurry."''', c('"Then make the delay more expensive than surrendering the agreement."', "leverage", flags=("jerribeth.counter_delay_shown",))),
    n("leverage", "Jerribeth", '''"He will surrender the agreement. He wants the rehearsal, if we have it, and the working adjustments. He wants us to say nothing about the mechanism."
{n}Vardess adds something. Jerribeth's delicate hands close together.{/n}
"He will also give me the catalogue. In exchange for one private performance, at a time he chooses. He has not finished trying to purchase the same thing."
{n}She looks at the portfolio, then at you.{/n}
"The catalogue contains rooms and entertainments other patrons have ordered from him. Names. Vanities. Designs he would dislike having compared. I could use it."
"And the performance?"
"No. But I would like him to leave something more interesting than an apology."''',
      c('"Take the agreement and require a signed account of the concealed mechanism. Leave him the catalogue."', "expose", flags=("jerribeth.counter_public_account",)),
      c('"Trade silence about tonight for the agreement and catalogue. No future performance owed."', "archive", flags=("jerribeth.counter_private_archive",))),
    n("expose", "Narrator", '''{n}Jerribeth gives your demand. Vardess begins a furious reply, then remembers the frame. He arranges his face into something more suitable for witnesses.{/n}
{n}She lets him watch her begin writing an account of what the miniature preserves. Serit's name goes beneath the invention. Vardess's goes beside the instruction to conceal its purpose.{/n}
"He will sign if we return the rehearsal and the working adjustments afterward. He wants no account of his entrance included."
{n}Jerribeth writes that limitation. Vardess reads every line twice. At last he signs. She lifts the sheet toward the charm long enough for you to read the whole of it.{/n}
"Now anyone who sees this can ask him why his entertainments need a hidden recorder. I am keeping a copy. He will have to wonder who has read it."
{n}Vardess pushes Serit's agreement across the table. The catalogue goes back beneath his arm.{/n}''', c('[Have her complete the exchange as agreed.]', "departure")),
    n("archive", "Narrator", '''{n}The bargaining becomes brisk. Vardess wants names removed from the catalogue. Jerribeth turns a page toward the frame and asks you whether a catalogue with blank spaces is worth keeping.{/n}
"No," you tell her.
{n}She gives him the answer. He wants the miniature. She offers the useless figures. He wants an undertaking never to approach his patrons. She laughs in his face.{/n}
{n}Finally he puts down both the agreement and the catalogue. In return, Jerribeth gives back the working adjustments and any rehearsal Serit supplied. She agrees to keep tonight's demonstration private. She promises no service and makes no promise about finding better clients.{/n}
"He will be able to finish the room," she tells you. "We have bought something else."
{n}Vardess waits for her to close the catalogue before he removes his hand from it.{/n}''', c('[Accept the trade, including the room he can still finish.]', "departure")),
    n("departure", "Jerribeth", '''{n}Vardess says his farewell without looking toward the charm. Jerribeth listens until his footsteps have passed beyond whatever room lies outside her image. Then she lifts the miniature chair and removes its crown.{/n}
"He has a great many acquaintances. Some of them will be pleased by this. Others will think I have become troublesome. I expect to hear from both."
{n}The chair cracks between her fingers. She looks at it, then lets the pieces fall.{/n}
"A cheap joint."
"You were angry."
"I still am. It has improved the evening considerably."
{n}She moves the broken pieces out of the light. Serit's agreement remains on the table.{/n}
"Come back when I have dealt with what we brought home. I have no intention of spending the rest of this evening letting him occupy the conversation."''', c('[Leave her the agreed work and return another evening.]', flags=("jerribeth.counter_audience_done",))),
], requires=("jerribeth.counter_clerk_dealt",), delay=48)


s("counterfeit_spoil", "What she keeps in the drawer", [
    n("start", "Narrator", '''{n}Jerribeth has cleared the theater from her table. A narrow drawer stands open beneath it. She closes the drawer as you establish the connection, then opens it again with visible irritation at herself.{/n}
"Before you ask. Serit's agreement. I have kept it here until we finish what we said we would do."
{n}She takes out the folded document and lays it within the image.{/n}
"He has returned. He has also asked whether I have any work. Apparently I am an improvement on his previous employer. I shall try not to be offended by the comparison."''',
      c('"You agreed to give him the document. Let him take it before discussing another job."', "return", requires=("jerribeth.counter_return_agreement",)),
      c('"Has he explained every adjustment he circled?"', "circles", requires=("jerribeth.counter_hold_agreement",))),
    n("return", "Narrator", '''{n}Jerribeth calls Serit into view. He stops just short of the table. She pushes the agreement toward him; he opens it, checks the signature, and folds it again with shaking fingers.{/n}
{n}He begins a grateful speech. She interrupts. It is impossible to mistake the impatience in her face, even without hearing her words.{/n}
"I have told him to inspect the rest before thanking me. People become tiresome when they discover another clause halfway through their gratitude."
{n}Serit examines the page. Then he tears it through his own signature. He does not ask to use her fire.{/n}
"He has no intention of selling that debt to anyone else," she says. "A pity. I could have taught him how."''', c('[Let him leave with the torn agreement.]', "work")),
    n("circles", "Narrator", '''{n}She holds up the construction sheet. Every circle has a corresponding diagram beneath it. Two have been redrawn in different ink.{/n}
"He attempted to omit the resetting pin. I made him begin again. He has now finished."
{n}She calls Serit into view and points to the last drawing. He demonstrates with a loose brass pin. Jerribeth watches, asks one question, and receives an answer short enough to satisfy her.{/n}
{n}Then she holds his agreement over the lamp on her side. The lower edge blackens. Serit watches until the flame reaches his signature.{/n}
"I could have made another copy," she tells you when he turns away. "I did not."
"Does he know that?"
"He asked. I answered. He will have to decide whether to believe me. That seems to trouble him more than the debt did."''', c('[Wait until the last fragment has burned.]', "work")),
    n("work", "Jerribeth", '''{n}Serit leaves her image. Jerribeth brushes a scrap of paper from the table with one careful finger.{/n}
"I offered him work. A moving backdrop, with his name where the audience can read it. Payment for each finished section. He demanded an advance."
"Did you agree?"
"A small one. He would not begin otherwise. He has become tiresomely aware of the value of refusing."
{n}She opens the drawer and closes it on nothing.{/n}
"Vardess has also found a way to make his displeasure known. We should discuss that before you imagine the evening ended when he left the frame."''',
      c('[Ask what followed the signed account.]', "account", requires=("jerribeth.counter_public_account",)),
      c('[Ask what followed the private bargain.]', "catalogue", requires=("jerribeth.counter_private_archive",))),
    n("account", "Jerribeth", '''"Two people declined invitations I sent. One was polite enough to say why. Vardess has described me as an artist who brings an inquisitor to a private demonstration."
"Have you shown the account?"
"To that one. She asked whether I would guarantee that no recording mechanism would be concealed in my own work. I have agreed to let her examine the construction. She has agreed to pay someone who knows how."
{n}Jerribeth's antennae press back.{/n}
"I dislike it. It will also make it difficult for Vardess to sell her the same room without answering the same question."
"And the other refusal?"
"Unanswered. I could send the account anyway, but then I would be spending another evening pleading for someone to be interested in me. I have other uses for it."
{n}She looks straight at the frame.{/n}
"This is one."''', c('[Ask what she would have kept if you had not asked for the account.]', "price")),
    n("catalogue", "Jerribeth", '''"One of his patrons has answered my inquiry. She wants an impossible staircase in which the person ascending can watch the person following arrive first. She has spent a fortune on guests who will mistake it for a compliment."
"Will you take it?"
"Probably. The catalogue showed me how much Vardess charged her for a less interesting version. I shall be extravagantly reasonable by comparison."
{n}She turns a page. Several names have been underlined.{/n}
"He has told people I steal clients. He also intends to finish the recording room. Serit says another artist has asked about the mechanism. We returned enough for someone competent to continue."
{n}Jerribeth leaves that page open.{/n}
"There is the bargain. I have useful names. He still has an unpleasant invention. We can dislike the second part, but we cannot pretend we purchased its destruction."''', c('[Ask what else she wanted to keep.]', "price")),
    n("price", "Jerribeth", '''"The rehearsal. All three attempts. Imagine needing three entrances before you can bear to let the evening begin. I would have liked to keep those."
"You returned it if Serit brought it."
"Yes. An irritating condition of our arrangement. Fortunately he gave us a little of his manner in person."
{n}She moves one hand as though adjusting an invisible collar. For a moment her own face becomes Vardess's, pinched with theatrical dignity. Then she abandons the imitation before it can become another performance.{/n}
"I would also have liked Serit to remain afraid enough to work cheaply. He was nearly there. You saw him."
{n}Her voice remains light. She watches which admission you choose to answer.{/n}''',
      c('"I saw. I am glad the bargain ended before you could make another toy of him."', "object"),
      c('"You would have had a frightened artisan. Now you have one who might surprise you. I thought you were bored with obedience."', "interest"),
      c('"You were good at frightening Vardess. I enjoyed watching. I still wanted Serit paid what we promised."', "complicit")),
    n("object", "Jerribeth", '''"The bargain ended where we put its end. You need not place a wreath upon the spot."
{n}She turns the lamp down. The drawer's brass handle vanishes into shadow.{/n}
"You looked at me differently when I considered keeping the agreement. I noticed. I considered keeping it anyway."
"I noticed that too."
{n}A brief chitter breaks the silence.{/n}
"Good. I should dislike becoming easy to admire through inattention."
{n}She restores the light, stopping before it reaches the drawer.{/n}''', c('"Then spend the rest of tonight on something we both want."', "end")),
    n("interest", "Jerribeth", '''"A dangerous argument. You are asking me to consider whether someone might be more entertaining when I leave them loose."
"Serit has already surprised you once."
"By stealing."
"By warning you where to look."
{n}Her hands separate. She considers the emptied space between them.{/n}
"He will steal again if he thinks he can profit. I shall watch the good sketches."
"And pay for the work you want."
"Do not ruin an agreeable thought by furnishing it with instructions. I have already offered the advance."
{n}She sounds annoyed that you have made the answer so easy to give.{/n}''', c('[Ask what she wants to show you now.]', "end")),
    n("complicit", "Jerribeth", '''{n}The antennae lift. She studies you for a moment before answering.{/n}
"I liked having you there when he sat down again. He had meant me to be the one discovering that every movement served somebody else. Then he had to wait while I repeated your words."
"You made him wait longer than necessary."
"Much longer. I enjoyed how politely you neglected to rescue him."
{n}She draws one finger along the edge of the frame on her side.{/n}
"I shall remember that expression. The one you brought for the occasion. You need not have become kind to everyone for me to be pleased you returned."''', c('"I returned for you. Show me what you saved for tonight."', "end")),
    n("end", "Jerribeth", '''{n}She places a little crowned figure on the table. This one has no face at all.{/n}
"The original was a bad likeness. I have made an improvement."
"By removing the face?"
"By admitting I do not know what you will say."
{n}She waits, then gives the figure a voice.{/n}
"You have spent too long being clever, Jerribeth. Invite me back when you have remembered how to be pleasant."
"That is still a bad likeness."
{n}She makes it bow out of sight.{/n}
"Then supply a better answer next time. I will clear the table. You can arrive without preparing to investigate it."''', c('[Accept the private invitation.]', flags=("jerribeth.counter_spoils_settled",))),
], requires=("jerribeth.counter_audience_done",))


s("counterfeit_after", "The voice she cannot rehearse", [
    n("start", "Narrator", '''{n}The table is gone from the image when you return. Jerribeth has made a window overlooking a city that could not stand. Its upper streets turn through one another; a tower bends until its highest balcony hangs beneath its own door. Small lights move along the impossible paths.{/n}
"No catalogue," she says. "I began this before Vardess learned to order a collar. I keep changing the streets. There is no need to decide where you want to go."
{n}Her own narrow silhouette stands beside the invented window. A passing light catches one wing and travels along its edge.{/n}
"You supplied a voice to my room. I have been thinking about how little opportunity I gave it to say anything that was not useful."''',
      c('"Then listen. I have been looking forward to seeing you."', "wanted"),
      c('"I enjoyed being useful with you. I also wanted the evening after."', "wanted"),
      c('[Keep this private invitation for another time.]', abort=True)),
    n("wanted", "Jerribeth", '''"Here it is. Try not to spend it explaining why you deserve one."
{n}She leaves the window in place and moves nearer the frame. There is no chair on your side that belongs to this room, and no hand comes through to offer you one. The image is close enough for you to see the moment she decides against a prepared smile.{/n}
"I wanted you to hear me say his name after he left. I had saved an excellent insult. Then you noticed the broken chair, and I forgot it."
"Have you remembered?"
"Yes. It is less good now."
{n}She lets you wait for it.{/n}
"A purse that has learned to resent the hand opening it."
"You were right. It improved while you withheld it."
{n}Her laugh is high and abrasive enough to make the painted lights flicker.{/n}''',
      c('"Stay as you are. I want to look at the face making that sound."', "own", flags=("jerribeth.counter_evening_own",)),
      c('"Choose a face for this impossible city. I would like to watch you make it."', "guise", flags=("jerribeth.counter_evening_guise",))),
    n("own", "Jerribeth", '''{n}She moves the nearest light until it catches the fine movements around her mouth. The antennae tilt forward. Her hands, which have been busy with the scenery, become still.{/n}
"You look carefully. I used to assume you were searching for the point at which something would become repellent."
"What do you assume now?"
"That you will tell me what you have found. You have been difficult to discourage."
{n}She turns slightly, showing you the edge of the other wing.{/n}
"There. The light is better. If you are going to continue looking, I intend to enjoy being seen."
{n}Behind her, a street rotates out of place. She does not turn to correct it.{/n}''', c('[Tell her which movement keeps drawing your attention.]', "attention")),
    n("guise", "Jerribeth", '''{n}The change begins at her hands. Ordinary knuckles emerge from the slender outline; then an adult elven face forms around her expression. She gives it a small scar at the corner of its mouth, frowns at the result, and moves the scar to the eyebrow.{/n}
"That one made every smile look calculated."
"It was."
"Yes, but I disliked how little work the audience had to do."
{n}She turns the face toward the impossible window. The pointed ears catch a pale light that was not there a moment before.{/n}
"I might keep her. She looks as though she has left an expensive party without saying goodbye."
"Whose party?"
"Anyone's. That is the attraction."
{n}The deliberate shimmer remains at the outline of the guise.{/n}''', c('[Tell her which expression belongs to her beneath the invented face.]', "attention"), portrait="Jerribeth-Guise"),
    n("attention", "Jerribeth", '''{n}You describe the pause before she decides to answer a provocation. She tries it deliberately, discovers that you recognize the attempt, and abandons it with an irritated little sound.{/n}
"You have made that difficult to do naturally."
"Wait until I annoy you again."
"I doubt I shall wait long."
{n}She draws the image closer to the frame. Her next words come without the amusement she usually puts in front of a request.{/n}
"Tell me what you would do if that window opened into your room."
{n}She waits. The impossible city continues moving behind her, with no movement at all across the border between you.{/n}''',
      c('"I would ask you to come closer. I want an evening where we can leave the conversation unfinished."', "desire", flags=("jerribeth.counter_desire_chosen",)),
      c('"I would show you where I keep this frame when I expect you to answer. Then I would ask you to stay and talk."', "quiet", flags=("jerribeth.counter_quiet_chosen",))),
    n("desire", "Jerribeth", '''"You would have to stop saying interesting things. I have found that inconvenient about you."
"I could try."
"Do not. I would notice the effort."
{n}Her hand moves to the edge of her own image, then rests there. She looks toward the place on your side where it would have arrived.{/n}
"I would come closer. I would like to discover whether you still look so pleased with yourself when I can interrupt an answer."
"You interrupt them already."
"I have imagined other methods."
{n}The reply is quiet. She lets it remain an invitation instead of improving it with a joke.{/n}
{n}You tell her that you want to hear more. For a while the conversation belongs to the room you imagine together, to an arrival neither of you pretends has happened. When the city begins repeating the same passing light, she lets it repeat.{/n}''',
      c('[Keep the shared imagining private, and stay afterward.]', "after", flags=("jerribeth.counter_intimate_evening",)),
      c('"Stay with me in conversation now. I want to hear your voice without another scene around it."', "quiet", flags=("jerribeth.counter_quiet_chosen",))),
    n("quiet", "Jerribeth", '''"Show me where you put it, then. Only what you want me to see."
{n}You describe the place you choose when you intend to answer her. She asks whether the frame stands upright or lies waiting to be turned. You tell her. The question seems to interest her more than the furnishings.{/n}
"Mine faces away until I am ready. I turn it toward me, decide something is wrong with the light, and move it. Then I become annoyed that I have spent so long preparing to appear unoccupied."
"You could answer before moving it."
"I could. You could stop noticing every pause I leave you. We are apparently fond of making unnecessary work."
{n}She puts the image of the city farther behind her. For the rest of the evening you tell her things too small to have found their way into a report. She remembers one later and asks about it before you have finished the next.{/n}''', c('[Stay until it is time to close the connection.]', "after")),
    n("after", "Narrator", '''{n}The invented city's lights have thinned. Jerribeth draws one street into a straight line, tries it, and puts it back the way it was.{/n}
"Serit will say it cannot be built. I shall enjoy explaining that I did not ask him to build it."
"Will you show him?"
"A part. The part I intend to pay him to make move. There is no reason he should have the window as well."
{n}She looks toward you again. The quiet lasts long enough for you to hear the faint hum of the charm.{/n}
"I have decided where I want it. If I acquire a room worth keeping, that wall. A city that refuses to settle into a sensible arrangement, and an evening in which no one arrives to tell me who owns it."
{n}She leaves the wish there, without furnishing it with a claim that such a room already exists.{/n}''',
      c('"Keep space for this frame beside it. I meant what I said about making time for you."', "promised", requires=("jerribeth.committed",)),
      c('"Show me the next street you change. I want another evening here."', "next"),
      c('"You asked me to find a loophole large enough for two. I have not forgotten. This window still opens only onto an image."', "fate", requires=("jerribeth.fate_terms",))),
    n("promised", "Jerribeth", '''"I have kept space. You have been occupying it with remarkable confidence for some time."
{n}Her hands move together, then part before they meet.{/n}
"I like the confidence. Do not become modest now that I have said so."
"I will try to endure the compliment."
"You will repeat it to yourself until I supply another. I have learned how to recognize that expression."
{n}She leaves a little light beside the invented window, exactly where a frame might stand.{/n}''', c('[Keep the next invitation without changing the promises already made.]', "end")),
    n("next", "Jerribeth", '''"Then come back before I improve it beyond recognition. I occasionally make that mistake."
{n}She moves one light to the corner of the window. It illuminates nothing yet.{/n}
"You may bring an opinion. I reserve the right to dislike it."
"You usually bring enough for both of us."
"Then you have no excuse to arrive empty-handed."
{n}The answer comes with the exact pause you described earlier. She notices you noticing, and this time leaves it alone.{/n}''', c('[Accept another evening without making a new promise about the future.]', "end")),
    n("fate", "Jerribeth", '''"I noticed. I have been extremely patient with the architecture."
{n}She traces the window's sill on her side, careful to remain within the image.{/n}
"Find your opening. Show me what it costs before you make it. I would prefer to arrive as myself, and I am attached to several inconvenient parts of that arrangement."
"Including your opinions?"
"Especially the ones you keep hoping will improve."
{n}She takes her hand away from the sill. The frame remains exactly as it was.{/n}''', c('[Keep the question open without claiming to have solved it.]', "end")),
    n("end", "Jerribeth", '''{n}Before you part, Jerribeth returns the little faceless puppet to the edge of her image. It raises one hand as though preparing to make a declaration.{/n}
"I have found its proper occupation," she says.
{n}The puppet opens a tiny door and gets out of the way. Beyond it is the impossible city, seen from beneath the first turning street.{/n}
"There. It finally knows when to stop talking."
"You should keep it."
"I intend to. It reminds me how much worse this conversation could have been."
{n}She waits through your laugh before wishing you a good night. The little door remains open until you turn the frame away.{/n}''', c('[End the evening and keep the invitation.]', flags=("jerribeth.counteroffer_kept",))),
], requires=("jerribeth.counter_spoils_settled",))
