"""Nidalynn on the Trickster path: "Out in the ash" (Writer/handoffs/11-ROSTER-PLAN-2.md §2, binding;
spec Writer/handoffs/trickster/nidalynn.md for canon and hooks only: its cheese appraisal, chalk label, Fye presence,
riddle test and priced second ask are dropped).

Canon (blueprints.zip / enGB):
- A Lawful Good silver dragon: "I, Nidalynn, a silver dragon, swear loyalty to you, gold dragon {name}!" (6a4beb10);
  NidalynnDragon c966ef14 (Female, Huge); Nidalynn_PolymorphBuff 885ee6e3. Natively she appears only on the Gold Dragon
  path (NidalynnQuest1 4adaa0e0, Chapter 5, Kenabres): "a woman in a clean, but worn dress... the bulging belly of an
  expectant mother" (Cue_0001 64b38b81), sharp in the part ("Pft! Fine!", Cue_0009 e630e823; "Is this a joke? Are you
  trying to play a trick on me?", Cue_0013 c7e26a7e).
- Her own voice once the part is dropped (DragonsKenabres): "As a silver dragon, I believe kindness and sincerity are of
  the utmost importance. However, it is not just the soul that needs to be nourished. You must also sustain your body!...
  eat it slowly, savor its flavor.... and be grateful!" (Cue_0015 115f3b59); "It's not what you say that matters... it's
  what you do!" (Cue_0009 6b89e1d4); "I knew that an absurd request from a pregnant woman would seem foolish. But she
  could have taught you a valuable lesson." (Cue_0016 37d0134d); "Typical Orgomandias" (Cue_0003 b3399115).
- The Windstep clan's brand, "a mare galloping beneath the stars", and "Reudger the White"; "I remember him sitting
  there, smoking his pipe, as he watched the mares graze" (NidalynnQuest1 Cue_0012 ebae4003, Cue_0017 913f48fe); her
  grandfather's riddle, "What is Golarion's 'salt'?... the common folk" (Cue_0018 1d1fd011, Cue_0023 90cc684e); "Warriors
  are not the only ones worth remembering." (Cue_0024 0f34a4ab).
- Metallic dragons wanted Devarra's clutch: "they may disguise themselves as druids, and ask the crusaders to give them
  the woundwyrm eggs the Commander took from the Ivory Sanctum. Thank you for those, by the way. Rest assured, we'll take
  good care of them." (DragonsKenabres Cue_0058 7e1a31d4, Nidalynn's line; Gold Dragon path).
- The clutch (Ivory Sanctum): the golems over the eggs, "Or else your eggs will be destroyed!" (Golems_DragonEggs
  Cue_0001 b8dfb42d / Cue_0047 ea54d573), "In unison, the golems swing their fists above the eggs on the ground"
  (Cue_0006 24de2c3e); built sloppily ("The details are crude... enchanted very clumsily", Cue_0067 2a3bcece), their
  "behavioral schematic for controlling the dragon" done by Zhan Sebao, whom his fellow student calls lazy (Cue_0033
  234c128b, Cue_0040 69431140); "These are woundwyrm eggs and they look like they will soon hatch." (Cue_0045 9c653a90);
  "You can feel the heat radiating out from the thick shell" (DragonEggs Cue_0001 b2bf1f68); Greybor: "we need to destroy
  them." (DragonEggs Cue_0016 99a468ad).

The device (11 §2 as corrected by the coordinator after the Astra review: no invented rule about how the golems perceive
the eggs, since no native blueprint, dialog or cue describes one): under the golems' raised fists (Cue_0006) the Commander
takes the smallest egg, the coldest, and buries it in the chamber's ash-bin, and carries it out grey with ash as "a rock".
Earned by a Stealth or Trickery check; a failed check puts the Commander's hand under a golem fist (the golems natively
answer intruders, Cue_0047 / Cue_0034), and the egg is saved all the same. Then the Commander chooses not to smash it. Fallback, while the
crated clutch waits in the Drezen vault: the same soot among the crates, and the egg carried out hot (burnt palms).

Authored, and labelled as authored: that metallic dragons were watching the clutch on Trickster too; that Nidalynn lives
in Drezen as the same pregnant widow she plays in canon Kenabres, on the steps opposite the jeweller where the refugees
sell what they carried out of Sarkoris; that she was a girl at Reudger's fire and called him grandfather; his rite of
bread and salt; the lime-kiln below the east wall; everything she says here.

Delivery: a presence of her own (the widow, then her chosen form) opposite JewelerCapitalTrader, and rest-delivered
visits for the kiln, the hatching and the ridge. The courtship is nidalynn_kiln and nidalynn_salt.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
REL = "nidalynn"
P = "nidalynn.trickster."
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
JEWELLER = "bc1093231b1577a4485a730c29595195"      # JewelerCapitalTrader (Arueshalae's evil fallback, Ch5 only, stands front 2.0)
WIDOW_UNIT = "e24a8cb4f83960748b5bead99d58a36e"    # Commoner_Noble_Female_Refugee2 (a Kenabres refugee woman; no Drezen spawner uses it)
CHOSEN_UNIT = "3191b154bbed71b4595a5154ad067e90"   # Commoner_Noble_Female_Refugee1 (her own chosen form; a different body)
GOLEM_LIST = "dd8ac86f25e0f6b4cac75386eb528851"    # IvorySanctum/Golems_DragonEggs/AnswersList_0002
GOLEM_RETURN = "d39b1e850904daa43b7e6dab3a6e7f83"  # Golems_DragonEggs/Cue_0046 "Only a very large creature could lay eggs like these."
GREYBOR_LIST = "174d6c94b6725f44aad1d2a76993a926"  # Companions/Grimbor/AnswersList_0002
ULBRIG_HUB = "0a50c9c878844ed4a69b8d6131304c5e"    # DLC4_Shifter/Shifter_CompanionDialogue/AnswersList_0001
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"    # CompanionDialogues/Woljif/AnswersList_0003
WIDOW = "nidalynn.presence"
CHOSEN = "nidalynn.presence.chosen"

STARTED = "nidalynn.started"
CLOSED = "nidalynn.closed"
COMMITTED = "nidalynn.committed"
CRATED = "nidalynn.trickster.eggs_crated"         # latch on eggs.project (trickster_world LATCHES)
WOLJIF_SIGHED = "nidalynn.woljif_sighed"            # SeenCues DragonEggs/Cue_0018 d2f3ae3a (his sigh over the smashed clutch)
DV_RETURNED = "devarra.trickster.returned"         # read in nodes only (ledger 05 row 5: neither route gates the other)
DV_HUNTING = "devarra.trickster.hunting_druids"
DV_BILL = "devarra.trickster.cost.egg_withheld"   # set by devarra_tower's "The smallest egg" (the bill lands on the Commander)

PRIMED = P + "primed"                              # one egg saved, by either device
GOLEM = P + "egg.golems"
VAULT = P + "egg.vault"
STRAW = P + "egg.straw"                            # PP10: the twelfth the druids left in the straw, kept by the Commander
# Polish (coordinator, 2026-10-03; Devarra polish): the debt is incurred the moment the Commander takes the twelfth egg, by
# any device (the golems, the vault, the straw). Devarra reads it on her return; her own bill, named later at her tower,
# stays devarra.trickster.cost.egg_withheld (its readers, her call-in and ledger, need the bill she has actually named).
EGG_OWED = P + "egg_owed"
STRAW_BURNED = P + "straw.burned"                  # PP10: the Commander let it go out with the bedding (her door never opens)
QUARTERMASTER = P + "quartermaster_knew"           # PP10: the quartermaster wrote "disposed of" knowing it was a lie
GIVEN = P + "eggs_given"                           # PP10: latch on eggs.druids (trickster_world LATCHES)
STORYTELLER_SUPPLIES = "storyteller.supplies"     # PP10: SeenCues StoryTeller_MainDialogue/Cue_0629 459bf324 (his portal supplies, Ch4)
SLATE = P + "cost.slate"                           # PP10: the lie on the stores' slate, in the Commander's mark (confessed at the kiln)
CLEAN = P + "egg.clean"
HAND = P + "cost.hand"                             # a golem fist, on the failed check
PALMS = P + "cost.palms"                           # the vault egg carried out hot
CLERK = P + "clerk_saw"
CRUSHED = P + "egg_crushed"
ROCK_JOKE = P + "rock_joke"
HEARTH = P + "hearth.grey_stone"                   # scene ids double as flags once completed
MET = P + "met"
TOLD_ROCK = P + "told_rock"
TOLD_EGG = P + "told_egg"
TOLD_NOTHING = P + "told_nothing"
KILN_AGREED = P + "kiln_agreed"
REVEALED = P + "revealed"
PARTNER_DISGUISE = "nidalynn.partner_claim.disguise"  # authored disclosure, not a real partner stance
WHY_SMALL = P + "why.smallest"
WHY_COULD = P + "why.could"
WHY_USE = P + "why.useful"
WHY_DUNNO = P + "why.dont_know"
HAND_SET = P + "hand_set"
KILN = P + "kiln"
HATCHED = P + "hatched"
CONFESSED = P + "confessed"
LIED = P + "lied_at_kiln"
LIE_KEPT = P + "lie_kept"
GIVEN_UP = P + "given_to_the_crowd"
RENOUNCED = P + "cost.claim_given_up"
CLAIMED = P + "claimed"
LEFT_WITH_IT = P + "left_with_it"
FORM = P + "form_chosen"
KISSED = P + "kissed"
PROPOSED = P + "proposed"
BREAD_KEPT = P + "bread_kept"
SALT = P + "cost.salt_eaten"
SNOW = P + "snowfield"
REFUSED = P + "refused"
LATE_COMMITTED = P + "late_committed"
MET_EARLY = P + "met_before_abyss"                 # Q9 (Sol INT): she was met before the Abyss (Chapter05 not yet playing)
CH5 = "irabeth.chapter_five"                       # the Chapter05 etude (5b01aa69), bound by irabeth_independent
GOAT_CORRECTED = P + "goat.corrected"              # Q9 (Sol VOI): the wolves story taken back; the sentries cleared
GOAT_STANDS = P + "goat.lie_kept"                  # Q9: the wolves story kept; she will not raise her on it
EGG_WORLDS = ("eggs.omelet", "eggs.druids", "eggs.project", "eggs.destroyed")

DERIVED = {
    # R2-6: she has put off the widow for the Commander; if the war ends before the hatchling flies, the epilogue carries
    # her proposal (Last Call and the household read it).
    # PP10 (Sol INT): after the kiss on the wall (wall.wings), an explicit romantic act, not her own face alone.
    LATE_COMMITTED: [["trickster.ever", KISSED]],
    # 05 §2.5 voice note: she joins a household the way she joined the Windstep, by being fed at its fire and feeding it.
    "nidalynn.harem.voice.fed_at_the_fire": [[COMMITTED], [LATE_COMMITTED]],
}

RELATIONSHIP = dict(
    Title="Salt on Bread",
    Description=("I kept the smallest of Devarra's eggs alive. The citadel calls it my rock. A Sarkorian widow on the steps opposite the jeweller heard it singing in my hearth. She says it is dying, and means to do something about it."),
    Objective="Keep the smallest egg alive",
    Guidance=("On the Trickster path, in the Ivory Sanctum, look at the smallest of the eggs under Xanthir Vang's "
              "golems before they act, and get it out from under their fists. If the clutch was crated to Drezen instead, the eggs wait in "
              "the citadel vault until the druids or the cooks take them; and if the druids come for them, see what they "
              "leave in the straw. After that, a widow on the steps opposite the jeweller will want a word."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[], FailureFlags=[],
    TricksterAccess={
        "golems": dict(detect=["trickster"], device=P + "eggs.lamp_black", returned=MET),
        "vault": dict(detect=["eggs.project"], device=P + "eggs.vault", returned=MET),
        "straw": dict(detect=["eggs.druids"], device=P + "eggs.straw", returned=MET),
    },
)

PRESENCES = {
    # The widow, as she sits in canon Kenabres: across the square from the jeweller, where the refugees sell their clan
    # torcs. Arueshalae's evil fallback (Chapter 5, evil path only) stands front 2.0 of the same trader: 3.2 m apart.
    WIDOW: dict(Unit=WIDOW_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=JEWELLER, Side="left", Distance=2.5),
                Requires=["trickster.ever", HEARTH], Forbids=[CLOSED, FORM, LEFT_WITH_IT], MinChapter=3, MaxChapter=5,
                AnswerLists=[], Dialog="hub",
                Greeting="{n}On the steps across from the jeweller's stall, where the refugees come to sell what they "
                         "carried out of Sarkoris, a woman in a clean, worn dress sits with her hands folded on the swell of "
                         "her belly. A basket of mending is beside her. She is not mending it. She is watching who sells "
                         "what, and for how much.{/n}"),
    # Her own chosen form, once the widow is put off: the same step, a different body, never the belly.
    CHOSEN: dict(Unit=CHOSEN_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=JEWELLER, Side="left", Distance=2.5),
                 Requires=["trickster.ever", FORM], Forbids=[CLOSED, LEFT_WITH_IT], MinChapter=3, MaxChapter=5,
                 AnswerLists=[], Dialog="hub",
                 Greeting="{n}On the jeweller's steps, where the widow used to sit, a tall woman sits with her knees "
                          "drawn up and a white braid over one shoulder. The refugees who pass nod to her as if they "
                          "have always known her. She is eating an apple, slowly, and looks at you as though you are "
                          "late.{/n}"),
}


def nd(id, text, *choices, **kw):
    return n(id, "Nidalynn", text, *choices, portrait="Nidalynn", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Nidalynn", **kw)


def steps(id, title, entry, nodes, requires, forbids=(), delay=24, chosen=False, chapters=(3, 5), optional=False,
          into=None, **extra):
    """A physical scene at her presence on the jeweller's steps (the widow's hub, or her chosen form's)."""
    (SCENES if into is None else into).append(scene(
        id, title, "Nidalynn", min(chapters), entry, nodes,
        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
        forbids=tuple(dict.fromkeys((CLOSED, LEFT_WITH_IT, *forbids))), delay=delay, last=max(chapters),
        optional=optional, Relationship=REL, Chapters=list(chapters), ContactUnit=CHOSEN_UNIT if chosen else WIDOW_UNIT,
        Areas=[DREZEN], InteractionHub=CHOSEN if chosen else WIDOW, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, chapters=(3, 5), kind="visit", optional=False, owner="Nidalynn",
          into=None, **extra):
    """A rest-delivered page: she comes to the Commander, or takes the Commander somewhere (the kiln, the ridge)."""
    (SCENES if into is None else into).append(scene(
        id, title, owner, min(chapters), "", nodes,
        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
        forbids=tuple(dict.fromkeys((CLOSED, LEFT_WITH_IT, *forbids))), delay=delay, last=max(chapters),
        optional=optional, Relationship=REL, Chapters=sorted(set(chapters)), Remote=True, Kind=kind,
        **({} if kind == "letter" else dict(Areas=[DREZEN])), **extra))


# --- The device (physical, Chapter 3): the smallest egg, out from under the fists in the ash-bin -------------------------
# Inline on the golems' list, while "the golems swing their fists above the eggs" (Cue_0006). No rule about how the golems
# see is claimed: the Commander is simply not seen taking it (Stealth or Trickery), or is seen and pays with a hand, as any
# intruder among them would ("Intruder detected!", Cue_0047; "We are under attack! Alert!", Cue_0034). The native answers
# still decide the other eleven.

SCENES.append(scene(P + "eggs.lamp_black", "Out in the ash", "Nidalynn", 3, "[Look at the smallest egg, the one at the edge of the straw]", [
    nar("look", '''{n}The golems have not moved. Their fists hang over the clutch, and their blank metal faces are turned toward the eggs, and nothing in the chamber is quite still except them.{/n}
{n}The smallest egg lies at the edge of the straw, half out of it, as if it had been nudged aside. It is duller than the rest and a hand's breadth shorter, and when you hold your palm near it the heat coming off it is only warm, where the others burn. The runt of the clutch, and the coldest.{/n}
{n}By the wall behind the golems stands an iron bin of old ash and cinders, the leavings of some fire the cultists kept here. It is deep. It is exactly the colour of a dirty stone.{/n}''',
        c("[Stealth: go in under the raised fists, take the smallest egg, and bury it in the ash-bin]",
          mythic="Trickster", check=dict(Skill="SkillStealth", DC=22, Success="taken", Failure="fist", CommanderOnly=True)),
        c("[Trickery: roll a stone of the same size into the straw where it lay, and palm the egg into the ash-bin]",
          mythic="Trickster", check=dict(Skill="SkillThievery", DC=22, Success="taken", Failure="fist", CommanderOnly=True)),
        c("[Leave the eggs to the golems.]", abort=True)),
    nar("taken", '''{n}You go in low, under the fists, with your eyes on the metal faces and not on your hands. The shell is hotter than it looked; it scorches your fingers through your gloves. Three steps back, and it goes into the ash-bin, and you shovel the cinders over it with your forearm until there is nothing in the bin but ash and something that might be a stone.{/n}
{n}The fists stay over the clutch. The ash you stirred up hangs in the air and settles, slowly, on the straw and on the golems' shoulders and on the floor, where your boots have left a grey track from the clutch to the bin and back. Nobody here is going to read it but you. Nobody here, you think.{/n}''',
        c("Continue", "held", flags=(CLEAN,))),
    nar("fist", '''{n}You have the egg in your hands and one step taken toward the wall when the nearest golem's head turns. It is not quick. It does not need to be.{/n}
{n}The fist comes down. You get the egg out from under it and your hand does not quite follow; stone and stone meet across your knuckles with a sound like a dropped plate. The egg goes out of your grip and into the ash-bin, and the ash goes up in a grey cloud over both of you.{/n}
{n}The magical mouth shrieks about intruders, and the whole row of fists swings toward you. Somebody in your company is already shouting, drawing them off with steel and noise, and you go to your knees by the bin with your hand pressed against your chest. It is not a shape a hand should be.{/n}''',
        c("Continue", "held", flags=(HAND,))),
    nar("held", '''{n}When you dig it out of the bin it looks like a stone: grey with ash, black with cinders, dull. Only when you hold it does it give itself away, heavier than a stone and warm through the grime, and something inside it turns over against your palm, slowly, the way a sleeper turns.{/n}
{n}The golems stand over eleven eggs with their fists up. Whatever happens to those eleven now will happen whatever you do with the one in your hand.{/n}
{n}It is a woundwyrm, or it will be: Devarra's get, the spawn of the thing that tried to burn your army out of the sky. Greybor would say it needs smashing. The heel of your boot would finish it.{/n}''',
        c("[Wrap it in your cloak and put it at the bottom of your pack.]", "rock"),
        c("[Put your heel through it. Some things are better never hatched.]", "crushed", flags=(CRUSHED,))),
    nar("crushed", '''{n}The shell holds longer than you expect, and then it doesn't. What comes out into the ash is hot and wet and very small, and it does not live long.{/n}
{n}The golems do not turn their heads. Whatever they are watching for, it is not this.{/n}''',
        c("[Step back from the clutch.]")),
    nar("rock", '''{n}Somebody in your company asks what you have just put in your pack, and why it made you swear.{/n}''',
        c('"It\'s a rock. I painted it."', "packed", flags=(ROCK_JOKE,)),
        c('"A souvenir."', "packed")),
    nar("packed", '''{n}Nobody believes you, and nobody asks again, because the golems are still standing over eleven eggs with their fists up, and that is a more pressing question.{/n}
{n}At the bottom of your pack, wrapped in your cloak and grey with ash, something the golems failed to crush is still warm.{/n}''',
        c("[Turn back to the golems.]", flags=(PRIMED, GOLEM, EGG_OWED))),
], requires=("trickster",), forbids=(PRIMED, CRUSHED, "eggs.destroyed", "eggs.project"), last=3, Relationship=REL,
    Chapters=[3], AnswerLists=[GOLEM_LIST], NativeReturnCue=GOLEM_RETURN, TricksterDevice=True, TricksterState="golems"))


# Polish r2 (audit COX, ledger 05 §4: one Chapter 5 delivery): a Commander who takes the egg in Chapter 5 gets the grey
# stone's nights inside the same page, so the late start is one rest delivery, not two. The old final choice is kept and
# gated to the earlier chapters; the folded ending is appended.
HEARTH_FOLD = '''{n}It lives in the ashes of your hearth after that, at the back, where the fire is hottest, and it looks like a stone that somebody has been careless with. Within the week your steward has burned his fingers on it twice and calls it "the Commander's rock" with a particular expression, and soon so does the whole citadel.{/n}
{n}At night, when the house is quiet, the ashes around it shiver, and a cup on the mantel hums against the stone, and once, near midnight, you wake certain that someone is singing in the next room, very low, a long way off. Every morning the rock is a little colder. The hearth is as hot as your steward can make it. It is not enough.{/n}'''


# --- The fallback (a page, Chapters 3 and 5): the same soot, in the citadel vault -------------------------------------
# The clutch was crated to Drezen (DragonEggsProjectGained) and waits for the druids or the cooks. Worse terms: the vault
# clerk, and an egg that has to be carried out hot.

visit(P + "eggs.vault", "Coal", [
    nar("vault", '''{n}The eggs came up from the Ivory Sanctum packed in straw, twelve to a wagon, and the quartermaster put them in the dry vault under the citadel, next to the lamp oil, because it was the warmest room he had. They are still warm. The whole corridor smells of hot stone.{/n}
{n}Every evening at the eighth bell a clerk with a lamp comes down and counts them, because the quartermaster has heard that the druids want them and the kitchens want them and he does not trust either. He counts by the glow. You have watched him do it. The smallest egg, in the crate nearest the door, is the coldest of the twelve; he always has to hold his lamp away to see it.{/n}''',
        c("[Stealth: go down before the eighth bell with a bucket of coal and your lantern's soot]",
          mythic="Trickster", check=dict(Skill="SkillStealth", DC=20, Success="coal", Failure="clerk", CommanderOnly=True)),
        c("[Leave the crates to the quartermaster.]", abort=True)),
    nar("coal", '''{n}You black the smallest egg with soot until it will not glow for any lamp, and bury it in the coal bucket, and put a lump of coal the same size in its place in the straw. Nobody sees you go down.{/n}
{n}At the eighth bell the clerk counts eleven, frowns, counts again, and writes down twelve, because the slate says twelve and he would rather be wrong about eggs than about the slate.{/n}''',
        c("Continue", "carry")),
    nar("clerk", '''{n}You have the egg in the coal bucket and the lump of coal in the straw when the lamp comes round the corner an hour early.{/n}
{n}The clerk is young, and very tired, and he looks at the Commander of the crusade standing in the vault at night with soot to the elbow and a bucket of coal, and you watch him decide that he has not seen anything, because he would like to keep his post.{/n}
{n}He will remember it all the same. People always do.{/n}''',
        c("Continue", "carry", flags=(CLERK,))),
    nar("carry", '''{n}The coal bucket is no good for the stairs; it tips. You take the egg out and carry it up in your hands, under your coat, against your chest, the way you would carry a lamp through wind.{/n}
{n}It is much hotter than it looked. By the second landing the skin of both palms has gone white and tight, and by your own door it has started to blister. You do not put it down until it is in the ashes of your hearth, and then you sit on the floor and hold your hands in the washbasin, and the water goes warm.{/n}''',
        c("[Leave it in the ashes.]", flags=(PRIMED, VAULT, PALMS, EGG_OWED), forbids=(CH5,)),
        c("[Leave it in the ashes.]", "nights", requires=(CH5,))),
    nar("nights", HEARTH_FOLD, c("[Bank the fire.]", flags=(PRIMED, VAULT, PALMS, HEARTH, EGG_OWED))),
], requires=("trickster", CRATED), forbids=(PRIMED, CRUSHED, "eggs.druids", "eggs.omelet", "eggs.destroyed"), delay=24,
    kind="event", owner="Commander", TricksterDevice=True, TricksterState="vault")


# --- The straw (a page, Chapters 3 and 5, PP10): what the druids left ----------------------------------------------------
# An authored door for the world where the golems' count and the vault were both missed and the decree gave the clutch to
# the druids (Eggs_DragonsInEducation -> DragonsInEducationFinished e4374a17, "The woundwyrm eggs have been given to the
# druids." 5755378a). Canon: asked whether they would raise the hatchlings gentle, "a druid evasively replied that he and
# his companions 'should not get in the way of nature'" (fc8bb151); on the Gold Dragon path Nidalynn says dragons "may
# disguise themselves as druids" to take those very eggs (DragonsKenabres a3ab444b). Authored: that four came, carried
# eleven, and left the smallest, gone cold and silent, in the straw as nature's; that the Commander kept it against every
# word and signed it off the stores as disposed of. No golem rule, no magic: a lie in the Commander's own hand, which the
# kiln's confession names. It sets STRAW, not PRIMED: Devarra's count (devarra.tower.one_short) reads PRIMED and tells of
# an egg carried out of the chamber or the vault, which this one was not.

visit(P + "eggs.straw", "Disposed of", [
    nar("chit", '''{n}A chit from the citadel stores comes up with the evening dispatches, in the quartermaster's square hand:{/n}
"Commander. The druids have been for the eggs, as decreed: four of them and a handcart. They took eleven. The twelfth they left in the straw, the small one out of the crate by the door. Their man put his hand on it and listened a long while, and said there was nothing in it now. I asked would they not take it all the same and try. He said they should not get in the way of nature.
I'll not burn a Commander's spoil without the Commander's word, so it is by the stores' brazier on a folded sack, pending orders. It is no warmer for it. It is cold as a cellar stone. Am I to throw it out with the bedding, or does the Commander want it buried proper? It was a dragon's, whatever else."''',
        c("[Go down to the vault and look at it yourself.]", "vault"),
        c("[Put the chit aside for now.]", abort=True)),
    nar("vault", '''{n}The vault is cold now. The smell of hot stone went out with the crates, and the straw has been raked into a heap by the door for burning. Beside the stores' brazier, on a folded sack, where somebody set it down carefully and then did not know what to do next, sits the smallest egg. The sack is warm. The egg is not.{/n}
{n}It is dull and grey and a hand's breadth shorter than the others were, and when you lift it, it is no warmer than the flagstones. You hold it to your ear. Nothing. You hold it there a long time, until the quartermaster coughs on the stair. Nothing at all.{/n}
{n}Four people who were not, you are fairly sure, druids looked at this egg and gave it up. Every soldier in Drezen would cheer the cart that took it to the midden: it is Devarra's get, the spawn of the thing that tried to burn your army out of the sky. A thing everybody agrees is dead is the one thing nobody will ever come looking for.{/n}''',
        c("[Persuasion: tell the quartermaster you'll bury it yourself, sign it off his slate as disposed of, and carry it up under your coat as a stone]",
          mythic="Trickster", check=dict(Skill="CheckBluff", DC=20, Success="signed", Failure="seen_through", CommanderOnly=True)),
        c("[Put it on the heap. Let it go out with the bedding.]", "bedding", flags=(STRAW_BURNED,))),
    nar("bedding", '''{n}The quartermaster's boy carries the straw out to the midden at dusk and burns it, and the grey thing on top of it with the rest. It does not make a sound in the fire.{/n}''',
        c("[Go back up the stair.]")),
    nar("signed", '''"Buried, Commander. Right you are." {n}He licks his chalk and writes it on the slate under the eleven, in his square hand, and holds the slate out for your mark beside it: DISPOSED OF. You make your mark. He does not watch where your other hand goes, because he has no reason to, and the stone under your coat is a stone.{/n}''',
        c("Continue", "carry")),
    nar("seen_through", '''"Buried. Right you are." {n}The quartermaster looks at you, and at the shape under your coat, and at the empty top of the straw heap, and he has been a quartermaster for thirty years. He licks his chalk anyway and writes it on the slate under the eleven, DISPOSED OF, and holds it out for your mark.{/n}
"I'll write it, Commander, since you've signed it. I'll not pretend I didn't see where it went." {n}He wipes the chalk off his thumb.{/n} "And if that thing ever hatches, I'll not pretend then either."''',
        c("Continue", "carry", flags=(QUARTERMASTER,))),
    nar("carry", '''{n}It goes up four flights under your coat, cold against your ribs, and into the ashes at the back of your hearth where the fire is hottest. You bank the coals over it with the poker until there is nothing to see but a grey stone that somebody has been careless with.{/n}
{n}Then, because you have staked your name in chalk on a thing everybody else heard was empty, you sit up with it. Near midnight, so faintly that you could have imagined it, something inside it turns over. Once.{/n}''',
        c("[Leave it in the ashes.]", flags=(STRAW, SLATE, EGG_OWED), forbids=(CH5,)),
        c("[Leave it in the ashes.]", "nights", requires=(CH5,))),
    nar("nights", HEARTH_FOLD, c("[Bank the fire.]", flags=(STRAW, SLATE, HEARTH, EGG_OWED))),
], requires=("trickster", GIVEN), forbids=(PRIMED, CRUSHED, STRAW, STRAW_BURNED, "eggs.omelet", "eggs.destroyed"), delay=12,
    kind="event", owner="Commander", TricksterDevice=True, TricksterState="straw")   # Chapters 3 and 5: the quartermaster
    # keeps it by the stores' brazier pending the Commander's word, so a decree finished late, or a Commander away in the
    # Abyss, still finds it (PP10 Sol INT)


# --- The grey stone (a page): the rock in the Commander's hearth -------------------------------------------------------

visit(P + "hearth.grey_stone", "The Commander's rock", [
    nar("hearth", '''{n}It lives in the ashes of your hearth, at the back, where the fire is hottest, and it looks like a stone that somebody has been careless with. Your steward has tried to take it out twice to sweep, and burned his fingers both times, and now he calls it "the Commander's rock" with a particular expression, and sweeps around it.{/n}
{n}Soon the whole citadel calls it that. A sergeant you have never spoken to asks if it is lucky.{/n}''',
        c("Continue", "night")),
    nar("night", '''{n}At night, when the house is quiet, it makes a sound.{/n}
{n}Not a sound, exactly. The ashes around it shiver. A cup on the mantel hums against the stone. Once, near midnight, you wake and are certain that someone is singing in the next room, very low, a long way off, and there is no one in the next room and never was.{/n}
{n}In the morning the rock is a little colder than it was the night before. The hearth is as hot as your steward can make it. It is not enough.{/n}''',
        c('[Tell the steward it\'s a stone from the Sanctum, and to mind his own business.]', "end"),
        c("[Tell the steward nothing at all.]", "end")),
    nar("end", '''{n}He minds it, with the expression. The hearth is banked higher every night after that without your asking, which is how you know he has heard it singing too.{/n}''',
        c("[Bank the fire.]")),
], requires=(), forbids=(HEARTH,), delay=12, kind="event", owner="Commander",
    RequiresAnyGroups=[[PRIMED, STRAW]])   # PP10: the egg the druids left (STRAW) comes to the same hearth


# --- The meeting (physical, the widow's step) ---------------------------------------------------------------------------

steps(P + "steps.widow", "The widow on the steps", "[Sit down on the step beside the widow.]", [
    nd("start", '''"Sit if you're sitting, Commander. Mind the belly; it takes the whole step." {n}She moves her mending basket without looking at you. She is watching a Kellid girl across the square try to sell a copper torc to the jeweller, who is shaking his head the way jewellers shake their heads.{/n}
"You'll want to know why I've been watching your door. Everybody who sits on this step wants to know something, and they all start by saying it's a nice day." {n}She sniffs.{/n} "It isn't. It's going to snow."''',
        c('"Why have you been watching my door?"', "rock"),
        c('"It\'s a nice day."', "nice")),
    nd("nice", '''"Pft." {n}The corner of her mouth moves. For a heartbeat the widow is gone and somebody much older is enjoying herself.{/n} "Well. At least you listen."''',
        c("Continue", "rock")),
    nd("rock", '''"The Commander's rock." {n}She says it the way the sergeants say it, with the same expression your steward uses.{/n} "The whole citadel talks about it. It sits in your hearth and burns anyone who touches it, and at night it sings. The laundress on the second floor hears it through the flue. The laundress thinks it's a ghost."
{n}She turns her head and looks at you, and she has very pale eyes for a Sarkorian, grey with no brown in them at all.{/n} "And it needs turning. A quarter-turn, with the seam away from the coals." {n}Her needle stops. You have never told the laundress about a seam.{/n} "Oh, don't look so pleased. Bring me up to it before your steward tries turning it with a poker. What is it?"''',
        c('"A rock."', "lie", flags=(TOLD_ROCK,)),
        c('"A woundwyrm egg. I took it out from under the golems in the Ivory Sanctum."', "truth", flags=(TOLD_EGG,), forbids=(VAULT, STRAW)),
        c('"Who\'s asking?"', "who", flags=(TOLD_NOTHING,)),
        c('"A woundwyrm egg. I took it out of the citadel vault in a coal bucket, past my own clerk."', "truth", flags=(TOLD_EGG,),
          requires=(VAULT,)),
        # PP10: the egg the druids left in the straw.
        c('"A woundwyrm egg. The druids left it in my vault for dead. I didn\'t believe them."', "truth", flags=(TOLD_EGG,),
          requires=(STRAW,))),
    nd("lie", '''"Is this a joke? Are you trying to play a trick on me?" {n}It is exactly the voice of a tired woman who has been lied to by men all her life, and it is a very good voice, and she drops it at once.{/n} "No. You are. I can hear you doing it."
"It isn't a rock. Rocks don't turn over when you speak near them."''',
        c("Continue", "worlds")),
    nd("truth", '''{n}She lets out a breath she has been holding, and it smokes in the cold air a little longer than a breath should.{/n} "Yes. The smallest one." {n}She pats the belly, absently, the way the widow would.{/n} "Thank you for not lying about it. Most people would have. I had a speech ready for when you did."''',
        c("Continue", "worlds")),
    nd("who", '''"A widow on a step." {n}She pats the belly.{/n} "With a basket of mending and nobody to talk to. Who else would I be?" {n}She holds your eye, and it is not a widow's look at all.{/n} "Don't answer that. We'd both be lying, and it's too cold for it."''',
        c("Continue", "worlds")),
    nd("worlds", '''"I was in the Sanctum after you, Commander. I went down when the dust had settled, because somebody should."''',
        c("Continue", "destroyed", requires=("eggs.destroyed",)),
        c("Continue", "omelet", requires=("eggs.omelet",)),
        c("Continue", "druids", requires=("eggs.druids",), forbids=("eggs.omelet", STRAW)),
        c("Continue", "vault", requires=("eggs.project",), forbids=("eggs.druids", "eggs.omelet")),
        c("Continue", "chamber", forbids=EGG_WORLDS),
        c("Continue", "straw", requires=(STRAW,))),
    nd("destroyed", '''"Eleven shells on the chamber floor. Slop and shell, and ash over all of it." {n}Her voice does not change, and her hands in her lap do not move.{/n} "Eleven. There were twelve. I counted twice. And by the wall the ash-bin was dug out, and there was a place in the cinders where somebody had knelt."''',
        c("Continue", "mother")),
    nd("omelet", '''"Your kitchens made them into a supper for the whole city. I stood at the back of the soup line and watched the soldiers eat it." {n}She says it very evenly.{/n} "They were hungry. I won't hold that against them. But the quartermaster's slate said the cooks had eleven. There were twelve in the Sanctum. I counted."''',
        c("Continue", "mother")),
    nd("druids", '''"I was one of the druids." {n}She says it plainly, as she might say she was one of the washerwomen.{/n} "Four of us came for them, with a handcart and a story about nature. None of us was a druid. We carried eleven eggs out of your citadel. Eleven. There were twelve in the Sanctum; I had counted them before you ever came."''',
        c("Continue", "hunted", requires=(DV_HUNTING,)),
        c("Continue", "mother", forbids=(DV_HUNTING,))),
    nd("straw", '''"I was one of the druids." {n}She says it plainly, as she might say she was one of the washerwomen.{/n} "Four of us came for them, with a handcart and a story about nature. None of us was a druid. We carried eleven out of your citadel and left the twelfth in the straw. It had gone cold and quiet, and our eldest put his hand on it and listened, and said it was dead. I believed him. It was cold, and I was carrying eleven that were not."
{n}Her needle stops.{/n} "I stopped believing him somewhere on the road, with the others safe in the cart. So I came back for it in this shawl. Your quartermaster would not hand the crusade's goods to a beggar-woman at his door; it was waiting on the Commander's word, he said. I don't take things out of other people's stores. I was raised better." {n}She looks across the square at the citadel.{/n} "Then the Commander gave the word, and your hearth began to sing."''',
        c("Continue", "hunted", requires=(DV_HUNTING,)),
        c("Continue", "mother", forbids=(DV_HUNTING,))),
    nd("hunted", '''{n}Her mouth thins.{/n} "And something grey and hungry has been following our trail ever since, and it didn't find us by chance. You told her where to look." {n}She holds up a hand before you can speak.{/n} "Not now. We'll talk about that, you and I. Not on a step."''',
        c("Continue", "mother")),
    nd("vault", '''"There are eleven eggs cooling in straw under your citadel, and a clerk who counts them every night by lamplight." {n}She sniffs again.{/n} "There were twelve in the Sanctum. I counted them before you ever came."''',
        c("Continue", "mother")),
    nd("chamber", '''"I found the ash-bin by the wall dug out, and a place in the cinders where somebody had knelt." {n}She almost smiles.{/n} "There were twelve eggs in that chamber when I first went down to look at them. I had counted them. I'm good at counting eggs."''',
        c("Continue", "mother")),
    nd("mother", '''"So. One of them is in your hearth, and it's the smallest, and it's cold, and it's dying." {n}She says the last word gently, as a fact, the way a midwife would.{/n}''',
        c("Continue", "mother_alive", requires=(DV_RETURNED,)),
        c("Continue", "ask", forbids=(DV_RETURNED,))),
    nd("mother_alive", '''"And its mother is alive. I can smell her on your coat, Commander: hot iron and old meat. Don't tell me how. I can guess, and I would rather not know which of you I'd be angrier with."''',
        c("Continue", "ask")),
    nd("ask", '''"I'll come and look at it. Tonight, or tomorrow; when your guards have changed and the sergeant with the squint is on the door, because he lets pregnant women through and calls them 'mother'." {n}She picks up her mending, at last.{/n} "Keep the fire high until then. Higher than you think. And eat something, for pity's sake. You look like porridge."''',
        c('"Who are you?"', "who_end"),
        c('"Tonight, then."', "end")),
    nd("who_end", '''"Tonight." {n}She threads her needle.{/n} "I don't tell people who I am on steps. I tell them in their own houses, where they can sit down."''',
        c("[Leave her to her mending.]", flags=(MET, STARTED), requires=(CH5,)),
        c("[Leave her to her mending.]", flags=(MET, STARTED, MET_EARLY), forbids=(CH5,))),
    nd("end", '''{n}She nods, and threads her needle, and goes back to watching the jeweller cheat the Kellid girl out of her grandmother's torc, with an expression that would frighten the jeweller very much if he ever looked up.{/n}''',
        c("[Leave her to her mending.]", flags=(MET, STARTED), requires=(CH5,)),
        c("[Leave her to her mending.]", flags=(MET, STARTED, MET_EARLY), forbids=(CH5,))),
], requires=(HEARTH,), forbids=(MET,), delay=24)   # PP10: the hearth implies an egg (PRIMED or STRAW)


# --- Reactions (exactly Greybor, Ulbrig and Woljif; each behind his own guard) -----------------------------------------

SCENES.append(reaction("Greybor", P + "react.greybor.rock", (HATCHED,),
    '''{n}Greybor does not stop sharpening.{/n} "Your rock hatched." {n}The stone passes along the edge.{/n} "I know what those eggs were. I'd have done that one for free. Now there's a woundwyrm inside our walls." {n}He tests the edge on his thumb.{/n} "When it's big enough to be a job, somebody will pay me to do it. I'll tell them the price has gone up. You've given it time to grow."''',
    answer_list=GREYBOR_LIST, relationship=REL, forbids=("greybor.dead", "greybor.kicked_out", CLOSED),
    entry='"You\'ve heard about the kiln."', chapter=3, last=5, delay=24, portrait="Greybor"))
SCENES.append(reaction("Ulbrig", P + "react.ulbrig.white_girl", (MET, "ulbrig.in_party"),
    '''"That woman on the jeweller's steps, eh." {n}Ulbrig turns his cup round and round.{/n} "She hums the Windstep mare-songs. Nobody's sung those since before I went to sleep, warchief. The Windstep were horse-folk, north of the Moutray. Old Reudger's lot. Their mares could outrun a griffon for a mile; I know, I tried." {n}He stops turning the cup.{/n} "There was a white-haired girl at Reudger's fire when I was a lad. That widow's got the look of her, about the eyes. Her granddaughter, maybe, eh. Or I'm getting old." {n}He drinks.{/n} "My gran would've said: then mind your manners with her, whoever she is."''',
    answer_list=ULBRIG_HUB, relationship=REL, forbids=("ulbrig.dead", "ulbrig.kicked_out", CLOSED),
    entry='"You look like you\'ve seen a ghost, Ulbrig."', chapter=3, last=5, delay=48))
SCENES.append(reaction("Woljif", P + "react.woljif.small_one", (HATCHED, WOLJIF_SIGHED),
    '''"Chief. That thing at the kiln. That's one of the eggs from the Sanctum, ain't it." {n}Woljif is not grinning, which is unusual.{/n} "I said somethin' down there, when you smashed the rest. About how maybe they were the lucky ones, 'cause kids without moms don't do so well." {n}He scratches at a horn.{/n} "Then you went and pinched the runt, and got some old Sarkorian lady to be its mom. So now I gotta figure out if I was wrong." {n}He brightens a little.{/n} "Tell her it likes rats. I seen it eat four. That's good. That's a kid that knows how to get by."''',
    answer_list=WOLJIF_HUB, relationship=REL, forbids=("woljif.dead", "woljif.kicked_out", CLOSED, "chapter_later"),   # PP10 (Sol COX): retired; Woljif is outside her reactor allocation
    entry='"Something on your mind, Woljif?"', chapter=3, last=5, delay=24))
SCENES.append(reaction("Ulbrig", P + "react.ulbrig.snowfield", (SNOW, "ulbrig.in_party"),
    '''"Warchief." {n}Ulbrig is grinning into his cup and trying not to.{/n} "Half of Drezen saw you come down off the north peak with frost in your hair and that white-haired woman barefoot beside you, eh. The other half heard it by noon." {n}The grin goes.{/n} "My gran would've said: a woman who sings the Windstep songs doesn't break her salt for just anybody. Don't make her sorry she broke it for you. That's all. That's all I'll say." {n}He drinks.{/n} "...She feeds you, though. Good. You've needed feeding since the day I met you."''',
    answer_list=ULBRIG_HUB, relationship=REL, forbids=("ulbrig.dead", "ulbrig.kicked_out", CLOSED),
    entry='"You\'ve a look on you, Ulbrig."', chapter=5, last=5, delay=24))


# --- Epilogue pages (ordered siblings; read-only) ------------------------------------------------------------------------

EPI = "NidalynnEpilogue"
NAME_SOOT = P + "name.soot"
NAME_PEBBLE = P + "name.pebble"
NAME_NONE = P + "name.none"
FED_DEMONS = P + "fed.demons"
FED_GOATS = P + "fed.goats"
FED_RATS = P + "fed.rats"
TORC_BOUGHT = P + "torc.bought"
TORC_LIFTED = P + "torc.lifted"
TORC_LEFT = P + "torc.left"
FIRST_DEMON = P + "after.first_demon"


# Authored Trickster resolution (CANON-PARTNERS-DESIGN, Nidalynn): the husband is part of her disguise.
# Native NidalynnQuest1 Cue_0007/0008 (0c798d10 / f2c61bcd) claims a husband;
# DragonsKenabres Cue_0011/0016 (5f41445c / 37d0134d) reveals the staged test, but does not
# establish a spouse's existence or fate. This addition resolves her claim only in this route.
# A fictional bond gets no share/exclusive/secret choices (the design's explicit exception).
PARTNER_HISTORY = '''{n}The husband in the pregnant woman's tale had never existed. Nidalynn had invented him along with the belly; there was no abandoned spouse waiting for her to come home.{/n}'''


def epilogue(id, text, requires, forbids=(), paragraphs=(), **extra):
    SCENES.append(scene(P + "epilogue." + id, "", EPI, 6, "", [nar("page", text + "\n" + PARTNER_HISTORY, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=forbids, last=6, Relationship=REL, **extra))


ALIVE = dict(ForbidOverrides={"sacrifice": "trickster.commander_back"})   # Q9 (Sol BEL): living pages need the Commander back


EPILOGUE_PARAGRAPHS = (
    p('''{n}The young dragon grew up black-red and ill-tempered, with a pale seam down its spine where the Wound had touched it in the egg. It hunted demons along the Worldwound's edge from its second year, because they were the only thing it had ever been fed that it truly hated, and it hated them with a thoroughness its mother would have recognised.{/n}''', requires=(FED_DEMONS,)),
    p('''{n}The young dragon grew up black-red and ill-tempered, with a pale seam down its spine where the Wound had touched it in the egg. It never lost its taste for goat. Wherever it denned, the nearest villages kept a flock for it by arrangement, and were paid, and complained about the price every year on principle.{/n}''', requires=(FED_GOATS,)),
    p('''{n}The young dragon grew up black-red and ill-tempered, with a pale seam down its spine where the Wound had touched it in the egg. It never could pass a rat. The citadel cooks said the winter it cleared Drezen's undercroft was the best thing the crusade ever did.{/n}''', requires=(FED_RATS,)),
    p('''{n}The soldiers called it Soot, after the ash and soot it was hidden in. It never answered to the name, and it never let anyone else use one.{/n}''', requires=(NAME_SOOT,)),
    p('''{n}The soldiers called it Pebble, after the joke, and the joke outlived the war. It answered to the name from her mouth and from nobody else's. When it was the size of a barn it still came when she called it that, and bit whoever laughed.{/n}''', requires=(NAME_PEBBLE,)),
    p('''{n}It chose its own name in its tenth year, in Draconic, and told it to her and to no one else. She said it was a good name, and a long one, and that it had the word for "ash" in it.{/n}''', requires=(NAME_NONE,)),
    p('''{n}A Kellid woman in the refugee quarter wore a copper torc with a hare on it until she was very old, and told her grandchildren a Commander had bought it back from a jeweller at the full price, which nobody believed.{/n}''', requires=(TORC_BOUGHT,)),
    p('''{n}A jeweller in Drezen swore for years that a copper torc had walked off his counter on its own. The Kellid woman who wore it swore just as hard that she had never sold it.{/n}''', requires=(TORC_LIFTED,)),
    p('''{n}The Commander carried a white scar across two knuckles of one hand from the day in the Sanctum. A Sarkorian bonesetter had set the fingers before any priest got to them, and the crusade's healers found nothing left to mend but the scar, which she would not let them touch. She said a hand ought to remember what it did.{/n}''', requires=(HAND, HAND_SET)),
    p('''{n}The Commander carried a white scar across two knuckles of one hand from the day in the Sanctum. The crusade's healers mended the bones; nobody mended the scar, and the Commander never asked them to.{/n}''', requires=(HAND,), forbids=(HAND_SET,)),
    p('''{n}The Commander's palms stayed shiny and tight for the rest of the war, like a smith's, and never took a callus again. The only person who ever asked about them was told that a dragon's egg is a hot thing to carry and a hotter thing to put down.{/n}''', requires=(PALMS,)),
    p('''{n}The soldier from the ford took his twenty lashes and his month in the cells, and deserted in the spring, and was not seen in Drezen again. The kiln's sergeant said he had gone north to look for the grey one's tower. Nobody ever heard whether he found it.{/n}''', requires=(P + "spear.provost",)),
    p('''{n}The soldier from the ford lived out the war and a good deal longer, and never spoke of the night on the tanners' stair. He was the first man in Drezen to take his hat off when the young dragon flew over.{/n}''', requires=(P + "spear.freed",)),
    p('''{n}The soldier from the ford came down to the kiln every week after that, for as long as there was a dragon in it, with a pig's ear in his pocket, and sat on the step without saying much. The young dragon bit him only once, and he said it was fair, and that her mother had done worse.{/n}''', requires=(P + "spear.seen",)),
    p('''{n}The Kellid widow whose goat the young dragon ate lived near the wall for the rest of the war, where the wind did not come in. Her son grew up to be a drover, and would not have a goat in his herd, and said he could not remember why.{/n}''', requires=(P + "goat.asked",)),
    p('''{n}Three wolves were blamed for the goat in the refugee quarter, and two sentries of the east wall were flogged for letting them over. The widow whose goat it was never said otherwise, to anyone, and moved to the far side of the quarter in the spring.{/n}''', requires=(P + "goat.wolves",), forbids=(GOAT_CORRECTED,)),
    p('''{n}No wolves came over the east wall that winter, whatever the Commander had said for one morning. The two sentries kept their backs and their pay, and the Kellid widow whose goat it was had milk till the spring and a new goat after it, and told everyone in the quarter exactly what had eaten the old one.{/n}''', requires=(GOAT_CORRECTED,)),
    p('''{n}Ulbrig Olesk came down to the kiln every week that she kept it and he was in Drezen, and brought his own bread, and argued with her about horses until the embers went grey. Neither of them ever said what they talked about besides horses. The sergeant with the squint said it was mostly the dead.{/n}''', requires=(P + "ulbrig_met",)),
    p('''{n}The chaplain's report went to the see in Mendev and was read there, and argued over for a year, and filed. A copy of it is said to be in the archives still, with a note in a later hand in the margin: "And the woundwyrm? Enquire." Nobody ever did.{/n}''', requires=(P + "chaplain_prayed",)),
    p('''{n}Eleven young dragons grew up fat and furious in a valley three rivers east, under a gold one who pretended to be a stork. Every one of them flew over Drezen once, as if by accident, to look at the twelfth.{/n}''', requires=("eggs.druids",)),
)

# Polish (audit INT/BEL/COX): the grey dragon's bill, recorded the same way on every page but her living partner's. It says
# what Devarra asked (standing, or named at the rift: PP10, her Last Call coda) and nothing about who kept a fire for whom,
# so a departure, a closure or a Commander who never came back reads true, and nobody else's welcome is spoken for.
BILL_RECORD = (
    p('''{n}The grey dragon's bill for the smallest egg was never paid, and never cancelled. It was written against the Commander's name and no one else's; she had been particular about that.{/n}''',
      requires=(DV_BILL,), forbids=("devarra.lastcall.called",)),
    p('''{n}At the rift the grey dragon named her bill for the smallest egg, and it was not the hatchling and not the silver who raised her. It was a month of the Commander's every year, on her ridge.{/n}''',
      requires=(DV_BILL, "devarra.lastcall.called")),
)

# Polish: the domestic payoffs are the living partner's alone (epilogue.salt, whose page already needs the Commander alive
# or back). Never on a death page, a departure or a closure; flags never clear, so each forbids the ways she left as well.
GONE = (CLOSED, LEFT_WITH_IT, LIE_KEPT)
SALT_PARAGRAPHS = (
    p('''{n}The saddler whose name the Commander said at the fire below the east wall was never written down anywhere. Nine thousand, four hundred and some other names were never written down either. She kept them all, and taught the Commander one a night, when neither of them could sleep.{/n}''',
      requires=(P + "wake.name_said", COMMITTED), forbids=GONE),
    p('''{n}The grey dragon's bill for the smallest egg was never paid, and never cancelled. Once a year a scale the colour of eggshell was left on the Commander's windowsill, the way a creditor leaves a card. Nidalynn said that was only manners, and that dragons have excellent manners when they are owed something.{/n}''',
      requires=(DV_BILL, COMMITTED, "devarra.present_now"), forbids=("devarra.lastcall.called", "devarra.trickster.refused", *GONE)),
    BILL_RECORD[1],   # named at the rift: the same record, then what it cost at home
    p('''{n}Nidalynn kept the kiln banked high every winter the Commander was away on the ridge, and fed the Commander for a week when the Commander came back thinner. "Eat first," she said, every year, and put the bowl down. "Then tell me what she had you do."{/n}''',
      requires=(COMMITTED, DV_BILL, "devarra.lastcall.called", "devarra.present_now"), forbids=("devarra.trickster.refused", *GONE)),
)

# Historical debt persists after departure; it does not make the creditor visit.
SALT_PARAGRAPHS = (*SALT_PARAGRAPHS, p(BILL_RECORD[0]["Text"],
    requires=(DV_BILL, COMMITTED), forbids=("devarra.lastcall.called", "devarra.present_now", "devarra.trickster.refused", *GONE)),
    p('{n}Devarra never came back to a keeper. The grey tower stood empty. Her bill for the smallest egg remained '
      'in the account beside the kiln. No scales arrived at the Commander\'s window.{/n}',
      requires=(DV_BILL, COMMITTED, "devarra.trickster.refused"), forbids=("devarra.lastcall.called", *GONE)))

epilogue("salt", '''{n}Nidalynn stayed in Drezen after the war, in the old lime-kiln below the east wall, which she roofed with slate and never once let cool. The refugees who stayed called her the widow long after she stopped looking like one, and brought her their disputes, their broken bones and their bread, and she fed every one of them before she let them talk.{/n}
{n}She was never in a hurry. The Commander learned that it was not patience, exactly. It was that she had already decided, and she saw no reason to rush the part she was enjoying. When the Commander came home, she cleared the lime sacks from their bed herself. The next morning she opened the kiln door late, with her braid loose and no apology for it.{/n}''',
         requires=(COMMITTED,), forbids=(CLOSED, "sacrifice"), paragraphs=(*EPILOGUE_PARAGRAPHS, *SALT_PARAGRAPHS), **ALIVE)

epilogue("late", '''{n}The war ended before the young dragon was ready to fly. It flew in the spring after Threshold, off the kiln roof, badly, and then well, and circled Drezen three times shrieking while the whole city came out to point.{/n}
{n}That evening a tall woman with a white braid came up the citadel stair with a loaf of bread, a knife and a little salt folded in a paper, and put them on the Commander's table without a word, and sat down to wait. She broke salt onto two pieces and held one out. The Commander took it and ate; she ate hers, watching. "Now we're both of the same fire." That night she took the Commander to the private snowfield. By morning they had a kiln to return to and a city still needing breakfast.{/n}''',
         requires=(LATE_COMMITTED,), forbids=(COMMITTED, CLOSED, BREAD_KEPT, "sacrifice"), paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD), **ALIVE)

epilogue("heel", '''{n}The heel of the loaf stayed on the shelf in the kiln, wrapped in a cloth, long after it was stone-hard and good for nothing. She never moved it and never mentioned it.{/n}
{n}People who knew them both said that the Commander came down to the kiln more evenings than not, and that the two of them sat by the fire and talked until late, and that it was the most patient courtship anyone in Drezen had ever seen, and that it was not clear to anyone, including the two of them, which of them was doing the courting.{/n}''',
         requires=(BREAD_KEPT,), forbids=(COMMITTED, CLOSED, "sacrifice"), paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD), **ALIVE)

epilogue("wolves", '''{n}No wolves ever came over the east wall that winter, and the two sentries who were flogged for them never learned what had. At the thaw the woman from the jeweller's steps went north with a young red-black dragon, and did not come back, and did not write.{/n}
{n}On the kiln step she left a heel of bread and a pinch of salt, untouched, where the Commander would be sure to pass.{/n}''',
         requires=(GOAT_STANDS,), forbids=(GIVEN_UP, LIE_KEPT, LEFT_WITH_IT))   # polish r3: one closure page each

epilogue("unreturned", '''{n}When word came down from Threshold that the Commander would not be coming back, Nidalynn banked the kiln under the east wall and did not let it cool, that winter or any winter after. The young dragon was fed. The refugees were fed. She said the Commander's name at the fire the way she said the others, and every year on that night she set out bread and salt for one more than came, and ate her own share slowly, and was grateful, because she had said she would be.{/n}''',
         requires=("sacrifice",), forbids=("trickster.commander_back", CLOSED),
         RequiresAnyGroups=[[COMMITTED, LATE_COMMITTED, BREAD_KEPT]], paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD))

epilogue("apart", '''{n}The widow was gone from the jeweller's steps by the end of the war. The refugees said she had gone north with a young dragon that would not stay in a city, and that whatever she had said to the Commander she had said in the kiln, where nobody could hear it.{/n}
{n}Sometimes, when it snowed, a silver shape went over Drezen very high, and did not come down.{/n}''',
         requires=(MET, CLOSED), forbids=(COMMITTED, LEFT_WITH_IT, LIE_KEPT, GIVEN_UP, GOAT_STANDS), paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD))

epilogue("claimed", '''{n}The Commander kept a young woundwyrm in the kiln below the east wall for a season, and fed it, and called it the crusade's, and the crusade was proud of it for exactly as long as it took the creature to learn to fly.{/n}
{n}On the day it flew it went to her, not to the Commander, and she went with it. The kiln was cold by evening. The Commander's claim was good in every court in Mendev, and there was not one court in Mendev that could have enforced it.{/n}''',
         requires=(LEFT_WITH_IT,), forbids=(GIVEN_UP, LIE_KEPT), paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD))

epilogue("lie", '''{n}The Commander never said, in front of anyone who mattered, where the dragon in the kiln had come from. The widow did not say it either. She left Drezen at the first thaw with a young dragon under her shawl, and on the jeweller's step where she had sat all winter she left a heel of bread and a pinch of salt, untouched, where anyone could see them.{/n}''',
         requires=(LIE_KEPT,), forbids=(GIVEN_UP,), paragraphs=(*EPILOGUE_PARAGRAPHS, *BILL_RECORD))

epilogue("given", '''{n}The Commander gave the thing that came out of the rock to the chaplain's fire. The fire never got it. The old lime-kiln below the east wall lost its roof that night, all of a piece, and the lower town swears to this day that something silver went up out of the smoke, bigger than the sky over the tanners' stair, with something small and red held against its breast, and put out every torch in the lane as it passed.{/n}
{n}The widow was not seen on the jeweller's steps again. The Kellid women who had shared her step said she had never been a widow, and never been with child; but refugees will say anything.{/n}''',
         requires=(GIVEN_UP,))

def integrate(payload):
    """Her presences and her own Derived keys. World keys (the egg outcomes, the eggs_crated latch, Devarra's flags, the
    companions' guards) bind on demand in trickster_world."""
    # Extend only this route's Last Call entry, from its owning module. The shared file stays untouched.
    # Append once: make_expansion() can run repeatedly in the same interpreter.
    from storylines import lastcall_partners
    partner = next(part for part in lastcall_partners.PARTNERS if part["rel"] == REL)
    # Authored finale staging: rewrite only Nidalynn's own entry before the shared factory runs.
    # Existing paragraph/answer positions and terminal effects remain unchanged.
    partner["opener"] = "{n}When the Commander came home, Nidalynn opened the kiln door herself. She took one look, put the bread down and drew the Commander inside. The sergeant shut the door after them.{/n}"
    paragraphs = list(partner["paragraphs"])
    paragraphs[0]["Text"] = "{n}At the rift the Commander called over the broken ground. Nidalynn rose from the camp below, where she had waited with the young dragon. She landed beside the Commander, looked at the blood and torn clothes, and took the Commander's hand. Behind her the youngster screamed at the rift. Nidalynn stayed until the last decision was made.{/n}"
    paragraphs[3]["Text"] = "{n}That summer the young dragon visited the grey tower and came back with an eggshell-coloured scale caught under one claw. Nidalynn set it beside the Commander's bowl. The mother's bill still stood; raising her child had not paid it.{/n}"
    paragraphs[4]["Text"] = "{n}The young dragon visited her mother that summer and returned to the kiln. The grey one had named her bill at Threshold: a month of the Commander's every year. Before the first journey, Nidalynn heard the account at her own fire. She packed food for the ridge, and when the Commander came back she pulled out a chair beside hers.{/n}"
    for index in (3, 4):
        paragraphs[index]["Requires"] = list(dict.fromkeys([*paragraphs[index]["Requires"], "devarra.present_now"]))
        paragraphs[index]["Forbids"] = list(dict.fromkeys([*paragraphs[index]["Forbids"], "devarra.trickster.refused"]))
    paragraphs[5]["Text"] = "{n}The salt was still unbroken when the war ended. In spring she brought it to the Commander's table with a loaf and a knife. She broke it over two pieces of bread. The Commander ate the offered piece; she ate hers. \"Now we're both of the same fire.\" That night they flew to her snowfield, and in the morning came home together.{/n}"
    partner["paragraphs"] = tuple(paragraphs)
    spec = partner["call"]
    spec["text"] = "{n}You have heard her hum the herding-call at the kiln. Now she waits beyond the broken ground, by the Threshold camp. You put her name at the end and give it what breath you have left. Above the camp, silver wings open.{/n}"
    text, effects, requires, forbids = spec["choices"][0]
    spec["choices"][0] = ("[Listen. Beyond the broken ground, she answers.]", effects, requires, forbids)
    history = lastcall_partners.page_p('''Her husband had been a lie, like the belly under the shawl. There was no marriage waiting elsewhere while she kept the fire below Drezen's wall.''')
    if history not in partner["paragraphs"]:
        partner["paragraphs"] = (*partner["paragraphs"], history)
    additions = (
        lastcall_partners.page_p("She had followed the expedition as far as its camp. When no call came she returned to Drezen, banked the kiln and kept the fire through the night, with bread and salt in her lap. The young dragon sat beside her and would not sleep. When the Commander returned, she made room on the step and kept hold of the Commander's hand long after the bread was gone.",
            requires=(COMMITTED,), forbids=("nidalynn.lastcall.called",)),
        lastcall_partners.page_p("The grey tower stood empty. Her bill for the smallest egg remained against the Commander's name. Nidalynn kept the account beside the kiln; nobody's absence made it paid.",
            requires=(DV_BILL,), forbids=("devarra.present_now", "devarra.trickster.refused")),
        lastcall_partners.page_p("Devarra never came back to a keeper. The grey tower stood empty. Her bill for the smallest egg remained against the Commander's name; Nidalynn kept the account beside the kiln.",
            requires=(DV_BILL, "devarra.trickster.refused")),
    )
    for paragraph in additions:
        if paragraph not in partner["paragraphs"]:
            partner["paragraphs"] = (*partner["paragraphs"], paragraph)
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)
    have = payload.setdefault("SeenCues", {}).get(WOLJIF_SIGHED)
    if have is not None and have != ["d2f3ae3a8d7d0eb4aab722e777b7c260"]:
        raise ValueError("Conflicting binding: " + WOLJIF_SIGHED)
    payload["SeenCues"][WOLJIF_SIGHED] = ["d2f3ae3a8d7d0eb4aab722e777b7c260"]
    # PP10: the Storyteller's portal supplies (shared key; Delamere's bark binds the same cue).
    have = payload["SeenCues"].get(STORYTELLER_SUPPLIES)
    if have is not None and have != ["459bf324a71c81c4ba5f3eead9ba42bb"]:
        raise ValueError("Conflicting binding: " + STORYTELLER_SUPPLIES)
    payload["SeenCues"][STORYTELLER_SUPPLIES] = ["459bf324a71c81c4ba5f3eead9ba42bb"]
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'nidalynn.trickster.steps.widow',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
