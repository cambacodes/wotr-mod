"""Authored ix-b encounters: present women disagree over native campaign outcomes.

No prior meetings, return devices, romance ladder or changes to native outcomes.
Gesmerha's bench and Aranka's existing capital placements supply the meetings;
Nenio approaches the recruited succubus in Drezen. Missing participants suppress
the encounter rather than supplying an invented report of their fate.
"""
from story_format import reaction

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"
FALLEN = "arueshalae.evil_recruited"
REPLACEMENT = ("nenio.trickster.cost.recreated", "nenio.trickster.cost.unremembered")

# Canon: BlindCarver/Cue_0039, blueprint 3d7327a78f3fdb04d9b824c9734e09ad,
# enGB d1a5d57a-4fc5-4749-b2a4-d9455fa4e0f5 (Soana's runestones).
# DLC1/Iz/SoanaMain/Cue_0010, blueprint 278c5d4e7250465e86b5c80493ffc624,
# enGB 68ee13a9-a6d6-4301-a77a-5ed173c0896b supports her forest allegiance
# only: no DLC march or membership of Wintersun is imported into this history.
# Orso: SoanaAfterQuest/Cue_0019 62d721f0-e917-4a6b-81c0-20e79c350dbf,
# Cue_0020 7ddce51e-9ccb-43f5-b693-d01b4e2eb48e; binding Abyss spirits:
# SoanaAfterBear/Cue_0026 29caf584-0542-4a19-b852-9394f1c20f16.
for truth in (False, True):
    for ruling in (False, True):
        for dead in (False, True):
            sid = "gesmerha.react.soana.%s.%s.%s" % (
                "truth" if truth else "illusions", "marhevok" if ruling else "chief", "lost" if dead else "orso")
            requires = ["trickster", "gesmerha.present_now", "soana.present_now",
                        "gesmerha.wintersun_resolved", "soana.after_quest",
                        "gesmerha.truth" if truth else "gesmerha.illusions"]
            forbids = ["gesmerha.trickster.clan_destroyed"] + ([] if truth else ["gesmerha.truth"])
            (requires if ruling else forbids).append("gesmerha.marhevok_rules")
            (requires if dead else forbids).append("soana.guardian_dead")
            deception = ('"The clan knows what the Lady was now. Your stones gave us no warning when we needed it." {n}Gesmerha says.{/n}'
                         if truth else
                         '"The clan still trusts the Lady. I asked about your stones because I could not trust that silence." {n}Gesmerha says.{/n}')
            chief = ('"Marhevok still rules us. He took my eyes, and you speak of him as though he were merely a bad hunter." {n}Gesmerha says.{/n}'
                     if ruling else
                     '"Marhevok is no longer our chief. His cruelty did not end at the edge of your woods." {n}Gesmerha says.{/n}')
            guardian = ('"Orso is dead," {n}Soana snaps.{/n} "And I must find another guardian while you argue over the old one."'
                        if dead else
                        '"Orso still guards my forest," {n}Soana snaps.{/n} "He protects me while I draw the unhappy spirits out of the animals."')
            text = '''{n}Gesmerha lays her carving knife flat on the bench. Soana brushes a curl of wood from her sleeve.{/n}
"Soana the Wise. We spoke your name whenever we spoke of the runestones. Sit down. I have a question for you." {n}Gesmerha says.{/n}
%s
"Then ask whoever silenced them. I did not put that oglin in your chief's bed." {n}Soana says.{/n}
%s
"And you think I should have abandoned the forest to fight him? The Worldwound was eating it alive. I bound an Abyss spirit to defend it." {n}Soana says.{/n}
%s
"Our hunters went into those woods," {n}Gesmerha says.{/n} "Did your protection include them?"
"It included the roots beneath their feet. Tear those out and see how long your village lasts." {n}Soana says.{/n}
{n}Gesmerha finds the knife's handle but leaves it lying down.{/n}
"Next time, tell us what walks among the trees. We have had enough of protectors who keep us ignorant." {n}Gesmerha says.{/n}
"Then teach your hunters to ask before they strike. I have had enough of those." {n}Soana says.{/n}''' % (deception, chief, guardian)
            SCENES.append(reaction("Gesmerha", sid, requires, text,
                answer_list="2063ee21356b772408f5c9cfb3ed5bd0", forbids=forbids,
                relationship="gesmerha", entry='"Soana has come to your bench?"', chapter=3, last=5,
                Chapters=[3, 5], Areas=["0a5654e7dc18f074d9356009d55eb51b"],
                ContactUnit="3ba3a0ff8575be8419159221177c1411", portrait="Gesmerha"))

# Canon: DesnaAdept2/Cue_0016, blueprint 2e756329fd5fa1c4daa7c654bf53df93,
# enGB 19fd597c-eff5-46e5-9c1b-9838060f835c; DesnaTempleFinal/Cue_0020,
# blueprint f21279d12e1c70449bd037e75d7fd4a7, enGB a4a8ff32-09b8-4296-88c5-a21126d9146b.
# Her song here is ordinary music: no drain cure, ward or forced redemption.
WELCOME = '''{n}Aranka stops tuning her lute when Arueshalae approaches. Behind them, a wagon rattles toward Drezen's gates, piled with spears.{/n}
"Another follower of Desna! I was beginning to think all the others had better sense than to come here. Do you sing?" {n}Aranka says.{/n}
"I used to sing for people I meant to hurt." {n}Arueshalae says.{/n}
{n}Aranka's fingers fall still on the strings.{/n} "That wasn't the answer I expected."
"You should know who you are inviting." {n}Arueshalae says.{/n}
"I invited you to sing. I didn't ask you to pretend. There's a difference." {n}Aranka says.{/n}
{n}Arueshalae watches the carters pass.{/n} "I want to help them. Sometimes I hear their hearts before I hear their voices."
"Then start with mine. I'll make it very loud." {n}Aranka says.{/n}
{n}Aranka strikes a chord. Arueshalae stays across from her, with the lute between them.{/n}
"No. Something quieter. They have enough shouting waiting for them outside the walls." {n}Arueshalae says.{/n}
"You're right. But if you sing as badly as you look frightened, I'm choosing the next tune." {n}Aranka says.{/n}
{n}Arueshalae laughs once, in surprise. Aranka begins again, softer; this time she waits for the second voice. Neither reaches across the instrument.{/n}'''

REFUSAL = '''{n}Aranka's song breaks off as Arueshalae leans against the wagon beside her. The succubus glances at the soldiers listening nearby.{/n}
"Keep singing. I like them with their mouths open." {n}Arueshalae says.{/n}
"They're listening to a song, not asking to be eaten." {n}Aranka says.{/n}
"Oh, a Desnan. Will you sing me back to goodness? How dreary. Can't you sing about something filthy?" {n}Arueshalae says.{/n}
{n}Aranka puts her palm over the strings.{/n} "No. And you won't use my music to draw them closer."
"How disappointing. I could give you something worth singing about." {n}Arueshalae says.{/n}
"I've seen enough demons in Kenabres to fill a songbook. You aren't getting a pretty verse because you have a pretty face." {n}Aranka says.{/n}
{n}Arueshalae's smile thins. She looks Aranka over slowly.{/n} "You would sound sweeter begging."
"And you would sound better with your mouth shut." {n}Aranka says.{/n}
{n}The carters have stopped to listen. Aranka raises her voice.{/n} "That's all for today. There's work waiting at the gates."
{n}The men lift their load of spears. Arueshalae watches them go, then gives the bard a small, contemptuous bow.{/n}
"Keep your hymn. I'll find my own supper." {n}Arueshalae says.{/n}'''

for fallen, text in ((False, WELCOME), (True, REFUSAL)):
    for yard in (False, True):
        sid = "aranka.react.arueshalae.%s%s" % ("fallen" if fallen else "dreamer", ".yard" if yard else "")
        hub = "aranka.presence.yard" if yard else "aranka.presence"
        SCENES.append(reaction("Aranka", sid,
            ("trickster", "aranka.present_now", "arueshalae.present_now", "aranka.trickster.in_drezen",
             FALLEN if fallen else "arueshalae.changed"), text,
            answer_list="7d6ad178bd7a1ef4ca737ab167570c79" if fallen else "03ebad9587cbea0438d901a0f8df44f1",
            relationship="aranka", chapter=5 if fallen else 3, last=5,
            Chapters=[5] if fallen else [3, 5], Areas=[DREZEN],
            forbids=(*(() if fallen else (FALLEN,)), *(("aranka.presence.failed",) if not yard else ())),
            RequiresAnyGroups=[["aranka.presence.failed"]] if yard else [], portrait="Aranka",
            ContactUnit="e3bc95db7e2181d41847b3a1d858258d" if fallen else "a352873d37ec6c54c9fa8f6da3a6b3e1",
            entry='"What did Arueshalae make of your song?"'))

# Canon: EvilArueshalaeNenio/Banter_EvilArueshalaeNenio_banter1_pack2,
# blueprint 02c00f71641c8a24d89fdb5a77fce468; enGB f7a10e86-6617-482b-9f28-bae38382e6bb
# and b2d584ee-068b-4b77-8b16-fb1883f483bc (predation / analytic refusal).
# banter2_pack2, blueprint b876ddfdaac36aa45be29fe1070bb5e7,
# enGB 660adf73-23ef-40c5-a8c3-a453cb64ad54 compares their forms, not an immunity.
for replacement in (False, True):
    sid = "nenio.react.fallen_arueshalae." + ("replacement" if replacement else "scholar")
    identity = ('"I have no recollection of you. State your purpose before you touch my notes." {n}Nenio says.{/n}'
                if replacement else
                '"Demon girl! I have a question about your hunting methods." {n}Nenio says.{/n}')
    text = '''{n}Nenio sets a sheet of notes before Arueshalae. From the square comes the hammering of soldiers repairing a shield.{/n}
%s
"Put those away. Look at me. Wouldn't you rather forget this tiresome war for a little while?" {n}Arueshalae says.{/n}
{n}Nenio lifts her head, then immediately begins writing.{/n}
"An appeal to fatigue, followed by an instruction to abandon the current task. Is that persuasion or hypnosis?" {n}Nenio says.{/n}
"It's an invitation, you tedious little fox." {n}Arueshalae says.{/n}
"That does not answer the question. Repeat it without the instruction. We must isolate the method." {n}Nenio says.{/n}
{n}Arueshalae catches the edge of the sheet beneath one fingernail.{/n} "I could make you forget how to write."
"Then you would destroy the only useful result of this conversation. No." {n}Nenio says.{/n}
{n}Nenio pulls the sheet free before the claw can tear it.{/n}
"The proposed experiment kills the researcher. Rejected." {n}Nenio says.{/n}
"My prey usually has more imagination." {n}Arueshalae says.{/n}
"Your prey presumably does not need to publish its findings." {n}Nenio says.{/n}
{n}Arueshalae bares her teeth. Nenio draws a line beneath the last observation and turns the sheet over.{/n}
"Now, can you attempt the same appeal without baring your teeth? You have introduced another variable." {n}Nenio says.{/n}''' % identity
    SCENES.append(reaction("Nenio", sid,
        ("trickster", "nenio.present_now", "arueshalae.present_now", FALLEN), text,
        answer_list="7d6ad178bd7a1ef4ca737ab167570c79", relationship="nenio",
        chapter=5, last=5, Areas=[DREZEN], ContactUnit="e3bc95db7e2181d41847b3a1d858258d",
        forbids=() if replacement else REPLACEMENT,
        RequiresAnyGroups=[["nenio.in_party", "nenio.trickster.visitor"],
                           *([list(REPLACEMENT)] if replacement else [])], portrait="Nenio",
        entry='"Nenio, what are you writing about Arueshalae?"'))
