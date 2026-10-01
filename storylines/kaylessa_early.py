"""Kaylessa's early beats (pacing pass PP2; Writer/handoffs/13-PACING-PASS.md section 2, 2a and 2b).

Path-neutral (N-all): no Trickster gate, device, promise or native key. Off the Trickster she still dies at the Chapter 3
reveal on every path (14-PATH-FIT: a pre-death Chapter 1-3 thread only); these beats are that thread. Each sets
`kaylessa.early.<beat>.seen` on its first choice and exactly one outcome flag on every terminal path.

Both sit on her root list, Kaylessa_main/AnswersList_0002 30fa5be3, and return to Cue_0070 c3ac44c6 ("{n}The elf nods
stiffly.{/n}", answers that list only; no conditions or actions: tools/retcheck.py OK). The list is shared by her two
native meetings, so each beat is pinned to its chapter: Kenabres is Chapter 1, the war camp (KaylessaDisguised a1569a07)
Chapter 2.

- Chapter 1, Kenabres: "The elf hunched up next to you is clutching a small, but deep, puncture wound." (Kaylessa_main/
  Cue_0001 2d7d6df4); to a healer's offer: "Don't. I can handle it myself. I don't like it when strangers cast spells on
  me." (Cue_0066 0ab8f1a1); healed anyway: "the next person who uses magic on me without my permission gets an arrow"
  (Cue_0071 b046d877, after Answer_0068 9f98ffa7, bound as kaylessa.healed_by_force). The beat is the binding without a
  spell; a wound already closed by force closes it. Field dressing is Lore (Nature), as native Forn_Ambush/Check_0014
  (assessing Forn's wound).
- Chapter 2, the war camp, after she has said who she hunts ("To find someone. His masters want me dead", Cue_0040
  1988bcd8; or "I'm looking for an outsider here", Cue_0053 1a44532f; bound here as kaylessa.camp_hunt_told): how she
  will know the hunter. Her warning is general (authored); canon shows the ruse only in Chapter 3: "His wound is just for show... His goal is to lure you in so
  his cronies can attack you." (Forn_Ambush/Cue_0058 15268637); "his injured leg was nothing more than a ruse" (Cue_0025
  bceafa08). Here she says it first, as her own warning, and tests whether the Commander can see a false limp.

Voice anchors (enGB, hers): "Everyone's a soldier in a war, generals and privates alike." (Cue_0073 425898fa); "I am no
lamb to the slaughter" (Cue_0040 1988bcd8); "There's no point in you knowing, soldier." (Cue_0004 e5d64e54). Clipped,
suspicious, a soldier's report rather than a confession.

Consequences (her merged route, Trickster): kaylessa_wasps "Hands" offers the Commander a line about the Kenabres binding
(appended choice); the Chapter 5 hunter's visit (kaylessa_trickster alive.hunter) offers her lesson against the bandage:
no roll if the Commander read the cook-fire limp, an easier one if they missed it.
"""
from story_format import c, n, scene
from storylines.kaylessa_trickster import CLOSED, DEAD, HEALED, REL, SCENES

MAIN_LIST = "30fa5be33ddd7b144963473692af6942"   # Kaylessa_main/AnswersList_0002 (her root list, Kenabres and war camp)
NODS = "c3ac44c65a5183e4f89fd2990a5fc58c"        # Kaylessa_main/Cue_0070 "{n}The elf nods stiffly.{/n}"

REFUSED_SPELL = "kaylessa.refused_spell"          # Kaylessa_main/Cue_0066 seen ("I don't like it when strangers cast spells on me")
HUNT_TOLD = "kaylessa.camp_hunt_told"             # Cue_0040 or Cue_0053 seen: in the war camp she said she hunts someone
SEEN_CUES = {REFUSED_SPELL: ["0ab8f1a13d91d9e4d8ac8870ca4e576d"],
             HUNT_TOLD: ["1988bcd88fe35424ebf4371eec3f96c5", "1a44532f0f3f8a849b8c5284fd19ed40"]}

DRESSED = "kaylessa.early.dressed"
DRESSED_SEEN = DRESSED + ".seen"
DRESSED_BOUND = DRESSED + ".bound"     # the Commander's knot held, and she watched the Commander's hands do it
DRESSED_LIED = DRESSED + ".lied"       # the knot slipped; she tied it herself and lied about why no spells
DRESSED_WAVED = DRESSED + ".waved"     # the Commander left it to her
TELLS = "kaylessa.early.tells"
TELLS_SEEN = TELLS + ".seen"
TELLS_READ = TELLS + ".read"           # the Commander saw the false limp at the cook-fire
TELLS_MISSED = TELLS + ".missed"       # the Commander named the wrong leg; she named the right one
TELLS_REFUSED = TELLS + ".refused"     # the Commander would not play her game

PATH_FIT = {DRESSED: "N-all", TELLS: "N-all"}


def kay(id, text, *choices):
    """Kaylessa inside her own native dialog (she is its conversant in both meetings)."""
    return n(id, "conversant", text, *choices)


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices)


# --- Chapter 1, Kenabres: the wound, bound by hand. ------------------------------------------------------------------------

SCENES.append(scene(DRESSED, "No spells", "Kaylessa", 1, '[Look at the wound] "That needs binding."', [
    nar("open", '''{n}The puncture is under her ribs on the left, small and deep, the kind a narrow blade leaves. She has packed it with a wad of her own cloak, and the cloak is soaked through.{/n}''',
        c("Continue", "refused", requires=(REFUSED_SPELL,), flags=(DRESSED_SEEN,)),
        c("Continue", "fresh", forbids=(REFUSED_SPELL,), flags=(DRESSED_SEEN,))),
    kay("refused", '''"I told you. No spells." {n}She shifts her weight off the wound and hisses through her teeth.{/n} "You deaf, soldier, or just stubborn?"''',
        c('"Linen, then. No magic in it. Just my hands."', "offer"),
        c('"Suit yourself. It\'s your side."', "waved")),
    kay("fresh", '''"It needs a priest, and I don't want one." {n}She shifts her weight off the wound and hisses through her teeth.{/n} "Don't you dare start chanting at me, soldier."''',
        c('"Linen, then. No magic in it. Just my hands."', "offer"),
        c('"Suit yourself. It\'s your side."', "waved")),
    kay("offer", '''{n}She looks at your hands for a long moment, as if they might be hiding something up the sleeve.{/n} "Just hands." {n}She takes the wad of cloak away from the wound.{/n} "Fine. Quickly. And if you're going to faint, do it now, not halfway through."''',
        c("[Clean it, pack it and bind it tight. Lore (Nature) DC 16.]",
          check=dict(Skill="SkillLoreNature", DC=16, Success="bound", Failure="slipped"))),
    kay("bound", '''{n}It is a soldier's dressing, nothing more: clean water from your flask, a pad of clean linen, a long strip wound twice round her ribs and knotted where she can reach it. She watches your hands the whole time, the way a hawk watches the glove, and never once looks at your face.{/n}
"Not bad." {n}She tests the knot with two fingers.{/n} "Your hands don't lie, soldier. That's rarer than you'd think." {n}She pulls the torn cloak back over it.{/n} "Don't make anything of it."''',
        c("[Let her be]", flags=(DRESSED_BOUND,))),
    kay("slipped", '''{n}The strip of linen is too short and her ribs are slick with blood, and your knot slides loose the moment she breathes.{/n} "Give it here." {n}She takes the linen out of your hands, holds one end in her teeth and ties it off one-handed, fast, the way somebody does who has done it in the dark before.{/n}
{n}When you ask her why not a spell, she answers without a flicker:{/n} "My mother's people keep the old ways. A stranger's prayer on the body is a sin to them, and I'm the last of them who cares." {n}It is a good lie, smoothly told. You are almost sure it is one.{/n}''',
        c("[Let her keep it]", flags=(DRESSED_LIED,))),
    kay("waved", '''"Finally. A soldier with sense." {n}She presses the wad of cloak back against the wound and leans her head against the wall, eyes half shut, watching you through her lashes in case you change your mind.{/n} "I've walked further on worse."''',
        c("[Leave it to her]", flags=(DRESSED_WAVED,))),
], forbids=(CLOSED, DEAD, HEALED, DRESSED_SEEN, DRESSED_BOUND, DRESSED_LIED, DRESSED_WAVED), last=1, Relationship=REL,
    Chapters=[1], AnswerLists=[MAIN_LIST], NativeReturnCue=NODS))


# --- Chapter 2, the war camp: how she will know the hunter. -----------------------------------------------------------------

SCENES.append(scene(TELLS, "The hunter's limp", "Kaylessa", 2,
    '"The man you\'re hunting. In a camp this size, how will you know him?"', [
    kay("start", '''"By how he moves." {n}It comes out flat, like a line from a report.{/n} "A hunter who wants you to come to him gives you a reason to. A bandage. A limp. A sad face by the side of the road. Anyone who stops to help is the one he wanted." {n}She glances at the cook-fires.{/n} "A bandage can be bait. Watch a man when he thinks nobody's looking. You're a soldier. Can you tell a wound from a lie?"''',
        c('"Show me."', "test", flags=(TELLS_SEEN,)),
        c('"I don\'t play games with spies."', "refused", flags=(TELLS_SEEN,))),
    kay("test", '''{n}She tips her chin, without looking, at a sergeant limping away from the cook-fire with a ladle in his fist and a quartermaster shouting after him.{/n} "That one. Which leg, and is it hurt?"''',
        c("[Watch him walk. Perception DC 15.]", check=dict(Skill="SkillPerception", DC=15, Success="read", Failure="missed"))),
    kay("read", '''{n}It is the left, and it is not hurt. He favours it while the quartermaster is shouting, and forgets it entirely the moment he is round the tent, where he walks off quite briskly toward the latrine detail he was meant to be digging.{/n}
"Good." {n}She sounds almost disappointed.{/n} "You'd last a week in Kyonin, soldier. Maybe two." {n}She pulls her shawl back up over her mouth.{/n} "Remember it. The arm, the leg, whatever he's bandaged. Watch it when he forgets it."''',
        c("[Remember it]", flags=(TELLS_READ,))),
    kay("missed", '''"The right?" {n}She actually laughs, once, through her nose.{/n} "It's the left, and it isn't hurt. Watch him round the tent." {n}He forgets the limp entirely the moment the quartermaster is out of sight, and walks off quite briskly toward the latrine detail he was meant to be digging.{/n}
"You'd be dead, soldier. That's how it goes: you'd walk up to help, and he'd stand up." {n}She pulls her shawl back up over her mouth.{/n} "Remember it anyway. Watch the bandage when he forgets it."''',
        c("[Remember it]", flags=(TELLS_MISSED,))),
    kay("refused", '''"Spies." {n}She tastes the word and doesn't like it.{/n} "I'm not here for your camp, soldier. I'm here for one man. When he finds me, you won't have to wonder which of us was the spy." {n}She turns her face away.{/n}''',
        c("[Leave it there]", flags=(TELLS_REFUSED,))),
], requires=(HUNT_TOLD,), forbids=(CLOSED, DEAD, TELLS_SEEN, TELLS_READ, TELLS_MISSED, TELLS_REFUSED), last=2,
    Relationship=REL, Chapters=[2], AnswerLists=[MAIN_LIST], NativeReturnCue=NODS))


def integrate(payload):
    """Register the two seen-cue keys these beats read (conflict-checked)."""
    seen = payload.setdefault("SeenCues", {})
    for key, cues in SEEN_CUES.items():
        if seen.get(key, cues) != cues:
            raise ValueError("Conflicting seen-cue binding: " + key)
        seen[key] = list(cues)
