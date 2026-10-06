"""Galfrey, Chapter 5 (T): Kitrane (the courtship on her presence in Drezen; 11-ROSTER-PLAN-2 §2 build sheet, R4).

She comes back from Iz as a knight of the Green Crows with an old sword and a borrowed month's wage, and stands where the crowd
is thickest: at the curio stall in the market square (beside the tiefling trader's stall in the lower town when the market
anchor cannot be found). Every beat opens from there.

The beats: her first morning (boots bought with her own coin); Sir Anselm, who went home in her coffin (the pivotal choice her
last decision reads); the elixir she will not take again (she will age); her hands (does the Inheritor still answer a paladin who
lies?); the Inquisitor at prayer; the Knight-Captain's silence; the dragon's sorcery (and the dragon); the order of one; the
ford (an order she may refuse); two false crowns (the Fool King); the farewell letter; the conversation the Queen kept putting
off; news from Nerosyan; the market reel. Then the commit (she kneels; the Commander refuses her oath), the release of an oath
accepted, the tent in the field camp, the war table, and her last choice: Kitrane for good, or the crown back after Threshold.
"""
import copy

from story_format import c, n, scene
from storylines.galfrey_trickster import (SEELAH_BED, MANU, CROWS_DREZEN, NATIVE_REFUSED, FINAL, FINISHED, LET_DIE, CARRIED_CROWS, CARRIED_IRABETH,
    ALONE, BLIND, CLOSED, COFFIN, COMMITTED, CROWN, DEAD, DISGUISED, DRILL, DREZEN, EULOGY_SIGN, EULOGY_LEGEND, EULOGY_TRUE,
    FAREWELL, FOREVER, KEPT, LETTER_BURNED, LETTER_MOOTED, NAMED, OFFER_REFUSED, P, PLANTED, READ, REFUSED_ORDER, REL, RENT,
    RETURNED, ROMANCE, SWORN, TENT, TERENDELEV_BACK, tag)

SCENES = []

HUB = "galfrey.presence"
HUB_FB = "galfrey.presence.stall"
HUB_FAILED = HUB + ".failed"
CURIO = "bad9f602b81a80047ac470b01ebe65a9"     # ExoticCapitalTrader (the market; Aranka front 2.5, Nenio behind 2.5: 3.5 m apart)
TIEFLING = "23eabf5b6364d4a4e86202dc5d27600b"  # Vendor_Tiefling (the lower town; Terendelev front 2.5, Mielarah behind 2.5)
# Anchor note: the build sheet's Hurlun_InDrezen (35733470) carries a PretendUnit component, so in game its Blueprint reports
# Hurlun (6b66b009) and E12b's NearUnit match (unit.Blueprint == anchor) would never find it. The market is used instead.

FIRST = P + "first_morning"
POSTPONED = P + "oath_postponed"          # she took the refused oath home to think; her answer comes 48 h later
ELIXIR = P + "kitrane.elixir_told"
HANDS = P + "kitrane.hands"
HULRUN_SEEN = P + "kitrane.hulrun_seen"
IRABETH_SPOKEN = P + "kitrane.irabeth_spoken"
IZ_SPOKEN = P + "kitrane.iz_spoken"
CROWS_ORDER = P + "kitrane.squire_sworn"
FORD = P + "ride.seen"
FORD_TRIAL = P + "ride.trial"
FORD_HANGED = P + "ride.hanged"
FORD_ANSWERED = P + "ride.answered"
FORD_PROMISED = P + "ride.promised"   # the Commander agreed to her terms; answered only once the visit is made   # the Commander met her terms after the hanging: the oath may be offered again
KING_SEEN = P + "kitrane.king_seen"
LETTER_SPOKEN = P + "kitrane.letter_spoken"
CONVERSATION = P + "kitrane.conversation"
MENDEV = P + "kitrane.mendev_news"
REEL = P + "kitrane.reel"
TABLE = P + "kitrane.war_table"

GREETING = ("{n}At the curio stall in the market square, where the crowd is thickest, a knight in plain armour with three black "
            "birds on her green surcoat is haggling over a pair of boots. She is losing, and appears to be enjoying it "
            "enormously.{/n}")
PRESENCES = {
    # Left of the curio trader: Aranka (front 2.5) and Nenio (behind 2.5) are each 3.5 m away.
    HUB: dict(Unit=DISGUISED, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=CURIO, Side="left", Distance=2.5),
              Requires=["trickster.ever", RETURNED], Forbids=[CLOSED, HUB_FAILED], MinChapter=5, MaxChapter=5,
              AnswerLists=[], Dialog="hub", Greeting=GREETING),
    # Fallback: right of the tiefling trader, 3.5 m out (E-Q7-33 live probe, Chapter 5 save, DrezenCapital: at 2.5 m a market
    # citizen stood 1.8 m from her; at 3.5 m the spot is 0.08 m from the mesh with room for her body; Terendelev front 2.5 and
    # Mielarah behind 2.5 are each about 4.3 m away).
    HUB_FB: dict(Unit=DISGUISED, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TIEFLING, Side="right", Distance=3.5),
                 Requires=["trickster.ever", RETURNED, HUB_FAILED], Forbids=[CLOSED], MinChapter=5, MaxChapter=5,
                 AnswerLists=[], Dialog="hub",
                 Greeting=("{n}Beside the tiefling trader's stall in the lower town, a knight of the Green Crows sits on "
                           "an upturned bucket, mending a boot strap with an awl and considerable profanity. Passers-by step "
                           "round her without a second glance. She seems to like that best of all.{/n}")),
}


def ki(id, text, *choices, **kw):
    return n(id, "Galfrey", text, *choices, portrait="Galfrey", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Galfrey", **kw)


def page(id, title, nodes, requires, forbids=(), delay=24, chapters=(5,), kind="visit", **extra):
    SCENES.append(scene(id, title, "Galfrey", min(chapters), "", nodes, requires=tuple(dict.fromkeys(requires)),
                        forbids=tuple(dict.fromkeys(forbids)), delay=delay, last=max(chapters), Relationship=REL,
                        Chapters=list(chapters), Remote=True, Kind=kind, **extra))


PLACES = ((HUB, "", ()), (HUB_FB, "_stall", (HUB_FAILED,)))


def beat(id, title, entry, nodes, requires, forbids=(), delay=0, **fields):
    """A beat opened from her presence (the curio stall, or the tiefling's): the same scene on each hub, each forbidding the
    other's completion."""
    for hub, suffix, extra in PLACES:
        twin = id + ("_stall" if not suffix else "")
        SCENES.append(scene(id + suffix, title, "Galfrey", 5, entry, copy.deepcopy(nodes),
                            requires=("trickster.ever", RETURNED, *requires, *extra),
                            forbids=(CLOSED, twin, *forbids), delay=delay, last=5, Relationship=REL,
                            Chapters=[5], Areas=[DREZEN], ContactUnit=DISGUISED, InteractionHub=hub, **copy.deepcopy(fields)))
        tag(id + suffix, "T")


# --- 1. The first morning: boots -------------------------------------------------------------------------------------------

beat(P + "after.first_morning", "Boots", '"Did you get your boots?"', [
    ki("start", '''"I did." {n}She lifts one foot for inspection: stout brown leather, badly stitched at the heel, a size too large.{/n} "Four silver. The stallholder asked five, I offered three, and he looked at me with such pity that I paid four and thanked him. In Nerosyan a steward would have settled it, and I would never have learned the price." {n}She flexes her toes inside the boot with evident satisfaction.{/n} "The Crows' paymaster advanced me a month's wage against my good character. Four silver and a lecture on thrift. I have spent the four silver."''',
        c('"And the lecture?"', "lecture"),
        c('"You were cheated."', "cheated")),
    ki("lecture", '''"I am saving it." {n}Perfectly grave.{/n} "He told me a knight who cannot keep a month's wage for a week will end by selling her sword. I have heard that same speech from my treasurer, in the council chamber, about the whole of Mendev. It was much more convincing in a tent, from a man with ink on his cuffs."''',
        c("Continue", "morning")),
    ki("cheated", '"Abominably." {n}She examines the heel of her new boot.{/n} "He told me a sad story about his mother. I did not believe him, and paid him anyway. Then he winked when he gave me my change." {n}Her mouth curves.{/n} "My steward would have settled it before I ever saw the boots. I should have missed the performance." {n}She flexes her toes.{/n} "They pinch. I shall wear them until they do not."',
        c("Continue", "morning")),
    ki("morning", '"I have been standing here since the sixth bell. Nobody has bowed. Nobody has asked me to decide anything." {n}She watches a woman go past with a basket of eels, a boy with a crate of chickens, two off-duty pikemen arguing about a girl.{/n} "I have cut my hair with the sergeant\'s knife and I wear the Crows\' old helm, and I find that nobody looks at the face under a minor order\'s helm; they look at the surcoat, and decide I am nobody, and look away. A child sold me a pie. It was cold in the middle. I ate it standing up, in the street, with my fingers." {n}Something moves in her face, and is mastered.{/n} "I ate it before anyone brought me a paper to sign. Cold pie, no silver, and I enjoyed it."',
        c('"What will you do with the rest of the day?"', "day"),
        c('[Flirt] "You have pie on your chin, Kitrane."', "chin")),
    ki("chin", '{n}Her hand goes to her chin before she can stop it. There is no pie on her chin. She looks at you for a long, flat second, with the whole century of her reign in it.{/n} "That," {n}says Kitrane of the Green Crows,{/n} "was impudent." {n}Then she laughs, a real laugh, and a pikeman turns to look.{/n} "You waited until my hands were full. Coward. Try it again when I can reach you."',
        c("Continue", "day")),
    ki("day", '''"Stand here." {n}Simply.{/n} "Watch. Learn what a city sounds like when nobody is afraid I am listening. Tomorrow I shall see about the Crows. There are two of them left, and a squire, and a tent that leaks." {n}She glances at you sidelong.{/n} "Come back when the war lets you. I find I watch the crowd for your face. It is a new habit. I have not decided yet whether I approve of it."''',
        c("[Leave her to the crowd.]", flags=(FIRST,)),
        c('[Flirt] "I\'ll make sure it\'s worth watching for."', flags=(FIRST,))),
], requires=(), forbids=(FIRST,), delay=6)


# --- 2. Sir Anselm's name (the choice her last decision reads) -----------------------------------------------------------------

beat(P + "kitrane.coffin", "Sir Anselm's name", '"You look like you\'ve had news."', [
    nar("start", '''{n}She has a folded broadsheet in one hand, a Nerosyan printing gone soft from the courier's saddlebag. She has read it enough times that the fold is starting to tear.{/n}''',
        c("Continue", "news")),
    ki("news", '''"They buried the Queen." {n}She hands you the broadsheet without looking at it.{/n} "In the crypt under the cathedral in Nerosyan, beside her father. Every bell in the city. The knights of three orders stood the vigil. The bishop wept, which I did not know he could." {n}Her finger finds a line lower down, and taps it.{/n} "And here. 'Among those missing at Iz: Sir Anselm Wray of the Green Crows, sixty-one years, of Nerosyan. His daughter asks any who saw him fall to write to her at the sign of the Three Keys.'"''',
        c('"She\'ll get no letter."', "letter"),
        c("[Say nothing. Wait.]", "letter")),
    ki("letter", '"She will get no letter." {n}Her voice stays level. She folds the broadsheet along its torn crease.{/n} "She will get a grave with no one in it, and a crypt with the wrong man in it, and a lifetime of looking at every grey-haired knight who comes through the gate." {n}She takes the broadsheet back and folds it, precisely, along its tearing seam.{/n} "I did that. I did it with my last breath as Queen, and I would do it again, and I cannot make those two things lie down together."',
        c('[He should have his name back] "One day Sir Anselm gets his name back. Even if it costs you the one you\'re wearing."',
          "named", flags=(NAMED,)),
        c('[He chose this] "He stood beside you so you\'d live. He\'s still standing there. Let him."', "kept", flags=(KEPT,)),
        c('[Coldly] "It\'s done. Grieving him won\'t unbury him, and you have a war to be useful in."', "cold", flags=(KEPT,))),
    ki("named", '''{n}She looks at you for a long breath, and then down at the broadsheet in her hands.{/n} "Even if it costs me mine." {n}She says it slowly, testing the weight.{/n} "You understand what you are saying. The only way to give him back his name is for someone to open that crypt and say who is in it, and the only person who can say so and be believed is the woman who is supposed to be lying there." {n}A pause.{/n} "Yes. I think that is right. I think I have known it was right since the milestone. I only wanted to hear someone else say it."''',
        c("Continue", "belt")),
    ki("kept", '''"Still standing there." {n}Her mouth twists.{/n} "That is what he would have said. He would have said it in a much louder voice, being deaf, and then asked me to repeat mine." {n}She folds the broadsheet away inside her surcoat, over her heart, and leaves her hand there.{/n} "Very well. He keeps his post. I shall try to be worth guarding."''',
        c("Continue", "belt")),
    ki("cold", '''{n}Her eyes come up, and for a moment it is the Queen who looks at you, and the Queen has had people removed from the council chamber for less.{/n} "Useful." {n}The word lands like a gauntlet on a table.{/n} "Yes. You would know about that; it is what I made you for." {n}She puts the broadsheet away.{/n} "You are right, and I shall not forgive you for it this week. Perhaps next week. Go away, Commander."''',
        c("Continue", "belt")),
    ki("belt", '''"I sent his daughter his sword-belt this morning. No letter. The courier was told to say it came from a knight who owed him a debt." {n}She looks out over the market.{/n} "She will know it is his. She will not know what it means. That is the most I can give her today, and it is a coward's gift, and I gave it anyway."''',
        c("[Stay with her a while.]"),
        c("[Leave her to her grief.]")),
], requires=(FIRST, COFFIN), forbids=(NAMED, KEPT), delay=12)


# --- 3. The elixir: she will age --------------------------------------------------------------------------------------------

beat(P + "kitrane.elixir", "The last dose", '"Is something wrong?"', [
    ki("start", '''{n}She is holding a small steel mirror, the kind soldiers use to shave, at arm's length, and frowning at it the way she frowns at a map with a bad road on it.{/n} "I have found a grey hair." {n}She turns the mirror so you can see, which you cannot.{/n} "Here. Above the left temple. I have not had a grey hair since I drank the second cup."''',
        c('"You\'re a hundred years old, Kitrane."', "old"),
        c('[Flirt] "It suits you."', "suits")),
    ki("suits", '''"Flatterer." {n}But she looks at the mirror again, and something in her frown eases.{/n} "The Queen would have had it plucked before breakfast by a lady of the bedchamber. Kitrane has only the one mirror, and it belongs to the Crows' sergeant." {n}She lowers it.{/n} "But that is not why I am frowning."''',
        c("Continue", "old")),
    ki("old", '"The church paid for two cups of sun orchid elixir. The priests said Mendev needed me. I accepted their decision, and drank." {n}She tilts the little mirror.{/n} "This hair may mean the second cup is wearing thin. I do not know. I have spent enough years trusting it not to."',
        c("Continue", "grow")),
    ki("grow", '''"I am going to grow old, Commander." {n}She says it very simply.{/n} "I had forgotten that it was a thing that happens to people. That one wakes one morning with a knee that aches in the rain, and a grey hair, and then another. I have been the same age for so long I had stopped noticing." {n}She is quiet.{/n} "I lay awake last night, and I could not tell whether I was frightened or glad. I think I was both, in turns, until the Crows' squire started snoring and I could no longer think at all."''',
        c('"Would the church buy another cup if you returned?"', "church"),
        c('"Does it frighten you?"', "frighten"),
        c('[Flirt] "Then I\'ll get to watch. I\'ve always wanted to see what you look like when you\'re sixty."', "watch")),
    ki("church", '"They might find another cup if I went back. They would ask for their Queen with it." {n}She lowers the mirror.{/n} "I accepted both cups. I shall not pretend I was forced to drink them. But I will take no third. I can still hold a sword when my hair is white."',
        c("[Leave it there.]", flags=(ELIXIR,))),
    ki("frighten", '''"A little." {n}She considers.{/n} "I have faced demons in the Wound and not been frightened. I have faced the bishops of Iomedae over a budget and been very frightened indeed. This is nearer the second." {n}A dry sideways look.{/n} "I shall take no third cup. Ask me in ten years whether I regret it, and I shall lie to you, and you will know, and we shall both be very civil about it."''',
        c("[Leave it there.]", flags=(ELIXIR,))),
    ki("watch", '''{n}She stares at you. Then she laughs, low and helpless, and has to put a hand on the stall to steady herself, and the curio-seller looks up in alarm.{/n} "Sixty." {n}She wipes her eyes.{/n} "Commander, I have been sixty. It was a very long time ago, and I had a great deal less patience then. You have no idea what you are asking for." {n}And then, lower, still smiling:{/n} "But you are asking to be there for it. That is not a thing people ask a queen."''',
        c("[Leave it there.]", flags=(ELIXIR,))),
], requires=(FIRST,), forbids=(ELIXIR,), delay=24)


# --- 4. Her hands: does the Inheritor still answer? --------------------------------------------------------------------------

beat(P + "kitrane.hands", "Lay on hands", '"There\'s blood on your gauntlet."', [
    ki("start", '''"Not mine." {n}She wipes it on her surcoat without a second thought, a soldier's gesture.{/n} "A carter's boy got his hand under a wheel an hour ago, just there. Crushed to the wrist. His mother was screaming for a priest, and there was no priest, and I was standing closest." {n}She looks at her own palm as though it belonged to someone else.{/n} "I have laid hands on the wounded every day of my life since I took my oaths. This morning I did not know whether I could."''',
        c('"Why wouldn\'t you?"', "why")),
    ki("why", '''"Because I am a paladin of the Inheritor, Commander, and I am living a lie." {n}Very quietly, so that the curio-seller cannot hear.{/n} "Iomedae does not ask much of her paladins that she does not ask of everyone. But she asks that we do not lie. I lied with my last breath as Queen and I have been lying every hour since, in a green surcoat, to a whole city in mourning." {n}Her hand closes.{/n} "I knelt by that boy and I thought: now I shall find out."''',
        c('"And?"', "and")),
    nar("and", '''{n}She opens her hand again. There is nothing to see in it: a swordswoman's palm, callused along the heel, with a thin old scar across the base of the thumb.{/n}
{n}"It came," she says. "The way it always comes. Like warm water. The bones went back where they belonged, and the boy stopped screaming and started crying, which is better, and his mother tried to kiss my feet and I would not let her."{/n}''',
        c('"Then the goddess doesn\'t mind."', "mind"),
        c('[Trickster] "Gods like a lie told for the right reasons more than their priests do."', "gods", mythic="Trickster"),
        c('"Maybe she\'s waiting to see what you do with it."', "waiting")),
    ki("mind", '"The boy\'s hand mended under mine. I am grateful. I shall still have to kneel in the chapel and answer for the coffin."',
        c("Continue", "end")),
    ki("gods", '''{n}Her eyebrows rise, and she very nearly rebukes you; then does not.{/n} "You would know better than I what the gods like, I suppose. You have been in rooms with more of them." {n}Drily:{/n} "Iomedae is not a god who enjoys a joke, Commander. But she has always had a great deal of patience with fools who mean well. I am counting on it. So, I suspect, are you."''',
        c("Continue", "end")),
    ki("waiting", '''"Yes." {n}At once, as if you had said something she has been saying to herself.{/n} "That is what I would do, in her place. Give the woman her power back, and watch what she spends it on." {n}She looks down at the stain on her surcoat.{/n} "A carter's boy. It is a better beginning than I deserved."''',
        c("Continue", "end")),
    ki("end", '''"The Queen had a chaplain to confess to. Kitrane has the Commander of the crusade, who is a very poor substitute, and does not even have the decency to wear a collar." {n}The corner of her mouth moves.{/n} "Thank you for listening. Go and win something. I shall stand here and try not to heal anyone else in public; the boy's mother has told the whole market."''',
        c("[Leave her to her market.]", flags=(HANDS,))),
], requires=(FIRST,), forbids=(HANDS,), delay=24)


# --- 5. The Inquisitor at prayer ---------------------------------------------------------------------------------------------

beat(P + "kitrane.hulrun", "The Inquisitor at prayer", '"Where were you last night?"', [
    ki("start", '''"At the chapel door." {n}She says it as though confessing to a tavern.{/n} "I go at the ninth bell. Inquisitor Hulrun is always there by then, on his knees before the altar, alone. He prays for the Queen's soul. By name. At length." {n}Her mouth twists.{/n} "He has a great deal to say to the Inheritor about her. Most of it is complimentary. I had no idea."''',
        c('"You stand there and listen?"', "listen"),
        c('"That\'s a risk you don\'t need to take."', "risk")),
    ki("listen", '"I stand at the back, in the dark, and listen." {n}She looks down at her new boots.{/n} "I have known that man thirty years. I have signed his warrants and argued with him over the fire and the rack until we were both hoarse. I have heard him condemn men without a tremor. He falters over these prayers." {n}Very low:{/n} "And every night he kneels on those stones, and is kind to me."',
        c("Continue", "sign", requires=(EULOGY_SIGN,)),
        c("Continue", "why", forbids=(EULOGY_SIGN,))),
    ki("risk", '"It is. I take it anyway." {n}Unrepentant.{/n} "Hulrun has hanged cultists on less evidence than a woman who stands at the back of a chapel with her hood up. I know. I read his reports." {n}She shrugs, a knight\'s shrug, armour creaking.{/n} "He keeps his eyes on the altar while I am there. I do not mistake that for blindness."',
        c("Continue", "sign", requires=(EULOGY_SIGN,)),
        c("Continue", "why", forbids=(EULOGY_SIGN,))),
    ki("sign", '"Last night he looked toward the door." {n}Her voice drops.{/n} "At the end, after the last amen. He turned his head and looked at the door, the way a man looks at a draught. I went away very quickly." {n}She meets your eyes.{/n} "He was in the chapel when you spoke of the Green Crows and the wounded they carried out. Hulrun is not stupid. He is a great many things I dislike, but he is not stupid."',
        c("Continue", "why")),
    ki("why", '"Do you know why I keep going? He grieves for the difficult woman who cut his budget as well as for the Queen. I have heard him condemn men without a tremor. He falters over these prayers." {n}A breath.{/n} "He misses her. I find that I owe him the courtesy of hearing it."',
        c('"Then keep going. I\'ll deal with it if he turns round."', "end"),
        c('"Stop. For both our sakes."', "stop"),
        c('"You could tell him."', "tell")),
    ki("stop", '''"No." {n}Not unkindly, but with the whole weight of a century behind it.{/n} "You may command a knight of the Green Crows in the field, Commander. You may not command her prayers." {n}Then, gentler:{/n} "I shall stand further back. That is the most I can promise."''',
        c("Continue", "end")),
    ki("tell", '"And make him choose between his Queen and his office?" {n}She shakes her head.{/n} "He would choose the office. He always has; it is why the Church keeps him. He would have to name what he saw at Iz a demon\'s trick, and me a thing wearing her face, and he would light the fire with his own hands and weep while he did it." {n}She looks toward the chapel.{/n} "No. The knights who carried me out would answer for it with me. So would you. I shall not lay that on them to ease his grief."',
        c("Continue", "end")),
    ki("end", '''"Kitrane has begun to pray for him in return. At the back, very quietly. It seems only fair." {n}The ghost of a smile.{/n} "I do not suppose the Inheritor has ever before had two people praying for each other's souls in the same chapel while one of them believes the other is dead. She must find it very instructive."''',
        c("[Leave her to her market.]", flags=(HULRUN_SEEN,))),
], requires=(FIRST,), forbids=(HULRUN_SEEN, "hulrun.dead", "hulrun.away_c5"), delay=24)


# --- 6. The Knight-Captain's silence -----------------------------------------------------------------------------------------

beat(P + "kitrane.irabeth", "The Knight-Captain", '"You were watching the barracks."', [
    ki("start", '''"I was." {n}She does not pretend otherwise.{/n}''',
        c("Continue", "alive", requires=(CARRIED_IRABETH,), forbids=("irabeth_dead",)),
        c("Continue", "alive", requires=(CARRIED_IRABETH, "irabeth_dead", "irabeth.trickster.returned")),
        c("Continue", "drezen", requires=(CROWS_DREZEN,), forbids=("irabeth_dead", P + "react.irabeth.learned")),
        c("Continue", "drezen_knows", requires=(CROWS_DREZEN, P + "react.irabeth.learned"), forbids=("irabeth_dead",)),
        c("Continue", "drezen", forbids=(CARRIED_IRABETH, CROWS_DREZEN, "irabeth_dead")),
        c("Continue", "drezen", requires=(CROWS_DREZEN, "irabeth_dead", "irabeth.trickster.returned"), forbids=(P + "react.irabeth.learned",)),
        c("Continue", "drezen_knows", requires=(CROWS_DREZEN, "irabeth_dead", "irabeth.trickster.returned", P + "react.irabeth.learned")),
        c("Continue", "died_back", requires=("irabeth_dead", "irabeth.trickster.returned"), forbids=(CARRIED_IRABETH, CROWS_DREZEN)),
        c("Continue", "gone", requires=("irabeth_dead", CARRIED_IRABETH), forbids=("irabeth.trickster.returned",)),
        c("Continue", "gone_before", requires=("irabeth_dead",), forbids=("irabeth.trickster.returned", CARRIED_IRABETH))),
    ki("alive", '''"Knight Tirabade crossed the square an hour ago. She passed within ten feet of me. She did not look." {n}Galfrey's hands are folded on the pommel of her sword, very still.{/n} "She salutes the Queen's empty chair at the high table every evening, I am told. She has not missed once. And she has not looked at me once since Iz. I laid the Queen's last lie on the one knight in Mendev who cannot tell one, and she carried it, and she will carry it until she dies."''',
        c('"She\'d forgive you if you asked her."', "ask"),
        c('"Do you want me to talk to her?"', "talk"),
        c('"She obeyed. That was her choice as much as yours."', "choice")),
    ki("ask", '''"Yes. I think she would." {n}Quietly.{/n} "That is exactly why I shall not ask. A queen who asks forgiveness of her knight is asking her for one more service, and I have had enough of hers." {n}She looks at the barracks door.{/n} "Let her be angry. She has earned that too. It is the one thing I left her that is entirely her own."''',
        c("Continue", "end")),
    ki("talk", '''"No." {n}At once.{/n} "Do not go to her on my account. Do not carry messages, or apologies, or anything else. She has been given enough to carry by people who outrank her." {n}A pause.{/n} "If she comes to you, and asks, tell her the truth. She would know if you did not. And tell her that the knight in the Crows' tent sleeps badly. She will not care. I should like her to know it all the same."''',
        c("Continue", "end")),
    ki("choice", '''{n}Galfrey turns her head and looks at you with something close to approval.{/n} "Yes. It was. You are the first person to say so." {n}A breath.{/n} "She could have refused me. She could have shouted it across the field at Iz. She looked at me, dying, with the order in her ears, and she decided I was worth one lie she would never have to tell. I shall spend the rest of my life trying to deserve that. It will not be enough."''',
        c("Continue", "end")),
    ki("gone", '"Knight Tirabade is dead." {n}She says it without looking away from the barracks.{/n} "She carried my last command out of Iz and then she did not come home. The Crows who carried me say she was quiet all the way to the gate. She had the order in her ears and nothing else." {n}Her hands tighten on the pommel.{/n} "I look at the barracks because I keep expecting her to come out of it. It is a habit. I have a great many habits I am going to have to break."',
        c("Continue", "end")),
    ki("drezen", '''"Knight Tirabade was in Drezen when I fell; the Queen had left her to hold the city. She does not know." {n}Galfrey's hands are folded on the pommel of her sword, very still.{/n} "She salutes the Queen's empty chair at the high table every evening, I am told. She wept for me in front of her whole company. And every day I stand in the same square as the most honest knight in Mendev and let her grieve a lie." {n}A breath.{/n} "The Crows carried me. They are old men and very discreet. She is neither, and she would never forgive them for it. So I keep my hood up."''',
        c('"She\'d want to know."', "ask"),
        c('"Do you want me to tell her?"', "talk")),
    ki("drezen_knows", '''"Knight Tirabade was holding Drezen when I fell, and the Crows' sergeant has told her, drunk, which he never is." {n}Galfrey's hands are folded on the pommel of her sword, very still.{/n} "She knows. She crosses the square every evening and does not look at me, and now it is a choice she makes, not a thing she does not see." {n}A breath.{/n} "I find I would rather be refused by her with her eyes open than grieved by her with them shut. It is a very small mercy. It is hers."''',
        c("Continue", "end")),
    ki("died_back", '''"Knight Tirabade fell at Iz before I could give her anything to carry, and came back, I am told, on some errand of yours." {n}Galfrey's hands are folded on the pommel of her sword, very still.{/n} "She crosses the square every evening. She has not looked at me once. I cannot tell whether that is because she does not know, or because she does." {n}A breath.{/n} "Either way, it is her silence. I shall not take it from her."''',
        c("Continue", "end")),
    ki("gone_before", '"Knight Tirabade is dead." {n}She says it without looking away from the barracks.{/n} "She fell at Iz before I could give her anything to carry. I called her name with my last command in my mouth, and two old Crows came instead." {n}Her hands tighten on the pommel.{/n} "I look at the barracks because I keep expecting her to come out of it. It is a habit. I have a great many habits I am going to have to break."',
        c("Continue", "end")),
    ki("end", '''"Go on, Commander. I shall stand here a while longer. The barracks has a very interesting door."''',
        c("[Leave her watching.]", flags=(IRABETH_SPOKEN,))),
], requires=(FIRST,), forbids=(IRABETH_SPOKEN,), delay=36)


# --- 7. The dragon's sorcery (and the dragon) --------------------------------------------------------------------------------

beat(P + "kitrane.iz", "The sorcery at Iz", '"Does the wound still trouble you?"', [
    ki("start", '''{n}She turns down the collar of her surcoat, briefly, so that you can see it: a pale, puckered seam running from her collarbone down under the mail, healed as if it were years old. There is no dark light in it now. There is nothing in it at all.{/n} "It aches in the cold. It will ache in the cold for the rest of my life, I expect. That is only a scar. I have a great many."''',
        c("Continue", "read", requires=(READ,)),
        c("Continue", "rent", forbids=(READ,))),
    ki("read", '''"It let go when the sergeant hammered the seal onto the Queen's coffin, with her name on the lid, after an hour in which I had no heartbeat at all. I felt it open like a hand." {n}She fastens the collar again.{/n} "I have thought about it a great deal since. You saw it flinch at my title. You wagered my life on what you saw. You were right, and you did not know that you were right, and you did it anyway."''',
        c("Continue", "dragon", forbids=(MANU,)),
        c("Continue", "priestess", requires=(MANU,))),
    ki("rent", '''"It let go when the bells rang. Not before." {n}Her voice catches on the last word, the faint tearing sound it makes now on certain syllables, and she waits for it to pass with the patience of long habit.{/n} "It left that behind. The priests of the Crows say it will not mend. I say I have had a century of speeches; the world can manage with fewer of mine."''',
        c("Continue", "dragon", forbids=(MANU,)),
        c("Continue", "priestess", requires=(MANU,))),
    ki("dragon", '''"Terendelev was our protector and friend." {n}She says it the way she said it at Iz, to her knights, before the charge; you can hear her remembering it.{/n} "I went to Iz to grant rest to her soul and her body. That was the duty. I would have done it with my own hands, and I very nearly did."''',
        c("Continue", "back", requires=(TERENDELEV_BACK,)),
        c("Continue", "rest", forbids=(TERENDELEV_BACK,))),
    ki("priestess", '''"It was not even the dragon." {n}Something wry in it.{/n} "I went into the Temple of Stone Manuscripts after the enemy's knowledge, because the Lexicon said it was there, and a priestess of the Lord of Locusts was waiting in the dark with exactly what she meant to use. She knew her work. It did not merely wound; it rent." {n}Her hand rests on the scar under her collar.{/n} "My knights put down what was left of Terendelev elsewhere in that city, without me. I was meant to be there. I went for the books instead."''',
        c("Continue", "back", requires=(TERENDELEV_BACK,)),
        c("Continue", "end", forbids=(TERENDELEV_BACK,))),
    ki("back", '''"And then I heard what you did at the bones." {n}She looks at you steadily.{/n} "You went into the fire after her. You opened your own wound over what was left, and a woman walked out, and now she sits on a crate in the lower town and lets children stare at her." {n}A long breath.{/n} "I have seen her. I went and stood across the street, in my hood, the way I stand at the chapel door. I did not cross it."''',
        c('"Do you hate her?"', "hate", forbids=(MANU,)),
        c('"Do you want to?"', "hate", forbids=(MANU,)),
        c('"Do you mind?"', "hate_manu", requires=(MANU,))),
    ki("hate_manu", '''"Mind." {n}She considers it with care.{/n} "It was not her that rent me; it was a priestess in the dark with her god's work in her hands. Terendelev was never mine to put down. My knights went to her while I went for the books, and I have thought since that I should have gone with them." {n}Drier:{/n} "So no, I do not mind that she walks the lower town. I mind that I was not there to say goodbye to her the first time. It seems I shall have to say good morning instead."''',
        c("Continue", "end")),
    ki("hate", '''"No." {n}She sounds almost surprised at herself.{/n} "It was not her claw that rent me. It was the thing he made of her bones. I have been a paladin long enough to know the difference between a sword and the hand on it." {n}Then, drier:{/n} "I envy her, a little, which is worse. She died, and she came back as herself, and the whole lower town knows her name. I died, and came back as a knight nobody has heard of." {n}A beat.{/n} "I granted her rest, and you undid it. You seem to make a habit of undoing my duties, Commander."''',
        c("Continue", "end")),
    ki("rest", '''"She is at rest. I made sure of that, at least, before the sorcery took me. It is the one thing I did at Iz that I am entirely certain of." {n}Her hand rests a moment on the scar under her collar.{/n} "Her voice used to carry across the whole square in Kenabres at the festival. I heard it once, when I was a young woman, and I thought: that is what the protector of a city should sound like." {n}She shakes her head.{/n} "Mine has a tear in it now, or it does not. Either way it was never that."''',
        c("Continue", "end")),
    ki("end", '''"Enough of scars. They are dull things to talk about, except to the people who have them." {n}She turns back to the crowd.{/n} "Come back when you have something more cheerful. A demon's head, say. Or a better pie."''',
        c("[Leave her to the crowd.]", flags=(IZ_SPOKEN,))),
], requires=(FIRST,), forbids=(IZ_SPOKEN,), delay=24)


# --- 8. The order of one -----------------------------------------------------------------------------------------------------

beat(P + "kitrane.crows", "An order of one", '"How are the Crows?"', [
    ki("start", '"Diminished." {n}She counts on her gauntleted fingers.{/n} "The sergeant, who is sixty and says so every morning. The squire, who is fourteen and says nothing at all. And me, who am new to this surcoat again and a hundred and some in every other respect. We have one tent, which leaks, and one mule, which bites." {n}She looks rather pleased about all of it.{/n} "The Green Crows were never a great order. Small enough that nobody checks. That was the point of them."',
        c('"And now?"', "now")),
    ki("now", '"And now a girl from the eel stall has asked to join." {n}She nods across the market, where a thin, sunburned girl of perhaps sixteen is gutting eels with savage concentration and glancing over every few moments.{/n} "Her brother died on the walls when the city was retaken. She wants to learn the sword. She asked me because, she said, I look like somebody who has never once been told no." {n}A dry breath.{/n} "I have been told no rather often since I joined their tent."',
        c('"Take her."', "take"),
        c('"You can\'t afford a squire on four silver a month."', "afford"),
        c('"Is it fair to make her a Crow? Kitrane is a lie."', "lie")),
    ki("take", '"I shall. The Crows cannot offer her silk or court tutors, but they can teach her to hold a sword." {n}She watches the girl put down her eel knife.{/n} "An appointment at court would have brought a family\'s petitions with it. This girl asked to fight demons. I can give her an answer myself."',
        c("Continue", "swear")),
    ki("afford", '"I cannot afford a mule on four silver a month, and I have one." {n}Unperturbed.{/n} "The sergeant says the girl can gut eels for the camp and sleep in the leaking half of the tent. My court squires had better beds. They would have complained about the eel smell." {n}She glances at you.{/n} "I shall take her. I only wanted you to argue with me first. Nobody argues with me any more. Kitrane is too unimportant."',
        c("Continue", "swear")),
    ki("lie", '''{n}She is quiet.{/n} "Kitrane is. The Crows are real enough: a minor order, small enough that nobody checks. But I made myself one of them in a war camp, and three good men wore my lie with me, and one of them is in my tomb." {n}She looks at the girl.{/n} "But a lie that people keep, and bleed for, and teach the sword under, becomes something else in time. I have seen it happen to kingdoms." {n}A dry note.{/n} "The first crusade was a handful of knights and a promise. Ask any Sarkorian what it looked like from their side of the river."''',
        c("Continue", "swear")),
    nar("swear", '''{n}She crosses the square without another word. You watch her stop in front of the eel stall; you watch the girl go white, and then red, and put down her knife and wipe her hands on her apron, twice. You cannot hear what Kitrane says. It is short.{/n}
{n}The girl kneels in the eel-guts and the straw, and Kitrane of the Green Crows puts her hand on the girl's head, and nobody in the market so much as looks up.{/n}''',
        c("Continue", "back")),
    ki("back", '''{n}When she comes back she is smiling the way people smile when they have been given something, not when they have given it.{/n} "She will be terrible. She holds a sword like an eel knife. She asked me whether the Crows fight demons, and I said they fight whatever the Commander points them at." {n}Her eyes glint.{/n} "So do point us at something worthy, Commander. I have a squire to impress."''',
        c('"I\'ll find you a demon."', flags=(CROWS_ORDER,)),
        c('[Flirt] "I thought I was the one you had to impress."', flags=(CROWS_ORDER,))),
], requires=(FIRST,), forbids=(CROWS_ORDER,), delay=24)


# --- 9. The ford (the pivotal node: an order she may refuse) ------------------------------------------------------------------

FORD_ORDERS = (
    c('[Order them hanged at the ford] "Hang them. All six. We don\'t carry cultists back through our own lines."', "hang",
      flags=(FORD, FORD_HANGED, REFUSED_ORDER), alignment=("Evil", 1)),
    c('[Order them sent to Drezen for trial] "Bind them. They go back to Drezen and answer for it there."', "trial",
      flags=(FORD, FORD_TRIAL)),
)

beat(P + "kitrane.ford", "The ford", '"I\'m riding out to clear the eastern ford. Will the Crows come?"', [
    ki("start", '''"The Crows will come." {n}She is already reaching for her helm.{/n} "All three of us, and the mule, and the squire, who will stay with the mule, whatever she says to the contrary."''',
        c("[Ride out.]", "ford")),
    nar("ford", '''{n}The eastern ford is a mile of reeds and brown water where a supply road crosses a stream, and a band of the Lord of Locusts' faithful has been cutting the throats of carters there for a week. They do not expect horses. They are wrong about a great many things, and that is the last of them.{/n}
{n}Kitrane fights like what she is: a knight of a hundred years' practice, without a single wasted movement, with no guard at her back, as she has not fought since she was a girl. When it is over she is splashed to the thighs and breathing hard, and she is laughing under her helm.{/n}''',
        c("Continue", "prisoners")),
    nar("prisoners", '''{n}There are six of them left alive, kneeling in the mud with their hands on their heads: four men, a woman with a locust burned into her cheek, and a boy of perhaps fifteen who will not stop shaking. Your soldiers are looking at you. So is the knight of the Green Crows, with her visor up and her sword still bare.{/n}''',
        *FORD_ORDERS,
        c('"Kitrane. You\'ve judged a hundred of these. You decide."', "decide")),
    ki("decide", '"I have judged prisoners and signed death warrants. These six surrendered to my sword. You command this column, and you will answer for what you order."',
        *FORD_ORDERS),
    ki("hang", '{n}Nobody moves. Then your sergeants start for the prisoners, because orders are orders.{/n}\n"No." {n}Kitrane sheathes her sword, very deliberately.{/n} "I will not." {n}She does not raise her voice; she does not need to.{/n} "Not the boy, not the woman, not the four men. They surrendered to a knight. A knight does not hang what surrendered to her at a ford for the convenience of the baggage train." {n}She looks at you across the reeds.{/n} "They surrendered to me. I accepted it in the Inheritor\'s name. Your order does not release me from that."',
        c('"Then stand aside. It will be done without you."', "hanged"),
        c('"Noted. Do it anyway, sergeant."', "hanged")),
    nar("hanged", '''{n}She stands aside. She watches it done, all of it, to the last kick of the last rope, and when it is done she mounts her horse and rides back to Drezen alone, at a walk, with her squire and the mule and the two old Crows strung out behind her like mourners.{/n}
{n}She does not speak to you that night, or the next morning. On the second day she is back at the curio stall, and nods to you, and says nothing about the ford at all. It is very much worse than shouting.{/n}''',
        c("[Let her be.]")),
    ki("trial", '{n}Something goes out of her shoulders that you had not known was there.{/n} "Bind them," {n}she tells the Crows\' sergeant, and then, to you, lower:{/n} "Thank you." {n}She watches the boy being hauled to his feet.{/n} "I have sent prisoners to the Inquisition before. Some were condemned. These six will have their names and charges heard before anyone brings a rope."',
        c('"You would have refused, if I\'d ordered them hanged?"', "would"),
        c("[Ride back to Drezen beside her.]", "home")),
    ki("would", '"Yes. I accepted their surrender. I should refuse that order whether I wore the Crows\' colours or Mendev\'s crown."',
        c("[Ride back to Drezen beside her.]", "home")),
    nar("home", '''{n}You ride back side by side, the prisoners stumbling on a rope behind the mule, the squire full of a battle she watched from a hillock. Halfway home Kitrane takes off her helm to let the wind at her hair, and does not put it back on, and three farmers at a gate stare at her as she goes by without the faintest idea why.{/n}''',
        c("[Let the road run out.]")),
], requires=(FIRST, CROWS_ORDER), forbids=(FORD,), delay=24)



# --- 9b. After the ford: her terms (the hanging is a breach until it is answered) ------------------------------------------------

beat(P + "kitrane.ford_after", "Six ropes", '"You haven\'t spoken to me since the ford."', [
    ki("start", '''"No." {n}She is standing very straight by the curio stall, in full armour, as if on parade.{/n} "I have been deciding whether to leave. The Crows' sergeant has packed the mule twice. I unpacked it twice." {n}Her hand is white on the pommel of the old sword.{/n} "There was a boy of fifteen at that ford, Commander. He surrendered to a knight. I have hanged men, and signed for the hanging of more, and I have never once hanged a boy who had put his hands on his head for me."''',
        c("Continue", "terms")),
    ki("terms", '"So. Terms." {n}The Queen\'s voice, the one that ended wars.{/n} "His name was Tobin; the Inquisition\'s clerk wrote it down before the rope. His mother sells tallow in the lower town. You will go to her yourself, and tell her who gave the order, and not send a clerk. Fifty from the crusade\'s coffers for his grave. You will put it in her hands yourself." {n}A breath.{/n} "And never again, under the Crows\' colours or near them. That is all. It is not small. It is not meant to be."',
        c('"Agreed. All of it. We go now."', "agreed"),
        c('"It was the right call. I won\'t apologise to a cultist\'s mother."', "refused")),
    ki("agreed", '''{n}She looks at you for a long breath.{/n} "Now. Yes." {n}She pulls her hood up.{/n} "I will walk behind you. It is your errand, not mine."''',
        c("[Walk down to the lower town.]", "tallow")),
    nar("tallow", '{n}The tallow-seller\'s stall is two streets below, where the gutters run grey. She is a small woman with burned hands, and she knows who you are before you open your mouth. You tell her anyway: that her son Tobin surrendered at the eastern ford with his hands on his head, that a knight of the Green Crows refused to hang him, that you gave the order and it was carried out.{/n}\n{n}She does not weep. When you put the purse for the grave down beside her hands she looks at it a long while, and pushes it back an inch, and then, slowly, draws it to her. "You came yourself," she says. "The knights never come themselves." She sets two tallow candles beside the purse. You take them and go.{/n}',
        c("Continue", "candle")),
    ki("candle", '''{n}At the top of the street Kitrane takes one of the candles out of your hand without a word, and puts it inside her surcoat, next to the broadsheet about Sir Anselm.{/n} "I will not forget the six of them, Commander," {n}she says quietly.{/n} "I do not ask you to. I ask you to remember them in the same place I do. The mule stays unpacked."''',
        c("[Stand beside her a while.]", flags=(FORD_ANSWERED,))),
    ki("refused", '''"Then I am your knight, and I shall do my duty, and there it will stay." {n}Without heat, which is worse.{/n} "The mule stays packed. When you are ready to walk down to the tallow-seller's, Commander, I shall still be here. I am old. I can wait." {n}She salutes.{/n}''',
        c("[Leave her.]", abort=True)),
], requires=(FIRST, FORD_HANGED), forbids=(FORD_ANSWERED,), delay=24)


# --- 21. The herald from Nerosyan (a discovery by someone with no reason to keep it) ------------------------------------------

ENVOY_PAID = P + "envoy.paid"
ENVOY_FACED = P + "envoy.faced"
ENVOY_SENT = P + "envoy.sent_home"

beat(P + "kitrane.envoy", "The herald from Nerosyan", '"Who is the man in the regency\'s colours?"', [
    nar("start", """{n}A herald in the blue and silver of the Mendevian regency is standing at the curio stall with his hat in his hand, and he is not buying anything. He is looking at the knight of the Green Crows, and he has gone the colour of tallow.{/n}
{n}Kitrane has not moved. She has one hand on the pommel of Sir Anselm's sword and her other hand very still at her side, and she is looking at him the way she used to look at ambassadors who had forgotten who they were addressing.{/n}""",
        c("Continue", "herald")),
    n("herald", "Herald of the regency", """"Commander." {n}His voice is not steady.{/n} "I served at court nineteen years. I carried her train at the jubilee. I would know that jaw at the bottom of a well." {n}He swallows.{/n} "The regents sent me to count the crusade's lances. I think I have found something they would pay a great deal more to know. Or a great deal more not to.\"""",
        c("[Pay him] \"Then take this, go home, and count lances.\"", "paid", flags=(ENVOY_PAID,), crusade=("Finances", -500)),
        c("[Send him home under escort] \"You'll be riding back to Nerosyan tonight, with two of my knights and nothing to report.\"", "sent", flags=(ENVOY_SENT,)),
        c("[Let her answer him] \"Ask her yourself.\"", "faced", flags=(ENVOY_FACED,))),
    n("paid", "Herald of the regency", """{n}He takes the purse. He does not look at it; he looks at her, and something in his face collapses.{/n} "I would have kept it for nothing, Your Majesty," {n}he says, very low.{/n} "I wanted you to know that. I am taking the money because I have four children." {n}He bows to the knight of a minor order, too deep, and goes.{/n}""",
        c("Continue", "after")),
    n("sent", "Herald of the regency", """{n}He goes pale, then red.{/n} "Under escort. Like a prisoner." {n}He looks at her, and at you, and at your knights already stepping in on either side.{/n} "The regents will ask why their herald came home early with nothing in his book. I shall tell them the crusade was very busy." {n}A pause.{/n} "They will not believe me. They never do.\"""",
        c("Continue", "after")),
    ki("faced", """{n}Kitrane steps forward. Not far; just into his light.{/n} "Master Orwen. You carried the train at the jubilee and trod on it twice, and I told the court it was the wind." {n}Her voice is perfectly level.{/n} "The Queen of Mendev is dead. You were at her vigil; you wept. Go home and tell the regents what you saw here: a knight of a minor order who looked, for a moment, like someone you loved. It happens to everybody who has lost someone. It will not happen to you again.\"""",
        c("Continue", "faced_after")),
    n("faced_after", "Herald of the regency", """{n}He stares at her for a long breath. Then he bows, exactly as deep as a herald bows to a knight of a minor order, not a hair further, and his hands are shaking.{/n} "As you say, Dame Kitrane. A knight who looked like someone." {n}He puts his hat on.{/n} "I shall write it in my book so. I shall not burn the page.\"""",
        c("Continue", "after")),
    ki("after", """{n}When he has gone she lets out a breath she has been holding since he walked up.{/n} "That will happen again." {n}Quite calm.{/n} "Not often; people see the surcoat. But there are nine hundred people in Mendev who have stood close enough to see my face, and some of them will come to Drezen. Every one of them is a door." {n}She looks at you.{/n} "I chose this, Commander. I did not choose for it to be free.\"""",
        c("[Stay beside her until her hand comes off the sword.]")),
], requires=(FIRST,), forbids=(ENVOY_PAID, ENVOY_FACED, ENVOY_SENT), delay=48)


# --- 10. Two false crowns (the Fool King) ------------------------------------------------------------------------------------

beat(P + "kitrane.king", "Two false crowns", '"I hear you\'ve been drinking with the King."', [
    ki("start", '''"I have." {n}She does not trouble to look abashed.{/n} "The Crows' sergeant said the tavern with the drunkard in the paper crown served the cheapest beer in Drezen, and a knight on four silver a month must economise." {n}A pause, beautifully timed.{/n} "He is the worst monarch I have ever met, Commander. I have met the Lord of Locusts' cultists, and they were better organised."''',
        c('"Did he recognise you?"', "recognise"),
        c('"You\'ve met a lot of monarchs."', "monarchs")),
    ki("recognise", '''"He did not recognise the Queen. He recognised a fellow sufferer." {n}Her mouth twitches.{/n} "He looked at me over his tankard and said I held my cup like somebody who was used to people watching her drink. He said he had the same trouble, since his coronation, and that the cure was to spill some, on purpose, early in the evening, so that everybody could stop waiting for it."''',
        c("Continue", "happy")),
    ki("monarchs", '''"Eleven. Two emperors, a prince of Taldor who could not read, and a great many kings and queens who could, and wished they could not." {n}She ticks them off with a dry precision.{/n} "Your King Thaberdine is the only one I have ever met who was happy. He has a crown of paper and a kingdom of drunks and a barrel he has made a baron, and he is happier than any of them. Including me."''',
        c("Continue", "happy")),
    ki("happy", '''"He offered me a seat on his council." {n}She shakes her head slowly.{/n} "I told him I had sat on one. He said then I knew how dull they were, and poured me another, and asked what I would do if I were queen." {n}A pause.{/n} "I told him the truth, because it was very late and the beer was very bad. I said I would abdicate the first chance I had, and go and be a knight of some small order that nobody had heard of."''',
        c("Continue", "said")),
    ki("said", '''"And he laughed until he fell off his throne, which is a bench, and said that was the only sensible thing a queen had ever said in his tavern, and knighted me with a sausage." {n}She keeps an entirely straight face.{/n} "So I am now a knight twice over, Commander. Once of the Green Crows, and once of the Kingdom of the Tavern, by royal sausage. I am told the barrel is my superior in rank."''',
        c('[Laugh] "Congratulations, Dame Kitrane."', "end"),
        c('"I made him king, you know."', "made")),
    ki("made", '''"I know. The whole tavern told me, at length, with gestures." {n}Her eyes rest on you, amused and something else.{/n} "You found a drunkard and a forged stone and made a king of him, and he is happy. You found a queen dying in the rubble and made a knight of her, and she is..." {n}She stops, and considers it with great care.{/n} "I had better not finish that sentence in a public market. You collect crowns, Commander, and give people the wrong ones, and somehow they fit."''',
        c("Continue", "end")),
    ki("end", '''"If the Queen of Mendev had ever drunk in that tavern she would have closed it by morning. Kitrane intends to go back on Oathday. He owes her a rematch at dice, and she suspects he cheats worse than she does."''',
        c("[Leave her smiling.]", flags=(KING_SEEN,))),
], requires=(FIRST, "fool_king.available"), forbids=(KING_SEEN,), delay=24)


# --- 11. The farewell letter -------------------------------------------------------------------------------------------------

beat(P + "kitrane.letter", "Forgive me", '"I\'ve read your letter. The one you hid in the wall."', [
    ki("start", '''{n}Her whole face stills, the way a pond stills under ice.{/n} "The Storyteller." {n}It is not a question.{/n} "Of course. He touched my goblet, I expect, and went rummaging in the wall like a housebreaker. That old man has no sense of privacy whatsoever. It is the one quality he shares with the Inquisition."''',
        c('"Are you angry?"', "angry"),
        c("[Quote it back to her] \"'I don't know where you are now. Are you even still alive?'\"", "quote")),
    ki("angry", '''"I am mortified." {n}Crisply.{/n} "It is worse. Anger is a thing a queen may permit herself in public. Mortification one must bear in private, and I have not got a private any more; I have a tent that leaks." {n}She looks at you, and some of the ice goes.{/n} "What did you think, when you read it?"''',
        c("Continue", "wrote")),
    ki("quote", '''{n}She closes her eyes.{/n} "Don't." {n}And then, as if she cannot help it, finishing it herself, low:{/n} "'I don't know what to do. But I am Queen and I must act accordingly.'" {n}She opens them again.{/n} "That line. That is the whole of my life, Commander, in one line. I did not know I had written my epitaph. I thought I was writing to you."''',
        c("Continue", "wrote")),
    ki("wrote", '''"I wrote it after I sent you into the Abyss, when no word came back. After the court had gone, and the candles were down, and I had done what the Queen had to do and could not undo it." {n}Her hand rests on the hilt of her old sword.{/n} "I did not know where you were. I did not know if I had killed you. I wrote 'forgive me' to someone who might be dead, and hid it in a wall so that nobody would ever read it, because a queen does not ask forgiveness in writing." {n}A breath.{/n} "And now I am the one who is dead, and you are the one who read it."''',
        c("Continue", "letter2", requires=(LETTER_MOOTED,)),
        c("Continue", "choice", forbids=(LETTER_MOOTED,))),
    ki("letter2", '''"You have two letters of mine, then." {n}A faint, crooked smile.{/n}''',
        c("Continue", "burned", requires=(LETTER_BURNED,)),
        c("Continue", "kept", forbids=(LETTER_BURNED,))),
    ki("burned", '"Or you had. One from the Queen, begging forgiveness from a wall. And one from Kitrane, the night before the Fane, which you burned in the Abyss because it named me. I approve. It was the right thing to do." {n}Drily:{/n} "It was also the one letter I wrote that I wished you had kept."',
        c("Continue", "choice")),
    ki("kept", '"One from the Queen, begging forgiveness from a wall. And one from Kitrane, the night before the Fane, which you carried through the Abyss next to your heart like a fool." {n}Her voice is not quite steady.{/n} "In one I asked forgiveness. In the other I asked where the road went. You kept both. I find that difficult to be sensible about."',
        c("Continue", "choice")),
    ki("choice", '''"What will you do with it?"''',
        c('"Give it back to you. It\'s yours."', "give"),
        c('"Keep it. You wrote it to me."', "keep"),
        c('"Answer it." [Take her hand.] "I forgive you."', "forgive")),
    ki("give", '''{n}She takes it from you, and looks at it, and without a word she folds it once more and tucks it inside her surcoat, next to the broadsheet about Sir Anselm.{/n} "The Queen's things," {n}she says.{/n} "I seem to be collecting them. I shall have a trunk of her soon, like any other widow."''',
        c("[Leave her with it.]", flags=(LETTER_SPOKEN, P + "kitrane.letter_returned"))),
    ki("keep", '''"I did." {n}A long breath.{/n} "Keep it, then. Keep it somewhere no Inquisitor goes. And if I am ever tempted to be the Queen again, show it to me, and remind me what she was like at the end of a day."''',
        c("[Put it away.]", flags=(LETTER_SPOKEN, P + "kitrane.letter_kept"))),
    ki("forgive", '{n}Her hand is cold and still in yours. Then her fingers close.{/n} "I wanted to hear it when I wrote the letter. I still did this morning." {n}She does not take her hand back.{/n}',
        c("[Hold her hand a moment longer.]", flags=(LETTER_SPOKEN, P + "kitrane.letter_kept"))),
], requires=(FIRST, FAREWELL), forbids=(LETTER_SPOKEN,), delay=24)


# --- 12. The conversation the Queen kept putting off (the native romance, remembered) ----------------------------------------

beat(P + "kitrane.conversation", "The conversation", '"You said we never had our conversation."', [
    ki("start", '''"I did." {n}She takes a breath like a woman stepping into cold water.{/n} "Very well. Here, then, among the eels and the curio-seller and his dreadful astrolabes. The Queen always meant to have it somewhere with a door that shut." {n}A dry glance.{/n} "Kitrane has discovered that doors are overrated."''',
        c("Continue", "camp")),
    ki("camp", '''"In the war camp you flirted with me, and I told you that if you wanted to impress me, you would have to do better than that. Do you remember?" {n}She does not wait.{/n} "You did better. You did a great deal better, over and over, all the way to Drezen and out of it, and I noticed every time, and I told you nothing, because a queen does not." {n}Her jaw sets.{/n} "In Drezen, before the Fane, I stopped you on the stair and asked to speak with you alone. I nearly said it then. I said something about strategy instead."''',
        c('"What would you have said?"', "said"),
        c('[Flirt] "Say it now. Nobody\'s listening."', "said")),
    ki("said", '''"That I did not want a Knight Commander." {n}Very low, and very clear.{/n} "I had a hundred of those. I wanted you. The stubborn, impossible creature who looked at a map of the Worldwound as if it were a puzzle somebody had left out for them. I wanted to be the one person in the world you did not treat as a puzzle." {n}A breath.{/n} "And then I sent you into the Abyss, because the Queen had to. And wrote 'forgive me' to a wall."''',
        c("Continue", "now")),
    ki("now", '"So." {n}She squares her shoulders.{/n} "I am accustomed to keeping the court waiting. I find I am less patient about this conversation." {n}The corner of her mouth moves.{/n} "You do know who she is. That is the difficulty."',
        c('[Kiss her] "I know exactly who she is."', "kiss", flags=(CONVERSATION,)),
        c('"I\'ve been waiting a long time to hear that."', "waited", flags=(CONVERSATION,)),
        c('[Flirt] "Then I\'ll court you properly. With flowers, and a very bad poem."', "slow", flags=(CONVERSATION,))),
    nar("kiss", '''{n}She lets you. Her mouth is warm and startled and then not startled at all; her gauntleted hand comes up and closes on the back of your neck, hard, a sword-hand, and holds you there as if you might be taken away.{/n}
{n}When she lets go, the curio-seller is staring at you both with his mouth open, and she turns and gives him a look that has made ambassadors withdraw. He finds something very interesting to do with a box of amulets.{/n}
{n}"There," says Kitrane, a little breathless. "That was overdue."{/n}''',
        c("[Leave her before either of you says anything foolish.]")),
    ki("waited", '''"I know." {n}A flicker of the old severity.{/n} "I kept you waiting deliberately. It is an old habit of monarchs. It establishes the terms." {n}Then, much softer:{/n} "I have no terms left to establish. I find that I do not want any. It is a very alarming feeling, Commander, and I should like you to go away now so that I can have it in private."''',
        c("[Go, smiling.]")),
    ki("slow", '''"A poem." {n}She looks at you as if you had offered her something rare and slightly alarming.{/n} "I have had odes written to me by three court poets and a prince of Taldor who rhymed 'Galfrey' with 'palfrey' for eleven stanzas." {n}The corner of her mouth goes.{/n} "Make it worse than his. I shall know if you do not try."''',
        c("[Leave her with that.]")),
], requires=(FIRST, ROMANCE), forbids=(CONVERSATION,), delay=36)


# --- 13. News from Nerosyan ---------------------------------------------------------------------------------------------------

beat(P + "kitrane.mendev", "News from Nerosyan", '"More broadsheets?"', [
    ki("start", '''"More broadsheets." {n}She has three of them spread on the curio-seller's counter, weighted with his brass, and he has given up protesting.{/n} "They say the council of regents in Nerosyan met four times this week and agreed on nothing but the colour of the mourning. They say a cousin of mine in the south has discovered a great-grandmother he never mentioned before. They say the knights of two orders have gone home to guard the border, because without the Queen, why stay?"''',
        c('"How much of it is true?"', "true"),
        c('"Does it hurt, reading it?"', "hurt")),
    ki("true", '"The knights are leaving. I can see the gaps on the muster boards." {n}She lays her hand flat on the paper.{/n} "A dead Queen, an unpaid army, and claimants measuring the empty throne. I knew what my death would do to our forces. Knowing has not made it easier to read."',
        c("Continue", "tempt")),
    ki("hurt", '"I appointed those regents for the day I could no longer rule. I expected arguments. I did not expect them to send for men we still need here." {n}She taps the muster figures.{/n} "The reports from the Wound should be on their table beside these claims of descent. I doubt anyone has opened them."',
        c("Continue", "tempt")),
    ki("tempt", '"I could show them my face." {n}Her hand closes on the broadsheet.{/n} "Then they would demand the coffin opened, the surgeon questioned, and every knight who carried me brought before an inquiry. Those knights are in your column. The lords would fight over who had the right to summon them." {n}She looks toward the citadel.{/n} "I can answer for the lie. I will not hold up the army while they decide how to hear it."',
        c('"Mendev still needs its Queen. What would bringing you back cost the army?"', "go"),
        c('"Keep the column moving. They must govern while we finish the war."', "learn"),
        c('"Would they believe you if you walked into the council?"', "could")),
    ki("go", '"An inquiry now, and the officers you need on the road called home as witnesses. Some would obey the summons. Some would refuse it. The rest would wait for me to give them an order." {n}She folds the paper.{/n} "After the war I can face them. Today we have to keep the men who are still willing to fight."',
        c("Continue", "orders")),
    ki("learn", '"Yes. For now." {n}She draws the muster board toward her.{/n} "I shall not call desertion a lesson in government. They are frightened, their wages are overdue, and the regents are offering them a reason to go home. We must answer that."',
        c("Continue", "orders")),
    ki("could", '"Some would. Others would call me an impostor until it suited them to believe me. A few would kneel and ask whose lands I intended to confiscate." {n}She gives the paper a hard crease.{/n} "You would get no troops from that quarrel in time for this campaign."',
        c("Continue", "orders")),
    ki("orders", '"The Eagle Watch stays. The Crimson Bridle and the Southern March are leaving: two hundred lances. Their paymaster says nobody has paid them since Iz." {n}She studies the figures.{/n} "That money came from my privy purse. The purse belongs to a dead Queen now. It is my doing. Paying the arrears may keep them here; it will not settle the succession."',
        c('[Pay 400 Finances] "Pay the arrears. Keep the lances here."', "paid", flags=(MENDEV, P + "mendev.paid"), crusade=("Finances", -400)),
        c('[Spend 150 Favors] "Let them guard Mendev. Send Kitrane the recruits for Drezen."', "let_go", flags=(MENDEV, P + "mendev.let_go"), crusade=("Favors", -150))),
    ki("paid", '"Four hundred for two hundred lances. Pay the men before their officers find another reason to leave." {n}She returns the muster.{/n} "That buys their service for this campaign. After the war, the regents will still want their witnesses. So will Anselm\'s daughter."',
        c("[Leave her with her papers.]")),
    ki("let_go", '"Mendev\'s border needs guarding too. I will not pretend that makes these gaps harmless." {n}She reads the numbers once more.{/n} "Send me the recruits left to hold Drezen. I can drill them and keep the Crows on the walls while your veterans go forward. It will not replace two hundred lances. It is what I can do here."',
        c("[Leave her with her papers.]")),
], requires=(FIRST,), forbids=(MENDEV,), delay=48)


# --- 14. The market reel -------------------------------------------------------------------------------------------------------

beat(P + "kitrane.reel", "The market reel", '"There\'s music in the square."', [
    nar("start", '''{n}Somebody has brought a fiddle to the market, and somebody else a drum made from a crusader's shield, and in the space between the eel stall and the curio-seller a ring of off-duty soldiers and market women is stamping through a reel that is older than Mendev. Kitrane stands at the edge of it with her arms folded, watching the way she watches everything.{/n}''',
        c("Continue", "watch")),
    ki("watch", '"I have danced at every court between Nerosyan and Absalom. Pavanes. The slow galliard. A thing in Taldor that takes forty minutes and involves a fan." {n}Her foot is keeping time on the cobbles, apparently without her knowledge.{/n} "I have never once danced this. I watched this one from a balcony at the harvest fair. From there I could never see how they kept their feet out of each other\'s way."',
        c('[Offer your hand] "Find out."', "dance"),
        c('"Nobody\'s stopping you."', "dance")),
    nar("dance", '{n}She watches one more turn, then unbuckles her sword-belt and offers you her hand.{/n}',
        c("Continue", "breath")),
    nar("breath", '''{n}When the fiddler finally takes pity on everyone and stops, she is flushed to the ears and her hair has come out of its tie, and she is holding onto your arm with both hands as if the cobbles might tip her over. Her breath is warm against your jaw. Somebody whistles.{/n}
{n}"Commander," she says, low, not letting go. "Do you know the most extraordinary thing about being nobody?"{/n}''',
        c('"Tell me."', "nobody")),
    ki("nobody", '"If you kissed me now, the fiddler would play louder and that pikeman would whistle. I would rather hear them than another council\'s questions about the succession."',
        c("[Kiss her in front of the whole market.]", "kissed", flags=(REEL,)),
        c('[Flirt] "Then I\'ll save it for somewhere they can\'t whistle."', "saved", flags=(REEL,))),
    nar("kissed", '{n}They whistle. They go back to their eels. The fiddler strikes up again, something slower, and a pikeman with a bruised foot shouts something about officers that makes Kitrane laugh into your mouth.{/n}\n"There," {n}she says when she can.{/n} "Nobody wrote it down." {n}She does not let go of you for some time.{/n} "I heard the whistle. I shall forgive him if you keep hold of me."',
        c("[Stay for the next dance.]")),
    ki("saved", '''"Somewhere they cannot whistle." {n}Her mouth curves slowly.{/n} "You are a very careful strategist, Commander. I have always admired it in you. I am beginning to find it maddening." {n}She lets go of your arm at last, and retrieves her sword-belt, and buckles it on without looking at it.{/n} "Choose the ground well. I intend to hold you to it."''',
        c("[Leave her flushed and laughing.]")),
], requires=(FIRST, HANDS), forbids=(REEL,), delay=24)


# --- The commit: she kneels, and the Commander refuses her oath ---------------------------------------------------------------

beat(P + "commit.oath", "The oath", '"The Crows\' sergeant says you asked for me."', [
    nar("start", '{n}It is dusk, and the market is closing: shutters going up, the eel-girl sluicing her stall, the curio-seller counting his takings with his back to the wall. Kitrane is waiting by the stall in her plain armour, polished until it looks almost new, with her old sword at her hip and the green surcoat freshly brushed.{/n}\n{n}"I did," she says. "I have something to say to you. The market is closing; at least nobody will call a clerk to record it."{/n}',
        c("Continue", "ford", requires=(REFUSED_ORDER,)),
        c("Continue", "trial", requires=(FORD_TRIAL,)),
        c("Continue", "speak", forbids=(REFUSED_ORDER, FORD_TRIAL))),
    ki("ford", '"I refused you at the ford, and you hanged them anyway, and then you walked down to the tallow-seller\'s, as I asked." {n}She says it first, so that it is out of the way.{/n} "I would refuse you again. I want you to know that I have not forgotten the six of them, and that I have come anyway, and that what I am about to do is not obedience. You paid for Tobin\'s grave. That did not make your order right. I have come to offer service, and I shall refuse such an order again."',
        c("Continue", "speak")),
    ki("trial", '''"At the ford you sent six cultists back to Drezen to stand trial, when you had a rope and a tree and nobody to stop you." {n}She nods, once.{/n} "I watched you decide. That is why I am here."''',
        c("Continue", "speak")),
    ki("speak", '''"A knight of the Green Crows owes service. I have lived on the Crows' pay and your army's bread since I walked out of Iz, and I have sworn to nobody. That is not how a knight lives." {n}She draws her sword. Then, in the straw and the eel-water and the last of the light, the Queen of Mendev goes down on one knee in front of you and holds it out, hilt first, across her forearm.{/n}''',
        c("Continue", "oath")),
    ki("oath", '"Kitrane of the Green Crows offers her sword to the Commander of the Fifth Crusade." {n}Her voice is quite steady, and carries no further than it needs to.{/n} "In the Inheritor\'s sight, to serve until released or dead." {n}She looks up at you.{/n} "I gave you an army and a title. Tonight I am offering my own sword."',
        c("Continue", "crowd")),
    nar("crowd", '''{n}Nobody in the market so much as turns their head. A knight kneeling to an officer is nothing; there are a dozen such oaths sworn in Drezen every week. At the eel stall a thin girl has stopped sluicing and is holding her breath. Otherwise the world goes on shutting up for the night around the Queen of Mendev on her knees in the straw.{/n}''',
        c('[Refuse her oath; offer your hand] "No. I won\'t take your sword. Get up."', "refuse"),
        c('[Accept her oath] "I accept it. Rise, Kitrane of the Green Crows."', "sworn", flags=(SWORN,))),
    ki("refuse", '''{n}She does not get up. She stays exactly where she is, with the sword across her arm, and looks at your outstretched hand as though it were a piece of very bad news from the front.{/n} "You refuse the fealty of a knight. In the middle of a market." {n}Very evenly:{/n} "I have had oaths refused before, Commander. Always by people who wanted something better. What do you want?"''',
        c('"I don\'t want your sword. I want you."', "yes"),
        c('"Keep your sword. I am asking whether you want to stay beside me."', "yes"),
        c('[Flirt] "I want you on your feet, so I can kiss you properly."', "yes"),
        c('"Whatever you choose to give. Take as long as you need."', "postpone")),
    ki("postpone", '{n}She sheathes the sword and rises without your hand.{/n} "Not tonight. I want to answer after I have stopped wondering who saw me kneel." {n}She touches two fingers to your wrist.{/n} "Two days. Ask the Crows\' sergeant where I am."',
        c("[Let her go.]", flags=(POSTPONED,))),
    ki("yes", '''{n}For the space of a breath the Queen of Mendev looks at you with the whole of her reign in her face: every envoy, every oath, every knight she ever sent into the Wound.{/n}
{n}Then Kitrane sheathes her sword, and takes your hand, and lets you pull her up out of the straw, and does not let go.{/n} "Then I shall have to find something else to give you." {n}Her other hand comes up to your face.{/n} "And I find I know exactly what."''',
        c("Continue", "kiss")),
    nar("kiss", '{n}She holds your jaw between fingers rough from the sword. The first kiss is brief; she draws back just far enough to look at you, then catches your lower lip with hers and brings you close. A brass astrolabe hits the cobbles beside the stall. She laughs into your mouth before letting you breathe.{/n}',
        c("Continue", "invite")),
    ki("invite", '"The Crows\' tent is at the end of the minor orders\' row in the field camp. It leaks on the left. The sergeant sleeps like a stone and the squire has been sent into town with the mule; I have already arranged it." {n}She steps back, and her eyes are very bright, and very steady.{/n} "Come tonight, after the ninth bell. Bring nothing. Do not keep me waiting, Commander."',
        c('"I\'ll be there."', flags=(COMMITTED,)),
        c('[Flirt] "Is that an order, Kitrane?"', "order_q")),
    ki("order_q", '''"From a knight of a minor order to the Commander of the crusade?" {n}She lets the corner of her mouth go.{/n} "Certainly not. It is a promise. I have been told I am rather good at keeping those."''',
        c('"Then I\'ll be there."', flags=(COMMITTED,))),
    ki("sworn", '''{n}She rises at once, smoothly, and salutes, and the sword goes back into its scabbard with a click.{/n} "Commander." {n}It is correct. It is entirely correct.{/n} "The Green Crows are at your disposal: one knight, one sergeant, one squire, one mule. Point us at something."''',
        c("Continue", "sworn2")),
    ki("sworn2", '''{n}Something in her face has closed, gently, like a book.{/n} "The Queen had knights. I used to wonder what it was like from their side." {n}A pause.{/n} "It is very simple, it turns out. One knows exactly where one stands." {n}She salutes again.{/n} "Good night, Commander."''',
        c("[Return the salute.]")),
], requires=(FIRST,), forbids=(COMMITTED, SWORN, POSTPONED, FORD_HANGED), delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED},
    RequiresAnyGroups=[[REEL, CROWS_ORDER, KING_SEEN, CONVERSATION], [NAMED, KEPT, HANDS, ELIXIR, LETTER_SPOKEN]])


# --- Her answer, two days on (after her own postponement) -----------------------------------------------------------------------

beat(P + "commit.answer", "Two days", '"The Crows\' sergeant says you have an answer."', [
    ki("start", '"I have." {n}Her hands rest on Sir Anselm\'s sword.{/n} "I spent one day angry that you had let me go, and another angry that I had gone. That is a foolish way to prepare an answer." {n}She looks at you.{/n} "The Crows ride before dusk. I shall have to stop thinking about you long enough to check their pickets."',
        c('"And?"', "answer"),
        c("[Wait.]", "answer")),
    ki("answer", '"Yes. I considered the question when you were not there to make the answer easier." {n}She steps close and kisses you hard enough to stop your reply.{/n} "The Crows\' tent. After the ninth bell. Bring nothing."',
        c('"I\'ll be there."', flags=(COMMITTED,)),
        c("[Kiss her back.]", flags=(COMMITTED,))),
], requires=(POSTPONED,), forbids=(COMMITTED, FORD_HANGED), delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED})


# --- The release: the soft no answered ----------------------------------------------------------------------------------------

beat(P + "commit.release", "Released", '"I have something to say to my knight."', [
    ki("start", '"Commander." {n}She straightens and gives the formal salute used for reports.{/n} "The Crows are ready. What are your orders?"',
        c('[Release her from the oath] "I release you, Kitrane. From the oath, and from my service."', "release"),
        c('"Nothing. Carry on."', abort=True)),
    ki("release", '{n}She does not move.{/n} "The Crows release service for death, disgrace, or another duty that must come first. That is the oath I offered. I am alive and have kept it." {n}Her eyes stay on yours.{/n} "What has changed, Commander?"',
        c('"I was wrong to take it. I should have refused."', "choose"),
        c('"I accepted service when you offered company. I would rather hear your answer now."', "choose"),
        c('"I don\'t want a knight. I want Kitrane."', "choose"),
        c('[Command her] "You\'re released. Now come to my tent tonight."', "ordered")),
    ki("ordered", '{n}Her face stills. She salutes precisely.{/n} "You cannot release my service and summon my bed in the same breath. No, Commander." {n}She turns on her heel.{/n} "When you know the difference, you know where the Crows\' tent is. Until then I am your knight, and nothing else."',
        c("[Let her go.]", abort=True)),
    ki("choose", '{n}She studies you, then lowers the hand that had begun another salute.{/n} "You took the oath I offered. I cannot fault you for accepting it. I can ask what you meant by releasing it." {n}She glances toward the Crows\' tents.{/n} "They ride tonight. I would rather settle this before they do."',
        c("Continue", "yes")),
    ki("yes", '{n}She steps close and puts her hand flat on your chest.{/n} "I want you to come tonight. The Crows\' tent, after the ninth bell."',
        c('"I\'ll be there."', flags=(COMMITTED,)),
        c('[Kiss her] "Consider it an order refused."', flags=(COMMITTED,))),
], requires=(SWORN,), forbids=(COMMITTED, FORD_HANGED), delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED})


# --- The Crows' tent (a visit: the night, the threshold, the cut, and the morning drill) ----------------------------------------

page(P + "visit.tent", "The Crows' tent", [
    nar("start", '''{n}The field camp outside Drezen is dark but for cookfires, and the minor orders' row is the darkest part of it. At its far end a tent sags a little to the left, and a mule tethered by the flap lays back its ears at you as you pass. From somewhere inside the next tent a sergeant of sixty is snoring, pointedly.{/n}
{n}A single lantern is burning inside the Crows' tent. Kitrane is standing beside it in full plain armour, as if for inspection.{/n}''',
        c("Continue", "armour")),
    ki("armour", '"I kept it on." {n}She holds out her gauntleted hands.{/n} "I have had squires take me out of armour for most of my life. Tonight I want your hands doing it." {n}Her chin lifts.{/n} "Gauntlets first. Then the straps under the pauldrons. I shall try not to correct you more than necessary."',
        c("[Start with the gauntlets.]", "buckles"),
        c('[Flirt] "Your Majesty\'s armourer, at your service."', "majesty")),
    ki("majesty", '''"Don't." {n}But she is laughing, low in her throat.{/n} "Or do. There is nobody here to hear it but the mule, and I am told the mule has no politics." {n}She holds out her hands.{/n} "Gauntlets first. Then I shall instruct you, since you clearly need it."''',
        c("[Start with the gauntlets.]", "buckles")),
    nar("buckles", '{n}One pauldron comes away. She taps the strap you missed beneath the other and gives you a long, severe look.{/n} "Have you only ever done this to corpses?" {n}Your fingers catch at the wrong buckle again. She laughs, braces herself against your shoulder, and reaches behind her own back to help.{/n}',
        c("Continue", "mail")),
    nar("mail", '''{n}The cuirass comes away, and the tassets, and the mail she shrugs off herself with a soldier's practised twist. Underneath she is in a padded arming doublet, dark with sweat at the collar, and she stops laughing.{/n}
{n}She unlaces the doublet herself, slowly, watching you the whole time, her fingers very sure. Under it the linen is thin and old. At her collarbone the pale seam of Iz runs down beneath the cloth, and she does not try to hide it. She takes your hand and lays it there, over the scar, and holds it.{/n}''',
        c("Continue", "want")),
    ki("want", '"It still aches in the cold." {n}She holds your hand against the seam at her collarbone, then brings your fingers to her mouth.{/n} "Tonight it can wait." {n}Her voice roughens.{/n} "I want you. I have made a great many preparations for this war, Commander. Getting you out of that shirt should require fewer."',
        c("[Kiss the scar.]", "scar"),
        c("[Let her lead.]", "lead")),
    nar("scar", '''{n}You bend your head and put your mouth to the seam of it, and she draws a breath like a woman surfacing from deep water. Her hands go into your hair, and pull, and hold you there, and then drag you up to her mouth.{/n}''',
        c("Continue", "bed")),
    nar("lead", '{n}She unfastens your collar, slowly now, and kisses the skin beneath it. Her callused palm rests against your ribs; when you move closer, she keeps you still until the next fastening is open. She raises her eyes to yours and smiles, then draws the loosened shirt from your shoulders.{/n}',
        c("Continue", "bed")),
    nar("bed", "{n}She pulls the linen over her head. The lantern lights her breasts, the hard muscle of her shoulders, and the pale seam descending from her collarbone. She leaves the cloth where it falls. Three saddle-blankets and a cloak make the Crows' bed; she catches your wrist and draws you down onto it. Your remaining clothes join the linen beside the bed; she presses close before you can reach for the cloak.{/n}",
        c("Continue", "cut")),
    nar("cut", '{n}Her mouth is warm against yours; her bare body presses close, breath unsteady now. She pulls the cloak beneath your shoulders, settles her knees at your hips and looks into your face.{/n} "Come here." {n}Her hand closes over yours and draws it between you -{/n}',
        c("Continue", "after")),
    ki("after", '{n}In the grey before morning she lies with her head on your shoulder, one hand flat on your chest.{/n} "I thought I should lie awake. Instead I have slept through the sergeant\'s snoring." {n}She tests the light at the flap with one half-open eye.{/n} "The Crows drill at first light. I am their only knight. He will be insufferable if I am late."',
        c('"Stay."', "morning", requires=(CROWS_ORDER,)),
        c("[Pull the cloak over her shoulders.]", "morning", requires=(CROWS_ORDER,)),
        c('"Stay."', "morning_alone", forbids=(CROWS_ORDER,)),
        c("[Pull the cloak over her shoulders.]", "morning_alone", forbids=(CROWS_ORDER,))),
    nar("morning", '''{n}She does not stay; she is a knight of the Green Crows, and the Crows drill at first light. By the time you have found your boots she is out on the trampled ground behind the tent in her padded doublet with the old sword in her hand, running the eel-girl through a guard, while the sergeant of sixty leans on the mule and offers loud, contradictory advice.{/n}''',
        c("Continue", "drill")),
    nar("morning_alone", '''{n}She does not stay; she is a knight of the Green Crows, and the Crows drill at first light. By the time you have found your boots she is out on the trampled ground behind the tent in her padded doublet with the old sword in her hand, running the forms alone against the morning, cut and guard and cut, while the sergeant of sixty leans on the mule and offers loud, contradictory advice.{/n}''',
        c("Continue", "drill")),
    nar("drill", '{n}An Eagle Watch column passes on the road to Drezen. Kitrane finishes the guard before she looks after it, then returns to her drill.{/n} "No salute. I might finish the whole exercise before anyone asks me for an order."',
        c('"Get used to it."', flags=(TENT, DRILL)),
        c("[Salute her, very badly.]", flags=(TENT, DRILL))),
], requires=("trickster.ever", COMMITTED, RETURNED), forbids=(TENT, CLOSED, FORD_HANGED), delay=8, ForbidOverrides={FORD_HANGED: FORD_ANSWERED}, Areas=[DREZEN])
tag(P + "visit.tent", "T")


# --- After: the war table ------------------------------------------------------------------------------------------------------

beat(P + "kitrane.table", "The war table", '"I want your eyes on the maps for Threshold."', [
    ki("start", '''{n}She looks at you for a moment as if you had asked her to put the crown back on.{/n} "A knight of the Green Crows has no business at the Commander's war table." {n}And then, because she is who she is, she is already reaching for the rolled maps under your arm.{/n} "Show me."''',
        c("[Spread the maps on the curio-seller's counter.]", "maps")),
    ki("maps", '''{n}She reads them the way other people read letters from home: fast, and then slowly, and then with a finger tracing the lines.{/n} "You will go in along the old Sarkorian road, here, because it is the only road an army can use toward the heart of the Wound. They know that as well as we do." {n}Her finger stops where the inked roads run out into blank vellum.{/n} "Past here, nobody knows anything. In a hundred years no spell and no scout has come back from Threshold with so much as a sketch of it. So do not plan the fortress yet. Plan the road." {n}She taps three marks your outriders made last week.{/n} "Your scouts say the ground has opened along it in three places since the spring. Anything that marches that road, the enemy will be waiting for at the second."''',
        c('"What would you do?"', "would"),
        c('"How far do you trust the scouts?"', "first")),
    ki("first", '"Not very far." {n}Flatly.{/n} "Three riders went out and two came back, and the one who did not is the one I should most like to have heard. I have read scouts\' reports on the Wound for most of my life, Commander. The road can open again before the wagons reach it. I would send riders ahead of each stage." {n}She taps the map.{/n} "So I would not trust that road with anything I could not afford to lose. That is what I would do."',
        c("Continue", "would")),
    ki("would", '"Send the baggage along the road, loudly, with every banner you own, and the army a day behind it along the dry riverbed to the east, which your scouts found dry this season and which nobody marches by because nobody wants to lose the wagons." {n}She looks up.{/n} "It is a guess, built on three riders. Say so when you carry it to the council." "Choose drivers who know when to abandon the decoys. Pay them properly, and say plainly what you are asking them to risk."',
        c('"I\'ll take it to the council as your plan."', "credit", flags=(P + "kitrane.table_credited",)),
        c('"I\'ll take it to the council as mine."', "mine")),
    ki("credit", '''"As the plan of a knight of the Green Crows?" {n}Her mouth twitches.{/n} "They will laugh you out of the chamber, and then they will adopt it, and in a year somebody will write a treatise about the brilliant unknown knight who advised the Commander at Threshold." {n}She rolls the maps up neatly.{/n} "Do it. I should enjoy being brilliant and unknown. It will make a change from being brilliant and blamed."''',
        c("[Take the maps.]", flags=(TABLE,))),
    ki("mine", '''"Good." {n}At once, and with evident approval.{/n} "A plan that comes from a dead queen is a relic; nobody questions it, and so nobody improves it. A plan that comes from the Commander will be argued over until it is better than mine." {n}She hands you the maps.{/n} "Besides. I have had a century of credit. I find I do not miss it half as much as I expected."''',
        c("[Take the maps.]", flags=(TABLE,))),
], requires=(COMMITTED,), forbids=(TABLE,), delay=24)


# --- Her choice: Kitrane for good, or the crown after Threshold ---------------------------------------------------------------
# Hers first. The Commander's word colours her answer; what she decides follows from what the Commander said of Sir Anselm.

beat(P + "kitrane.crown", "The crown or the crow", '"You wanted to walk the wall with me."', [
    nar("start", '''{n}She walks with you up onto the citadel wall, where you have gone to look at the weather over the Wound, and stands beside you for some time without speaking. She has a broadsheet folded in her belt and the old sword at her hip, and she looks, for once, exactly her age.{/n}''',
        c("Continue", "speak")),
    ki("speak", '''"Threshold." {n}She nods toward the Wound.{/n} "After it, this war ends, one way or the other. If it ends the right way, there will be a world afterwards, and Mendev will be in it, and a crypt in Nerosyan with the wrong man lying in it under my name." {n}She does not look at you.{/n} "I have decided what I shall do, on the other side. I wanted you to hear it from me before anyone else did."''',
        c("Continue", "named", requires=(NAMED,)),
        c("Continue", "kept", requires=(KEPT,), forbids=(NAMED,))),
    ki("named", '''"You said Sir Anselm should have his name back one day, even if it cost me mine. I have thought of little else." {n}Her hand rests on the hilt of her sword.{/n} "When the war is over I shall ride to Nerosyan and walk into the cathedral in this surcoat, and have that crypt opened, and say who is in it and who is not. His daughter will have her father back to bury. Mendev will have its Queen back, and a scandal to go with her."''',
        c('"They\'ll want to know how."', "how"),
        c('"And Kitrane?"', "kitrane")),
    ki("how", '"They will. I shall tell them about the name, the cart, and the man in the coffin." {n}A thin smile.{/n} "You will be answering for that, Commander, before bishops and regents and the whole of the Mendevian court, for years. I am sorry. I am not sorry enough not to do it."',
        c("Continue", "kitrane")),
    ki("kitrane", '''"Kitrane will not end. She will have a crown on again, that is all, and know the difference between the woman and the hat." {n}She turns to you at last.{/n} "I shall take no more elixir. The church may offer it; I shall refuse it at the altar, in front of them all. The Queen of Mendev will grow old like anybody, and when she is tired, she will abdicate, and go and be a knight of some small order that nobody has heard of."''',
        c('"I\'ll stand beside you in the cathedral."', "end_crown", flags=(CROWN,)),
        c('"You don\'t have to do this."', "must", flags=(CROWN,))),
    ki("must", '"I made the choice at Iz. I can answer for it now. Do not ask me to leave Anselm\'s daughter with a missing father because you would rather spare me the hearing."',
        c("Continue", "end_crown")),
    ki("end_crown", '"After Threshold, then." {n}She looks back out at the Wound.{/n} "Until then I am Kitrane of the Green Crows, and I have Crows to drill, and a mule who bites. Do not tell anyone, Commander. I should like to enjoy the last of it."',
        c("[Stand with her on the wall until the light goes.]")),
    ki("kept", '''"You said Sir Anselm chose to stand beside me, and still does. I have decided you were right." {n}She breathes out, slowly.{/n} "He keeps his post in the crypt at Nerosyan. The Queen stays dead. His daughter has his sword-belt, and every year, on the day of Iz, she will find a purse at her door from a knight who owed him a debt. It will never be enough. It will be every year until I die."''',
        c('"And the crown?"', "crown")),
    ki("crown", '"The regents will have to name a successor. I shall not pretend that leaving them to it is without cost." {n}She touches the green surcoat at her breast.{/n} "I shall take no more elixir. I shall grow old in a leaking tent, and teach eel-girls to hold a sword, and drill with the Crows. Kitrane, for good."',
        c('"Kitrane, for good."', "end_forever", flags=(FOREVER,)),
        c('"Are you certain?"', "certain", flags=(FOREVER,))),
    ki("certain", '''"No." {n}Promptly.{/n} "I mistook certainty for good judgment more than once in my reign, and Iz was the last time." {n}Drily:{/n} "It brought me to a rubble-heap with Mendev's name in my ears." {n}Her mouth curves.{/n} "I am not certain. I am decided. It is a much more comfortable thing to be."''',
        c("Continue", "end_forever")),
    ki("end_forever", '''"There. It is said." {n}She leans her forearms on the parapet beside yours.{/n} "Now stand here with me a while and look at the weather over the Wound, as if we were two knights with nothing better to do. I have always wanted to do that, too."''',
        c("[Stand with her on the wall until the light goes.]")),
], requires=(), forbids=(FOREVER, CROWN), delay=48, RequiresAnyGroups=[[NAMED, KEPT]])



def integrate(payload):
    # eng8-q8d: the pending device stages the living sergeant, not Galfrey.
    # Her own two presences still require Returned independently.
    from storylines import earned_presence
    earned_presence.PRESENCE_BOOTSTRAPS['galfrey'] = {'galfrey.dead': {
        'Flag': P + 'kitrane_taken',
        'Reason': 'The accepted Iz device brings the Crows sergeant to conduct the vigil and escort the earned arrival.'}}
    # end eng8-q8d
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)


# --- 15. A pie from a paladin (Seelah, acknowledged from her side) ------------------------------------------------------------

SEELAH_SPOKEN = P + "kitrane.seelah_spoken"

beat(P + "kitrane.seelah", "A pie from a paladin", '"Who was that you were talking to?"', [
    ki("start", '''{n}She is holding a meat pie in a twist of paper, still steaming, and looking after someone who has already vanished into the crowd.{/n}''',
        c("Continue", "seelah", requires=(SEELAH_BED,), forbids=("seelah_dead", "seelah_gone")),
        c("Continue", "seelah", requires=(SEELAH_BED, "seelah_dead", "seelah.trickster.returned")),
        c("Continue", "seelah", requires=(SEELAH_BED, "seelah_gone", "seelah.trickster.returned"), forbids=("seelah_dead",)),
        c("Continue", "seelah_drezen", forbids=(SEELAH_BED, "seelah_dead", "seelah_gone")),
        c("Continue", "seelah_drezen", requires=("seelah_dead", "seelah.trickster.returned"), forbids=(SEELAH_BED,)),
        c("Continue", "seelah_drezen", requires=("seelah_gone", "seelah.trickster.returned"), forbids=(SEELAH_BED, "seelah_dead")),
        c("Continue", "stranger", requires=("seelah_dead", SEELAH_BED), forbids=("seelah.trickster.returned",)),
        c("Continue", "stranger_absent", requires=("seelah_dead",), forbids=(SEELAH_BED, "seelah.trickster.returned")),
        c("Continue", "stranger", requires=("seelah_gone", SEELAH_BED), forbids=("seelah_dead", "seelah.trickster.returned")),
        c("Continue", "stranger_absent", requires=("seelah_gone",), forbids=("seelah_dead", SEELAH_BED, "seelah.trickster.returned"))),
    ki("seelah", '''"Your paladin. The one with the quick hands, who cut purses in Solku before she ever held a sword for the Inheritor." {n}She turns the pie over in its paper.{/n} "She walked up to me, bought this from the girl with the tray, put it in my hands, and walked away again. She did not say a word. She did not look at my face." {n}A long breath.{/n} "She was at the bed at Iz. She cried out, 'Your Majesty!', and I felt the thing in me turn its head at it like a hound."''',
        c('"She knows."', "knows"),
        c('"She\'s kind. That\'s all."', "kind")),
    ki("seelah_drezen", '"Your paladin. The one with the quick hands, who cut purses in Solku before she ever held a sword for the Inheritor." {n}She turns the pie over in its paper.{/n} "She walked up to me, bought this from the girl with the tray, put it in my hands, and walked away again. She did not say a word. She said nothing about my face." {n}A long breath.{/n} "She looked at me here for as long as it takes to count a purse, and knew. She put the pie in my hands before I could decide what to say."',
        c("Continue", "knows")),
    ki("knows", '"She knows." {n}Galfrey turns the pie in its paper.{/n} "I had begun composing a very proper speech of thanks. She was gone before I could say a word of it." {n}Her mouth curves.{/n} "I shall have to catch her before drill. Without this pie, or she will bring me another."',
        c("Continue", "end")),
    ki("kind", '"She recognized me and kept my name. Then she bought me a pie. I shall remember both." {n}She takes a bite at last, and burns her tongue, and swears like a sergeant.{/n}',
        c("Continue", "end")),
    ki("stranger", '"A woman from the Eagle Watch. She bought it from the girl with the tray and put it in my hands and walked off, the way soldiers do for a knight who looks hungry." {n}She turns it over.{/n} "There was a paladin in your company once, with quick hands, who was at the bed at Iz. She cried out, \'Your Majesty,\' and I felt the thing in me turn its head at it." {n}Her voice drops.{/n} "She is not here to thank. I shall have to remember the kindness without saying so."',
        c("Continue", "end")),
    ki("stranger_absent", '"A woman from the Eagle Watch. She bought it from the girl with the tray and put it in my hands." {n}She turns the pie over.{/n} "I was considering how to thank her when she walked off. Your paladin would have laughed at me. I find I should have liked to hear it."',
        c("Continue", "end")),
    ki("end", '''"Here." {n}She breaks the pie in two, with scrupulous fairness, and holds out the larger half.{/n} "A knight shares her rations with her Commander. It is in the regulations. I wrote the regulations."''',
        c("[Take the larger half.]", flags=(SEELAH_SPOKEN,)),
        c("[Take the smaller half.]", flags=(SEELAH_SPOKEN,))),
], requires=(FIRST,), forbids=(SEELAH_SPOKEN,), delay=24)


# --- 16. The blind man knows her voice (the Storyteller) ----------------------------------------------------------------------

STORYTELLER_SPOKEN = P + "kitrane.storyteller"

beat(P + "kitrane.storyteller", "A voice he knows", '"You look shaken."', [
    ki("start", '''"I went to the Storyteller's shelves. I should not have." {n}She is gripping the pommel of her sword hard enough to whiten her knuckles.{/n} "I wanted a book. The Crows' squire cannot read, and I thought I would teach the boy from something with pictures. I asked the old man if he had anything suitable for a squire of fourteen."''',
        c('"And?"', "and")),
    ki("and", '''"He was very still. Then he said, 'For a squire of fourteen, Your Majesty? I should think the Lays of the First Crusade. You always liked them best.'" {n}She lets out a breath.{/n} "He is blind, Commander. I had forgotten. He has never once seen my face, in any of the times he has told my story. He knows me by my voice."''',
        c("Continue", "rent", requires=(RENT,)),
        c("Continue", "said", forbids=(RENT,))),
    ki("rent", '''"Even this voice." {n}She touches her throat, where the tear catches.{/n} "I thought the rending had changed it enough. It has not. He said it was like hearing a song he knew played on a cracked bell. He said he would know it anywhere, and he was very sorry, and he would not tell."''',
        c("Continue", "said")),
    ki("said", '"He found a book with a knight on the cover and told me the boy should have something worth reading after drill. He would not take my four coppers." {n}She rests her hand on the book.{/n}',
        c('"He won\'t tell anyone."', "tell"),
        c('"Did you thank him?"', "thank")),
    ki("tell", '''"No. He will not." {n}Certain.{/n} "He will tell it, one day, in some tavern in Absalom, long after we are all dust, and change the names, and nobody will believe it. That is his kind of silence." {n}She loosens her grip on the sword at last.{/n} "I find I do not mind. I should like, very much, to be a story nobody believes."''',
        c("[Leave her with the book.]", flags=(STORYTELLER_SPOKEN,))),
    ki("thank", '"I thanked him. He said, \'You are welcome, Kitrane,\' and asked me to bring the book back before the squire ruined it." {n}She relaxes her grip on the sword.{/n} "I was grateful for the errand."',
        c("[Leave her with the book.]", flags=(STORYTELLER_SPOKEN,))),
], requires=(FIRST,), forbids=(STORYTELLER_SPOKEN, "storyteller.dead"), delay=36)


# --- 17. The sergeant's stories (Sir Anselm, remembered) ----------------------------------------------------------------------

SERGEANT = P + "kitrane.sergeant"

beat(P + "kitrane.sergeant", "What the sergeant remembers", '"Your sergeant was telling stories last night."', [
    ki("start", '''"He always does, after the second cup. Tonight it was Sir Anselm." {n}She is sitting on an upturned crate by the stall, oiling the old sword with slow, careful strokes.{/n} "I have known the Crows as Kitrane since the war camp, Commander, and as the Queen for forty years, since they first stood behind my chair at court. I found last night that I knew almost nothing about any of them."''',
        c('"What did he tell you?"', "told")),
    ki("told", '''"That Sir Anselm cheated at cards. Badly. That he kept a list of every demon he had killed, and lost it, and started a new one from memory, and that the second list was a good deal longer than the first." {n}Her mouth twitches.{/n} "That he used to say, whenever I rode out in front of the line, that the Queen of Mendev had the tactical sense of a charging goat, and that he said it loudly, being deaf, so that I would hear."''',
        c('"Did you?"', "heard")),
    ki("heard", '''"Every time." {n}The oil-cloth stops.{/n} "I thought he was being impertinent. I thought I was being gracious, not having him disciplined." {n}She looks down at the blade.{/n} "He was telling me to stay behind him. Every time, for forty years, in the only way a knight may tell his Queen anything. And at Iz I did not, and he stepped in front of what was meant for me instead, and that is how he came to be in the box."''',
        c('"It wasn\'t your fault."', "fault"),
        c('"He did what he meant to do."', "meant"),
        c("[Say nothing. Sit down beside her.]", "sit")),
    ki("fault", '''"No. It was the enemy's fault, and the Lord of Locusts', and the Worldwound's." {n}Very even.{/n} "I am a paladin, Commander. I know exactly how much blame to take and where to put it down. I have done it ten thousand times." {n}Her hands resume on the blade.{/n} "I am only finding it very hard to put this particular one down. It is shaped like a deaf old man."''',
        c("Continue", "end")),
    ki("meant", '''{n}She is silent for a while.{/n} "Yes. He did. That is the only mercy in it." {n}She holds the sword up, and turns it, and you notice the name scratched small and crooked near the hilt, under the Crows' mark.{/n} "This is his. Mine went home on the coffin, because the Queen's sword must go home with the Queen, and when the Crows brought me out I took his. I did not think about it at the time. I think about nothing else now."''',
        c("Continue", "end")),
    nar("sit", '{n}You sit down on the next crate. She goes on oiling the sword for a long time, stroke after stroke, until the steel shines, and neither of you says anything. When she has finished she lays the blade across her knees and rests both hands on it.{/n}\n{n}"Thank you," she says at last. "He would have talked until the sword was dry. I find I needed the quiet today."{/n}',
        c("Continue", "end")),
    ki("end", '''"He would have liked you, I think. He liked anyone who told me no." {n}She sheathes the sword.{/n} "Go on, Commander. The sergeant has a third cup waiting for me tonight, and I intend to hear every story he has left before he forgets them."''',
        c("[Leave her with the sword.]", flags=(SERGEANT,))),
], requires=(FIRST, COFFIN), forbids=(SERGEANT,), delay=36)


# --- 18. After the tent: the grey hair, counted ---------------------------------------------------------------------------------

GREY = P + "kitrane.grey"

beat(P + "kitrane.grey", "Counting", '"You\'re frowning at that mirror again."', [
    ki("start", '"Three." {n}She holds out the sergeant\'s mirror.{/n} "I counted one when I last showed you. Now there are three. At this rate the Crows will have a white-haired knight before the war is done. Do inspect it properly, Commander."',
        c('[Flirt] "I\'ll count them for you. Every one."', "count"),
        c('"Do you mind?"', "mind")),
    ki("count", '''{n}She hands you the mirror, and then, after a moment's consideration, takes it back and bends her head instead, right there beside the curio stall, so that you can part her hair with your fingers and look.{/n} "Report, Commander," {n}she says to the cobbles, a little muffled.{/n}''',
        c('"Four."', "four"),
        c('"Three. And a very handsome ear."', "ear")),
    ki("four", '''"Four!" {n}She straightens up so fast that her hair falls in her eyes.{/n} "Four. You are a liar and a scoundrel and I shall never let you count again." {n}She is laughing.{/n} "I have been counted by treasurers and physicians and priests of the Inheritor for a hundred years, Commander, and not one of them ever made it feel like this."''',
        c("Continue", "end")),
    ki("ear", '''"Flatterer." {n}But she stays where she is, head bent, for a breath longer than she needs to, your fingers in her hair.{/n} "The Queen had a lady of the bedchamber whose only duty was to see that no one ever saw her like this. Uncombed. Going grey. Leaning on somebody in the street." {n}She straightens slowly.{/n} "I should like to give her a pension and a letter of thanks, and tell her she is no longer required."''',
        c("Continue", "end")),
    ki("mind", '''"I thought I would." {n}She considers the mirror.{/n} "I lay awake over the first one. I have not lain awake over these. I think that is your fault." {n}A sidelong look.{/n} "One does not lie awake worrying about growing old when one has somebody to grow old beside. I had not known that. It is not in any chronicle I have read."''',
        c("Continue", "end")),
    ki("end", '''{n}She tucks the mirror back into her belt.{/n} "Enough vanity. There is a war on, and the Crows drill at first light." {n}And then, as you turn to go, lower:{/n} "Come to the tent tonight. Bring nothing. Count again."''',
        c('"I\'ll be there."', flags=(GREY,)),
        c('[Flirt] "I\'ll bring a lantern. For accuracy."', flags=(GREY,))),
], requires=(COMMITTED, TENT, ELIXIR), forbids=(GREY,), delay=24)


# --- 19. The Queen's likeness (a relic of herself, sold in the market) -----------------------------------------------------------

LIKENESS = P + "kitrane.likeness"

beat(P + "kitrane.likeness", "The Queen's likeness", '"What are you holding?"', [
    ki("start", '''{n}It is a woodcut, crudely coloured, on cheap paper: a woman in a crown and blue armour with a sword raised over her head and a dragon dying at her feet, and a banner across the bottom that reads THE MARTYR OF IZ.{/n} "A pedlar is selling them at the corner. Two coppers each, or three for a silver." {n}She holds it up beside her own face.{/n} "Do you see the resemblance?"''',
        c('"None whatsoever."', "none"),
        c('[Flirt] "She isn\'t half as handsome."', "handsome"),
        c('"The jaw."', "jaw")),
    ki("none", '''"Nor do I. Nor does he. I stood beside his tray for a quarter of an hour, holding this, and he tried to sell me two more." {n}She lowers it.{/n} "I have sat for thirty portraits, Commander. I know exactly how a painter lies. This man has never seen my face, and nor has whoever cut the block, and they have made a better queen than I ever was out of nothing but grief and bad ink."''',
        c("Continue", "sold")),
    ki("handsome", '''"She is not, is she?" {n}Critically.{/n} "Her nose is wrong. Her sword is wrong: nobody holds a blade over her head like that unless she wants to lose it. And she has never in her life looked so certain of anything." {n}The corner of her mouth moves.{/n} "You are very kind to a dead woman, Commander. Or very unkind to her likeness. I have not decided which I prefer."''',
        c("Continue", "sold")),
    ki("jaw", '''"The jaw." {n}She looks at the woodcut again, with the air of a general reviewing a bad map.{/n} "Yes. He has the jaw. Every portrait of me for a century has had the jaw; I think it is the one thing about me nobody can flatter." {n}She sighs.{/n} "My cousin said it told him to take his elbows off the table. I expect it will be telling pedlars' customers the same thing for a hundred years."''',
        c("Continue", "sold")),
    ki("sold", '''"He has sold forty since morning. To soldiers, mostly, and to women with sons at the front, and to one very old man who wept." {n}She folds the woodcut in half, carefully, so as not to crease the crowned woman's face.{/n} "They pin them up over their beds, the pedlar says. They pray to her before battles." {n}Her voice drops.{/n} "The Martyr of Iz. I did not die a martyr, Commander. I died a bargain. And they are praying to the bargain."''',
        c('"Does it matter, if it helps them?"', "helps"),
        c('"You could tell them the truth one day."', "truth"),
        c('"Buy the whole tray. Burn them."', "burn")),
    ki("helps", '"They pray for the army when they pin her above their beds. I shall not take that from them. I would rather hear them ask the Inheritor to bring their sons home than argue about the face on a woodcut."',
        c("[Leave her with it.]", flags=(LIKENESS,))),
    ki("truth", '''"One day." {n}She weighs it, as she weighs everything.{/n} "And break forty soldiers' hearts, and the old man's, and every mother's with a son at the front, to tell them that the Martyr of Iz bought boots in the market with a borrowed month's wage." {n}She looks out at the crowd.{/n} "Perhaps. When the war is over, and they have less need of her. The truth can wait until it will not hurt anyone who is still fighting."''',
        c("[Leave her with it.]", flags=(LIKENESS,))),
    ki("burn", '{n}She stares at you, and then, to your surprise, laughs.{/n} "You would, wouldn\'t you? Buy up every last one and burn them in the square, and call it a public service." {n}She shakes her head.{/n} "No. They paid their coppers. I will not take the pictures out of their hands because I dislike the face." {n}She tucks the woodcut away.{/n} "I shall keep this one. For the jaw."',
        c("[Leave her with it.]", flags=(LIKENESS,))),
], requires=(FIRST, HANDS), forbids=(LIKENESS,), delay=24)


# --- 20. The squire's question ---------------------------------------------------------------------------------------------------

SQUIRE_ASKED = P + "kitrane.squire_asked"

beat(P + "kitrane.squire", "The squire's question", '"Your squire looks as if she\'s been crying."', [
    ki("start", '''"She has." {n}Kitrane is watching the girl across the square, who is scouring a helmet with sand as if it had personally wronged her.{/n} "She asked me a question this morning, while I was showing her how to hold a guard. She asked it the way children ask things, all at once, without looking." {n}A breath.{/n} "She asked whether I was the Queen."''',
        c('"What did you tell her?"', "told"),
        c('"How did she guess?"', "guess")),
    ki("guess", '"The woodcuts. The way the Crows straighten when I enter the tent, before they remember. And once I said \'we\' about Mendev when I meant \'they\'." {n}She looks across the square.{/n} "I am training her to notice what an enemy gives away. I ought to have expected her to practise on me."',
        c("Continue", "told")),
    ki("told", '"She asked whether I was the Queen." {n}Her hands tighten on the pommel.{/n} "I told her to call me Kitrane in the camp, and that she need not answer anyone\'s questions about the Queen. Then she cried."',
        c('"You told her the truth, and she heard it."', "heard"),
        c('"It\'s too heavy for a girl of sixteen."', "heavy"),
        c('"You shouldn\'t have told her anything."', "careful")),
    ki("heard", '"She heard what I would not say outright. I shall have to earn the trust I asked her to keep." {n}She watches the girl scour.{/n} "Since I came back, the Crows have carried enough of my secrets. I had hoped to leave her out of them."',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
    ki("heavy", '"It is." {n}At once.{/n} "The first time they put a crown on my head, in a procession, it was too heavy as well. I should have told her what to do before she had to ask." {n}She lifts her chin toward the girl.{/n} "Look at her. She is angry and frightened and scouring that helm as if she means to wear through it. She is also standing up straighter than she did yesterday. I know that look. I wore it for a year."',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
    ki("careful", '"Perhaps not." {n}She turns to look at you.{/n} "She asked me directly. I could not bear to lie to her face. I shall have to be more careful about what that costs her."',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
], requires=(FIRST, CROWS_ORDER, LIKENESS), forbids=(SQUIRE_ASKED,), delay=36)


# --- The living Queen (T): Kitrane by lamplight ----------------------------------------------------------------------------------
# On the Trickster path the Queen's own answer in Chapter 5 is Cue_0041: "As the queen, you have my trust. But as Galfrey, I cannot
# trust you." The native romance ends there (Cue_0039 completes it). These scenes answer that line: not as the Queen, and not as
# Galfrey, but as the knight she once invented, and only if the Commander can prove a plan kept. Inline on her Chapter 5 hub
# (AnswersList_0002), returning to her clean greeting Cue_0003 "Yes, Commander? Did you want something?".

HUB5 = "fed166af2f1d509478d18ea63a40339f"
HUB5_BACK = "344bc63f6bbace64fab2a3e6c69561fe"
EVENING = P + "alive.evening"
PLAN_TOLD = P + "alive.plan_told"
PLAN_KEPT = P + "alive.plan_kept"
TRIAL_KEPT = P + "alive.trial_kept"     # Q12: the next plan, one she objects to, told first and her objection answered; four days of orders shown
TRIAL_PRICED = P + "alive.trial_priced"  # Q12: the Commander told her the cultist might kill, and let him go unwatched anyway (she refused it)


def alive(id, title, entry, nodes, requires, forbids=(), delay=0):
    SCENES.append(scene(id, title, "Galfrey", 5, entry, nodes, requires=("trickster", FINAL, *requires),
                        forbids=(DEAD, CLOSED, FINISHED, "galfrey.romance_active", *forbids), delay=delay, last=5, Relationship=REL,
                        Chapters=[5], AnswerLists=[HUB5], NativeReturnCue=HUB5_BACK))
    tag(id, "T")


def conv5(id, text, *choices):
    return n(id, "conversant", text, *choices)


alive(P + "alive.kitrane", "As Kitrane", '"You trust the Commander as the Queen. Would Kitrane?"', [
    conv5("start", """{n}The Queen's eyebrows rise, very slowly.{/n} "Kitrane." {n}She glances past you at the hall, the clerks, the knights at the door, and lowers her voice.{/n}""",
        c("Continue", "refused", requires=(NATIVE_REFUSED,)),
        c("Continue", "never", forbids=(NATIVE_REFUSED,))),
    conv5("refused", """"I told you I cannot trust you as Galfrey. I meant it. Your powers are unreliable, and so, I think, are you." {n}A pause.{/n} "And you answer by asking after a knight of a minor order who has not existed since the war camp. That is either very clever or very impudent.\"""",
        c("Continue", "offer")),
    conv5("never", """"A knight of a minor order who has not existed since the war camp. You ask after her as if she were a friend who had gone home on leave." {n}Her mouth twitches.{/n} "Very well. What would you say to her, that you will not say to me?\"""",
        c("Continue", "offer")),
    conv5("offer", """{n}She waits, arms folded, the prosecutor at her trial again.{/n}""",
        c('"Come out tonight, in the Crows\' surcoat. Nobody will look twice. I\'ll tell you one plan of mine before I carry it out, and you can watch me keep it."', "tell", flags=(EVENING,)),
        c('"Nothing. Forget I asked."', abort=True)),
    conv5("tell", """{n}She gives you a long, calculating look, and then, very slightly, nods.{/n} "Tell me now. Here. Before anyone else knows it, including your quartermaster.\"""",
        c("[Tell her the whole plan: the empty wagons up the eastern road, loudly, and the real column a day behind by the dry riverbed.]", "accept", flags=(PLAN_TOLD,))),
    conv5("accept", """{n}Something moves behind her eyes that has not moved there in a long while.{/n} "One plan, told in advance, and kept." {n}She says it like terms of surrender.{/n} "Very well. Carry it out, and then come and tell me how it went. Kitrane will be listening. If you change it on the road without a word, she will take it as your first broken promise, and she will not wait for a second.\"""",
        c("[Bow to the Queen.]")),
], requires=(), forbids=(EVENING,))

alive(P + "alive.plan", "One plan, kept", '"The eastern road marches at dawn, Your Majesty."', [
    conv5("start", '{n}She looks up from her dispatches, her eyes going to the door and back.{/n} "At dawn, as you told me. If anything has changed, tell me before the first wagon leaves."',
        c("[Carry it out exactly as you told her: the empty wagons first, loudly, and the column by the riverbed.]", "kept",
          requires=(PLAN_TOLD,), flags=(PLAN_KEPT,), crusade=("Materials", -150)),
        c('[Trickster] [Improvise on the road: a third column she knows nothing about.]', "third"),
        c('"Not yet, Your Majesty."', abort=True)),
    n("kept", "Narrator", '{n}The quartermaster counts out the wagons and strikes them from his stores. Banners are rolled for the empty train. Galfrey checks the riverbed orders against the copy you gave her.{/n}',
        c("Continue", "kept_her")),
    conv5("kept_her", '"The empty wagons first. The real column a day behind." {n}She gives back the orders.{/n} "The drivers leave the decoys before the raiders reach them. I want their names on the returning muster. Bring me the report when the column is through."',
        c("[Bow to the Queen.]")),
    conv5("third", '{n}Her face stills when you describe a third column absent from her copy.{/n} "Then it is a different plan. Tell me the whole of it before you send anyone onto that road." {n}She pushes the dispatch back.{/n} "I will not be informed after the wagons have burned."',
        c("[Leave her.]", abort=True)),
], requires=(EVENING,), forbids=(PLAN_KEPT,), delay=48)

# Q12: the next plan is one she objects to. Told first, argued, and her objection answered rather than overruled; then four
# days in which every order reaches her an hour before it goes. Her distrust (Cue_0041) is of the Commander's powers and
# decisions, so the reversal is earned on a decision, not on a name.
alive(P + "alive.trial", "The next one", '"I have the next one, Your Majesty. Before anyone."', [
    conv5("start", """{n}She sets down her pen and folds her hands on the dispatches, which is how the Queen of Mendev listens to bad news.{/n} "Go on.\"""",
        c("[Tell her: the Locust cultist your patrols took on the north road escapes tonight, by your arrangement, with a forged march-order sewn into his boot.]", "objects")),
    conv5("objects", """{n}She is quiet long enough that a clerk at the far table stops writing.{/n} "You will turn loose a priest of the Lord of Locusts, in my lands, to carry a lie to his master." {n}Each word set down like a weight on a scale.{/n} "He will not go straight home, Commander. Men like that never do. There are farms between here and the Wound. What becomes of them?\"""",
        c('"Two of the Crows follow him the whole way. When the order is delivered, they take him again, and he hangs where he was caught."', "answered", crusade=("Finances", -100)),
        c('[Trickster] "Perhaps he kills on the way. That is the price of the lie. I will carry it."', "priced", flags=(TRIAL_PRICED,)),
        c('"You\'re right. I\'ll find another way."', "dropped")),
    conv5("priced", """"Then carry it." {n}She picks up her pen.{/n} "I will not. Not as the Queen and not as anyone else. I have buried enough farmers to know what that price is, and who pays it." {n}She does not look up again.{/n} "Bring me the next one when it costs only you.\"""",
        c("[Leave her.]", abort=True)),
    conv5("dropped", """"No." {n}At once, and sharply.{/n} "Do not do that. I did not ask you to drop it; I asked you what becomes of the farms. A general who folds at the first objection is worse than one who never listens to any." {n}She taps the dispatch.{/n} "Go away and come back with an answer to my question, not a retreat.\"""",
        c("[Leave her.]", abort=True)),
    n("answered", "Narrator", '{n}She studies the forged order, the north-road map, and the Crows\' instructions.{/n} "They follow him from the gate until he delivers it. If he turns toward a farm, they take him there. No farmer pays for this deceit." {n}She marks the dispatch.{/n} "For four days, every order from your desk comes to mine an hour before it goes. When I object, answer me. The Crows report to me first."',
        c("Continue", "four_days")),
    conv5("four_days", '"Four days, Commander. I shall be at this desk. You know where to bring the orders."',
        c("[Bow to the Queen.]", flags=(TRIAL_KEPT,))),
], requires=(PLAN_KEPT,), forbids=(TRIAL_KEPT, COMMITTED), delay=48)

alive(P + "alive.oath", "The Crows' oath, by lamplight", '"The Crows\' sergeant says Kitrane has something to say to me."', [
    conv5("start", """"She does." {n}The Queen does not look up from her dispatches, but her pen has stopped.{/n} "Not here. The Crows' tent, after the ninth bell." {n}She lets the pen fall.{/n} "Bring nothing. And do not dare salute.\"""",
        c("[Go to the Crows' tent after the ninth bell.]", "tent")),
    n("tent", "Narrator", '{n}She is waiting in the Crows\' tent by one lantern, in the green surcoat with the three black birds, her hair loose. Before you can speak she draws the old sword and goes down on one knee in the straw, and holds it out to you hilt-first across her forearm.{/n}\n{n}"Kitrane of the Green Crows offers her sword to the Commander of the Fifth Crusade," she says. "In the Inheritor\'s sight, to serve until released or dead."{/n}',
        c('[Refuse her oath; offer your hand] "No. I don\'t want your sword. Get up."', "refuse"),
        c('"Not like this. Not as your Commander."', "not_yet")),
    conv5("not_yet", '{n}She sheathes the sword and rises without your hand.{/n} "The sword was easier to offer. I knew the words." {n}She sets it beside the lantern.{/n} "Go tonight. I shall send for you when I have decided what to say without it."',
        c("[Leave her in the lamplight.]", abort=True)),
    n("refuse", "Narrator", '{n}She looks from the offered hand to the sword, then sheathes it and rises. She keeps your hand, her thumb pressed against your pulse.{/n} "I had prepared a very fine oath. You have spoiled it." {n}She catches your collar and kisses you. When your back strikes the tent pole, she steadies the swinging lantern without releasing you.{/n} "There. I prefer that answer."',
        c("Continue", "threshold")),
    n("threshold", "Narrator", '{n}She works your buckles quickly, then closes your reaching hand around her waist while she loosens her own laces. The surcoat drops beside the sword. Linen follows it. Her bare shoulders are strong, her skin marked by old pale scars; her breath catches when your mouth finds the hollow above her breast.{/n}\n\n{n}She pulls you down onto the saddle-blankets and settles close over you, bare skin warm against yours, her loose hair brushing both your faces.{/n} "You have kept me talking long enough, Commander." {n}Her knees tighten at your hips. She takes your hand and draws it between your bodies -{/n}',
        c("Continue", "morning")),
    n("morning", "Narrator", '{n}By first light she is gone. At the Queen\'s table she is crowned and signing dispatches. There is a small bruise above the collar of her gown. She catches you looking and moves the next order toward you.{/n} "Commander." {n}Then, below the clerks\' hearing:{/n} "I slept very well. Do attend to the dispatch before you look so pleased."',
        c("[Bow to the Queen.]", flags=(COMMITTED, P + "alive.committed"))),
], requires=(PLAN_KEPT, TRIAL_KEPT), forbids=(COMMITTED,), delay=48)
# eng8-q8d: earlier waits leave room for her unchanged two-day reservation.
for _eng8_scene in SCENES:
    if _eng8_scene['Id'] in (P + 'commit.oath', P + 'commit.oath_stall'):
        _eng8_scene['DelayHours'] = 12

# Authored Crows sergeant, using Owlcat's ordinary crusader unit; he waits only
# while Kitrane's earned return is pending. Neither hub impersonates Galfrey.
ENG8_SERGEANT = '8a23e71893cf8ab428e7ebd64b10ad27'  # Prologue_KenabresCrusader_Male
for _eng8_hub, _eng8_anchor, _eng8_side, _eng8_req, _eng8_forb in (
    ('galfrey.presence.sergeant', CURIO, 'left', (), ('galfrey.presence.sergeant.failed',)),
    ('galfrey.presence.sergeant_stall', TIEFLING, 'right', ('galfrey.presence.sergeant.failed',), ())):
    PRESENCES[_eng8_hub] = dict(Unit=ENG8_SERGEANT, Area=DREZEN, Mode='spawn-copy',
        At=dict(NearUnit=_eng8_anchor, Side=_eng8_side, Distance=2.5 if _eng8_side == 'left' else 3.5),
        Requires=['trickster.ever', P + 'kitrane_taken', DEAD, *_eng8_req],
        Forbids=[CLOSED, RETURNED, *_eng8_forb], MinChapter=5, MaxChapter=5,
        AnswerLists=[], Dialog='hub',
        Greeting='{n}The Crows\' sergeant waits with his helm under his arm. The chapel bells have left him tight-lipped.{/n} "Commander."')

_eng8_tent = next(s for s in SCENES if s['Id'] == P + 'visit.tent')
_eng8_tent.pop('Kind', None)
_eng8_tent.update(Remote=False, Entry='[Go with Kitrane to the Crows\' tent.]',
    ContactUnit=DISGUISED, InteractionHub=HUB, Areas=[DREZEN])
# Keep the threshold narration free of an unchosen Commander speech line.
_eng8_cut = next(n for n in _eng8_tent['Nodes'] if n['Id'] == 'cut')
_eng8_cut['Text'] = _eng8_cut['Text'].replace(
    '"Kitrane," you say, because it is the only name she has left, and she answers it with her whole body',
    'She meets you with her whole body')
_eng8_twin = copy.deepcopy(_eng8_tent)
_eng8_twin['Id'] += '_stall'
_eng8_twin['InteractionHub'] = HUB_FB
_eng8_twin['Requires'].append(HUB_FAILED)
_eng8_twin['Forbids'].append(_eng8_tent['Id'])
_eng8_tent['Forbids'].extend([_eng8_twin['Id'], HUB_FAILED])
SCENES.append(_eng8_twin)
# Galfrey's own guarded acknowledgment keeps her cousin in her life without
# spending a reactor slot. This is authored speech, not a native cue rewrite.
for _eng8_host in (s for s in SCENES if s['Id'] in (P + 'kitrane.conversation', P + 'kitrane.conversation_stall')):
    _eng8_host['Nodes'][0]['Choices'].append(c('"Has your cousin noticed?"', 'eng8.cousin',
        forbids=('daeran.dead', 'daeran.kicked_out')))
    _eng8_host['Nodes'].append(ki('eng8.cousin', '"My cousin would recognize the jaw. He would enjoy telling me so."', c('[Leave her to the crowd.]', flags=(CONVERSATION,))))
# end eng8-q8d


# Reviewed Galfrey polish: authored operations, decisions and debt, using the
# existing contacts, affordability checks and receipt-based delay contract.
PLAN_DISPATCHED = P + "alive.plan_dispatched"
TRIAL_STARTED = P + "alive.trial_started"
ANSWER_RESERVED = P + "answer_reserved"
ANSWER_REPORTED = P + "answer_reported"
ANSWER_ALLY = P + "answer_ally"
ANSWER_REFUSED = P + "answer_refused"
OATH_RESERVED = P + "alive.oath_reserved"
RESERVED_ALLY = P + "alive.reserved_ally"
RESERVED_REFUSED = P + "alive.reserved_refused"
SEELAH_KNOWS = "trickster.secret.galfrey_eulogy.known.seelah"


def _reviewed_existing_beats():
    for host in SCENES:
        sid = host["Id"].removesuffix("_stall")
        nodes = {node["Id"]: node for node in host["Nodes"]}
        if sid == P + "kitrane.ford_after":
            nodes["agreed"]["Choices"][0].update(
                Text="[Pay 50 Finances; walk down to the lower town.]",
                Crusade={"Resource": "Finances", "Amount": -50})
            nodes["agreed"]["Choices"].append(c("[Return when you have the money.]", abort=True))
        elif sid == P + "kitrane.seelah":
            for nid in ("knows", "kind"):
                nodes[nid]["Choices"][0]["Set"].append(SEELAH_KNOWS)
        elif sid == P + "commit.answer":
            host["Forbids"].extend([ANSWER_RESERVED, ANSWER_ALLY, ANSWER_REFUSED])
            nodes["start"]["Choices"].append(c('"Have you decided, or do you need to ride first?"', "reservation"))
            host["Nodes"].append(ki("reservation", '"I have decided to ride first. If I answer now, I shall spend the patrol wondering whether I meant it." {n}She takes her helm.{/n} "The pickets need seeing to. You shall have my muster return tomorrow. My answer comes after I have been out with them."',
                c("[Let her ride.]", flags=(ANSWER_RESERVED,))))
        elif sid == P + "commit.release":
            host["Forbids"].extend([ANSWER_RESERVED, ANSWER_ALLY, ANSWER_REFUSED])
            nodes["ordered"]["Choices"][0]["Set"].append(P + "release_order_refused")
            nodes["choose"]["Choices"].append(c('"Do you want to answer now?"', "reservation"))
            host["Nodes"].append(ki("reservation", '"No. My oath stands until the Crows are back from the pickets. I shall not confuse leaving your service with coming to your tent." {n}She takes up her helm.{/n} "Let me ride first. You shall have the muster tomorrow, and my answer after the watch."',
                c("[Let her ride.]", flags=(ANSWER_RESERVED,))))
        elif sid == P + "alive.plan":
            host["Forbids"].append(PLAN_DISPATCHED)
            nodes["start"]["Choices"][0]["Set"] = [PLAN_DISPATCHED]
        elif sid == P + "alive.trial":
            host["Forbids"].append(TRIAL_STARTED)
            nodes["four_days"]["Choices"][0]["Set"] = [TRIAL_STARTED]
        elif sid == P + "alive.oath":
            host["Forbids"].extend([OATH_RESERVED, RESERVED_ALLY, RESERVED_REFUSED])
            nodes["tent"]["Choices"].append(c('"Did you mean to offer me your sword, or ask me to stay?"', "not_yet"))
            nodes["not_yet"]["Choices"][0].update(Abort=False, Set=[OATH_RESERVED])
            nodes["threshold"]["Choices"][0]["Text"] = "[Draw her close.]"
        elif sid == P + "visit.tent":
            nodes["cut"]["Choices"][0]["Text"] = "[Hold her close.]"


_reviewed_existing_beats()

# Append follow-ups after all existing scenes and twins: old scene order is saved.
alive(P + "alive.plan_report", "The riverbed muster", '"The riverbed column is through, Your Majesty."', [
    nar("start", '{n}The report lists the burned wagons first. Then the drivers, all accounted for, and the supplies that reached the army by the dry riverbed. Galfrey reads the muster twice before she looks up.{/n}', c("Continue", "kept_her")),
    conv5("kept_her", '"One plan, told and kept." {n}She sets the muster beside your copy of the orders.{/n} "Your powers remain unreliable. I still dislike half your decisions. But the men came back, the supplies went through, and you did what you said." {n}She reaches for her pen.{/n} "Bring me the next one before you send it."', c("[Bow to the Queen.]", flags=(PLAN_KEPT,))),
], requires=(PLAN_DISPATCHED,), forbids=(PLAN_KEPT, "trickster.failed"), delay=48)

alive(P + "alive.trial_report", "Four days of orders", '"The Crows have returned, Your Majesty."', [
    nar("start", "{n}Four days of copied orders lie on Galfrey's desk. Two carry your corrections beneath her objections; nine carry your reasons for leaving them unchanged. The Crows' report is on top.{/n}", c("Continue", "report")),
    conv5("report", '"He reached the enemy with the forged order. The Crows took him on his way back. He approached no farm." {n}Her finger rests on the patrol\'s report.{/n} "The sentence was carried out at the north gate this morning. The patrol names every man who saw it. I have read those names."',
        c("Continue", "judgment", requires=(NATIVE_REFUSED,)),
        c("Continue", "judgment_never", forbids=(NATIVE_REFUSED,))),
    conv5("judgment", '"I told you I could not trust you as Galfrey. I had reason. Your powers have not become any less dangerous, but you have stopped treating my objections as an interruption." {n}She lays the report beside your orders.{/n} "You told me what you meant to do. You answered me. You did it. I can trust that."', c("Continue", "message")),
    conv5("judgment_never", '"I have commanded soldiers who promised less than you and failed to keep it. You told me what you meant to do, answered my objections, and did it." {n}She lays the report beside your orders.{/n} "Your powers still trouble me. Your word troubles me rather less. That is a beginning."', c("Continue", "message")),
    conv5("message", "\"The Crows' sergeant has a message for you. You need not make him shout it across the hall.\"",
        c("[Bow to the Queen.]", flags=(TRIAL_KEPT,))),
], requires=(TRIAL_STARTED,), forbids=(TRIAL_KEPT, COMMITTED, "trickster.failed"), delay=96)

beat(P + "commit.answer_report", "The Crows' muster", '\"The Crows\' muster return?\"', [
    ki("start", '"All present. One lame horse, two men who insist they were never cold, and a picket fire visible from the enemy\'s side of the ford." {n}She puts the return on your pile.{/n} "The fire has been moved. I shall tell you about the other matter after the next watch."', c("[Take the return.]", flags=(ANSWER_REPORTED,))),
], requires=(ANSWER_RESERVED,), forbids=(ANSWER_REPORTED, COMMITTED, ANSWER_ALLY, ANSWER_REFUSED, FORD_HANGED),
    delay=24, ForbidOverrides={FORD_HANGED: FORD_ANSWERED})

beat(P + "commit.answer_again", "After the watch", '"You said there was another matter."', [
    ki("start", '"There is. The patrol is done. I have had enough time to decide without an audience."',
        c('"And what did you decide?"', "yes"),
        c('"Do you still want to ride beside me?"', "ally"),
        c('"Tell me plainly, even if it is no."', "refused")),
    ki("yes", '"I want you. I shall come after the ninth bell, and you shall not greet me as though I were reporting for duty." {n}She takes your hand before you can salute.{/n}', c('"I\'ll be there."', flags=(COMMITTED,))),
    ki("ally", '"Beside you in the field, yes. You have my sword when the Crows ride. I will not give you an invitation merely because you waited for one." {n}She fastens her helm to her belt.{/n} "Keep a place for us on the muster."', c("[Accept her answer.]", flags=(ANSWER_ALLY,))),
    ki("refused", '"No, Commander. I considered it. You deserved an answer, and that is mine." {n}Her hand stays on the sword-belt.{/n} "The Crows\' service stands. Leave the other question here."', c("[Leave the question.]", flags=(ANSWER_REFUSED,))),
], requires=(ANSWER_REPORTED,), forbids=(COMMITTED, ANSWER_ALLY, ANSWER_REFUSED, FORD_HANGED),
    delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED})

alive(P + "alive.after_no", "Without the sword", '"You sent for me?"', [
    conv5("start", '"I did. The sword is with my armourer. This time there is no oath between the question and my answer."',
        c('"What is your answer?"', "yes"),
        c('"Would you rather leave it at friendship?"', "ally"),
        c('"If you have decided against it, tell me."', "refused")),
    conv5("yes", '"Stay tonight. I want you beside me when the papers are finished, and considerably closer after that." {n}She closes the dispatch book and takes your hand.{/n}', c("Continue", "approach")),
    nar("approach", '{n}After the ninth bell she is waiting in the Crows\' tent, her hair loose, the green surcoat unlaced at the throat. She catches your collar and kisses you before you can speak. Your back strikes the tent pole; she steadies the lantern without releasing you.{/n} "There. No oath required."', c("Continue", "threshold")),
    nar("threshold", '{n}She works your buckles quickly, then closes your reaching hand around her waist while she loosens her own laces. The surcoat drops beside the lantern. Linen follows it. Her bare shoulders are strong, her skin marked by old pale scars; her breath catches when your mouth finds the hollow above her breast.{/n}\n\n{n}She pulls you down onto the saddle-blankets and settles close over you, bare skin warm against yours, her loose hair brushing both your faces.{/n} "You have kept me talking long enough, Commander." {n}Her knees tighten at your hips. She takes your hand and draws it between your bodies -{/n}', c("[Draw her close.]", "morning")),
    nar("morning", '{n}By first light she is gone. At the Queen\'s table she is crowned and signing dispatches. There is a small bruise above the collar of her gown. She catches you looking and moves the next order toward you.{/n} "Commander." {n}Then, below the clerks\' hearing:{/n} "I slept very well. Do attend to the dispatch before you look so pleased."', c("[Bow to the Queen.]", flags=(COMMITTED, P + "alive.committed"))),
    conv5("ally", '"I would. I value your company, Commander. I can offer it freely without offering more."', c("[Keep her company a while.]", flags=(RESERVED_ALLY,))),
    conv5("refused", '"I have decided against it. The plans you kept mattered. They still matter. They do not oblige me to share your bed." {n}She draws the next dispatch toward her.{/n} "You have my support in the war. Let that suffice."', c("[Accept her answer.]", flags=(RESERVED_REFUSED,))),
], requires=(OATH_RESERVED,), forbids=(COMMITTED, RESERVED_ALLY, RESERVED_REFUSED, "trickster.failed"), delay=48)


# Round 2 authored set pieces: GAL-01/02/03/04. Native service and witnessed
# knowledge are different facts. No paper, rescue, kiss or night earns trust.
def _round2_situations():
    from storylines.galfrey_trickster import SERVICE, LATE_FOUND, history_variant
    from storylines import galfrey_trickster as origin
    for host in SCENES:
        sid = host["Id"].removesuffix("_stall")
        nodes = {node["Id"]: node for node in host["Nodes"]}
        if sid == P + "kitrane.crows":
            nodes["start"]["Text"] = ('"Diminished." {n}She counts on her gauntleted fingers.{/n} "Two veterans. The sergeant tells us he is sixty every morning; '
                'the other tells him to stop. A boy of fourteen learning the sword. And me. We have one leaking tent and one bad-tempered mule." '
                '{n}She looks across the market.{/n} "Anselm should have been here to complain about them."')
            nodes["lie"]["Text"] = ('"The Crows are real. So are the men who carried my command at Iz. Two came back. Anselm went into my tomb." '
                '{n}She looks toward the girl.{/n} "I wore their colours on the march. I shall have to earn my place in them again. '
                'This girl wants to fight demons. She deserves a knight who will teach her properly."')
            history_variant(host, "lie", SERVICE,
                '"The Crows are real. They carried my command at Iz, and took me among their wounded under the name I had kept ready. '
                'Two veterans came home. Anselm went into my tomb." {n}She watches the girl.{/n} '
                '"I came to their tent needing everything. I can give this girl something now. She deserves to be taught properly."', "new_service")
        elif sid == P + "kitrane.sergeant":
            nodes["start"]["Text"] = ('"Sir Anselm, tonight." {n}She sits on an upturned crate, oiling his sword.{/n} '
                '"The Crows have stood behind my chair for forty years. Now I sleep in their tent and learn what their pay buys. '
                'Last night the sergeant told me what Anselm sent home to his daughter. I had never asked."')
        elif sid == P + "kitrane.hulrun":
            nodes["tell"]["Text"] = ('"He would have to investigate the coffin. Sir Anselm\'s name, my command, your eulogy." '
                '{n}She looks toward the chapel.{/n} "Knight Tirabade carried my last order out of Iz. Her part in it would be entered beside the Crows\' testimony. '
                'I will answer for the deception when the campaign can survive that hearing. I shall not summon it merely to ease my conscience tonight."')
            history_variant(host, "tell", CARRIED_IRABETH,
                '"He would have to investigate the coffin. Sir Anselm\'s name, my command, your eulogy." '
                '{n}She looks toward the chapel.{/n} "The two Crows who carried me would have to give evidence. '
                'Knight Tirabade was not given that command. I will answer for the deception when the campaign can survive the hearing. '
                'I shall not summon it merely to ease my conscience tonight."', "crows_carried")
        elif sid == P + "kitrane.irabeth":
            # Do not make an uninformed knight forgive a secret she has not heard.
            for nid in ("drezen", "died_back"):
                if nid == "drezen":
                    nodes[nid]["Text"] = ('"Knight Tirabade does not know. The Crows carried me. Every evening she salutes the Queen\'s empty chair." '
                        '{n}Galfrey looks toward the barracks.{/n} "She ought to hear it from me. I have made her wait long enough."')
                else:
                    nodes[nid]["Text"] = ('"Knight Tirabade fell before I gave my last command. Now she has returned, and I have still let her salute an empty chair." '
                        '{n}Galfrey puts a hand on her sword-belt.{/n} "I shall tell her myself."')
                for choice in nodes[nid]["Choices"]:
                    choice["Next"] = "disclose"
                    choice["Requires"].append("irabeth.present_now")
                nodes[nid]["Choices"].append(c("[Leave her to speak when Knight Tirabade is back.]",
                    forbids=("irabeth.present_now",), abort=True))
            host["Nodes"].extend([
                ki("disclose", '{n}She walks to the barracks and lowers her hood before Irabeth can salute.{/n} '
                    '"Knight Tirabade. The Crows carried me out of Iz. Anselm lies in the royal coffin. I ordered it. '
                    'Do not answer until you have heard all of it."', c("Continue", "irabeth_answer")),
                n("irabeth_answer", "Irabeth", '{n}Irabeth grips the edge of the open door. For a moment she cannot speak.{/n} '
                    '"Your Majesty. We held a vigil. I gave your chair the salute every night." {n}She looks past Galfrey at you, then back.{/n} '
                    '"The watch will hear nothing from me tonight. But I will not take another false order to my knights. Tell me what you mean to do when this war is over."',
                    c("Continue", "disclosure_end", flags=(P + "react.irabeth.learned",)), portrait="Irabeth"),
                ki("disclosure_end", '"You shall hear it from me before the court." {n}Galfrey holds her gaze.{/n} '
                    '"I have given you grief and an empty chair. I will not ask you to thank me for ending either." '
                    '{n}Irabeth steps back to let her into the barracks. The door closes behind them.{/n}', c("[Leave them to speak.]")),
            ])
        elif sid == P + "kitrane.king":
            direct = ('"I know. The whole tavern told me." {n}She gives you an amused look.{/n} '
                '"You made a drunkard a king. At Iz you offered me a knight\'s name, and I ordered the Crows to carry it out. '
                'I think I made the better bargain. My mule cannot demand a royal pension."')
            alone = (
                '"I know. The whole tavern told me." {n}She gives you an amused look.{/n} '
                '"You made a drunkard a king. I chose to be a knight in the rubble at Iz. Your standing orders left me a cart to do it with. '
                'Do not claim my decision as another of your coronations, Commander."')
            history_variant(host, "made", ALONE, direct, "direct")
            nodes["made"]["Text"] = alone
            # Late recovery also records ALONE. Select it before crediting the
            # prepared escape; the Commander was present only at the chapel.
            history_variant(host, "made", LATE_FOUND, alone, "prepared_alone")
            nodes["made"]["Text"] = (
                '"I know. The whole tavern told me." {n}She gives you an amused look.{/n} '
                '"You made a drunkard a king. In the chapel you offered me a knight\'s name, and I chose to answer it. '
                'You were late for that coronation. I shall not let you forget it."')
        elif sid == P + "kitrane.ford":
            nodes["start"]["Text"] = ('{n}She straightens the clasp at your shoulder before reaching for her helm.{/n} "There. The Crows will come. '
                'Myself and both veterans. The boy stays with the mule." {n}She checks the ford map.{/n} '
                '"We ride along the supply road. I want the carters to see us there."')
            # Entry text names only the boy; the acquired girl joins the baggage.
            host["Nodes"].append(ki("girl_with_baggage", '"The girl stays with the boy and the mule. She has learned one guard, Commander, not a battle."', c("[Ride out.]", "ford")))
            nodes["start"]["Choices"][0]["Forbids"].append(CROWS_ORDER)
            nodes["start"]["Choices"].append(c("[Ride out.]", "girl_with_baggage", requires=(CROWS_ORDER,)))
        elif sid == P + "kitrane.conversation":
            nodes["start"]["Text"] = ('"I did." {n}She catches your sleeve as the eel-seller closes her shutters.{/n} '
                '"You have time for a patrol report, two petitions and a quarrel over arrows. You can find time to speak to me." '
                '{n}The curio-seller bends industriously over his accounts.{/n} "Here will do. He can count with his ears shut."')
            nodes["camp"]["Text"] = ('"You flirted with me on the march. I told you to do better." {n}Her thumb presses against your wrist.{/n} '
                '"I noticed when you did. I kept choosing a military subject whenever we were alone. You must have thought me very fond of siege reports."')
            nodes["said"]["Text"] = ('"That I wanted you." {n}She says it plainly, though her grip has tightened.{/n} '
                '"I can argue with your orders and still want your hands on me. You need not settle the war before answering."')
            history_variant(host, "camp", ROMANCE,
                '"I have watched you return to this stall when you had no orders for me. I have watched myself look up every time." '
                '{n}Her fingers tighten on your sleeve.{/n} "You asked for the conversation. Now do not retreat into a dispatch."', "new_courtship")
            nodes["waited"]["Text"] = ('"Then stop looking so solemn." {n}She draws you nearer by the sleeve, glances at your mouth, and releases you with visible reluctance.{/n} '
                '"I have said it. The rest requires a better place than the eel stall. Go before I forget that."')
        elif sid == P + "commit.oath":
            nodes["speak"]["Text"] = nodes["speak"]["Text"].replace("since I walked out of Iz", "since the Crows carried me from Iz")
            nodes["sworn"]["Text"] = ('{n}She rises and salutes. The sword clicks into its scabbard.{/n} "Commander. '
                'The Green Crows are at your disposal: myself, both veterans, the boy squire and the mule. Point us at something."')
            history_variant(host, "sworn", CROWS_ORDER,
                '{n}She rises and salutes. The sword clicks into its scabbard.{/n} "Commander. '
                'The Green Crows are at your disposal: myself, both veterans, the boy squire and the mule. Point us at something."', "boy_only")
            nodes["sworn"]["Text"] = nodes["sworn"]["Text"].replace("the boy squire and", "both squires and")
            for nid in ("invite", "order_q"):
                for choice in nodes[nid]["Choices"]:
                    if choice["Next"] is None:
                        choice["Text"] = '"After the ninth bell. I know the minor orders\' row."'
            nodes["invite"]["Text"] = ('"The Crows\' tent, at the end of the minor orders\' row. The squires are in town with the mule; '
                'the sergeant has agreed to sleep next door." {n}She brings your hand to her lips before letting it go.{/n} '
                '"After the ninth bell. I arranged this before I offered the sword. Do not make me regret the order of my preparations."')
        elif sid == P + "kitrane.table":
            nodes["credit"]["Text"] = ('"As a knight of the Green Crows? They may laugh. Let them examine the distances before they dismiss it." '
                '{n}She rolls up the map.{/n} "Tell them where the guess is, and whose it is. I should like to hear their objections. '
                'I have been brilliant and blamed often enough to survive a council laughing."')
        elif sid == P + "kitrane.crown":
            direct = ('"I shall tell them what happened at Iz: your offer, my last command, the name on the coffin and the wounded knight in the cart." '
                '{n}She looks at you.{/n} "You will answer for the eulogy. I will answer for Anselm. Neither of us can leave the hearing to the other."')
            alone = ('"I shall tell them I chose the escape myself in the rubble. You had prepared the Crows, and you proclaimed the Queen dead. '
                'You were not at my side when I gave the order." {n}She looks at you.{/n} "You will answer for the eulogy. '
                'I will answer for Anselm and the command. The inquiry must hear what happened, not a tidier account."')
            history_variant(host, "how", ALONE, direct, "direct")
            nodes["how"]["Text"] = alone
            history_variant(host, "how", LATE_FOUND, alone, "prepared_alone")
            nodes["how"]["Text"] = ('"I shall tell them you came to the chapel after I had fallen at Iz. '
                'You offered the name beside the open coffin. I ordered Anselm put in my place." {n}Her hand rests on his sword.{/n} '
                '"The sergeant must account for the vigil. You must account for the eulogy. I shall account for the order."')
            nodes["must"]["Text"] = ('"I gave the order that put him in the coffin. I can answer for it now. '
                'Do not ask me to leave Anselm\'s daughter with a missing father to spare myself a hearing."')
            nodes["certain"]["Text"] = ('"No. I mistook certainty for good judgment at Iz." {n}She touches the sword-hilt.{/n} '
                '"I have considered the regents, the border and Anselm\'s daughter. I have made my decision. I am telling you because you matter to me."')
        elif sid == P + "visit.tent":
            # The reel's deferred kiss is collected here, by her action. Selected
            # answer flags identify the invitation without deriving commitment.
            saved = P + "reel_kiss_saved"
            origin.DERIVED[saved] = [[P + "kitrane.reel.saved"], [P + "kitrane.reel_stall.saved"]]
            for reel in SCENES:
                if reel["Id"].removesuffix("_stall") == P + "kitrane.reel":
                    reel_nodes = {n["Id"]: n for n in reel["Nodes"]}
                    marker = reel["Id"] + ".saved"
                    if marker not in reel_nodes["saved"]["Choices"][0]["Set"]:
                        reel_nodes["saved"]["Choices"][0]["Set"].append(marker)
            history_variant(host, "armour", saved, nodes["armour"]["Text"], "no_deferred_kiss")
            nodes["armour"]["Text"] = ('{n}She catches your collar and kisses you before you can touch a buckle.{/n} '
                '"There. The fiddler cannot whistle here." {n}She holds out her gauntlets.{/n} "Now take these off. '
                'I have had squires do it most of my life. Tonight I want your hands. The straps are under the pauldrons."')
            history_variant(host, "majesty", saved, nodes["majesty"]["Text"], "no_deferred_kiss")
            nodes["majesty"]["Text"] = ('"Your Majesty? In the place you chose because nobody could whistle?" '
                '{n}She catches your collar, laughing, and kisses you until you stop trying to answer.{/n} '
                '"There. Now the gauntlets. I cannot do much with these on."')
            nodes["after"]["Text"] = ('{n}Before dawn she lies against you, her hand spread on your chest. When you stir, she draws you back for a kiss.{/n} '
                '"Not yet." {n}The sergeant coughs in the next tent. She shuts her eyes.{/n} "Damn him. '
                'The drill, then. Keep that cloak warm. I shall want it when I come back."')
            for nid in ("morning", "morning_alone"):
                nodes[nid]["Text"] = nodes[nid]["Text"].replace("She does not stay; she is a knight of the Green Crows, and the Crows drill at first light.",
                    "She dresses before the first-light muster.")
            nodes["drill"]["Text"] = ('{n}An Eagle Watch column passes on the ford road. Kitrane finishes the exercise, hears both veterans\' objections, '
                'and dismisses the drill. She comes back to the tent with her doublet damp and her sword sheathed.{/n} '
                '"You have found your boots. A pity." {n}She sits beside you and takes the warm cloak, leaning against your shoulder.{/n} '
                '"Stay until the camp wakes properly. Then I shall walk back with you."')
            slot = host["Id"] + ".explicit.1"
            # Explicit-slot brief: her directed first night, returned body,
            # no witness, rescue obligation or political decision in the act.
            import json
            from pathlib import Path
            brief = json.loads((Path(__file__).parents[1] / "tools/route_packs/explicit_slots/galfrey" / (slot + ".json")).read_text(encoding="utf-8"))
            nodes["cut"]["Choices"][0]["Next"] = slot
            host["Nodes"].append(nar(slot, brief["default_text"], c("Continue", "after")))
        elif sid == P + "kitrane.grey":
            nodes["four"]["Text"] = ('"Four! Liar." {n}She straightens, laughing, and traps your hand against her cheek.{/n} '
                '"The sergeant inspected my sword for half an hour. You have inspected my hair for less than a minute and already invented a defect."')
            nodes["ear"]["Text"] = ('"A handsome ear." {n}She turns her head into your hand and kisses your palm.{/n} '
                '"That is a very poor report. Keep looking. I like your method rather better than your accuracy."')
            nodes["mind"]["Text"] = ('"The first one, yes. I borrowed this mirror twice to be sure." {n}She puts it away and smooths your collar.{/n} '
                '"These can wait. I have a patrol to inspect, and you to keep me awake afterwards. Come back tonight."')
            nodes["end"]["Text"] = ('{n}She pockets the mirror and draws you close enough to brush her lips against your ear.{/n} '
                '"The same tent. I shall be back from the pickets before the ninth bell. '
                'We can put the lantern where it was last time. Your boots rather further from the flap."')
        elif sid == P + "alive.kitrane":
            host["Entry"] = '"Will you hear one of my plans before I put it into motion?"'
            host["DelayHours"] = 0
            nodes["start"]["Text"] = ('{n}Galfrey sets down the dispatch she was signing. The clerks wait at the far table.{/n} '
                '"A whole plan, Commander. I dislike discovering the dangerous part after the wagons have left."')
            nodes["refused"]["Text"] = ('"I told you I could not trust your powers or your judgment. I meant it." {n}She leans back.{/n} '
                '"Kitrane rode with your column. A plain surcoat did not make her a less exacting judge. '
                'You are offering to tell me the plan before sending it. That is new. Begin."')
            history_variant(host, "refused", SERVICE,
                '"I told you I could not trust your powers or your judgment. I meant it." {n}She leans back.{/n} '
                '"There was a disguise I considered before the march: Kitrane of the Green Crows. I never rode in it. '
                'Do not ask me to be less exacting because I could answer to a knight\'s name. Tell me your plan."', "new_name")
            history_variant(host, "never", SERVICE,
                '"I once considered riding with the Green Crows as Kitrane, an old friend of yours. I remained in Nerosyan." '
                '{n}She studies you.{/n} "An old friend would still want to know whether the drivers come home. You may begin there."', "new_name")
            nodes["never"]["Text"] = ('"Kitrane once rode with your column. She saw how your plans worked from the road." '
                '{n}Her mouth twitches.{/n} "Tell me this one before she has to find out from the survivors."')
        elif sid in (P + "alive.plan", P + "alive.trial", P + "alive.oath"):
            host["DelayHours"] = 0
            if sid == P + "alive.trial":
                nodes["start"]["Text"] = ('{n}She draws the chair beside hers out from under the dispatch table. The clerk at the far end pauses, then returns to his work.{/n} '
                    '"Sit here. I want to see the whole map this time." {n}Her hand rests briefly on your sleeve before she takes up her pen.{/n} "Go on."')
        elif sid == P + "alive.plan_report":
            host["DelayHours"] = 24
        if sid in (P + "alive.oath", P + "alive.after_no"):
            if sid == P + "alive.after_no":
                nodes["approach"]["Text"] = ('{n}At the ninth bell she meets you at the Crows\' tent, takes your hand and brings you inside. '
                    'The finished dispatch book lies beside the lantern. She turns it face down, then catches your collar and kisses you.{/n} '
                    '"I have heard enough objections for tonight. Come closer."')
                nodes["threshold"]["Text"] = ('{n}She opens your collar and draws your shirt from your shoulders. Her own surcoat is already unlaced; '
                    'she slips it off and lets the linen follow, then brings you down onto the blankets. '
                    'Her hair falls against your face as she kisses you again, slower this time.{/n} '
                    '"Yes. Here." {n}She moves close, bare skin against yours, and draws your hand between you —{/n}')
            else:
                nodes["refuse"]["Text"] = ('{n}She sheathes the sword and rises, keeping your offered hand.{/n} "A very fine oath. Wasted." '
                    '{n}Her thumb presses your pulse; then she pulls you against her and kisses you, hard enough to make you take a step back. '
                    'She laughs once, breathlessly, before kissing you again.{/n} "Stay. I want that answer."')
            nodes["morning"]["Text"] = ('{n}At first light she dresses and returns to her dispatches. Later you find her crowned at the table; '
                'a small bruise shows above her collar. She catches you looking and pushes the next order toward you.{/n} '
                '"Attend to that before you look so pleased." {n}When it is sealed she dismisses the clerks and comes around the table. '
                'Her fingers close on your collar again.{/n} "Now. Where were we?"')
            slot = host["Id"] + ".explicit.1"
            # Explicit-slot brief: living Queen's own invitation after kept
            # reports; reserved yes has no oath, no returned-Iz scar or witness.
            import json
            from pathlib import Path
            brief = json.loads((Path(__file__).parents[1] / "tools/route_packs/explicit_slots/galfrey" / (slot + ".json")).read_text(encoding="utf-8"))
            nodes["threshold"]["Choices"][0]["Next"] = slot
            host["Nodes"].append(nar(slot, brief["default_text"], c("Continue", "morning")))
        if sid in (P + "commit.answer_again", P + "alive.after_no"):
            # Her declaration precedes the acceptance; a request for candour is
            # never interpreted as the player's choice to make her refuse.
            nodes["start"]["Text"] += ' {n}She looks directly at you.{/n} "I want you to stay. If you would rather keep this to service, say so. I have finished deciding for myself."'
            nodes["start"]["Choices"][0]["Text"] = '"Then I want to stay."'
            nodes["start"]["Choices"][2]["Text"] = '"Tell me plainly: is that what you want?"'
            nodes["start"]["Choices"][2]["Next"] = "yes"
            # Keep the refusal node and expose it with an honest appended exit.
            nodes["start"]["Choices"].append(c('"I do not want to begin this. Let us leave the courtship here."', "refused"))
            nodes["refused"]["Text"] = ('"Then it ends here." {n}She takes up her sword-belt.{/n} '
                '"You shall still have my support in the campaign. Neither of us need pretend that means more."')


_round2_situations()

# Authored late living account, held unregistered: departure_lint requires an
# entry in tools/departure_contracts.json, outside this task's edit scope.
# Coordinator: register this nonromantic surface and append it to SCENES only
# with the matching Galfrey present_now contract. No Last Call entitlement.
from story_format import p
ALIVE_UNFINISHED = scene(P + "epilogue.alive_unfinished", "The orders still waiting", "GalfreyEpilogue", 6, "", [
    nar("page", '{n}Galfrey stood with the crusade at Threshold and returned to Mendev still crowned. '
        'Her dispatch desk had held more than campaign business, but no shared future had been agreed. She kept her own counsel on that question.{/n}',
        paragraphs=(
            p('{n}The riverbed muster lay among the plans she kept: the drivers accounted for and the column through. '
              'She had asked to see the next plan before it left the Commander\'s desk.{/n}', requires=(PLAN_KEPT,)),
            p('{n}A copy of the riverbed orders remained in her papers. The Commander had paid for the wagons and dispatched them; '
              'she had not yet received the returning muster.{/n}', requires=(PLAN_DISPATCHED,), forbids=(PLAN_KEPT,)),
            p('{n}She had received the four-day report and answered the Commander\'s objections in the margins. '
              'Her trust in their word had grown. She had not offered a night merely because the reports were kept.{/n}', requires=(TRIAL_KEPT,)),
            p('{n}The four-day review had begun, with the farms under the Crows\' watch. '
              'The war ended before she received its final report. She would not call an unfinished test a kept promise.{/n}', requires=(TRIAL_STARTED,), forbids=(TRIAL_KEPT,)),
            p('{n}She had put her sword away and reserved her personal answer. Threshold came before she gave it. '
              'The Commander had her aid in the campaign; she had promised nothing more.{/n}', requires=(OATH_RESERVED,), forbids=(RESERVED_ALLY, RESERVED_REFUSED)),
            p('{n}She and the Commander kept the company she had offered. When she returned to Drezen on royal business, '
              'she brought the campaign maps to their table. The invitation ended there.{/n}', requires=(RESERVED_ALLY,)),
            p('{n}Their courtship had ended with a plain answer. She wrote to the Commander about the border and the crusade, '
              'and did not reopen the personal question.{/n}', requires=(RESERVED_REFUSED,)),
        )),
], requires=("trickster.ever", FINAL, EVENING),
    forbids=(DEAD, RETURNED, COMMITTED, ROMANCE, FINISHED, CLOSED, "sacrifice", "lastcall.active"),
    last=6, Relationship=REL, ForbidOverrides={"sacrifice": "trickster.commander_back"})
