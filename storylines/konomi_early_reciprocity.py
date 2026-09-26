"""An optional early encounter and earned personal callbacks at the first supper."""
from copy import deepcopy

from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
CONTACT = "ca2d58c5c65723945857e04fb85d30ce"
ID = "konomi.a_turn_for_herself"

SCENES = [scene(ID, "A turn for herself", "Konomi", 3,
    '"Would you like some company away from your desk?"', [
    n("start", "Konomi", '''"Yes. Though I have a use for you, if you are willing."
{n}Konomi places a small wooden box on her desk. Inside are an ordinary pair of soft shoes, carefully brushed.{/n}
"The people who hosted the reception have lent me their room for an hour. There was a dance I wanted to finish. Somebody began a speech before the second figure."
{n}She closes the box.{/n}
"I know the steps. What I do not have is a partner who will let me enjoy them without asking whom I intend to impress."
{n}Her gaze rests on you, amused and direct.{/n}
"Can you spare a little time? The room will have no audience. You need not arrive with an accomplishment to demonstrate."''',
      c('"I would like that. Show me."', "room"),
      c('"Another time. Keep your hour; I would rather not rush it."', abort=True)),
    n("room", "Narrator", '''{n}When you meet her in the borrowed room, the tables have been pushed against the wall. There is no supper laid out. Konomi has placed her outdoor shoes beneath a chair and opened one shutter for light.{/n}
{n}She crosses the empty floor, turns, and comes back with a small, precise lift of her heel. Her skirt follows the turn without catching. The pleasure on her face appears before she notices you watching.{/n}
"There. That is the part I wanted. A room full of conversation is apt to swallow it."
{n}She marks a rhythm with her fingertips against the chair, then hums a few bars. Without accompaniment, her voice is low and rather practical.{/n}
"The tune repeats. I can supply it, provided you do not expect singing worth paying for. We can stop whenever we wish."
{n}She offers her hand.{/n}''',
      c('"Let me follow you. I spend enough of my day deciding where everyone goes."', "follow"),
      c('"I would enjoy leading. Tell me if I am pulling you where you do not want to go."', "lead"),
      c('"I would rather learn beside you before we hold each other."', "beside")),
    n("follow", "Konomi", '''"Then look at my shoulder, not your feet. I shall tell you when to turn."
{n}She waits for you to settle your hand, adjusts her own, and begins slowly. The first change of direction is so small that you nearly continue straight ahead. She stops before your feet tangle.{/n}
"You need not anticipate me. I am enjoying choosing. Let me have that part."
{n}On the next attempt you wait for the pressure of her hand. She brings you through the turn and smiles with unmistakable satisfaction.{/n}
"Again. This time I should like the whole figure."''',
      c('[Let her set the pace through the next figure.]', "listen", flags=("konomi.dance_followed",))),
    n("lead", "Konomi", '''"I will tell you. You may find that reassuring or rather inconvenient."
{n}She shows you the opening, then places her hand in yours. At your first turn she follows readily. At the second she stops and looks down at the narrowing space between her skirt and the chair.{/n}
"If you want a larger circle, move the chair. Do not make me dance around it while you enjoy the view."
{n}You move it together. This time there is room for the sweep she demonstrated. She follows your lead, then adds the little lift at the end, smiling before she recovers her breath.{/n}
"Yes. That was what I wanted. You may be pleased with yourself."''',
      c('[Offer the next turn without hurrying her through the finish.]', "listen", flags=("konomi.dance_led",))),
    n("beside", "Konomi", '''"Of course. Watch the turn from here. It is easier than watching it approach your feet."
{n}She makes room beside her and demonstrates without touching you. You try the figure in parallel, with a generous gap between you. On the return she takes the turn outward, leaving your space clear.{/n}
"That works rather well. I can see when you are about to go the wrong way."
{n}She is smiling. You repeat the opening, and this time she adds the lift at its end. You can attempt it or keep the plain turn; she gives you time for either.{/n}
"We could keep this version. I wanted company, not a particular arrangement of your hands."''',
      c('[Keep the space between you and repeat the figure together.]', "listen", flags=("konomi.dance_beside",))),
    n("listen", "Konomi", '''{n}A cart rattles past outside, briefly drowning the tune. Konomi stops humming, waits for it to pass, and laughs when its final wheel finds a loose stone.{/n}
"It has no sense of timing."
{n}She reaches the shutter before you do, but pauses with her hand on its edge.{/n}
"Open or closed? We shall lose a little light if I shut it."
{n}The question is ordinary enough. So is her waiting. She has no recommendation prepared for you to defend yourself against.{/n}''',
      c('"Closed. I keep listening for somebody who needs me, even when nobody has called."', "quiet"),
      c('"Leave it open. Ordinary noise makes it easier to believe I am allowed to be here."', "street"),
      c('"Open. I like the light, and I would rather tell you what I enjoy than explain a hurt."', "pleasure")),
    n("quiet", "Konomi", '''{n}She closes the shutter. A thin stripe of daylight remains beneath it.{/n}
"I had a maid once who learned to knock so softly that I never heard her. I thought I wanted silence. What I wanted was to decide when I answered. She could not possibly have guessed that from my instructions."
{n}Konomi leaves the shutter fastened and comes back to you.{/n}
"Nobody has been told to bring us messages here. If you want to finish early, say so. I would rather know than watch you pretend not to hear something."
{n}She begins the rhythm again, quietly, giving you the first few beats before moving.{/n}
"And if you stay, I would like your attention for the turn. I have been looking forward to doing it properly with you."''',
      c('"I can give you this figure. Begin again."', "quiet_end")),
    n("street", "Konomi", '''"Then open it shall be."
{n}She pushes the shutter back against the wall. Somewhere below, two people disagree about where a delivery was meant to go. Neither asks your opinion.{/n}
"I like hearing someone call a name I do not know. It usually means I shall not have to remember what I promised its owner."
{n}Her smile becomes a little rueful.{/n}
"I do enjoy being recognized. I have worked quite hard at it. Occasionally I would prefer to walk into a room without watching people remember why they ought to be pleased."
{n}She comes back to her place on the floor.{/n}
"When you arrived, I was pleased before I had decided what to say. That was agreeable. I should like to become used to it."''',
      c('"I was pleased to find you dancing before you saw me. Keep that part."', "street_end")),
    n("pleasure", "Konomi", '''"Fair. I asked about a shutter, not your most carefully guarded sorrow."
{n}She opens it fully and steps into the light. A few bright threads in her cuff catch the sun as she raises her hand.{/n}
"I like this sleeve. It was expensive. I have received sufficiently many useful compliments on it that I sometimes forget I bought it because I wanted to watch it move."
{n}She turns her wrist, admiring the embroidery without apology.{/n}
"There. Something I enjoy, with no improvement in character attached. Your turn. Tell me something you want more of in an ordinary day."''',
      c('"Play. Something with no prize I have to justify winning."', "play"),
      c('"Beauty. I want to notice it before I start counting what might destroy it."', "beauty")),
    n("play", "Konomi", '''"Then I propose that we put the ending at the beginning and see whether we can get back to where we started."
{n}She tries it first, discovers that the turn has left her facing the wrong wall, and looks over her shoulder at you.{/n}
"You are permitted to laugh. You are also required to suggest the next part."
{n}You choose a step. She follows it, adds one of her own, and soon the borrowed room contains a dance neither of you would recognize outside it. When you finally return to the starting place, Konomi bows with extravagant gravity.{/n}''',
      c('[Return the bow with equal seriousness.]', "finish", flags=("konomi.dance_play",))),
    n("beauty", "Konomi", '''{n}Her hand stills. For a moment you can hear the street more clearly than either of your breathing.{/n}
"Then watch. I should like to be seen enjoying myself."
{n}She gives you the whole figure, taking the space she wanted, the bright cuff circling through the light. You have time to notice the concentration before the turn and the pleasure after it.{/n}
{n}When she returns, she holds out her hand without closing the distance.{/n}
"You may join me, or ask me to do that again. I should be flattered by either."''',
      c('"Again. I want to watch you enjoy it."', "finish", flags=("konomi.dance_beauty",))),
    n("quiet_end", "Narrator", '''{n}This time the rhythm reaches the turn without interruption. Konomi finishes with her chin lifted, visibly pleased. She lets the last note go instead of filling the silence that follows.{/n}
{n}You stay for another figure. Nothing has been solved outside the room, but for these few minutes she has your attention, and you have hers.{/n}''',
      c('[Keep these few minutes free of explanations.]', "finish", flags=("konomi.dance_quiet",))),
    n("street_end", "Narrator", '''{n}She begins before the noise outside has faded. The tune passes in and out of hearing, and you keep its rhythm together when the street briefly swallows it.{/n}
{n}At the end Konomi is laughing. She looks toward the window, then back at you, and starts the opening once more without waiting for the city to become quiet.{/n}''',
      c('[Begin with her while the ordinary city goes on below.]', "finish", flags=("konomi.dance_street",))),
    n("finish", "Konomi", '''{n}You stop before the borrowed hour is over. Konomi sits to change her shoes, leaving the soft pair beside her until their warmth has gone.{/n}
"I shall ask to use the room again. Even if you cannot come."
{n}She looks up with a small smile.{/n}
"But I would rather you could."
{n}When she is ready to leave, she offers you the empty box to hold while she puts the shoes inside. Her fingers brush yours as she takes it back.{/n}
"Thank you. I wanted a partner, and I enjoyed discovering whom I had invited."''',
      c('"So did I. We should keep finding out."')),
], requires=("konomi.present", "konomi.reception"),
    forbids=("konomi.evening", "konomi.lovers", "konomi.dismissed", "inhuman"),
    optional=True, Relationship="konomi", Areas=[DREZEN], Chapters=[3, 5],
    AnswerLists=["0dc8b8604bb33c846a63f3eb62443674"], ContactUnit=CONTACT)]
for item in SCENES:
    for page in item["Nodes"]:
        page["Portrait"] = "Konomi"


def integrate(payload):
    evening = next(s for s in payload["Scenes"] if s["Id"] == "konomi.evening")
    if any(page["Id"] == "remembered_quiet" for page in evening["Nodes"]):
        raise ValueError("Konomi early reciprocity overlay applied twice")
    supper = next(page for page in evening["Nodes"] if page["Id"] == "supper")
    for key, answer, text in (
        ("quiet", '"I liked the quiet you made room for when we danced."', '''"I remember. The shutter here closes properly, and nobody has been asked to bring us messages."
{n}Konomi gets up to fasten it, then returns to her place beside you.{/n}
"Tell me if you want it open. I have no intention of turning one afternoon into an instruction you must live with forever."'''),
        ("street", '"I liked dancing while the city went on outside. Could we open the window?"', '''"Yes. Though if somebody begins singing, I shall expect you to defend your preference."
{n}She opens the window. Voices rise from below, and she pauses to listen before returning to you.{/n}
"There. Nobody seems to require us. I am glad you are here."'''),
        ("play", '"I am still trying to remember the dance we invented."', '''"So am I. I suspect it will have to be invented again."
{n}She taps the opening rhythm against the table, loses it deliberately, and smiles when you notice.{/n}
"We could try after supper. I should like to discover whether the ending remains where we left it."'''),
        ("beauty", '"I have been remembering how pleased you looked when you finished that turn."', '''"I was pleased. With the dance, and with your attention."
{n}She turns toward you, letting you see the pleasure return without finding an excuse for it.{/n}
"Tonight I would like a little more of that attention. You need not invent a useful reason to give it to me."'''),
    ):
        node_id = "remembered_" + key
        supper["Choices"].append(c(answer, node_id, requires=(ID, "konomi.dance_" + key)))
        # Preserve the same intimacy/quiet/transformation options after the callback.
        evening["Nodes"].append(n(node_id, "Konomi", text,
            *deepcopy(supper["Choices"][:4]), portrait="Konomi"))
