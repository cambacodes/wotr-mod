"""Camellia: cloud voice-owner pass (villain-route-camellia, design-first).

Applied last, after every route, harem row, Last Call partner, engine appender and the Areelu layer
(expansion._make_expansion), so the paragraphs it appends never shift an index another pass registers. Text and
flag-gated paragraphs only: no scene, node or choice id, choice position, Next, Set, gate, check, cost or GuidFor
changes. Every target must resolve against the reviewed text, or the build fails. Review and machine truth table:
tools/route_packs/redesign/camellia/cloud-review.md, truth-table.json.

Structure fixed here (read-only consumers of flags the route already sets, and producer text that states what its
flags mean):
  * epilogue.refused told a Camellia the Commander had raised from the coffin and then walked away from (eng8.price
    "Leave her", performance "Stay dead", the burned letter) that "Her death stood"; the paragraph now holds for the
    register and the raised history has its own reader;
  * promises with no reader: kills_answered "Once" (oath_loophole) and "Touch her again" (oath_threatened), the Abyss
    night the Commander talked her quiet (masks.quieted); the household lovers (Arueshalae, Vellexia), Seelah's kept
    confession and Soana's unanswered claim never reached her epilogues;
  * kills summarised as paperwork: the witness "slipped on the wet steps" in a report two days later, the prisoner
    "died in his chains" in the chaplain's record, the refusal epilogue's "sent the Commander the report"; each is
    now on screen or one beat off with the body attached;
  * stale cross-variant staging: the living and camp witness (Radan, a tavern by the river) was visited "at the
    infirmary door" and given a veiled Nerosyan double the living Camellia never had; "that face in the chapel" in
    every variant; the witness's account kept "her veil" on the living page;
  * the Kaylessa pair sold a "merchant's description" to a buyer of "observations" (CHARACTER-TRUTH 2): the carrier is
    now her fetcher and dies in the tannery lane for following the wrong elf;
  * invented appetite: "I would simply have eaten her" (Nurah reactions); she kills, she does not eat;
  * [PROSE PENDING] voiced: household.pair.seelah_camellia (settle, retry), camellia_arueshalae (inspection x6,
    company), nenio_camellia (settle, retry).

Canon used (writer knowledge/characters/camellia/native-lines.json): 744a8ca4 (hissing whisper), e8969812 (the
gravel voice), 13fff43a (looks in the eyes of those she kills), 4b3e16df, 068b5a5c, 99bf4ab1 (the knife in the bed),
1e718920 and 895ef55d (Seelah), b0cec021 and b4b76d52 (class contempt), 871ccb20 (the chicken's name), 363f363e
(privacy with the poor elf), d135c54d and 4bcc01be (flush and lip-licking), fa214b1b (the stiletto held in).
No new lore: no Mireya voice, no teacher's name, no blood-drinking, no cure.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, overlay_node, record
from story_format import p

P = "camellia.trickster."
VARIANTS = ("", "_alive", "_camp")
PENDING = "[PROSE PENDING"

TEXT = {}        # (scene, node) -> (substring the reviewed text contains, new text)
PLACEHOLDER = {}  # (scene, node) -> new text for a [PROSE PENDING] node
CHOICE = {}      # (scene, node, index) -> (substring the reviewed choice contains, new text)
PARA = {}        # (scene, node, index) -> (substring the reviewed paragraph contains, new text)
ADD = {}         # (scene, node) -> paragraphs appended after every existing paragraph


def text(scene, node, expect, body):
    TEXT[(scene, node)] = (expect, body.strip())


def pending(scene, node, body):
    PLACEHOLDER[(scene, node)] = body.strip()


def choice(scene, node, index, expect, body):
    CHOICE[(scene, node, index)] = (expect, body.strip())


def para(scene, node, index, expect, body):
    PARA[(scene, node, index)] = (expect, body.strip())


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


def when(flags, body, forbids=()):
    flags = (flags,) if isinstance(flags, str) else tuple(flags)
    return p(body, requires=flags, forbids=forbids)


# ---------------------------------------------------------------------------------------------------------------------
# bond.witness: "Do it your way" was a report two days later. The push is on screen, the Commander holds the lantern.
# The living and camp witness is Radan, in a tavern by the river (alive_w / dead_w); only the dead-route witness is
# Lethra in the infirmary (killed_w). Each variant's other branches now match its own witness.
# ---------------------------------------------------------------------------------------------------------------------
HERS_TAIL = '''{n}The steps are very steep there. Camellia stands at the edge and watches the whole fall, and the stillness at the bottom, with her lips parted, and she does not look away until the rain has begun to move the hair on the body's face. When she turns back to you her cheeks are flushed and her breath comes short and quick.{/n}
"There," {n}she says, in that low, rough voice that is not her drawing-room one.{/n} "Tomorrow everyone will agree it was a terrible accident."
{n}At dinner the next night she wears a new dress and is charming to everyone, and she does not look at you once until the dessert, and then she does not stop.{/n}'''

text(P + "bond.witness", "hers", "the report says the witness slipped", '''"Thank you." {n}She says it as sincerely as she has ever said anything, and takes your arm.{/n} "Come with me, then, and carry the lantern. I want you to see how tidy I am."
{n}Two nights later Lethra leaves the infirmary against the physicians' advice, to light a candle at the chapel for the dead woman she saw. Camellia waits for her at the head of the river steps in the rain, veiled, and you stand three paces back with the hooded lantern. The candle-seller sees the lace first. Then Camellia lifts it for her, so that there can be no mistake, and steps in as close as a friend, and lays one gloved hand flat on the woman's breastbone.{/n}
"Lady Gwerm," {n}Lethra whispers.{/n}
"Yes," {n}Camellia says kindly, and pushes.{/n}
{n}The steps are very steep there. Camellia stands at the edge and watches the whole fall, and the stillness at the bottom, with her lips parted, and she does not look away until the rain has begun to move the hair on the body's face. When she turns back to you her cheeks are flushed and her breath comes short and quick.{/n}
"There," {n}she says, in that low, rough voice that is not her drawing-room one.{/n} "Tomorrow everyone will agree it was a terrible accident."
{n}At dinner the next night she wears a new dress and is charming to everyone, and she does not look at you once until the dessert, and then she does not stop.{/n}
{n}The dress is the colour of dark wine, cut to come off in one pull, and she is charming to everyone in it. She makes the table weep with laughter over a cousin's wedding, and not once through the soup or the fish does she look at you, though under the cloth her ankle finds yours and rests there, warm and deliberate. At the dessert she looks up. Her tongue passes slowly over her lower lip. Her colour is as high as it was on the steps in the rain, her breath has the same short, quick edge, and her foot slides up the inside of your calf while she tells the table a perfectly ordinary joke.{/n}
"You are very quiet tonight, my friend," {n}she says across the candles, in the voice that is not hers, and under it, low enough that only you can hear, the other one, the gravel.{/n} "I think you are thinking about the steps. Don't stop."''')
for suffix in ("_alive", "_camp"):
    text(P + "bond.witness" + suffix, "hers", "the report says the witness slipped", '''
"Thank you." {n}She says it as sincerely as she has ever said anything, and takes your arm.{/n} "Come with me, then, and carry the lantern. I want you to see how tidy I am."
{n}Radan drinks at the tavern by the river until the shutters go up, and then he goes home the short way, down the river steps. Camellia is waiting for him halfway down, in the rain, and you stand above her with the hooded lantern. He sees her face, the memorable one, and starts to tell her that he never said a word to anyone, not a word, my lady. She lets him get almost to the end of the sentence. Then she steps in as close as a friend, lays one gloved hand flat on his chest, and pushes.{/n}
''' + HERS_TAIL.replace("it was a terrible accident", "he had been drinking"))

text(P + "bond.witness", "lied", "You visit the witness at the infirmary door", '''
{n}You visit Lethra at the infirmary door. She tells it again, angrily, when you ask whether she might have mistaken the woman: the face, the laugh, the way the young lady used to pick through her father's candles as if they might bite. You let her finish. Then you ask Fye to introduce his veiled Nerosyan customer to the watch, by the name the widow has chosen. Lethra is free to repeat her story; the watch now has two women to ask about. She leaves the infirmary that afternoon and will not let your escort walk her home. From the end of Fye's bar, Camellia watches her pass the window.{/n}''')
for suffix in ("_alive", "_camp"):
    text(P + "bond.witness" + suffix, "lied", "You visit the witness at the infirmary door", '''
{n}You find Radan at the tavern by the river and let him tell it again, louder, while you pay for the round: the alley behind the tannery, the lady with her sleeves rolled up. You let him finish. Then you tell the watch sergeant at the next table, as if it hardly mattered, about a veiled Nerosyan widow who drinks alone at Fye's and was asking that week for the tannery lane. There is no such widow. Radan is free to repeat his story; the watch now has two ladies to ask about, and only one of them can be found. He goes home without your escort, the long way, not by the river steps. Camellia watches him from the tavern door.{/n}''')

text(P + "bond.witness", "r2.public", "The witness gives their name to the watch", '''
{n}Lethra gives her name to the watch and tells it exactly as she saw it, before the whole tavern, while the muster drum is still beating outside. A soldier tries to add a bloody knife; she corrects him. She saw no knife, only a face. When the watch offers her an escort home, she takes it. Camellia stands by the door the whole time, and smiles at her as she passes.{/n}''')
for suffix in ("_alive", "_camp"):
    text(P + "bond.witness" + suffix, "r2.public", "The witness gives their name to the watch", '''
{n}Radan gives his name to the watch and tells it exactly as he saw it, before the whole tavern, while the muster drum is still beating outside. A soldier tries to add a bloody knife; he corrects him. He saw no knife, only a lady's face and her sleeves rolled up. When the watch offers him an escort home, he takes it, and does not look at the door. Camellia stands by it the whole time, and smiles at him as he passes.{/n}''')

for suffix in VARIANTS:
    text(P + "bond.not_today" + suffix, "ghost", "That face in the chapel", '''
"Your witness is still talking. My face, my sleeves, my laugh: the story grows a little every time it is told, like a child." {n}Her nail scrapes the window frame.{/n} "And Fye has started looking at my hands when I laugh. You have made my evenings very inconvenient, and I have let you. I wonder why."''')

# ---------------------------------------------------------------------------------------------------------------------
# evening.the_prisoner "He's yours": the chaplain's record was the whole kill. The Commander leaves; the stair does not.
# The guards' "failure of the heart" and the laugh stay, because epilogue.kept P13 quotes them.
# ---------------------------------------------------------------------------------------------------------------------
for suffix in VARIANTS:
    text(P + "evening.the_prisoner" + suffix, "yes", "the chaplain records", '''
"Thank you." {n}She says it quite simply, the way one thanks a friend for passing the salt. She takes a small, clean knife from her sleeve.{/n} "You should go now, my friend. Or stay. It's up to you. I know it isn't pretty."
{n}You leave. You are on the fourth step when she begins to talk to him, softly, pleasantly, as if she were telling him a bedtime story, and on the ninth when he begins to scream. The guards on the stair do not look at you. He screams for a long time. Then he laughs, once, high and wrong, and after that there is only her voice, still talking, and then not even that.{/n}
{n}In the morning two guards carry him up under a blanket that is too short. One wound shows where it ends, very neat, just under the breastbone, and the face above the blanket is still looking at something. The chaplain writes "failure of the heart" and asks nobody anything. Camellia comes to breakfast with her hands scrubbed pink and eats everything on her plate.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# returned.terms: the Abyss night the Commander talked or held the flies quiet (masks.quieted) had no reader.
# ---------------------------------------------------------------------------------------------------------------------
for suffix in VARIANTS:
    add(P + "returned.terms" + suffix, "flies", when(P + "masks.quieted", '''
{n}She taps her temple again, more slowly.{/n} "In the Abyss you sat with me and lied until I laughed, and for one night it was quiet. I have tried to make that happen again by myself. It does not work. I find that very insulting, and I have not forgiven you for it."'''))

# ---------------------------------------------------------------------------------------------------------------------
# Epilogues. Locked Claude prose: only failing paragraphs re-voiced in place (same gates, same indices); new readers
# appended after every existing paragraph.
# ---------------------------------------------------------------------------------------------------------------------
E = P + "epilogue."
text(E + "refused", "page", "Her name remained among the crusade's records", '''
{n}The Commander closed the door on Camellia, and she did not knock twice. She had never knocked twice on any door in her life.{/n}''')
TAME = '''{n}The Commander once asked her to put the knife away for good. She did. She put it away in someone else, in Nerosyan, the following spring, and sent the Commander a pressed camellia folded into a stranger's glove. The glove had been washed, very carefully, and was still stiff at the fingertips.{/n}'''
para(E + "refused", "page", 2, "sent the Commander the report", TAME)
para(E + "refused_living", "page", 0, "sent the Commander the report", TAME)
para(E + "refused", "page", 5, "A pressed camellia arrived without a letter", '''
{n}After the war she went her own way. Once a year a pressed camellia came for the Commander, with no letter and no name, addressed in the careful schoolroom hand the Commander remembered; and every year, in whatever city it had been posted from, somebody had been found that week with one wound, very neat, right where a friend would stand.{/n}''')
para(E + "refused", "page", 6, "No further orders went to her; no reply came from her", '''
{n}She was thrown out of the crusade, and went without a scene, which frightened the quartermaster more than any scene would have. Nobody in Drezen could say afterwards where she slept. Twice that winter the watch pulled a man out of the canal with one wound under the breastbone, very neat, and did not think to connect him with anybody.{/n}''')
para(E + "refused", "page", 7, "Her death stood. The room was cleared", '''
{n}In the crusade's register her death stood. Her room was cleared, and no new flowers arrived.{/n}''')
para(E + "refused", "page", 8, "She had returned once. Her later death", '''
{n}She had come back once. The second time she did not, and nobody brought the wrong lilies.{/n}''')
para(E + "refused", "page", 9, "No further orders went to her, and no reply came", '''
{n}The woman who had climbed out of a coffin was thrown out of the crusade as well. She took the dismissal with exquisite courtesy, and her knife, and the Commander never saw her again; the Commander did, now and then, read about her, the way one reads about a fever moving through a district.{/n}''')
add(E + "refused", "page", when(P + "raised", '''
{n}The register was wrong, and only the Commander knew it. The woman who had climbed out of that coffin did not come to the Commander again. She left Drezen veiled, and the Commander learned to read the city's reports of the dead for one wound, very neat, right where a friend would stand.{/n}''', forbids=(P + "returned",)))

LIST = '''{n}She kept the list on the Commander's shelf all her life, and went on adding to it. Some mornings a name had a fresh line through it and a date beside it in her small schoolroom hand, and her gloves were drying by the fire, and she watched the Commander read it over breakfast. The Commander always decided, in the end, to say nothing. She never once thanked them for it; she only looked pleased, the way a cat looks pleased.{/n}'''
para(E + "kept", "page", 15, "the Commander could watch the ink dry", LIST)
WITNESS = '''{n}The witness's account stayed with the watch, and so did the witness, alive, which Camellia never entirely forgave. She changed her table at Fye's and her gloves, and nothing else. Every week of the peace she made the Commander walk her past the tavern where the account had been read aloud, slowly, so that she could watch the Commander's face as they passed.{/n}'''
para(E + "kept", "page", 24, "Camellia changed her veil and her table at Fye's", WITNESS)
para(E + "commit", "page", 3, "Camellia changed her veil and her table at Fye's", WITNESS)

HOUSE = "household.pair."
READERS = (
    when(P + "oath_loophole", '''
{n}The woman she had killed once, who had not stayed killed, lived out her life in the same city as Camellia. Camellia kept the terms of her own game to the letter: once was all she had been promised. She never touched her again. She bade her good morning in the street, very pleasantly, every time, and watched her decide whether to answer.{/n}'''),
    when(P + "oath_threatened", '''
{n}The Commander had once promised to show her how convincingly a Commander could kill. She never forgot it. On the evenings when the knife came out of her sleeve she would sometimes ask, very politely, whether that promise still stood, and she put the knife away only when the answer pleased her.{/n}'''),
    when((HOUSE + "camellia_arueshalae.choice.both_yes", "participant.arueshalae.available"), '''
{n}Arueshalae still came to the workroom some nights, and Camellia still made her ask at the door, and neither of them ever told the Commander what was said on the other side of it. Camellia came back to bed smelling of something sweeter than lilies, and slept like a cat that has been fed.{/n}'''),
    when((HOUSE + "camellia_vellexia.choice.both_yes", "participant.vellexia.available"), '''
{n}Vellexia kept a chair for her beside her own at every salon she held after the war. Camellia sat in it perhaps one evening in three and said very little, and the guest who laughed first at the wrong moment on those evenings was never invited again. Some of them were never seen again at all. Vellexia said that was the best thing about her.{/n}'''),
    when((HOUSE + "seelah_camellia.method.confession", "seelah.present_now"), '''
{n}Seelah kept the paper with Camellia's confession on it for the rest of her life, and Camellia never once asked for it back. They fought side by side whenever the crusade asked it of them. Seelah never turned her back on her, and Camellia never stopped smiling at the place between her shoulders.{/n}'''),
    when((HOUSE + "soana_camellia.claim.left_standing", "soana.present_now"), '''
{n}Soana never let her past the edge of the forest again, and said so, loudly, to anyone who would listen. Camellia never asked to be let in. Once a year she rode out to the edge of the trees, and stopped, and looked for a long time, and rode back with her lips parted.{/n}'''),
)
add(E + "kept", "page", *READERS)
add(E + "commit", "page", *READERS)

# Last Call: the Kaylessa pair is no longer a sold description (see below).
para("camellia.lastcall.page", "page", 5, "without a word about the merchant or his carrier", '''
{n}Camellia passed Kaylessa at the feast without a word about the tannery lane or the man she had left sitting in it. "I still miss that perfume," she told the Commander later. "The next man who fetches an elf for me had better be worth losing it for."{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# Nurah reactions (Camellia speaks; her row owns them): she kills, she does not eat.
# ---------------------------------------------------------------------------------------------------------------------
text("nurah.trickster.react.camellia_draft", "start", "I would simply have eaten her", '''
"Your runaway halfling is selling pamphlets with an insult to herself on the first page, in her own hand."
{n}Camellia turns a page of one; she has a copy.{/n} "I would simply have opened her throat over her own printing press. Your way is so much more... literary."''')
text("nurah.trickster.react.camellia_veiled_draft", "start", "I would simply have eaten her", '''
{n}A folded card comes up with the evening dispatches, sent over from Fye's tavern by his pot-boy. It smells of lilies. It was left, the boy says, by the lady at the far end of the bar, who has still not touched her wine.{/n}
"Your runaway halfling's pamphlet is on the bar. Someone left it here for me, as a joke, I think. There is an insult to her on the first page, in her own hand. I read it three times. I would simply have cut her throat, darling. Your way leaves so much more of her for later."''')

# ---------------------------------------------------------------------------------------------------------------------
# household.pair.camellia_wenduag (Camellia's row owns it): the snared cultist is hers to finish, on screen;
# Wenduag's rival register at the "princess" (Wenduag review, section 4).
# ---------------------------------------------------------------------------------------------------------------------
for step in ("settle", "retry"):
    text(HOUSE + "camellia_wenduag." + step, "reversed", "Keep pointing. I'll move my hunters.", '''
{n}In the courtyard, Camellia crouches beside the wire without letting her skirt touch the mud. She lifts the loop and points to a scrape beneath the alley arch.{/n}
"There. Shoulder height, when the foot catches. Not the neck. You would pull it loose."
{n}Wenduag watches her hands, then signals the scouts onto the flanking roofs herself.{/n}
"Keep pointing, princess. I'll keep my hunters off your skirt."
{n}You drag the anchor round, drive it between the stones and haul the wire taut. By the time you take cover, your palms are raw. Boots scrape in the alley. The first cultist falls hard; the scouts' bolts drive his companions back against the wall. Camellia reaches the snared man before anyone else does. She kneels in the mud she would not let touch her skirt, sets the point of her rapier in the hollow of his throat, and pushes it in slowly, looking into his eyes the whole way.{/n}
"Your quarry would have admired it from the other street," {n}Camellia murmurs.{/n}
"You know how to make something struggle." {n}Wenduag studies her instead of the dead man. Camellia pulls her glove straight.{/n} "I'll remember that."
"Remember the alley. Your hunters are waiting for you."''')

# ---------------------------------------------------------------------------------------------------------------------
# household.pair.kaylessa_camellia: the "merchant's description" for a buyer of "observations" was paperwork in place
# of the woman who natively asks for privacy with the poor elf (363f363e). The sheet is a hunting mark, the carrier is
# her fetcher, and he dies for following the wrong elf. Flags unchanged: the shipment, her copy, her clasp, the cover.
# ---------------------------------------------------------------------------------------------------------------------
K = HOUSE + "kaylessa_camellia."
text(K + "settle", "start", "Camellia slides a merchant's description", '''
{n}A perfume chest stands beneath the corner table. Camellia lays a sheet of her small schoolroom hand across its lid: a hooded elf in a courier's grey cloak, the market road she takes at dusk, the lane behind the tannery where that road runs empty, and the hour. Kaylessa reads it without touching the paper. Beyond the tavern windows, a cart carries broken crusader shields to the smithy.{/n}
"My carrier fetches things for me," {n}Camellia says.{/n} "Perfume. Powder. Now and then a person, to a cellar where we can talk without being interrupted. He wears my clasp so the gate lets him by. He has fetched three since Kenabres, and not one of them has complained." {n}She smooths the sheet flat.{/n} "I haven't given him this. Yet."
"Tell me where the load is going, soldier. Then tell me what she left out."
{n}Camellia taps the chest.{/n} "My powder and perfume go out with the caravan, and he goes with them, and he follows whoever wears that grey cloak. A dreadful waste. But he can be made to follow the wrong passenger."
"You," {n}Kaylessa says, looking at you.{/n} "Not some fool you found outside. I'll choose your coat. No spells, and nothing hidden from me."''')
LANE = '''{n}He follows you all the way to the tannery lane. Camellia is waiting there in the dark. She lets him come close enough to reach for your sleeve; then she steps out behind him and puts her knife in under his ribs, up and in, as close as a friend. He turns his head to look at her, very surprised. She holds him up until he stops trying to speak, and lowers him against the wall, and wipes the blade on his coat.{/n}
"He followed the wrong elf," {n}she says.{/n} "I never keep a man who can be fooled by a coat. And he has seen your face under that hood, which is more of you than I let anyone see."'''
text(K + "settle", "landed", "The lashings can be switched", '''
{n}You switch the lashings without leaving a mark. The perfume chest goes out with the ordinary caravan, away from Kaylessa's market road, and at dusk you put on the coat Kaylessa chose and walk past the carrier's window, slowly, hood up.{/n}
''' + LANE + '''
{n}She holds her copy of the sheet to your lantern until it catches.{/n} "There goes my perfume, and a useful fool. I could have bought a very fine dress with what tonight has cost me."
{n}Kaylessa steps out of the next doorway, where she has been watching the whole time. She weighs a silver clasp in her hand; she took it off his collar in the market that morning.{/n} "You get this back when that burns." {n}It burns.{/n} "Good. Now he sells my face to nobody. I'll stop using the grey cloak."''')
text(K + "settle", "carried", "The chest is light enough to carry", '''
{n}The chest is light enough to carry. Walking it out to the outbound caravan yourself takes the evening you had left free for the Fool King's court, and you do it in the dark coat Kaylessa picks, slowly, past the carrier's window, so that he gets a good long look at the wrong elf.{/n}
''' + LANE + '''
{n}Back at the corner table, she holds her copy beside the flame.{/n} "There goes my perfume. And my carrier. I shall have to find someone else to fetch things for me."
"Nobody will fetch me." {n}Kaylessa offers the silver clasp; she took it off his collar in the market that morning.{/n} "Burn that first. Then I won't have a reason to keep this."''')
text(K + "settle", "missed", "He used to know better.", '''
{n}The lashings will not pass inspection. A loose end betrays the switch; the coat intended for the false passenger is still lying beside the chest. Kaylessa stays inside, out of the carrier's sight.{/n}
"Too curious," {n}Camellia murmurs, and touches the knife in her sleeve.{/n} "He used to know better. I may have to remind him."
"He'll learn a coat, not my face," {n}Kaylessa says.{/n} "Don't send me down that road. Give him time to stop watching the gate, then we'll use another."
{n}The shipment can still be held back. Neither the sheet nor the clasp has changed hands.{/n}''')
text(K + "settle", "declined", "How unfortunate that my man cannot hear it.", '''
{n}Camellia folds the sheet once and tucks it into her glove.{/n}
"A gallant speech. My man cannot hear it, of course. He only ever hears me."
"Keep the paper, then," {n}Kaylessa says.{/n} "You won't get the road I take tomorrow."
{n}Camellia smiles at her the way she smiles at a name she has not crossed out yet. Kaylessa does not smile back. Outside, another wounded patrol passes the windows.{/n}''')
text(K + "retry", "start", "I shall have to find someone else to carry my little purchases.", '''
{n}Kaylessa waits beside the tavern's back door, wearing a courier's grey cloak. Camellia has brought the perfume chest. Outside, wagons creak towards Drezen's gate, past wounded crusaders coming in.{/n}
"Your carrier recognized the false passenger," {n}Kaylessa says.{/n} "He hasn't seen my face. Keep it that way."
"He has become quite tiresome," {n}Camellia replies.{/n} "Burn the chest where he can see it, and walk away from the fire in her coat. Let him chase you. I shall be waiting at the end of whatever lane he chases you down."
"The northern caravan, soldier. I'll give you a different coat. And you can explain every turn before we leave."''')
text(K + "retry", "sealed", "Do bring back my clasp.", '''
{n}The northern caravan is ready to leave. Taking its road will cost your evening at the Fool King's court. Kaylessa lays a dark coat over the chest, keeping its collar turned away from Camellia.{/n}
"No magic. No lies to me," {n}she says.{/n} "He follows your coat, not mine."
{n}The chest burns in the yard, where he can see it, and he follows the coat out of the firelight and into the tannery lane, and does not come out again. Camellia does, a little later, drawing on a clean pair of gloves.{/n}
"And I lose my perfume, my powder, and a useful fool." {n}She holds her copy of the sheet over the candle.{/n} "Do give me back my clasp. I would hate to leave anything prettier than him in that lane."
{n}Kaylessa opens her palm. The silver clasp lies there.{/n}''')
text(K + "retry", "refused", "People who think they have found something valuable always do.", '''
{n}Camellia closes the chest without locking it.{/n}
"He will ask again. People who think they have found something valuable always do. And then he will come and tell me, and I shall go and look."
"Then I won't use that road," {n}Kaylessa says.{/n} "And I won't forget whose man is watching it."
{n}The caravan's departure bell sounds outside. Neither woman moves.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# household.pair.seelah_camellia: [PROSE PENDING] voiced. She wants public cover; Seelah withholds the blessing and keeps
# her as dangerous company (Camellia natively mocks Seelah's tender heart and her tiefling youth, 895ef55d, 1e718920).
# ---------------------------------------------------------------------------------------------------------------------
SC = HOUSE + "seelah_camellia."
REASONED = '''
"Mercy, then, and no blessing." {n}Camellia says it as if tasting a wine she has been warned about.{/n} "How very precise of you, my friend. I only wanted the chaplains to see me standing near something holy. It saves so many tiresome questions about my sleeves."
{n}Seelah lights the candle. She does not ask Camellia to bow her head, and Camellia does not. She stands at Seelah's shoulder, unblessed, and watches the dead man's shield all through the prayer with the polite, absorbed attention of a woman at someone else's funeral.{/n}
"Stand there, then," {n}Seelah says when it is done.{/n} "Not one step nearer. I'll fight beside you. I won't lie for you."
"Nobody asked you to lie, paladin. Only to stand still while I do. Are all paladins so tender about the difference?"'''
EVIDENCE = '''
{n}Camellia reads her own admission upside down across the table: that there was never any Mireya, that she made her up. Her smile stays exactly where it is. Her voice does not.{/n}
"You kept it." {n}It comes out low and hoarse, like gravel under a boot.{/n} "In writing. Beside a dead man's shield, where the whole Table can read it."
"I'll keep it here," {n}Seelah says.{/n} "I won't call murder holy because we need another blade on the walls. You'll fight. You won't hide behind a spirit at my table again."
{n}The polish comes back over Camellia's face like a glove drawn on.{/n} "Keep it close, then. Paper burns so easily. So do tents." {n}She takes up her wine.{/n} "Light your candle, paladin. I shan't spoil your prayer. I have never once needed one."'''
for step in ("settle", "retry"):
    pending(SC + step, "reasoned", REASONED)
    pending(SC + step, "evidence", EVIDENCE)
pending(SC + "retry", "start", '''
{n}Seelah has brought the cracked shield back to the corner table. The candle beside it is still unlit. Camellia sits down across from her before she is asked, and folds her hands like a girl at a recital.{/n}
"Back again," {n}Seelah says.{/n} "If you want me to pray over you, the answer hasn't changed."
"Over me? Heavens, no." {n}Camellia smiles at the shield.{/n} "Near me will do. The chaplains are so much more polite to a woman they have seen standing beside a paladin at prayer, and I am so tired of their questions."
"Then say plainly what you want, or let me finish for the dead."''')
pending(SC + "retry", "word", '''
{n}The candle catches by itself. Seelah's hand goes to her sword before she looks round at you.{/n}
"Again? You can end an argument with that trick. You can't make me bless her."
"I had not asked you to." {n}Camellia rises and smooths her skirt.{/n} "I only wanted to be seen standing here while you prayed. Keep your blessing, paladin. I have a great deal of use for a woman who will not lie for me. She is so very easy to predict."
"Demons," {n}Seelah says.{/n} "Go and kill demons. And keep that knife where I can see it."''')
pending(SC + "retry", "refused", '''
"Such solemnity, again, over a little courtesy." {n}Camellia's knuckles whiten on the cloth; her smile does not move.{/n} "Very well, paladin. Pray alone. I shall stand at the back of every chapel in Drezen instead, where nobody minds who I am."
{n}Seelah takes the shield and stands.{/n} "Come on. There's still a wall to hold. Don't walk behind me."
{n}Camellia lets her go first anyway, and watches the place between her shoulders all the way to the door.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# household.pair.camellia_arueshalae: [PROSE PENDING] voiced (she owns the shared pair; the Arueshalae row is lower).
# ---------------------------------------------------------------------------------------------------------------------
CA = HOUSE + "camellia_arueshalae."
INSPECT = '''
"Very well. No more pretty invitations." {n}Camellia takes the cloth off the bench. Under it lies a crusade blade with something dark worked into the edge, and a stoppered bottle that she keeps under her own hand.{/n} "This is what I was doing while I asked you to sit closer. It is for the march: a cut that will not close, and a man who takes all night to understand it." {n}She turns the edge to the lamp, toward Arueshalae, and keeps her thumb on the hilt.{/n} "Look, if you like. Do not touch, and do not ask me for the bottle. I should hate to waste it on you."'''
for sid in ("settle.good", "settle.evil", "retry.good", "retry.evil"):
    pending(CA + sid, "inspection_camellia", INSPECT)
FALLEN = '''
{n}Arueshalae leans over the bench until her hair nearly brushes the steel, and breathes in, slowly, the way she breathes near a throat. Her hands stay folded behind her back.{/n}
"Bitter. Something from a sickroom and something from a garden. It would spoil you for me." {n}She smiles with her teeth.{/n} "And it's uneven, there, beside your thumb. Don't look at me like that, Cami. I'm not going to lick it to prove I'm right."
{n}Camellia turns the blade, finds the patch, and draws it back to her side.{/n} "No. You are going to sit there and want something you cannot have. How novel for you."
"For both of us." {n}Arueshalae takes the chair at last, and leaves her hands where Camellia can see them.{/n}'''
for sid in ("settle.evil", "retry.evil"):
    pending(CA + sid, "inspection_arueshalae", FALLEN)
choice(CA + "company", "start", 3, "[PROSE PENDING: choice", "[Leave them the evening over the work she has already shown.]")
pending(CA + "company", "witnessed_company", '''
{n}The treated blades are already packed; Arueshalae has seen them, and Camellia does not take them out again. She pours two cups instead and pushes one across the bench.{/n}
"You have inspected my work. There is nothing left on this bench to inspect but me, and I find I do not mind." {n}She watches Arueshalae lift the cup.{/n} "Tell me something you have never told the Commander. I shall know if it is a lie, and I shall enjoy it either way."
{n}Arueshalae laughs, low, and tells her. Camellia listens with her chin on her hand, her lips a little parted, and does not interrupt once.{/n}''')

# ---------------------------------------------------------------------------------------------------------------------
# household.pair.nenio_camellia: [PROSE PENDING] voiced. One limited method shown, the rest kept "for people".
# ---------------------------------------------------------------------------------------------------------------------
NC = HOUSE + "nenio_camellia."
LESSON = '''
"One sample, then, little fox. One." {n}Camellia lifts the dry sample between finger and thumb and holds it to the lamp.{/n} "Your column says 'inert'. It is not inert. It is waiting. It wants warmth and a pinch of salt, like everything else that kills."
{n}She has you hold the dish steady over the flame while she breathes on the crust and works it with the flat of a knife. The grey goes dark and wet, and a smell rises from it like a sickroom.{/n} "There. That is the one thing I shall show you. My other methods are not for columns, Nenio. They are for people."'''
REFUSED = '''
"No lesson." {n}Camellia sweeps the dry sample into her handkerchief and folds it away into her glove.{/n} "You heard the Commander. Put me in whatever column you like, little fox. 'Uncooperative', perhaps. Do underline it."
{n}She takes the remaining samples with her. Nenio's sheet stays half empty.{/n}'''
MANUAL = '''
"Warmth first. Your hands, my friend, not mine; she is watching mine." {n}Camellia stands at your shoulder and tells you exactly where to hold the dish over the lamp, for how long, and how much salt. The grey crust darkens under your fingers and goes wet, and the sickroom smell rises.{/n} "Enough. Now she has seen it done, by hands that do not know why it works." {n}She smiles at Nenio.{/n} "That is my advantage spent, little fox. Write it down. It is the only page of me you will ever have."'''
for step in ("settle", "retry"):
    pending(NC + step, "lesson", LESSON)
    pending(NC + step, "refused", REFUSED)
    pending(NC + step, "manual_correction", MANUAL)
pending(NC + "settle", "spoiled", '''
"Proves what its owner is?" {n}Camellia laughs, prettily, and lifts the dry sample off the bench before Nenio can reach it.{/n} "It proves I keep a tidy workbench. If you mean to accuse me of something, my friend, do find a better witness than a pinch of dust."
{n}She pockets the remaining samples one by one, watching Nenio's pen.{/n} "Your classification will have to stay incomplete. So many things do, around me."''')


# ---------------------------------------------------------------------------------------------------------------------


def _scenes(payload):
    return {scene["Id"]: scene for scene in payload["Scenes"]}


def _node(scenes, sid, nid):
    return overlay_node(scenes, sid, nid)


# struct3-b readers: the once-only oath was kept, and the woman it spared is gone again by other hands or her own choice.
# Nothing is revived; the loss lands on Camellia, who had agreed not to touch her a second time.
OATH_LOST = {
    "nurah": '''{n}She had killed the little writer once, and had agreed to kill her no more, and she kept to it. Then the writer was gone from Drezen a second time, and Camellia had not so much as lifted a finger. She learned it from a clerk over the soup. She finished the soup. That night she took the lilies she had bought for no one and shredded them over the Commander's floor, petal by petal, in the lamplight, with her small neat hands. "She was mine," she said, very pleasantly, to the pile. "Once. That was the whole bargain, and somebody has broken it for me." Three nights later a copyist who had mocked the dead woman's spelling in a tavern was found in a gutter, and the knife had been a long time about its work. She did not tell the Commander. She did not have to.{/n}''',
    "soana": '''{n}Soana Wintersun had been bled once on Camellia's own blade and sent back to her forest, and Camellia had agreed to leave her there. She kept to it. She was not at the forest's edge when the Wintersun woman was lost the second time, and she could not forgive that. She rode out alone to the line of the trees, stopped where she always stopped, and sat her horse a long time looking at the empty path between them. Nobody scolded the crows. Nobody told her to go home. When she came back she smelled of woodsmoke, and her sleeve was wet to the elbow, and the hunter who had wandered into the wrong clearing that evening did not come home at all. "Disappointed in me, I suppose," she said at supper, turning the knife under the candle. "It is rather rude of her to do it where I cannot hear."{/n}''',
    "kaylessa": '''{n}The elf under the tailor's awning had watched Camellia's hands for years without once being touched by them again, and Camellia had enjoyed that more than she cared to say. Then the awning was empty, and the wrapped shape was gone from it, and nobody in the market could say when or how. She stood under it for an hour with her veil down. She asked the tailor, politely, and then the tailor's apprentice, less politely, and the apprentice's two fingers were left on the cutting table, and he told her the only thing he knew, which was nothing. "I was promised her once," she told the Commander afterwards, and the knife ticked against the plate. "I did not think I would have to be so careful with her afterwards. Someone else has been careless with my property. I do hope you will let me find out who."{/n}''',
}
OATH_LEGACY = '''{n}Camellia never named the one she had been allowed to kill only once, and nobody asked her to. After a few glasses she would say that the promise had held, to the letter, to the end, and that she was proud of keeping it. Then she would smile at the Commander over the rim, and ask whether anyone, anywhere, had ever been so well behaved.{/n}'''



def integrate(payload):
    scenes = _scenes(payload)
    for (sid, nid), body in PLACEHOLDER.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            if not node["Text"].startswith(PENDING):
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail="camellia cloud: %s/%s is no longer a placeholder" % (sid, nid))
            node["Text"] = body
    for (sid, nid), (expect, body) in TEXT.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            if expect not in node["Text"]:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(expect)[:70])
            node["Text"] = body
    for (sid, nid, index), (expect, body) in CHOICE.items():
        with overlay_item():
            choices = _node(scenes, sid, nid)["Choices"]
            if index >= len(choices) or expect not in choices[index]["Text"]:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(expect)[:70])
            choices[index]["Text"] = body
    for (sid, nid, index), (expect, body) in PARA.items():
        with overlay_item():
            paras = _node(scenes, sid, nid).get("Paragraphs") or []
            if index >= len(paras) or expect not in paras[index]["Text"]:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(expect)[:70])
            paras[index]["Text"] = body
    for (sid, nid), extra in ADD.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in extra]
    touched = {k[0] for k in PLACEHOLDER} | {k[0] for k in TEXT} | {k[0] for k in CHOICE} | {k[0] for k in PARA} \
        | {k[0] for k in ADD}
    for sid in touched:
        if sid not in scenes:
            record("overlay.scene_resolution", scene=sid)
            continue
        for node in scenes[sid]["Nodes"]:
            with overlay_item():
                texts = [node["Text"]] + [c["Text"] for c in node["Choices"]] + [x["Text"] for x in node.get("Paragraphs", [])]
                if any(PENDING in t for t in texts):
                    raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=node.get("Id"), detail="camellia cloud: prose still pending at %s/%s" % (sid, node["Id"]))

    # struct3-b: bind the anonymous living callback to the actual oath victim.
    # Run after voice transformations; retain the original paragraph and index.
    for ending in ("kept", "commit"):
        with overlay_item():
            page = _node(scenes, E + ending, "page")
            callback = next((x for x in page["Paragraphs"]
                             if x.get("Requires") == [P + "oath_loophole"]), None)
            if callback is None:
                raise OverlayMismatch("overlay.paragraph_resolution", scene=E + ending, node="page")
            callback["Requires"] = [*callback["Requires"], P + "oath_victim.available"]
            for woman in ("nurah", "soana", "kaylessa"):
                page["Paragraphs"].append(when(
                    (P + "oath_loophole", P + "oath_victim." + woman),
                    OATH_LOST[woman],
                    forbids=(woman + ".present_now",)))
            page["Paragraphs"].append(when(
                P + "oath_loophole",
                OATH_LEGACY,
                forbids=(P + "oath_victim.recorded",)))

    # fix15: the retry's later voice overlay cannot award an offscreen killing.
    from storylines.harem_rows import s42
    s42.require_shown_retry(payload)
