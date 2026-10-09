"""Melazmera: cloud voice-owner pass (villain-route-melazmera, design-first).

Applied late, from storylines/harem_rows/zzz_melazmera_cloud.py, after the S36
pair row has attached its Last Call readers to melazmera.lastcall.page. Text and
flag-gated paragraphs only: no scene, node or choice id, choice position, Next,
Set, gate, check, cost or speaker changes. Existing paragraphs keep their gates
and indices; new readers are appended after them. Review and truth table:
tools/route_packs/redesign/melazmera/cloud-review.md, truth-table.json.

Structure fixed here (read-only consumers of flags the route already sets):
  * melazmera.trickster.terms.owed is set by three different answers (you owe me
    for the sailors / call the harpoon even / the missed ship was my first gift)
    and all three were answered with one "Owe." reply; the owed node now answers
    each claim (gated on the same voyage flags as the three choices), and
    commit.stone reads the terms the Commander chose (owed, rent) at the hoard;
  * the owed and rent replies cited the Hepzamirah truce as live even when
    hepzamirah.dead (ch4.hunt's own truce_dead says the truce died with her);
  * promises and costs with no reader: queen_poison_lie, terms.rent,
    fed.demons ("I will come back and eat your priests' prisoners anyway"),
    beat.soul_lied / soul_refused ("I will be at the end of her line"),
    beat.dinner_eaten, beat.flight_let_go, beat.greybor_claimed,
    morning.stayed now reach the hunt, the hoard, the epilogues, the mourning
    page and the Last Call page;
  * wrong medium and paperwork: the docker's letter "with the Knight
    Commander's seal" (a seal the Commander no longer owns) in beat.crew:paid,
    the lord's letter and receipt in ch5.hunger, the inquisitor's copies and
    packets (spoken by the Inquisitor portrait, carrying Melazmera's lines), the
    report/archive/compensation epilogue lines, and the first-person ledger
    lines ("I promised to take the dangerous last wagon") on her Last Call page
    are restaged as on-screen consequences in narration;
  * commit.stone:stone named the sapphire before she does.
Voice: beat.queen's candle-eating (voice pack "She never says: cute drift:
candle-crunching") becomes a harpy eaten on the desk.

Canon used (enGB keys): 2433842e (the deck massacre, the purr), 70c883b1 (eats
everything, even dead souls; the giggle), 832dc662 (rocks wrapped in illusions),
a68b28c8 (the truce with Hepzamirah), 784e7903 (the harpoon), 7580716e (the
rattling of chains draws her), dd1d7b49 (a dragon's hoard).
"""
from story_format import p

M = "melazmera.trickster."
PENDING = "[PROSE PENDING:"

NODES = {}
PARAS = {}
RETEXT = {}


def text(scene, node, body, paras=()):
    NODES[(scene, node)] = body
    if paras:
        PARAS.setdefault((scene, node), []).extend(paras)


def add(scene, node, *paras):
    PARAS.setdefault((scene, node), []).extend(paras)


def retext(scene, node, old, new):
    """Replace one existing paragraph text (all copies), keeping its gates and index."""
    RETEXT.setdefault((scene, node), []).append((old, new))


ATE, HARPOONED, CREVICE = "melazmera.ate_sailors", "melazmera.harpooned", "melazmera.voyage.crevice"
OWED, RENT = M + "terms.owed", M + "terms.rent"
GREYBOR_GONE = "melazmera.greybor_gone"

# ---------------------------------------------------------------------------
# The first meeting (three copies: Colyphyr, the Abyss camp, Drezen).
# ---------------------------------------------------------------------------
HUNTS = ("ch4.hunt", "ch4.hunt_found", "ch5.hunt_window")

OWED_OPEN = '''"Owe." {n}She rolls the word round her mouth like a knucklebone she means to crack.{/n}'''
OWED_PARAS = (
    p('''"I ate your sailors, so now I owe you." {n}She giggles.{/n} "That is backwards, thief. Things I eat do not send bills. They are inside me, and they are quiet, and they were salty."
{n}She bends close enough to smell your throat.{/n} "You put a ring in my cave and then came to my fire to collect for men I have already finished. I will come back. Try to collect. I want to see what you dare ask for with my mouth this close."''',
      requires=(ATE,)),
    p('''"Even." {n}Her hand goes to her side, where for a heartbeat the gown is torn purple plate.{/n} "Your captain put a hook in me and turned me over in the air in front of my whole island, and you want to call that even with one ring. Nothing is even with me, thief. Things are mine, or they are eaten."
{n}She bends close enough to smell your throat.{/n} "A fresh start. Good. I will start by deciding which of you I eat first, you or the man with the harpoon. I will come back and tell you."''',
      requires=(HARPOONED,), forbids=(ATE,)),
    p('''"A first gift." {n}She looks delighted and insulted at once.{/n} "You made me go home hungry and you call it a present. A meal that gets away is not a gift, thief. It is a debt, and it is a whole ship's worth of supper."
{n}She bends close enough to smell your throat.{/n} "You will pay it. Not tonight. I will come back with my appetite, and we will see what you have in your pockets."''',
      requires=(CREVICE,), forbids=(ATE, HARPOONED)),
)
RENT_TEXT = '''"Rent." {n}Her eyebrows go up, and the rock on her head tilts with them.{/n} "You are paying me rent. For my island. With a ring."
{n}She throws her head back and laughs, and somewhere in the dark a thing that was sleeping wakes up and runs.{/n} "The swamp queen pays me in knights, although she does not know it. Goats pay me in goat. And now the crusade pays me in jewellery." {n}She wipes her eyes with one knuckle.{/n} "Very well, tenant. I will come and inspect my tenant. Tenants who are late with the rent get eaten, and tenants who are early get looked at very closely. Keep your fire lit. I like to see where things are."'''
POISON = p('''"She tells the harpies you are carrying poison into my nest for her." {n}Melazmera licks her thumb.{/n} "I have eaten poison. It tastes of whoever made it. Bring me some of yours one day, thief. I want to know what you taste like when you are lying."''',
           requires=(M + "queen_poison_lie",))
for _scene in HUNTS:
    text(M + _scene, "owed", OWED_OPEN, OWED_PARAS)
    text(M + _scene, "rent", RENT_TEXT)
    add(M + _scene, "swamp", POISON)

# ---------------------------------------------------------------------------
# ch5.hunger: the cells (her chains, 7580716e) and the herd, face to face.
# ---------------------------------------------------------------------------
S = M + "ch5.hunger"
text(S, "ask", '''{n}She comes and sits on the edge of your desk, so close that you feel the cold coming off her, a cold like the inside of a well.{/n}
"There is a hole under your castle with men in it," {n}she says.{/n} "Men who pray to the fly. They rattle their chains all night. I can hear them from your roof, and every time they rattle I get hungrier. Chains are a dinner bell, thief; everybody on my island knows that." {n}Her scarlet eyes are very bright.{/n}
"Your priests have finished asking them questions. I listened at the grating; they have nothing left to say. They are fat, because you feed them. You are feeding them to nothing. Give them to me. Nobody will miss them. Your priests will be glad of the room."''')

text(S, "forbid_after", '''{n}Two days later a Mendevian lord who has lent the crusade two hundred spears walks into your war council with mud to his knees and his drovers' dogs at his heels, and the dogs will not stop howling. His herd, driven up from the south to feed his men, is gone from its pen outside the walls in a single night: forty head of cattle, the pen whole, the gate shut, the herdsmen asleep, and nothing left in the morning but a stink of cold iron and one hoof, bitten off clean, on the gatepost.{/n}
{n}The hoof lands on your map. The lord wants to know what you mean to do about it. From the roof above the council chamber comes a long, satisfied belch, and every dog in the room lies down flat.{/n}''')

text(S, "herd_cover", '''"A loss to enemy action." {n}The lord takes the crusade's favour with a face like a slammed door, and doubles the pickets on what is left of his stores. That night Melazmera drops a horn on your desk, still warm at the root.{/n}
"Enemy action." {n}She tries the words out, delighted.{/n} "I like my new name. I am going to be enemy action again, when I am hungry."''')

text(S, "herd_honest", '''{n}The lord takes your favour and keeps his spears in the line, and swears in front of the whole council that no beast of his will come within a day's drive of your dragon again. Melazmera watches him go from the windowsill, picking her teeth with a splinter of the pen gate.{/n}
"Forty cows, and he wants to keep all the others. Greedy." {n}She bites the glove he left on the table, thumb first, and swallows it.{/n}''')

# ---------------------------------------------------------------------------
# commit.stone: the hoard reads the terms the Commander chose at the fire.
# ---------------------------------------------------------------------------
S = M + "commit.stone"
add(S, "count",
    p('''"Rent," {n}she adds, and her teeth show.{/n} "You called it rent, on my island. Tenants do not leave when they like, tenant. Read the terms again. Oh. There are no terms. There is me."''',
      requires=(RENT,)),
    p('''"You came to my fire to tell me I owed you for the sailors." {n}She giggles.{/n} "Now you are in my hoard with them. Collect from in here."''',
      requires=(OWED, ATE)),
    p('''"You wanted to call the harpoon even." {n}She presses her palm to her side.{/n} "This is even, thief. You on my heap, and your captain still walking about because I have not got round to him yet."''',
      requires=(OWED, HARPOONED), forbids=(ATE,)),
    p('''"You owed me a ship's worth of supper." {n}She spreads her fingers over the heap.{/n} "I am not going to eat it. That is worse for you. I will be hungry for it every night, and you will be lying right there."''',
      requires=(OWED, CREVICE), forbids=(ATE, HARPOONED)),
)
text(S, "stone", '''{n}You climb the heap. The stones shift and clack under your knees, warm as bread, and she does not move. She taps a grey stone beneath her palm. You reach for that one. You put your hand under hers, flat on the heap, and her fingers are cold as a well, and you slide out from under them one grey stone the size of a hen's egg, lumpy and dull and heavy for its size, and close your hand on it.{/n}
{n}She watches it go. Her whole body goes tight, every line of her, the way a hound's does when you take its bone. Her lip comes back off her teeth. You stop with your wrist beneath them. She presses her free hand into the heap, grinding the stones together, and holds still. You draw the stone clear.{/n}''')

# ---------------------------------------------------------------------------
# beat.crew: the swindle on the quay, told by her, not by a docker's letter.
# ---------------------------------------------------------------------------
text(M + "beat.crew", "paid", '''{n}She is gone three nights. On the fourth morning the sack is back on your war map, empty and damp, with the old seal pressed into its clay, and beside it lies a heap of rocks: grey, lumpy, ordinary, the kind a child could throw.{/n}
"They would not let me land." {n}She is on the sill, in the woman she wears, delighted, picking a flake of grey rock off her thumbnail.{/n} "They stood on the Alushinyrra quay, the wives and the mothers and one very old man, and they screamed and threw fish-hooks at me. So I hung over them with the sack open and let the gold come down on them like rain. They went on their knees in it. They fought over it. One of them bit another one's hand." {n}She giggles.{/n}
"It stayed gold until the first bell. Then it was rocks, in every hand on the quay, and they were all looking up at me. So I told them whose seal was on the sack. I said your name very clearly. Twice. They have it now."
{n}The empty leather smells of salt. Her claw has scored SALTY across it.{/n} "You said pay them. You did not say in what."''')

# ---------------------------------------------------------------------------
# beat.queen: a harpy, not candles.
# ---------------------------------------------------------------------------
S = M + "beat.queen"
text(S, "start", '''{n}You come back to your quarters and find her sitting on your desk in the woman she wears, gnawing the wing of a harpy. The rest of the harpy is under the desk. Some of it is still trying to get away.{/n}
"I had news from my island," {n}she says, around a mouthful of feathers.{/n} "This one came up through the hole. I ate its legs first, so it could not leave, and it told me everything while I ate the rest. Harpies always talk."''')
text(S, "crowned", '''"The thing in the swamp is wearing a rock on her head," {n}she says, delighted.{/n} "A grey rock, from your path. The harpy says it has sunk an inch into her and she will not let anyone near it, and she tells the whole island that the Knight Commander brought her a crown and that it shines." {n}She cracks a wing-bone with her back teeth.{/n}
"You gave her a rock and called it a crown. I give thieves rocks and call them crowns. The difference is that she thanked you." {n}Her eyes gleam in the dark.{/n} "You are very cruel, thief. I did not know."''')
text(S, "denied", '''"The thing in the swamp says you would not bring her my crown," {n}she says.{/n} "She says you told her it was a rock, to her face, and she sank to the bottom of her pool and sulked, and she is going to remember it when the island is hers." {n}She spits out a quill.{/n}
"You told the puddle the truth. Nobody tells the puddle the truth; it is not worth the breath." {n}She looks at you over the harpy.{/n} "Now she has two enemies on her island and one of them is in my hoard. She will not sleep for a hundred years."''')
text(S, "turned", '''"The thing in the swamp turned on you." {n}She sounds delighted.{/n} "She promised you her love and her affection and then she tried to drown you in her whirlpool, because she is too good for the likes of you. The harpy told me all of it. The harpy did the voice, right up until I got to its throat." {n}She does the voice too, wetly, and it is very good.{/n}
"Love and affection, and then a whirlpool. She should have offered you the whirlpool first. At least she owns one."''')
text(S, "fought", '''"You fought the thing in the swamp." {n}She grins with feathers in her teeth.{/n} "The harpy heard her screaming about her powafulness. It did the voice."
{n}She repeats the word in a wet, shrill gurgle.{/n} "I would have liked to hear it myself. I have never heard her say it while somebody was hitting her."''')
text(S, "plain", '''"The thing in the swamp is telling everyone that the Knight Commander was her knight," {n}she says.{/n} "That the Knight Commander came to her in her cave and did everything she said and went away grateful, and that she is going to be queen of the whole island now that the fat lizard has gone." {n}She cracks a wing-bone.{/n}
"I am the fat lizard." {n}She sounds more amused than offended.{/n} "She has been calling me that for years. When I am finished with your war, I am going to go back and sit on her swamp until it is dry."''')
text(S, "keep", '''"Harmless." {n}She licks harpy off her fingers.{/n} "She sent knights to be my supper for years and called it a present to herself. You can keep your pity. I have a cave on your side now."''')
text(S, "ask", '''"Bring your steel, then." {n}She cracks the harpy's skull between her palms like a walnut.{/n} "I will bring my mouth. We can find something worth using both on. Not tonight. Your pickets have left me a warm trail."''')
text(S, "anyone", '''"To anyone," {n}she repeats.{/n} "To get into my cave." {n}She puts down what is left of the harpy and looks at you over it.{/n} "Then you are a liar and a thief, and you went into a dragon's cave on a puddle's word, and you did not even take the crown." {n}She licks blood off her thumb.{/n} "I am going to keep a very close watch on you."''')
text(S, "happy", '''"She thanked you for my bait." {n}Melazmera giggles, licking blood off her thumb.{/n} "Next time she sends a knight, I shall ask him to bow to it before I eat him."''')
text(S, "learned", '''"You learned badly. I get a meal when somebody takes my crown. You got thanked." {n}She presses your old seal into the harpy's breast, neatly, as if it were wax.{/n} "Still. Her face. I wish I had seen her face."''')
text(S, "dismiss", '''{n}She drops the harpy's skull onto your report.{/n} "Fine. I will not talk about your swamp. I did not say I would not sit on it. What is for supper?"''')

text(M + "beat.joke", "laughs", '''"Other people." {n}She tilts her head.{/n} "I do not laugh at jokes either. I laugh when things are funny. A goat running the wrong way, into my mouth. A paladin who says foul beast and then touches my crown. The thing in the swamp trying to be beautiful."
"You are the one your soldiers say makes jokes. So make one. If it is bad I will eat your horse."''')

# ---------------------------------------------------------------------------
# beat.inquisitor: the inquiry face to face, the meal on screen.
# ---------------------------------------------------------------------------
S = M + "beat.inquisitor"
text(S, "do", '''{n}She smiles at you, slowly, with every tooth she has, and for a moment the woman is not there at all.{/n}
"There," {n}she says softly.{/n} "You are learning what I am for."
{n}She goes out over the sill. A little before dawn she is back on it, licking her fingers one at a time, and drops something in your lap: a sunburst medallion on a broken chain, bent nearly double by a bite.{/n} "Thin," {n}she says.{/n} "I told you. All gristle and prayers. He said his goddess's name the whole way down, as if she were going to come and get him."
{n}In the morning the inquisitor's acolyte comes to the gatehouse alone, white to the lips, and says that his master went down to the cellars with the lamp and told him to wait on the stairs, and that the lamp went out, and that his master did not come up. The gaoler writes missing in his book, this time, not escaped. He does not look at you when he writes it. That is worse.{/n}''')
text(S, "inquiry_lie", '''"Sealed." {n}He does not write it down. He looks at the locks again for a long time, as if they might change their story, and then at you.{/n} "Then I will keep looking, Knight Commander, until the seal breaks."
{n}That night Melazmera hangs head-down outside your window and laughs at you through the glass: seven cells, such a small lie for such a large meal. Far below, a lamp moves through the cellars until dawn.{/n}''')
text(S, "inquiry_admit", '''"Then it is your name, not the gaoler's." {n}He closes the gaoler's book the way a man closes a coffin. His acolyte is white to the lips.{/n} "My goddess will hear it from me, Knight Commander. So will every knight who asks why your cellars are cold."
{n}That night Melazmera finds you at the window and sniffs at your mouth, delighted. You told him, she says, and he walked away with all his fingers, and now she will have to find her dinner somewhere else.{/n}''')
text(S, "inquiry_refuse", '''"Then your silence goes with me, and the cold in those stones." {n}He does not argue. He takes the lamp from his acolyte and leaves it burning in the last empty cell, the way a man leaves a light on a grave.{/n}
{n}That night Melazmera eats the lamp, glass and all, sitting on your windowsill. You are keeping him alive, she tells you, chewing, not quiet; she can tell the difference even if you cannot.{/n}''')

# ---------------------------------------------------------------------------
# Epilogues: consequences on screen, not in reports; promised readers appended.
# ---------------------------------------------------------------------------
EPILOGUES = ("epilogue.together", "epilogue.commit", "epilogue.declined", "epilogue.left_free")
RETEXTS = (
    ("{n}The inquisitor's report named the Commander as the one who gave seven prisoners to Melazmera. The acolyte carried the confession with the measurements of the untouched locks.{/n}",
     "{n}The inquisitor named the Commander, not the gaoler, to every inquisitor and every knight who would listen. Melazmera sat on the chapter-house roof the night he preached it and ate a pigeon very loudly through the whole sermon.{/n}"),
    ("{n}The inquisitor sent the measurements and the Commander's refusal to answer up the chain. A second copy stayed in the chapter room. The seven names remained in it.{/n}",
     "{n}The inquisitor carried the Commander's silence up the chain of the Inquisition, and the cold of those cellars with it. He never came back to Drezen. The lamp he left in the last empty cell burned until Melazmera ate it.{/n}"),
    ("{n}Compensation kept the cattle owner's spears in the crusade. The owner's letter named Melazmera. No more cattle came near Drezen until the war ended.{/n}",
     "{n}The Mendevian lord took the crusade's favour, the spears stayed in the line, and every hall in Mendev heard the name of the dragon who kept company with the crusade's leader. No more cattle came near Drezen until the war ended. Melazmera was delighted; nobody had ever said her name in a hall before.{/n}"),
    ("{n}Forty cattle remained missing from the Mendevian lord's stores. The demand for compensation stayed on the war council's table, unanswered.{/n}",
     "{n}The Mendevian lord never got his answer. He left the bitten hoof on the war council's table, and nobody dared move it, and his drovers would not take a herd north of the Drezen road again.{/n}"),
    ("{n}In the archive of the Inquisition there is a report from Drezen, in a careful hand, about seven prisoners of the Knight Commander's who were moved to a place the Knight Commander would not name, and a cold in a cellar that would not come out of the stones. It was sent up the chain in the last year of the war. Nobody ever closed it.{/n}",
     "{n}The inquisitor never found the seven prisoners, and never stopped looking. He walked the Drezen cellars with his lamp for the rest of the war, and whenever the lamp went out on the stairs he stood very still in the dark until somebody came with a light. Melazmera made sure it went out often.{/n}"),
)
for _scene in EPILOGUES:
    for _old, _new in RETEXTS:
        retext(M + _scene, "page", _old, _new)
    add(M + _scene, "page", p(
        "{n}She had done as she was told once, and eaten the Wound's demons instead of the Commander's prisoners. "
        "She told it as a joke against herself for years: the one night a dragon obeyed, and how bored she was, "
        "and how she had lain on the cellar grating for a week afterwards, listening to the prisoners rattle their "
        "chains, to remind herself what it had cost her.{/n}",
        requires=(M + "fed.demons",)))

add(M + "epilogue.together", "page",
    p('''{n}She went on calling the Commander her tenant. The rent was a visit, paid in person, and she inspected the premises very thoroughly every time.{/n}''',
      requires=(RENT,)),
    p('''{n}The Commander had stayed in the hollow of the heap until she slept, that first morning. She never mentioned it. Every visit afterwards ended the same way, with the Commander pinned in the hollow under a flank like a fallen wall until she chose to wake.{/n}''',
      requires=(M + "morning.stayed",)),
    p('''{n}The Commander had once eaten from a demon's heart at her table and kept it down. She brought worse every year after that, still twitching, and watched the Commander's throat the whole time.{/n}''',
      requires=(M + "beat.dinner_eaten",)),
    p('''{n}Over the Wound, once, the Commander had let go of her spines. She never carried the Commander again without rolling at least once, high up, to see if the thief would do it again.{/n}''',
      requires=(M + "beat.flight_let_go",)),
    p('''{n}Whenever she liked, she borrowed Greybor to stand at the mouth of her cave and look at thieves in the right order. He charged her by the thief. She paid in square gold, and ate the thieves, and the arrangement suited everybody but the thieves.{/n}''',
      requires=(M + "beat.greybor_claimed",), forbids=(GREYBOR_GONE, M + "greybor_wary")),
    p('''{n}On the heap, among the real stones, she kept a lie the Commander had told her on a roof in Drezen, about a soul. It weighed nothing. She counted it anyway.{/n}''',
      requires=(M + "beat.soul_lied",)),
)

# The Commander gave everything and did not come back: her promises about the soul.
add(M + "epilogue.mourned", "page",
    p('''{n}She had told the Commander she would be at the end of the grey lady's line, and be very rude about it. Whether a dragon can reach that line, nobody living could say. The pickets on the north road said only that for a month she did not eat, and lay on the heap with her eyes open, looking down into the dark where the dead go.{/n}''',
      requires=(M + "beat.soul_refused",)),
    p('''{n}The Commander had promised her the soul on a roof in Drezen, and she had tasted the lie and kept it anyway. She put it on the heap with the rest and counted it every night. It was the only thing she owned that weighed nothing.{/n}''',
      requires=(M + "beat.soul_lied",)),
)

# ---------------------------------------------------------------------------
# Last Call page: the S36 readers in her own past tense, no first-person ledger
# lines; the soul promises when the world buried the Commander.
# ---------------------------------------------------------------------------
LC = "melazmera.lastcall.page"
LAST_CALL = (
    ('Melazmera traces the ridge with a grey nail. "Those two loads passed. The next driver had better stop and ask."',
     'Melazmera remembered the ridge above the meat wagons. "Two loads," she said, whenever anybody spoke of convoys. "I let two whole loads go by under my nose. Scratch it on a stone, thief, so nobody thinks I am getting soft."'),
    ('Melazmera sniffs the empty cart. "Your trail spoiled a whole load, thief. Don\'t bring that trick near my hoard."',
     'Melazmera never let the Commander forget the meat lost on the low road. "You laid a trail for the prowlers and they followed it to my supper," she said. "Next time, lay it to the horned one\'s door."'),
    ('Melazmera laughs at the Commander\'s stiff back. "You carried it after all. I let the next load through. Now take your wagons elsewhere."',
     'Melazmera liked best the night the Commander hauled the replacement meat up the ridge on a bent back. "I watched you bend all the way up," she said. "I let the load through because I wanted to see you do it again."'),
    ('Melazmera bares her teeth at the ridge. "If her guards come up, I hunt. You heard me."',
     'The ridge above the wagons stayed Melazmera\'s. The horned one\'s guards learned to walk the long way round it, and the ones who did not learn were not seen again.'),
    ('Melazmera wrinkles her nose. "Prisoners? I asked for my hunting ground. Keep your scraps."',
     'Melazmera never forgave the offer of prisoners on the ridge. "Scraps," she called them, for years. "You offered me scraps on my own hunting ground, like a dog."'),
    ('Melazmera scratches the empty cart. "No meat, no passage. Was that too difficult, thief?"',
     '"No meat, no passage," Melazmera said, and the road beyond Drezen stayed hers. She brought the lost load up whenever she was hungry, which was always.'),
    ("I promised to take the dangerous last wagon.",
     "The Commander had ridden the last wagon under her ridge, the one that smelt best. She thought about it the whole passage."),
    ("I kept the exposed rear watch.",
     "The Commander had kept the rear watch on the low road all night, with her shadow lying over the wagons."),
    ("My false trail cost us a cart of meat.",
     "A cart of meat lost to the prowlers stayed on the Commander's account. Melazmera had watched it go from the ridge and not lifted a claw."),
    ("I spent 400 Finances and hauled the replacement myself.",
     "The Commander had paid four hundred from the crusade's coffers and hauled the replacement up the ridge in person."),
    ("The outriders cost 300 Finances; I also gave up my reserved stores.",
     "The outriders had cost the crusade three hundred, and the Commander's own reserved stores went into the second wagon."),
    ("Melazmera yielded her hunting approach for the two convoy passages.",
     "For two passages Melazmera kept her claws off the wagons on the ridge. She told it afterwards as the greatest sacrifice of the war."),
    ("Hepzamirah sent both hired guards on the longer escort, leaving her door unguarded.",
     "Hepzamirah had sent both her hired guards the long way round and left her own door bare. Melazmera knew exactly how long it had stood open."),
)
for _old, _new in LAST_CALL:
    retext(LC, "page", "{n}" + _old + "{/n}", "{n}" + _new + "{/n}")
add(LC, "page",
    p('''{n}She had told the Commander she would wait at the end of the grey lady's line. When the world buried the Commander, the pickets on the north road saw her go up over the city in the night, very high, toward wherever it is the dead go, and she did not come back for a long time.{/n}''',
      requires=("lastcall.dead_on_record", M + "beat.soul_refused")),
    p('''{n}The Commander had promised her the soul once, and lied. When the world buried the Commander, she came to collect it anyway, and lay on the cathedral roof waiting for it to come out.{/n}''',
      requires=("lastcall.dead_on_record", M + "beat.soul_lied")),
)


def _pages(payload):
    return {s["Id"]: s for s in payload["Scenes"] if s["Id"].startswith(("melazmera.",))}


def _node(pages, sid, nid):
    matches = [n for n in pages[sid]["Nodes"] if n["Id"] == nid]
    if len(matches) != 1:
        raise KeyError("melazmera cloud: %s/%s matched %d nodes" % (sid, nid, len(matches)))
    return matches[0]


def integrate(payload):
    pages = _pages(payload)
    for (sid, nid), body in NODES.items():
        _node(pages, sid, nid)["Text"] = body.strip()
    for (sid, nid), pairs in RETEXT.items():
        node = _node(pages, sid, nid)
        for old, new in pairs:
            # COMMON paragraph dicts are shared between the epilogue pages, so a
            # paragraph may already carry the new text from an earlier page.
            hits = [para for para in node.get("Paragraphs", []) if para["Text"] in (old, new)]
            if not hits:
                raise KeyError("melazmera cloud: paragraph not found at %s/%s: %s" % (sid, nid, old[:60]))
            for para in hits:
                para["Text"] = new
    for (sid, nid), paras in PARAS.items():
        node = _node(pages, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in paras]
    touched = {key[0] for key in NODES} | {key[0] for key in PARAS} | {key[0] for key in RETEXT}
    for sid in touched:
        for node in pages[sid]["Nodes"]:
            texts = [node["Text"]] + [a["Text"] for a in node["Choices"]] + [
                para["Text"] for para in node.get("Paragraphs", [])]
            if any(PENDING in t for t in texts):
                raise ValueError("melazmera cloud: prose still pending at %s/%s" % (sid, node["Id"]))
    # Structural history selection must follow all late prose transformations.
    from storylines.melazmera_trickster import integrate_meeting_history
    integrate_meeting_history(payload)
