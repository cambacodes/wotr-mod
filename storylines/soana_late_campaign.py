"""Earned living Chapter 5 Soana return and authored campaign conclusions.

Contact remains the native Wintersun unit; no actor, guardian or forest is restored.
New people, temporary rites and local incidents exist in dialogue, not world-state APIs.
"""
from copy import deepcopy
from story_format import c, n, scene

SCENES = []
ACTOR = "64805abb52739e44280a758f850b300c"
ANSWERS = "2b1776f3e398685479ff6b16290b4cc2"
WINTERSUN = "0a5654e7dc18f074d9356009d55eb51b"
LOSS = ("soana.dead", "soana.killed_by_camellia", "soana.forest_dead")
VOICE_TALES = (
    c('"Something in the Abyss used your voice. I did as you taught me and did not answer it."', "voice_silent",
      requires=("soana.abyss_voice_unanswered",)),
    c('"Something in the Abyss used your voice. I asked it to insult me."', "voice_tested",
      requires=("soana.abyss_voice_tested",)),
    c('"Something in the Abyss used your voice. I went out after it."', "voice_followed",
      requires=("soana.abyss_voice_followed",)),
)


def s(id, title, entry, nodes, previous, delay=24):
    for page in nodes:
        page["Portrait"] = "Soana"
    SCENES.append(scene("soana." + id, title, "Soana", 5, entry, nodes,
        Relationship="soana", Chapters=[5], last=5, ContactUnit=ACTOR,
        Areas=[WINTERSUN], AnswerLists=[ANSWERS],
        RequiresAny=["soana.old_defender", "soana.bear_dead"],
        requires=("soana.after_quest", "soana.progression_kept", previous),
        forbids=(*LOSS, "soana.closed", "inhuman"), delay=delay, optional=True))


# --- PP6 (Chapter 4): past the firelight. ---------------------------------------------------------------------------------
# She is in Wintersun and the Commander is in the Abyss, and she sends nothing. What travels is what she taught at the
# shrine working (soana_later_progression: the_inherited_debt/price "Do not follow them into the trees", "A stolen sound is not
# your brother"; a_voice_in_the_dark/voice "It cannot make a conversation. It can only steal one side."). The voice at the camp's
# edge is authored and never identified. Path-neutral (N-all): it reads only her registered route. The Commander's answer is
# read by when_the_road_returns (Chapter 5), in the welcome or the friend greeting.
VOICE_SILENT = "soana.abyss_voice_unanswered"
VOICE_TESTED = "soana.abyss_voice_tested"
VOICE_FOLLOWED = "soana.abyss_voice_followed"
VOICE_CHOICES = (
    c('[Do as she taught you. Keep your place, keep the fire, and do not answer.]', "silent"),
    c('[Ask it for something only Soana would give you, and listen for the other side of the conversation.]', "tested"),
    c('[Take a burning stick from the fire and go out to see what is wearing her voice.]', "followed"),
)
memory_nodes = [
    n("start", "Narrator", '''{n}Night in the Abyss is a matter of opinion. The light goes a dull red, and the camp agrees to call it night. You have the second watch.{/n}
{n}Out past the firelight, where the ground falls away into something that is not quite rock, a voice calls you what she calls you.{/n}
"Hunter. You have let the fire get low. See to it, before I do it myself and burn my fingers."
{n}It is Soana's voice. Every crack in it is where it belongs.{/n}''',
        c("Continue", "heard", requires=("soana.rite_voice",)),
        c("Continue", "told", forbids=("soana.rite_voice",))),
    n("heard", "Narrator", '''{n}At the working she stood with her back to a stolen voice and would not turn round. "It cannot make a conversation," she said, with her eyes on the bowl. "It can only steal one side."{/n}
{n}Then it had used her own voice, younger and furious, and you watched her go pale and keep speaking.{/n}
{n}You cannot tell what is out there tonight. You remember what she taught you.{/n}''',
        *VOICE_CHOICES),
    n("told", "Narrator", '''{n}Before the working she told Meret what the thing would do, with you standing beside them. "If the voices come afterwards, they are scraps it has left behind. Do not follow them into the trees." And, when Meret asked whether it would keep her brother: "A stolen sound is not your brother."{/n}
{n}You cannot tell what is out there tonight. You remember what she taught you.{/n}''',
        *VOICE_CHOICES),
    n("silent", "Narrator", '''{n}You put another stick on the fire. The voice tells you again that you have let it get low, in the same words and the same tone, and then a third time.{/n}
{n}Soana would not scold you three times in the same words. She would have found a worse word by the second.{/n}
{n}Near the end of your watch it stops in the middle of "hunter", as if whatever was using it had run out of breath and could not find more.{/n}''',
        c("[Keep it to tell her.]", flags=(VOICE_SILENT,))),
    n("tested", "Narrator", '''"Soana," {n}you tell the dark.{/n} "Call me something rude. Anything. You have never once run short."
{n}The dark tells you that you have let the fire get low. You ask again. It tells you about the fire again, word for word, and there it is, the thing she showed you: one side of a conversation, and nobody on the other.{/n}
{n}You laugh, which you had not expected to do in the Abyss. Out past the firelight something goes quiet, and stays quiet until your watch is done.{/n}''',
        c("[Keep it to tell her.]", flags=(VOICE_TESTED,))),
    n("followed", "Narrator", '''{n}You take a burning stick and walk out past the light. The voice goes on ahead of you, always just over the next rise, telling you the fire is low.{/n}
{n}You go farther than you should. When you look back, the camp is a red coin in the dark. The voice stops. There is nothing on the rise and nothing beyond it, and the ground under your boots is warm, as if something had been lying there a moment ago and had moved off without a sound.{/n}
{n}You walk back with the stick burning down towards your fingers. The soldier you were meant to wake for the next watch is already up, blade drawn, and tells you in a furious whisper exactly what the camp thought had happened to you. She would call you a fool for this too. You find you want very much to hear her say it.{/n}''',
        c("[Keep it to tell her.]", flags=(VOICE_FOLLOWED,))),
]
for page in memory_nodes:
    page["Portrait"] = "Soana"
SCENES.append(scene("soana.past_the_firelight", "Past the firelight", "Soana", 4, "", memory_nodes,
    # Not soana.after_quest: SoanaAfterQuest plays only in WintersunOutdoor (area link), and this page is read in the Abyss.
    requires=("soana.progression_kept",),
    forbids=(*LOSS, "soana.closed", "inhuman", VOICE_SILENT, VOICE_TESTED, VOICE_FOLLOWED), delay=24, last=4, optional=True,
    Relationship="soana", Chapters=[4], Remote=True, Kind="memory"))


s("when_the_road_returns", "When the road returns", '"I wondered what you would say when I came back."', [
    n("start", "Soana", '''{n}Soana turns with a bundle of roots in her hand. She sets it on a stone, missing the flat part. The roots roll apart. Her eyes remain on your face.{/n}
"So. The road has spat you back at last."
{n}She catches a root at the edge of the stone.{/n}
"I had a fine scolding ready. Three fine scoldings. You have kept me waiting long enough to wear them all out."
"I came back."
"I have eyes, child. Come here before I remember the worst of them."
{n}She leaves the roots scattered and comes toward you, her stick still leaning against the cave wall.{/n}''',
        c('[Greet the woman you are courting.]', "welcome", requires=("soana.later_courting",)),
        c('[Greet your old friend.]', "friend", requires=("soana.later_friends",)),
        c('"I cannot stay yet. I came to show you I was back."', abort=True)),
    n("welcome", "Soana", '''{n}Soana catches both your hands and draws you down toward her. Her gaze passes over your face, stopping at a mark the road has left. She rubs it with her thumb.{/n}
"They have been careless with you."
"You are examining me?"
"Someone must. Hold your head down."
{n}She kisses you, firmly enough to push your head back a little herself. Then she grips your hands again.{/n}
"Thin as a winter hare. Have they forgotten that even Commanders eat?"
"I missed you."
"Then you have one scrap of sense left. Walk with me. Tell me what you saw. Something besides blood and ruined houses."
{n}She fetches her stick, keeping your hand until the broken ground forces her to watch her footing. Beyond it, her fingers close around yours again.{/n}
"And speak up. I have heard quite enough wind at this cave mouth. It never brings an interesting tale, however much noise it makes."''', c('[Walk with her toward the nursery.]', "nursery"),
        # PP6: what the Commander did with the voice past the firelight (past_the_firelight, Chapter 4).
        *VOICE_TALES),
    n("friend", "Soana", '''"Still that foolish opening. Did nobody teach you a better greeting on the road?"
"You could begin again."
"And leave those roots to shrivel while we exchange courtesies? Walk, child."
{n}She takes her stick and waves you to her side. When you glance at the roots, she raps the stone with its end.{/n}
"Leave them. They have survived worse than being dropped."
{n}You tell her about a place on the road where wind in dry grass sounded like running water. She asks which way the ground sloped. At your answer she nods and looks toward the trees.{/n}
"Dry grass. There was a time when you could hear water all through these woods. Even under the songs at the festival."
{n}Her stick knocks a loose pebble out of the path.{/n}
"You remembered to bring me something besides a wounded beast. Wonders have not quite ceased. Come. There is more to see here than my doorstep."
{n}She turns toward the nursery. You follow beside her, stepping over the stone she dislodged.{/n}''', c('[Ask what the nursery looks like now.]', "nursery"),
        # PP6: what the Commander did with the voice past the firelight (past_the_firelight, Chapter 4).
        *VOICE_TALES),
    n("nursery", "Narrator", '''{n}You turn off the path before Soana points out the loose stone. She glances at your boots.{/n}
"The road has not shaken everything out of your head."
{n}Between two sheltering banks she stops and raises her stick toward the nursery ground.{/n}''',
        c('[Look at the trees her voice saved.]', "saved", requires=("soana.nursery_saved",)),
        c('[Look at the ground the working stripped bare.]', "lost", requires=("soana.nursery_lost",))),
    n("saved", "Soana", '''"Two died. A third insists on growing sideways. Look at it! The whole sky overhead, and it thrusts its head into the bank."
{n}She points to the crooked sapling. Small, plain leaves cover the surviving stems.{/n}
"The voices stopped at last. No more calling from the dark with a stolen mouth. Then that little wretch began to lean. I have been quarrelling with it ever since."
"You could have told me that first."
"I brought you here to see living trees. Look at them. I would spend the voice again."
{n}She bends the crooked stem between two fingers, then releases it. It springs back toward the bank.{/n}
"Stubborn thing. Corven used to laugh like that, before I had even finished telling him what he had done wrong."
"Like a tree?"
"Like someone who knew I could not uproot him. Do not spoil a perfectly good complaint."
{n}She wipes sap from her fingers onto her skirt.{/n}
"I still have no news of him. A thing stealing his voice knew no more than I did. It never stole that laugh. It could not have borne the scolding."''', c('[Return toward the upper path with her.]', "path")),
    n("lost", "Soana", '''{n}A few seedlings stand in a sheltered corner. Between them the soil is bare. Soana kneels and lifts a fallen twig from a tender shoot.{/n}
"Meret's seed. Some took. The rest has given me ample cause to curse."
"You have begun again."
"A forest does not wait for me to finish mourning it. Nor do dead stems turn green because I plant beside them. Look up there."
{n}Pale sticks stand farther along the slope. The dry ridge where the thing was contained has no green shoots.{/n}
"The bowl stays shut. The shrine stays shut. Let the fools who think silence means safety put their own fingers into a sleeping adder's mouth."
{n}She rises, brushing soil from her palm.{/n}
"Meret has found something beyond the hollow. She wants me to see it before her camp leaves. I was beginning to think you would arrive after every last hunter had gone. Then I could have blamed the whole lot of you at once."
{n}She takes up her stick and points toward the upper path.{/n}''', c('[Ask what Meret found.]', "path")),
    n("path", "Soana", '''{n}Meret waits at the upper bend with a cut length of wire wrapped around a stick. Her bow is on her back, the worn family mark at her belt.{/n}
"Snares beyond the hollow," {n}she says.{/n} "Not ours. Fresh hazel cuts, too, and sacks dragged over the ground. This one was empty. I left the others alone."
"You have kept your ankles, then," {n}Soana says.{/n}
"And I intend to keep up with my camp when it leaves."
{n}Soana tightens her mouth. Meret holds the wire out to you.{/n}
"I watched the eastern paths, as I said I would. Now you can follow what I found. Do not wait for me to settle here and grow a beard."
"I had not asked you to."
"Good. She has asked enough for both of you."
{n}Soana takes the stick, turns it without touching the wire and looks toward the way through the woods.{/n}
"Your grandmother never wasted breath on such impudence."
"She saved it for worse."''',
        c('"The carts stayed out of the cleft. Let us see who went beyond the path."', "cleft", requires=("soana.path_cleft",)),
        c('"We let them shelter from floods, not lay snares. Let us find the trapper."', "flood", requires=("soana.path_flood",))),
    n("cleft", "Soana", '''"Varn still carries his loads through. I hear his curses at the narrow turn before I see his face. He has found several new ones."
{n}Meret gives a short laugh.{/n}
"These cuts are beyond his carrying path. We follow the feet that went there. I will not frighten every fool carrying a sack and let the one with the knife escape."
"What would you have done without me?"
"Tracked them. Caught them. Found out whether a sharp word or a sharper fright would put some sense into their heads. Do you suppose I sat on that stone waiting for a Commander to tell me how?"
{n}She gives the wire back to Meret.{/n}
"Leave it outside the cave. I want to see whether the next trap has the same knots. And mind the loose end. Whoever made it did not trouble to smooth the cut."''', c('[Agree to inspect the eastern ground in daylight.]', "end")),
    n("flood", "Soana", '''"The families sheltered there twice. They left the marker and brought back kindling. One bundle was so wet I nearly sent it back tied to the fool who carried it."
"Did you tell Varn?"
"He heard. So did everyone within half a day's walk."
{n}Meret turns aside, her shoulders shaking once.{/n}
"The camp ends well short of this wire," {n}Soana says.{/n} "I want the hands that set it. And I want every loop out of the ground. Whether its owner leaves with ringing ears or a ringing head we can discover afterwards."
{n}She hands the wrapped wire back to Meret.{/n}
"Keep it by the cave. No bare fingers through the loop. It was made to close on something struggling. A hunter should know better than to lend it a hand."''', c('[Agree to inspect the eastern ground in daylight.]', "end")),
    n("end", "Soana", '''{n}Meret will show you the trail before her camp leaves. Soana starts to speak, then taps the wire with her stick.{/n}
"And your last report?"
"Here. I can stay for the inspection. After that you will have to manage without my grandmother looking over your shoulder."
"Your grandmother knew when to stop enjoying a point."
"No, she did not."
{n}Soana snorts. At the cave she gathers the scattered roots and drops them into their basket. She turns one over, breaks off a rotten end and flings it away.{/n}
"Snares. Cut branches. A hunter with a tongue like a thorn hedge. A fine welcome you have found."
{n}Her hand closes briefly on your forearm.{/n}
"Come in daylight. Wear boots you can put in mud. I have no use for someone standing on a stone admiring the shine of them."
{n}She pushes the root basket out of your way, leaving the place beside the entrance clear.{/n}''', c('[Return in daylight to follow the trail.]', flags=("soana.late_returned",))),
    n("voice_silent", "Soana", '''{n}You tell her about the voice past the firelight in the Abyss, and that you kept your place and did not answer it.{/n}
"Good." {n}She says it at once, then gives you a sidelong look.{/n} "And what did it say? In my voice."
"That I had let the fire get low."
"Pff! Then it had that much right. You always do." {n}She walks a few steps before she speaks again.{/n} "Three times, the same words? Then it had never heard me twice. I would have found a worse word by the second."''',
        c('[Walk on with her toward the nursery.]', "nursery")),
    n("voice_tested", "Soana", '''{n}You tell her about the voice past the firelight in the Abyss, and that you asked it to insult you.{/n}
"You asked it for an insult?" {n}She stops on the path.{/n}
"It only had the one. It kept telling me about the fire."
{n}Soana laughs, a short bark that startles something out of the bushes.{/n} "Of course it did. A stolen sound has one side and no temper. You should have asked me. I have dozens." {n}She raps your shin with her stick, not hard.{/n} "There. Now you have heard the real thing. Do not forget the difference."''',
        c('[Walk on with her toward the nursery.]', "nursery")),
    n("voice_followed", "Soana", '''{n}You tell her about the voice past the firelight in the Abyss, and that you took a burning stick and went after it.{/n}
"You followed it." {n}Her stick comes down on the path between your boots.{/n} "Into the dark. In the Abyss. Because it had my voice."
"There was nothing there."
"There was nothing there that night." {n}She takes hold of your sleeve and does not let go.{/n} "I said it before the working, in plain words, with my own mouth. Do not follow them. And you went after a copy of my mouth instead." {n}Her grip tightens.{/n} "Fool. Bloody hunter."
{n}Then, more quietly, still holding on:{/n} "Was it so very like me?"''',
        c('"Like enough to follow. Not like enough to scold me."', "nursery")),
], "soana.progression_kept", delay=0)

s("a_track_with_two_ends", "A track with two ends", '"Show me where Meret found the wire."', [
    n("start", "Soana", '''{n}Meret leads you beyond the upper bend to churned earth. Soana carries a short hooked stick, its lower end wrapped in cloth.{/n}
"For lifting wire. Keep your sword out of it unless you want a loop round your wrist."
{n}Dragged sacks have left two furrows. Hoofprints cross them. A narrower trail passes beneath a hazel with its low branches cut away. Coarse gray hair clings to a thorn.{/n}
"I heard something there," {n}Meret says.{/n} "It stopped when I stopped. A wolf, perhaps."
{n}Soana bends toward the hair, keeping her fingers off it.{/n}
"Perhaps. Keep your feet back. You have already muddied enough ground for a herd of swine."
{n}Beyond the hazel something scrapes against a root. Meret lifts her head and listens. Soana points the hook toward the narrow trail.{/n}
"Now look. The earth has kept better count than the hunter."''',
        c('[Lore Nature DC 26] [Read the animal tracks and the trail of the trappers.]', check=dict(Skill="SkillLoreNature", DC=26, Success="read", Failure="mistake", CommanderOnly=True)),
        c('[Set Meret to watch while you and Soana examine the ground a strip at a time.]', "slow"),
        c('"We should come back when we can watch every step."', abort=True)),
    n("read", "Narrator", '''{n}The thorn carrying the hair stands below the height of the hoofprints' owner. The smaller tracks belong to a dog. A tether dragged beside them has brushed a line into the wet soil. Under the cut hazel the paw marks bunch together and stop.{/n}
{n}You point out the tether. Meret circles the hazel over bare stone and looks down at a dog lying with a hind foot caught in a wire loop.{/n}
"Alive. He would like me to count his teeth."
{n}Soana crouches where the dog can see her. She murmurs to it. A growl answers.{/n}
"Keep them, foolish beast. Nobody is taking your teeth."
{n}You trace the wire to its peg and show Meret where to slacken it. Soana lifts the loop with the padded hook. The dog bites the cloth, drags its leg free and crawls beneath the hazel before attempting to stand.{/n}
"Back," {n}she says.{/n} "Let it smell you before you thrust another hand at it."
{n}Beyond the freed animal more knots of wire run toward the camp along the small beasts' tracks. One loop holds a dead hare. Meret lifts her boot over an empty snare and points out the next.{/n}''', c('[Mark the other loops before following the tether toward its owner.]', "found_end")),
    n("found_end", "Soana", '''{n}The tether leads toward a woman carrying two empty sacks. The dog limps out to her. She drops the sacks and kneels.{/n}
"Tarn! You were tied."
{n}She finds the bitten tether, then sees the wire in Meret's hand.{/n}
"My snare. I did not set it for him."
"You are not hungry enough to eat your dog yet, then," {n}Soana says.{/n} "What were you after?"
"Hares. People at camp have to eat."
{n}The woman gives her name as Hessa. Her hand stays on Tarn's back as he tries the injured foot. Soana watches him stand.{/n}
"Show me the traps. All of them."
"Now?"
"While we can see them. Unless you would rather find the next with your own foot."
{n}Hessa leads you along the line, Tarn limping beside her. Before the light fails, every peg has been found and every loop pulled up. You gather the dead hare. Hessa takes it, leaving the dismantled snares wound tight around the stick.{/n}
"Settle the dog," {n}Soana tells her.{/n} "Then come to my cave. Bring whoever counts your stores. I want to hear how much of this wood you meant to carry away."
{n}Hessa picks up the sacks and nods.{/n}''', c('[Return knowing who set the snares and where they ran.]', flags=("soana.late_track_read", "soana.late_trail_known"))),
    n("mistake", "Narrator", '''{n}You take the narrow trail for the passage of an animal still moving in the scrub. A dry patch lies ahead. You step onto it. Wire draws tight against a branch, and a hoarse yelp comes from beneath the hazel.{/n}
{n}Soana catches your sleeve and jerks you back into your own footprint.{/n}
"Another line, bloody hunter! Use your eyes before your boots."
{n}A dog struggles beneath the branches. A snare holds its hind foot; its loose tether has caught in a second loop. Your step has pulled that line and sent the animal wrenching against the wire.{/n}
{n}Meret reaches bare stone beyond the hazel and calls to it. A woman comes running down the slope. Soana thrusts her stick across the woman's path.{/n}
"Look down!"
"Tarn. Stay, you foolish thing. Stay."
{n}At his owner's voice the dog stops pulling. She reaches him over the stone, supports his chest and holds him while Soana lifts the wire. Afterwards he stands on three feet, keeping the fourth raised.{/n}
{n}You say where you went wrong. The woman nods and bends over the injured foot. Soana winds the loose wire onto her stick.{/n}
"Now we look at every inch. Your blundering has not pulled the other snares out for us."''', c('[Help carry the dog clear, then inspect with Hessa rather than guessing again.]', "late_end")),
    n("slow", "Soana", '''{n}Meret climbs above the hazel and watches from a rock. She calls down when she has a clear view.{/n}
"A dog. Low to the ground. He is pulling toward a tether caught on a root. There is wire at his foot. I cannot see the end."
{n}You and Soana begin at undisturbed earth. Her stick points to a bent twig, a leaf lying against its neighbors, a scrape at a root. You trace each line before moving anything. The dog growls whenever a branch shifts.{/n}
"Yes, yes," {n}Soana mutters.{/n} "Bite the air if you must. Leave that foot alone."
{n}An empty loop comes first. The second holds the tether; a third grips the dog's hind foot. You call their positions to Meret. She repeats them, then climbs down over stone.{/n}
{n}A woman from the camp hears you and arrives while you loosen the first peg. She names herself Hessa and the traps as hers. Soana sends her over the stone to hold the dog while the wire comes away.{/n}
{n}Tarn limps out of the scrub. He can walk, though he keeps stopping to lick the foot. The search has taken most of the clear afternoon. Shadows now cover the rest of the line.{/n}
"No one crosses tonight," {n}Soana says.{/n} "Not even the fool who swears she remembers every peg. Especially her."''', c('[Mark the closed approach and arrange to finish the inspection in daylight.]', "slow_end")),
    n("late_end", "Soana", '''{n}Hessa carries Tarn to dry ground near the camp and settles him on an old cloak. She will keep him off the foot and watch it. No one offers a cure.{/n}
{n}You follow her back along the traps she remembers. Those loops come up; the remaining approach is marked. At the first failing light Soana plants her stick across the path.{/n}
"Enough. You have half your wits beside that dog. I will not lend my ankle to find what the other half has forgotten."
{n}At dawn Hessa meets you alone. Tarn is with someone at camp. Two more loops lie hidden under leaves. You dismantle them and take up the remaining wire. Hessa lifts the hare from the snare that caught it.{/n}
"I will bring our stores keeper to hear what you want."
"You have ears. Bring someone who can answer for what you took."
{n}Hessa wraps the empty wire around a piece of wood and agrees. Meret has held back her departure to finish the inspection. She shoulders her pack again and points toward the cave.{/n}
"The meeting, then I go. You can quarrel without me."''', c('[Return after the inspection, remembering Tarn\'s injured foot.]', flags=("soana.late_track_missed", "soana.late_trail_known"))),
    n("slow_end", "Soana", '''{n}Hessa takes Tarn to camp. The marked approach remains empty overnight. In the morning she brings the sacks and walks the trap line from its beginning, pointing out every loop before anyone crosses it.{/n}
{n}Tarn follows for a short distance. Hessa sends him back. He lifts his sore foot, looks at the scrub and limps toward camp without further argument.{/n}
{n}You dismantle the line. One snare holds a hare. Hessa glances at Soana before taking it.{/n}
"Eat it," {n}the shaman says.{/n} "I have no use for hungry people and a rotting hare. Then bring whoever counts your stores to my cave. I want to hear what else you meant to take."
{n}Hessa ties the bundle of wire. Meret has stayed for the search and will leave after the meeting.{/n}
"I stayed for this," {n}she tells Soana.{/n} "My grandmother has no hand on my pack."
"I heard you the first time."
"Then the second should be easy."
{n}Soana studies the bundled snares. The corner of her mouth twitches; she presses it flat with a thumb.{/n}''', c('[Return after the careful search has established the whole line.]', flags=("soana.late_track_slow", "soana.late_trail_known"))),
], "soana.late_returned")

s("what_the_hollow_costs", "What the hollow costs", '"Hessa said she would bring someone to answer for the stores."', [
    n("start", "Soana", '''{n}Hessa brings a narrow sack and a woman with a bandaged palm. They wait outside the cave. Meret stands by the path, her pack fastened.{/n}
"Mava. I count our food. And the things people swear they cannot eat until their bellies growl."
{n}Hessa opens the sack. Hazelnuts and loose husks lie inside, with thin branches cut for smoking meat.{/n}
"We can give these back," {n}Mava says.{/n} "The hare has been eaten. I cannot pull that out of anyone's belly."
"How many sacks?" {n}Soana asks.{/n}
"Two. This is the rest of the second."
{n}Soana reaches toward the sack. Her fingers stop above the nuts.{/n}
"And those branches?"
"The hazel crowded the trail."
"Its own ground, and you cut it for being in your way."
{n}Mava looks at the fresh ends. Hessa shifts the sack so the branches no longer protrude toward Soana.{/n}''',
        c('[Hear Soana question them about the harvest.]', "stores"),
        c('"We must hear this through. Let us meet again when there is time."', abort=True)),
    n("stores", "Soana", '''"Three days of gathering," {n}Mava says.{/n} "We sell the good nuts for meal and keep the small ones. Hessa can smoke what she catches."
"Nothing from that hollow."
"There was no notice."
"A forest in a country the Abyss is eating, and you wanted a notice before you stripped it? Pff!"
{n}Hessa draws the sack shut. Mava watches the knot form.{/n}
"Our first store was taken on the road. The next village sells meal for money, not for what we swear we will earn later. Send us there with less if you mean to. But look in this sack first."
{n}Soana turns toward Meret. The hunter shakes her head.{/n}
"I cannot feed two camps. I can show them the road when mine leaves."
"I had not asked."
"I know that look."
{n}Soana's nostrils flare. She turns back to Mava.{/n}
"The deer cannot buy meal in your village. Nor can the hares you missed. You empty their hollow and walk away. The next hungry mouths find husks. I shall still be here to see what your sacks have cost."''', c('"What can the ground bear? Show us that much before we decide."', "ground")),
    n("ground", "Soana", '''{n}Together you walk to the hazel edge. Meret waits where she can watch the camp's approach and the path home. Mava opens the sack and looks from its contents to the nuts overhead.{/n}
{n}Soana points out stripped branches and heaps of husks. Farther south, rougher ground carries a heavier crop. Full sacks would be harder to carry from there, but the gatherers would stay clear of the deer hollow.{/n}
"Three visits, in daylight. No snares. No cutting. Empty sacks past me on the way in, full sacks past me on the way out. I shall spend three mornings counting what I would rather leave on the trees."
"Enough?" {n}you ask Mava.{/n}
"Less meal. Enough to bargain for some."
"And if they go now?"
"They leave this sack and take Meret's road. I keep the edge shut while the animals feed. And watch it. Words have never stopped a hungry hand reaching for a branch."
{n}Soana knocks her stick against a low root.{/n}
"I can put a fright into someone coming this way. No farther. The whole wood will not fit under my shawl, child."
"Tell them what fright."
"They shall hear. Before I put it in their path."''', c('[Hear the working and its limits.]', "thorn")),
    n("thorn", "Soana", '''"A turning thorn. Three cuts in dead wood, ash from that branch, and a name for this patch of ground. Cross the mark and you hear feet behind you. Press farther in, they follow closer. Turn back, they stop."
"Whose feet?" {n}Hessa asks.{/n}
"Nobody's. A sound I remember. Nothing lives inside it, and nothing bites. A stubborn fool can walk through. A frightened one may run and break an ankle on those roots. Look at them before you laugh."
{n}Hessa folds her arms.{/n}
"You mean to frighten us."
"I mean to keep something in this hollow when my back is turned. Your empty bellies have not made the deer's belly any fuller."
{n}Soana draws a line in the dirt.{/n}
"Only the approach I mark. Rain washes the ash away. A wet cloth across the cuts breaks it. No life tied to its life."
{n}She holds your gaze over the line.{/n}
"You have seen the other binding. There is no bear in these sticks."
"And with three days of gathering?"
"The thorn goes beyond the southern trees. They fill their sacks on this side. More ground left open, more nuts carried off. I shall count every one of those sacks."''',
        c('"Close the hollow. They have a road out. Leave its food for the animals."', "reserve"),
        c('"Give them three days at the southern trees. Mark the inner approach and let them sell a harvest."', "harvest")),
    n("reserve", "Soana", '''"Leave the sack," {n}Soana says.{/n} "Take the road Meret showed you. Keep the hare in your bellies. I have no spell for getting it back, nor any wish to see one."
{n}Mava looks at the nuts. Hessa asks for enough to eat on the morning's walk. Soana measures a portion into her empty hands and takes the rest.{/n}
"You know our names," {n}Mava says.{/n} "Use them when you tell yourself why we arrived hungry."
"I will remember. And I would remember an empty hollow."
{n}Mava ties the nearly empty sack. Meret tells her how far they can travel before dark. The women discuss which loads to lighten. Hessa will stay to see the marked approach before they go. Meret repeats the directions and leaves to join her own camp.{/n}
{n}Soana waits until they have moved away.{/n}
"That is the answer I wanted. Do not let Mava lay it all at your feet."
"You heard her."
"I have ears. I heard the dog, too, and saw what her hungry friend laid for the hares."
{n}She lifts her stick toward the inner path.{/n}
"Now the thorn. I will hear it myself before it goes after anyone else. Stay and hold the cloth. If it follows me out, wipe those cuts clean."''', c('[Agree to test the closed approach with her.]', flags=("soana.late_reserve", "soana.late_boundary_agreed"))),
    n("harvest", "Soana", '''{n}Soana stares at the southern hazel, then names three mornings. Each visit will end at midday, leaving light for her inspection. Mava repeats the days. Hessa adds, without prompting, that no snares will go in.{/n}
"This sack?" {n}Mava asks.{/n}
"Counts toward what you take. Do not bring me one sack and call the rest untouched."
{n}Mava nods. She and Hessa will gather and leave later than Meret's camp. The road will have fewer travelers with them. Meret describes the safer fork twice and makes Hessa point toward it before lifting her pack.{/n}
"Now I am going."
"Go," {n}Soana says.{/n} "Before I find another wire for you to pull out of the bushes."
{n}Meret hands Hessa the wrapped snares. The deer hollow lies beyond the gathering ground. Soana watches the hunters part, then strikes her stick against the earth.{/n}
"Three mornings. The trees will hear me curse every sack. We test the inner line before the first one goes in. I will not have somebody running through those roots because I put a fright where it could not be escaped."
{n}She looks toward the slope and measures the approach with her eyes.{/n}''', c('[Test the line before the gathering begins.]', flags=("soana.late_harvest", "soana.late_boundary_agreed"))),
], "soana.late_trail_known")

s("where_the_steps_end", "Where the steps end", '"I am ready to hear the thorn before anyone has to trust it."', [
    n("start", "Soana", '''{n}Three pieces of dead thorn lie beside a shallow dish of ash. Each carries a different notch. The bowl from the old shrine is absent.{/n}
"Buried," {n}Soana says, following your glance.{/n} "Leave it there. I have other wood to work with."
{n}She puts a wet cloth in your hand.{/n}
"Across all three cuts. That silences the thorn. If the feet follow anyone beyond the mark, wipe it out. At once. I shall curse the wasted ash afterwards."
"And if they stop inside?"
"We listen. See whether a stranger would turn back, and where a frightened one would put a foot."
{n}She takes up the thorn pieces. Her fingertips find each notch without looking. A little ash falls onto her skirt. She brushes it off impatiently.{/n}
"Keep that cloth wet. A dry rag is a poor weapon against this working, however splendidly you wave it."''',
        c('[Ask where to stand, remembering how the voice-working ended.]', "changed_role", requires=("soana.voice_interrupted",)),
        c('[Ask which part of the test to take.]', "role", forbids=("soana.voice_interrupted",)),
        c('"Not now. Leave the marks dark until I can watch them."', abort=True)),
    n("changed_role", "Soana", '''"At the approach. Cross when I have spoken, then come back the same way. If the sound follows you out, use the cloth."
"You said someone else would close the next bowl."
"And I meant it. Look at my hands. Thorn wood. No bowl, no mouth waiting to steal a voice."
{n}She turns the middle thorn between her fingers.{/n}
"I shall speak here. You shall walk there. You do not have to hold me through anything. If this wood misbehaves, drown the ash and we begin again with bare sticks."
"I remember the nursery."
"So do I, child. Every time I swallow. Do not imagine I have forgotten because I found another use for you."
{n}She sets the thorn against her palm and closes her hand around it.{/n}
"There is still a forest outside this cave. I cannot tend it by staring at one buried bowl until the roots grow over my feet."
{n}She points her stick toward the approach and leads you there, watching once to see that you carry the cloth.{/n}''', c('[Take the cloth to the approach.]', "placing")),
    n("role", "Soana", '''"Walk when I tell you. Listen, then turn back. Do not draw steel at empty bushes. I shall be beside the marker."
"Have you used this before?"
"A smaller sign round a store people would not leave alone. Frightened a thief. Frightened a visitor I was expecting, too. After that I showed people where to put their feet."
{n}She picks up the last thorn.{/n}
"Not on this slope. Sound runs strangely between banks. We shall find where it goes before Hessa brings her sacks through."
"You could have done the walking yourself."
"And listened from both sides at once? A fine new skill you credit me with. Perhaps I could grow a second pair of ears for your next visit."
{n}She taps your elbow as she passes, then points toward the ground to be marked. The wet cloth drips against your knuckles.{/n}
"You tell me what you hear. No praising my wisdom over the noise. I heard quite enough of that before Sarkoris fell."''', c('[Follow her to the marked approach.]', "placing")),
    n("placing", "Narrator", '''{n}Soana sets one thorn in a crack of dead wood beside the path, a second where earth meets roots, and a third facing the return route. She presses ash into the notches and speaks low to the ground.{/n}
{n}No voice answers. A leaf turns on its stem and stills. She moves beside the marker.{/n}
"Now. Watch your footing."
{n}You cross the first mark. A heavy step grinds grit behind you. Nobody has followed. Your shoulders tighten. The next step comes after your own, close enough to sound at your heel.{/n}
{n}You stop. The unseen walker takes one more step, then stops too.{/n}
"Back," {n}Soana says.{/n}
{n}You turn and retrace the approach. At the first thorn the footsteps cease. A pebble falls from the bank. You look back sharply. Soana points at the little stone where it rests.{/n}
"That one is real. Sit down if your knees are shaking. Then tell me where the other feet stopped."''',
        c('"Keep the sound this strong. The end is clear, and a warning must make someone stop."', "strong"),
        c('"Make it softer. Someone running from that could be hurt before they understand the way out."', "soft")),
    n("strong", "Soana", '''"Again," {n}Soana says.{/n} "With me walking. Hessa will know the mark. A stranger may not."
{n}You stand beside the marker. Soana crosses the first thorn. Her hand tightens on her stick when the steps sound behind her. She turns without hurrying and returns to the outer stone.{/n}
"I dislike being followed. Good. So will the next person with a sack."
{n}You walk the outer edge together. Beneath one bank a distant scrape reaches you though neither has crossed the mark. Soana moves the second thorn toward the first and speaks over its notch again. On the next circuit the outer ground remains silent.{/n}
"A smaller patch. It will have to do."
{n}Hessa and Mava come to see the marker. Mava stops at the first sound and looks carefully at the way back.{/n}
"Someone arriving late could miss that stick."
{n}Soana sets pale stones on either side of the first thorn. Hessa looks from them to the roots beyond.{/n}
"Tell your people," {n}Soana says.{/n} "The stones mean turn back. If they cannot remember two pale stones, keep them out of my wood."''', c('[Stay while she marks the beginning and checks where the sound ends.]', "strong_end")),
    n("soft", "Soana", '''{n}Soana looks past you at the roots and broken earth.{/n}
"A trespasser would find the one place to break a leg. Then I should have that to deal with as well."
{n}She rubs ash from the middle cut and repeats the working. When you cross, a tread rustles through dry leaves behind you. It turns your head but no longer grinds against your heels.{/n}
"Some will walk straight through that."
"Some would walk through the louder one."
"More will walk through this. Keep your eyes on those roots, child. I have heard your argument."
{n}You circle the outer ground. A faint scrape reaches beneath the bank. She moves the second thorn inward. On the next test no sound escapes the marked approach.{/n}
{n}Hessa and Mava come to see it. Hessa crosses one step and retreats at the tread.{/n}
"I would have looked for something in the bushes."
"Yes. Look, then go back past these stones. Show everyone you bring."
{n}Mava says she would rather hear a request to leave.{/n}
"You have heard one," {n}Soana replies.{/n} "Now you have heard this."
{n}She plants her stick beside the pale stones and waits while they study the way out.{/n}''', c('[Stay until the gentler warning has been tested from both sides.]', "soft_end")),
    n("strong_end", "Soana", '''{n}At the cave Soana takes the unused cloth and lays it over a pot rim. She sets the marked stick close to her knee before lowering herself onto the stone.{/n}
"I shall look after rain. Until then, that path can growl without me standing on it."
"And the rest of the forest?"
"Still there. Still larger than three sticks. Must we count every unguarded tree before I sit down?"
{n}She raises a finger as you open your mouth.{/n}
"Hessa saw the line. Mava saw the stones. The sound stays where I put it. One morning without a loose snare round someone's ankle. I call that a good morning."
{n}She taps the stone beside her with her palm.{/n}
"Sit. Tell me about the first step. Heavy boots, or bare feet? I heard it here. I want to know what followed you there."
{n}She leans forward to hear, the wet cloth slowly darkening the rim of the pot.{/n}''', c('[Keep the stronger warning and return to hear about the gatherers.]', flags=("soana.late_thorn_strong", "soana.late_thorn_tested"))),
    n("soft_end", "Soana", '''{n}Soana drapes the unused cloth over a pot rim and puts the marked stick beside her. She sits and rubs the back of one knee.{/n}
"More walking for me. A soft tread will not turn every fool away. I shall have to look more often."
"Will you regret it?"
"Ask after the third walk in rain. I shall have a splendid answer by then."
{n}She taps the place beside her.{/n}
"Sit before I find a use for you that involves carrying something. Tell me what changed at the second crossing."
"Leaves underfoot. The sound did not seem so close."
"And you could turn without stumbling?"
{n}You describe the tread, the roots you could see and the first mark where the sound ended. She traces that point in spilled ash with one finger.{/n}
"There, then. I will look at those roots again before Hessa arrives. She has enough trouble with the dog's foot. I do not want hers added to it."''', c('[Keep the gentler warning and return to hear about the gatherers.]', flags=("soana.late_thorn_soft", "soana.late_thorn_tested"))),
], "soana.late_boundary_agreed", delay=0)

s("the_days_she_counted", "The days she counted", '"How did Hessa and Mava keep the bargain?"', [
    n("start", "Soana", '''{n}Soana sits outside the cave with a marked thorn across her knees. Rain has washed one notch clean. She turns the pale cut toward you.{/n}
"Rain. No respect for a shaman's labor. I went to look afterwards. Not a footstep left in the approach."
"Will you renew it?"
"When I want that ground kept. I will not feed ash to a useless stick because I carved it myself."
{n}She sets it beside her walking stick and knocks dust off the stone beside her.{/n}
"Sit. Hessa and Mava did not vanish when we finished quarrelling. You shall hear what they took and what they left."
{n}A trace of ash remains on her knee. She brushes at it, misses and turns to you instead.{/n}''',
        c('[Ask about the families who left without the harvest.]', "reserve", requires=("soana.late_reserve",)),
        c('[Ask about the three days of gathering.]', "harvest", requires=("soana.late_harvest",)),
        c('"I want to hear it when I can stay."', abort=True)),
    n("reserve", "Soana", '''"The nuts stayed. Hessa carried the wire wound so tight nothing could put a foot through it. Mava asked which village sold meal. I told her, and gave her the road."
{n}Soana looks toward the upper bend.{/n}
"Tarn walked until his foot hurt. Hessa made a sling out of an empty sack. Last I saw, she was trying to persuade him to lie in it while he tried to climb out."
"Anything else?"
"Mava said I would find the hollow quiet. I did."
{n}She turns a pebble with the end of her stick.{/n}
"I put the nuts in heaps under the hazel, clear of the path. Some were gone next morning. I did not sit all night counting mouths. Something ate where there was food left to eat."
"Worth sending them away with less?"
"Yes. Mava may curse me over her thin supper. I shall not pretend she walked out of a full larder. Nor shall I empty this hollow to stop her cursing."
{n}Her stick leaves a furrow beside the pebble.{/n}
"You came to a forest shaman, child. The animals have no stores keeper to stand here speaking for them."''', c('[Stay to hear the rest of her account.]', "meret")),
    n("harvest", "Soana", '''"Three mornings. Six sacks. Seven complaints about the climb. One branch cut before they arrived, which Hessa was delighted to rub under my nose."
"Did you say you were wrong?"
"Two words. She tried to get a third."
{n}One corner of her mouth lifts.{/n}
"They stayed on the southern ground. Mava wanted another hour at the end. No. Nuts still overhead, sacks still open, and she could see the meal hanging on the branches. She told me how much the last sack would buy."
"And stopped?"
"After I asked how many last sacks followed the first. She tied them."
{n}Soana brushes ash from her sleeve.{/n}
"Fewer tracks there next morning. Six sacks do not walk quietly. I cannot tell you which beasts will come back first. The inner hollow was untouched, and the camp is empty."
"The warning?"
"Left alone. Hessa carried off the wire. Tarn walked part of the road and rode in a sack for the rest. Perhaps he will smell a trap next time and keep his foot out."
{n}She taps the clean notch of the thorn.{/n}
"Three mornings, child. They got three mornings. When the next crop ripens, Mava will have to speak to me again."''', c('[Ask about Meret after the camp departed.]', "meret")),
    n("meret", "Soana", '''"Meret went with her people before Hessa was ready. I pointed out another patch she might inspect on the road. She asked if I was showing her the way or trying to keep her here."
"Which?"
"Both. She took the directions and went. Impudent girl."
{n}Soana folds her hands over one knee.{/n}
"Her grandmother's mark still hangs at her belt. She brought me a useful report. I would have liked another pair of eyes in the eastern wood, and she would have liked her pack on the road. You saw which of us got our wish."
"Will you ask her again?"
"If she comes. Until then, someone else will have to look. A forest does not grow smaller because one hunter has left it."
{n}She watches you reach toward your belongings.{/n}
"Sit."
"Another task?"
"Must I find a broken handle whenever I want you on that stone? Sit, child. The handle can wait."
{n}She shifts closer and knocks a burr from your sleeve. It clings to her finger. She curses and flicks it into the dust.{/n}''', c('[Ask what to record before you leave again.]', "guardian")),
    n("guardian", "Soana", '''"Write down the thorn. Where the steps began, where they stopped, what Hessa took. No fine title. Anyone reading it should find the right path, not come here expecting Soana the Seer to have an answer for every root in the wood."
{n}Her hand rises to the hollow at her throat, then drops onto her knee.{/n}
"And put this in plainly. The clay medallion was another working. So was the brand on Orso. No fool is to read your account and think a damp rag across three sticks could undo that knot."
{n}She points toward the thorn beside her stick.{/n}
"Wood and ash here. A life there. Write it large if you must."''',
        c('"The thorn did not release Orso. The binding and its cost remain."', "bound", requires=("soana.old_defender",), forbids=("soana.bear_dead", "soana.medallion_pulverized")),
        c('"The thorn did not bring Orso back, or supply a replacement guardian."', "dead", requires=("soana.bear_dead",)),
        # Polish (Sol CAN): the medallion bitten to dust (SoanaBear/Cue_0023) withers Orso with no BearDead etude.
        c('"The thorn did not bring Orso back, or supply a replacement guardian."', "dead", requires=("soana.medallion_pulverized",), forbids=("soana.bear_dead",))),
    n("bound", "Soana", '''"Yes. You still hate the binding. I still fear what comes into the wood if I break it. You can warm your hands at my fire without settling that quarrel."
{n}Her jaw tightens. She keeps her knee beside yours.{/n}
"I can silence this thorn with water. Nothing dies. I shall find what else can be done that way. But three sticks have not grown into a guardian because you and I sat looking at them."
"Nor have I stopped objecting because we share a fire."
"I heard you the first time, stubborn creature. I have not stuffed wool in my ears."
{n}She takes folded bark from beside the water pot. An old beginning has been rubbed away, leaving a dark smear.{/n}
"Another account. No traps or sacks in this one."
{n}She opens the fold with her thumbnail, looks at the writing and turns it toward herself again.{/n}
"Corven. I finished what I began."''', c('[Let her show you what became of the letter to Corven.]', "letter")),
    n("dead", "Soana", '''"No guardian. No bear coming back out of the trees. I know what is missing."
{n}She listens toward the path, her head turned as though something heavy might still move there.{/n}
"And I have found no other creature to put in his place. You saw three sticks, ash and a cloth. That is what I have made. Let nobody carry a grander tale away from my cave."
"The forest is still in danger."
"Has it ever ceased? Sit down. I am not sending you after another beast tonight."
{n}She takes folded bark from beside the water pot. The smear of an earlier beginning remains on the outer face. Her fingers flatten its curled edge.{/n}
"I finished this. Corven will have a fine long answer to give me, if he ever comes to read it."
{n}She glances at the writing once, then holds it against her knee.{/n}''', c('[Hear what she wrote to Corven.]', "letter")),
    n("letter", "Soana", '''"The spring as it stands. The work. Where I planted, where the ground stayed bare. Your name. I began a sentence telling him he had married a difficult woman, then scratched it out. He knew that before he brought the flowers."
{n}She turns the bark over, keeping its writing toward her palm.{/n}
"No address. No grave I know of. Nobody has come through the trees with news. It stays here until there is someone to carry it to him. My own words. I will not have a kindly fool smoothing them into something he would never recognize."
"What did you say about me?"
"That you came back. I wanted you back. If he objects, he can come and tell me himself."
{n}She presses the folded bark beneath its weight beside the pot. Her hand rests there until the edge lies flat.{/n}
"There. Enough talking to someone who is not here. You are."
{n}She turns toward you and draws her stick away from the stone between your feet.{/n}''',
        c('"And I want to keep coming home to you."', "future", requires=("soana.later_courting",)),
        c('"Your friend is here. What shall we do with our next visit?"', "friend", requires=("soana.later_friends",))),
    n("future", "Soana", '''"Then come home with something besides a sick beast or another question for the witch. Come with your own boots, your own appetite. Tell me when to look for you. I dislike discovering your plans from a traveler who knows less than the birds."
{n}She looks into the cave.{/n}
"I stay here. This wood has held my life through blood and fire. There is a dry place for your things beside the blanket. You can see it without a scribe naming it for you."
"And time for me?"
"Do you think the trees will fall down if I leave them an afternoon? They have tried before. They can wait."
{n}Her eyes travel from your shoulders to your mouth.{/n}
"I have uses for an afternoon. And for you, stripped of all that clattering iron."
{n}She catches your sleeve and draws you nearer.{/n}
"Corven gave me flowers, and I was his wife. Writing his name on bark has told me nothing of where he is now. You know that. I will not invent a grave to make you a welcome."
"I am here, Soana."
"Then say whether you mean to stay."''',
        c('"I want a life with you. Keep that place beside your blanket for me."', "commit"),
        c('"I want you, and I will come again. I cannot promise a life here yet."', "open"),
        c('"I cannot go on as your lover. I want to remain your friend."', "part_as_friends")),
    n("commit", "Soana", '''{n}She takes your hand and presses it to her cheek. Her eyelids lower. When she looks up, she scowls at the smile on your face.{/n}
"Do not grin like that. I heard you."
"You could stop talking now."
"In my own cave? Bold already."
{n}She kisses your palm and keeps it against her cheek. Her thumb rubs over a callus on your wrist.{/n}
"Beloved, then. When you have not done something foolish. Your name will serve when I want to scold you. I have no wedding wreath to hang on that great head of yours."
{n}You put a few belongings beside her blanket and settle on a longer visit when the fighting allows. She moves your bundle twice before deciding where it should lie.{/n}
"Before the final fighting, come here. No broken handles. No bear to chase. An evening. I want you beside me, with nothing in your hands that I must mend."
{n}She pushes the bundle against the wall with her heel, then takes your hand again.{/n}''', c('[Keep your place beside her and return before the final fighting.]', flags=("soana.committed", "soana.late_future_chosen"))),
    n("open", "Soana", '''{n}Soana draws breath through her nose. Her fingers remain beside yours on the stone.{/n}
"Not staying, then. I had begun to picture your boots there."
"I will come back."
"Then come. I shall see whether I am still inclined to let those boots muddy my floor. Do not look so solemn. I said I wanted you. I have not spat you out because you failed to bring a household in your pack."
{n}One rough finger strokes your knuckles.{/n}
"Before the final fighting. I still want that evening. Leave your fine promises on the road if they do not fit in your mouth. Bring your mouth."
"I can do that."
"At last, something simple from a Commander."
{n}She hooks her fingers through yours and pulls until your knees touch. Her gaze stays on your face.{/n}
"And do not keep me waiting while you look for a gift. I have enough roots and foolish trinkets. Come yourself."''', c('[Return to her as a lover, without promising a household.]', flags=("soana.late_open", "soana.late_future_chosen"))),
    n("part_as_friends", "Soana", '''{n}Her fingers close against her palm. She looks toward the path. A small muscle jumps beside her mouth.{/n}
"Friend. That was not what you called me with your mouth on mine."
"I meant it then."
"See that you remember it. I will not have those evenings turned into two fools exchanging courtesies."
{n}She drags the end of her stick through the dust, then lifts it onto her knee.{/n}
"You may come as my friend. Leave the pity at the bend. And do not rush to carry every pot because you think I have gone frail from hearing you."
"I would not."
"You might. People grow remarkably foolish when they are trying to be kind."
{n}She looks at you again.{/n}
"Come before the fighting. We can sit. I may curse you once or twice. You have heard worse, and deserved some of it."
{n}She shifts the stick off the place beside her.{/n}''', c('[Remain her friend, remembering the courtship.]', flags=("soana.late_friends", "soana.late_romance_ended", "soana.late_future_chosen"))),
    n("friend", "Soana", '''"A visit with no bleeding beast waiting behind you. Those always seem to come last."
{n}She takes the worn proposal from under its weight. Corrections crowd both sides. She holds it toward the light, frowns and turns it over.{/n}
"Come before the fighting with a foolish tale. I have spent enough evenings telling you where you went wrong. You can tell me where somebody else went wrong for once."
"And you will leave the lesson out?"
"Do not ask for miracles."
{n}She hands you the proposal, watches you read a correction and takes it back before you can fold it away.{/n}
"Mine. I kept it through all your clever suggestions, and I mean to keep it through the next ones."
{n}She slides it under the weight.{/n}
"I remember that goat in the song, too. The wretched creature has followed me through several mornings when I wanted to think about something useful. You can answer for that when you return."
{n}You settle on another evening. Soana puts her stick on the far side and stays beside you until the light has moved off the cave wall.{/n}''', c('[Keep the friendship and the promised evening.]', flags=("soana.late_friends", "soana.late_future_chosen"))),
], "soana.late_thorn_tested", delay=72)

s("before_the_far_road", "Before the far road", '"I came for the evening, before I have to leave."', [
    n("start", "Soana", '''{n}No experiment waits at the cave mouth. The water pot stands in its cradle; tools have been put away. A clean cloth covers your usual seat. Soana's stick rests within her reach instead of across the entrance.{/n}
"I thought of the bend. Then I remembered the damp stone. Let the owls sit on it. We have dry shelter."
{n}She fastens her shawl crookedly, notices and jerks the clasp straight.{/n}
"How long?"
"The evening."
"Then come in. Let any speech you brought go hungry while we eat."
{n}She lifts the cloth from your seat and shakes it once. The tools remain covered. She sets the pot between the two places and looks impatiently at your boots.{/n}
"There is no mire to inspect tonight. You can put those down."''',
        c('[Sit beside your beloved.]', "beloved", requires=("soana.committed",)),
        c('[Sit beside the woman you are courting.]', "courtship", requires=("soana.late_open",)),
        c('[Spend the evening with your friend.]', "friend", requires=("soana.late_friends",)),
        c('"I cannot stay tonight. I will return for the evening."', abort=True)),
    n("beloved", "Soana", '''{n}Soana leans against you as you settle. Her hand finds yours beneath the shawl. She turns it over and runs a thumb along your palm.{/n}
"A fine collection of scars. Do not go adding a last one to make a prettier tale for the fools who praise you."
"What would you have me do?"
"Come back. Stay for that long visit. Leave your things in the wrong place so I can scold you. I may even move them there myself."
{n}She lifts her head and looks at you.{/n}
"You will be wanted here. Remember that when someone starts singing of a glorious death."
"I want to come back."
"Then do it."
{n}Her fingers tighten around yours. She pushes the shawl off your joined hands.{/n}
"Tonight you are here. I have wasted enough daylight thinking about the next road. Turn this way. I have no wish to spend the evening staring at the side of your head."''', c('[Turn toward her.]', "desire")),
    n("courtship", "Soana", '''"You came. And without a cartload of promises."
"Were you expecting one?"
"People become generous with words before a dangerous road. I had a scolding ready for every wheel."
"Save them."
"They will keep. Yours may not have."
{n}Her shoulder presses yours. She takes your hand and traces the edge of your thumb, then lifts it beneath her shawl.{/n}
"I want you. I have had enough of the cave wall for company. It never argues, and I have yet to find a pleasant use for kissing it."
"I should hope to do better."
"Then stop boasting."
{n}She glances at your mouth. One foot catches the edge of the blanket and draws it nearer.{/n}
"Tomorrow you can look down that road. Tonight look at me. You have spent quite enough of our visits looking at sticks and bowls."
{n}She tilts her face toward yours, the clasp of her shawl gleaming between you.{/n}''', c('[Turn toward her.]', "desire")),
    n("desire", "Soana", '''{n}Soana cups your cheek. Her thumb is rough with work. You lean toward her, and she draws you the rest of the way into a kiss. Her fingers slip behind your neck.{/n}
"There. I was beginning to wonder if the fighting had shaken that out of you too."
{n}A strand of gray hair catches at her lip. You brush it aside. She turns and kisses your wrist, then pulls your hand against the warm skin below her throat.{/n}
"I want your mouth on me. I want you in that blanket until the birds make such a racket we cannot pretend it is still night."
"No scolding?"
"I have other uses for my tongue. Do not tempt me to waste it."
{n}She laughs low against your cheek. The shawl slips from one shoulder. She opens its crooked clasp and lets the wool fall into her lap.{/n}
"How much of you is the road taking tonight?"
{n}Her palm lies warm against your chest, fingers working beneath the edge of your collar.{/n}''',
        c('"None. Keep me here all night."', "night"),
        c('"Your kisses, and the evening. I must leave before the night is over."', "kiss"),
        c('"Hold me tonight. Just that."', "hold")),
    n("night", "Narrator", '''{n}Soana pulls you close. Your kiss drives her shawl beneath your knee; she laughs into your mouth when the wool catches, then tugs it free and throws it over the tools.{/n}
"Let them wait. I have waited longer."
{n}Her hands find your buckles. She works one loose, curses the next and pushes your shirt off your shoulders. You open her clothing at the throat. She draws it down her arms, baring warm skin, and presses herself against your chest.{/n}
"Too much iron between us. There. Better."
{n}She bites lightly at the join of your neck. Your hands close around her waist. She pulls you down onto the blanket, her gray braid loosening across your chest, and plants her knees on either side of your hips. She holds your mouth to hers while your hands draw her closer, bare skin hot against yours.{/n}
{n}In the morning a branch scrapes the rock outside. Soana lifts her head from your shoulder and listens. Then she puts a hand over your chest and lies down again.{/n}
"A branch. Do not leap up and make it an errand."
{n}You kiss the gray hair at her temple. She turns her mouth to yours.{/n}
"And do not tread on my braid. You have been careless with it already."
{n}She keeps you beneath the blanket until light has crossed the water pot.{/n}''', c('[Rise together when it is time to leave.]', "leave_night")),
    n("leave_night", "Soana", '''{n}At the entrance she catches your hand. Her grip hardens as you turn toward the path.{/n}
"Go carefully. Spare me the song about how little a life weighs against a victory. I have heard enough songs."
"I will."
"Keep your head down when something sharp comes at it. Eat. And come back with those feet still under you."
{n}She straightens your collar with a sharp tug, then lets your hand go. Before you reach the bend she calls after you.{/n}
"Your things are beside the blanket. I am not carrying them down the road to find you!"''', c('[Take leave after the night together.]', flags=("soana.lovers", "soana.late_farewell_night", "soana.late_campaign_kept"))),
    n("kiss", "Narrator", '''{n}Soana draws you into her lap as far as the stone allows, then pulls your head down to kiss you. Her palm presses the back of your neck; your hand rests beneath the fallen edge of her shawl. She laughs at the cold of your fingers and warms them against her skin.{/n}
"You should have come sooner."
{n}Afterwards she leans against you and begins the goat song. You join where you remember the verse. She changes the words and stops to look up at you.{/n}
"That goat has been busy since you left. Keep up."
{n}She sings the new ending into your shoulder. You laugh against her hair, and she starts the verse again, louder. The cave gives the foolish words back in a faint echo.{/n}
{n}At the hour you named she rises. At the entrance she catches your collar and draws you down for another kiss. You brace a hand against the rock; her fingers stay on your throat when your mouths part.{/n}
"Go carefully. I want to hear you spoil that verse again."
{n}She tugs the collar straight and watches you take the first steps onto the path.{/n}''', c('[Leave before the night is over, carrying her last kiss.]', flags=("soana.late_farewell_kiss", "soana.late_campaign_kept"))),
    n("hold", "Narrator", '''{n}Soana draws the blanket over your knees and pulls your head against her shoulder. You shift until the stone no longer digs into your hip. Her hand settles at the back of your neck.{/n}
{n}A bird rustles outside. Leaves brush the rock. Water sounds down the slope. You begin to speak of the coming road, then break off.{/n}
"Which turn?" {n}she asks.{/n}
{n}You try again, naming the part you have been picturing. Her fingers move once through your hair. When your account runs out, she pulls the blanket higher instead of reaching for her stick.{/n}
"Tomorrow has a road of its own. It can wait outside tonight."
{n}You lie against her while the cave mouth darkens. Once she mutters at a root pressing through the blanket and shifts you both away from it. Her arm stays around your shoulders.{/n}
{n}At the entrance she draws your head down until your foreheads touch. She speaks your name, then straightens the cloth at your neck before turning you toward the path.{/n}
"Watch your feet, child."''', c('[Leave after resting in her arms.]', flags=("soana.late_farewell_held", "soana.late_campaign_kept"))),
    n("friend", "Soana", '''{n}Soana passes you the wooden clapper from the warning experiment. Its edges have been worn smooth by hands.{/n}
"Good wood. I keep looking at it and finding another use."
"It might be finished."
"Then it can lie there and be idle. I did not bring you here to carve it."
{n}She sets it beside the pot. You tell your foolish road tale: two people defending the same direction while pointing different ways. Soana asks who admitted the mistake. You describe the bargain that let each depart still claiming to be right.{/n}
"They should have asked the road. It was there throughout."
{n}She tells you of a cloak misplaced during the festival and a man who found it on the person he had spent the evening trying to impress. At the man's outraged words she pitches her voice so high you nearly spill your drink.{/n}
"He was a better dancer than a singer. The mead made him forget which he was doing."
{n}When you leave, she grips your arm at the entrance.{/n}
"Come back. Bring another fool's tale. And yourself, before you bring me a beast with a thorn in its foot."
{n}She squeezes once, releases you and knocks the clapper farther from the edge of the stone.{/n}''', c('[Take leave of the friend who asked for your company.]', flags=("soana.late_farewell_friend", "soana.late_campaign_kept"))),
], "soana.late_future_chosen", delay=24)


def ending(id, title, text, requires=(), forbids=(), any_flags=(), owner="Epilogue"):
    SCENES.append(scene("soana.ending_" + id, title, owner, 0, "", [
        n("start", "Narrator", text, portrait="Soana")],
        Relationship="soana", last=99, requires=requires, forbids=forbids,
        RequiresAny=list(any_flags)))


ORDINARY = (*LOSS, "soana.closed", "inhuman", "ascended", "sacrifice")
ending("kept_life", "A life with an open path", '''{n}The Commander returned with time to stay. Boots and a travel bundle took their place beside Soana's blanket. She moved them out of the damp, then scolded their owner for putting them where she had left them. On some afternoons the tools lay untouched while two cups stood empty beside the water pot.{/n}
{n}Messages came up the path when fighting delayed a visit. Soana read them twice and cursed the weather, the roads or the messenger's slowness. When the Commander arrived, there was smoked fish by the fire and a dry blanket laid out. She complained about the appetite that would devour both her stores and her evening.{/n}
{n}The bark addressed to Corven stayed under its weight. No news came with it. Sometimes a flower lay beside the writing until its petals dried. Soana called the Commander beloved when she was pleased and something much sharper when boots tracked mud into the cave.{/n}
{n}After rain she inspected the thorn. When the hollow wanted guarding she rubbed fresh ash into its cuts; otherwise it lay pale and silent. Visitors watched for the stones. From the cave, on a good evening, her laughter carried farther than the warning ever had.{/n}''',
    requires=("soana.late_campaign_kept", "soana.committed"), forbids=ORDINARY)
ending("chosen_visits", "The next invitation", '''{n}The Commander's belongings still traveled in a pack. Visits came when the roads and the fighting allowed. Soana demanded dates, cursed missed ones and looked down the path when an arrival was due. A delayed message might earn its bearer a scolding intended for someone else.{/n}
{n}No household gathered beside the blanket. There were evenings with two cups, however, and nights when the shawl landed on top of the tools. At parting Soana sometimes caught the Commander's collar and pulled it down for another kiss. Sometimes she only demanded a longer stay next time.{/n}
{n}The forest claimed most mornings. She inspected shoots and renewed ash, quarrelled with hunters and remembered which branches had been cut. But a familiar step at the cave mouth could leave the roots half sorted on their stone. "They will keep," she would say, already reaching for the visitor's hand.{/n}''',
    requires=("soana.late_campaign_kept", "soana.late_open"), forbids=(*ORDINARY, "soana.committed"))
ending("familiar_company", "Company without a debt", '''{n}The Commander kept visiting as Soana's friend. A second cup stood by the water pot. There were disputes over a working, a path and the proper words of a goat song. Soana could spend more breath correcting a verse than explaining a rite, particularly when the wrong verse made her laugh.{/n}
{n}Meret carried her grandmother's mark away with her own camp. When she returned through the eastern woods, Soana asked what she had seen and grumbled over what she had missed. Other hunters brought reports too. They learned to point out their tracks before the shaman pointed out their foolishness.{/n}
{n}The worn proposal remained beneath its weight, both sides crowded with corrections. In the last bare corner Soana wrote the date of an evening spent singing. When the Commander next reached for the page, she took it back at once. "Mine," she said, and put it where the rain could not reach.{/n}''',
    requires=("soana.late_campaign_kept", "soana.late_friends"), forbids=(*ORDINARY, "soana.committed", "soana.late_open"))
ending("sacrifice", "The visit that did not follow", '''{n}The news from the Worldwound reached Soana's cave with praise for the Commander who had closed it. She heard the account to its end. When the messenger began the praise again, she sent him down the path with words he did not repeat in his next telling.{/n}
{n}The clean cloth from the last evening lay folded beside the blanket. Soana put it away, took it out once more and shook it free of dust. No boots sounded at the bend. Sometimes she set down a second cup before snatching it back onto the shelf.{/n}
{n}Hard rain washed the thorn quiet. She went out with her stick, checked the pale stones and lifted a branch from the seedlings. At the cave she caught herself turning to complain about the mud. The place beside her was empty. She struck the mud from her boots harder than it deserved.{/n}''',
    requires=("soana.late_campaign_kept", "sacrifice"), forbids=(*LOSS, "soana.closed", "inhuman", "ascended"))
ending("beyond_the_forest", "An invitation without a summons", '''{n}When word came of the Commander's ascent, Soana listened with her stick across her knees. "A god," she said. "Does a god still know the way to a cave?" She gave the messenger an invitation and exact directions, as though divinity were another traveler likely to miss the bend.{/n}
{n}No charm bore the Commander's name. No offering of forest life followed the message. She kept the thorn for the hollow and the written invitation for the road. If the messenger returned without an answer, she questioned him about every turning he had taken.{/n}
{n}The blanket stayed dry. Sometimes Soana began to recount her day's work aloud, then stopped and looked at the entrance. She had heard no returning footstep. "You could send word," she told the empty path, before picking up the root she had been peeling.{/n}''',
    requires=("soana.late_campaign_kept", "ascended"), forbids=(*LOSS, "soana.closed", "inhuman"))
ending("unrecognizable_return", "The unwelcome return", '''{n}Soana heard what the Commander had become. She moved the travel bundle from beside her blanket and set it outside the cave. When a visitor tried to soften the news with tales of the old evenings, she drove the end of her stick into the ground.{/n}
{n}"I know who sat here. Do not teach me my own memories. And do not bring that thing to my door." The water pot stayed in its cradle, the worn proposal beneath its weight. She took up the thorn and went to inspect the approach. That night she sat facing the entrance, her stick across her knees.{/n}''',
    requires=("soana.late_campaign_kept", "inhuman"), forbids=(*LOSS, "soana.closed"))
SCENES.append(scene("soana.ending_native_loss", "The path that could not be kept", "Epilogue", 0, "", [
    n("start", "Narrator", '''{n}News from Wintersun followed the Commander's last visit. At the cave the water pot still stood in its cradle. The path ran past the stone where Soana had sorted roots, toward ground no familiar scolding could keep as it had been.{/n}''',
        c("[Remember Soana's death at Camellia's hand.]", "camellia", requires=("soana.killed_by_camellia",)),
        c('[Remember the woman who died.]', "dead", requires=("soana.dead",), forbids=("soana.killed_by_camellia",)),
        c('[Remember the forest that was lost.]', "forest", requires=("soana.forest_dead",), forbids=("soana.dead", "soana.killed_by_camellia",)), portrait="Soana"),
    n("camellia", "Narrator", '''{n}Camellia killed Soana. The cave kept a stick worn smooth at the grip and a blanket folded beside the wall. No sharp greeting came when the Commander reached the entrance. Dust had gathered where the shaman's heel used to strike the stone.{/n}
{n}The last evening returned in scraps: a cup, a foolish verse, her fingers catching a sleeve. Camellia's blade had left those objects where they were. The Commander could still find the turn in the path without looking. There was no voice at its end.{/n}''', portrait="Soana"),
    n("dead", "Narrator", '''{n}After Soana's death the repaired carrier stood by the water pot. Her stick leaned against the wall, smooth where her fingers had gripped it. Corrections crowded the worn proposal. Someone picking it up might still hear the scorn with which she had struck out a foolish line.{/n}
{n}The place beside the blanket remained clear. No hand came to knock dust off the stone. Outside, a root rolled from the sorting ledge and fell. Nobody caught it before it reached the ground.{/n}''', portrait="Soana"),
    n("forest", "Narrator", '''{n}The forest was lost. The hazel crop, the deer hollow and the young trees could no longer feed what had sheltered there. Rain washed the ash from the thorn. Pale stones marked an approach to ground that no longer carried the old scent of leaves.{/n}
{n}At the cave the water pot stood in its cradle. The Commander remembered Soana pointing her stick toward the wood, scolding a hunter for looking at a single beast while the whole forest stood behind it. Beyond the upper bend, that forest no longer answered.{/n}''', portrait="Soana"),
], Relationship="soana", last=99, requires=("soana.late_campaign_kept",), RequiresAny=list(LOSS)))
ending("aeon", "A path outside the remembered world", '''{n}In the history without the Worldwound, the road that had brought the Commander to Soana's cave left no such trail. No trapped fox led to the repaired water carrier. No stolen voice drew three people to the sealed bowl. The last evening had no date in that world's reckoning.{/n}
{n}No account from that history reached the vanished traveler. There was no letter telling where Soana lived, no word of Corven, no familiar scolding from a cave mouth. The forest stood outside the memory of those visits. No bootprint from the old road remained to show where the Commander had once turned toward it.{/n}''',
    requires=("soana.progression_kept",), owner="AeonEpilogue")

# Preserve completed late endings; these acknowledge a history interrupted earlier.
ending("unfinished_sacrifice", "The conversation left unfinished", '''{n}Soana had saved a question for the Commander's next visit. When news of the sacrifice came, she asked the messenger where he had heard it and made him repeat the answer. Then she told him to go. His fine account of the victory ended at the bend, drowned by her voice.{/n}
{n}The worn proposal stayed under its weight. A dry blanket lay beside the water pot. Once she fetched the page as if to point out another error, found no one on the stone and pressed it flat again with her palm. The question she had saved was never put to the messenger.{/n}
{n}Some mornings she began the foolish festival song while sorting roots and broke off before the goat appeared. On others she sang to the end. Once the last verse made her laugh. She looked toward the empty seat, then threw a rotten root down the slope.{/n}''',
    requires=("soana.progression_kept", "sacrifice"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept", "inhuman", "ascended"))
ending("unfinished_ascent", "A question beyond its former reach", '''{n}Word of the Commander's ascent arrived before the next visit. Soana asked whether anyone had seen the new god walking a road. The messenger had no answer. "Then take a message," she snapped. "God or no god, there is a conversation waiting here."{/n}
{n}She named the cave, the upper bend and the turn beside the loose stone. No revelation answered her. The shrine remained closed. The worn proposal still lay under its weight, bearing corrections the Commander had yet to hear.{/n}
{n}She put no divine name into a charm. When the day's work was done, she sat by the entrance and called the old name toward the path. On evenings when no answer came, she cursed the poor manners of distant powers and went inside before the blanket grew damp.{/n}''',
    requires=("soana.progression_kept", "ascended"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept", "inhuman"))
ending("unfinished_change", "An invitation withdrawn", '''{n}When Soana learned what the Commander had become, she put her stick across the entrance. The next visitor found her sorting roots behind it. "The one I knew could sit and argue," she said. "This thing stays outside. Carry that back exactly. I shall hear if you sweeten it."{/n}
{n}She kept the worn proposal and the repaired carrier. The closed shrine remained closed. Sometimes an old correction on the page made her snort; sometimes she folded it away before reaching that line. No messenger was sent to bring its former reader home.{/n}
{n}At the upper bend she scraped mud from the pale stones. She listened to the woods, then looked down the empty approach. Her hand tightened around the stick. She stayed there until the failing light drove her back to the cave.{/n}''',
    requires=("soana.progression_kept", "inhuman"),
    forbids=(*LOSS, "soana.closed", "soana.late_campaign_kept"))

# These loss pages concern only earlier shared objects, never an unplayed late rite.
unfinished_loss = deepcopy(next(s for s in SCENES if s["Id"] == "soana.ending_native_loss"))
unfinished_loss["Id"] = "soana.ending_unfinished_loss"
unfinished_loss["Title"] = "The earlier path that ended"
unfinished_loss["Requires"] = ["soana.progression_kept"]
unfinished_loss["Forbids"] = ["soana.late_campaign_kept"]
unfinished_loss["Nodes"][0]["Text"] = '''{n}News from Wintersun came before the next evening at Soana's cave. The repaired carrier remained beside the water pot, the worn proposal beneath its weight. There were still corrections the Commander had not heard, and a clean place on the stone where another visit had been expected.{/n}'''
unfinished_loss["Nodes"][-1]["Text"] = '''{n}The forest was lost before the visits reached their farewell. The warning line could keep one approach; the sealed shrine had held one danger. Beyond them the hazel and the hollow failed. Young trees no longer lifted leaves over the bare soil.{/n}
{n}The Commander remembered a carrier set down by the water pot, Soana's stick rapping the ground and the sharp voice that had called a visitor back to sit. The road still reached the cave. Beyond its upper bend lay no harvest to quarrel over.{/n}'''
SCENES.append(unfinished_loss)
