"""Arueshalae's early beat (pacing pass PP2; Writer/handoffs/13-PACING-PASS.md section 2, 2a and 2b).

Path-neutral (N-all): no Trickster gate, device, promise or native key. Her native romance (ArueshalaeRomance d6a90c0f)
has no state in Chapter 2, so the beat neither reads nor writes it (pacing lint H3), and it never delays her Chapter 3
romance keys: it happens in the Drezen prison, before she joins.

Host (corrected from the 13 section 2 table): that row's host, Arusha_DrezenPrison/Cue_0003 122e3e82 -> AnswersList_0033
bd4d782f, has no incoming reference anywhere in blueprints.zip (only its child Cue_0032 names it, as ParentAsset), so it is
never shown. The beat sits instead on the prison's root list, AnswersList_0006 7c789226, which every live branch of the
meeting returns to; it returns to Cue_0045 cec49de7 ("{n}Arueshalae quietly hums a few more notes.{/n}", answers that
list only; no conditions or actions: tools/retcheck.py OK), and every branch ends with her humming.

Gate: she has named Desna herself first, "Desna helped me understand how disgusting the life of a succubus is"
(Cue_0008 37899239, bound here as arueshalae.prison_desna_named); Chapter 2 only. The prison dialog exists only in
Chapter 2 (c2_vs/DrezenSiege), and the list holds no Chapter 3 meeting.

Voice anchors (enGB, hers): "You have no reason to trust me. I am a succubus, which means no matter how believable my
words are, all of them could be a sweet lie." (Cue_0010 7d59d7b3); "I only ask for one thing: let me out of this prison."
(Cue_0012 b44ff8e9); "I... wasn't the only one seeing that, was I?" (Cue_0003). Timid, exact, testing.

Canon for what is said: Desna is the goddess of freedom, travel, luck and dreams (her altar text, enGB e86daca7-af14-4338-
a00e-bc25114e2cb7); Sarenrae of healing and redemption (enGB 3564571f-2489-4952-9ace-338be4e12352); Arueshalae entered a
Desnan priestess's dying dreams (Fortress_Arusha_End/Cue_0011 57197a1b), only alluded to here; she hopes to earn Desna's
forgiveness (Fortress_Arusha_Start/Cue_0026 11a081f1); her warning failed to save Kenabres (Cue_0019 787910d8). The prayer
is the Commander's own words, not scripture.

Consequence: arueshalae_treatment's "Night reading" (Chapter 3, her first Trickster session, where the Commander is
found reading Desna's mercy) opens with what she kept of the prison talk.
"""
from story_format import c, n, scene

SCENES = []
REL = "arueshalae"
PRISON_LIST = "7c789226898962e43802ccf27dc88395"    # Arusha_DrezenPrison/AnswersList_0006 (the prison's root list)
HUMS = "cec49de78daa68e449e2b83cc664661e"           # Arusha_DrezenPrison/Cue_0045 "Arueshalae quietly hums a few more notes."
DESNA_NAMED = "arueshalae.prison_desna_named"       # Cue_0008 seen: "Desna helped me understand..."
SEEN_CUES = {DESNA_NAMED: ["37899239473b1d5489109c6155245398"]}

DESNA = "arueshalae.early.desna"
DESNA_SEEN = DESNA + ".seen"
DESNA_KEPT = DESNA + ".kept"         # the Commander made her a traveller's prayer in their own words, and she kept it
DESNA_DOUBTED = DESNA + ".doubted"   # the Commander promised Sarenrae's pardon in Desna's name, and she said so
DESNA_PLAIN = DESNA + ".plain"       # the Commander admitted knowing nothing of Desna, only that her warning failed

PATH_FIT = {DESNA: "N-all"}


def a(id, text, *choices):
    """Arueshalae inside her own native dialog: the scene owner, so the cue takes Cue_0045's speaker (her prison unit)."""
    return n(id, "Arueshalae", text, *choices)


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices)


SCENES.append(scene(DESNA, "A star and a road", "Arueshalae", 2,
    '"You said Desna helped you. Tell me about her."', [
    a("start", '''"About her?" {n}She comes to the bars, slowly, and stops a hand's breadth short of them, as though the iron might be warm.{/n} "I first saw her light in a dream I had no business being in. That's all I can tell you that's mine." {n}She hesitates.{/n} "Do you know any of her prayers? I... would like to hear one. Nobody has said one where I could hear it since they put me in here."''',
        c("[Say a prayer to Desna, as well as you can make one. Lore (Religion) DC 15.]", flags=(DESNA_SEEN,),
          check=dict(Skill="SkillLoreReligion", DC=15, Success="kept", Failure="doubted")),
        c('"I don\'t know the first thing about her. I know you tried to warn Kenabres, and it wasn\'t enough."', "plain",
          flags=(DESNA_SEEN,))),
    nar("kept", '''{n}You have no priest's words for it, so you make your own, the way travellers do at a crossroads: a star, a road, one night, and the goddess asked to watch over whoever is walking it. You don't ask her who they are, or where they have been, or what they did there.{/n}''',
        c("Continue", "kept_her")),
    a("kept_her", '''"...Yes." {n}She lets out a long breath.{/n} "That's how it felt, when she found me. Not forgiven. I haven't earned that yet; I don't know if I ever will. Just a road, and a star over it, and nobody standing in the way." {n}Her hand comes up toward the bars, and stops, and goes behind her back.{/n}
{n}She turns half away, and under her breath, very softly, she begins to hum.{/n}''',
        c("[Let her hum]", flags=(DESNA_KEPT,))),
    nar("doubted", '''{n}You tell her that Desna forgives every sinner who comes to her repenting, and you hear it go wrong as you say it: the shape of somebody else's sermon, a dawn goddess's, not a dreamer's.{/n}''',
        c("Continue", "doubted_her")),
    a("doubted_her", '''"You're kind." {n}She steps back from the bars.{/n} "I think that's the Dawnflower's promise, not hers. Desna never promised me anything. She gave me a chance, and I'm still trying to deserve it." {n}A small, tired tilt of her head.{/n} "Maybe she'll forgive me one day. I don't think anyone can say it for her."
{n}She turns her face to the wall, and after a while she begins to hum to herself, as if you had already gone.{/n}''',
        c("[Leave her to it]", flags=(DESNA_DOUBTED,))),
    a("plain", '''"No. It wasn't enough." {n}She looks at you for a long moment, as if a thing she had braced for had not come.{/n} "Thank you for not telling me it was."
{n}She sits down on the cold floor of the cell with her wings folded round her knees, and, very softly, she begins to hum.{/n}''',
        c("[Let her hum]", flags=(DESNA_PLAIN,))),
], requires=(DESNA_NAMED,), forbids=("arueshalae.closed", DESNA_SEEN, DESNA_KEPT, DESNA_DOUBTED, DESNA_PLAIN),
    last=2, Relationship=REL, Chapters=[2], AnswerLists=[PRISON_LIST], NativeReturnCue=HUMS))


def integrate(payload):
    """Register the seen-cue key this beat reads (conflict-checked)."""
    seen = payload.setdefault("SeenCues", {})
    for key, cues in SEEN_CUES.items():
        if seen.get(key, cues) != cues:
            raise ValueError("Conflicting seen-cue binding: " + key)
        seen[key] = list(cues)
