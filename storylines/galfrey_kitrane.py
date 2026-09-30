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
from storylines.galfrey_trickster import (SEELAH_BED, CARRIED_CROWS, CARRIED_IRABETH,
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
    # Fallback: right of the tiefling trader (Terendelev front 2.5 and Mielarah behind 2.5 are each 3.5 m away).
    HUB_FB: dict(Unit=DISGUISED, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TIEFLING, Side="right", Distance=2.5),
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
    ki("start", '''"I did." {n}She lifts one foot for inspection: stout brown leather, badly stitched at the heel, a size too large.{/n} "Four silver. The stallholder asked five, I offered three, and he looked at me with such pity that I paid four and thanked him. I have never bought anything in my life, Commander. Somebody else always paid." {n}She flexes her toes inside the boot with evident satisfaction.{/n} "The Crows' paymaster advanced me a month's wage against my good character. Four silver and a lecture on thrift. I have spent the four silver."''',
        c('"And the lecture?"', "lecture"),
        c('"You were cheated."', "cheated")),
    ki("lecture", '''"I am saving it." {n}Perfectly grave.{/n} "He told me a knight who cannot keep a month's wage for a week will end by selling her sword. I have heard that same speech from my treasurer, in the council chamber, about the whole of Mendev. It was much more convincing in a tent, from a man with ink on his cuffs."''',
        c("Continue", "morning")),
    ki("cheated", '''"Abominably." {n}She looks delighted.{/n} "By a man with one eye and a very sad story about his mother. I did not believe a word of it, and I paid him anyway, and he winked at me when he gave me my change. The Queen would have had him flogged, or given him a pension. Kitrane has been cheated at a market stall, like anybody." {n}She considers the boots.{/n} "They pinch. I intend to wear them until they do not."''',
        c("Continue", "morning")),
    ki("morning", '''"I have been standing here since the sixth bell. Nobody has bowed. Nobody has asked me to decide anything." {n}She watches a woman go past with a basket of eels, a boy with a crate of chickens, two off-duty pikemen arguing about a girl.{/n} "A child sold me a pie. It was cold in the middle. I ate it standing up, in the street, with my fingers." {n}Something moves in her face, and is mastered.{/n} "I have eaten at every high table between Nerosyan and Absalom, Commander. I do not think I have ever enjoyed a meal so much."''',
        c('"What will you do with the rest of the day?"', "day"),
        c('[Flirt] "You have pie on your chin, Kitrane."', "chin")),
    ki("chin", '''{n}Her hand goes to her chin before she can stop it. There is no pie on her chin. She looks at you for a long, flat second, with the whole century of her reign in it.{/n} "That," says Kitrane of the Green Crows, "was impudent." {n}Then she laughs, a real laugh, and a pikeman turns to look.{/n} "Nobody has lied to me for my own amusement in a hundred years. Do it again sometime. Not today."''',
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
    ki("letter", '''"She will get no letter." {n}Galfrey's voice is perfectly level, which is how you know.{/n} "She will get a grave with no one in it, and a crypt with the wrong man in it, and a lifetime of looking at every grey-haired knight who comes through the gate." {n}She takes the broadsheet back and folds it, precisely, along its tearing seam.{/n} "I did that. I did it with my last breath as Queen, and I would do it again, and I cannot make those two things lie down together."''',
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
    ki("start", '''{n}She is holding a small steel mirror, the kind soldiers use to shave, at arm's length, and frowning at it the way she frowns at a map with a bad road on it.{/n} "I have found a grey hair." {n}She turns the mirror so you can see, which you cannot.{/n} "Here. Above the left temple. I have not had a grey hair in eighty years."''',
        c('"You\'re a hundred years old, Kitrane."', "old"),
        c('[Flirt] "It suits you."', "suits")),
    ki("suits", '''"Flatterer." {n}But she looks at the mirror again, and something in her frown eases.{/n} "The Queen would have had it plucked before breakfast by a lady of the bedchamber whose family has held that office for four generations. Kitrane has only the one mirror, and it belongs to the Crows' sergeant." {n}She lowers it.{/n} "But that is not why I am frowning."''',
        c("Continue", "old")),
    ki("old", '''"The church of Iomedae bought the Queen her years." {n}She says it the way she said it once in a war camp, to a stranger who asked.{/n} "Sun orchid elixir. Twice, a cup of it was set before me at the altar, bought at a price that would have fed Mendev for a winter. I was needed, they said. I accepted." {n}Her hand closes on the mirror.{/n} "The second cup was meant to last until they could find a third. It is beginning not to. And the church does not buy a third cup for a knight of the Green Crows."''',
        c("Continue", "grow")),
    ki("grow", '''"I am going to grow old, Commander." {n}She says it very simply.{/n} "I had forgotten that it was a thing that happens to people. That one wakes one morning with a knee that aches in the rain, and a grey hair, and then another. I have been the same age for eighty years." {n}She is quiet.{/n} "I lay awake last night, and I could not tell whether I was frightened or glad. I think I was both, in turns, until the Crows' squire started snoring and I could no longer think at all."''',
        c('"The church would give it back if you told them who you are."', "church"),
        c('"Does it frighten you?"', "frighten"),
        c('[Flirt] "Then I\'ll get to watch. I\'ve always wanted to see what you look like when you\'re sixty."', "watch")),
    ki("church", '''"Yes. They would." {n}Flatly.{/n} "They would find a third cup, and give me back the crown with it, and thank Iomedae for the miracle, and in five years the Queen would be forty again and Sir Anselm would still be in her crypt." {n}She puts the mirror away.{/n} "No. They bought the Queen. They cannot have Kitrane. Whatever years she has, she will have them the way everyone else does: one at a time, and badly."''',
        c("[Leave it there.]", flags=(ELIXIR,))),
    ki("frighten", '''"A little." {n}She considers.{/n} "I have faced demon lords and not been frightened. I have faced the bishops of Iomedae over a budget and been very frightened indeed. This is nearer the second." {n}A dry sideways look.{/n} "But I chose it. That makes a difference I did not expect. A fear one chooses is a sort of possession. I have so few."''',
        c("[Leave it there.]", flags=(ELIXIR,))),
    ki("watch", '''{n}She stares at you. Then she laughs, low and helpless, and has to put a hand on the stall to steady herself, and the curio-seller looks up in alarm.{/n} "Sixty." {n}She wipes her eyes.{/n} "Commander, I have been sixty. It was a very long time ago, and I had a great deal less patience then. You have no idea what you are asking for." {n}And then, lower, still smiling:{/n} "But you are asking to be there for it. Nobody has ever asked me that."''',
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
    ki("mind", '''"Perhaps." {n}She does not sound sure.{/n} "Or perhaps she is patient. I have been her servant for a hundred years. She knows I will come and tell her, in the end, and she is waiting until I do." {n}A breath.{/n} "I have not been into her chapel since Iz. I stand at the door. It is the first time in my life I have been afraid of the Inheritor, and I find it is not her I am afraid of."''',
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
    ki("listen", '''"I stand at the back, in the dark, and listen." {n}She looks down at her new boots.{/n} "I have known that man thirty years. I have signed his warrants and argued with him over the fire and the rack until we were both hoarse. I have never once heard him be kind to anyone." {n}Very low:{/n} "And every night he kneels on those stones, and is kind to me."''',
        c("Continue", "sign", requires=(EULOGY_SIGN,)),
        c("Continue", "why", forbids=(EULOGY_SIGN,))),
    ki("risk", '''"It is. I take it anyway." {n}Unrepentant.{/n} "Hulrun has hanged cultists on less evidence than a woman who stands at the back of a chapel with her hood up. I know. I read his reports." {n}She shrugs, a knight's shrug, armour creaking.{/n} "But he has never once turned round. He does not expect the dead to come and listen. Nobody does."''',
        c("Continue", "sign", requires=(EULOGY_SIGN,)),
        c("Continue", "why", forbids=(EULOGY_SIGN,))),
    ki("sign", '''"Except that last night he did." {n}Her voice drops.{/n} "At the end, after the last amen. He turned his head and looked at the door, the way a man looks at a draught. I went away very quickly." {n}She meets your eyes.{/n} "He was in the chapel when you spoke of a knight of a minor order who slept under canvas. He is not a stupid man, Commander. He is a great many things I dislike, but he is not stupid."''',
        c("Continue", "why")),
    ki("why", '''"Do you know why I keep going?" {n}She does not wait for you to answer.{/n} "Because he is the only person in Drezen grieving for the Queen as she actually was. Not the legend. Not the chronicles. The difficult old woman who took his budget away and would not let him burn a priest of Desna." {n}A breath.{/n} "He misses her. I find that I owe him the courtesy of hearing it."''',
        c('"Then keep going. I\'ll deal with it if he turns round."', "end"),
        c('"Stop. For both our sakes."', "stop"),
        c('"You could tell him."', "tell")),
    ki("stop", '''"No." {n}Not unkindly, but with the whole weight of a century behind it.{/n} "You may command a knight of the Green Crows in the field, Commander. You may not command her prayers." {n}Then, gentler:{/n} "I shall stand further back. That is the most I can promise."''',
        c("Continue", "end")),
    ki("tell", '''"And make him choose between his Queen and his office?" {n}She shakes her head.{/n} "He would choose the office. He always has; it is why the Church keeps him. He would have to name what he saw at Iz a demon's trick, and me a thing wearing her face, and he would light the fire with his own hands and weep while he did it." {n}She looks toward the chapel.{/n} "No. It is not only my secret. It is Knight Tirabade's, and Sir Anselm's, and yours. I shall not spend it to ease an old man's grief."''',
        c("Continue", "end")),
    ki("end", '''"Kitrane has begun to pray for him in return. At the back, very quietly. It seems only fair." {n}The ghost of a smile.{/n} "I do not suppose the Inheritor has ever before had two people praying for each other's souls in the same chapel while one of them believes the other is dead. She must find it very instructive."''',
        c("[Leave her to her market.]", flags=(HULRUN_SEEN,))),
], requires=(FIRST,), forbids=(HULRUN_SEEN, "hulrun.dead", "hulrun.away_c5"), delay=24)


# --- 6. The Knight-Captain's silence -----------------------------------------------------------------------------------------

beat(P + "kitrane.irabeth", "The Knight-Captain", '"You were watching the barracks."', [
    ki("start", '''"I was." {n}She does not pretend otherwise.{/n}''',
        c("Continue", "alive", requires=(CARRIED_IRABETH,), forbids=("irabeth_dead",)),
        c("Continue", "alive", requires=(CARRIED_IRABETH, "irabeth_dead", "irabeth.trickster.returned")),
        c("Continue", "drezen", forbids=(CARRIED_IRABETH, "irabeth_dead")),
        c("Continue", "drezen", requires=("irabeth_dead", "irabeth.trickster.returned"), forbids=(CARRIED_IRABETH,)),
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
    ki("gone", '''"Knight Tirabade is dead." {n}Her voice does not change, which is how you know what it costs.{/n} "She carried my last command out of Iz and then she did not come home. The Crows who carried me say she was quiet all the way to the gate. She had the order in her ears and nothing else." {n}Her hands tighten on the pommel.{/n} "I look at the barracks because I keep expecting her to come out of it. It is a habit. I have a great many habits I am going to have to break."''',
        c("Continue", "end")),
    ki("drezen", '''"Knight Tirabade was in Drezen when I fell; the Queen had left her to hold the city. She does not know." {n}Galfrey's hands are folded on the pommel of her sword, very still.{/n} "She salutes the Queen's empty chair at the high table every evening, I am told. She wept for me in front of her whole company. And every day I stand in the same square as the most honest knight in Mendev and let her grieve a lie." {n}A breath.{/n} "The Crows carried me. They are old men and very discreet. She is neither, and she would never forgive them for it. So I keep my hood up."''',
        c('"She\'d want to know."', "ask"),
        c('"Do you want me to tell her?"', "talk")),
    ki("gone_before", '''"Knight Tirabade is dead." {n}Her voice does not change, which is how you know what it costs.{/n} "She fell at Iz before I could give her anything to carry. I called her name with my last command in my mouth, and two old Crows came instead." {n}Her hands tighten on the pommel.{/n} "I look at the barracks because I keep expecting her to come out of it. It is a habit. I have a great many habits I am going to have to break."''',
        c("Continue", "end")),
    ki("end", '''"Go on, Commander. I shall stand here a while longer. The barracks has a very interesting door."''',
        c("[Leave her watching.]", flags=(IRABETH_SPOKEN,))),
], requires=(FIRST,), forbids=(IRABETH_SPOKEN,), delay=36)


# --- 7. The dragon's sorcery (and the dragon) --------------------------------------------------------------------------------

beat(P + "kitrane.iz", "The dragon's sorcery", '"Does the wound still trouble you?"', [
    ki("start", '''{n}She turns down the collar of her surcoat, briefly, so that you can see it: a pale, puckered seam running from her collarbone down under the mail, healed as if it were years old. There is no dark light in it now. There is nothing in it at all.{/n} "It aches in the cold. It will ache in the cold for the rest of my life, I expect. That is only a scar. I have a great many."''',
        c("Continue", "read", requires=(READ,)),
        c("Continue", "rent", forbids=(READ,))),
    ki("read", '''"It let go on the road, as you said it might. At the second milestone. I felt it open like a hand." {n}She fastens the collar again.{/n} "I have thought about it a great deal since. You saw it flinch at my title. You wagered my life on what you saw. You were right, and you did not know that you were right, and you did it anyway."''',
        c("Continue", "dragon")),
    ki("rent", '''"It let go when the bells rang. Not before." {n}Her voice catches on the last word, the faint tearing sound it makes now on certain syllables, and she waits for it to pass with the patience of long habit.{/n} "It left that behind. The priests of the Crows say it will not mend. I say I have had a century of speeches; the world can manage with fewer of mine."''',
        c("Continue", "dragon")),
    ki("dragon", '''"Terendelev was our protector and friend." {n}She says it the way she said it at Iz, to her knights, before the charge; you can hear her remembering it.{/n} "I went to Iz to grant rest to her soul and her body. That was the duty. I would have done it with my own hands, and I very nearly did."''',
        c("Continue", "back", requires=(TERENDELEV_BACK,)),
        c("Continue", "rest", forbids=(TERENDELEV_BACK,))),
    ki("back", '''"And then I heard what you did at the bones." {n}She looks at you steadily.{/n} "You went into the fire after her. You opened your own wound over what was left, and a woman walked out, and now she sits on a crate in the lower town and lets children stare at her." {n}A long breath.{/n} "I have seen her. I went and stood across the street, in my hood, the way I stand at the chapel door. I did not cross it."''',
        c('"Do you hate her?"', "hate"),
        c('"Do you want to?"', "hate")),
    ki("hate", '''"No." {n}She sounds almost surprised at herself.{/n} "It was not her claw that rent me. It was the thing he made of her bones. I have been a paladin long enough to know the difference between a sword and the hand on it." {n}Then, drier:{/n} "I envy her, a little, which is worse. She died, and she came back as herself, and the whole lower town knows her name. I died, and came back as a knight nobody has heard of." {n}A beat.{/n} "I granted her rest, and you undid it. You seem to make a habit of undoing my duties, Commander."''',
        c("Continue", "end")),
    ki("rest", '''"She is at rest. I made sure of that, at least, before the sorcery took me. It is the one thing I did at Iz that I am entirely certain of." {n}Her hand rests a moment on the scar under her collar.{/n} "Her voice used to carry across the whole square in Kenabres at the festival. I heard it once, when I was a young woman, and I thought: that is what the protector of a city should sound like." {n}She shakes her head.{/n} "Mine has a tear in it now, or it does not. Either way it was never that."''',
        c("Continue", "end")),
    ki("end", '''"Enough of scars. They are dull things to talk about, except to the people who have them." {n}She turns back to the crowd.{/n} "Come back when you have something more cheerful. A demon's head, say. Or a better pie."''',
        c("[Leave her to the crowd.]", flags=(IZ_SPOKEN,))),
], requires=(FIRST,), forbids=(IZ_SPOKEN,), delay=24)


# --- 8. The order of one -----------------------------------------------------------------------------------------------------

beat(P + "kitrane.crows", "An order of one", '"How are the Crows?"', [
    ki("start", '''"Diminished." {n}She counts on her gauntleted fingers.{/n} "The sergeant, who is sixty and says so every morning. The squire, who is fourteen and says nothing at all. And me, who am two weeks old in the war camp and a hundred and some in every other respect. We have one tent, which leaks, and one mule, which bites." {n}She looks rather pleased about all of it.{/n} "The Green Crows were never a great order. Small enough that nobody checks. That was the point of them."''',
        c('"And now?"', "now")),
    ki("now", '''"And now a girl from the eel stall has asked to join." {n}She nods across the market, where a thin, sunburned girl of perhaps sixteen is gutting eels with savage concentration and glancing over every few moments.{/n} "Her brother died on the walls when the city was retaken. She wants to learn the sword. She asked me because, she said, I look like somebody who has never once been told no." {n}A dry breath.{/n} "I have been told nothing else for a week."''',
        c('"Take her."', "take"),
        c('"You can\'t afford a squire on four silver a month."', "afford"),
        c('"Is it fair to make her a Crow? The Crows are a lie."', "lie")),
    ki("take", '''"I shall." {n}She says it at once, as if she had only been waiting for somebody to agree.{/n} "I cannot knight her; I am a knight of an order of three, and our patent of arms is in a trunk in Nerosyan under another name. But I can take a squire. Any knight can." {n}She is already watching the girl.{/n} "No council to consult, no succession to weigh, no bishop to ask. I have made a great many choices in my life, Commander, and every one of them was Mendev's. This one is only mine."''',
        c("Continue", "swear")),
    ki("afford", '''"I cannot afford a mule on four silver a month, and I have one." {n}Unperturbed.{/n} "The sergeant says the girl can gut eels for the camp and sleep in the leaking half of the tent. It is a better bargain than the Crown ever made with its squires; they got silk and tutors and never once learned to sharpen their own blades." {n}She glances at you.{/n} "I shall take her. I only wanted you to argue with me first. Nobody argues with me any more. Kitrane is too unimportant."''',
        c("Continue", "swear")),
    ki("lie", '''{n}She is quiet.{/n} "Yes. They are. They were a lie I told in a war camp, and three good men wore it for me, and one of them is in my tomb." {n}She looks at the girl.{/n} "But a lie that people keep, and bleed for, and teach the sword under, becomes something else in time. I have seen it happen to kingdoms." {n}A dry note.{/n} "Mendev was a lie once. A handful of knights and a grudge. Ask any Sarkorian."''',
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
    ki("decide", '''"No." {n}She says it without heat.{/n} "I have judged more of these than you have seen, and I sent most of them to the Inquisition and some of them to the rope, and I never once lost sleep." {n}She wipes her blade on the reeds.{/n} "I asked to be a face in your crowd, Commander. I do not get to hand the decision back to the Queen when it is ugly. You are the Commander. Command."''',
        *FORD_ORDERS),
    ki("hang", '''{n}Nobody moves. Then your sergeants start for the prisoners, because orders are orders.{/n}
"No." {n}Kitrane sheathes her sword, very deliberately.{/n} "I will not." {n}She does not raise her voice; she does not need to.{/n} "Not the boy, not the woman, not the four men. They surrendered to a knight. A knight does not hang what surrendered to her at a ford for the convenience of the baggage train." {n}She looks at you across the reeds.{/n} "The Queen was never once given an order, Commander. I find that Kitrane can refuse one."''',
        c('"Then stand aside. It will be done without you."', "hanged"),
        c('"Noted. Do it anyway, sergeant."', "hanged")),
    nar("hanged", '''{n}She stands aside. She watches it done, all of it, to the last kick of the last rope, and when it is done she mounts her horse and rides back to Drezen alone, at a walk, with her squire and the mule and the two old Crows strung out behind her like mourners.{/n}
{n}She does not speak to you that night, or the next morning. On the second day she is back at the curio stall, and nods to you, and says nothing about the ford at all. It is very much worse than shouting.{/n}''',
        c("[Let her be.]")),
    ki("trial", '''{n}Something goes out of her shoulders that you had not known was there.{/n} "Bind them," {n}she tells the Crows' sergeant, and then, to you, lower:{/n} "Thank you." {n}She watches the boy being hauled to his feet.{/n} "The Queen would have sent them to Hulrun, and Hulrun would have burned at least four of them, and I would have signed the warrant. I do not know that Kitrane is any kinder than the Queen was. I know that tonight she did not have to decide."''',
        c('"You would have refused, if I\'d ordered them hanged?"', "would"),
        c("[Ride back to Drezen beside her.]", "home")),
    ki("would", '''"Yes." {n}Without hesitation.{/n} "And I would have stood aside while your sergeants did it, and hated you for a week, and come back to the market after. That is what it means to follow somebody. It is very new to me." {n}Dry:{/n} "I did not say it was pleasant."''',
        c("[Ride back to Drezen beside her.]", "home")),
    nar("home", '''{n}You ride back side by side, the prisoners stumbling on a rope behind the mule, the squire full of a battle she watched from a hillock. Halfway home Kitrane takes off her helm to let the wind at her hair, and does not put it back on, and three farmers at a gate stare at her as she goes by without the faintest idea why.{/n}''',
        c("[Let the road run out.]")),
], requires=(FIRST, CROWS_ORDER), forbids=(FORD,), delay=24)



# --- 9b. After the ford: her terms (the hanging is a breach until it is answered) ------------------------------------------------

beat(P + "kitrane.ford_after", "Six ropes", '"You haven\'t spoken to me since the ford."', [
    ki("start", '''"No." {n}She is standing very straight by the curio stall, in full armour, as if on parade.{/n} "I have been deciding whether to leave. The Crows' sergeant has packed the mule twice. I unpacked it twice." {n}Her hand is white on the pommel of the old sword.{/n} "There was a boy of fifteen at that ford, Commander. He surrendered to a knight. I have hanged men, and signed for the hanging of more, and I have never once hanged a boy who had put his hands on his head for me."''',
        c("Continue", "terms")),
    ki("terms", '''"So. Terms." {n}The Queen's voice, the one that ended wars.{/n} "His name was Tobin; the Inquisition's clerk wrote it down before the rope. His mother sells tallow in the lower town. You will go to her yourself, and tell her who gave the order, and pay for his grave, and not send a clerk." {n}A breath.{/n} "And never again, under the Crows' colours or near them. That is all. It is not small. It is not meant to be."''',
        c('"Agreed. All of it. I\'ll go today."', "agreed", flags=(FORD_PROMISED,)),
        c('"It was the right call. I won\'t apologise to a cultist\'s mother."', "refused")),
    ki("agreed", '''{n}She looks at you for a long breath, and some of the parade goes out of her shoulders.{/n} "Then I shall unpack the mule a third time." {n}Quietly:{/n} "I will not forget the six of them, Commander. I do not ask you to. I ask you to remember them in the same place I do."''',
        c("[Go to the lower town.]")),
    ki("refused", '''"Then I am your knight, and I shall do my duty, and there it will stay." {n}Without heat, which is worse.{/n} "The mule stays packed. When you are ready to walk down to the tallow-seller's, Commander, I shall still be here. I am old. I can wait." {n}She salutes.{/n}''',
        c("[Leave her.]", abort=True)),
], requires=(FIRST, FORD_HANGED), forbids=(FORD_PROMISED, FORD_ANSWERED), delay=24)


# --- 9c. The tallow-seller (a visit: the terms kept) -------------------------------------------------------------------------------

page(P + "kitrane.tallow", "The tallow-seller", [
    nar("start", '''{n}The tallow-seller's stall is two streets below the curio stall, in the part of the lower town where the gutters run grey. She is a small woman with burned hands, and she knows who you are before you open your mouth; everybody in Drezen knows the Commander's face.{/n}
{n}You tell her anyway. That her son Tobin surrendered at the eastern ford with his hands on his head. That a knight of the Green Crows refused to hang him. That you gave the order, and it was carried out.{/n}''',
        c("Continue", "mother")),
    nar("mother", '''{n}She does not weep. She listens to the whole of it with her burned hands folded on the counter, and when you have finished and put the purse for the grave down beside them, she looks at it a long while and does not touch it.{/n}
{n}"He was a fool," she says at last. "He went to the Locust men because they fed him. I told him he would hang." {n}She pushes the purse back an inch, and then, slowly, draws it to her.{/n} "You came yourself. The knights never come themselves." {n}That is all she says. You buy two candles from her, because it seems wrong to leave with nothing, and she wraps them, and you go.{/n}''',
        c("Continue", "kitrane")),
    nar("kitrane", '''{n}At the top of the street, by the curio stall, a knight in a green surcoat has been watching the whole time from under her hood. She does not come down. When you reach her she takes one of the candles out of your hand without a word, and puts it inside her surcoat, next to the broadsheet about Sir Anselm.{/n}''',
        c("[Stand beside her a while.]", flags=(FORD_ANSWERED,))),
], requires=("trickster.ever", RETURNED, FORD_PROMISED), forbids=(FORD_ANSWERED, CLOSED), delay=12, kind="visit", Areas=[DREZEN])
tag(P + "kitrane.tallow", "T")

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
    ki("end", '''"If the Queen of Mendev had ever drunk in that tavern she would have closed it by morning. Kitrane intends to go back on Thursday. He owes her a rematch at dice, and she suspects he cheats worse than she does."''',
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
    ki("burned", '''"Or you had. One from the Queen, begging forgiveness from a wall. And one from Kitrane, the night before the Fane, which you burned in the Abyss because it named me. I approve. It was the right thing to do." {n}Drily:{/n} "It was also the only letter anyone ever wrote me that I wished had been kept."''',
        c("Continue", "choice")),
    ki("kept", '''"One from the Queen, begging forgiveness from a wall. And one from Kitrane, the night before the Fane, which you carried through the Abyss next to your heart like a fool." {n}Her voice is not quite steady.{/n} "The Queen asked you to forgive her. Kitrane asked you where the road went. I think I prefer Kitrane's. She was braver, and she was two weeks old."''',
        c("Continue", "choice")),
    ki("choice", '''"What will you do with it?"''',
        c('"Give it back to you. It\'s yours."', "give"),
        c('"Keep it. You wrote it to me."', "keep"),
        c('"Answer it." [Take her hand.] "I forgive you."', "forgive")),
    ki("give", '''{n}She takes it from you, and looks at it, and without a word she folds it once more and tucks it inside her surcoat, next to the broadsheet about Sir Anselm.{/n} "The Queen's things," she says. "I seem to be collecting them. I shall have a trunk of her soon, like any other widow."''',
        c("[Leave her with it.]", flags=(LETTER_SPOKEN,))),
    ki("keep", '''"I did." {n}A long breath.{/n} "Keep it, then. Keep it somewhere no Inquisitor goes. And if I am ever tempted to be the Queen again, show it to me, and remind me what she was like at the end of a day."''',
        c("[Put it away.]", flags=(LETTER_SPOKEN,))),
    ki("forgive", '''{n}Her hand is cold, and very still in yours, and then it is not.{/n} "That," she says, not quite steadily, "is a thing I have wanted to hear from you since the night I wrote it, and I would have had you flogged for saying it to the Queen." {n}She does not take her hand back.{/n} "Kitrane will allow it. Just this once. In a market. Where nobody is looking."''',
        c("[Hold her hand a moment longer.]", flags=(LETTER_SPOKEN,))),
], requires=(FIRST, FAREWELL), forbids=(LETTER_SPOKEN,), delay=24)


# --- 12. The conversation the Queen kept putting off (the native romance, remembered) ----------------------------------------

beat(P + "kitrane.conversation", "The conversation", '"You said we never had our conversation."', [
    ki("start", '''"I did." {n}She takes a breath like a woman stepping into cold water.{/n} "Very well. Here, then, among the eels and the curio-seller and his dreadful astrolabes. The Queen always meant to have it somewhere with a door that shut." {n}A dry glance.{/n} "Kitrane has discovered that doors are overrated."''',
        c("Continue", "camp")),
    ki("camp", '''"In the war camp you tried to kiss my hand, and I told you that if you wanted to impress me, you would have to do better than that. Do you remember?" {n}She does not wait.{/n} "You did better. You did a great deal better, over and over, all the way to Drezen and out of it, and I noticed every time, and I told you nothing, because a queen does not." {n}Her jaw sets.{/n} "In Drezen, before the Fane, I stopped you on the stair and asked to speak with you alone. I nearly said it then. I said something about strategy instead."''',
        c('"What would you have said?"', "said"),
        c('[Flirt] "Say it now. Nobody\'s listening."', "said")),
    ki("said", '''"That I did not want a Knight Commander." {n}Very low, and very clear.{/n} "I had a hundred of those. I wanted you. The stubborn, impossible creature who looked at a map of the Worldwound as if it were a puzzle somebody had left out for them. I wanted to be the one person in the world you did not treat as a puzzle." {n}A breath.{/n} "And then I sent you into the Abyss, because the Queen had to. And wrote 'forgive me' to a wall."''',
        c("Continue", "now")),
    ki("now", '''"So." {n}She squares her shoulders, knight to Commander.{/n} "There it is. A hundred years late and a crown short. Kitrane has no talent for these things; she is two weeks old and has never been courted by anyone who knew who she was." {n}The corner of her mouth moves.{/n} "You do know who she is. That is the difficulty."''',
        c('[Kiss her] "I know exactly who she is."', "kiss", flags=(CONVERSATION,)),
        c('"I\'ve been waiting a long time to hear that."', "waited", flags=(CONVERSATION,)),
        c('"Then let\'s take it slowly. We have time now."', "slow", flags=(CONVERSATION,))),
    nar("kiss", '''{n}She lets you. Her mouth is warm and startled and then not startled at all; her gauntleted hand comes up and closes on the back of your neck, hard, a sword-hand, and holds you there as if you might be taken away.{/n}
{n}When she lets go, the curio-seller is staring at you both with his mouth open, and she turns and gives him a look that has made ambassadors withdraw. He finds something very interesting to do with a box of amulets.{/n}
{n}"There," says Kitrane, a little breathless. "That was overdue."{/n}''',
        c("[Leave her before either of you says anything foolish.]")),
    ki("waited", '''"I know." {n}A flicker of the old severity.{/n} "I kept you waiting deliberately. It is an old habit of monarchs. It establishes the terms." {n}Then, much softer:{/n} "I have no terms left to establish. I find that I do not want any. It is a very alarming feeling, Commander, and I should like you to go away now so that I can have it in private."''',
        c("[Go, smiling.]")),
    ki("slow", '''"Slowly." {n}She looks at you as if you had offered her something rare.{/n} "Nobody has ever let me do anything slowly. There was always a war, or a council, or a bishop at the door." {n}She nods.{/n} "Very well. Slowly. Do not mistake it for reluctance, Commander. It is appetite, taking its time."''',
        c("[Leave her with that.]")),
], requires=(FIRST, ROMANCE), forbids=(CONVERSATION,), delay=36)


# --- 13. News from Nerosyan ---------------------------------------------------------------------------------------------------

beat(P + "kitrane.mendev", "News from Nerosyan", '"More broadsheets?"', [
    ki("start", '''"More broadsheets." {n}She has three of them spread on the curio-seller's counter, weighted with his brass, and he has given up protesting.{/n} "They say the council of regents in Nerosyan met four times this week and agreed on nothing but the colour of the mourning. They say a cousin of mine in the south has discovered a great-grandmother he never mentioned before. They say the knights of two orders have gone home to guard the border, because without the Queen, why stay?"''',
        c('"How much of it is true?"', "true"),
        c('"Does it hurt, reading it?"', "hurt")),
    ki("true", '''"Some of it. The part about the great-grandmother, certainly; I have met him. He has been discovering relatives since he was twelve." {n}Dry, and then not.{/n} "And the knights. That part is true. I can see it in the gaps on the muster boards." {n}She lays a flat hand on the paper.{/n} "My death sows chaos among our forces. I said so, in the war camp, to you. I was right. I had hoped, a little, to be wrong."''',
        c("Continue", "tempt")),
    ki("hurt", '''"Like pressing on a bruise." {n}She does not look up from the paper.{/n} "I built that council. I chose every one of those regents myself, for a day when I should not be there. They are good men and women, and they are quarrelling like cats in a sack because I am not there to tell them which of them is right." {n}A breath.{/n} "I always told them. I never once taught them to decide."''',
        c("Continue", "tempt")),
    ki("tempt", '''"I could end it." {n}She says it very quietly.{/n} "I could ride to Nerosyan, walk into that council chamber in this surcoat, take off my hood, and say four words. By nightfall there would be no quarrel at all." {n}Her hand closes on the broadsheet.{/n} "And by the next nightfall, the Queen would be back, and Sir Anselm would still be in her crypt, and nobody in Mendev would ever again learn to decide anything without her."''',
        c('"Then go. Mendev needs you."', "go"),
        c('"Let them learn. It\'s the last thing you can teach them."', "learn"),
        c('"Could you really walk back in?"', "could")),
    ki("go", '''"Mendev has needed me for a hundred years." {n}Not unkindly.{/n} "That is rather the trouble, Commander. You of all people should understand what it is to be needed so much that wanting becomes a luxury." {n}She folds the papers.{/n} "Not yet. Perhaps not ever. But thank you for saying it plainly. The regents never did."''',
        c("Continue", "orders")),
    ki("learn", '''{n}She looks up at last, and something like gratitude moves across her face and is put carefully away.{/n} "Yes. That is what I have been telling myself since dawn, and it sounds a great deal better in your voice than in mine." {n}She folds the broadsheets into a neat square.{/n} "Let them quarrel. They will learn, or they will not, and either way it will be theirs."''',
        c("Continue", "orders")),
    ki("could", '''"Easily." {n}At once.{/n} "That is what frightens me. The crown is not a weight, Commander. It is a shape, and I have been that shape so long that I could step back into it without a stumble." {n}She touches the green surcoat at her breast.{/n} "This is the first thing in a century I have had to learn to wear. I should like to learn it properly before I decide whether to take it off."''',
        c("Continue", "orders")),
    ki("orders", '''{n}She taps one broadsheet, then another, with the precision of a woman reading a muster roll.{/n} "The Eagle Watch are staying. The Order of the Crimson Bridle and the knights of the Southern March are going: two hundred lances, and their paymaster's reason is that nobody has paid them since Iz." {n}Very drily:{/n} "Nobody has, because I used to, out of the privy purse, and I am dead. That is my doing, Commander, and I shall not pretend otherwise."''',
        c("[Pay the two orders' arrears out of the crusade's coffers.]", "paid", flags=(MENDEV, P + "mendev.paid"), crusade=("Finances", -400)),
        c('"Let them go home. Mendev\'s border needs them too."', "let_go", flags=(MENDEV, P + "mendev.let_go"))),
    ki("paid", '''"Four hundred in gold, for two hundred lances." {n}She nods once, the way she used to nod at a treasurer.{/n} "It is a fair price. It is also the price of my holiday, and I shall remember that every time I buy boots." {n}She folds the broadsheets away.{/n} "Thank you. Do not tell them where the idea came from."''',
        c("[Leave her with her papers.]")),
    ki("let_go", '''"Yes." {n}After a moment.{/n} "Yes, they do. The border was always thin; I kept it thin to feed the crusade. They will be of more use at home than sulking in Drezen." {n}She does not sound as if she believes all of it.{/n} "Two hundred lances fewer at Threshold. I shall stand in one of the gaps myself. It seems only fair."''',
        c("[Leave her with her papers.]")),
], requires=(FIRST,), forbids=(MENDEV,), delay=48)


# --- 14. The market reel -------------------------------------------------------------------------------------------------------

beat(P + "kitrane.reel", "The market reel", '"There\'s music in the square."', [
    nar("start", '''{n}Somebody has brought a fiddle to the market, and somebody else a drum made from a crusader's shield, and in the space between the eel stall and the curio-seller a ring of off-duty soldiers and market women is stamping through a reel that is older than Mendev. Kitrane stands at the edge of it with her arms folded, watching the way she watches everything.{/n}''',
        c("Continue", "watch")),
    ki("watch", '''"I have danced at every court between Nerosyan and Absalom. Pavanes. The slow galliard. A thing in Taldor that takes forty minutes and involves a fan." {n}Her foot is keeping time on the cobbles, apparently without her knowledge.{/n} "I have never once danced this. The Queen watched it from a balcony at the harvest fair, every year, and I used to think: what must it be like, to be allowed?"''',
        c('[Offer your hand] "Find out."', "dance"),
        c('"Nobody\'s stopping you."', "dance")),
    nar("dance", '''{n}She hesitates for exactly as long as it takes a queen to overrule a century. Then she unbuckles her sword-belt, hands it to her squire, and takes your hand, and you are in the ring.{/n}
{n}She is terrible at it. She is terrible at it with enormous dignity for the first turn and with rapidly diminishing dignity for the second, and by the third she has trodden on a pikeman's foot and apologised to him with a curtsey that makes the whole ring roar, and she is laughing so hard she can barely stand.{/n}''',
        c("Continue", "breath")),
    nar("breath", '''{n}When the fiddler finally takes pity on everyone and stops, she is flushed to the ears and her hair has come out of its tie, and she is holding onto your arm with both hands as if the cobbles might tip her over. Her breath is warm against your jaw. Somebody whistles.{/n}
{n}"Commander," she says, low, not letting go. "Do you know the most extraordinary thing about being nobody?"{/n}''',
        c('"Tell me."', "nobody")),
    ki("nobody", '''"If you kissed me now, in front of the whole market, not one of these people would care." {n}Her eyes are very bright.{/n} "They would whistle, and go back to their eels. Nobody would write it down. Nobody would send an envoy to ask what it meant for the succession."''',
        c("[Kiss her in front of the whole market.]", "kissed", flags=(REEL,)),
        c('[Flirt] "Then I\'ll save it for somewhere they can\'t whistle."', "saved", flags=(REEL,))),
    nar("kissed", '''{n}They whistle. They go back to their eels. The fiddler strikes up again, something slower, and a pikeman with a bruised foot shouts something about officers that makes Kitrane laugh into your mouth.{/n}
{n}"There," she says when she can. "Nobody wrote it down." {n}She does not let go of you for some time.{/n}''',
        c("[Stay for the next dance.]")),
    ki("saved", '''"Somewhere they cannot whistle." {n}Her mouth curves slowly.{/n} "You are a very careful strategist, Commander. I have always admired it in you. I am beginning to find it maddening." {n}She lets go of your arm at last, and retrieves her sword-belt, and buckles it on without looking at it.{/n} "Choose the ground well. I intend to hold you to it."''',
        c("[Leave her flushed and laughing.]")),
], requires=(FIRST, HANDS), forbids=(REEL,), delay=24)


# --- The commit: she kneels, and the Commander refuses her oath ---------------------------------------------------------------

beat(P + "commit.oath", "The oath", '"The Crows\' sergeant says you asked for me."', [
    nar("start", '''{n}It is dusk, and the market is closing: shutters going up, the eel-girl sluicing her stall, the curio-seller counting his takings with his back to the wall. Kitrane is waiting by the stall in her plain armour, polished until it looks almost new, with her old sword at her hip and the green surcoat freshly brushed.{/n}
{n}"I did," she says. "I have something to say to you, and I should like to say it here, where nobody will pay the slightest attention."{/n}''',
        c("Continue", "ford", requires=(REFUSED_ORDER,)),
        c("Continue", "trial", requires=(FORD_TRIAL,)),
        c("Continue", "speak", forbids=(REFUSED_ORDER, FORD_TRIAL))),
    ki("ford", '''"I refused you at the ford, and you hanged them anyway, and then you walked down to the tallow-seller's, as I asked." {n}She says it first, so that it is out of the way.{/n} "I would refuse you again. I want you to know that I have not forgotten the six of them, and that I have come anyway, and that what I am about to do is not obedience. I have had a century of obedience. I know what it looks like, and this is not it."''',
        c("Continue", "speak")),
    ki("trial", '''"At the ford you sent six cultists back to Drezen to stand trial, when you had a rope and a tree and nobody to stop you." {n}She nods, once.{/n} "I watched you decide. That is why I am here."''',
        c("Continue", "speak")),
    ki("speak", '''"A knight of the Green Crows owes service. I have lived on the Crows' pay and your army's bread since I walked out of Iz, and I have sworn to nobody. That is not how a knight lives." {n}She draws her sword. Then, in the straw and the eel-water and the last of the light, the Queen of Mendev goes down on one knee in front of you and holds it out, hilt first, across her forearm.{/n}''',
        c("Continue", "oath")),
    ki("oath", '''"Kitrane of the Green Crows offers her sword to the Commander of the Fifth Crusade." {n}Her voice is quite steady, and carries no further than it needs to.{/n} "In the Inheritor's sight, to serve until released or dead." {n}She looks up at you.{/n} "In a war camp, a long time ago, I gave you an army and a title. You never knelt for either. I thought it only fair that one of us should."''',
        c("Continue", "crowd")),
    nar("crowd", '''{n}Nobody in the market so much as turns their head. A knight kneeling to an officer is nothing; there are a dozen such oaths sworn in Drezen every week. The eel-girl, her squire, has stopped sluicing and is holding her breath. Otherwise the world goes on shutting up for the night around the Queen of Mendev on her knees in the straw.{/n}''',
        c('[Refuse her oath; offer your hand] "No. I won\'t take your sword. Get up."', "refuse"),
        c('[Accept her oath] "I accept it. Rise, Kitrane of the Green Crows."', "sworn", flags=(SWORN,))),
    ki("refuse", '''{n}She does not get up. She stays exactly where she is, with the sword across her arm, and looks at your outstretched hand as though it were a piece of very bad news from the front.{/n} "You refuse the fealty of a knight. In the middle of a market." {n}Very evenly:{/n} "I have had oaths refused before, Commander. Always by people who wanted something better. What do you want?"''',
        c('"I don\'t want your sword. I want you."', "yes"),
        c('"Nobody should own your oath again. Least of all me."', "yes"),
        c('[Flirt] "I want you on your feet, so I can kiss you properly."', "yes")),
    ki("yes", '''{n}For the space of a breath the Queen of Mendev looks at you with the whole of her reign in her face: every envoy, every oath, every knight she ever sent into the Wound.{/n}
{n}Then Kitrane sheathes her sword, and takes your hand, and lets you pull her up out of the straw, and does not let go.{/n} "Then I shall have to find something else to give you." {n}Her other hand comes up to your face.{/n} "And I find I know exactly what."''',
        c("Continue", "kiss")),
    nar("kiss", '''{n}She kisses you in the closing market like a commander taking a hill: slowly, and then all at once. Her hand is on your jaw, callused from a hundred years of the sword, and very sure. Somewhere nearby the curio-seller drops a brass astrolabe, and does not pick it up.{/n}
{n}Nobody else looks. That is the whole point, and she is smiling against your mouth because of it.{/n}''',
        c("Continue", "invite")),
    ki("invite", '''"The Crows' tent is at the end of the minor orders' row in the field camp. It leaks on the left. The sergeant sleeps like a stone and the squire will be at her mother's; I have already arranged it." {n}She steps back, and her eyes are very bright, and very steady.{/n} "Come tonight, after the ninth bell. Bring nothing. And do not keep me waiting, Commander. I have done enough of that for both of us."''',
        c('"I\'ll be there."', flags=(COMMITTED,)),
        c('[Flirt] "Is that an order, Kitrane?"', "order_q")),
    ki("order_q", '''"From a knight of a minor order to the Commander of the crusade?" {n}She lets the corner of her mouth go.{/n} "Certainly not. It is a promise. I have been told I am rather good at keeping those."''',
        c('"Then I\'ll be there."', flags=(COMMITTED,))),
    ki("sworn", '''{n}She rises at once, smoothly, and salutes, and the sword goes back into its scabbard with a click.{/n} "Commander." {n}It is correct. It is entirely correct.{/n} "The Green Crows are at your disposal: one knight, one sergeant, one squire, one mule. Point us at something."''',
        c("Continue", "sworn2")),
    ki("sworn2", '''{n}Something in her face has closed, gently, like a book.{/n} "The Queen had knights. I used to wonder what it was like from their side." {n}A pause.{/n} "It is very simple, it turns out. One knows exactly where one stands." {n}She salutes again.{/n} "Good night, Commander."''',
        c("[Return the salute.]")),
], requires=(FIRST,), forbids=(COMMITTED, SWORN, FORD_HANGED), delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED},
    RequiresAnyGroups=[[REEL, CROWS_ORDER, KING_SEEN, CONVERSATION], [NAMED, KEPT, HANDS, ELIXIR, LETTER_SPOKEN]])


# --- The release: the soft no answered ----------------------------------------------------------------------------------------

beat(P + "commit.release", "Released", '"I have something to say to my knight."', [
    ki("start", '''"Commander." {n}She is at attention before you have finished speaking. She has been at attention, you realise, every time you have seen her since the market at dusk: correct, prompt, unfailingly courteous, and not once laughing.{/n} "The Crows are ready. What are your orders?"''',
        c('[Release her from the oath] "I release you, Kitrane. From the oath, and from my service."', "release"),
        c('"Nothing. Carry on."', abort=True)),
    ki("release", '''{n}She does not move.{/n} "On what grounds?" {n}The Queen's voice, the one that has heard a great many petitions.{/n} "A knight is released for three reasons, Commander. Death, disgrace, or a better use. I am not dead, and I have not disgraced you. What better use do you have for me?"''',
        c('"I was wrong to take it. I should have refused."', "choose"),
        c('"None. I want you free, and then I want you to choose."', "choose"),
        c('"I don\'t want a knight. I want Kitrane."', "choose"),
        c('[Command her] "You\'re released. Now come to my tent tonight."', "ordered")),
    ki("ordered", '''{n}Something in her face shuts, gently, like a book.{/n} "You release me from one order and give me another in the same breath." {n}She salutes, precisely.{/n} "No, Commander. Not like that. Not ever like that. I have had a century of being sent for." {n}She turns on her heel.{/n} "When you know the difference, you know where the Crows' tent is. Until then I am your knight, and nothing else."''',
        c("[Let her go.]", abort=True)),
    ki("choose", '''{n}For a long breath she simply looks at you, and the correctness goes out of her face a little at a time, like armour being unbuckled.{/n} "Choose." {n}She tries the word.{/n} "You took my oath, and I let you, because it was easier than being refused. And then I stood at attention for two days waiting for you to notice what you had done." {n}She draws a breath.{/n} "Very well. Released. Hear what I choose, then."''',
        c("Continue", "yes")),
    ki("yes", '''{n}She steps in close, closer than any knight stands to her Commander, and puts her hand flat on your chest.{/n} "I choose you. Not your service. Not your army. You." {n}Very low:{/n} "The Crows' tent, at the end of the minor orders' row. After the ninth bell. Bring nothing, and do not dare salute me."''',
        c('"I\'ll be there."', flags=(COMMITTED,)),
        c('[Kiss her] "Consider it an order refused."', flags=(COMMITTED,))),
], requires=(SWORN,), forbids=(COMMITTED, FORD_HANGED), delay=48, ForbidOverrides={FORD_HANGED: FORD_ANSWERED})


# --- The Crows' tent (a visit: the night, the threshold, the cut, and the morning drill) ----------------------------------------

page(P + "visit.tent", "The Crows' tent", [
    nar("start", '''{n}The field camp outside Drezen is dark but for cookfires, and the minor orders' row is the darkest part of it. At its far end a tent sags a little to the left, and a mule tethered by the flap lays back its ears at you as you pass. From somewhere inside the next tent a sergeant of sixty is snoring, pointedly.{/n}
{n}A single lantern is burning inside the Crows' tent. Kitrane is standing beside it in full plain armour, as if for inspection.{/n}''',
        c("Continue", "armour")),
    ki("armour", '''"I kept it on." {n}Before you can say anything.{/n} "I have been armoured and unarmoured by squires every day of my life since I was fifteen. Some of them were very good. None of them were you." {n}She lifts her chin, and her eyes are very dark in the lantern light.{/n} "I have put this night off since the war camp, Commander, for good reasons, every one of them Mendev's. I am done putting it off. I want to be taken out of this armour by someone I chose."''',
        c("[Start with the gauntlets.]", "buckles"),
        c('[Flirt] "Your Majesty\'s armourer, at your service."', "majesty")),
    ki("majesty", '''"Don't." {n}But she is laughing, low in her throat.{/n} "Or do. There is nobody here to hear it but the mule, and I am told the mule has no politics." {n}She holds out her hands.{/n} "Gauntlets first. Then I shall instruct you, since you clearly need it."''',
        c("[Start with the gauntlets.]", "buckles")),
    nar("buckles", '''{n}She instructs you. She instructs you in exactly the voice she uses on a parade ground: left pauldron, the strap underneath, no, the other strap, have you never taken off a suit of plate in your life? You have, and you tell her so, and she says that you have plainly only taken it off corpses, and then she starts to laugh and cannot stop.{/n}
{n}The Queen of Mendev, standing in a leaking tent with one pauldron off and her own Commander fumbling at the buckle of her cuirass, laughing until she has to lean on your shoulder: nobody in a hundred years has ever seen it. You are the only one who ever will.{/n}''',
        c("Continue", "mail")),
    nar("mail", '''{n}The cuirass comes away, and the tassets, and the mail she shrugs off herself with a soldier's practised twist. Underneath she is in a padded arming doublet, dark with sweat at the collar, and she stops laughing.{/n}
{n}She unlaces the doublet herself, slowly, watching you the whole time, her fingers very sure. Under it the linen is thin and old. At her collarbone the pale seam of Iz runs down beneath the cloth, and she does not try to hide it. She takes your hand and lays it there, over the scar, and holds it.{/n}''',
        c("Continue", "want")),
    ki("want", '''"There." {n}Her voice has gone low and rough.{/n} "That is where the Queen ended. Everything below it is Kitrane's, and Kitrane knows exactly what she wants and has decided to have it." {n}Her hand tightens over yours.{/n} "I am not asking you for anything either. I am telling you. I want you, Commander, and I intend to be thorough about it."''',
        c("[Kiss the scar.]", "scar"),
        c("[Let her lead.]", "lead")),
    nar("scar", '''{n}You bend your head and put your mouth to the seam of it, and she draws a breath like a woman surfacing from deep water. Her hands go into your hair, and pull, and hold you there, and then drag you up to her mouth.{/n}''',
        c("Continue", "bed")),
    nar("lead", '''{n}She leads. She undresses you the way she took apart a war council, one article at a time, in a sensible order, with a total absence of hurry that is very nearly unbearable, and she kisses every piece of you she uncovers as if taking possession of a province.{/n}''',
        c("Continue", "bed")),
    nar("bed", '''{n}The linen goes over her head and away into the dark of the tent. In the lantern light she is all long, hard lines, a swordswoman's shoulders and a century of scars, pale seams and old white nicks, and the new one at her collarbone like a signature. There is no crown anywhere on her. She is more beautiful for it than any portrait of her ever painted.{/n}
{n}The Crows' bedroll is three saddle-blankets and a cloak on the ground. She pulls you down onto it by the collar of what is left of your shirt, and laughs again, softly, at nothing, at everything.{/n}''',
        c("Continue", "cut")),
    nar("cut", '''{n}"Kitrane," you say, because it is the only name she has left, and she answers it with her whole body, rising under you, her knees tightening at your hips. Her hand closes over yours and draws it down between you, and her eyes stay open on your face, full of the same unhesitating certainty she has carried onto every field she ever meant to win.{/n}
{n}Outside, the mule shifts its feet. The lantern gutters, and steadies, and burns on.{/n}''',
        c("Continue", "after")),
    ki("after", '''{n}Much later, in the grey before morning, she lies with her head on your shoulder and one hand spread flat on your chest, as if keeping a place in a book.{/n} "I have slept beside no one in a hundred years." {n}Her voice is drowsy and quite unsurprised.{/n} "I did not know that I would like it. One learns such a lot, being nobody." {n}She yawns.{/n} "The Crows drill at first light. I am the only knight. I shall be late, and the sergeant will say so."''',
        c('"Stay."', "morning", requires=(CROWS_ORDER,)),
        c("[Pull the cloak over her shoulders.]", "morning", requires=(CROWS_ORDER,)),
        c('"Stay."', "morning_alone", forbids=(CROWS_ORDER,)),
        c("[Pull the cloak over her shoulders.]", "morning_alone", forbids=(CROWS_ORDER,))),
    nar("morning", '''{n}She does not stay; she is a knight of the Green Crows, and the Crows drill at first light. By the time you have found your boots she is out on the trampled ground behind the tent in her padded doublet with the old sword in her hand, running the eel-girl through a guard, while the sergeant of sixty leans on the mule and offers loud, contradictory advice.{/n}''',
        c("Continue", "drill")),
    nar("morning_alone", '''{n}She does not stay; she is a knight of the Green Crows, and the Crows drill at first light. By the time you have found your boots she is out on the trampled ground behind the tent in her padded doublet with the old sword in her hand, running the forms alone against the morning, cut and guard and cut, while the sergeant of sixty leans on the mule and offers loud, contradictory advice.{/n}''',
        c("Continue", "drill")),
    nar("drill", '''{n}A column of the Eagle Watch goes by on the road to Drezen. Not one of them looks twice at a knight of a minor order at her drill in the mud. Not one of them salutes. Kitrane watches them pass out of the corner of her eye, and her face, when she turns back to her forms, is so full of something that you have to look away from it.{/n}
{n}"Nobody saluted," she tells you afterwards, sheathing her sword. "I have been saluted every morning of my life. I did not know how heavy it was until this one."{/n}''',
        c('"Get used to it."', flags=(TENT, DRILL)),
        c("[Salute her, very badly.]", flags=(TENT, DRILL))),
], requires=("trickster.ever", COMMITTED), forbids=(TENT, CLOSED, FORD_HANGED), delay=8, ForbidOverrides={FORD_HANGED: FORD_ANSWERED}, Areas=[DREZEN])
tag(P + "visit.tent", "T")


# --- After: the war table ------------------------------------------------------------------------------------------------------

beat(P + "kitrane.table", "The war table", '"I want your eyes on the maps for Threshold."', [
    ki("start", '''{n}She looks at you for a moment as if you had asked her to put the crown back on.{/n} "A knight of the Green Crows has no business at the Commander's war table." {n}And then, because she is who she is, she is already reaching for the rolled maps under your arm.{/n} "Show me."''',
        c("[Spread the maps on the curio-seller's counter.]", "maps")),
    ki("maps", '''{n}She reads them the way other people read letters from home: fast, and then slowly, and then with a finger tracing the lines.{/n} "You will go in along the old Sarkorian road, here, because it is the only road. They know that. They have known it for a century." {n}Her finger stops.{/n} "Every crusade has gone in along that road, and every crusade has found the same three places where the ground gives way. I lost my first army at the second of them. Here. I was very young, and very sure."''',
        c('"What would you do?"', "would"),
        c('"Tell me about your first army."', "first")),
    ki("first", '''"Four hundred men of the Mendevian levy, and I was so proud of them I could barely sit my horse." {n}Flatly.{/n} "The ground opened under the vanguard and something came up out of it that had no name in any book I had read. We lost a hundred and sixty in a quarter of an hour. I learned more in that quarter hour than in all the years since." {n}She taps the map.{/n} "So. That is what I would do."''',
        c("Continue", "would")),
    ki("would", '''"Send the baggage along the road, loudly, with every banner you own, and the army a day behind it along the dry riverbed to the east, where no crusade has ever gone because no crusade has ever been willing to lose its wagons." {n}She looks up.{/n} "You would lose the wagons. You would lose the men who drive them, unless you choose them very carefully and pay them very well. The Queen could never have ordered it. It is exactly the sort of thing you would do."''',
        c('"I\'ll take it to the council as your plan."', "credit"),
        c('"I\'ll take it to the council as mine."', "mine")),
    ki("credit", '''"As the plan of a knight of the Green Crows?" {n}Her mouth twitches.{/n} "They will laugh you out of the chamber, and then they will adopt it, and in a year somebody will write a treatise about the brilliant unknown knight who advised the Commander at Threshold." {n}She rolls the maps up neatly.{/n} "Do it. I should enjoy being brilliant and unknown. I have never tried it."''',
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
    ki("how", '''"They will. And I shall tell them: that I lay dying at Iz, and the Commander of the crusade offered me another name, and I took it." {n}A thin smile.{/n} "You will be answering for that, Commander, before bishops and regents and the whole of the Mendevian court, for years. I am sorry. I am not sorry enough not to do it."''',
        c("Continue", "kitrane")),
    ki("kitrane", '''"Kitrane will not end. She will have a crown on again, that is all, and know the difference between the woman and the hat." {n}She turns to you at last.{/n} "I shall take no more elixir. The church may offer it; I shall refuse it at the altar, in front of them all. The Queen of Mendev will grow old like anybody, and when she is tired, she will abdicate, and go and be a knight of some small order that nobody has heard of."''',
        c('"I\'ll stand beside you in the cathedral."', "end_crown", flags=(CROWN,)),
        c('"You don\'t have to do this."', "must", flags=(CROWN,))),
    ki("must", '''"No. I do not have to. That is why I can." {n}Quite gently.{/n} "For a hundred years I chose for Mendev, and chose well. This I choose for myself. You taught me the difference, at Iz, with a name. Do not try to unteach it now."''',
        c("Continue", "end_crown")),
    ki("end_crown", '''"After Threshold, then." {n}She looks back out at the Wound.{/n} "Until then I am Kitrane of the Green Crows, and I have a squire to drill, and a mule who bites. Do not tell anyone, Commander. I should like to enjoy the last of it."''',
        c("[Stand with her on the wall until the light goes.]")),
    ki("kept", '''"You said Sir Anselm chose to stand beside me, and still does. I have decided you were right." {n}She breathes out, slowly.{/n} "He keeps his post in the crypt at Nerosyan. The Queen stays dead. His daughter has his sword-belt, and every year, on the day of Iz, she will find a purse at her door from a knight who owed him a debt. It will never be enough. It will be every year until I die."''',
        c('"And the crown?"', "crown")),
    ki("crown", '''"Mendev will find another. It will quarrel first, and it will make mistakes, and it will learn to decide without me, which it should have learned fifty years ago." {n}She touches the green surcoat at her breast.{/n} "I shall take no more elixir. I shall grow old in a leaking tent, and teach eel-girls to hold a sword, and nobody will ever salute me again. Kitrane, for good."''',
        c('"Kitrane, for good."', "end_forever", flags=(FOREVER,)),
        c('"Are you certain?"', "certain", flags=(FOREVER,))),
    ki("certain", '''"No." {n}Promptly.{/n} "I was certain every day of my reign, and look where it brought me: dying in a rubble-heap, being asked what becomes of Mendev." {n}Her mouth curves.{/n} "I am not certain. I am decided. It is a much more comfortable thing to be."''',
        c("Continue", "end_forever")),
    ki("end_forever", '''"There. It is said." {n}She leans her forearms on the parapet beside yours.{/n} "Now stand here with me a while and look at the weather over the Wound, as if we were two knights with nothing better to do. I have always wanted to do that, too."''',
        c("[Stand with her on the wall until the light goes.]")),
], requires=(), forbids=(FOREVER, CROWN), delay=48, RequiresAnyGroups=[[NAMED, KEPT]])



def integrate(payload):
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
        c("Continue", "seelah_drezen", forbids=(SEELAH_BED, "seelah_dead", "seelah_gone")),
        c("Continue", "stranger", requires=("seelah_dead", SEELAH_BED)),
        c("Continue", "stranger_absent", requires=("seelah_dead",), forbids=(SEELAH_BED,)),
        c("Continue", "stranger", requires=("seelah_gone", SEELAH_BED), forbids=("seelah_dead",)),
        c("Continue", "stranger_absent", requires=("seelah_gone",), forbids=("seelah_dead", SEELAH_BED))),
    ki("seelah", '''"Your paladin. The one with the quick hands, who cut purses in Solku before she ever held a sword for the Inheritor." {n}She turns the pie over in its paper.{/n} "She walked up to me, bought this from the girl with the tray, put it in my hands, and walked away again. She did not say a word. She did not look at my face." {n}A long breath.{/n} "She was at the bed at Iz. She cried out, 'Your Majesty!', and I felt the thing in me turn its head at it like a hound."''',
        c('"She knows."', "knows"),
        c('"She\'s kind. That\'s all."', "kind")),
    ki("seelah_drezen", '''"Your paladin. The one with the quick hands, who cut purses in Solku before she ever held a sword for the Inheritor." {n}She turns the pie over in its paper.{/n} "She walked up to me, bought this from the girl with the tray, put it in my hands, and walked away again. She did not say a word. She did not look at my face." {n}A long breath.{/n} "She was not at Iz. She has only ever seen the Queen across a war council, and at the head of a column. And she looked at me across a market for as long as it takes to count a purse, and knew."''',
        c("Continue", "knows")),
    ki("knows", '''"She knows." {n}Quietly.{/n} "A thief knows a disguise; a paladin knows a lie. She is both, and she has decided to be neither where I am concerned." {n}She looks at the pie.{/n} "The Queen would have summoned her and thanked her formally and given her a ring. Kitrane has no rings. Kitrane is going to eat the pie, standing up, and think well of her for the rest of her life. I believe that is the better bargain for both of us."''',
        c("Continue", "end")),
    ki("kind", '''"Kindness is never all, Commander. Not in a paladin." {n}She shakes her head.{/n} "Kindness is what one does with what one knows. She knows, and she bought me a pie. I have had dukes do a great deal less with a great deal more." {n}She takes a bite at last, and burns her tongue, and swears like a sergeant.{/n}''',
        c("Continue", "end")),
    ki("stranger", '''"A woman from the Eagle Watch. She bought it from the girl with the tray and put it in my hands and walked off, the way soldiers do for a knight who looks hungry." {n}She turns it over.{/n} "There was a paladin in your company once, with quick hands, who was at the bed at Iz. She cried out, 'Your Majesty,' and I felt the thing in me turn its head at it." {n}Her voice drops.{/n} "She is not in Drezen now. I find I should have liked to thank her. That is the trouble with being dead, Commander. One keeps missing people."''',
        c("Continue", "end")),
    ki("stranger_absent", '''"A woman from the Eagle Watch. She bought it from the girl with the tray and put it in my hands and walked off, the way soldiers do for a knight who looks hungry." {n}She turns it over.{/n} "Kindness from strangers. I had a century of kindness from people who wanted something, Commander. This is a great deal more alarming." {n}A dry breath.{/n} "There was a paladin in your company once, with quick hands. She would have known me in a heartbeat. I find I am glad and sorry, in equal parts, that she is not here to try."''',
        c("Continue", "end")),
    ki("end", '''"Here." {n}She breaks the pie in two, with scrupulous fairness, and holds out the larger half.{/n} "A knight shares her rations with her Commander. It is in the regulations. I wrote the regulations."''',
        c("[Take the larger half.]", flags=(SEELAH_SPOKEN,)),
        c("[Take the smaller half.]", flags=(SEELAH_SPOKEN,))),
], requires=(FIRST,), forbids=(SEELAH_SPOKEN,), delay=24)


# --- 16. The blind man knows her voice (the Storyteller) ----------------------------------------------------------------------

STORYTELLER_SPOKEN = P + "kitrane.storyteller"

beat(P + "kitrane.storyteller", "A voice he knows", '"You look shaken."', [
    ki("start", '''"I went to the Storyteller's shelves. I should not have." {n}She is gripping the pommel of her sword hard enough to whiten her knuckles.{/n} "I wanted a book. The Crows' squire cannot read, and I thought I would teach her from something with pictures. I asked the old man if he had anything suitable for a girl of sixteen."''',
        c('"And?"', "and")),
    ki("and", '''"He was very still. Then he said, 'For a girl of sixteen, Your Majesty? I should think the Lays of the First Crusade. You always liked them best.'" {n}She lets out a breath.{/n} "He is blind, Commander. I had forgotten. He has never once seen my face, in any of the times he has told my story. He knows me by my voice."''',
        c("Continue", "rent", requires=(RENT,)),
        c("Continue", "said", forbids=(RENT,))),
    ki("rent", '''"Even this voice." {n}She touches her throat, where the tear catches.{/n} "I thought the rending had changed it enough. It has not. He said it was like hearing a song he knew played on a cracked bell. He said he would know it anywhere, and he was very sorry, and he would not tell."''',
        c("Continue", "said")),
    ki("said", '''"He did not ask how. He said only that he had told a great many stories that ended at Iz, and never one that ended in a market." {n}Her mouth tightens.{/n} "Then he gave me the book, and would not take my four coppers, and said that stories were the only things in the world that were allowed to change their endings, and that he had always thought mine deserved a better one." {n}A pause.{/n} "I did not know what to say to him. I have made speeches to armies. I did not know what to say to one old man."''',
        c('"He won\'t tell anyone."', "tell"),
        c('"Did you thank him?"', "thank")),
    ki("tell", '''"No. He will not." {n}Certain.{/n} "He will tell it, one day, in some tavern in Absalom, long after we are all dust, and change the names, and nobody will believe it. That is his kind of silence." {n}She loosens her grip on the sword at last.{/n} "I find I do not mind. I should like, very much, to be a story nobody believes."''',
        c("[Leave her with the book.]", flags=(STORYTELLER_SPOKEN,))),
    ki("thank", '''"I said 'thank you,' and he said, 'You are welcome, Kitrane,' as if he had known the name all his life." {n}Her eyes are suddenly bright.{/n} "That is the first time anyone has called me by it without being told to. I nearly wept on his shelves, Commander. In front of the curio-seller's cousin. I shall never be able to buy spices on that street again."''',
        c("[Leave her with the book.]", flags=(STORYTELLER_SPOKEN,))),
], requires=(FIRST,), forbids=(STORYTELLER_SPOKEN, "storyteller.dead"), delay=36)


# --- 17. The sergeant's stories (Sir Anselm, remembered) ----------------------------------------------------------------------

SERGEANT = P + "kitrane.sergeant"

beat(P + "kitrane.sergeant", "What the sergeant remembers", '"Your sergeant was telling stories last night."', [
    ki("start", '''"He always does, after the second cup. Tonight it was Sir Anselm." {n}She is sitting on an upturned crate by the stall, oiling the old sword with slow, careful strokes.{/n} "I have known the Crows six weeks, Commander, if one counts from the war camp, and forty years if one counts from when they first stood behind my chair at court. I found last night that I knew almost nothing about any of them."''',
        c('"What did he tell you?"', "told")),
    ki("told", '''"That Sir Anselm cheated at cards. Badly. That he kept a list of every demon he had killed, and lost it, and started a new one from memory, and that the second list was a good deal longer than the first." {n}Her mouth twitches.{/n} "That he used to say, whenever I rode out in front of the line, that the Queen of Mendev had the tactical sense of a charging goat, and that he said it loudly, being deaf, so that I would hear."''',
        c('"Did you?"', "heard")),
    ki("heard", '''"Every time." {n}The oil-cloth stops.{/n} "I thought he was being impertinent. I thought I was being gracious, not having him disciplined." {n}She looks down at the blade.{/n} "He was telling me to stay behind him. Every time, for forty years, in the only way a knight may tell his Queen anything. And at Iz I did not, and he stepped in front of the dragon instead, and that is how he came to be in the box."''',
        c('"It wasn\'t your fault."', "fault"),
        c('"He did what he meant to do."', "meant"),
        c("[Say nothing. Sit down beside her.]", "sit")),
    ki("fault", '''"No. It was a dragon's fault, and the Lord of Locusts', and the Worldwound's." {n}Very even.{/n} "I am a paladin, Commander. I know exactly how much blame to take and where to put it down. I have done it ten thousand times." {n}Her hands resume on the blade.{/n} "I am only finding it very hard to put this particular one down. It is shaped like a deaf old man."''',
        c("Continue", "end")),
    ki("meant", '''{n}She is silent for a while.{/n} "Yes. He did. That is the only mercy in it." {n}She holds the sword up, and turns it, and you notice the name scratched small and crooked near the hilt, under the Crows' mark.{/n} "This is his. Mine went with Kitrane, so his went on the coffin, and when the Crows brought me out I took his. I did not think about it at the time. I think about nothing else now."''',
        c("Continue", "end")),
    nar("sit", '''{n}You sit down on the next crate. She goes on oiling the sword for a long time, stroke after stroke, until the steel shines, and neither of you says anything. When she has finished she lays the blade across her knees and rests both hands on it.{/n}
{n}"Thank you," she says at last. "The Queen never had anyone who simply sat."{/n}''',
        c("Continue", "end")),
    ki("end", '''"He would have liked you, I think. He liked anyone who told me no." {n}She sheathes the sword.{/n} "Go on, Commander. The sergeant has a third cup waiting for me tonight, and I intend to hear every story he has left before he forgets them."''',
        c("[Leave her with the sword.]", flags=(SERGEANT,))),
], requires=(FIRST, COFFIN), forbids=(SERGEANT,), delay=36)


# --- 18. After the tent: the grey hair, counted ---------------------------------------------------------------------------------

GREY = P + "kitrane.grey"

beat(P + "kitrane.grey", "Counting", '"You\'re frowning at that mirror again."', [
    ki("start", '''"Three." {n}She holds out the sergeant's little steel mirror to you, accusingly.{/n} "There were three this morning. I had one a fortnight ago. At this rate I shall be white as the Storyteller by Threshold, and you will have to lead me into battle by the elbow."''',
        c('[Flirt] "I\'ll count them for you. Every one."', "count"),
        c('"Do you mind?"', "mind")),
    ki("count", '''{n}She hands you the mirror, and then, after a moment's consideration, takes it back and bends her head instead, right there beside the curio stall, so that you can part her hair with your fingers and look.{/n} "Report, Commander," she says to the cobbles, a little muffled.''',
        c('"Four."', "four"),
        c('"Three. And a very handsome ear."', "ear")),
    ki("four", '''"Four!" {n}She straightens up so fast that her hair falls in her eyes.{/n} "Four. You are a liar and a scoundrel and I shall never let you count again." {n}She is laughing.{/n} "I have been counted by treasurers and physicians and priests of the Inheritor for a hundred years, Commander, and not one of them ever made it feel like this."''',
        c("Continue", "end")),
    ki("ear", '''"Flatterer." {n}But she stays where she is, head bent, for a breath longer than she needs to, your fingers in her hair.{/n} "The Queen had a lady of the bedchamber whose only duty was to see that no one ever saw her like this. Uncombed. Going grey. Leaning on somebody in the street." {n}She straightens slowly.{/n} "I should like to give her a pension and a letter of thanks, and tell her she is no longer required."''',
        c("Continue", "end")),
    ki("mind", '''"I thought I would." {n}She considers the mirror.{/n} "I lay awake over the first one. I have not lain awake over these. I think that is your fault." {n}A sidelong look.{/n} "One does not lie awake worrying about growing old when one has somebody to grow old beside. I had not known that. It is not in any chronicle I have read."''',
        c("Continue", "end")),
    ki("end", '''{n}She tucks the mirror back into her belt.{/n} "Enough vanity. There is a war on, and I have a squire who still holds a sword like an eel knife." {n}And then, as you turn to go, lower:{/n} "Come to the tent tonight. Bring nothing. Count again."''',
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
    ki("helps", '''"I do not know." {n}Honestly.{/n} "I spent a century being a thing people prayed to before battles. It helped them. It helped Mendev. It very nearly finished me, and it never once let me be anybody." {n}She tucks the folded woodcut inside her surcoat.{/n} "Let them have her. She is better at it than I was. And she will never have to disappoint them."''',
        c("[Leave her with it.]", flags=(LIKENESS,))),
    ki("truth", '''"One day." {n}She weighs it, as she weighs everything.{/n} "And break forty soldiers' hearts, and the old man's, and every mother's with a son at the front, to tell them that the Martyr of Iz bought boots in the market with a borrowed month's wage." {n}She looks out at the crowd.{/n} "Perhaps. When the war is over, and they have less need of her. The truth can wait until it will not hurt anyone who is still fighting."''',
        c("[Leave her with it.]", flags=(LIKENESS,))),
    ki("burn", '''{n}She stares at you, and then, to your surprise, laughs.{/n} "You would, wouldn't you? Buy up every last one and burn them in the square, and call it a public service." {n}She shakes her head.{/n} "No. They paid their coppers. They are theirs. The only thing a dead queen may not do is take back what people have made of her." {n}She tucks the woodcut away.{/n} "I shall keep this one. For the jaw."''',
        c("[Leave her with it.]", flags=(LIKENESS,))),
], requires=(FIRST, HANDS), forbids=(LIKENESS,), delay=24)


# --- 20. The squire's question ---------------------------------------------------------------------------------------------------

SQUIRE_ASKED = P + "kitrane.squire_asked"

beat(P + "kitrane.squire", "The squire's question", '"Your squire looks as if she\'s been crying."', [
    ki("start", '''"She has." {n}Kitrane is watching the girl across the square, who is scouring a helmet with sand as if it had personally wronged her.{/n} "She asked me a question this morning, while I was showing her how to hold a guard. She asked it the way children ask things, all at once, without looking." {n}A breath.{/n} "She asked whether I was the Queen."''',
        c('"What did you tell her?"', "told"),
        c('"How did she guess?"', "guess")),
    ki("guess", '''"The woodcuts, she said. And the way the old Crows stand when I come into the tent, before they remember not to. And the way I said 'we' once, about Mendev, when I meant 'they'." {n}Dry.{/n} "She is sixteen and guts eels for a living, and she saw through me in three weeks. The regents of Mendev never managed it in a hundred years. I have taken on the wrong squire, Commander, or exactly the right one."''',
        c("Continue", "told")),
    ki("told", '''"I told her that the Queen of Mendev died at Iz." {n}Kitrane's voice is perfectly steady.{/n} "Which is true. I told her that I was there, and saw it, and that I have been a different woman ever since. Which is also true." {n}Her hands tighten on the pommel.{/n} "And then I told her that if she ever meets anyone who says otherwise, she is to tell them that her knight is Kitrane of the Green Crows, and that her knight does not lie to her squires." {n}A pause.{/n} "That is when she cried."''',
        c('"You told her the truth, and she heard it."', "heard"),
        c('"It\'s too heavy for a girl of sixteen."', "heavy"),
        c('"You shouldn\'t have told her anything."', "careful")),
    ki("heard", '''"She heard it." {n}Quietly.{/n} "She is a Crow now. She will carry it the way the others carry it, and she will never have to say a false word, because every word I gave her was true. Knight Tirabade taught me that, at Iz, without meaning to." {n}She watches the girl scour.{/n} "I have learned more from knights these last weeks than in a century of being served by them."''',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
    ki("heavy", '''"It is." {n}At once.{/n} "The first time they put a crown on my head, in a procession, it was too heavy as well. Everything worth carrying is." {n}She lifts her chin toward the girl.{/n} "Look at her. She is angry and frightened and scouring that helm as if she means to wear through it. She is also standing up straighter than she did yesterday. I know that look. I wore it for a year."''',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
    ki("careful", '''"Perhaps not." {n}She does not bristle; she considers it, as she considers everything.{/n} "It is a risk. You would have lied to her, I think, kindly and well, and she would never have known." {n}She turns her head and looks at you.{/n} "But I will not start a knighthood with a lie to the only person who asked me for the truth. The Queen could afford that. Kitrane cannot. She has nothing else to offer anyone."''',
        c("[Leave her watching her squire.]", flags=(SQUIRE_ASKED,))),
], requires=(FIRST, CROWS_ORDER, LIKENESS), forbids=(SQUIRE_ASKED,), delay=36)
