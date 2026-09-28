"""Seelah continuation draft; restoration and transformed contact access are separate work."""
from story_format import c, n, scene
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


s("changed_opening", "An unfamiliar way to begin", 5, '"I would like to spend time with you, if you would consider it."', [
    n("start", "Seelah", '''{n}Seelah listens without moving closer. When she answers, she chooses her words carefully.{/n}
"I agreed to talk. I haven't agreed that everything between us is settled."
{n}She rests her hands at her sides.{/n}
"If you're asking whether I can still care about you, yes. If you're asking whether that makes me less troubled by what your power does, it doesn't. I won't pretend those are the same question."''',
      c('"I am asking whether you would want something personal between us."', "ask"),
      c('"Then let us keep this as friendship."', "friend")),
    n("ask", "Seelah", '''"I might. That's the difficult answer."
{n}For a moment her expression is almost angry, though she stays.{/n}
"I know what I usually do when I like somebody. I bring food. I find an excuse to sit close. I make a joke and hope they laugh. Here I don't even know which of those would be welcome."
{n}She takes a breath.{/n}
"I could begin by asking what spending an evening together would mean for you."''',
      c('"Talk to me. Tell me about your day, and ask about mine."', "time"),
      c('"Let us find something we can both enjoy, without pretending my body has not changed."', "time")),
    n("time", "Seelah", '''"All right. One evening. Then we can ask each other whether we want another."
{n}A little warmth returns to her face.{/n}
"I reserve the right to make a terrible joke. I'd hate you to think becoming difficult to court would spare you that."''', c('[Agree to begin carefully.]', flags=("seelah.courting", "seelah.changed_beginning"))),
    n("friend", "Seelah", '''{n}She nods.{/n}
"I can do that. And I appreciate you telling me what you meant, even when it was awkward."''', c('[Keep the relationship platonic.]', flags=("seelah.closed",))),
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
{n}She sits on the edge of the bed, leaving room beside her.{/n}
"Before I start saying worse things, I know there may be other people you love. I don't need you to stop caring about them. I do need to know whether you've promised somebody something that makes this a lie."
{n}She rubs a thumb over a worn seam in the blanket.{/n}
"I'd rather be nervous for the ordinary reasons."''',
      c('"I can make room for you honestly. I want you here."', "honest", flags=("seelah.open_terms",)),
      c('"I need to settle a promise before we go further."', "wait")),
    n("wait", "Seelah", '''{n}She looks disappointed, then stands to open the door again.{/n}
"All right. Tell me when you've done that. Don't give me a lovely answer tonight and hope it becomes true later."
{n}As you prepare to leave, she asks you to wait.{/n}
"I still want another evening. You haven't ruined that by telling me."''', c('[Leave the invitation open for another time.]', abort=True)),
    n("honest", "Seelah", '''"Good."
{n}She lets out a breath, then laughs at herself.{/n}
"I've been thinking of something charming to say. All of it has gone. You may have to put up with me wanting you rather badly and being no use at describing it."''',
      c('[Sit beside her and kiss her.]', "kiss", forbids=("inhuman",)),
      c('"I want to stay tonight. Let us stop trying to make speeches."', "night", forbids=("inhuman",)),
      c('"I want to be close. I am not ready for more tonight."', "quiet", forbids=("inhuman",)),
      c('"My body makes some of this impossible. I want us to find what is possible."', "different", requires=("inhuman",))),
    n("kiss", "Seelah", '''{n}Seelah meets you halfway. Her hand settles at the back of your neck, warm and steady, and her next kiss is less tentative than the first.{/n}
{n}When you draw apart, she rests her forehead against yours.{/n}
"There. I should have started with that."''',
      c('"Stay with me tonight."', "night"),
      c('[Kiss her again, then settle beside her to talk.]', "quiet", flags=("seelah.kissed",))),
    n("night", "Seelah", '''{n}She turns the latch, then comes back to you. In the lamplight you can see the old scars on her hands and the small crease of a smile she keeps failing to suppress.{/n}
"You can tell me if I'm being clumsy," she says. "Preferably before I knock the lamp over."
{n}She is not clumsy. She unbuckles her sword belt and hangs it on the bedpost as if it has earned a rest, then pulls her shirt over her head in one impatient motion and stands there in the lamplight, freckled to the waist, grinning at your face.{/n}
"I've been thinking about that look all day," she says. "Now you. Hurry up. I'm a paladin, not a saint."
{n}She helps, which is to say she undoes your laces faster than you do and kisses every part of you that comes free of them. The bed is too narrow for two and she does not care. She pushes you down onto it, climbs over you, knees either side of your hips, and takes your face in both hands to kiss you, slow now, as she settles her weight down onto you.{/n}
{n}The lamp survives. Neither of you remembers to put it out until much later.{/n}
{n}When the room is quiet, Seelah finds your hand beneath the blanket and holds it as she falls asleep, still smiling, one foot hooked over yours as if you might try to leave.{/n}''', c('[Stay through the night.]', flags=("seelah.lovers", "seelah.private_night", "seelah.kissed"))),
    n("quiet", "Seelah", '''"Then we'll have a quiet evening. I can manage one of those."
{n}She settles beside you, then makes a face.{/n}
"That sounded like a challenge. Give me a moment."
{n}She tells you about a disastrously expensive horse she once admired from a distance, and how much less handsome it became when she learned what it ate. Eventually the story gives way to a comfortable silence.{/n}
{n}When you leave, she asks you to come again. This time she manages it without apologizing for how much she hopes you will.{/n}''', c('[Arrange another evening.]', flags=("seelah.lovers", "seelah.quiet_closeness"))),
    n("different", "Seelah", '''{n}She considers the room, then the place she left for you.{/n}
"Tell me. I don't want to keep offering you things because they would comfort me."
{n}You begin with what you can share here. Some answers make her sad, and she does not conceal that from you. Others make her curious enough to ask another question.{/n}
"I can learn," she says. "You may have to stop me when I try to learn everything at once."''', c('[Spend the evening discovering what you can share.]', flags=("seelah.lovers", "seelah.changed_closeness"))),
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
"I asked if she was hungry. She said yes. I may have started solving things rather quickly after that."
{n}She looks toward the storehouse.{/n}
"Come with me? I think I ought to find out whether she has anywhere to keep this dry."''', c('[Go with her.]', "visit")),
    n("visit", "Seelah", '''{n}The woman accepts one loaf and declines the others. What she needs is a place to leave her bedding while she looks for work. Seelah listens, asks who has already turned her away, and promises to speak to the storekeeper about a dry corner.{/n}
{n}On the way back, three loaves remain in the bag.{/n}
"You may laugh," Seelah says. "I've earned it."
{n}Before you answer, she adds:{/n}
"I will ask the storekeeper. I won't just arrive with her blankets and an expression of heroic determination."''',
      c('"I like your determination. I am glad you let her finish speaking."', "honest"),
      c('"We should find someone who actually wants three loaves."', "bread")),
    n("honest", "Seelah", '''"So am I."
{n}She adjusts the bag, thoughtful now.{/n}
"Being hungry is miserable. Having everybody decide what sort of hungry person you are can be almost as bad. I ought to remember that before I start being splendid at people."''', c('"You caught yourself. Now keep the smaller promise."', "end")),
    n("bread", "Seelah", '''"The guards will. They have never refused anything that could be eaten while standing up."
{n}She grins at you over the bag.{/n}
"Don't tell them how much I paid. I have a reputation for knowing what I'm doing. In a few places."''', c('[Help her find a use for the bread.]', "end")),
    n("end", "Seelah", '''{n}When she has delivered the bread, Seelah leans against the wall for a moment.{/n}
"I was going to make today terribly impressive. Now I'd rather find somewhere to sit."
{n}She looks at you, suddenly a little shy.{/n}
"Would you come even if I was tired and had nothing clever to say? I think I would like to find out what that's like."''', c('"Yes. Save me a place."', flags=("seelah.knows_need",))),
], requires=("seelah.door",), delay=24)

s("weight", "An argument worth finishing", 3, '"Do you ever worry that loving someone will make your judgment worse?"', [
    n("start", "Seelah", '''"Yes. Usually just after I've told somebody else to be sensible."
{n}She moves her shield away from the chair beside her.{/n}
"I want the people I love to be all right. Sometimes I want that so badly I start looking for a good reason to excuse them. Sometimes I get frightened of doing that and judge them harder than I would a stranger."
{n}She looks directly at you.{/n}
"If you're asking whether I will always take your side, I won't. I hope you knew that already."''',
      c('"I want you to tell me when I am wrong, even when I dislike hearing it."', "tell", flags=("seelah.frank_terms",)),
      c('"I want you to hear my reasons before deciding I am wrong."', "hear", flags=("seelah.hear_terms",)),
      c('"I expect loyalty from someone who loves me."', "loyalty")),
    n("tell", "Seelah", '''"I can do that. You might have to remind me to let you answer."
{n}She rubs at a nick in the shield's rim.{/n}
"And I need you to tell me things before I've made a fool of myself defending a version that isn't true. That's happened often enough without us helping it along."''', c('"You will hear it from me."', "end")),
    n("hear", "Seelah", '''"Fair. I can get halfway through a speech before I notice somebody trying to explain."
{n}She grimaces.{/n}
"But hearing you isn't a promise to agree. If somebody is being hurt, I won't stand there politely while we work out whose argument sounds better."''', c('"Then we should do this talking before someone is hurt."', "end")),
    n("loyalty", "Seelah", '''{n}Her expression closes.{/n}
"You have it. You do not have permission to use me to frighten people, or to make me watch something cruel because leaving would prove I didn't love you enough."
{n}She puts the shield down.{/n}
"I want you. I am not ashamed of that. Don't make it a thing I have to defend against you."''',
      c('"That was unfair. I was asking for reassurance and turned it into a demand."', "end", flags=("seelah.corrected_demand",)),
      c('"Then I cannot give you the relationship you want."', "part")),
    n("end", "Seelah", '''{n}The conversation has left her thoughtful. She turns the shield so its nicked rim rests against the wall.{/n}
"Stay for a while? We don't have to settle everything tonight. I'd just rather we didn't finish the evening by marching off in different directions."
{n}She makes room for you, and the question is easier to answer than the ones that came before it.{/n}''', c('[Stay and finish the evening together.]', flags=("seelah.judgment_terms",))),
    n("part", "Seelah", '''{n}She nods after a long silence.{/n}
"I'm sorry. I would have liked us to find a way."
{n}She gathers her things, leaving you room to leave without walking around her.{/n}
"I'll still do the work I came here to do. We can be civil while we do it."''', c('[End the romance.]', flags=("seelah.closed", "seelah.parted",))),
], requires=("seelah.morning",), delay=24)

SCENES.append(scene("seelah.watch", "The watch she keeps", "Seelah", 4, "", [
    n("start", "Seelah", '''{n}At the Nexus, Seelah is sitting apart from the little camp. She has been repeating a few words under her breath. When she sees you, she stops and shifts over.{/n}
"I keep thinking about what they call ordinary here. The things people walk past. Then I catch myself getting used to some of it, because I can't be furious every moment I'm awake."
{n}She looks down at her hands.{/n}
"That frightens me more than the shouting."''',
      c('"You have not stopped caring because you need to rest."', "rest"),
      c('"Tell me what you saw. I will listen."', "tell")),
    n("tell", "Seelah", '''"A man being priced as though he were a horse. The buyer wanted to know whether an old injury would slow him down. He spoke quite politely."
{n}She presses her palms together.{/n}
"I wanted to break his jaw. Then I wanted to know where the other slaves were, and who could get them somewhere safe, and whether hitting him would get somebody else killed before I reached them."
{n}Her voice drops.{/n}
"I hate having to become good at thinking like that."''', c('"You were thinking about how to help him survive."', "rest")),
    n("rest", "Seelah", '''"I know. I needed someone else to say it."
{n}She lets her hands fall to her knees.{/n}
"Sit with me until I stop trying to solve the whole city? I promise I'll notice when I'm doing it. Eventually."
{n}Beyond the camp, unfamiliar lights move in the darkness. Seelah looks at them once, then turns back to you.{/n}
"Tell me something ordinary. I would like to remember what we're trying to get back to."''',
      c('"You still owe me an evening when you are allowed to be tired."', "together", requires=("seelah.knows_need",)),
      c('"I am looking forward to hearing you complain about wet boots again."', "together")),
    n("together", "Seelah", '''{n}She laughs, softly at first, then with enough surprise that she has to catch her breath.{/n}
"I'll find something to complain about. You can count on me."
{n}You stay until she is ready to join the camp again. Before she goes, she asks you to find her tomorrow, even if neither of you has anything useful to report.{/n}''', c('[Promise to find her.]', flags=("seelah.abyss_together",))),
], Relationship="seelah", Remote=True, Areas=["7847c3e3537104f4694167af0b9fcd0e"],
    requires=("seelah.courting",), delay=24, last=4, optional=True))

s("souls", "After they opened their eyes", 5, '"You have been very quiet since the souls were returned."', [
    n("start", "Seelah", '''{n}Seelah has been cleaning her shield. The cloth in her hand has stopped moving.{/n}
"I thought I would feel it all at once. Relief. Joy. Something large enough to make sense of what we did."
{n}She looks up.{/n}
"Instead I keep wondering whether everybody has somewhere to sleep tonight. Whether they'll be frightened when they close their eyes. Whether I've forgotten someone because I was so relieved to see the others wake up."''',
      c('"We can ask who needs help. You do not have to guess alone."', "care"),
      c('"You can be glad and still hurt for what happened."', "hurt")),
    n("care", "Seelah", '''"Arsinoe will know more than I do about what they need now. I should speak to her before I arrive with a plan she has already tried."
{n}She smiles faintly.{/n}
"I've been practicing that part. Asking first."''', c('"I would like to speak to her too."', "grief", flags=("arsinoe.introduced",))),
    n("hurt", "Seelah", '''"I know. I keep forgetting that knowing something doesn't make you good at it."
{n}She folds the cloth, then unfolds it.{/n}
"I wanted to bring them back and be finished being frightened. That was a little much to expect from people who had only just got their lives back."''', c('[Give her time to continue.]', "grief")),
    n("grief", "Seelah", '''{n}She sets the cloth aside.{/n}
"There is one part I keep coming back to."''',
      c('"Elan."', "elan", requires=("seelah.elan_dead",)),
      c('"Tell me."', "survived", forbids=("seelah.elan_dead",))),
    n("elan", "Seelah", '''{n}Seelah nods, looking at the floor.{/n}
"I keep starting to think of something to tell him. Something foolish. Then I remember."
{n}She presses her palm against her knee.{/n}
"Saving the others matters. I know it matters. I just hate that I can't turn around and find him being impatient with me for taking so long."''',
      c('"Tell me one of those foolish things, if you want to."', "memory"),
      c('"I will stay. You do not have to talk."', "quiet")),
    n("memory", "Seelah", '''"He would have had an opinion about the way I'm holding this shield."
{n}She gives a small, unsteady laugh.{/n}
"There. That's what I wanted to tell him. That he could stop correcting me for one evening, because I'd earned it."
{n}She lets the silence follow without trying to make the story more worthy of him.{/n}''', c('[Stay beside her.]', "end")),
    n("survived", "Seelah", '''"How close we came. I keep trying to imagine a version where we were a little slower."
{n}She catches herself and shakes her head.{/n}
"No. I won't spend tonight losing people who are still here. I'd rather ask them how they are."''', c('"Begin with yourself. How are you?"', "quiet")),
    n("quiet", "Seelah", '''"Tired. Glad you're here. Not very good company."
{n}She looks at you, and the familiar self-mocking smile returns for a moment.{/n}
"You did agree to that last part. I remember."''', c('"I meant it."', "end")),
    n("end", "Seelah", '''{n}You stay until she is ready to put the shield away. Before you leave, she chooses a time to speak to Arsinoe about the people who still need help.{/n}
"Tomorrow," she says. "Tonight I think I'd like to be here with you."''', c('[Keep the evening with her.]', flags=("seelah.aftercare",))),
], requires=("seelah.morning", "seelah.souls_returned"), delay=24, optional=True)

s("road", "The road and the room", 5, '"I want to talk about a life after the fighting."', [
    *future_gate_nodes(),
    n("start", "Seelah", '''{n}Seelah has been polishing a buckle. She sets it down as soon as she hears you.{/n}
"I have been trying to think about that without feeling as though I'm tempting something awful to happen."
{n}She brings her chair closer.{/n}
"I want a life with you in it. I also know there will still be people who need help when this war is over. I won't be very good at pretending I haven't heard about them."''',
      c('"Then we make a home you can leave without losing it."', "home"),
      c('"We can travel together when our work allows it."', "travel"),
      c('"As a Trickster, I could steal us a future that fate forgot to offer."', "fate", requires=("trickster",))),
    n("home", "Seelah", '''"A place I can come back to. With a shelf that nobody borrows while I'm away."
{n}She smiles, then grows serious again.{/n}
"And letters. Bad ones are fine. Tell me the roof leaks, or you're angry with me, or somebody has stolen my shelf. I don't want to find that we've become strangers while we were being considerate about each other's work."''', c('"You will have letters. And the shelf."', "choose", flags=("seelah.home_plans",))),
    n("travel", "Seelah", '''"I'd like that. Somewhere we can stop because the view is pretty, instead of because somebody has been murdered."
{n}She leans back, allowing herself to imagine it.{/n}
"Some journeys will still be mine, though. Or yours. We should learn how to miss each other without making it a punishment."''', c('"We can tell each other when it becomes difficult."', "choose", flags=("seelah.travel_plans",))),
    n("fate", "Seelah", '''"Could you?"
{n}The hope in her voice is immediate. She doesn't laugh it away.{/n}
"There are people I would give a great deal to see standing in front of me again. If you find a way, I want to help."
{n}She studies your face.{/n}
"But tell me what you're doing. I don't want to find out afterward that somebody else paid for the happy ending. And if you bring someone back, let them be angry about what happened. They may need to be."''', c('"We will find the price before we agree to it."', "choose", flags=("seelah.fate_terms",))),
    n("choose", "Seelah", '''"I don't need us to promise that nothing will change. I would like to know that you mean to keep choosing this when it takes a little work."
{n}Her hand rests open on the chair between you.{/n}''',
      c('"I do. I want you in my life, and I intend to make room."', "yes", flags=("seelah.committed",)),
      c('"I love what we have had. I cannot promise to build a future around it."', "no")),
    n("yes", "Seelah", '''{n}For a moment she looks too happy to speak.{/n}
"Well. Good."
{n}She tries again, and laughs.{/n}
"I had something better prepared. You'll hear it eventually, probably while we're buying a shelf."
{n}The plans begin badly, with both of you talking at once. Neither seems inclined to stop.{/n}''', c('[Begin making plans together.]', "development_check", flags=("seelah.chosen_future",))),
    n("no", "Seelah", '''{n}She closes her hand and draws it back.{/n}
"Thank you for telling me before I started imagining it in detail."
{n}She attempts a smile, then lets it go.{/n}
"Too much detail, anyway. I think I'd like to be alone for a while."''', c('[Give her the space she asks for.]', flags=("seelah.closed", "seelah.parted",))),
    n("development_check", "Narrator", '''{n}You leave the conversation with a promise to keep, and the days you have actually shared behind it.{/n}''',
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept"), forbids=("seelah.letter_unsettled",)),
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled", "seelah.copyist_followed")),
      c('[Keep the future you have discussed.]', flags=("seelah.developed_commitment",), requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled", "seelah.letter_return_addressed"), forbids=("seelah.copyist_followed",)),
      c('[Keep the existing promise and return to the unspoken details later.]', forbids=("seelah.future_reviewed",)),
      c('[Keep the existing promise without claiming the missed days together.]', requires=("seelah.future_reviewed",), forbids=("seelah.late_race_kept",)),
      c('[Keep the existing promise and return to the unresolved copyist conversation.]', requires=("seelah.future_reviewed", "seelah.late_race_kept", "seelah.letter_unsettled"), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed"))),
], requires=("seelah.weight",), delay=24)

s("ordinary", "An evening with nothing to prove", 5, '"I came to see you. No emergency."', [
    n("start", "Seelah", '''{n}Seelah opens the door with her hair half unbraided and a weary expression that brightens when she sees you.{/n}
"Good. I'm not fit for an emergency. I tried to put my boot on the wrong foot and got angry with the boot."
{n}She lets you in. There is a chair for you, a lamp, a hairbrush on the table, and no attempt to disguise the heap of clothing she has not yet sorted.{/n}
"You said you would come when I was tired. I was hoping you meant tonight."''',
      c('"Sit down. Tell me what you want within reach."', "rest"),
      c('"I can be quiet company. Try me."', "quiet")),
    n("rest", "Seelah", '''"Nothing, actually. The brush is right here. I remembered to put it within reach."
{n}She picks it up and works at a stubborn braid.{/n}
"I thought I would have something worth telling you. Instead I spent most of the day getting people to stand in the right places, and then explaining that they needed to stay there."
{n}She pauses over the brush.{/n}
"Actually, you may be exactly the person to complain to about that."''', c('[Listen to the complaints and offer a few of your own.]', "end")),
    n("quiet", "Seelah", '''{n}She takes the brush and settles with a long sigh. For a while the only sound is the bristles catching softly in her hair.{/n}
"This is nice," she says eventually.
{n}A little later she adds:{/n}
"I'm resisting the urge to improve it by telling you how nice it is."''', c('[Let the quiet last.]', "end")),
    n("end", "Seelah", '''{n}By the time you leave, she has put the brush down and left the clothes where they are. She looks rested enough to notice that you are reluctant to go.{/n}
"Come again tomorrow, if you can. I won't clean up especially."
{n}She gives you a tired, mischievous smile.{/n}
"That's how you know I trust you."''', c('[Promise another ordinary evening.]', flags=("seelah.at_home",))),
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
"I want all those stupid conversations. I don't want to decide afterward that I should have spent every moment saying something important."''', c('"Then we should have as many as we can."', "end")),
    n("end", "Seelah", '''"I love you. That one was worth saying."
{n}She stays close for a moment, with no speech prepared and no need to find one. When she finally lifts her shield, her hand is steady.{/n}
"Ready when you are."''', c('[Go forward together.]', flags=("seelah.farewell_kept",))),
], requires=("seelah.ordinary",), delay=24)

s("parting", "A conversation without armor", 3, '"We need to talk about our relationship."', [
    n("start", "Seelah", '''{n}Seelah's attention sharpens.{/n}
"All right. Tell me."''',
      c('"I want to end the romance."', "end"),
      c('"I have been distant. I want us to make time for each other again."', "stay")),
    n("end", "Seelah", '''{n}She listens without interrupting. When you finish, she takes a moment before answering.{/n}
"I'm going to miss you. I may need a little space before I get good at being your friend again."
{n}She looks away, then back at you.{/n}
"But I'm glad you said it to me. I would have hated guessing from the way you stopped looking for me."''', c('[Part honestly.]', flags=("seelah.closed", "seelah.parted",))),
    n("stay", "Seelah", '''"Then let's choose a time now. Out loud, with a day in it." She counts on her fingers. "I've had three suppers go cold waiting for you this month, and I told everyone who asked that you were busy saving the world. You were. I still ate them alone."
{n}She waits while you work out when you can both be free.{/n}''', c('[Keep the relationship and make a plan.]', abort=True)),
], requires=("seelah.lovers",), optional=True)


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    nodes = [n("start", "Narrator", text, c(), portrait="Seelah")]
    consequences = {
        "together": "Returning the stolen souls gave Seelah reasons for hope, but it did not decide what anyone would choose afterward.",
        "unsettled": "The rescue left Seelah with questions she needed time, and sometimes distance, to examine.",
        "grieving": "Returning souls had not undone every loss, and Seelah's grief remained part of the life she had to live.",
        "unfinished_work": "Seelah still wanted to find out what could be done for the people she had been unable to help.",
        "changed": "The Commander's changed nature did not silence Seelah's objections or make closeness easy.",
        "ascended": "The Commander's ascent did not turn Seelah's affection into worship or settle her unfinished work.",
    }
    if id in consequences:
        consequence = consequences[id]
        nodes = [n("history", "Narrator", "{n}The war left them with the promises they had actually made.{/n}",
                   c('[Continue.]', "start", requires=("seelah.developed_commitment",)),
                   c('[Continue.]', "short_history", requires=("seelah.short_future_chosen",), forbids=("seelah.developed_commitment",)),
                   c('[Continue.]', "earlier_promise", forbids=("seelah.developed_commitment", "seelah.short_future_chosen")), portrait="Seelah"),
                 *nodes,
                 n("short_history", "Narrator", "{n}" + consequence + "{/n}\n{n}She and the Commander had chosen to keep seeing one another without pretending they had already built a shared life. Some invitations became evenings together; others remained hopes. They had left themselves room to discover what more they could offer, and neither could honestly claim to know the answer yet.{/n}", portrait="Seelah"),
                 n("earlier_promise", "Narrator", "{n}" + consequence + "{/n}\n{n}The promise she and the Commander had made remained important to her. It did not supply the days they had yet to spend together. There were plans to try, obligations to explain, and an affection whose place in their lives would have to be discovered by living them.{/n}", portrait="Seelah")]
    SCENES.append(scene("seelah.ending_" + id, "A place beside the fire", owner, 5, "", nodes,
                       Relationship="seelah", last=99, requires=requires, forbids=forbids))


ending("together", '''{n}Seelah continued to find people who needed her help. Loving the Commander had done little to cure that habit, though it gave her someone to complain to when she came home with ruined boots.{/n}
{n}Their plans changed often. Some journeys they made together; others ended with a letter, an overdue arrival, and an evening neither was willing to surrender. Seelah learned that she could come home tired and have nothing impressive to say, and still find someone glad she had come.{/n}''', requires=("seelah.committed", "seelah.souls_returned"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone", "seelah.ending_moderate", "seelah.ending_bad"))
ending("unsettled", '''{n}Seelah still had questions she needed to answer away from the Commander. Affection had not spared her doubt, and there were journeys she chose to make alone.{/n}
{n}Their meetings became less frequent than either had hoped. When they did meet, the pleasure of each other's company remained. She asked for patience without promising a date when she would be finished with her questions, and the letters she kept sending were often more honest than reassuring.{/n}''', requires=("seelah.committed", "seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone", "seelah.ending_bad"))
ending("grieving", '''{n}Returning the stolen souls had not given Seelah back everyone she lost. Some days she found it difficult to speak about the people she had been unable to save, even to the Commander.{/n}
{n}She spent much of her time away. Their meetings were precious partly because they were rare, and affection could not make every one of them easy. She kept writing, though, and sometimes a familiar joke found its way into a letter beside the harder things she needed to say.{/n}''', requires=("seelah.committed", "seelah.souls_returned", "seelah.ending_bad"), forbids=("seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone"))
ending("unfinished_work", '''{n}The ending of the war did not settle what Seelah felt about the people she had been unable to help. She spent long stretches away, sometimes writing freely and sometimes finding it difficult to describe where her thoughts had taken her.{/n}
{n}The relationship survived in those letters and in meetings too rare to become ordinary. She was still glad to see the Commander. She still needed a life in which loving them did not mean setting her unanswered questions aside.{/n}''', requires=("seelah.committed",), forbids=("seelah.souls_returned", "seelah.closed", "inhuman", "ascended", "seelah_dead", "seelah_gone"))
ending("changed", '''{n}Seelah never became indifferent to what the Commander's power could do. Their arguments continued, sometimes across a distance neither could easily cross.{/n}
{n}When they could meet, they kept searching for ways to share an evening. She still spoke plainly about what frightened her. She still laughed at familiar jokes. Whatever shape their closeness took, it required more care than either had imagined, and she kept asking for that care in her own voice.{/n}''', requires=("seelah.committed", "inhuman"), forbids=("seelah.closed", "ascended", "seelah_dead", "seelah_gone"))
ending("ascended", '''{n}The Commander's divinity did not make Seelah especially reverent in private. Her prayers concerned the people who needed help. Her personal messages were more likely to concern an invitation, or a complaint that even a god ought to answer a letter.{/n}
{n}She kept a place for the person she had loved before anybody thought to build a shrine. Her own unanswered questions remained, and there were journeys she needed to make alone. When they found time together, she was glad to discover that some conversations could still be wonderfully unimportant.{/n}''', requires=("seelah.committed", "ascended"), forbids=("seelah.closed", "seelah_dead", "seelah_gone"))
ending("apart", '''{n}Seelah and the Commander stopped planning their evenings together. For a time she found herself saving small stories to tell them, then remembering why she no longer should.{/n}
{n}She did not regret every part of what they had shared. In later years she could speak of it without anger, though some memories remained hers alone.{/n}''', requires=("seelah.lovers", "seelah.closed"), forbids=("seelah_dead",))
ending("unfinished", '''{n}Seelah remembered a few evenings she had hoped would become the beginning of something more. The war left little room for discovering whether that hope would survive an ordinary life.{/n}
{n}She kept the memories without making promises on the Commander's behalf. There were still people to help, and roads she had not traveled.{/n}''', requires=("seelah.courting",), forbids=("seelah.committed", "seelah.closed", "seelah_dead", "seelah_gone"))
ending("aeon", '''{n}In a world spared the Worldwound, Seelah had other roads to travel. One evening, resting beside a fire, she moved her belongings to make room and sat for a long time without speaking.{/n}
{n}Nobody came that evening. The space remained until morning. Whatever she carried from the life that might have been, she kept that part of it to herself.{/n}''', requires=("seelah.committed",), forbids=("seelah.closed",), owner="AeonEpilogue")
