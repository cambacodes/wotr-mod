"""Authored Trickster encounters: interaction gaps 1, 2, 3, 6 and 8.

These encounters stage new meetings at an earned Drezen rest. Angel-only
accounts supply characterization, never a Trickster expedition or prior meeting.
The banner supplies a voice, not Iomedae's body. No romance state is awarded.
Imported after Yaniel's scenes; append-only registration preserves old identities.
"""
from story_format import reaction
from storylines import galfrey_trickster as gf
from storylines import iomedae_trickster as io
from storylines import targona_trickster as tg
from storylines import yaniel_trickster as yn

SCENES = []


def encounter(owner, suffix, title, text, women, requires=(), forbids=()):
    route = owner.lower()
    sid = route + ".trickster.react.ix_a." + suffix
    gates = ["trickster", *(woman + ".present_now" for woman in women), *requires]
    channel = {}
    if "Iomedae" == owner:
        # Her first spoken dream is not the banner appointment. Reuse the
        # existing earned appointment and both existing banner channels.
        gates += ["iomedae.reachable_by_letter", io.SPOKEN, io.CALLED]
        channel = dict(RequiresAny=[io.BANNER_HELD, io.ORDER_BANNER])
    SCENES.append(reaction(
        owner, sid, gates, text, remote=True, relationship=route,
        title=title, chapter=5, last=5, portrait=owner,
        forbids=(route + ".closed", *forbids),
        Areas=[yn.DREZEN], Chapters=[5], Kind="sending" if owner == "Iomedae" else "visit",
        **channel))
    if route != "targona":
        {"iomedae": io, "yaniel": yn}[route].tag(sid)


# Gap 1: c4/Mythic_Angel/Yaniel/Cue_0010.jbp,
# enGB 79a38d96-86dc-496d-88ae-6cdae0dfc14a: their meeting occurs AFTER rescue.
# Cue_0011.jbp / 53562448-9d48-4f7a-aae5-206ac80f02ee supports kindred
# altered powers; do not import the Angel Abyss expedition or Holy Warden status.
encounter("Targona", "yaniel", "Two survivors", '''{n}Yaniel has brought a wounded sentry down from the wall. Targona kneels beside his pallet in the supply yard. When she opens her wings to make room, Yaniel stops looking at the bandage.{/n}
"Areelu?" {n}Yaniel asks.{/n}
"Yes," {n}Targona answers. Her dark wing draws closer to her back.{/n}
"Minagho had me. Areelu gave me to her." {n}Yaniel holds out the clean linen.{/n} "Here. He's bleeding through that."
{n}Targona takes it. Between them they lift the sentry's shoulder without disturbing the broken arm.{/n} "You are Yaniel. They told me someone had come out of the Fane alive."
"One. Don't let them make it sound like a victory."
"One is still worth saving. I am glad you are here," {n}Targona says.{/n}
"Then help me get him back on his feet. The east wall needs men." {n}Yaniel points to the tower.{/n}
"His arm needs time. So do you." {n}Targona keeps her hand beneath the broken arm.{/n}
{n}Yaniel's jaw tightens.{/n} "I have had enough time lying helpless."
"And I have seen enough wounded sent back before they could hold a weapon." {n}Targona ties off the bandage.{/n} "He stays here tonight. You can take his watch."
{n}Yaniel looks at the sleeping man, then takes up his cloak.{/n} "That was what I came to offer."''',
          ["targona", "yaniel"], requires=(tg.IN_DREZEN, yn.RETURNED))


# Gap 2: NPC_Common/Galfrey_Incognito/Cue_0010.jbp (the audit's c3 alias
# resolves here), enGB 13e07068-5a48-4cb6-903a-d6b75c94ffdf: the church
# paid for the elixirs and chose its ruler. Her future remains HER decision.
QUEEN_BANNER = '''{n}Galfrey brings a campaign map to the platform. The raised banner stirs above her; the voice comes from its cloth.{/n}
"Galfrey. What will you do when this war ends?" {n}It is Iomedae's voice.{/n}
'''
BANNER_END = '''
"Mendev will still have wounded soldiers and enemies across its borders," {n}says Iomedae.{/n} "Your decision does not send them away."
"I know their numbers. I have been signing their orders longer than most of their fathers lived. I shall make provision for them," {n}Galfrey answers.{/n}
"You must answer for what you leave in other hands," {n}Iomedae says.{/n}
{n}Galfrey flattens a curled corner of the map.{/n} "Then ask me about those hands. I will name them. But the church must hear my answer about the elixir from me."
{n}The cloth pulls taut.{/n} "It shall. Show me the border."
{n}Galfrey moves a marker toward the Wound. Her finger stays on it while she describes the exposed road.{/n}'''
encounter("Iomedae", "galfrey.queen", "The ruler's answer", QUEEN_BANNER + '''"Return to my throne. The war has not relieved me of my crown." {n}Galfrey lays down her dispatches.{/n}
"Will you answer for your orders at Iz?" {n}Iomedae asks.{/n}
"Yes. I shall answer for them as Queen. I will not ask a regent to bear them while I take the credit for victory." {n}Galfrey holds the papers flat against the wind.{/n}''' + BANNER_END,
          ["galfrey"], requires=(gf.FINAL,), forbids=(gf.RETURNED,))
encounter("Iomedae", "galfrey.crown", "The ruler's answer", QUEEN_BANNER + '''"Return to Mendev and reclaim the crown. I chose the coffin at Iz. I must explain that choice before the court," {n}Galfrey says.{/n}
"You could send an account," {n}Iomedae replies.{/n}
"An account cannot stand before the people I left to govern over my grave. I can. They may refuse me. I shall go nevertheless." {n}Galfrey sets her gloves on the dispatches.{/n}''' + BANNER_END,
          ["galfrey"], requires=(gf.RETURNED, gf.CROWN))
encounter("Iomedae", "galfrey.kitrane", "The knight's answer", QUEEN_BANNER + '''"Remain Kitrane. Grow old. The Green Crows have work enough for a knight who knows the border." {n}Galfrey touches the birds on her surcoat.{/n}
"The church chose you to rule," {n}Iomedae says.{/n}
"And I accepted. I am choosing now. I shall tell Mendev what I did at Iz, but I shall not swallow another elixir merely because the priests fear choosing someone else," {n}Galfrey answers.{/n}''' + BANNER_END,
          ["galfrey"], requires=(gf.RETURNED, gf.FOREVER), forbids=(gf.CROWN,))


# Gap 3: c3/AreeluLaboratory/TargonaWings/Cue_0007.jbp,
# enGB e23336cc-e4f9-4ac7-867c-7e0ede541063: blade of the Heavenly Host.
# c3/Drezen_C3/Herald/Cue_0109.jbp / 15ed4f5e-b942-47ac-bf5c-418488490187:
# shame over the demonic wing, not loss of faith or a cure promised by Iomedae.
encounter("Iomedae", "targona", "The blade before the banner", '''{n}Targona stands below the raised banner. She has folded the dark wing tightly enough that its claws scrape the stone. The voice in the banner speaks her name.{/n}
"My lady. I have come to report." {n}Targona bows her head.{/n}
"Then report," {n}Iomedae says.{/n}
"There are wounded behind the stores. I can heal some. Others need hands, clean water, a place out of the wind. I have stayed with them," {n}Targona answers.{/n}
"And the wing?" {n}Iomedae asks.{/n}
{n}Targona lowers her eyes.{/n} "Still Areelu's work. It has not fallen away with prayer. I would not bring it among the Host unexamined."
"You would keep it from my sight?" {n}Iomedae's voice sharpens.{/n}
"No." {n}She opens it. The black feathers lift in the wind off the Wound.{/n} "But I will not call it harmless because I wish to stand beside you."
"I have asked for your report, Targona. You have given it. What duty do you ask?" {n}Iomedae waits for her answer.{/n}
"The wounded. Until they can travel, or fight, or be buried," {n}Targona says.{/n}
"Attend to them. Send word of any change in the wing," {n}Iomedae commands.{/n}
{n}Targona bows. She studies the dark feathers before folding them again; the claws leave fresh marks beside her feet.{/n} "I will, my lady. All of it."''',
          ["targona"], requires=(tg.IN_DREZEN,))


# Gap 6: c3/MidnightFane/TrueYaniel/Cue_0002.jbp,
# enGB a934c33c-3785-48b1-999c-74225ec05fa0: paladin, rage at the husks' deaths.
# c4/Mythic_Angel/Yaniel/Cue_0018.jbp / 2c71bb86-0c66-4151-8cf5-2688e7c4050e:
# she challenged crusade leaders; no earlier personal divine audience is claimed.
encounter("Iomedae", "yaniel", "An oath still standing", '''{n}Yaniel climbs to the banner with mud on her boots and a nick in her borrowed sword. When the cloth speaks, she reaches for the parapet instead of kneeling.{/n}
"Yaniel. You have kept your oath." {n}Iomedae's voice carries above the wind.{/n}
"I kept it in the Fane. It did not get the others out," {n}Yaniel answers.{/n}
"You remember them," {n}Iomedae says.{/n}
"I remember what was left of them. I want the next patrol to find the pits before the demons empty them. The officers want another day to count spears." {n}Yaniel looks toward the Wound.{/n}
"Will you go alone?" {n}Iomedae asks.{/n}
{n}Yaniel's fingers tighten on the stone.{/n} "I tried that once. No. But I shall argue until they give me men."
"Argue for men you can bring back. They have sworn service too," {n}Iomedae says.{/n}
"Then let them serve. I am tired of hearing priests praise courage while captives rot within marching distance." {n}Yaniel strikes the parapet with her palm.{/n}
"Do you accuse every priest?" {n}Iomedae asks.{/n}
"The ones who do it. They can stop, and I shall stop accusing them," {n}Yaniel replies.{/n}
{n}For a moment only the halyard knocks against the pole.{/n}
"Bring your officers the ground you know," {n}says Iomedae.{/n} "I will hear their prayers. You must hear their objections."
"Hear them, yes. Agree with them? We shall see." {n}Yaniel takes up her sword.{/n}''',
          ["yaniel"], requires=(yn.RETURNED,))


# Gap 8: c4/Mythic_Angel/Yaniel/Cue_0007.jbp,
# enGB 3d3ca397-a798-455f-8daf-11d7e0663237: the neglected rescued veteran.
# This is a NEW troop encounter, not that history's Angel mission announcement.
VETERAN = '''{n}A recruit outside the citadel recognizes Yaniel's name and asks whether she will stand before his company. Galfrey hears him out. Yaniel does not.{/n}
"If they need someone to hold a sword over her head, fetch the statue," {n}Yaniel says.{/n}
"They have lost men," {n}Galfrey says.{/n} "They want to see someone who survived."
"Then show them the wounded. There are plenty." {n}Yaniel points toward the supply yard.{/n}
"That is not what he asked," {n}Galfrey answers.{/n}
"I heard him. I will inspect their watch. I will tell them where demons got through Drezen's walls. I will not tell them captivity made me holy," {n}Yaniel says.{/n}
'''
VETERAN_END = '''
{n}Yaniel looks back at the recruit.{/n} "Bring your sergeant. And the men who are actually standing watch tonight."
"The whole company wished to hear you," {n}Galfrey says.{/n}
"Then the whole company can learn where to put a sentry."
{n}The recruit salutes and runs to fetch his sergeant. Galfrey studies the nicked blade at Yaniel's belt; Yaniel turns it so the damaged edge catches the light.{/n} "They can sharpen this while we talk."'''
encounter("Yaniel", "galfrey.queen", "The veteran and the company", VETERAN + '''"As Queen, I could order you to the muster," {n}Galfrey says.{/n}
"You could. And have a fine public argument before your frightened men." {n}Yaniel folds her arms.{/n}
{n}Galfrey's mouth tightens.{/n} "The watch inspection, then. I shall tell their captain what you have offered. He can dispense with the ceremony."''' + VETERAN_END,
          ["yaniel", "galfrey"], requires=(yn.RETURNED, gf.FINAL), forbids=(gf.RETURNED,))
encounter("Yaniel", "galfrey.crown", "The veteran and the company", VETERAN + '''"When I return to Mendev, I shall have to stand before people who believed me dead," {n}Galfrey says.{/n}
"Answer their questions. Don't take me along to improve the spectacle." {n}Yaniel's eyes narrow.{/n}
"I did not ask you to come," {n}Galfrey replies.{/n}
"Good. I have had enough ceremonies in my name." {n}Yaniel turns back to the recruit.{/n}''' + VETERAN_END,
          ["yaniel", "galfrey"], requires=(yn.RETURNED, gf.RETURNED, gf.CROWN))
encounter("Yaniel", "galfrey.kitrane", "The veteran and the company", VETERAN + '''"The Crows could use that lesson," {n}Galfrey says.{/n} "I can ask their sergeant. I cannot order this company to attend."
"Kitrane, is it? Then attend with the other knights," {n}Yaniel says.{/n}
"I know something of Drezen's walls myself," {n}Galfrey replies.{/n}
"Then contradict me when I get something wrong. They'll learn more from that than from cheering." {n}Yaniel beckons to the recruit.{/n}''' + VETERAN_END,
          ["yaniel", "galfrey"], requires=(yn.RETURNED, gf.RETURNED), forbids=(gf.CROWN,))

yn.SCENES.extend(SCENES)
