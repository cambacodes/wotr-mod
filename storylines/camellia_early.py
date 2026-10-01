"""Camellia's early beats (pacing pass PP2; Writer/handoffs/13-PACING-PASS.md section 2, 2a and 2b).

Path-neutral (N-all): no Trickster gate, no device, no romance promise, and nothing native is set or started. Each beat
sets `camellia.early.<beat>.seen` on its first choice and exactly one outcome flag on every terminal path. Her native
romance (CamelliaRomance 89f8c2f1) has no live state in the Prologue or Chapter 2, so neither beat reads it; neither
beat writes it (pacing lint H3).

- The Prologue (chapter 0), MeetCamelia (c0/CavesUnderKenabres): after she introduces herself (Cue_0008 e6ba2640,
  "Allow me to introduce myself: I am Camellia"), her skirts are "torn and stained with blood, dust, and dirt" (Cue_0006
  ea1fdd24) and "the butchered" man lies at her feet. Canon never says whose blood it is, and neither does the beat: the
  Commander can only see that no wound on her would explain so much of it. Host AnswersList_0009 1ca6cf08 (reached only from
  MeetCamelia's own cues). ReturnToList, because Cue_0008 would replay her introduction (13 errata 2026-09-30).
- Chapter 2, GargoyleAttack/Camelia: "Camellia is hiding behind the cart... she watches the chaos around her with squeamish
  apprehension. The butchered corpse of a crusader lies at her feet." (Cue_0001 872dbbcc). Host AnswersList_0002
  f40abd19 (reached only from that dialog). ReturnToList, because Cue_0001 would replay the first sighting.

Voice anchors (enGB, hers): "Really? I'm so ever glad to hear it..." (MeetCamelia/Cue_0008 e6ba2640); "...we've seen how
powerless they truly are." (Cue_0013 90bddeeb, "with ruthless precision"); "Henceforth we shall have no one but ourselves
to rely on, I suppose?" (Cue_0013); "I am. But our army... It's an even sadder spectacle than usual." (GargoyleAttack/
Camelia/Cue_0006 3dc95933). Courtesy laid over appetite; the fear is a performance she can drop.

Consequence: camellia_masks' Two lies and a truth (Chapter 3, her first Trickster courtship scene) opens with what she
remembers of each: the Commander who asked about the blood is tested first, and the one who shielded her or watched her
at the cart is named for it.
"""
from story_format import c, n, scene
from storylines.camellia_trickster import CLOSED, GONE, REL, SCENES, UNIT, nar

PROLOGUE_LIST = "1ca6cf08fceeac141a0df689cecc784a"   # MeetCamelia/AnswersList_0009
CART_LIST = "f40abd195a8b1ea46945b47576fa732a"       # GargoyleAttack/Camelia/AnswersList_0002

BLOOD = "camellia.early.blood"
BLOOD_SEEN = BLOOD + ".seen"
BLOOD_ASKED = BLOOD + ".asked"       # the Commander said it aloud: the blood is not hers
BLOOD_KEPT = BLOOD + ".kept"         # the Commander kept it, and she decided they had missed it
CART = "camellia.early.cart"
CART_SEEN = CART + ".seen"
CART_SHIELD = CART + ".shield"       # the Commander put themself between her and the gargoyle
CART_WATCH = CART + ".watch"         # the Commander stood still and watched what she would do

PATH_FIT = {BLOOD: "N-all", CART: "N-all"}


def cam(id, text, *choices):
    """Camellia inside her own native dialog: a ReturnToList cue names her unit (Camelia_Companion, the speaker of
    MeetCamelia/Cue_0008 and GargoyleAttack/Camelia/Cue_0001), or it would be narrated."""
    return n(id, "Camellia", text, *choices, portrait="Camellia", speaker_unit=UNIT)


# --- The Prologue: the blood on her skirts. ------------------------------------------------------------------------------

SCENES.append(scene(BLOOD, "The blood on her skirts", "Camellia", 0, "[Look more closely at her skirts]", [
    nar("start", '''{n}The stains on her skirts are not dust. They are blood, a great deal of it, thickest at the hem and thinning toward the knee. There is no wound on her that you can see that would explain so much of it. At her feet the dead man lies with his eyes open.{/n}
{n}She sees where you are looking. Her hand stays exactly where it was, on the hilt of her rapier.{/n}''',
        c('"None of that blood is yours."', "asked", flags=(BLOOD_SEEN,)),
        c("[Say nothing, and look back at her face]", "kept", flags=(BLOOD_SEEN,))),
    cam("asked", '''"How observant." {n}She glances down at her skirts as though somebody had spilled wine on them at a party, and she were too well bred to mention it.{/n} "The square was very... crowded, at the end. Everyone was running, and some of them were running with rather less of themselves than they started with. One cannot choose whom one stands beside in a massacre."
{n}Her smile is perfect. It does not reach her eyes, and she does not try to make it.{/n} "You must forgive me. I am not used to being looked at so closely by strangers. I shall have to get used to it, I suppose."''',
        c("[Let it go, for now]", flags=(BLOOD_ASKED,))),
    nar("kept", '''{n}You say nothing. Camellia's eyes go from her skirts to your face and rest there a moment, measuring, the way a woman at a draper's measures a length of cloth against the light. You give her nothing to measure.{/n}
{n}She seems satisfied. She turns to Seelah with a small, brave smile, as though you had been looking at the cave wall all along.{/n}''',
        c("[Let it go, for now]", flags=(BLOOD_KEPT,))),
], forbids=(CLOSED, *GONE, BLOOD_ASKED, BLOOD_KEPT, BLOOD_SEEN), last=0, Relationship=REL, Chapters=[0],
    AnswerLists=[PROLOGUE_LIST], ReturnToList=True,
    ReturnText="{n}Camellia smooths her torn skirts and waits, perfectly composed.{/n}"))


# --- Chapter 2: the cart, when the gargoyles came. ------------------------------------------------------------------------

SCENES.append(scene(CART, "Behind the cart", "Camellia", 2, "[Look up: one of the gargoyles has turned back toward the cart]", [
    nar("start", '''{n}One of the gargoyles has seen her. It banks over the burning tents and comes back low, wings folded, straight at the cart. Camellia shrinks against the wheel with a hand pressed to her mouth, the very picture of a frightened girl. Her other hand, the one in the shadow of her skirts, has found the hilt of her rapier.{/n}''',
        c("[Step in front of her]", "shield", flags=(CART_SEEN,)),
        c("[Stay where you are, and watch what she does]", "watch", flags=(CART_SEEN,))),
    nar("shield", '''{n}You step between her and the open square. The gargoyle sees steel where it expected a girl, pulls up short of the cart with a shriek like a dragged slate, and wheels away to look for easier meat among the tents.{/n}''',
        c("Continue", "shield_her")),
    cam("shield_her", '''"How gallant." {n}Her hand is on your sleeve. She takes it away, one finger at a time, and smooths her skirts.{/n} "Now, if you would be so kind as to see to the rest of your army, my friend. They seem to need you a great deal more than I do."''',
        c("[Let her keep her performance]", flags=(CART_SHIELD,))),
    nar("watch", '''{n}You don't move. The gargoyle comes in over the cart with its claws out, and Camellia stops trembling. Her rapier takes it through the stretched skin of one wing, a single neat thrust, and it lurches aside into the tents, shrieking, and does not come back.{/n}
{n}When she turns to you, her hand is at her mouth again.{/n}''',
        c("Continue", "watch_her")),
    cam("watch_her", '''"You were very patient, my friend." {n}She looks at you over her fingers. Her eyes are perfectly dry.{/n} "I trust you will be quicker when the next one comes. I might not be so lucky twice."''',
        c("[Let her keep her performance]", flags=(CART_WATCH,))),
], forbids=(CLOSED, *GONE, CART_SHIELD, CART_WATCH, CART_SEEN), last=2, Relationship=REL, Chapters=[2],
    AnswerLists=[CART_LIST], ReturnToList=True,
    ReturnText="{n}Camellia straightens her gloves and looks out over the burning camp, waiting for your orders.{/n}"))
