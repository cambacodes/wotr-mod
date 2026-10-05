"""Seelah continuation draft; restoration and transformed contact access are separate work."""
from story_format import c, n, p, scene
from storylines.seelah_progression import future_gate_nodes, farewell_gate_nodes

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, chapter, entry, nodes, **conditions):
    for node in nodes:
        if not node["Portrait"]:
            node["Portrait"] = "Seelah"
    SCENES.append(scene("seelah." + id, title, "Seelah", chapter, entry, nodes,
                        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
                        Areas=[DREZEN], Chapters=[ch for ch in (3, 5) if ch >= chapter], **conditions))


s("changed_opening", "An unfamiliar way to begin", 5, '"Will you spend an evening with me?"', [
    n("start", "Seelah", '''{n}Seelah hears you out, her feet planted where they are.{/n}
"I said I'd talk to you. Don't go mistaking that for a clean bill of health."
{n}Her fingers curl, then straighten.{/n}
"Yes, I still care about you. And yes, your power still scares me. Liking you hasn't made me blind."''',
      c('"Do you want me as more than a friend?"', "ask"),
      c('"Then let us keep this as friendship."', "friend")),
    n("ask", "Seelah", '''"I might. There. Said it. Still haven't made it any easier."
{n}She scowls at the ground, then looks up at you.{/n}
"Usually I'd bring something to eat, sit too close, and make a fool of myself until somebody laughed. With you... would the food even help?"
{n}She scratches her cheek.{/n}
"What would we do with an evening? You and me?"''',
      c('"We can talk. I want to hear how your day went. You can hear about mine."', "time"),
      c('"This body is what I have now. Let us find something we can enjoy together."', "time")),
    n("time", "Seelah", '''"All right. One evening. If we like it, we can have another."
{n}A little warmth returns to her face.{/n}
"I reserve the right to make a terrible joke. I'd hate you to think becoming difficult to court would spare you that."''', c('[Arrange the first evening.]', flags=("seelah.courting", "seelah.changed_beginning"))),
    n("friend", "Seelah", '''{n}She nods.{/n}
"Friends, then. Good to hear it from your own mouth. Even if we both tripped over our tongues getting there."''', c('[Remain friends.]', flags=("seelah.closed",))),
], requires=("inhuman",), forbids=("seelah.courting",))

s("door", "The latch on the inside", 3, '"Could we have an evening somewhere with a door?"', [
    n("start", "Seelah", '''"A door. That should improve our chances of finishing a conversation without somebody asking me to carry something."
{n}Seelah has borrowed a small room in Drezen. She shows it to you with a sweep of her arm that nearly catches the lamp.{/n}
"There. Bed, chair, window that mostly shuts. I have even put the lamp somewhere I am unlikely to kick it."''',
      c('"You remembered that I wanted some privacy."', "private", requires=("seelah.next_private",)),
      c('"I am glad you wanted this too."', "wanted")),
    n("private", "Seelah", '''"I did. And I nearly asked you to help carry a crate on the way here."
{n}She closes the door, looking pleased with herself.{/n}
"I found someone with a free evening and considerably less interesting plans. The crate is in excellent hands."''', c('"Then I have you to myself for a while."', "wanted")),
    n("wanted", "Seelah", '''{n}Her amusement gives way to something less easily hidden.{/n}
"I've wanted it all day. It's been making me very bad company. Someone asked me a perfectly reasonable question about a saddle, and I told them there was a window."
{n}She sits on the edge of the bed and pats the blanket beside her.{/n}
"One thing before I make a complete fool of myself. If you love somebody else, say so. I can stomach that. But have you sworn to them that there would be nobody else? Because I won't help you break your word."
{n}She rubs a thumb over a worn seam in the blanket.{/n}
"I'd rather be nervous for the ordinary reasons."''',
      c('"I have broken no promise by coming here. I want you."', "honest", flags=("seelah.open_terms",)),
      c('"I have a promise to settle before I can stay with you."', "wait")),
    n("wait", "Seelah", '''{n}She looks disappointed, then stands to open the door again.{/n}
"All right. Tell me when you've done that. Don't give me a lovely answer tonight and hope it becomes true later."
{n}As you prepare to leave, she asks you to wait.{/n}
"And come back when it's done. I still want you here, you idiot."''', c('[Leave the invitation open for another time.]', abort=True)),
    n("honest", "Seelah", '''"Good."
{n}She lets out a breath, then laughs at herself.{/n}
"I've been thinking of something charming to say. All of it has gone. You may have to put up with me wanting you rather badly and being no use at describing it."''',
      c('[Sit beside her and kiss her.]', "kiss", forbids=("inhuman",)),
      c('"I want to stay tonight. Let us stop trying to make speeches."', "night", forbids=("inhuman",)),
      c('"I want to be close. I am not ready for more tonight."', "quiet", forbids=("inhuman",)),
      c('"Some things are impossible in this body. I still want to try what we can."', "different", requires=("inhuman",))),
    n("kiss", "Seelah", '''{n}Seelah meets you halfway. Her hand settles at the back of your neck, warm and steady, and her next kiss is less tentative than the first.{/n}
{n}When you draw apart, she rests her forehead against yours.{/n}
"There. I should have started with that."''',
      c('"Stay with me tonight."', "night"),
      c('[Kiss her again, then settle beside her to talk.]', "quiet", flags=("seelah.kissed",))),
    n("night", "Seelah", '''{n}She turns the latch, then comes back to you. In the lamplight you can see the old scars on her hands and the small crease of a smile she keeps failing to suppress.{/n}
"If I knock that lamp over, we're blaming the bedpost," {n}she says.{/n}
{n}She is not clumsy. She unbuckles her sword belt and hangs it on the bedpost as if it has earned a rest, then pulls her shirt over her head in one impatient motion and stands there in the lamplight, freckled to the waist, grinning at your face.{/n}
"I've been thinking about that look all day," {n}she says.{/n} "Now you. Hurry up. I'm a paladin, not a saint."
{n}She helps, which is to say she undoes your laces faster than you do and kisses every part of you that comes free of them. The bed is too narrow for two and she does not care. She pushes you down onto it, climbs over you, knees either side of your hips, and takes your face in both hands to kiss you, slow now, as she settles her weight down onto you.{/n}
{n}The lamp survives. Neither of you remembers to put it out until much later.{/n}
{n}When the room is quiet, Seelah finds your hand beneath the blanket and holds it as she falls asleep, still smiling, one foot hooked over yours as if you might try to leave.{/n}''', c('[Stay through the night.]', flags=("seelah.lovers", "seelah.private_night", "seelah.kissed"))),
    n("quiet", "Seelah", '''"Then we'll have a quiet evening. I can manage one of those."
{n}She settles beside you, then makes a face.{/n}
"That sounded like a challenge. Give me a moment."
{n}She tells you about a disastrously expensive horse she once admired from a distance, and how much less handsome it became when she learned what it ate. Eventually the story gives way to a comfortable silence.{/n}
{n}When you leave, she catches your sleeve. "Come back soon. I'll find another horse to complain about."{/n}''', c('[Arrange another evening.]', flags=("seelah.lovers", "seelah.quiet_closeness"))),
    n("different", "Seelah", '''{n}She looks from the bed to you, then draws her feet aside.{/n}
"Well, come and tell me what works. I won't get far guessing from my own skin."
{n}You talk about what the two of you can still share. At one answer she bites her lip. At another she leans forward, a question already on her tongue.{/n}
"All right. I can learn. Preferably before I make a fool of myself, but I won't hold my breath."''', c('[Stay and try an evening together in your changed body.]', flags=("seelah.lovers", "seelah.changed_closeness"))),
], requires=("seelah.courting",), delay=24)

s("morning", "Four loaves and a bad bargain", 3, '"What have you bought this time?"', [
    n("start", "Seelah", '''{n}Seelah is carrying four loaves in a cloth bag. One has escaped far enough that she has to catch it with her elbow.{/n}
"Breakfast. Several people's breakfast. I went looking for one loaf and made the mistake of listening to the baker."
{n}She sets the bag down.{/n}
"The woman sleeping behind the storehouse needed bread. He said she could have yesterday's if somebody paid for it. I told him I would pay for fresh, and he looked so pleased that I bought enough to make it his problem to carry the rest."''',
      c('"That sounds like a very expensive victory."', "bargain"),
      c('"Did she want four loaves?"', "ask")),
    n("bargain", "Seelah", '''"It was going well until I remembered I had to carry these."
{n}She peers into the bag.{/n}
"I used to know exactly how much bread I could get for a coin. Apparently being paid regularly has made me a menace at a stall."''', c('"Did you ask what she needed?"', "ask")),
    n("ask", "Seelah", '''{n}Seelah opens her mouth, then closes it.{/n}
"She said she was hungry. Then I charged straight at the bread stall. I should have let her get another word in."
{n}She looks toward the storehouse.{/n}
"Come with me? I think I ought to find out whether she has anywhere to keep this dry."''', c('[Go with her.]', "visit")),
    n("visit", "Seelah", '''{n}The woman accepts one loaf and declines the others. What she needs is a place to leave her bedding while she looks for work. Seelah listens, asks who has already turned her away, and promises to speak to the storekeeper about a dry corner.{/n}
{n}On the way back, three loaves remain in the bag.{/n}
"Go on, laugh," {n}Seelah says.{/n} "Three spare loaves. A magnificent victory."
{n}Before you answer, she adds:{/n}
"I will ask the storekeeper. I won't just arrive with her blankets and an expression of heroic determination."''',
      c('"Good thing you heard her out. You would have marched off with the wrong job."', "honest"),
      c('"We should find someone who actually wants three loaves."', "bread")),
    n("honest", "Seelah", '''"So am I."
{n}She adjusts the bag, thoughtful now.{/n}
"An empty belly is bad enough. Then somebody with a full one comes along and tells you what you ought to want. I should know better."''', c('"You heard her. Now go and get her that dry corner."', "end")),
    n("bread", "Seelah", '''"The guards will. They have never refused anything that could be eaten while standing up."
{n}She grins at you over the bag.{/n}
"Don't tell them how much I paid. I have a reputation for knowing what I'm doing. In a few places."''', c('[Help her find a use for the bread.]', "end")),
    n("end", "Seelah", '''{n}When she has delivered the bread, Seelah leans against the wall for a moment.{/n}
"I was going to make today terribly impressive. Now I'd rather find somewhere to sit."
{n}She looks at you, suddenly a little shy.{/n}
"Come and sit with me? Fair warning, you've already had my best joke. I might fall asleep halfway through the next one."''', c('"Yes. Save me a place."', flags=("seelah.knows_need",))),
], requires=("seelah.door",), delay=24)

s("weight", "An argument worth finishing", 3, '"Do you ever worry that loving someone will make your judgment worse?"', [
    n("start", "Seelah", '''"Yes. Usually just after I've told somebody else to be sensible."
{n}She moves her shield away from the chair beside her.{/n}
"When it's somebody I love, I start making excuses. Then I catch myself and come down on them twice as hard. Ha! Some fine judgment that is."
{n}She looks directly at you.{/n}
"If you're asking whether I will always take your side, I won't. I hope you knew that already."''',
      c('"I want you to tell me when I am wrong, even when I dislike hearing it."', "tell", flags=("seelah.frank_terms",)),
      c('"I want you to hear my reasons before deciding I am wrong."', "hear", flags=("seelah.hear_terms",)),
      c('"I expect loyalty from someone who loves me."', "loyalty")),
    n("tell", "Seelah", '''"I can do that. You might have to remind me to let you answer."
{n}She rubs at a nick in the shield's rim.{/n}
"And tell me the truth before I go defending you to half the city. I've made that sort of fool of myself often enough."''', c('"You will hear it from me."', "end")),
    n("hear", "Seelah", '''"Fair. I can get halfway through a speech before I notice somebody trying to explain."
{n}She grimaces.{/n}
"But don't expect me to nod along. If you're hurting somebody, I'll stop you. We can argue afterward."''', c('"Then we should do this talking before someone is hurt."', "end")),
    n("loyalty", "Seelah", '''{n}Her expression closes.{/n}
"You've got my loyalty. You haven't bought my sword to wave at helpless people. And don't you dare ask me to watch cruelty to prove I love you."
{n}She puts the shield down.{/n}
"I want you. I won't blush over that. But I won't help you do wrong. Not even you."''',
      c('"That was unfair. I wanted to hear you were with me. I had no right to demand more."', "end", flags=("seelah.corrected_demand",)),
      c('"Then this will not work between us."', "part")),
    n("end", "Seelah", '''{n}The conversation has left her thoughtful. She turns the shield so its nicked rim rests against the wall.{/n}
"Stay a bit. My head's full of arguments, and I'm tired of marching. I'd rather sit here with you."
{n}She nudges the empty chair toward you with her boot.{/n}''', c('[Stay and finish the evening together.]', flags=("seelah.judgment_terms",))),
    n("part", "Seelah", '''{n}She says nothing for a while, then nods.{/n}
"Damn it. I wanted this to work."
{n}She picks up her shield and steps aside.{/n}
"The crusade still needs us. I'll do my part. We can manage that much without snarling at each other."''', c('[End the romance.]', flags=("seelah.closed", "seelah.parted",))),
], requires=("seelah.morning",), delay=24)

SCENES.append(scene("seelah.watch", "The watch she keeps", "Seelah", 4, "", [
    n("start", "Seelah", '''{n}At the Nexus, Seelah is sitting apart from the little camp. She has been repeating a few words under her breath. When she sees you, she stops and shifts over.{/n}
"They buy people here, and stroll past screaming like somebody's haggling over turnips. Today I caught myself walking past, too. Just too tired to be angry again."
{n}She looks down at her hands.{/n}
"That frightens me more than the shouting."''',
      c('"You are exhausted, Seelah. Even you have to sit down sometime."', "rest"),
      c('"Tell me what you saw. I will listen."', "tell")),
    n("tell", "Seelah", '''"A man being priced as though he were a horse. The buyer wanted to know whether an old injury would slow him down. He spoke quite politely."
{n}She presses her palms together.{/n}
"I wanted to break his jaw. Then I wanted to know where the other slaves were, and who could get them somewhere safe, and whether hitting him would get somebody else killed before I reached them."
{n}Her voice drops.{/n}
"I hate it. A man's in chains, and I have to count exits before I can hit the bastard holding them."''', c('"A broken jaw would do him no good if the other slavers killed him for it."', "rest")),
    n("rest", "Seelah", '''"Right. Yes. Easier to remember when you say it."
{n}She lets her hands fall to her knees.{/n}
"Sit with me? If I start planning another charge at the city, remind me I haven't even stood up yet."
{n}Beyond the camp, unfamiliar lights move in the darkness. Seelah looks at them once, then turns back to you.{/n}
"Tell me something from home. Something stupid. I'd like to remember there's more to the world than this place."''',
      c('"You promised me an evening after you had worn yourself out. Here we are."', "together", requires=("seelah.knows_need",)),
      c('"I am looking forward to hearing you complain about wet boots again."', "together")),
    n("together", "Seelah", '''{n}She laughs, softly at first, then with enough surprise that she has to catch her breath.{/n}
"I'll find something to complain about. You can count on me."
{n}You stay until she is ready to join the camp again. Before she goes, she asks you to find her tomorrow, even if neither of you has anything useful to report.{/n}''', c('[Promise to find her.]', flags=("seelah.abyss_together",))),
], Relationship="seelah", Remote=True, Areas=["7847c3e3537104f4694167af0b9fcd0e"],
    requires=("seelah.courting",), delay=24, last=4, optional=True))

s("souls", "After they opened their eyes", 5, '"You have been very quiet since the souls were returned."', [
    n("start", "Seelah", '''{n}Seelah has been cleaning her shield. The cloth in her hand has stopped moving.{/n}
"They opened their eyes. I thought I'd cheer loud enough to shake the roof."
{n}She looks up.{/n}
"Now all I can think is, have they got beds? Will they wake up screaming? And who haven't I counted? I keep counting them again."''',
      c('"Let us go and ask what they lack. I will come with you."', "care"),
      c('"They are alive. That is worth cheering. What happened to them still hurts."', "hurt")),
    n("care", "Seelah", '''"Arsinoe's been looking after them. I'll ask her before I blunder in with another cartload of bread."
{n}She smiles faintly.{/n}
"See? I do learn. Eventually."''', c('"I would like to speak to her too."', "grief", flags=("arsinoe.introduced",))),
    n("hurt", "Seelah", '''"Yes. Try telling that to the knot in my stomach."
{n}She folds the cloth, then unfolds it.{/n}
"I thought once we got them back I'd stop being afraid. They've barely opened their eyes, and here I am expecting them to put me right, too. Foolish."''', c('[Wait for her to go on.]', "grief")),
    n("grief", "Seelah", '''{n}She sets the cloth aside.{/n}
"There's something I can't get out of my head."''',
      c('"Elan."', "elan", requires=("seelah.elan_dead",)),
      c('"Tell me."', "survived", forbids=("seelah.elan_dead",)),
      c('"And Jannah?"', "jannah", requires=("jannah.joined",))),
    n("elan", "Seelah", '''{n}Seelah nods, looking at the floor.{/n}
"I keep starting to think of something to tell him. Something foolish. Then I remember."
{n}She presses her palm against her knee.{/n}
"Saving the others matters. I know it matters. I just hate that I can't turn around and find him being impatient with me for taking so long."''',
      c('"Tell me one of those foolish things, if you want to."', "memory"),
      c('"I will stay. You do not have to talk."', "quiet")),
    n("memory", "Seelah", '''"He would have had an opinion about the way I'm holding this shield."
{n}She gives a small, unsteady laugh.{/n}
"There. That's what I wanted to tell him. That he could stop correcting me for one evening, because I'd earned it."
{n}Her laugh falters. She looks down at the shield again.{/n}''', c('[Stay beside her.]', "end")),
    n("survived", "Seelah", '''"We nearly lost them. I keep thinking, one wrong turn, a few more minutes..."
{n}She catches herself and shakes her head.{/n}
"No. I won't spend tonight losing people who are still here. I'd rather ask them how they are."''', c('"And how are you holding up?"', "quiet")),
    n("quiet", "Seelah", '''"Tired. Glad you're here. Not very good company."
{n}She looks at you, and the familiar self-mocking smile returns for a moment.{/n}
"You were warned about that last part. No refunds."''', c('"I meant it."', "end")),
    n("end", "Seelah", '''{n}You stay until she is ready to put the shield away. Before you leave, she chooses a time to speak to Arsinoe about the people who still need help.{/n}
"Tomorrow," {n}she says.{/n} "Tonight I'm staying here with you."''', c('[Keep the evening with her.]', flags=("seelah.aftercare",))),
    # Her Q3 returned Jannah (ktc_DeserterJoins/Cue_0019 651ecf0c); Seelah's own word on her (Q3 epilogue line bedca9f9).
    n("jannah", "Seelah", '''{n}The cloth stops moving again, but this time her mouth softens.{/n}
"Jannah. She came back to us with a fresh scar and nothing but her word, and then she kept it. Elan told her to stay and watch the door, and she stayed and watched the door, and she hated every moment of it. I could see her hating it."
"She didn't break. She changed. I don't think I've ever seen her prouder than on the night we brought Sunhammer down."''',
      c('"And the piece of your mind you promised her?"', "jannah_mind")),
    n("jannah_mind", "Seelah", '''"I haven't given it to her yet." {n}She smiles at the shield, a little crookedly.{/n}
"Every time I try, I find I'd rather buy her a drink. That isn't very paladin-like of me. I've decided Iomedae will cope."''',
      c('"And you? How are you?"', "quiet")),
], requires=("seelah.morning", "seelah.souls_returned"), delay=24, optional=True)

s("road", "The road and the room", 5, '"I want to talk about a life after the fighting."', [
    *future_gate_nodes(),
    n("start", "Seelah", '''{n}Seelah has been polishing a buckle. She sets it down as soon as she hears you.{/n}
"Every time I start thinking of it, I want to say a prayer and check my sword. As if making plans will bring some demon down on us."
{n}She brings her chair closer.{/n}
"I want you there when I come home. But if somebody's crying for help down the road, I'll go. War or no war."''',
      c('"Then there will be a home waiting when you come back."', "home"),
      c('"We can travel together when our work allows it."', "travel"),
      c('"Fate has cheated enough people. Perhaps I can find a way to cheat it back."', "fate", requires=("trickster",))),
    n("home", "Seelah", '''"A place I can come back to. With a shelf that nobody borrows while I'm away."
{n}She smiles, then grows serious again.{/n}
"And write to me. Tell me the roof leaks, or you're angry, or somebody's pinched my shelf. Don't go keeping quiet for fear of bothering me until we hardly know each other."''', c('"You will have letters. And the shelf."', "choose", flags=("seelah.home_plans",))),
    n("travel", "Seelah", '''"I'd like that. Somewhere we can stop because the view is pretty, instead of because somebody has been murdered."
{n}She leans back and stretches her legs, smiling at the thought.{/n}
"Sometimes I'll have to go without you. And you without me. I'll miss you, but don't sit at home cursing me for going."''', c('"If I miss you badly, you will hear about it. Tell me when you miss me, too."', "choose", flags=("seelah.travel_plans",))),
    n("fate", "Seelah", '''"Could you?"
{n}The hope in her voice is immediate. She doesn't laugh it away.{/n}
"There are people I would give a great deal to see standing in front of me again. If you find a way, I want to help."
{n}She studies your face.{/n}
"But let me see the plan. I won't have somebody else dragged into a grave to keep ours empty. And don't expect anyone you bring back to kiss your feet. They've every reason to be angry."''', c('"We will find the price before we agree to it."', "choose", flags=("seelah.fate_terms",))),
    n("choose", "Seelah", '''"I know plans go wrong. I want you to stick with me when they do. Even when the roof leaks and I'm cross and there isn't a glorious thing about it."
{n}She reaches across the chair and lays her hand beside yours.{/n}''',
      c('"I will. I want a life with you."', "yes", flags=("seelah.committed",)),
      c('"I have loved being with you. But I cannot promise you that life."', "no")),
    n("yes", "Seelah", '''{n}For a moment she looks too happy to speak.{/n}
"Well. Good."
{n}She tries again, and laughs.{/n}
"I had something better prepared. You'll hear it eventually, probably while we're buying a shelf."
{n}The plans begin badly, with both of you talking at once. Neither seems inclined to stop.{/n}''', c('[Begin making plans together.]', "development_check", flags=("seelah.chosen_future",))),
    n("no", "Seelah", '''{n}She closes her hand and draws it back.{/n}
"Good thing you said it now. I was already picking out that shelf."
{n}She attempts a smile, then lets it go.{/n}
"Stupid, isn't it? A shelf. Go on. I'd rather be alone tonight."''', c('[Leave her alone tonight.]', flags=("seelah.closed", "seelah.parted",))),
    n("development_check", "Narrator", '''{n}Seelah walks you to the door. The promise goes with you.{/n}''',
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept"), forbids=("seelah.letter_unsettled",)),
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled", "seelah.copyist_followed")),
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled", "seelah.letter_return_addressed"), forbids=("seelah.copyist_followed",)),
      c('[Keep your promise. Talk through the rest of the plans another day.]', forbids=("seelah.future_reviewed",)),
      c('[Keep your promise. You still owe her the days you missed.]', requires=("seelah.future_reviewed",), forbids=("seelah.late_race_kept",)),
      c('[Keep your promise. Speak about the copyist again later.]', requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled"), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed"))),
], requires=("seelah.weight",), delay=24)

s("ordinary", "An evening with nothing to prove", 5, '"I came to see you. No emergency."', [
    n("start", "Seelah", '''{n}Seelah opens the door with her hair half unbraided and a weary expression that brightens when she sees you.{/n}
"Good. I'm not fit for an emergency. I tried to put my boot on the wrong foot and got angry with the boot."
{n}She lets you in. There is a chair for you, a lamp, a hairbrush on the table, and no attempt to disguise the heap of clothing she has not yet sorted.{/n}
"You said you would come when I was tired. I was hoping you meant tonight."''',
      c('"Sit down. Shall I pass you anything?"', "rest"),
      c('"I can be quiet company. Try me."', "quiet")),
    n("rest", "Seelah", '''"Nothing, actually. The brush is right here. I remembered to put it within reach."
{n}She picks it up and works at a stubborn braid.{/n}
"I thought I would have something worth telling you. Instead I spent most of the day getting people to stand in the right places, and then explaining that they needed to stay there."
{n}She pauses over the brush.{/n}
"Actually, you may be exactly the person to complain to about that."''', c('[Listen to the complaints and offer a few of your own.]', "end")),
    n("quiet", "Seelah", '''{n}She takes the brush and settles with a long sigh. For a while the only sound is the bristles catching softly in her hair.{/n}
"This is nice," {n}she says eventually.{/n}
{n}A little later she adds:{/n}
"Look at me. Given a perfectly good silence, and I have to put my boot in it."''', c('[Let the quiet last.]', "end")),
    n("end", "Seelah", '''{n}By the time you leave, she has put the brush down and left the clothes where they are. She looks rested enough to notice that you are reluctant to go.{/n}
"Come again tomorrow, if you can. I won't clean up especially."
{n}She gives you a tired, mischievous smile.{/n}
"If you can bear the boots and the dirty shirts, I reckon you'll survive another visit."''', c('[Promise another ordinary evening.]', flags=("seelah.at_home",))),
], requires=("seelah.road", "seelah.committed"), delay=24)

s("farewell", "Before the last road", 5, '"Before we go any further, I want a moment with you."', [
    *farewell_gate_nodes(),
    n("start", "Seelah", '''{n}Seelah checks the fastening on her shield, then makes herself stop checking it.{/n}
"Yes. So do I."
{n}She waits until you have a little privacy before speaking again.{/n}
"I keep thinking of things I ought to say, and then they sound like something carved on a tomb. I'd rather give you a reason to come back and argue with me."''',
      c('"We still have to choose your shelf."', "shelf", requires=("seelah.home_plans",)),
      c('"We have not chosen the first place we will travel together."', "journey", requires=("seelah.travel_plans",)),
      c('"I intend to hear more complaints about your boots."', "boots")),
    n("shelf", "Seelah", '''"Something sturdy. I have a talent for acquiring things that don't look heavy until you put them together."
{n}She smiles, then reaches for the shield again and stops herself.{/n}
"I want to be there when we choose it. I want that very much."''', c('"So do I."', "end")),
    n("journey", "Seelah", '''"Somewhere with a good road. I reserve the right to become more adventurous after my feet stop hurting."
{n}She takes a breath.{/n}
"I want to see you somewhere nobody needs to call you Commander."''', c('"Keep thinking of places. I will too."', "end")),
    n("boots", "Seelah", '''"I can promise those. I have several saved up already."
{n}She smiles, though her eyes remain serious.{/n}
"I want the stupid talk, too. All of it. I'm not turning every evening we have left into a funeral speech."''', c('"Then we should have as many as we can."', "end")),
    n("end", "Seelah", '''"I love you. That one was worth saying."
{n}She presses close, her cheek against yours. When she finally lifts her shield, her hand is steady.{/n}
"Ready when you are."''', c('[Go forward together.]', flags=("seelah.farewell_kept",))),
], requires=("seelah.ordinary",), delay=24)

s("parting", "A conversation without armor", 3, '"Seelah, there is something I have to tell you about us."', [
    n("start", "Seelah", '''{n}Seelah's attention sharpens.{/n}
"All right. Tell me."''',
      c('"I do not want to be your lover anymore."', "end"),
      c('"I have kept you waiting too often. I want to start seeing you again."', "stay")),
    n("end", "Seelah", '''{n}She listens without interrupting. When you finish, she takes a moment before answering.{/n}
"I'll miss you. Don't come round tomorrow expecting me to laugh about it. Give me a few days before we try being friends."
{n}She looks away, then back at you.{/n}
"But I'm glad you said it to me. I would have hated guessing from the way you stopped looking for me."''', c('[Part honestly.]', flags=("seelah.closed", "seelah.parted",))),
    n("stay", "Seelah", '''"Then let's choose a time now. Out loud, with a day in it." {n}She counts on her fingers.{/n} "I've had three suppers go cold waiting for you this month, and I told everyone who asked that you were busy saving the world. You were. I still ate them alone."
{n}She waits while you work out when you can both be free.{/n}''', c('[Stay her lover and arrange your next evening together.]', abort=True)),
], requires=("seelah.lovers",), optional=True)


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    nodes = [n("start", "Narrator", text, c(), portrait="Seelah")]
    consequences = {
        "together": "The stolen souls were home again. Seelah could plan for tomorrow, though she still had to ask who would come with her.",
        "unsettled": "After the rescue, Seelah took her doubts onto the road. Some letters told of her travels; others ended with a question she still could not answer.",
        "grieving": "The souls had returned. Some graves stayed filled, and Seelah still remembered the people in them.",
        "unfinished_work": "Seelah kept asking after the people she had failed to help, and following whatever leads she found.",
        "changed": "Seelah still argued with the Commander over their power. Even finding a way to sit together could take some doing.",
        "ascended": "Seelah loved the Commander before they became a god. She still had complaints to bring them, and work of her own to do.",
    }
    if id in consequences:
        consequence = consequences[id]
        nodes = [n("history", "Narrator", "{n}The war ended. Seelah had not forgotten what they had promised each other.{/n}",
                   c('[Continue.]', "start", requires=("seelah.developed_commitment",)),
                   c('[Continue.]', "short_history", requires=("seelah.short_future_chosen",), forbids=("seelah.developed_commitment",)),
                   c('[Continue.]', "earlier_promise", forbids=("seelah.developed_commitment", "seelah.short_future_chosen")), portrait="Seelah"),
                 *nodes,
                 n("short_history", "Narrator", "{n}" + consequence + "{/n}\n{n}Seelah and the Commander had promised to meet again. Sometimes she arrived to find supper waiting; sometimes a letter had to do. They had few evenings behind them and plenty of plans still to try. Neither yet knew how often the roads would bring them back to each other.{/n}", portrait="Seelah"),
                 n("earlier_promise", "Narrator", "{n}" + consequence + "{/n}\n{n}Seelah meant to keep her promise to the Commander. There were still invitations she had never sent, journeys to arrange, and evenings they had yet to spend together. She would have to find them between the calls for help. A promise alone would not fill the empty chair.{/n}", portrait="Seelah")]
    SCENES.append(scene("seelah.ending_" + id, "A place beside the fire", owner, 5, "", nodes,
                       Relationship="seelah", last=99, requires=requires, forbids=forbids))


ending("together", '''{n}Seelah continued to find people who needed her help. Loving the Commander had done little to cure that habit, though it gave her someone to complain to when she came home with ruined boots.{/n}
{n}Their plans changed often. Sometimes they traveled together; sometimes Seelah sent a letter and came home late, with an evening's worth of complaints. On the nights when she was too tired even for those, the Commander pulled up a chair and sat with her.{/n}''', requires=("seelah.committed", "seelah.souls_returned"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone", "seelah.ending_moderate", "seelah.ending_bad"))
ending("unsettled", '''{n}Seelah took to the road alone, still turning over the doubts the rescue had left her. She kissed the Commander goodbye, but packed her saddlebags all the same.{/n}
{n}They met less often than either had hoped. Seelah was glad of every visit, but could never give the Commander a date for her return. Her letters still came. Some carried a joke; others told plainly of the doubts that kept her on the road.{/n}''', requires=("seelah.committed", "seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone", "seelah.ending_bad"))
ending("grieving", '''{n}Returning the stolen souls had not given Seelah back everyone she lost. Some days she found it difficult to speak about the people she had been unable to save, even to the Commander.{/n}
{n}She spent much of her time away. Their meetings were precious partly because they were rare, and affection could not make every one of them easy. She kept writing, though, and sometimes a familiar joke found its way into a letter beside the harder things she needed to say.{/n}''', requires=("seelah.committed", "seelah.souls_returned", "seelah.ending_bad"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone"))
ending("unfinished_work", '''{n}The war ended, but Seelah kept searching for the people she had failed to help. She spent months on the road. Some letters ran to pages; others told where she had stopped and little more.{/n}
{n}Letters and rare visits kept Seelah and the Commander together. She greeted them warmly when they met, and left reluctantly when the next lead drew her away. She would not abandon the search.{/n}''', requires=("seelah.committed",), forbids=("seelah.souls_returned", "seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone"))
ending("changed", '''{n}Seelah never became indifferent to what the Commander's power could do. Their arguments continued, sometimes across a distance neither could easily cross.{/n}
{n}When they could meet, they tried to find some way to spend the evening together. Seelah still said plainly what frightened her, and still laughed at their old jokes. Sometimes they found an answer. Sometimes she went away angry, and wrote again when she had cooled enough to put pen to paper.{/n}''', requires=("seelah.committed", "inhuman"), forbids=("seelah.closed", "ascended", "seelah_dead", "seelah_gone"))
ending("ascended", '''{n}The Commander's divinity did not make Seelah especially reverent in private. Her prayers concerned the people who needed help. Her personal messages were more likely to concern an invitation, or a complaint that even a god ought to answer a letter.{/n}
{n}She kept a place beside her for the person she had loved before the shrines appeared. Her doubts still sent her out alone with sword and saddlebags. When the Commander visited, she was glad to waste an evening talking about supper and ruined boots.{/n}''', requires=("seelah.committed", "ascended"), forbids=("seelah.closed", "seelah_dead", "seelah_gone"))
ending("apart", '''{n}Seelah and the Commander stopped planning their evenings together. For a time she found herself saving small stories to tell them, then remembering why she no longer should.{/n}
{n}She did not regret every part of what they had shared. In later years she could speak of it without anger, though some memories remained hers alone.{/n}''', requires=("seelah.lovers", "seelah.closed"), forbids=("seelah_dead",))
ending("unfinished", '''{n}Seelah remembered the evenings she had spent with the Commander, and the next visits she had hoped for. The war ended before they found out whether supper and a chair by the fire would follow.{/n}
{n}Sometimes Seelah smiled over those evenings. She had never heard the Commander promise more. There were still people calling for help, and she took her sword down the road.{/n}''', requires=("seelah.courting",), forbids=("seelah.committed", "seelah.closed", "seelah_dead", "seelah_gone"))
ending("aeon", '''{n}In a world spared the Worldwound, Seelah had other roads to travel and no memory of a crusade that never happened. She still drank too much at weddings, still won races she had no business winning, and still stopped in the street for any child who looked hungry enough to steal.{/n}
{n}Some evenings, for no reason she could name, she kicked her pack aside at the fire and left half the blanket empty. Nobody came. She slept on her own side of it anyway, and in the morning she rolled it up and went on.{/n}''', requires=("seelah.committed",), forbids=("seelah.closed",), owner="AeonEpilogue")


# Earned presence (rubric Binding context (3)): a Commander who stepped into the Wound and prepared no return is mourned,
# not met by the fire. The living endings above now Forbid the sacrifice unless trickster.commander_back holds.
SCENES.append(scene("seelah.ending_sacrifice", "A place beside the fire", "Epilogue", 5, "", [
    n("start", "Narrator", """{n}Word came back from the Wound with the heralds, and the heralds had already decided it was glorious. Seelah let one of them say so. When he said it a second time she took the trumpet out of his hands and told him to go and help somebody.{/n}
{n}There was no body to wait for. She took the chair the Commander had kept beside her fire, carried it out to the Kenabres road, and left it at the first shrine of Iomedae she passed, with a pair of ruined boots under it. The priests called it an offering. It was a complaint, and she meant the Inheritor to hear it.{/n}
{n}Then she went where she was needed, because that was the promise they had actually made each other, and she would not let the Wound have that as well.{/n}""", c(),
      portrait="Seelah", paragraphs=(
          p("""{n}The purse stayed in her pack, tied badly on purpose, with the note still inside that she had meant to leave on a pillow after the war. Nobody ever asked her properly. She never untied it.{/n}""",
            requires=("seelah.trickster.late_committed",)),
      )),
], Relationship="seelah", last=99, requires=("sacrifice",),
    forbids=("seelah.closed", "seelah_dead", "seelah_gone", "seelah.trickster.declined", "seelah.trickster.friends"),
    RequiresAnyGroups=[["seelah.committed", "seelah.lovers", "seelah.trickster.late_committed"]],
    ForbidOverrides={"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned",
                     "seelah.trickster.declined": "seelah.committed", "seelah.trickster.friends": "seelah.committed"}))
