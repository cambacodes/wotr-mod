"""A career decision and the future of Konomi's authored private courtship."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, nodes, requires=(), delay=48):
    for node in nodes:
        node["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", 3, "", nodes,
                        Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
                        requires=("konomi.dismissed", "konomi.office_completed", "konomi.private_returned", *requires),
                        forbids=("konomi.present", "inhuman", "konomi.farewell", "konomi.private_future"),
                        delay=delay, optional=True))


s("lease_offer", "The name on the next agreement", [
    n("start", "Konomi", '''{n}Konomi meets you outside the building whose lease brought her back to Drezen. A woman is locking the door behind her. She thanks Konomi, gives you a curious glance and leaves with a folded agreement under her arm.{/n}
"The tenant," {n}Konomi says.{/n} "She has signed. Fewer rooms than she wanted, with the option to take the rest after the first season. She will have less space and enough money left to put something in it."
{n}She watches the woman turn the corner.{/n}
"The owner has offered me a different kind of work. I have been trying to decide how much of my pleasure in the offer is vanity."''',
      c('"Tell me what she wants you to do."', "offer"),
      c('[Arrange to hear about it when you have more time.]', abort=True)),
    n("offer", "Konomi", '''"Negotiate her future leases. Choose which proposals reach her table. Introduce her to people in the capital who have money and no trustworthy place to put their goods. She has buildings. I have names."
{n}Konomi glances up at the shuttered windows.{/n}
"I spent this week keeping her from obtaining everything she asked for. Apparently she would prefer me on her side of the next table."
{n}She sounds pleased, and does not attempt to disguise it.{/n}
"This is work that could become something. A person who decides which proposals are heard eventually receives rather more interesting proposals."''',
      c('"You miss having that kind of influence."', "influence"),
      c('"Your current client may not be pleased to hear it."', "client")),
    n("influence", "Konomi", '''"Yes. I miss being consulted before a decision is made, rather than being asked to rescue it afterward. I miss knowing that the woman who has ignored my letter will eventually have to answer me in person."
{n}She folds her hands behind her back.{/n}
"You may find that less attractive than watching me sort out two wagons. I enjoyed that work. I do not intend to spend the rest of my life proving how little I need."''', c('"What would accepting cost you?"', "cost")),
    n("client", "Konomi", '''"No. I shall have to tell her. She hired me to obtain terms the owner disliked, and now the owner would like to hire me. I have not forgotten how that looks."
{n}She turns toward you.{/n}
"I also know who will receive the offer if I refuse it. Somebody who will be very comfortable charging my former client more, without having spent a week hearing what she can afford."
{n}She pauses.{/n}
"That is a convenient argument. I have noticed."''', c('"Then what would accepting cost you?"', "cost")),
    n("cost", "Konomi", '''"Some of the people who trust me to negotiate for them will stop doing so. If I act for the owner, they should hire somebody else. I cannot promise them the same advocate on the other side of the bargain."
{n}She takes a folded offer from her sleeve but does not open it.{/n}
"The first decision concerns the empty rooms. The owner wants me to begin finding occupants immediately. My client's option gives her first refusal after the season. I negotiated that clause. I shall insist it is honored."
{n}Her thumb rests on the fold.{/n}
"I could finish the notices and accept now. Or I could wait until my client has had time to find somebody who will examine the arrangement solely for her. The owner will not hold the full fee open while I wait."''',
      c('"Honor the signed option, tell her about the change and take the work. She can choose her next adviser."', "accept", flags=("konomi.career_accepts_now",)),
      c('"Give her time to find that adviser. You negotiated the clause you would now be paid to work around."', "wait", flags=("konomi.career_waits",))),
    n("accept", "Konomi", '''"That is what I want to do. I asked you as though I were weighing it. I was canvassing a vote I already had."
{n}She unfolds the offer and reads the last lines again.{/n}
"I will tell her myself before I sign. She may decide I have been looking beyond her business all week. I was not, but I doubt another excellent explanation will make her pleased for me."
{n}She folds the paper carefully.{/n}
"I will have to bear that. I want the work."''', c('[Walk with her as she goes to find the tenant.]', "walk")),
    n("wait", "Konomi", '''"I would not be paid to break it."
{n}The answer comes quickly. She looks back at the building and is silent for a moment.{/n}
"But I would begin by knowing every concession she was prepared to make. Yes. She ought to have time to put somebody else beside her before I begin answering the owner's questions."
{n}She tucks the offer away.{/n}
"I will ask for a later start and accept the smaller fee. Do not expect me to be gracious when I discover what the delay cost. I can agree with you and still dislike the arithmetic."''', c('[Walk with her as she goes to find the tenant.]', "walk")),
    n("walk", "Konomi", '''{n}At the corner she stops and checks which way the tenant went.{/n}
"I will send word to arrange supper when I have finished speaking to them both. I may bring a less agreeable account of myself than the one I could write before this conversation."
{n}Her fingers brush yours.{/n}
"Save me a place anyway."''', c('[Agree to the evening.]', flags=("konomi.career_decided",))),
], requires=("konomi.reunion_kept",))

s("chosen_evening", "The evening she asked for", [
    n("start", "Narrator", '''{n}Konomi arrives at your agreed supper with her hair loosened from its traveling arrangement and no papers in her hands. She thanks you for waiting, sits and takes the cup you offer.{/n}
{n}She drinks before she speaks.{/n}
"I have told them both."''',
      c('[Ask how the tenant received her decision to begin now.]', "now", requires=("konomi.career_accepts_now",)),
      c('[Ask whether the owner accepted the later start.]', "later", forbids=("konomi.career_accepts_now",)),
      c('[Ask to postpone supper.]', abort=True)),
    n("now", "Konomi", '''"The owner was delighted. The tenant asked how much of our negotiation I had spent imagining what I would earn from the other side. I said none of it. She did not believe me."
{n}Konomi turns the cup in her hands.{/n}
"She paid what she owed and asked me not to introduce her to anybody else. I had several names ready. I did not give them to her."
{n}She looks up.{/n}
"I signed the new offer. I still intend to do the work. It would be convenient if regretting the way she looked at me made me want it less, but it has not."''',
      c('"A good bargain with a bad afternoon attached. They usually come together."', "heard"),
      c('"I understand why she is angry. You may have to let her stay angry."', "heard")),
    n("later", "Konomi", '''"At a smaller fee, as promised. She congratulated me on my scruples and deducted the amount before I had finished being pleased with myself."
{n}Konomi takes another drink.{/n}
"The tenant has found an adviser. She thanked me for waiting and then asked the adviser to examine everything I had negotiated. I nearly objected. Imagine how distinguished that would have sounded."
{n}She sets down the cup.{/n}
"They will meet without me before I begin for the owner. I shall spend the interval making introductions in Nerosyan. I have managed to acquire both less money and more traveling. I still want the work."''',
      c('"You kept your word on the clause. In your trade that is worth more than the fee."', "heard"),
      c('"I hope the introductions prove worth the cost."', "heard")),
    n("heard", "Konomi", '''"There. That is the whole account, and you did not interrupt it once. I may start billing you as a confessor."
{n}She reaches for the food. You eat while she describes the names she hopes to approach, growing more animated as she explains which woman might answer an invitation from which other woman.{/n}
{n}Halfway through an account of a profitable quarrel, she catches your expression and stops.{/n}
"I left the papers behind. I appear to have brought their contents with me."''',
      c('"You are enjoying yourself. I like seeing it."', "pleasure"),
      c('"Finish the quarrel. Then I want your attention for myself."', "attention")),
    n("pleasure", "Konomi", '''"I am. Even after today."
{n}She looks almost surprised to hear herself admit it.{/n}
"When I lost the office I assumed I would have to pick: a smaller life with you in it, or the capital without. I dislike choosing between two poor offers. I have spent my career refusing to."
{n}Her hand comes to rest beside yours.{/n}
"I am glad I did not."''', c('[Stay with her after supper.]', "close")),
    n("attention", "Konomi", '''"Then the abbreviated version: neither woman will yield first, but each would be offended if I approached the other before approaching her. I intend to invite them both to the same breakfast. I shall eat beforehand."
{n}She leans toward you, her smile deepening.{/n}
"There. You have my attention. I hope you intend to make good use of it."''', c('[Stay with her after supper.]', "close")),
    n("close", "Konomi", '''{n}After the dishes have been put aside, she draws her chair close enough for her knee to press against yours, and lays her fan on the table between the cups, closed.{/n}
"Two items remain on the agenda. I intend to keep seeing you like this. And I intend to kiss you. I have put them in order of importance, and I am about to take them out of order."''',
      c('"Yes. I want this courtship, and I want you to stay tonight."', "night", flags=("konomi.private_night_chosen",)),
      c('"Both items carried. Take the second slowly, and give me the rest of the evening sitting just like this."', "quiet", flags=("konomi.private_quiet_chosen",)),
      c('"I care for you, but I do not want a romance."', "friends")),
    n("night", "Konomi", '''{n}She takes your hand and rises with you. When you kiss her, she answers with an eagerness that makes the careful beginning of the evening seem very far away.{/n}
{n}Her fingers close on your collar. She draws you back when you start to speak.{/n}
"You may tell me afterward. I have waited through an entire correspondence for this; I am not waiting through a speech."
{n}She walks you backward to the bed by your collar, then releases it to shrug off her coat and pull her sash free. You open the robe. She presses into your hands, warm and quick-breathing, and gives a low, impatient laugh when your fingers pause. Her own fingers finish your fastenings.{/n}
{n}She pushes you back onto the bed and follows, kissing you until both of you need breath. Her loose hair brushes your chest. She draws your hands to her bare sides and pulls you closer.{/n}
{n}Her knees settle either side of you and she lowers her weight onto you, flushed to the collarbone, and presses down once, slowly, with her eyes shut and her lower lip caught in her teeth. The breath that leaves her is nearer a curse than a sigh. When she looks at you again the cool, composed correspondent has been dismissed from the room.{/n}
"There. You may stop being polite." {n}Her fingers go to your belt and are not delicate about it.{/n}''', c('[Stay together through the night.]', "morning")),
    n("quiet", "Konomi", '''"Gladly."
{n}She settles beside you. At first she keeps finding reasons to speak; then she puts her head against your shoulder and lets one unfinished sentence remain unfinished.{/n}
{n}You stay like that until a noise in the passage makes her lift her head. She looks toward the door, then settles back against you with a small, satisfied breath.{/n}
"Nothing that requires us."
{n}You arrange to share breakfast before parting for the night. She takes her time saying goodbye.{/n}''', c('[Meet her for breakfast as promised.]', "morning")),
    n("morning", "Konomi", '''{n}At breakfast, she watches you reach for the bread and moves the plate toward you before you ask.{/n}
"I meant what I said last night. I would like to keep doing this."
{n}She gives you a brief, searching look, then relaxes when you answer.{/n}
"Good. There is something about the journeys we should discuss before I go back. After we have eaten."''',
      c('[Agree to talk about your future together.]', flags=("konomi.lovers", "konomi.attracted", "konomi.private_evening_kept",))),
    n("friends", "Konomi", '''{n}She withdraws her hand and sits back. For a moment she looks down at her empty hands.{/n}
"I see. Plainly said, at least. Do not speak for a moment. I am revising several plans."''',
      c('[Tell her you want to end the relationship.]', "old_parting", requires=("konomi.lovers",)),
      c('[Explain that you do not want to begin a romance.]', "first_parting", forbids=("konomi.lovers",))),
    n("old_parting", "Konomi", '''"Then we are ending something. Do not make it smaller because that would be easier to explain. I know why I invited you. I remember why you used to come."
{n}She speaks firmly, but her hands remain very still.{/n}
"I can accept that you no longer want it. I cannot pretend that I had not been hoping to recover more of it with you."''', c('[Tell her it was worth every evening.]', "parting_finish")),
    n("first_parting", "Konomi", '''"I had hoped these evenings were becoming a courtship. I would have asked you here sooner if I had been less afraid of making that obvious."
{n}She looks toward you again.{/n}
"I am disappointed. I shall be disappointed at some length, in private. At least you did not sell me a promise you meant to default on. I have bought enough of those."''', c('[Let her have the last word.]', "parting_finish")),
    n("parting_finish", "Konomi", '''{n}She gathers herself before looking at you again.{/n}
"Do not ask me to be your friend by morning. I have never once signed a new treaty the same day the old one was torn up."
{n}She picks up her fan and does not open it. You say goodbye, and she lets you see yourself out.{/n}''',
      c('[Take her answer and end the courtship.]', flags=("konomi.closed", "konomi.private_parted", "konomi.private_future"))),
], requires=("konomi.career_decided",), delay=48)

s("private_future_choice", "The journeys after this one", [
    n("start", "Konomi", '''{n}Konomi has booked her journey back to Nerosyan. She tells you the departure day while you walk through the courtyard, then stops beside the place where you first saw her after the long correspondence.{/n}
"I have been offered the room here when I need it. I shall keep the one in Nerosyan as well, for as long as the work makes that sensible."
{n}She watches a woman carry a basket across the courtyard, waiting until you are alone again.{/n}
"I want to know whether we are making plans for visits, or for a life that includes them."''',
      c('"I want a life with you. It does not have to fit in one city."', "commit", forbids=("konomi.committed",)),
      c('"I still want the life we promised each other. Let us make room for these journeys in it."', "commit", requires=("konomi.committed",)),
      c('"I want to keep seeing you. I will not sign for a shared life yet."', "open", forbids=("konomi.committed",)),
      c('"I cannot keep this up. Not across two cities and a war."', "part"),
      c('[Ask to finish this conversation when you can give it your full attention.]', abort=True)),
    n("commit", "Konomi", '''{n}She takes a breath, and for once does not turn it immediately into an answer.{/n}
"Yes. I would like that."
{n}Her hand finds yours.{/n}
"Then here is the treaty. Tell me before you march, and I shall tell you before I buy a seat on a wagon. If the war takes an evening from us, send word when you can. I would rather curse a demon than spend the night wondering whether you forgot me."
{n}She smiles at you.{/n}
"There will also be days when I arrive earlier than expected. I have been thinking about those."''',
      c('"Every article agreed. And I keep the promises I have made elsewhere. You would think less of me if I broke them."', "kept", flags=("konomi.committed", "konomi.private_future_committed"))),
    n("open", "Konomi", '''"Then we shall make the next visit. I would rather know what you are offering than discover later that you agreed because I was about to leave."
{n}She lets the silence last for a moment.{/n}
"I may want more than that in time. If I do, I will tell you. For now, I would like to see you again."
{n}She offers her hand.{/n}
"Write when you have a date to offer. I shall do the same."''',
      c('[Promise another visit without promising more than you mean.]', "kept", flags=("konomi.private_future_open",))),
    n("kept", "Narrator", '''{n}You agree where to send the next letter and which plans must be settled before either of you travels. Konomi writes your answer beneath her own departure arrangements and folds the paper away.{/n}
{n}On the day she leaves, you meet her at the yard. There is less to explain this time. She holds your hand for a moment, checks that her bag is secure and climbs onto the bench.{/n}
{n}Before the wagon moves, she looks back.{/n}
"I shall write after the introductions. If they go badly, I expect you to read the whole account anyway."
{n}You watch her go with a plan for the next meeting already begun.{/n}''',
      c('[Keep the correspondence and the plans you made together.]', flags=("konomi.private_future",))),
    n("part", "Konomi", '''{n}She looks down at your hands, then moves hers to the strap of her bag.{/n}
"I thought you might say that. I had hoped you would not."
{n}You talk until she understands what you can and cannot offer. She asks one question twice, as though the second wording might produce an answer she would prefer. At last she nods.{/n}
"Then we should stop making plans that require you to want something different."
{n}At the courtyard gate she says goodbye. When her wagon leaves, you are not waiting at the yard.{/n}''',
      c('[Let the relationship end.]', flags=("konomi.closed", "konomi.private_parted", "konomi.private_future"))),
], requires=("konomi.private_evening_kept",), delay=24)


def ending(id, text, requires=(), forbids=()):
    SCENES.append(scene("konomi.ending_" + id, "Letters without a seal", "Epilogue", 5, "", [
        n("start", "Narrator", text, c(), portrait="Konomi"),
    ], Relationship="konomi", last=99, requires=("konomi.private_future", *requires), forbids=forbids))


ending("distance", '''{n}Lady Konomi's work took her between the capital and the people whose proposals she hoped to bring there. She acquired clients, influence and a number of correspondents who read her letters with mixed anticipation.{/n}
{n}Her journeys to the Commander were arranged with rather more care than her clients knew. Both kept promises elsewhere; both learned to send word when a visit had to change. There were quarrels, missed wagons and reunions for which Konomi abandoned the account she had prepared and simply took the Commander's hand.{/n}
{n}They never found a single address that described their life together. They grew very good at finding one another.{/n}''', requires=("konomi.committed",), forbids=("konomi.closed", "inhuman", "ascended"))
ending("distance_open", '''{n}Konomi and the Commander continued to exchange letters and arrange visits when their work allowed. Neither pretended that a meeting promised a future they had not agreed upon.{/n}
{n}Some visits were brief. Others lasted longer than planned. Konomi kept her rooms in Nerosyan, pursued the influence she wanted and learned which of the Commander's invitations she could accept without abandoning her own plans.{/n}
{n}What they had remained a courtship. For as long as they both chose it, they found reasons to make the journey.{/n}''', requires=("konomi.private_future_open",), forbids=("konomi.committed", "konomi.closed", "inhuman", "ascended"))
ending("distance_apart", '''{n}After their private courtship ended, Konomi ceased arranging her journeys around the Commander's free evenings. Her work still brought her to Drezen, but she stayed where her clients could find her and left when her business was done.{/n}
{n}The letters traveled with her for a while. Eventually she found a place for them in Nerosyan, among the things she wanted to keep without carrying on every journey.{/n}''', requires=("konomi.closed", "konomi.private_parted"))
ending("distance_changed_open", '''{n}The Commander's transformation overtook a courtship that had never become a promise of a shared life. Konomi stopped arranging visits. She had wanted more time to discover what they could become together; she had not agreed to every future that power might make possible.{/n}
{n}For a while she kept an unfinished letter beside her work. Eventually she put it away. Her own plans still required answers, and she began making them without waiting for another invitation.{/n}''', requires=("konomi.private_future_open", "inhuman"), forbids=("konomi.committed", "konomi.closed", "ascended"))
ending("distance_ascended_open", '''{n}After the Commander's ascension, Konomi sometimes addressed a letter to a destination no receiving agent could find. She described her work, recalled an evening and asked whether the new divinity had retained any interest in ordinary invitations.{/n}
{n}She did not build her life around an answer. There were journeys she could arrange herself, ambitions she could pursue and people who would meet her at an agreed address. Whatever became of the letters, she continued to make those plans.{/n}''', requires=("konomi.private_future_open", "ascended"), forbids=("konomi.committed", "konomi.closed"))
