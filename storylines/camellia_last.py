"""Camellia: the language of flowers, and the eve of the Threshold (camellia_trickster and its sibling modules).

Her pressed flowers are canon (Camelia/Cue_0071, the flower she is named for; the dried flowers she keeps, as other routes
also show her). The flower language she learned from her Varisian teacher is her own telling, and she says so.
"""
from story_format import c
from storylines.camellia_trickster import COMMITTED, NOT_TODAY, P, RET, SCENES, cam, met
from storylines.camellia_masks import TWO_LIES, living

FLOWERS = P + "day.the_language_of_flowers"
EVE = P + "day.the_eve"


# --- Before the kill: the language of flowers. -------------------------------------------------------------------------

living(FLOWERS, "The language of flowers", '"Did you leave a flower on my pillow?"', [
    cam("open", '''"Three. Did you only find one?" {n}Camellia looks up from her herbarium, a heavy book of pressed stems, with an expression of mild reproach.{/n} "There was a violet under your pillow and a sprig of rue in your boot. You must look properly, my friend. I went to a great deal of trouble."''',
        c('"What do they mean?"', "mean")),
    cam("mean", '''"Oh, everything means something, if you decide it does. My father's maids used to send each other bunches of flowers that meant things and giggle, so I made up a language of my own, a much more useful one." {n}She turns a page. A pressed foxglove, very purple.{/n}
"In mine, the violet means faithfulness. The rue means regret. And the one on your pillow..." {n}She smiles.{/n} "Well. You tell me what it was."''',
        c('"A white rose."', "rose"),
        c('"Something with berries on it."', "berries"),
        c('[Trickster] "It was a lily. The white kind. For a wedding."', "lily")),
    cam("rose", '''"A white rose means 'I am worthy of you.'" {n}She says it primly, like a governess.{/n} "Which is a lie, of course. Nobody is ever worthy of anybody. But it's a very pretty lie, and it's the one people most like to be told." {n}She closes the herbarium.{/n} "I left it because I thought you'd like to hear it. From someone who knows exactly how much it's worth."''',
        c("Continue", "yours")),
    cam("berries", '''"Nightshade." {n}She is delighted.{/n} "It means 'I am a dangerous companion.' My teacher said you should only ever send it to someone who already knows. It isn't a warning, you see. It's a compliment. It means 'I trust you to have noticed.'"
{n}She tilts her head.{/n} "You didn't eat it, I hope. It would spoil the whole message."''',
        c("Continue", "yours")),
    cam("lily", '''{n}She looks at you for a moment without any expression at all. Then she laughs, and it is the startled laugh of someone who has been answered in her own language.{/n}
"A lily. For a wedding. I didn't leave a lily, you liar." {n}She presses her hand flat on the herbarium.{/n} "But you wanted me to have. You made it up, and now it's in my head, a white lily on your pillow, and I shall have to go and find one and put it there, so that it's true."''',
        c("Continue", "yours")),
    cam("yours", '''"Now you." {n}She pushes the herbarium across to you.{/n} "Choose one. Any one. Don't tell me what it means. I'll know."''',
        c("[Choose the foxglove]", "foxglove"),
        c("[Choose a sprig of forget-me-not]", "forget"),
        c("[Close the book without choosing]", "none")),
    cam("foxglove", '''"Foxglove. 'Insincerity.'" {n}She smiles slowly.{/n} "You chose the flower for liars. For me, or for you? No, don't answer. It's better if I never know which of us you meant."''',
        c("Continue", "close")),
    cam("forget", '''{n}She looks at the little blue flower for a long time before she says anything.{/n}
"Forget-me-not." {n}Her voice is very soft.{/n} "It means exactly what it says. It's the only flower that does. It's the only honest thing in the whole book." {n}She takes it out of the page with great care and tucks it into the lace at her throat, beside the amulet.{/n} "I shan't. I never forget anyone. Ask anybody who ever knew me."''',
        c("Continue", "close")),
    cam("none", '''"No flower." {n}She regards the closed book.{/n} "That's a message too, you know. In the old language, an empty hand means 'I have nothing to say that you do not already know.'" {n}She draws the herbarium back into her lap.{/n} "It's either very romantic or very rude. My teacher said it depended entirely on the face."''',
        c("Continue", "close")),
    cam("close", '''"Look under your pillow tonight," {n}she says, as you go.{/n} "Look properly. I'll have thought of something new by then. I'm always thinking of something new." {n}She turns back to her pressed stems.{/n} "It's the only thing I do with my hands that nobody minds."''',
        c("[Go]")),
], requires=(TWO_LIES,), delay=48)


# --- After her answer: the eve of the Threshold. -----------------------------------------------------------------------

met(EVE, "The eve", '"Tomorrow we march on the Threshold."', [
    cam("open", '''"I know. The whole citadel is praying. I can hear them through the floor, like mice." {n}She is sitting on the end of your bed with her knife across her knees, polishing it, very slowly, with a square of silk.{/n} "I've never been to a battle where everyone expected to die. It's rather beautiful. Everyone is being so kind to everyone else."''',
        c("Continue", "ask")),
    cam("ask", '''"May I ask you something, my friend? I've never asked anyone this before, because nobody I asked it of ever lived long enough to answer." {n}She holds the blade up to the lamp, and turns it.{/n} "If you die tomorrow, will you do it convincingly?"''',
        c('"I don\'t intend to die."', "intend"),
        c('[Trickster] "No. I\'ll do it so badly you\'ll have to come and tell me I\'m overacting."', "badly"),
        c('"If I do, I want your face to be the last thing I see."', "face")),
    cam("intend", '''"Good." {n}She puts down the silk.{/n} "Then don't." {n}Somewhere below, a sergeant is shouting the names of a watch roster, and a horse is refusing a cart. She listens to both for a moment.{/n}''',
        c("Continue", "intend_dead", requires=(RET,)),
        c("Continue", "close", forbids=(RET,))),
    cam("intend_dead", '''"I did it once. I didn't care for the lying still. You'd hate it. You fidget."''',
        c("Continue", "close")),
    cam("badly", '''{n}For a moment she simply stares. Then she drops the knife on the blanket and laughs until she has to wipe her eyes on the corner of the silk.{/n}
"You would. You'd lie there on the Threshold with your mouth open and your eyes rolled up like a bad actor in a provincial farce, just to make me come and fetch you." {n}She shakes her head.{/n} "And I would. I'd walk into whatever's left of the Abyss and tell your corpse it was an embarrassment. You've ruined dying for me forever. I hope you're pleased."''',
        c("Continue", "close")),
    cam("face", '''{n}Her hand stops on the blade.{/n}
"My face." {n}She says it very quietly.{/n} "You want to see my face. At the end." {n}She looks down at the knife in her lap, and then back up at you, and her eyes are enormous and bright and quite dry.{/n}
"That's what I've always wanted. The other way round. And you'd give it to me for nothing, as a gift, as if it were a flower." {n}She puts the knife away, into its sheath, carefully, all the way home.{/n} "Then you'd better not die tomorrow. I'm not ready for that. I want to be so much better at it first."''',
        c("Continue", "close")),
    cam("close", '''"Go to sleep. I'll sit up." {n}She takes the lamp to the window, and sits with her back to the wall and her knife across her knees, facing the door.{/n} "Nothing is going to kill you in your sleep tonight, darling. I've made quite sure of that. I'm the only one in this city with the right."''',
        c("[Sleep]")),
], requires=("trickster.ever", COMMITTED, NOT_TODAY), delay=48, optional=True, living=())
# Q8 (Sol CAN): the eve is the eve. Chapter 5 only, and only once Iz is done and the march on the Threshold is next.
for _s in SCENES:
    if _s["Id"] in (EVE, EVE + "_camp", EVE + "_alive"):
        _s["MinChapter"], _s["Chapters"] = 5, [5]
        _s["Requires"] = list(dict.fromkeys([*_s["Requires"], "iz.done"]))

from storylines.camellia_trickster import city  # noqa: E402 (Q8)
city(EVE)
