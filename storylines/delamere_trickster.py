"""Delamere on the Trickster path: "Be the stag" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, binding; spec
Writer/handoffs/trickster/delamere.md for canon and hooks only: its backwards rite and god-priced raise are dropped).

Canon (blueprints.zip / enGB):
- Kyado, prior of her temple: "a white stag emerged from the forest and spoke to her in a human voice, telling her that she
  should hunt it... Delamere tracked that stag for three days and three nights... she made its antlers into a bow and its
  hide into armor" (Kyado_main_dialogue/Cue_0039 0a935738); her rule of fifty-three souls to a village (Cue_0038 67995417);
  cities corrupt the soul (Cue_0034 91cf4db8). Kyado keeps Rathimus's scrolls and reads foreign scripts (Cue_0020 a97f6700).
- Her own words (DelamereInTomb): the stag hunt "Three daysss we vied with each other in ssstealth and ssspeed... I did not
  eat the meat, but inssstead I offered it up to Erasssstil" (Cue_0034); "I wasss known... Feared... Ressspected...
  Loved..." (Cue_0032); undeath is "an abomination... A betrayal by Erassstil" (Cue_0040 50a96c40).
- The tomb: "I guard the eternal sleep of Delamere. Cursed be any who dare to destroy me." (TombOfDelamere_BookEvent/
  Cue_0019 0120467b). The invisible archer: taking her relics from a forced tomb, the Commander is "pierced by twenty-five
  inches of sturdy wood" and hears a hunting horn in the distance (Cue_0052 d8bed82b); closing the lid, "the sound of a
  taut bowstring being relaxed - as if the invisible archer... has decided not to let the arrow fly" (Cue_0054 15a598ea).
  Erastil answers at the seal with "A stag bellows in the distance" (Cue_0067 a58f2095, natively for his worshippers).
- Zanedra's cult used the sarcophagus as a feasting table (Cue_0002 8aeb58dc) and killed a peasant lad in the crypt
  (ZanedraInTemple); Kyado let them in under her rat curse (Kyado_main_dialogue/Cue_0057 5c11e73b).

The device, "Be the stag" (11 §1 hunt lure): with Kyado's crypt access (his key after the initiation, Cue_0094 062f826d,
or the visited tomb), the Commander sounds a stag's roar on the Kellid horn hung over her sarcophagus (Lore (Nature)).
Her soul, still at full draw on the hunt it never finished, answers her own vow and wakes her to chase; the Commander
runs as quarry (Mobility). Her arrow ends the first chase. The Commander keeps the limp for good; she keeps the right to
finish the hunt. This is a waking, not undeath and not a raise: no negative energy, no binding, no priced god. The Lich
raise (DelamereResurrected c0fd47d7, Lich-only) is a different thing, and she says so herself.

Authored, and labelled as authored: the horn over her sarcophagus and the Kellid line at its foot ("She fell on the
hunt. The hunt did not fall with her. When the stag calls, she answers."), her death on an unfinished hunt, the yew
grave-bow, the Drezen side chapel that holds her remains after the crusade project (DelameresRemains 4473ff54;
"her new resting place", Cue_0057 4a58ea06), and everything she says awake.

Delivery. Her only native units (TempleOfDelamere/Delamere 433b2850 and the Lich companion) share the undead prefab and
portrait, so nothing is spawned for her: the Ch3 beats with Kyado alive are physical on his temple list (AnswersList_0005
d7aadaa2; host_reason: he is prior of her temple and keeper of the crypt; he speaks in the scene), and the rest are
rest-delivered visits (she comes to the Commander) with her portrait key. Kyado's Drezen stall exists only on the Angel
path (Cue_0059_AngelReinf -> ZanedraKilledByKyado -> Cue_0085 starts KyadoTraderInDrezen), so no Trickster run has it.
The courtship is delamere_woods.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
P = "delamere.trickster."
KYADO_HUB = "d7aadaa261a8023489bdba49216cc334"     # Kyado_main_dialogue/AnswersList_0005 (the temple root list)
KYADO_RETURN = "5230d5fd7201db04287903ac6a95d30c"  # Kyado_main_dialogue/Cue_0036 "It was my pleasure to be of service, Commander."
ULBRIG_HUB = "0a50c9c878844ed4a69b8d6131304c5e"    # DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"    # CompanionDialogues/Woljif/AnswersList_0003
BOW_ITEM = "5fd95b425dd0b73488554abcb68382d3"      # DelameresBowItem (her antler bow, taken from the tomb: Cue_0056)
CURSED_BOW_ITEM = "15acf7ada5903ec429f7cd62a6162613"  # CursedDelameresBowItem (taken from a forced tomb: Cue_0052)

STARTED = "delamere.started"
CLOSED = "delamere.closed"
COMMITTED = "delamere.committed"
TOMB_VISITED = "delamere.tomb_visited"             # StartedDialogs TombOfDelamere_BookEvent (trickster_world)
REMAINS = "delamere.remains_finished"              # Etude DelameresRemainsFinished (trickster_world)
CRYPT_KNOWN = "delamere.crypt_known"               # Derived: kyado.initiated or kyado.crypt_door_seen (trickster_world)
INITIATED = "kyado.initiated"                      # SeenCue Cue_0094_TrickReinf (ledger 05 row 7)
KYADO_DEAD = "kyado.dead"                          # UnlockableFlag KyadoDead
RELICS_TAKEN = "delamere.relics_taken"             # UnlockableFlag GotDelamereLoot (Cue_0052 / Cue_0056 OnStop)
RELICS_CURSED = "delamere.relics_taken_forced"     # SelectedAnswers TombOfDelamere/Answer_0048 (the forced tomb's relics)
BOW_HELD = "delamere.bow_held"                     # InventoryItems DelameresBowItem
CURSED_BOW_HELD = "delamere.cursed_bow_held"       # InventoryItems CursedDelameresBowItem

RETURNED = P + "returned"
DECLINED = P + "declined"
HORN_LORE = P + "primed"                      # Kyado's lore: the white stag's roar
RAN_FAR = P + "ran_far"
RAN_SHORT = P + "ran_short"
LIMP = P + "cost.limp"
HUNT_OWED = P + "cost.hunt_owed"
BOW_RETURNED = P + "bow_returned"
YEW_BOW = P + "yew_bow"
WOKE_KYADO = P + "woke_with_kyado"
WOKE_ALONE = P + "woke_alone"
WOKE_DREZEN = P + "woke_in_drezen"
SAID_AGAIN = P + "stag_said_again"
SAID_MISSED = P + "stag_said_missed"
SAID_FINISH = P + "stag_said_finish"
# The courtship (delamere_woods) sets these; the epilogues and reactions read them.
SECOND_HUNT = P + "second_hunt_offered"
CAUGHT = P + "caught"
LATE_COMMITTED = P + "late_committed"
DERIVED = {
    # R2-6: she has proposed the second hunt; if the war ends first, the epilogue carries her yes (Last Call, household).
    LATE_COMMITTED: [["trickster.ever", SECOND_HUNT]],
    # 05 §2.1: eligibility ("delamere.harem.eligible") is derived by household.py from PARTNERS (committed or late).
    # 05 §2.5 voice note: a household is a village she can count (fifty-three, everyone known by name), never a city.
    "delamere.harem.voice.a_village_not_a_city": [[COMMITTED], [LATE_COMMITTED]],
}
BINDINGS = {
    "UnlockableFlags": {RELICS_TAKEN: "3de8e7db06d4b9043bddfa77888ecfa5"},     # GotDelamereLoot
    "SelectedAnswers": {RELICS_CURSED: "3357022e6d1c5e047a0075a223606210"},    # TombOfDelamere_BookEvent/Answer_0048
    "InventoryItems": {BOW_HELD: BOW_ITEM, CURSED_BOW_HELD: CURSED_BOW_ITEM},
}

RELATIONSHIP = dict(
    Title="The Stag's Hunt",
    Description=("Delamere the Blessed slept under her temple for centuries with an arrow on the string. I blew a horn "
                 "over her and ran. She caught me, and I still walk crooked from it. The hunt, she says, is not finished."),
    Objective="Stay ahead of Delamere",
    Guidance=("On the Trickster path, ask Kyado at the Temple of Delamere what hangs over her sarcophagus, then go down "
              "to her with him. If he is dead, or later in the war, or if her remains were taken to Drezen, the horn can "
              "still be sounded. After she wakes she finds you herself, a day or so apart; she does not come on command."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[], FailureFlags=[],
    TricksterAccess={
        "crypt": dict(detect=[TOMB_VISITED], device=P + "crypt.stag", returned=RETURNED),
        "unvisited": dict(detect=[INITIATED], device=P + "crypt.stag", returned=RETURNED),
        "drezen": dict(detect=[REMAINS], device=P + "drezen.stag", returned=RETURNED),
    },
)


def dl(id, text, *choices, **kw):
    """Delamere speaking. Inline, the line is narrated (her native portrait is the undead one); on a page, her portrait."""
    return n(id, "Delamere", text, *choices, portrait="Delamere", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Delamere", **kw)


def kyado(id, text, *choices):
    """Kyado, speaking inline in his own temple dialog (the native conversant)."""
    return n(id, "conversant", text, *choices)


def temple(id, title, entry, nodes, requires, forbids=(), delay=0, into=None, **extra):
    """A physical Chapter 3 scene on Kyado's temple list, returning to it. He must be alive and prior."""
    (SCENES if into is None else into).append(scene(
        id, title, "Delamere", 3, entry, nodes, requires=requires, forbids=(KYADO_DEAD, *forbids), delay=delay, last=3,
        Relationship="delamere", Chapters=[3], AnswerLists=[KYADO_HUB], NativeReturnCue=KYADO_RETURN, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=0, chapters=(3, 5), kind="visit", into=None, **extra):
    """A rest-delivered page: she comes to the Commander (visit), or a letter she sends (letter)."""
    (SCENES if into is None else into).append(scene(
        id, title, "Delamere", min(chapters), "", nodes, requires=requires, forbids=forbids, delay=delay,
        last=max(chapters), Relationship="delamere", Chapters=sorted(set(chapters)), Remote=True, Kind=kind, **extra))


# --- The primer (physical, Chapter 3): what hangs over her, and what is cut at her feet -----------------------------
# Directive 9 foresight: the lore makes the roar easier to sound (Lore (Nature) DC 18 instead of 26).

temple(P + "temple.horn_lore", "What hangs over her", '"Is there anything in the crypt I should know about?"', [
    kyado("horn", '''{n}Kyado glances at the flagstones as if he could see through them.{/n} "There's a horn. Over her. On an iron peg in the wall above her head, where you'd hang a lamp. Aurochs horn, very old, with a stag cut into the side of it."
{n}He rubs at a callus on his thumb.{/n} "Rathimus said the Kellid priests hung it there when they closed her in. He said nobody was ever to blow it. Not pilgrims. Not priors. Nobody."''',
        c('"Why not?"', "feet")),
    kyado("feet", '''"Because of the words at her feet. There are words cut all round the stone; most of them are the seal. But at the foot there's one line on its own, in old Kellid. Rathimus copied it out, and I've been trying to read it since I came here." {n}He colours.{/n} "I read foreign scrolls, you know. Slowly.
"It says: 'She fell on the hunt. The hunt did not fall with her.' And under that, smaller, as if the carver was afraid of it: 'When the stag calls, she answers.'"''',
        c("Continue", "felt", requires=(RELICS_CURSED,)),
        c("Continue", "arrow", forbids=(RELICS_CURSED,))),
    kyado("felt", '''{n}He looks at your chest, and then quickly away.{/n} "You felt it, didn't you. When you took her things out of the broken stone. The arrow that isn't there." {n}He swallows.{/n} "Pilgrims used to say they felt it too, if they touched her bow. Here, under the breastbone."''',
        c("Continue", "aiming")),
    kyado("arrow", '''"Pilgrims used to say that if you touched her bow you felt an arrow go into you. Here." {n}He touches his breastbone.{/n} "There isn't any arrow. I've looked."''',
        c("Continue", "aiming")),
    kyado("aiming", '''"I think... I think she's still aiming at something, Commander. I think she's been aiming at it since before there was a Worldwound, and she can't let go of the string."''',
        c('"What does a stag\'s call sound like? The kind she would answer."', "roar"),
        c('"Then I\'ll leave the horn on its peg."')),
    kyado("roar", '''"A white stag, it would have been. The one Erastil sent her." {n}Then, because he is a shepherd's son and cannot help answering a question about animals properly:{/n} "They don't bugle, whatever the songs say. In autumn they roar. Three or four short barks from the belly, and then one long one that breaks in the middle, like something being dragged up out of the ground. My father's sheep used to bolt every time one called in the hills."
{n}He stops. He has understood the question a moment too late.{/n} "Why do you want to know what it sounds like?"''',
        c("[Smile at him.]", "please", flags=(HORN_LORE,)),
        c('"Idle curiosity."', "please", flags=(HORN_LORE,))),
    kyado("please", '''"Commander. P-please." {n}His voice goes up and does not come back down.{/n} "Whatever you're thinking, it's the kind of thing Rathimus would have written me a very long letter about."''',
        c('"Then it\'s lucky he isn\'t here to write it."')),
], requires=("trickster",), forbids=(HORN_LORE, RETURNED, DECLINED, REMAINS), RequiresAnyGroups=[[TOMB_VISITED, INITIATED]],
    TricksterDevice=True, TricksterState="crypt")


# --- The waking: one script in three places ----------------------------------------------------------------------------
# Physical in the crypt with Kyado (Chapter 3); a page in the crypt without him (Kyado dead in Chapter 3, or Chapter 5);
# a page in the Drezen side chapel where the crusade laid her remains. Flags live on choices only.

PLACES = {
    "kyado": dict(
        open=kyado("start", '''"Down? T-to her? Now?" {n}Kyado takes the lamp off its hook and holds it in both hands, as if someone might take it away from him.{/n} "I'll come. It's my temple. I'm the prior." {n}He does not sound as if he believes the last part.{/n} "I'll come as far as the bottom step."''',
            c("Continue", "stair")),
        stair='''{n}The crypt still smells of the lye Kyado scrubbed it with, and under the lye, faintly, of the feasts it hosted before. His lamp makes the carved stag on the far wall jump and settle. He stops on the bottom step, exactly as he said he would.{/n}''',
        run_far='''{n}You take the crypt stair three at a time. Behind you Kyado shrieks and drops the lamp, and the dark comes up the stairwell after you like water. Through the temple, past the altar, out of the door and into the woods below the hill, and you are already doing the things a hunted thing does: doubling back through the stream, going up the far bank on stone, breaking a false trail through the bracken and leaving it for her to find.{/n}
{n}She finds every one of them and does not stop for any. You never hear her. You hear the woods go quiet in a line behind you, which is worse.{/n}''',
        run_short='''{n}You make the stair. You make the temple floor, and the door, and the cold night air, and three long strides across the yard toward the trees, with Kyado's shriek still ringing down in the crypt behind you.{/n}
{n}Three strides is what a stag gets, from a hunter who has waited this long.{/n}''',
        after=kyado("after", '''{n}Kyado comes out of the dark with the relit lamp held high and a roll of bandage clenched in his teeth. He takes one look at the woman kneeling over you, and his knees go.{/n} "She's... she's breathing. Erastil. Erastil, is it... is it the l-lich thing? The death thing? Commander, tell me you d-didn't..."''',
            c("Continue", "not_grave")),
        not_grave=dl("not_grave", '''{n}She turns her head and looks at him. He stops talking.{/n} "Do I stink of the grave, boy?" {n}Her voice is a dry scrape, a door that has not been opened in a long time.{/n} "Smell me. Go on. I stink of dust and a long sleep, and I am hungry enough to eat that lamp. The dead do not get hungry. Bring me the bandage, and then bring me bread."''',
            c("Continue", "cut")),
    ),
    "alone": dict(
        open=nar("start", '''{n}The temple is quiet when you come to it, and nobody stops you on the crypt stair.{/n}''',
            c("Continue", "stair")),
        stair='''{n}You go down alone with a lantern. Kyado's broom still leans at the bottom of the stair where he left it. Nobody has used it since. The carved stag on the far wall jumps in your light and settles.{/n}''',
        run_far='''{n}You take the crypt stair three at a time with the dark coming up after you like water. Through the empty temple, past the altar, out of the door and into the woods below the hill, and you are already doing the things a hunted thing does: doubling back through the stream, going up the far bank on stone, breaking a false trail through the bracken and leaving it for her to find.{/n}
{n}She finds every one and does not stop for any. You never hear her. You hear the woods go quiet in a line behind you, which is worse.{/n}''',
        run_short='''{n}You make the stair. You make the temple floor, and the door, and the cold night air, and three long strides across the yard toward the trees.{/n}
{n}Three strides is what a stag gets, from a hunter who has waited this long.{/n}''',
        after=nar("after", '''{n}There is nobody to bring a lamp. She lights nothing, needs nothing; she sees you in the dark the way she saw you on the stair. When she speaks again her voice is a dry scrape, a door that has not been opened in a long time.{/n}''',
            c("Continue", "not_grave")),
        not_grave=dl("not_grave", '''"You are wondering whether I am one of the dead that walk. I can hear you wondering." {n}She leans down until you can smell her: dust, cold stone, old leather, and under it, faint and rising, the warm salt smell of a living body.{/n} "The dead do not get hungry, and I could eat a horse, hooves and all. The dead do not bleed, either. Lie flat. This will hurt you more than it hurts me."''',
            c("Continue", "cut")),
    ),
    "drezen": dict(
        open=nar("start", '''{n}The side chapel where the crusade laid her is empty at this hour. Pilgrims come by day and leave her things: a sprig of fir, a snared hare, a child's carved deer. At night there is only the watch on the street outside, and one candle, and her.{/n}''',
            c("Continue", "stair")),
        stair='''{n}The masons who carried her up from the temple brought everything that was in the crypt with her, because nobody told them not to: the sarcophagus, its seal, and the old horn from its peg, which they hung above her head again out of plain country tidiness.{/n}''',
        run_far='''{n}You take the chapel door with your shoulder and the street with your feet. Through the lower town, over the fish-market barrows, up the tanners' stair and across the roofs, and you are already doing the things a hunted thing does: doubling through alleys, going to ground in a cart of fleeces, dropping over the curtain wall where the stones are rotten and running for the black line of the hills.{/n}
{n}She comes over the wall a heartbeat behind you. She has never seen a city in her life, and she takes this one the way she would take a thicket: straight through, and without once looking at it.{/n}''',
        run_short='''{n}You make the chapel door. You make the street, and the cold night air, and three long strides toward the corner, with a night-watchman's lantern swinging round to find you.{/n}
{n}Three strides is what a stag gets, from a hunter who has waited this long.{/n}''',
        after=nar("after", '''{n}The watchman's lantern arrives, and the watchman behind it, and he takes in the arrow and the woman with the knife and very sensibly goes to fetch someone else.{/n}''',
            c("Continue", "not_grave")),
        not_grave=dl("not_grave", '''"You are wondering whether I am one of the dead that walk. I can hear you wondering." {n}She lifts her head and sniffs the air of the street: smoke, dung, cabbage, ten thousand people. Her lip curls.{/n} "The dead do not get hungry, and they do not smell a city and want to be sick. I am both. Lie flat. This will hurt you more than it hurts me."''',
            c("Continue", "cut")),
    ),
}

# Chapter 5, when nobody knows where Kyado is: the same crypt, after the war has been through it.
PLACES["late"] = dict(PLACES["alone"],
    open=nar("start", '''{n}The war has been through the Temple of Delamere and gone. The doors stand open. Somebody has stabled horses in the nave and left again; somebody else has left an offering of three withered turnips on the altar, which can only have been one person.{/n}''',
        c("Continue", "stair")),
    stair='''{n}You go down the crypt stair alone, with a lantern. Kyado's broom leans at the bottom where he left it; dust has had a long time to settle on the handle. The carved stag on the far wall jumps in your light and settles.{/n}''')


def waking(place):
    """The waking as nodes for one place. Only the Kyado place has conversant lines; the others are pages."""
    t = PLACES[place]
    crypt = place != "drezen"
    nodes = [t["open"], nar("stair", t["stair"], c("Continue", "body_open", requires=(TOMB_VISITED,)),
                            c("Continue", "body_sealed", forbids=(TOMB_VISITED,)))]
    if not crypt:
        nodes[1] = nar("stair", t["stair"], c("Continue", "body_drezen"))
        nodes.append(nar("body_drezen", '''{n}She lies as the crusade laid her, on her back, with the lid set aside so the pilgrims can see her face. A tall woman gone to leather and bone, a dark mane of hair spread on the stone, the stag-hide breastplate laced over her ribs and the antler bow still locked in her hands.{/n}''',
                         c("Continue", "horn")))
    crypt_nodes = [
        nar("body_open", '''{n}The lid stands aside where you left it. She lies as you last saw her: a tall woman gone to leather and bone, a dark mane of hair spread on the stone, the stag-hide breastplate laced over her ribs. Above her head the horn hangs on its iron peg, exactly where it has hung since the Kellids closed her in.{/n}''',
            c("Continue", "in_hands", forbids=(RELICS_TAKEN,)),
            c("Continue", "given_back", requires=(RELICS_TAKEN, BOW_RETURNED)),
            c("Continue", "taken_held", requires=(RELICS_TAKEN, BOW_HELD), forbids=(BOW_RETURNED,)),
            c("Continue", "taken_cursed", requires=(RELICS_TAKEN, CURSED_BOW_HELD), forbids=(BOW_RETURNED, BOW_HELD)),
            c("Continue", "taken_gone", requires=(RELICS_TAKEN,), forbids=(BOW_RETURNED, BOW_HELD, CURSED_BOW_HELD))),
        nar("body_sealed", '''{n}The lid has never been moved. The seal sits whole in the middle of it, a ring of Kellid words around a ring of stone: "I guard the eternal sleep of Delamere. Cursed be any who dare to destroy me."{/n}
{n}You have no intention of destroying anything. You only mean to make a noise near it. Above the sarcophagus, on its iron peg, hangs the horn.{/n}''',
            c("Continue", "horn")),
        nar("in_hands", '''{n}Her hands are still closed on the antler bow.{/n}''', c("Continue", "horn")),
        nar("given_back", '''{n}Her hands are closed on the antler bow again, where you laid it.{/n}''', c("Continue", "horn")),
        nar("taken_held", '''{n}Her hands are closed on nothing. Her bow is on your back, where it has been since you lifted it out of her grip, and it has never once felt as if it belonged there.{/n}''',
            c("[Lay her bow back in her hands.]", "given_now", requires=(BOW_HELD,), remove_item=BOW_ITEM, flags=(BOW_RETURNED,)),
            c("[Keep it where it is.]", "yew", flags=(YEW_BOW,))),
        nar("taken_cursed", '''{n}Her hands are closed on nothing. Her bow is on your back, where it has been since you lifted it out of the broken stone, and every day since it has pulled at you like a dog that wants to go home.{/n}''',
            c("[Lay her bow back in her hands.]", "given_now", requires=(CURSED_BOW_HELD,), remove_item=CURSED_BOW_ITEM, flags=(BOW_RETURNED,)),
            c("[Keep it where it is.]", "yew", flags=(YEW_BOW,))),
        nar("taken_gone", '''{n}Her hands are closed on nothing. The antler bow is long gone from here, into some quartermaster's wagon or some merchant's back room.{/n}''',
            c("Continue", "yew", flags=(YEW_BOW,))),
        nar("given_now", '''{n}You fold her fingers back around the antler grip one at a time. They are cold, and stiffer than wood. The bow settles into them as if it had never been away, and something in the crypt that you had not noticed was strained goes quiet.{/n}''',
            c("Continue", "horn")),
        nar("yew", '''{n}At her feet, half under the hem of her shroud, lies the other bow the Kellid priests left her: plain yew, unstrung, a sheaf of grey-fletched arrows tied beside it. Something for the road, wherever the road went.{/n}''',
            c("Continue", "horn")),
    ]
    if crypt:
        nodes += crypt_nodes
    nodes += [
        nar("horn", '''{n}You take the horn down from its peg. It is heavier than it looks, and cold, and the stag cut into its side has been worn smooth by fingers that never once dared lift it to a mouth.{/n}''',
            c("Continue", "plea" if place == "kyado" else "lift")),
    ]
    if place == "kyado":
        nodes.append(kyado("plea", '''"Commander, n-no. Rathimus said nobody. 'When the stag calls, she answers.' You're not a stag. You're..."
{n}He looks at you properly, with the lamp shaking in both hands, and stops.{/n} "Oh, Erastil. You're going to be the stag."''',
            c("Continue", "lift")))
    nodes += [
        nar("lift", '''{n}The crypt waits. Somewhere above, the temple's timbers tick in the cold. You wet your lips.{/n}''',
            c('[Lore (Nature): sound a white stag\'s roar, the way Kyado described it] "Let\'s see who answers."',
              requires=(HORN_LORE,), mythic="Trickster", alignment=("Chaotic", 1),
              check=dict(Skill="SkillLoreNature", DC=18, Success="roar", Failure="fumble", CommanderOnly=True)),
            c('[Lore (Nature): sound a stag\'s roar in rut, as best you remember one] "Let\'s see who answers."',
              forbids=(HORN_LORE,), mythic="Trickster", alignment=("Chaotic", 1),
              check=dict(Skill="SkillLoreNature", DC=26, Success="roar", Failure="fumble", CommanderOnly=True)),
            c("[Hang the horn back on its peg.]", abort=True)),
        nar("fumble", '''{n}What comes out of the horn is not a stag. It is a calf with a head cold, or a goose sat on by a cow. It goes twice round the walls and dies in a corner.{/n}
{n}Nothing stirs. The stone is only stone. Whatever you would have to sound to call a hunter up out of the dark, it was not that.{/n}''',
            c("[Hang the horn back on its peg. Come back when you know the call.]", abort=True)),
        nar("roar", '''{n}You fill your chest and give it everything: three short barks from the belly, and then the long one, broken in the middle and rising, the sound a stag makes in the autumn hills when it wants the whole valley to know it is ready to fight anything that comes.{/n}
{n}It hits the walls and does not stop there. It goes up and out, and somewhere far off in the dark, over woods that have not heard that call in a very long time, something answers.{/n}
{n}Then the silence. Then, very close, a breath.{/n}''',
            c("Continue", "rise")),
        nar("rise", '''{n}It is not how the dead get up in stories. There is no green fire in her eyes, no rattle of bone on stone. There is breath: one long, dragging breath, as if the whole crypt had been holding it for her. Her ribs lift under the stag-hide and do not fall back.{/n}
{n}The leather of her face goes dark and soft, and then it is skin, grey with dust, and then it is not grey. Her eyes open. They are brown, and human, and they are looking straight at you over the lip of the stone.{/n}''',
            c("Continue", "draw_antler", forbids=(YEW_BOW,)),
            c("Continue", "draw_yew", requires=(YEW_BOW,))),
        nar("draw_antler", '''{n}She comes up out of the sarcophagus the way a hunter comes up out of a hide: no stretch, no stagger, everything at once. The antler bow is in her hands. An arrow is on the string. You did not see where it came from.{/n}''',
            c("Continue", "stag")),
        nar("draw_yew", '''{n}She comes up out of the sarcophagus the way a hunter comes up out of a hide: no stretch, no stagger, everything at once. Her hands close on the empty place where the antler bow should be, and she does not waste a heartbeat on it. The yew bow from her feet is strung before you see her string it. A grey-fletched arrow is on it.{/n}''',
            c("Continue", "stag")),
        nar("stag", '''{n}She says nothing. She has not come back to talk. She is looking at the horn in your hand, and at you, and her face holds no anger at all, only an enormous and terrible patience.{/n}
{n}There is a rule every child in the hill country learns before it learns its letters, and it surfaces in you now from somewhere you did not know you kept it: a stag that stands is meat.{/n}''',
            c("[Mobility: run.]", check=dict(Skill="SkillMobility", DC=24, Success="ran_far", Failure="ran_short", CommanderOnly=True))),
        nar("ran_far", t["run_far"], c("Continue", "moonset", flags=(RAN_FAR,))),
        nar("moonset", '''{n}Three days and three nights she hunted Erastil's white stag. You last until the moon goes down, which for a stag with a sword on its hip and no idea where the deer paths run is a very long time, and the woods will talk about it for a while.{/n}
{n}When the arrow comes, it comes from nowhere you were watching: twenty-five inches of ash and grey goose feather into the back of your thigh. Your leg goes out from under you, and the ground comes up, and you are on your face in the wet leaves with your mouth full of earth.{/n}''',
            c("Continue", "down")),
        nar("ran_short", t["run_short"], c("Continue", "doorstep", flags=(RAN_SHORT,))),
        nar("doorstep", '''{n}The arrow takes you in the back of the thigh on the third stride: twenty-five inches of ash and grey goose feather, driven in to the fletching. Your leg goes, and the ground comes up, and you are on your face in the cold with your mouth full of grit.{/n}''',
            c("Continue", "down")),
        dl("down", '''{n}She is on you before you have finished falling: one knee in the small of your back, one hand in your hair, a knife at the side of your throat. Her breath comes hard and quick. She has not breathed in a long time and her body is remembering how.{/n}
{n}She speaks to you low and gentle, the way you speak to a beast at the end.{/n} "Easy, brother. Easy. You ran well. The village thanks you. Old Deadeye will take you home."
{n}She turns your head to find the place for the knife, and sees a face.{/n}''',
            c('"Not yet. Hunt me again."', "not_yet", flags=(SAID_AGAIN,)),
            c('"You missed. I\'m still talking."', "missed", flags=(SAID_MISSED,)),
            c('"Go on, then. Finish it."', "finish", flags=(SAID_FINISH,))),
        dl("not_yet", '''{n}The knife stops.{/n} "The stag spoke to me once before. In my lord's woods, with a man's voice. It said: hunt me." {n}Her fingers tighten in your hair and then, slowly, let go.{/n} "Now a stag says: not yet. A hunter does not take a beast that has asked for another day. It is not done. It was never done, not in my time."''',
            c("Continue", "alive")),
        dl("missed", '''"I do not miss." {n}She puts one finger on the arrow standing out of your leg and presses, and waits politely for you to finish making noise.{/n} "I do not miss. I choose. I chose your leg because a stag with a leg in it still runs, and I have not finished running you." {n}The knife comes away from your throat.{/n} "And a stag that talks back is not a thing I have killed before. I will think about it."''',
            c("Continue", "alive")),
        dl("finish", '''"No." {n}The knife comes away from your throat as if it has burned her.{/n} "A stag that bares its throat is not a hunt. It is a slaughter, and I have never slaughtered. Not a beast, not a man." {n}She sits back on her heels.{/n} "You will get up, when you can get up. You are not finished running. I am not finished hunting."''',
            c("Continue", "alive")),
        nar("alive", '''{n}Then she looks at her own hands.{/n}
{n}Fingers. Nails, broken, as if she had spent a long time clawing at stone. Knuckles, a thin white scar across two of them that she clearly knows. She turns the knife in her grip and presses its point into the ball of her thumb, and watches what comes out.{/n}
{n}Red. It runs down into her palm, warm enough to steam in the cold.{/n}''',
            c("Continue", "remember")),
        dl("remember", '''"Red." {n}She says it the way another woman would say a prayer.{/n} "I was dead. I remember being dead. It is like standing at full draw in the dark, with nothing to loose at, for longer than there are words to count it."
{n}She flexes the bleeding hand and winces.{/n} "And now I am cold. And hungry. And my knees hurt." {n}Something in her face cracks, and for a heartbeat you cannot tell whether she is about to laugh or weep.{/n} "Erastil's mercy. My knees hurt."''',
            c("Continue", "lady")),
        dl("lady", '''{n}She looks up past you, at the dark overhead, and says something formal and low, the way you would speak to a magistrate across a table.{/n} "Lady of Graves. I did not run from your court. I was called out of it, and I answered, as I swore I would. Judge me for the answering when I come back to you. Not for the leaving."
{n}Then she looks down at you again, and she is only a tired woman with a knife.{/n}''',
            c('"Welcome back, Delamere the Blessed."', "name"),
            c('"You shot me."', "shot"),
            c('[Send her back to her grave] "I didn\'t wake you for company. Lie down again."', "grave")),
        dl("name", '''{n}Her head comes up.{/n} "You know my name. Then my glory is not all dust." {n}It pleases her more than she wants it to, and she hides it badly.{/n} "Good. Say it again later, when I can stand up straight to hear it."''',
            c("Continue", "clan")),
        dl("shot", '''"I did. Be glad I shot low." {n}She looks at the arrow with a craftsman's disapproval.{/n} "My arm is stiff from a long sleep. In my day that would have gone through the bone and out the other side."''',
            c("Continue", "clan")),
        dl("clan", '''"Tell me one thing, and then I will cut that arrow out of you." {n}She is listening past you, to the woods, the way you listen for a voice you know in a crowded room.{/n} "Whose clan holds these valleys now? The Stone Hares had the ford when I lay down, and the Ash-Cutters had the high meadows. I hear no dogs. There are always dogs."''',
            c('[Tell her gently] "Sarkoris is gone. A rift to the Abyss opened in the north, a long time ago. The clans are scattered, or dead."', "gone"),
            c('[Tell her straight] "There are no clans. The demons came. It\'s called the Worldwound, and it ate your country."', "gone")),
        dl("gone", '''{n}She does not move for a long breath. She does not weep, either. Her face goes very still and very old, the way a hillside goes still when a hawk's shadow crosses it.{/n}
"The Stone Hares had a girl who could track a fox across a frozen river. She was nine." {n}A pause.{/n} "I will count them later. All of them. The ones I can remember." {n}She wipes the knife on her thigh.{/n} "Not now. Now there is a stag bleeding in front of me, and I was taught to finish one thing before I start the next."''',
            c("Continue", "after")),
        dl("grave", '''{n}She laughs. It is not a kind sound, and the dust in her throat makes it worse.{/n} "There is no lying down again. The hunt is not finished, and a hunt that is not finished does not let its hunter sleep. You of all people should know that, stag. You called it."
{n}She gets up, leaves the knife in the earth beside your hand, and walks away into the dark without looking back.{/n} "Live, then. So will I. We need not do it together."''',
            c("[Let her go.]", flags=(DECLINED, CLOSED, LIMP))),
        t["after"],
        t["not_grave"],
        dl("cut", '''{n}She cuts the arrow out of you with the same knife, quickly and without apology, the way you would cut a barb out of a hound. The head has gone into the bone. When it comes free you hear it grate.{/n}
"You will walk crooked, stag. For the rest of your life." {n}She says it without pity, as a fact about weather.{/n} "That is what a good run costs. Every beast I ever took paid more."''',
            c("Continue", "right")),
        dl("right", '''{n}She binds the leg with a strip torn from her own shroud, and pulls the knot tight enough to make you see stars.{/n}
"Hear me, because I will say it once. I did not finish you. That means the hunt is not over; it means only that I have let you go for now. A stag that has asked for another day owes the hunter that day. When I want it, I will come for it."''',
            c('"And until then?"', "until"),
            c('"That sounds like a threat."', "until")),
        dl("until", '''"Until then, you had better stay quick." {n}She sits back on her heels and wipes the knife on the grass, and looks about her at last: the dark, the trees, the cold.{/n}''',
            c("Continue", "home_" + place)),
    ]
    homes = {
        "kyado": dl("home_kyado", '''"This is my temple. The boy may stay if he sweeps." {n}Kyado makes a sound like a kettle.{/n} "Go home to your war, stag, and put that leg up. I will come and see what kind of animal lives in your walls. When I am ready. Not before."''',
            c("[Limp home.]", flags=(RETURNED, STARTED, LIMP, HUNT_OWED, WOKE_KYADO))),
        "alone": dl("home_alone", '''"This is my temple. It has been swept, after a fashion, by somebody who is not here." {n}She looks at the broom at the foot of the stair for a while, and does not ask.{/n} "Go home to your war, stag, and put that leg up. I will come and see what kind of animal lives in your walls. When I am ready. Not before."''',
            c("[Limp home.]", flags=(RETURNED, STARTED, LIMP, HUNT_OWED, WOKE_ALONE))),
        "late": dl("home_late", '''"This is my temple. Horses in it." {n}She sniffs the air coming down the stair, and her lip curls.{/n} "Horses in my nave, and turnips on my altar. What has become of the world while I slept?" {n}She stands, and sways, and stands again.{/n} "Go home to your war, stag, and put that leg up. I will come and see what kind of animal lives in your walls. When I am ready. Not before."''',
            c("[Limp home.]", flags=(RETURNED, STARTED, LIMP, HUNT_OWED, WOKE_ALONE))),
        "drezen": dl("home_drezen", '''"I woke in a city." {n}She says it the way you would say you woke in a latrine.{/n} "Where is my temple? No. Do not tell me; I will find it. It is in the woods, where it belongs, and I am going there tonight, before this place gets into my lungs." {n}She stands.{/n} "Go home to your war, stag, and put that leg up. I will come and see what kind of animal lives in your walls. When I am ready. Not before."''',
            c("[Limp home.]", flags=(RETURNED, STARTED, LIMP, HUNT_OWED, WOKE_DREZEN))),
    }
    nodes.append(homes[place])
    return nodes


GATE_CRYPT = dict(RequiresAnyGroups=[[TOMB_VISITED, INITIATED]])

temple(P + "crypt.stag", "The stag's call", '"Bring your lamp, Kyado. We\'re going down to Delamere."', waking("kyado"),
       requires=("trickster", "trickster.ever"), forbids=(RETURNED, DECLINED, REMAINS),
       TricksterDevice=True, TricksterState="crypt", **GATE_CRYPT)

visit(P + "crypt.stag_alone", "The stag's call", waking("alone"),
      requires=("trickster", "trickster.ever", KYADO_DEAD), forbids=(RETURNED, DECLINED, REMAINS), chapters=(3, 5),
      TricksterDevice=True, TricksterState="crypt", RequiresAnyGroups=[[TOMB_VISITED, CRYPT_KNOWN]])

visit(P + "crypt.stag_late", "The stag's call", waking("late"),
      requires=("trickster", "trickster.ever"), forbids=(RETURNED, DECLINED, REMAINS, KYADO_DEAD),
      chapters=(5, 5), TricksterDevice=True, TricksterState="crypt", RequiresAnyGroups=[[TOMB_VISITED, CRYPT_KNOWN]])

visit(P + "drezen.stag", "The stag's call", waking("drezen"),
      requires=("trickster", "trickster.ever", REMAINS), forbids=(RETURNED, DECLINED), chapters=(3, 5),
      TricksterDevice=True, TricksterState="drezen")


# --- Reactions (Kyado, her prior; Ulbrig, a Kellid; Woljif, who once prayed to her in her temple, Cue_0146) ------------

ULBRIG = dict(requires=("ulbrig.in_party",), forbids=("ulbrig.dead", "ulbrig.kicked_out"))
WOLJIF = dict(forbids=("woljif.dead", "woljif.kicked_out"))

SCENES.append(reaction("Kyado", P + "react.kyado_woken", (RETURNED,),
    '''{n}Kyado is on his knees by the altar with a brush and a pail, scrubbing at a stain that is not there any more.{/n} "She eats everything, Commander. Everything. She ate the pilgrims' bread and the turnips and the candles, nearly. She says the dead don't get hungry. I looked it up in Rathimus's scrolls, and they don't." {n}He sits back and wipes his forehead with his wrist.{/n} "She told me I sweep like a man who expects to be forgiven for it. Then she took the broom and did it herself, and it's the cleanest it's ever been. I don't know if I'm the prior any more. I don't think I mind."''',
    answer_list=KYADO_HUB, relationship="delamere", forbids=(KYADO_DEAD, CLOSED), entry='"How are you getting on with Delamere?"',
    chapter=3, last=3, delay=24, NativeReturnCue=KYADO_RETURN))
SCENES.append(reaction("Kyado", P + "react.kyado_caught", (COMMITTED,),
    '''"She came back from the woods this morning singing." {n}Kyado says it in the tone of a man reporting a comet.{/n} "Not well. Something old, about a hunter and a hind. She hung a fresh hide in the yard to cure and told me that if I so much as looked at it she would make a pair of boots out of me." {n}He hesitates, turning red to the ears.{/n} "Commander, I'm happy for you. I think. Please don't let her make boots out of me."''',
    answer_list=KYADO_HUB, relationship="delamere", forbids=(KYADO_DEAD,), entry='"You look like you want to say something, Kyado."',
    chapter=3, last=3, delay=12, NativeReturnCue=KYADO_RETURN))
SCENES.append(reaction("Ulbrig", P + "react.ulbrig_huntress", (RETURNED, *ULBRIG["requires"]),
    '''"There's a Kellid woman in the woods under that old Erastil temple who talks like my grandmother's grandmother." {n}Ulbrig turns his cup round on the table.{/n} "I went to look. She asked me my clan and I told her. She asked how many of us are left and I told her that too. She didn't say sorry. Old ones never do. She said, 'Then you will have to be a great many men, one at a time.'" {n}He drinks.{/n} "Worst thing anyone's said to me in years, warchief. I've been thinking about it ever since."''',
    answer_list=ULBRIG_HUB, relationship="delamere", forbids=ULBRIG["forbids"], entry='"You look thoughtful, Ulbrig."',
    chapter=3, last=5, delay=48))
SCENES.append(reaction("Woljif", P + "react.woljif_limp", (RETURNED, LIMP),
    '''"Boss. Boss. Hold on." {n}Woljif falls in beside you and matches your walk, badly, on purpose.{/n} "I prayed to her, you know. In that temple, when we was there, I asked Delamere for a little help on a private matter. And now there's a big scary woman with a bow walkin' around sayin' she's her, and you're walkin' like that." {n}He stops limping.{/n} "I'm not askin' what you did. I'm askin' whether she heard me, 'cause I'd like to take it back."''',
    answer_list=WOLJIF_HUB, relationship="delamere", forbids=WOLJIF["forbids"], entry='"Something on your mind, Woljif?"',
    chapter=3, last=5, delay=24))


# --- Epilogue pages (ordered siblings; read-only) ------------------------------------------------------------------

EPI = "DelamereEpilogue"


def epilogue(id, text, requires, forbids=(), paragraphs=()):
    SCENES.append(scene(P + "epilogue." + id, "", EPI, 6, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=forbids, last=6, Relationship="delamere"))


VILLAGE_GIVEN = P + "village.given"
VILLAGE_FORCED = P + "village.forced"
VILLAGE_REFUSED = P + "village.refused"
VILLAGE_CLANS = P + "village.clans"
KYADO_SPOKEN = P + "kyado.spoken_for"
KYADO_JUDGED = P + "kyado.judged"
FIRST_FROST = P + "first_frost"
STAG_TOLD = P + "white_stag_told"
LIAR = P + "kept_the_lie"
CLAIMED = P + "claimed_her"
PROCLAIMED = P + "proclaimed"
KEPT_QUIET = P + "kept_quiet"
NAMES = P + "names_cut"
POACHERS_PROVOST = P + "poachers.provost"
POACHERS_HERS = P + "poachers.her_law"
POACHERS_TRICKED = P + "poachers.tricked"

EPILOGUE_PARAGRAPHS = (
    p('''{n}The families she led out of Drezen's camps built their villages in the old Sarkorian clearings below her temple. None of them ever grew past fifty-three. When one did, she walked in at the next new moon and chose who would go and found the next, and the families went, and did not thank her, and did well.{/n}''', requires=(VILLAGE_GIVEN,)),
    p('''{n}The families she drove out of Drezen's camps built their villages in the old Sarkorian clearings below her temple, the ones who lived to build them. They feared her, as her own people had feared her. They also never starved, and not one of their villages burned in the demon raids that followed the war. Their grandchildren still argue over which of those things matters more.{/n}''', requires=(VILLAGE_FORCED,)),
    p('''{n}Drezen kept its refugees behind its walls, as the Commander had wanted. She never forgave the city for it, and she never forgave the Commander, and she came to the city anyway, every market day, and sold her meat at the gate at a price that was an insult to everyone who paid it.{/n}''', requires=(VILLAGE_REFUSED,)),
    p('''{n}Every barracks in Drezen had an elder after the war, chosen by her, and every elder knew the names of fifty-three people and no more. The city clerks thought it was a joke of the Commander's. It was, and it worked, and she never once admitted either.{/n}''', requires=(VILLAGE_CLANS,)),
    p('''{n}Kyado stayed on as prior of her temple, and swept, and was told every day that he swept badly, and grew old and grey there in the end, as he had once said he hoped to. When he died she buried him herself, under the stag carved on the crypt wall, and she did not let anyone else touch the spade.{/n}''', requires=(KYADO_SPOKEN,)),
    p('''{n}Drezen never forgot the morning its Commander stood in the market and named her. Pilgrims came to her woods for the rest of her second life, and she hated every one of them, and fed every one of them, and sent them home with a hare and a scolding.{/n}''', requires=(PROCLAIMED,)),
    p('''{n}Drezen never learned who the tall Kellid woman at the market was. The minstrels went on singing her wrong. She preferred it.{/n}''', requires=(KEPT_QUIET,)),
    p('''{n}The names on the crypt wall reached nine hundred before she was done. The last she cut was a farm boy's, three valleys over from her temple; she walked there the first spring after the war to ask it, and found an old woman who still remembered him, and carried the name home.{/n}''', requires=(NAMES,)),
    p('''{n}The crusade's provost flogged three men for a doe in fawn in the spring of the war. It was the only time the crusade's law and hers agreed about anything, and she reminded the Commander of it at every quarrel after.{/n}''', requires=(POACHERS_PROVOST,)),
    p('''{n}Three Mendevian veterans settled below her temple after the war, in the village whose ditches they had dug. The one with the bad moustache married a cooper's widow there, and named his first daughter for the doe.{/n}''', requires=(POACHERS_HERS,)),
    p('''{n}The soldiers' story of Erastil's own doe outlived the crusade. Hunters in Mendev still let a doe in fawn pass, and some of them still look over their shoulders when they do it. She never corrected the story. She said it was the most useful lie ever told in her lord's name, and that she would answer to him for it herself, since the jester would only make him laugh.{/n}''', requires=(POACHERS_TRICKED,)),
    p('''{n}Kyado lived in the temple's stable for a year and said the prior's prayers from the doorway, as she had sentenced him to. On the first day of the second year she carried his bedroll back inside herself, and said nothing about it, then or ever.{/n}''', requires=(KYADO_JUDGED,)),
)

epilogue("caught", '''{n}Delamere the Blessed hunted the woods below her temple for years after the war, and the Worldwound's edge beyond them, and the demons that crossed into her woods learned what the marauders of old Sarkoris had learned before them.{/n}
{n}She never lived in a city. The Commander never lived anywhere else for long. Once a year, at the first frost, she came for the day she was owed, and the Commander ran, limping, through the dark hills with a horn in one hand and a laugh that carried for a mile, and she caught them every time, and every time she let the hunt go on.{/n}''',
         requires=(COMMITTED,), forbids=(CLOSED,), paragraphs=EPILOGUE_PARAGRAPHS + (
             p('''{n}At the first frost after Threshold she came for her day in the middle of the Commander's own victory feast, through a window, and took them out over the rooftops in front of half the crusade. Nobody at that table ever forgot it.{/n}''', requires=(FIRST_FROST,)),))

epilogue("late", '''{n}The war ended before she could run her second hunt, and she did not hold that against the war. In the first spring after Threshold she walked into the Commander's hall with her bow unstrung on her back and a haunch of venison over her shoulder, and dropped the meat on the table in front of the Commander's guests.{/n}
"My woods," she said. "Tonight. I will not make it easy." {n}She did not. The Commander caught her all the same, a little before dawn, in a blind below her temple where the embers were still warm, and she let herself be caught, and after that nobody asked the Commander where they went at the first frost every year.{/n}''',
         requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED), paragraphs=EPILOGUE_PARAGRAPHS)

epilogue("apart", '''{n}Delamere the Blessed kept to the woods below her temple after the war, and to the old law. The villages near her feared her and sent her their disputes, and she judged them as she had judged them in old Sarkoris, hard and without appeal.{/n}
{n}The Commander went on walking crooked. She never came to claim the day she was owed. The hunters say she keeps it anyway, the way you keep an arrow you have not decided where to put.{/n}''',
         requires=(RETURNED, CLOSED), forbids=(COMMITTED,), paragraphs=EPILOGUE_PARAGRAPHS + (
             p('''{n}She prayed to Erastil every night of her second life, on her knees, and he never once answered her. The Commander had once told her he had. She did not forget which of them had lied.{/n}''', requires=(LIAR,)),
             p('''{n}"Caught, and so owned," she told the one bard who dared ask her about the Commander. "That is how a hunter thinks about a hind. I had thought better of that one." She did not say more, and the bard did not ask.{/n}''', requires=(CLAIMED,)),))

epilogue("never", '''{n}The woman who woke in the Temple of Delamere walked away into the woods that night with her grave-dust still on her and was not seen again by anyone who could put a name to her. The Kellid villages that grew up below her temple after the war told stories of a huntress who judged their quarrels from the tree line and never came into the light.{/n}
{n}The Commander walked crooked for the rest of their life, and never told anyone why.{/n}''',
         requires=(DECLINED, CLOSED), forbids=(RETURNED,))

epilogue("unfinished", '''{n}Delamere the Blessed kept to the woods below her temple after the war. Now and then, on a cold night, the sentries on Drezen's wall heard a stag roar in the hills, far too close to the city, and in the morning there were tracks under the Commander's window that no stag had made.{/n}''',
         requires=(RETURNED,), forbids=(COMMITTED, CLOSED, LATE_COMMITTED), paragraphs=EPILOGUE_PARAGRAPHS)


def integrate(payload):
    """Her own native reads, items and Derived keys. Other world keys (kyado.*, delamere.tomb_visited, the remains
    project) bind on demand in trickster_world."""
    for kind, keys in (("UnlockableFlags", BINDINGS["UnlockableFlags"]), ("InventoryItems", BINDINGS["InventoryItems"])):
        for key, guid in keys.items():
            have = payload.setdefault(kind, {}).get(key)
            if have is not None and have != guid:
                raise ValueError("Conflicting binding: " + key)
            payload[kind][key] = guid
    for key, guid in BINDINGS["SelectedAnswers"].items():
        have = payload.setdefault("SelectedAnswers", {}).get(key)
        if have is not None and have != guid:
            raise ValueError("Conflicting binding: " + key)
        payload["SelectedAnswers"][key] = guid
    items = payload.setdefault("RemovableItems", [])
    for item in (BOW_ITEM, CURSED_BOW_ITEM):
        if item not in items:
            items.append(item)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]

