"""Herrax on the Trickster path: "The coup on her schedule" (Writer/handoffs/trickster/herrax.md for the canon research; the
binding plan is 11-ROSTER-PLAN-2 §2, Herrax block and build sheet, rewritten 2026-09-29 after Astra design review r3; it
supersedes the spec's scar appraisal).

Canon (Herraxa_dialogue b1a346ae, c4/TenThousandDelights):
- a ChaoticEvil succubus (Herraxa 9da37b67) with "a jagged scar ... cutting through her scarlet sensual lips", a blind left
  eye "surrounded by wounds from some caustic substance" and wings that are "tattered rags" (Cue_0001 1439d338); madam once
  ChivarroRemovedFormPower (065b6117) plays; "you can consider me in your debt", with her Golden Coin (Cue_0300 044dc44d,
  TenThousandDelightsArk_Mark 1d5570f0): "every arch will recognize you as my favored guest and teleport you here"
  (Cue_0063 68082e7d);
- her scars: "a reminder for others ... Now the smug scum will think twice before challenging my authority" (Cue_0064
  aeac18f3); "As the keeper of this place, I am beyond anyone's reach. That's my role." (Cue_0097 661508b5); "I inherited
  her riches, but not her debts." (Cue_0070 2aba385a); the aasimar "are an asset" (Cue_0315 fdbce4a3); "a small labyrinth
  dedicated to hedonism" (Cue_0025 31a7cb93); the "forgotten" rings "cut off a dead body along with the fingers" (Cue_0052
  d6955c2a);
- Rokhorn (25ad116e), her incubus, summoned from her own list (Answer_0087 -> AnswersList_0152 571f3167): asked why he obeys
  her (Answer_0187 c60613dc) he admits "Seize power? Well, I did try..." and that he paid healers to restore his face; "she
  keeps them to remind us what we looked like after she finished with us" (Cue_0192 3b1d8220); his patron Willodus, the
  Lady in Shadow's court magician, "no longer visits here" (Cue_0299 2e9aa440); he claws a guest's cheek to read a fate
  (Cue_0193 37ffd2b3); "Hello, hot stuff." (Cue_0150 d8c5d002).

Device (a con, earned in two native dialogues, no magic, no document): told that Rokhorn still wants her chair, Herrax sets
the night; the Commander sells it to him on his own list ("alone, on the private floor") and hands over her coin. The coin
does what canon says (any arch sets its bearer down under the Delights' own arch, Cue_0063, the PortalArk); past that, her
girls on the arch take a favoured guest up the back stair to her rooms, which is her house's custom (authored, hers), and
tonight they are hers. Every checkable detail is true except who will be waiting. A
failed Bluff plays out in public: he claws the Commander's cheek, reads the lie, tells the house her floor was offered, and
she cuts him anyway, before everyone. "Alone" is the lie told to Rokhorn about her guards; no partner is kept away and no
other route's state is read, so the night plays the same with every romance open.
The night is the pivotal moral node: cut him yourself (Evil), hand the knife back, or stay her hand (Good: her refusal,
"You took my knife in my own hall", answered only by the knife returned hilt-first before the Sinners).
Cost: her coin is lost either way (native item removed: the arches stop carrying the Commander to her).
Commit: she proposes, with no test. At closing she offers what her role forbids (Cue_0097): being reachable, by one person.
The courtship around the chain lives in herrax_house.
"""
from copy import deepcopy

from story_format import c, n, p, reaction, scene

SCENES = []
REL = "herrax"
H = "herrax.trickster."

HUB = "43f93812d6216c94db356622859397f1"        # Herraxa_dialogue/AnswersList_0004 (her hub)
RET = "1af69c65d15cc8949a4fe47a45c4f85d"        # Cue_0100 "Don't know where to look first? ... We have some true gems here."
ROK_LIST = "571f316720b8d164b819495959222919"   # Herraxa_dialogue/AnswersList_0152 (Rokhorn, summoned by Answer_0087)
ROK_RET = "e7d43c3ec7ab16444be9759414f48436"    # Cue_0159 "Let stupid vavakia fight in the arena..." (answers only 0152)
ROK_UNIT = "25ad116e1f5008e488b13f9b968596d4"   # Rokhorn.jbp (male incubus, ChaoticEvil)
COIN = "1d5570f0d0d2b7b4ba805d48f492a749"       # TenThousandDelightsArk_Mark, "Herrax's Golden Coin"

STARTED = "herrax.started"
CLOSED = "herrax.closed"
COMMITTED = "herrax.committed"
# Native keys (her own dialog; bound in integrate() or by trickster_world).
MADAM = "herrax.madam"                          # Etudes ChivarroRemovedFormPower (Chapter 4 only)
MET = "herrax.met"                              # SeenCues Cue_0300 (first meeting as madam; the coin)
CONFESSED = "herrax.rokhorn_confessed"          # SelectedAnswers Answer_0187 (Rokhorn: "Seize power? Well, I did try...")
CLIENT = "herrax.rokhorn_client"                # SelectedAnswers Answer_0157 ([Pay four thousand gold coins] his night)
COIN_HELD = "herrax.coin_held"                  # InventoryItems TenThousandDelightsArk_Mark
WILLODUS = "herrax.willodus_told"               # SeenCues Cue_0299 (node variant only)
ASKED_KILL = "herrax.asked_kill_chivarro"       # SeenCues Cue_0045_KillChivarro (trickster_world)
TOLD_DEAD = "herrax.told_chivarro_dead"         # SelectedAnswers Answer_0046 (the Commander's "Chivarro is dead.")
HAGGLED = "herrax.haggled"                      # Etudes HerraxaSlaveHaggling (node variant, Chapter 4 only)
SENT = "herrax.aasimars_sent"                   # SelectedAnswers MeatSlaver_dialogue/Answer_0039 2bfaec78: the Commander sent
                                                # Dyunk's aasimar girls "to the Ten Thousand Delights" (starts AasimarsBrothel)

# The chain.
PRIMED = H + "primed"                           # she set the night; the Commander agreed to sell it
BAIT = H + "bait_taken"                         # Rokhorn bought the night and took the coin
BLOWN = H + "cost.con_blown"                    # the Bluff failed; the house heard her floor was offered
CHEEK = H + "cost.clawed_cheek"                 # Rokhorn read the lie in the Commander's blood (Cue_0193's claw)
COIN_LOST = H + "cost.coin_lost"                # her coin gone: sold to him, or handed back before the house
COIN_BACK = H + "coin_handed_back"
LESSON = H + "lesson_given"
KNIFE_TAKEN = H + "knife_taken"                 # the Commander made the cut (Evil)
HANDED = H + "knife_handed_back"
DECLINED = H + "declined"                       # the Commander stayed her hand (Good): her refusal
RESTORED = H + "knife_restored"                 # the knife returned hilt-first before the Sinners
MORNING = H + "morning_served"                  # Rokhorn, stitched, served the breakfast
PROMISED = H + "promised"                       # a Chapter 5 promise to come back and sell the night in person
LATE_COMMITTED = H + "late_committed"
# The lie the Commander rehearsed with her (herrax_house.rehearsal); read by the sale.
LIE_GREED = H + "lie.greed"
LIE_SPITE = H + "lie.spite"
LIE_HUNGER = H + "lie.hunger"
# The unfinished contract on Chivarro (ledger 05 row 13): one discovery, hers.
CONTRACT = H + "cost.contract_unfinished"
KEPT_OUT = H + "contract.kept_out"
STOOD = H + "contract.stood_by_her"
# Cross-route reads (minagho_chivarro; node variants only, except chivarro_seen, which ledger 13 allowlists).
MC = "minagho_chivarro.trickster."
MC_REUNITED = MC + "reunited"
MC_RETURNED = MC + "returned_chivarro"
MC_DEPOSIT = MC + "chivarro_deposit"
MC_FAVOR = MC + "cost.herrax_favor"
MC_OWNED = MC + "chivarro_owned"

SELECTED_ANSWERS = {CONFESSED: "c60613dca14bf0943a428246cf51bb3a", CLIENT: "33447e2dcba529f4ba678688db744411",
                    SENT: "2bfaec7837a9a4a40a43e73f06b3cf51"}
SEEN_CUES = {WILLODUS: ["2e9aa440f006fc44ba3e34bf1a28de91"],
             "herrax.sermon_heard": ["2948da80165901a4ea1078f5ec441af3"],    # Cue_0321 (Arueshalae in her hall; variant)
             "herrax.sosiel_admired": ["e56632b9824273d4e89804db52ad7210"]}  # Cue_0303 (Sosiel on her scars; variant)
INVENTORY = {COIN_HELD: COIN}
# Native MorevetZeriexRoof/Answer_0009 e53587773fd446941ba4c53d6227ffa9
# starts MorevetKilled. No authored return overrides a deliberate kill.
MOREVET_DEAD = "herrax.morevet_dead"
ETUDES = {MOREVET_DEAD: "3e26a59ceb2d45a2afc05d35092ceb54"}

# Recovery: read-only native Nocticula_main/Cue_0022 dismissal; no authored audience.
SEEN_CUES[H + "palace_dismissed"] = ["30469883ce1583743a6b4228d24778bc"]

RELATIONSHIP = dict(
    Title="The keeper's night",
    Description=("Herrax keeps the Ten Thousand Delights, and keeps herself beyond anyone's reach. Her incubus still wants "
                 "her chair. She means to teach him otherwise, in front of the whole house, and she wants me to sell him "
                 "the lesson."),
    Objective="Sell Rokhorn her night",
    Guidance=("On the Trickster path, in Chapter 4, once Herrax rules the Ten Thousand Delights. Ask her incubus Rokhorn why "
              "he obeys her, keep the golden coin she gave you, and tell her what he still wants. If you left the Midnight Isles "
              "before it was finished, or never met her there, her courier will find you in Chapter 5."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[], FailureFlags=[], UnavailableOverrides={},
    TricksterAccess={
        "madam": dict(detect=[MADAM, MET, CONFESSED, COIN_HELD], device=H + "madam.schedule", returned=PRIMED),
        "not_started": dict(detect=["!" + PRIMED], device=H + "late.next_move", returned=PRIMED),
    },
)

DERIVED = {
    # R2-6: she was promised the night in Chapter 5, and the page after the Threshold answers it.
    LATE_COMMITTED: [["trickster.ever", PROMISED]],
    # 05 §2.5 voice note: she joins as the keeper; reachable by one person is her gift, never a demand on anyone else.
    "herrax.harem.voice.keeper": [[COMMITTED]],
}


def hx(id, text, *choices, **kw):
    """Herrax, inline in her own dialog (the native conversant)."""
    return n(id, "conversant", text, *choices, **kw)


def rk(id, text, *choices, **kw):
    """Rokhorn, inline: his own portrait and name on the cue (E14f)."""
    return n(id, "Rokhorn", text, *choices, speaker_unit=ROK_UNIT, **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def hl(id, text, *choices, **kw):
    """Herrax on paper (a rest-delivered page)."""
    return n(id, "Herrax", text, *choices, portrait="Herrax", **kw)


def rl(id, text, *choices, **kw):
    """Rokhorn, in person at the Commander's door (a rest-delivered page)."""
    return n(id, "Rokhorn", text, *choices, portrait="Rokhorn", **kw)


def hall(id, title, entry, nodes, requires, forbids=(), delay=24, optional=False, **extra):
    """A physical scene inline on her hub (Chapter 4): AnswersList_0004, back to Cue_0100."""
    SCENES.append(scene(id, title, "Herrax", 4, entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", MADAM, MET, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, *forbids))), delay=delay, last=4, optional=optional,
                        Relationship=REL, AnswerLists=[HUB], NativeReturnCue=RET, **extra))


def letter(id, title, nodes, requires, forbids=(), delay=0, kind="letter", chapter=5, optional=False, **extra):
    """A rest-delivered page: her letter, carried by Rokhorn, or Rokhorn himself at the Commander's door."""
    base = ("trickster.ever",) if "trickster" not in requires else ()
    SCENES.append(scene(id, title, "Herrax", chapter, "", nodes,
                        requires=tuple(dict.fromkeys((*base, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, *forbids))), delay=delay, last=chapter, optional=optional,
                        Relationship=REL, Remote=True, Kind=kind, Chapters=[chapter], **extra))


# --- 1. Her night (the setup): she sets it, the Commander agrees to sell it. ---------------------------------------------

hall(H + "madam.schedule", "Her chair", '"A word about Rokhorn."', [
    hx("start", '''{n}Herrax dismisses the girl pinning her hair with two fingers and turns her good eye on you. The blind one, milk-white in its ring of old burns, turns with it a moment later.{/n}
"Rokhorn? What has my boy done now, lover? Bitten a paying guest?" {n}She sounds delighted at the prospect.{/n} "He does that. They pay extra for it."''',
       c('[Tell her Rokhorn still wants her chair] "He told me how he tried for your chair and lost. He didn\'t tell it like a man who\'s done losing."',
         "chair", mythic="Trickster"),
       c('"Nothing. Forget I asked."', abort=True)),
    hx("chair", '''{n}Her good eye stays on you. Then she laughs, light and pleased, the laugh she keeps for news of other people's funerals.{/n}
"Of course he does. He's an incubus. He wants every chair he sits beside and every bed he's thrown out of. Wanting is his whole trade." {n}She touches the scar where it splits her lip, absently, the way another woman might touch a pearl.{/n}
"The difference, honey, is that he's started saying it to my guests. To you. That isn't wanting any more. That's recruiting."''',
       c('"He said your scars are there to remind the rest of them what he looked like when you were done."', "lesson"),
       c('"So what do you mean to do about it?"', "lesson")),
    hx("lesson", '''"They are. I left mine where everyone could see them, and every smug little climber in this house counts them on the way up the stairs and thinks twice." {n}Her mouth curls on the whole side of it.{/n}
"But Rokhorn paid the healers of three circles to put his pretty face back. He paid to forget. And a lesson you can buy your way out of isn't a lesson, lover. It's a rumour."
{n}She stands. The tattered wings behind her shift with a sound like old silk tearing.{/n}
"So. Let him come and sit in it. I pick the night. You sell it to him. I do the cutting, lover. Scars only teach when the right hand makes them."''',
       c('"Sell it to him how?"', "plan"),
       c('"Why me? You have a house full of liars."', "why")),
    hx("why", '''"I have a house full of liars he knows. He's watched every one of them lie to guests for years; he can smell my girls' perfume on a lie before it's out of their mouths." {n}She walks a slow circle round you.{/n}
"You're new. You're mortal, and mortals are greedy; everyone in Alushinyrra believes that. And you already rid this house of one madam. When the crusader who put Chivarro in the gutter comes to Rokhorn with a way to put me there too, he won't be listening for a lie. He'll be listening for his own name."''',
       c('"All right. How does it go?"', "plan")),
    hx("plan", '''"You go to him as a buyer. Not of his body; that's cheap. Of his ambition. You tell him I'll be alone on the private floor on the night I name, with my boys sent down to the arena for the crowd. You tell him you want a quarter of the house when he holds it."
"And you give him my coin." {n}Her eye drops to your belt, to the gold coin with its obscene little engraving, hanging where it has hung since the day she gave it to you.{/n}
"Every arch in the city knows it, and sets whoever carries it down under my arch, downstairs, as my favoured guest. My rooms are three locked doors past that, and the girls who keep the arch hold the keys. They take a favoured guest up the back stair at any hour and ask nothing. They take nobody else up. Not even my own incubus." {n}Her mouth curls.{/n} "He's watched them do it for Chivarro's pets for years, and wanted it every time. That is what makes it true, honey. Everything you tell him will be true, except which girl carries the keys that night, and who's waiting at the top."''',
       c('[Agree: her night, your sale, her knife] "Name the night."', "named", flags=(PRIMED, STARTED)),
       c('"Let me deal with him quietly. A knife in the dark, and your chair stays yours."', "quietly")),
    hx("quietly", '''"My house. My knife." {n}The warmth goes out of her face all at once, a lamp pinched out between two fingers.{/n}
"A quiet death teaches nobody anything, lover. A quiet death is a rumour too: the house says 'Rokhorn left', and next spring somebody else tries my chair to see if I made him leave. If you won't sell him my night, I'll find a worse liar who will. And I'll like you less."''',
       c("[Let it rest for now.]", abort=True)),
    hx("named", '''"The first arena night after he says yes. The arena crowd goes down to the Battlebliss after dark, and every guest who can walk goes with it." {n}She holds out a hand, palm up, and does not take the coin; she only looks at it, and then at you.{/n}
"Go to him when you like. He's on my list; ask for him as any guest would. Pay him for his night first, if you want him soft. He's always softest with people who've paid him."
"The coin goes with the sale, and you won't have it back. I don't give the same gift twice." {n}A beat.{/n} "And if he smells it on you, don't run. Running is how you tell a demon you were lying."''',
       c('"I don\'t run."'))],
    requires=("trickster", CONFESSED, COIN_HELD), forbids=(PRIMED,), delay=0,
    TricksterDevice=True, TricksterState="madam")


# --- 2. The sale, on Rokhorn's own list (a Bluff; failure plays out in public). -----------------------------------------

SALE_PITCH = ('[Bluff] "Because on the next arena night she\'ll be alone on the private floor, with her boys sent down to the '
              'arena. Here is her coin. Bring it to her arch after midnight and her girls will take you up the back stair '
              'as her favoured guest. I want a quarter of the house when you hold it."')

SCENES.append(scene(H + "madam.sell_the_night", "Her night, for sale", "Herrax", 4, '"Let\'s talk about business, not pleasure."', [
    rk("start", '''{n}Rokhorn stretches until his shoulders crack, and looks down at you with frank, bored appetite.{/n}
"Business, hot stuff? With me, business is pleasure. It just costs more, and I get to keep the marks." {n}He lounges against the pillar at his back.{/n} "Go on. What does a crusader want from an incubus, if it isn't the usual?"''',
       c('"You told me you tried for Herrax\'s chair once."', "wary", forbids=(CLIENT,)),
       c('"You told me you tried for Herrax\'s chair once."', "client", requires=(CLIENT,))),
    rk("client", '''{n}He looks you up and down, slowly, with the particular smile he keeps for people who have paid him.{/n}
"You. The one with the knees." {n}He sounds fond.{/n} "You paid my four thousand and took everything I gave you, which nobody believes when I tell them. A guest like that, I listen to. Once." {n}He glances at the stair, the couches, the door.{/n} "So. What's the crusader's business, if it isn't more of the same?"''',
       c("Continue", "wary")),
    rk("wary", '''"And lost. And paid. The healers who did my jaw still brag about it in the Upper City." {n}His smile doesn't move, but his eyes do: to the stair, to the girls at the far couch, to the door. Nobody is listening. He checks anyway.{/n}
"You say her name the way a man says the name of a horse he means to sell. Careful. In this house, walls have ears, and the ears are hers."''',
       c(SALE_PITCH, check=dict(Skill="CheckBluff", DC=28, Success="bait", Failure="blown"), forbids=(CLIENT, LIE_SPITE, LIE_HUNGER,)),
       c(SALE_PITCH, check=dict(Skill="CheckBluff", DC=23, Success="bait", Failure="blown"), requires=(CLIENT,), forbids=(LIE_SPITE, LIE_HUNGER,)),
       c('"Forget it. Just wondering."', abort=True),
       c('[Bluff] "She laughed at me in front of her girls. Let them laugh when you take her chair. Next arena night she\'ll be alone upstairs, her boys at the Battlebliss. Take her coin to the arch after midnight; her girls will bring you up the back stair. I want a quarter of the house when you hold it."', check=dict(Skill="CheckBluff", DC=28, Success="bait", Failure="blown"), requires=(LIE_SPITE,), forbids=(CLIENT,)),
       c('[Bluff] "She laughed at me in front of her girls. Let them laugh when you take her chair. Next arena night she\'ll be alone upstairs, her boys at the Battlebliss. Take her coin to the arch after midnight; her girls will bring you up the back stair. I want a quarter of the house when you hold it."', check=dict(Skill="CheckBluff", DC=23, Success="bait", Failure="blown"), requires=(LIE_SPITE, CLIENT,)),
       c('[Bluff] "I want Herrax. She won\'t sell. You will. Next arena night she\'ll be alone upstairs, her boys at the Battlebliss. Take her coin to the arch after midnight; her girls will bring you up the back stair. I want a quarter of the house when you hold it."', check=dict(Skill="CheckBluff", DC=28, Success="bait", Failure="blown"), requires=(LIE_HUNGER,), forbids=(LIE_SPITE, CLIENT,)),
       c('[Bluff] "I want Herrax. She won\'t sell. You will. Next arena night she\'ll be alone upstairs, her boys at the Battlebliss. Take her coin to the arch after midnight; her girls will bring you up the back stair. I want a quarter of the house when you hold it."', check=dict(Skill="CheckBluff", DC=23, Success="bait", Failure="blown"), requires=(LIE_HUNGER, CLIENT,), forbids=(LIE_SPITE,))),
    rk("bait", '''{n}He takes the coin between two claws and turns it to the lamplight. He bites it. He runs a thumb over the little engraving and snorts.{/n}
"Her coin. The real one." {n}He is quiet, and in the quiet you can watch him check every piece of what you told him, one by one, and find that every piece is true. The arena crowd. The private floor. The girls on the arch, who take the coin's bearer up and ask nothing. The crusader who put Chivarro in the gutter.{/n}''',
       c("Continue", "bait_greed", requires=(LIE_GREED,)),
       c("Continue", "bait_spite", requires=(LIE_SPITE,), forbids=(LIE_GREED,)),
       c("Continue", "bait_hunger", requires=(LIE_HUNGER,), forbids=(LIE_GREED, LIE_SPITE)),
       c("Continue", "bait_plain", forbids=(LIE_GREED, LIE_SPITE, LIE_HUNGER))),
    rk("bait_greed", '''"A quarter. You don't want her, you want the ledger." {n}He laughs, and it is a real laugh.{/n} "That, I believe. Mortals always want the ledger. You'll have your quarter, hot stuff, and I'll have the pleasure of watching you try to spend it in Alushinyrra."''',
       c("Continue", "bait_end")),
    rk("bait_spite", '''"She laughed at you." {n}He says it with enormous satisfaction, as if tasting it.{/n} "Of course she did. She laughs at everyone, and one day someone stops finding it charming. I know that feeling, hot stuff. I know how her laugh sounds when you're bleeding. Fine. You'll watch her face when I sit down."''',
       c("Continue", "bait_end")),
    rk("bait_hunger", '''"You want her under you and she won't sell. The keeper, beyond anyone's reach." {n}His grin is slow and wide.{/n} "When I hold the house, hot stuff, everything in it is for sale. Her included. I'll give you a discount. I'm generous with what isn't mine yet."''',
       c("Continue", "bait_end")),
    rk("bait_plain", '''"A quarter of the house, for a coin and a night." {n}He weighs it, and you can see him like the arithmetic.{/n} "Cheap, for you. Cheap for me. That's how you know a bargain in Alushinyrra: both sides think they robbed the other."''',
       c("Continue", "bait_end")),
    rk("bait_end", '''{n}He closes his fist on the coin. When he opens it again it is gone, somewhere under the belt of his loincloth.{/n}
"The next arena night, then. While her boys are down at the Battlebliss." {n}He rolls his neck.{/n} "Now go and look innocent somewhere, crusader. You're terrible at it."''',
       c("[Let him keep the coin.]", flags=(BAIT, COIN_LOST), remove_item=COIN, requires=(COIN_HELD,))),
    rk("blown", '''{n}His hand moves faster than your eye follows. A razor claw opens your cheek from the ear almost to the mouth, and before the sting arrives he is licking your blood off it, slowly, eyes half closed.{/n}
{n}His voice drops, low and strange, the voice he uses for reading fates.{/n} "I see a floor with nobody alone on it. I see a coin going back to the hand it came from. I see a knife that isn't mine." {n}His eyes open.{/n} "Oh, hot stuff. She sent you."''',
       c('"She didn\'t send me anywhere."', "loud"),
       c('[Say nothing, and touch your cheek.]', "loud")),
    rk("loud", '''{n}He doesn't answer you. He tips back his head and laughs at the ceiling, loud enough for the girls on the far couch, the boy at the stair and whoever stands behind the walls.{/n}
"Her floor is for sale! The favoured guest is selling the madam's floor!" {n}He spreads his arms.{/n} "Tell her I'm flattered. Tell her I'll be at her dais whenever she wants me. Let her bring the knife. I'll bring my healers."''',
       c("[Leave him laughing.]", flags=(BLOWN, CHEEK)))],
    requires=("trickster", PRIMED, COIN_HELD), forbids=(BAIT, BLOWN, CLOSED), delay=0, last=4, Relationship=REL,
    AnswerLists=[ROK_LIST], NativeReturnCue=ROK_RET))


# --- 3. The night (the pivotal moral node). --------------------------------------------------------------------------------

AFTER_CUT = (
    c("Continue", "coin_kept", requires=(BAIT,)),
    c("Continue", "coin_blown", requires=(BLOWN,), forbids=(BAIT,)),
    c("Continue", "coin_blown", forbids=(BAIT, BLOWN)),
)

hall(H + "madam.the_night", "The night", '"Is it time?"', [
    hx("start", '''{n}Herrax is already dressed for it: black silk to the throat, her hair pinned high to show every scar, a thin curved knife at her hip in a sheath of worked bone. She looks you over the way she looks over stock.{/n}
"It's time, lover. Come and stand where I tell you, and don't stand anywhere else."''',
       c("Continue", "arch", requires=(BAIT,)),
       c("Continue", "hall", requires=(BLOWN,), forbids=(BAIT,))),
    nar("arch", '''{n}Her rooms are at the heart of the labyrinth, three doors past any door a guest has seen. Tonight every lamp in them is out. The house lines the walls in the dark: the three Sinners, arm in arm; Morevet Honeyed Tongue with her lips parted; the Mad Glowworm cross-legged on a sideboard; a dozen of the boys with knives and no shirts. Nobody whispers.{/n}
{n}Herrax sits in the one chair at the far end, with her curved knife across her knees.{/n}
{n}Near midnight a lamp moves on the back stair. The girl who keeps the arch comes up it with her ring of keys, opening the three doors one after another, as she has opened them for favoured guests since Chivarro's time, and Rokhorn climbs behind her with the madam's coin hanging on his belt and his best smile already on. At the last door the girl steps aside to let him pass, and closes it behind him, and turns the key. The lamps come up all at once. The smile stays where it is for a heartbeat too long.{/n}''',
       c("Continue", "arch2")),
    nar("arch2", '''{n}Four of the boys have him on his knees before he gets his claws out. He doesn't struggle long. He looks round the room at every face that has come to watch him, and last of all at you, and he laughs, because there is nothing else left to do with his mouth.{/n}
"Hot stuff," {n}he says.{/n} "Every word of it was true."''',
       c("Continue", "arch3")),
    hx("arch3", '''{n}Herrax comes down one step from the dais, no more. Her voice is warm, and carries to every wall.{/n}
"You bought my night, sweet. You paid with my own coin, and you came up my own stair behind my own girl, because a stranger told you I'd be alone." {n}She tilts her head.{/n} "The coin brought you home. My girl opened every door she promised to open. You bought the part about being alone from someone who doesn't even work here." {n}She glances at you, amused.{/n} "Next time, sweet, ask what else comes with the room."
{n}Rokhorn says nothing. There is nothing he could say in this room that would not be bought and sold by morning, and he knows it.{/n}
{n}She nods to the boys. They walk him down through all three doors and the long stair into the great hall, where the lamps are lit and every guest still awake has been waiting, and they put him on his knees at the foot of Chivarro's old dais. Herrax climbs it and sits on the cushions, which still smell of the other woman's perfume.{/n}''',
       c("Continue", "knife")),
    nar("hall", '''{n}She does it in the great hall, under the lamps, where every guest and girl and boy in the Delights can see. Rokhorn is already on his knees at the foot of the old dais, held by four of the boys. Nobody has hurt him yet. They are saving it.{/n}
{n}Every head turns when you come in, and every eye goes to the claw mark on your cheek. The whole house heard what he shouted: the favoured guest offered the madam's floor. Herrax lets them look at you for as long as it takes to be sure they have.{/n}''',
       c("Continue", "hall_coin")),
    hx("hall_coin", '''"My favourite guest offered my floor to my incubus, and botched the sale, and let him shout it from the couches." {n}Her voice carries without being raised.{/n} "The whole house knows. So the whole house will watch what you give back to me. Come here."''',
       c("[Walk the length of the hall and give her back her coin, before the house.]", "hall_coin_given",
         flags=(COIN_BACK, COIN_LOST), remove_item=COIN, requires=(COIN_HELD,)),
       c("[Show her your empty hands. The coin is gone.]", "hall_no_coin", forbids=(COIN_HELD,))),
    hx("hall_coin_given", '''{n}She takes it off your palm without touching your skin and holds it up, so the lamps catch the gold and every eye in the hall follows it.{/n}
"Lent against me. Returned in public." {n}She closes her hand on it.{/n} "Now they all know whose hand it goes back to."''',
       c("Continue", "knife")),
    hx("hall_no_coin", '''{n}She looks at your empty hands and then, slowly, at your face.{/n} "Not on you. My gift. Tucked away somewhere safe, perhaps? Or in a stranger's pocket?" {n}She lets the house hear every word.{/n} "Empty hands, then. They'll watch what you do with mine."''',
       c("Continue", "knife")),
    hx("knife", '''{n}She stands, and draws the curved knife, and holds it out to you across the dais, hilt first. The house holds its breath.{/n}
"You sold him. The seller has the right of the first cut; that's the custom of this house, and I made the custom." {n}Her good eye does not leave yours.{/n} "Lip to cheekbone, where he paid to have his made smooth. So he remembers, every time he smiles at a guest, who made the lesson."
"Everyone is watching, lover. Choose where you stand."''',
       c("[Cut him yourself.]", "cut_you", alignment=("Evil", 1), flags=(LESSON, KNIFE_TAKEN)),
       c("[Hand it back to her.]", "cut_her", flags=(LESSON, HANDED)),
       c("[Stay her hand.]", "stayed", alignment=("Good", 1), flags=(LESSON, DECLINED))),
    nar("cut_you", '''{n}Rokhorn doesn't beg. You'll give him that. He holds his head up for it, and the boys hold it steady for you, and the knife is so sharp that the first part of the cut costs almost nothing: a line of cold, lip to cheekbone, and then the blood arrives all at once.{/n}
{n}He makes a sound through his teeth that everyone in the hall will remember. Herrax watches your hand, not his face, the whole time.{/n}''',
       c("Continue", "cut_you2")),
    hx("cut_you2", '''"Clean," {n}she says to the room, as if appraising a stone.{/n} "Clean, and not one hair deeper than I asked. Did you all see? That's a hand that does what it's told and means it."
{n}She takes the knife back from you and wipes it on Rokhorn's own hair.{/n} "No healers. Not in this circle, not in the next. Anyone who puts a spell on that face answers to me, and I'll give them one to match."''',
       *AFTER_CUT),
    nar("cut_her", '''{n}You turn the knife in your hand and give it back to her the way she gave it: hilt first. Something passes over her face, too quick to name.{/n}
{n}Then she steps down from the dais, takes Rokhorn by the jaw like a lover and opens his face from lip to cheekbone in one unhurried stroke. He screams. She lets him. When he is done she wipes the blade on his hair.{/n}''',
       c("Continue", "cut_her2")),
    hx("cut_her2", '''"There." {n}She says it to the house.{/n} "Now his face remembers what his purse forgot. No healers, not in this circle nor the next. Anyone who puts a spell on it answers to me."
{n}To you, lower, while the boys drag him out:{/n} "You gave the knife back. Most people keep a knife they're handed, lover. They can't help it."''',
       *AFTER_CUT),
    nar("stayed", '''{n}She takes the knife back from you, since you do not use it, and steps down to Rokhorn with it raised, and your hand closes on her wrist.{/n}
{n}The hall goes silent the way a hall goes silent before a fight. Along the walls a dozen of her boys have come off the plaster with their knives out, and one word from her would bring every one of them down on you; half the house is waiting to hear her say it. She doesn't say it. She looks at your hand on her wrist, in her own hall, in front of everyone.{/n}
{n}Then she opens her fingers, and the knife drops into your palm.{/n}''',
       c("Continue", "stayed2")),
    hx("stayed2", '''"Let him go." {n}The boys let him go. Rokhorn gets up with his face whole and doesn't laugh; he's not fool enough to laugh now. He goes out of the hall fast.{/n}
{n}Herrax turns to you. Her voice is very quiet, and every soul in the hall hears it.{/n}
"You took my knife in my own hall." {n}She looks at it in your hand.{/n} "Keep it. You've earned the right to carry it; you've earned nothing else. Get out of my sight."''',
       c("Continue", "stayed_coin", requires=(BAIT,)),
       c("[Go.]", forbids=(BAIT,))),
    hx("stayed_coin", '''{n}On your way out she calls after you, and you turn. She is holding up her gold coin, taken off Rokhorn's belt while he fled.{/n} "Lent against me. It stays with me." {n}She drops it into the bodice of her gown.{/n} "That's the one thing tonight that went where I meant it to."''',
       c("[Go.]")),
    hx("coin_kept", '''{n}When they have dragged him out, she stoops to the tiles where he knelt and picks up her coin. It came off his belt in the struggle. She turns it in the lamplight, blood on the gold.{/n}
"Lent against me. It stays with me." {n}She drops it into her bodice, and looks at you.{/n} "The arches won't carry you to me any more, lover. From now on you walk up my stairs like everyone else. See how you like it."''',
       c('"I\'ll like the stairs."')),
    hx("coin_blown", '''{n}The house breaks up slowly, in knots, whispering. She lets them. They'll carry it to every house in the Upper City by morning, and that is the point.{/n}
"You nearly cost me my floor, lover." {n}She turns the knife over in her fingers, clean now, and lays it across her knee.{/n} "And then you stood where I told you and paid for it in front of them. I'll have to think about which of those I remember."''',
       c('"Think about it."'))],
    requires=(), forbids=(LESSON,), delay=24, RequiresAnyGroups=[[BAIT, BLOWN]])


# --- 4. Closing: she proposes (no test). The yes, the dais, the cut, and the morning. ------------------------------------

def _intimacy(scene_id):
    """The yes, shared by both closings: desire, the threshold on Chivarro's old dais, the cut, the morning after."""
    return [
        hx("desire", '''{n}She doesn't smile at the word. She takes it the way she takes coin across the bar: weighs it, tests it, and puts it away somewhere nobody else will find it.{/n}
"Then come here." {n}She sits on the edge of the dais and draws you in by the belt, her claws hooked through it, until you are standing close enough to feel her breath. She tips her face up to the lamp, so that the scar runs bright from her cheekbone down through her mouth.{/n}
"Touch it. Everyone else pays not to."''',
           c("[Trace the scar with your thumb, down through her lip.]", "thumb"),
           c("[Kiss the seam in her lip.]", "kiss")),
        nar("thumb", '''{n}The old wound is ridged and smooth at once, like wax that cooled too fast. Where it splits her lower lip there is a seam, and when your thumb finds it her mouth opens under it, warm, and her tongue touches the pad of your thumb as if tasting a coin for gold. Her good eye stays open the whole time. So does the blind one.{/n}''',
           c("Continue", "threshold")),
        nar("kiss", '''{n}You find the seam with your mouth. It is ridged and smooth at once, like wax that cooled too fast, and she lets you learn the whole length of it before she opens her lips and kisses you back, slow, the way a jeweller turns a stone to see where it catches the light. She breathes in through the kiss, and you feel the breath go all the way down her, and something of yours go with it.{/n}''',
           c("Continue", "threshold")),
        nar("threshold", '''{n}She works the buckles of your armour loose without looking at them, one after another, as if she has undone a thousand, which she has. Each piece goes down on the tiles beside Rokhorn's dried blood with a sound that carries through the empty hall. The lamps are all still lit. She wants them lit.{/n}
{n}Her own gown has one clasp, at the throat. She puts your hand on it and waits.{/n}''',
           c("[Open the clasp.]", "threshold2")),
        nar("threshold2", '''{n}Black silk goes down her shoulders like water off a blade. Under it her body is flawless, the way a succubus's body is flawless, until the scars begin: the burn that ate her left eye runs its fingers down her neck, and old claw furrows cross her ribs where somebody once tried to open her. She lets you see all of it. She watches you see it.{/n}
{n}Behind her the tattered wings spread, rags of skin between long bones, and close around the two of you like a cloak with holes in it.{/n}
"You feel it?" {n}Her mouth is at your throat, and something is going out of you with each breath into her: warmth, a little strength, a thread of your life drawn off as lightly as a pickpocket's fingers.{/n} "We take a little more than we give, honey. It's our nature. I'll stop before you do."''',
           c('"You\'d better."', "cut"),
           c('"Take what you like."', "cut")),
        nar("cut", '''{n}She laughs against your skin, low, and her claws come out of your belt and into the small of your back. She pulls you down onto Chivarro's old cushions, into the smell of another woman's perfume, and rolls you under her. The lamps burn on over the empty hall.{/n}
{n}She is bare and hot and unashamed, every scar lit gold, the ragged wings pulled close around the two of you. She drags your hands to her hips, claws first and then palms, and holds them there only to watch your face change, as a madam samples a vintage before she decides what it will cost.{/n}
"Don't you look away, honey. Nobody gets this and a view of the ceiling." {n}Her hand finds the last of your buckles and breaks it.{/n}''',
           c("Continue", scene_id + ".explicit.1")),
        nar("morning", '''{n}You wake on the dais with the lamps burnt out and the grey light of the Isles coming down through the high windows. Somebody has put a fur over you. Herrax is sitting up beside you with her hair unpinned, eating a fig and reading the night's takings.{/n}
{n}Rokhorn brings the breakfast. He carries the tray up the dais steps himself, as she ordered, in front of the girls clearing the hall. The new wound on his face is sewn shut with black thread in a row of neat, ugly stitches, and it pulls when he moves his mouth. "Anything else, hot stuff?" His eyes meet yours over the tray. Herrax takes a fig. "You can start by looking pleased."{/n}
{n}He sets the tray down by your knee. He looks at neither of you.{/n}''',
           c("Continue", "morning2", flags=(MORNING,))),
        hx("morning2", '''"Thank you, Rokhorn." {n}She says it pleasantly. He goes back down the steps. Every girl in the hall watched him do it, and every one of them will tell it before noon.{/n}
"The whole house knows where you slept, lover. I made sure." {n}She tears the fig in half and gives you the larger piece.{/n} "It's good for business. And it's good for them to learn there's one person in the Delights who comes up my stairs without paying."
"You aren't paying for tonight. Your people are still paying for breakfast. Tell the next little bastard who asks for your rate." {n}She brushes a crumb from your mouth with her thumb.{/n} "Go back to your crusade when you like. Nobody will stop you at my door again."''',
           c('"I\'ll be back."'),
           c('"Not yet. The crusade can wait an hour."')),
        # Explicit brief: private first night; her unpaid guest, lit hall, no witnesses.
        nar(scene_id + ".explicit.1", ("{n}She draws you against her, the returned knife laid beyond the cushions, and kisses you until the hall falls quiet. She takes a little warmth from you, a little strength, and does not pretend it is anything but appetite; her ragged wings close round the two of you, and her laugh, when it comes, is hoarse and pleased.{/n}" if scene_id.endswith("reachable_restored") else "{n}Herrax draws you down against the cushions and takes your mouth, and the hall, the lamps and Rokhorn's dried blood go away. She takes a little more than she gives, as promised, and the warmth leaves you in long pulls that leave you dizzy and glad of it; her wings close round you both, and when she laughs at last it is ragged against your ear.{/n}"),
            c("Continue", "morning")),
    ]


def _variants(prefix):
    """Her regard, by what the Commander did at the night."""
    return (
        c("Continue", prefix + "cut_bait", requires=(KNIFE_TAKEN, BAIT)),
        c("Continue", prefix + "cut_blown", requires=(KNIFE_TAKEN, BLOWN), forbids=(BAIT,)),
        c("Continue", prefix + "handed_bait", requires=(HANDED, BAIT), forbids=(KNIFE_TAKEN,)),
        c("Continue", prefix + "handed_blown", requires=(HANDED, BLOWN, COIN_BACK), forbids=(KNIFE_TAKEN, BAIT)),
        c("Continue", prefix + "offer", forbids=(KNIFE_TAKEN, HANDED)),
        c("Continue", prefix + "offer", forbids=(BAIT, BLOWN)),
        c("Continue", prefix + "handed_blown_no_coin", requires=(HANDED, BLOWN), forbids=(KNIFE_TAKEN, BAIT, COIN_BACK)),
    )


OFFER_CHOICES = (
    c('"Yes. By me."', "desire", flags=(COMMITTED,)),
    c('"No. Stay out of reach."', "no", flags=(CLOSED,)),
)

hall(H + "madam.reachable", "At closing", '"The house is closing."', [
    hx("closing", '''{n}The last guest has gone down the stairs. The girls have cleared the cups and the boys have barred the street doors, and the great hall of the Delights is empty except for the two of you and the lamps, which she has not let anyone put out.{/n}
{n}Rokhorn's blood is still on the tiles below the dais, gone brown in the grout. She told the girls not to scrub it.{/n}
"Sit, lover. Not there. Here, on the step." {n}She sits above you on the dais, one bare foot on the step beside your hand.{/n}''',
       *_variants("")),
    hx("cut_bait", '''"He came up my back stair with my coin on his belt, and every word you'd told him was true, and then you took my knife and cut exactly where I told you." {n}She turns her head so the lamp finds her own scar.{/n} "Do you know how rare that is? A hand that does what it's told, and does it well, and doesn't shake afterwards. I've bought a great many hands. Never one like that."''',
       c("Continue", "offer")),
    hx("cut_blown", '''"You botched the sale. He laughed it all over my house." {n}She says it without heat.{/n} "And then you walked the length of my hall under their eyes, and took my knife, and cut clean. They've stopped talking about the sale, lover. They talk about the cut now. That's a thing I can respect: a mess, paid for in public, in full."''',
       c("Continue", "offer")),
    hx("handed_bait", '''"He came up my back stair with my coin, and every word you'd told him was true. And when I gave you the knife, you gave it back to me. Hilt first." {n}She is quiet a while.{/n} "Everyone keeps a knife they're handed in this house, lover. Everyone. You gave me my lesson back to make myself. I haven't decided if that was manners or cunning. I like it either way."''',
       c("Continue", "offer")),
    hx("handed_blown", '''"You botched the sale, and he laughed it all over my house. And then you walked the length of my hall and paid for it before all of them, and when I held out my knife you gave that back too." {n}She turns the knife over on her knee.{/n} "Twice in one night, the favoured guest put what was mine back in my hand where the house could see. They've stopped calling it a botch. They call it a tribute."''',
       c("Continue", "offer")),
    hx("offer", '''{n}She leans back on her hands.{/n}
"I've told kings and demons and half the Upper City the same thing, lover: the keeper of this place is beyond anyone's reach. That's my role. Anything in this house can be bought, and everyone in it, except me. It's the whole reason they keep coming up my stairs."
{n}She looks down at you on the step, and for once there is no price anywhere in her face.{/n}
"So here is something nobody has ever been offered. I'll be reachable. By one person. You can come to me without a coin, without an arch and without paying, and I'll be there, and I won't be for sale to you. You'll have to reach." {n}A beat.{/n} "That's all. Yes, or go down my stairs like anybody else."''',
       *OFFER_CHOICES),
    *_intimacy(H + "madam.reachable"),
    hx("handed_blown_no_coin", '"He shouted your lie off every couch. Then you walked into my hall with his claw across your cheek, took my knife and turned it hilt first." {n}She balances the blade across her palm.{/n} "That part they saw. That part I liked."', c("Continue", "offer")),
    hx("no", '''{n}She nods, as if you'd told her the price of wine had gone up.{/n}
"Then go down my stairs like anybody else." {n}She is already standing, already turning to the lamps.{/n} "You'll be welcome in my house, lover. You'll pay at the door."''',
       c("[Go down the stairs.]"))],
    requires=(LESSON,), forbids=(DECLINED, COMMITTED), delay=24)


# --- 5. Her refusal, and the way back: the knife, hilt first, before the Sinners. --------------------------------------

hall(H + "madam.hilt_first", "Hilt first", '"I brought your knife back."', [
    hx("start", '''{n}The bone sheath at Herrax's hip is empty. She has not replaced the knife. Every girl in the house has noticed, and every girl knows why.{/n}
{n}She looks at the knife in your hand and makes no move to take it.{/n}
"Not here, lover. Not quietly across the bar, where you can pretend it was a favour." {n}She nods at the great hall, where the three Sinners are lounging on the stair under the lamps, bored, beautiful and listening.{/n} "You took it in front of my house. Give it back in front of them."''',
       c("[Return her knife, hilt first, before the Sinners.]", "returned", flags=(RESTORED,)),
       c('"Another time."', abort=True)),
    nar("returned", '''{n}You walk out into the hall and stop at the foot of the stair, where the Sinners can see your face and she can see your hands. You turn the knife and hold it out to her, hilt first, the way she held it out to you on the night.{/n}
{n}The Sinners stop talking. One of them sits up. Herrax comes down the stair at her own pace and stands in front of you until the whole room is sure what it is watching. Then she takes the hilt.{/n}''',
       c("Continue", "returned2")),
    hx("returned2", '''{n}She slides it home in the bone sheath at her hip without looking.{/n}
"There." {n}To the Sinners, lightly:{/n} "Tell everyone. The favoured guest returns what belongs to the house."
{n}Then, to you, lower:{/n} "Rokhorn keeps his face until the house gathers. Then they watch me put right what you stopped, and you'll stand at the back and watch too." {n}Her good eye holds yours.{/n} "After that, I'll decide about you. Not before."''',
       c('"Decide, then."'))],
    requires=(DECLINED,), forbids=(RESTORED,), delay=24)

hall(H + "madam.reachable_restored", "At closing", '"The house is closing."', [
    hx("closing", '''{n}You watched her cut Rokhorn under the lamps, from the back of the hall. His blood is still in the grout below the dais; she told the girls not to scrub it. Now the hall is empty, and she has let the lamps burn.{/n}
"Sit, lover. On the step."''',
       c("Continue", "restored")),
    hx("restored", '''"You caught my wrist in my own hall. No one has done that since the night I took this chair." {n}She touches the knife at her hip.{/n} "I wanted to open your face for it. Half the house wanted me to. And then you walked out in front of the Sinners and gave it back, hilt first, knowing every one of them would tell it."
"A demon doesn't do that, lover. A demon keeps what it takes. So I've been sitting up here with it, deciding what you are." {n}She tilts her head.{/n} "I haven't finished. But I've decided what I'll offer."''',
       c("Continue", "offer")),
    hx("offer", '''{n}She leans back on her hands.{/n}
"The keeper of this place is beyond anyone's reach; that's my role. I've said it to kings and to demons, and I meant it every time. Anything in this house can be bought, and anyone in it, except me."
"So here is what nobody has ever been offered. I'll be reachable. By one person. No coin, no arch, no fee, and I won't be for sale to you. You'll have to reach, and you'll have to keep your hands off my knife while you do it." {n}The corner of her mouth moves.{/n} "Yes, or go down my stairs like anybody else."''',
       *OFFER_CHOICES),
    *_intimacy(H + "madam.reachable_restored"),
    hx("no", '''"Then go down my stairs like anybody else." {n}She says it lightly, and her hand stays on the knife until you're gone.{/n} "You'll be welcome in my house. You'll pay at the door."''',
       c("[Go down the stairs.]"))],
    requires=(RESTORED, "herrax.house.a_night_late"), forbids=(COMMITTED,), delay=24)


# --- 6. Chapter 5 fallbacks: her courier finds the Commander (one of the two, never both). ------------------------------

# Ledger 05 row 13 (the one discovery), folded into the one Chapter 5 letter so it never needs a second page: at the door,
# Rokhorn sees the woman Herrax asked the Commander to finish (Cue_0045_KillChivarro) alive in the Commander's hall. The
# reads are choice-level (node variants), as the ledger allows; the answer is the Commander's, and Herrax's reply follows.
def discovery_entry(prefix=""):
    return (
        c('"What are you staring at?"', prefix + "chiv", requires=(ASKED_KILL, MC_REUNITED, "chivarro.present_now"), forbids=(CONTRACT, MC_DEPOSIT, MC_FAVOR)),
        c('"What are you staring at?"', prefix + "chiv", requires=(ASKED_KILL, MC_RETURNED, "chivarro.present_now"),
          forbids=(CONTRACT, MC_DEPOSIT, MC_FAVOR, MC_REUNITED)),
    )


DISCOVERY_ENTRY = discovery_entry()


def discovery(prefix="", next=None):
    return [
        rl(prefix + "chiv", '''{n}He isn't looking at you. He is looking past your shoulder, into the hall, where a lilitu in borrowed wool sits at your table with a cup of your wine, and his smile has gone very still.{/n}
"Well, well. Chivarro." {n}He says it softly, like a man who has found a coin in the gutter.{/n} "My mistress asked you for that one, hot stuff. 'Can you take care of her for me, my love?' I was standing behind the dais when she said it. And here she is, taken care of, drinking your wine."
"She'll want to know what you meant by it. I carry answers. Choose yours."''',
           c('"Tell her Chivarro stays out of her house and out of her business. She has my word."', prefix + "chiv_kept",
             flags=(CONTRACT, KEPT_OUT)),
           c('"Tell her Chivarro goes where she likes. So do I."', prefix + "chiv_stood", flags=(CONTRACT, STOOD),
             alignment=("Chaotic", 1))),
        rl(prefix + "chiv_kept", '''"Your word." {n}Rokhorn weighs it the way she would, like a coin on a counter.{/n} "She'll bite it first. She bites everything. And if the lilitu ever sets one foot on her stairs, she'll finish what you didn't and send you the bill; I'd put money on it." {n}He tucks your answer away.{/n}''',
           c("Continue", next)),
        rl(prefix + "chiv_stood", '''"Goes where she likes." {n}Rokhorn's grin comes slow.{/n} "Then she'll keep a knife for the lilitu the way she keeps a room for you, hot stuff. Both ready. I'd stay out of the way of both, if I were you. I'm going to."''',
           c("Continue", next)),
    ]


COURIER = '''{n}The courier comes to the citadel gate at dusk and will not give the guard a name, only a smile that makes the guard take a step back. He is an incubus, tall and bare-chested under a traveller's cloak gone grey with Worldwound ash, and he came up the roads out of the rift the way demons come to Golarion these days. He hands you a letter sealed in black wax with a gold coin pressed into it.{/n}
"Her coin in her wax." {n}He says it before you can ask, and holds up his right thumb: blistered white across the pad.{/n} "She paid a hedge-witch in the Lower City the price of a night with one of the Sinners to ward her seals. Open one with anything but the hand it's meant for and the wax bites, and whatever's under it burns. I tried. Once. On the first night out of the Isles." {n}He leans on your doorframe and waits, and does not look at the letter.{/n}'''

# The late device (R2-2: a present, priced act): her letter is an innocent invitation, and the plan rides folded under the
# coin in her seal, which Rokhorn cannot lift unseen. On the doorstep he tries to buy the Commander, as she said he would;
# the Commander plays the buyer he wants, and pays for it now (his claw and a taste of blood, or crusade gold).
COST_LATE = H + "cost.late"                     # the late con's price: his taste of the Commander's blood, or crusade gold
LATE_RING = H + "late.earnest_ring"             # he paid his earnest with a ring off her tray; the Commander kept it
LATE_PAID = H + "late.paid_his_price"           # the Bluff failed and the Commander paid him to believe it

letter(H + "late.next_move", "A courier from the Isles", [
    nar("start", COURIER,
        c("Continue", "met", requires=(MET,)),
        c("Continue", "stranger", requires=(MADAM,), forbids=(MET,)),
        c("Continue", "stranger_house", forbids=(MET, MADAM))),
    # Where Chivarro never fell (ChivarroRemovedFormPower never played), Herrax is not the madam: she is a senior girl of
    # the house with her own rooms on the private floor, and Rokhorn wants them. Nothing of Chivarro's state is read or set.
    hl("stranger_house", '''"We haven't met. I'm Herrax. I work the Ten Thousand Delights, in Alushinyrra, under a madam who pays me less than I'm worth and sleeps better than she should. The Isles still talk about you: the mortal who came back out of the Isles with all ten fingers. I like a guest with all ten fingers. They tip.
Come and be my guest when your war is done. Ask for me by name, not for the madam. My boy will see you down the Wound road, if you ask him nicely. H."
{n}That is all the letter says. Then you turn the coin in the broken wax, and find a second sheet pressed flat beneath it, folded to the size of a thumbnail, in a smaller hand.{/n}''',
       c("Continue", "ask_house")),
    hl("ask_house", '''"The house's incubus wants my rooms. Rokhorn. He tried for them once and lost, and paid the healers of three circles to forget it. Now he's circling again: smiling at my guests, counting my girls, telling the madam I'm getting old and the best rooms on the private floor would earn more with him in them. I don't get old, honey. I get even.
I want him sold a night he won't forget. My night, in my rooms, with my girls waiting in the dark. I pick the night; a seller he doesn't know is mine sells it to him; I do the cutting. The madam won't stop me. She'll watch, and she'll learn something about who holds what in her house.
He'll try to buy you on your doorstep before he's had a cup of your wine; that's what he's for. Let him. Make him pay something on account. When the Wound is shut, if you're alive, come back to the Isles and deliver it. Burn this. H."''',
       c("Continue", "door")),
    hl("met", '''"My favourite guest left the Isles without a goodbye. Rude. I forgive it; I simply charge for it later.
Come and be my guest when your war is done, lover. The Delights keep a room for a favoured guest, and a cup, and a girl to pour it, and I keep the bill. My boy will see you down the Wound road, if you ask him nicely. He's very nice to people who ask. H."
{n}That is all the letter says. Then you turn the coin in the broken wax, and find a second sheet pressed flat beneath it, folded to the size of a thumbnail, in a smaller hand.{/n}''',
       c("Continue", "ask")),
    hl("stranger", '''"We haven't met. I'm Herrax. I keep the Ten Thousand Delights, in Alushinyrra, and everything in them that can be kept. The Isles still talk about you: the mortal who came back out of the Isles with all ten fingers. I like a guest with all ten fingers. They tip.
Come and be my guest when your war is done. My boy will see you down the Wound road, if you ask him nicely. H."
{n}That is all the letter says. Then you turn the coin in the broken wax, and find a second sheet pressed flat beneath it, folded to the size of a thumbnail, in a smaller hand.{/n}''',
       c("Continue", "ask")),
    hl("ask", '''"My incubus wants my chair. He tried for it once and lost, and paid the healers of three circles to forget it. Now he's circling again: smiling at my guests, counting my girls, telling anyone who'll listen that the madam is getting old. I don't get old, honey. I get even.
I want him sold a night he won't forget. My night, on my floor, with my house waiting in the dark. I pick the night; a seller he doesn't know is mine sells it to him; I do the cutting. Scars only teach when the right hand makes them.
He'll try to buy you on your doorstep before he's had a cup of your wine; that's what he's for. Let him. Make him pay something on account. A man who has paid for a thing doesn't look at it too closely when it's delivered.
When the Wound is shut, if you're alive, come back to the Isles and deliver it. Burn this. H."''',
       c("Continue", "door")),
    rl("door", '''{n}The incubus has been watching you read. When you look up, he smiles with his whole mouth.{/n}
"Hello, hot stuff. She says you might visit, after." {n}He straightens off the doorframe.{/n} "When you do, ask for me before you ask for her. I'm told you can be bought. So can the house."''',
       c('"Why would I come to you and not to her?"', "why", requires=(MADAM,)),
       c('[Play the buyer he wants] "Make me an offer, then."', "earnest"),
       c('"Tell her I\'m not for sale, and neither is anyone I know."', "refused", flags=(CLOSED,)),
       c('"Why would I come to you and not to her?"', 'why_senior', forbids=(MADAM,))),
    rl("why", '''"Because she's old, hot stuff, and I'm not." {n}He says it with total conviction.{/n} "She sits on Chivarro's cushions, counts the rings on her tray, and tells everyone the keeper is beyond anyone's reach. I've reached her. I had the scars to prove it; I just had the sense to have them taken off."
"When the chair changes hands, the people on my side of the stair get a cut." {n}He smiles with all his teeth.{/n} "Now. What shall I tell her?"''',
       c('[Play the buyer he wants] "Tell her I\'ll come. And tell me what you\'re offering."', "earnest"),
       c('"Tell her I\'m not for sale, and neither is anyone I know."', "refused", flags=(CLOSED,))),
    rl("promised", '''"Oh, I'll tell her." {n}He laughs, and pulls the ashy cloak up round his shoulders, and on the top step he looks back once, past you, into your hall, the way a courier looks at everything he will be asked about later. Then he goes down into the dusk, whistling all the way to the gate.{/n}''',
       c("[Keep the coin from the seal.]"), *DISCOVERY_ENTRY),
    rl("refused", '''"Shame." {n}He shrugs his cloak up round his shoulders.{/n} "She'll find another liar. The Abyss is full of them. Most of them are cheaper than you."''',
       c("Continue")),
    rl("earnest", '''"A quarter of what I take from her rooms and her guests, for the seller who brings me her floor." {n}He says it as though it were a love-word.{/n} "That's my offer. And because you're mortal, and mortals forget whose they are between one season and the next, I'll pay something on account." {n}He draws a ring off his smallest claw: heavy old gold with a black stone, the metal still worn flat on one side by somebody else's knuckle.{/n}
"Take it, and tell me you'll sell her to me in the spring. Look at me while you say it. I can smell a lie on a mortal from here, and I can taste one from closer."''',
       c('[Bluff] "Spring. Her floor, her night, your quarter. Give me the ring."',
         check=dict(Skill="CheckBluff", DC=22, Success="earnest_taken", Failure="earnest_doubted")),
       c('"Keep your ring. Tell her I\'m not for sale."', "refused", flags=(CLOSED,))),
    rl("earnest_taken", '''{n}He looks at you a long while, and then he laughs, and drops the ring into your palm.{/n}
"Greedy. Good. Greedy I understand." {n}He doesn't let go of your hand. One claw comes out, idly, and draws a line across the heel of your palm, and before it stings he has lifted it to his mouth.{/n} "Sellers in the Isles seal in blood, hot stuff. Now I've had a taste of you. If you sell her to anyone else, I'll know you in the dark from across the city." {n}He licks the last blood from his claw and laughs in his ordinary voice.{/n} "A taste, not a reading. Why spoil a good bargain with bad omens? Mm. Something burning. I'll remember it."''',
       c("[Close your hand on the ring and the cut.]", "promised", flags=(PRIMED, STARTED, PROMISED, COST_LATE, LATE_RING))),
    rl("earnest_doubted", '''{n}He studies your face, and the ring goes back onto his claw.{/n}
"No. You're lying, or you're frightened of her. A taste and a reading would tell me which, but you keep your hands to yourself." {n}He isn't angry. He sounds like a merchant who has been offered bad coin.{/n}
"Here's how it works in the Isles, hot stuff. People who mean it pay. The ones who only want to watch get a seat at the arena. Pay me for the privilege of selling to me, and I'll believe you're greedy. Greedy I trust."''',
       c("[Pay him out of the crusade's purse, for the privilege.]", "promised", crusade=("Finances", -500),
         flags=(PRIMED, STARTED, PROMISED, COST_LATE, LATE_PAID)),
       c('"Then tell her I\'m not for sale."', "refused", flags=(CLOSED,))),
    *discovery(),
    rl("why_senior", '''"Because she charges too much, hot stuff." {n}He glances past you at the letter.{/n} "Her own rooms, her own girls, and every guest wanting a look at those scars. Chivarro keeps the chair. Herrax keeps the best corner of the private floor. I mean to have that corner."
"Be the guest who lets me in, and you'll get your cut." {n}His smile widens.{/n} "Now. What shall I tell her?"''',
       c('[Play the buyer he wants] "Tell her I\'ll come. And tell me what you\'re offering."', "earnest"),
       c('"Tell her I\'m not for sale, and neither is anyone I know."', "refused", flags=(CLOSED,)))],
    requires=("trickster",), forbids=(PRIMED, COMMITTED), delay=0,
    TricksterDevice=True, TricksterState="not_started")

OWED_VARIANTS = (
    c("Continue", "unsold", requires=(COIN_HELD,), forbids=(BAIT, BLOWN)),
    c("Continue", "sold", requires=(BAIT,), forbids=(LESSON,)),
    c("Continue", "blown", requires=(BLOWN, COIN_HELD), forbids=(BAIT, LESSON)),
    c("Continue", "lesson", requires=(LESSON,), forbids=(DECLINED,)),
    c("Continue", "knife", requires=(DECLINED,), forbids=(RESTORED,)),
    c("Continue", "restored", requires=(RESTORED,), forbids=("herrax.house.a_night_late",)),
    c("Continue", "restored_watched", requires=(RESTORED, "herrax.house.a_night_late")),
    c("Continue", "unsold_lost", forbids=(BAIT, BLOWN, COIN_HELD)),
    c("Continue", "blown_lost", requires=(BLOWN,), forbids=(BAIT, LESSON, COIN_HELD)),
)

letter(H + "owed.night", "The night, owed", [
    nar("start", '''{n}The courier is an incubus in a traveller's cloak grey with Worldwound ash, and you know him. He leans in your doorway in Drezen as if he owned it, and holds out a letter sealed in black wax with a gold coin pressed into the seal.{/n}
"Warded," {n}Rokhorn says, before you can ask, and shows you the blistered pad of his thumb.{/n} "A hedge-witch's work; she paid a Sinner's night for it. Open it with any hand but yours and it burns. So I haven't read it, and I'd like it noted that I haven't read it." {n}He sounds as though it has cost him.{/n}''',
        *OWED_VARIANTS),
    hl("unsold", '''"You agreed to sell him my night, and then you left the Isles with the night still in your pocket. I waited up. I don't wait up, lover.
He's still circling. He thinks my favourite guest ran out on me, and he's right. He brought you this letter himself and has no idea what's in it. That's the sort of man he is."
{n}A line below the signature:{/n} "Still carrying my coin? It opens the Delights, lover. What I have to say to you isn't for sale."''',
       c("Continue", "ask")),
    hl("sold", '''"He came up my back stair the night after you left, with my coin on his belt and every word you'd told him ringing in his ears. My house was waiting in the dark. I did the cutting myself, lip to cheekbone. You'd have liked it. You weren't there.
The seller is supposed to stand where I tell them. You were halfway to the Worldwound. So the house watched, and the house noticed that the favoured guest missed the best night of the year." {n}Below, smaller:{/n} "He carries my letters now. Look at his face."''',
       c("Continue", "ask")),
    hl("blown", '''"You botched the sale, and he laughed it off every couch in my house, and then you left the Isles before the night came. So I did it anyway, in the great hall, under the lamps, with the whole house watching and my favourite guest nowhere at all.
They're still talking. They say the madam's floor was offered for sale, and the seller ran." {n}Below, smaller:{/n} "He carries my letters now. Look at his face. Still carrying my coin? Keep it out of this bargain."''',
       c("Continue", "ask")),
    hl("lesson", '''"You stood where I told you. I'll give you that. And the next night, at closing, I had something to say to you, lover, and the hall was empty, and you'd gone up the road to your war.
I sat on the dais until the lamps burnt out. Do you know how long it has been since I waited for anyone? Neither do I. Chivarro might remember. She kept better accounts than I did."''',
       c("Continue", "ask")),
    hl("knife", '''"You still have my knife.
You took it off me in my own hall, in front of my house, and then you left the Isles with it on your belt. Every girl in the Delights has looked at my empty sheath since you left. Rokhorn walks around with his face whole, smiling at them. He carried you this letter. Look at him, and think about what you've done to my house."''',
       c("Continue", "ask")),
    hl("restored", '''"You gave me my knife back, hilt first, in front of the Sinners. The house hasn't stopped telling it. And then you left before I'd decided about you. The night after, I put right what you'd stopped, and I looked for you at the back of the hall, and you were gone.
I'd decided, lover. I don't like having decided at nobody."''',
       c("Continue", "ask")),
    hl("restored_watched", '''"You gave me my knife back, hilt first, in front of the Sinners, and the next night you stood at the back of my hall and watched me put right what you'd stopped. You didn't flinch. The house noticed.
And then, before closing, before I'd said a word to you, you were gone up the road to your war. I'd decided, lover. I don't like having decided at nobody."''',
       c("Continue", "ask")),
    hl("ask", '''"So. When the Wound is shut, if you're alive, come back up my stairs. Whatever's owed between us is still owed; I don't close a book because the customer left town.
Come in person. Not with a coin. You'll have to reach. H."''',
       c('[Promise to come back] "Tell her I\'ll come up her stairs when the Wound is shut."', "promised",
         flags=(STARTED, PROMISED)),
       c('"Tell her not to wait for me."', "refused", flags=(CLOSED,))),
    rl("promised", '''{n}Rokhorn takes your answer with a courier's bow, which on him looks like an insult. If his face is stitched, the stitches pull when he smiles; he smiles anyway.{/n} "She'll be thrilled, hot stuff. She'll hide it very well." {n}On the top step he looks back once, past you, into your hall, the way a courier looks at everything he will be asked about later.{/n}''',
       c("Continue"), *DISCOVERY_ENTRY),
    rl("refused", '''"I'll tell her." {n}He sounds pleased about it.{/n} "She won't wait. She never has. That's the whole secret of her."''',
       c("Continue")),
    *discovery(),
    hl("unsold_lost", '''"You agreed to sell him my night, and then you left the Isles with the night still in your pocket. I waited up. I don't wait up, lover.
He's still circling. He thinks my favourite guest ran out on me, and he's right. He brought you this letter himself and has no idea what's in it. That's the sort of man he is."
{n}A line below the signature:{/n} "Lost my coin? Then you'll have to walk. I still expect to see you."''', c("Continue", "ask")),
    hl("blown_lost", '''"You botched the sale, and he laughed it off every couch in my house, and then you left the Isles before the night came. So I did it anyway, in the great hall, under the lamps, with the whole house watching and my favourite guest nowhere at all.
They're still talking. They say the madam's floor was offered for sale, and the seller ran." {n}Below, smaller:{/n} "He carries my letters now. Look at his face. If you've lost my coin as well as your nerve, you'll come up the stairs empty-handed. You'll still come."''', c("Continue", "ask"))],
    requires=(PRIMED,), forbids=(COMMITTED, PROMISED), delay=0)


# --- 7. The one discovery (ledger 05 row 13): the woman she asked the Commander to finish is alive, at the Commander's side.

# Physical since the Q4 Sol pass: after the one Chapter 5 letter (whichever was sent) Rokhorn stays in Drezen, drinking at
# the Fool King's bar (front of the King, 3.5 m: Eliandra left 2.5 and Shamira right 2.5 are over 4 m away; the curio
# trader's right side when the King is gone or cannot be found). He is there only while the discovery is pending: Chivarro
# alive at the Commander's side, Herrax's request on record, no answer yet, no sale. The letters still carry the discovery
# when Chivarro is already back when they arrive; this scene carries it when she comes back later. Spawn-copy of his own
# unit (no dialog of its own) with a click-to-talk hub (ERRATA, Presence.Dialog "hub").
DREZEN = "2570015799edf594daf2f076f2f975d8"
FOOL_KING = "cc50a88bbd8dd3e4da066d33d14fdfc8"
# F10 authored staging: ordinary tiefling trader; front 8.5 m clears Terendelev's front 4.5 m by 4 m and the roof edge (9 m snapped onto a roof). Live proof 20261005-082713.
TIEFLING = "23eabf5b6364d4a4e86202dc5d27600b"   # Vendor_Tiefling (the lower town; Terendelev front, Galfrey's stall right, Mielarah behind)
EXOTIC = "bad9f602b81a80047ac470b01ebe65a9"   # ExoticCapitalTrader, native capital actor
ROK_HUB = "herrax.presence.rokhorn"
ROK_HUB_ALT = "herrax.presence.rokhorn_stall"
ROK_FAILED = ROK_HUB + ".failed"
KING_GONE = "fool_king.gone"
LETTER_SENT = [H + "late.next_move", H + "owed.night", "herrax.letters.the_courier"]
PENDING = [[MC_REUNITED, MC_RETURNED], LETTER_SENT]
ROK_FORBIDS = [CLOSED, CONTRACT, MC_DEPOSIT, MC_FAVOR]
PRESENCES = {
    ROK_HUB: dict(Unit=ROK_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TIEFLING, Side="front", Distance=8.5),
                  Requires=["trickster.ever", STARTED, ASKED_KILL], Forbids=ROK_FORBIDS + [ROK_FAILED, KING_GONE],
                  RequiresAnyGroups=[list(g) for g in PENDING], MinChapter=5, MaxChapter=5, AnswerLists=[], Dialog="hub",
                  Greeting=("{n}Rokhorn has the whole stretch of cobbles at the far end of the lane past the tiefling trader's stall to himself. The passers-by have decided, without "
                            "discussing it, that a bare-chested incubus in a cloak grey with Worldwound ash is best left the "
                            "far end of anything. He raises his cup to you with two claws.{/n}")),
    ROK_HUB_ALT: dict(Unit=ROK_UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=EXOTIC, Offset=[1.0, -8.0]),
                      Requires=["trickster.ever", STARTED, ASKED_KILL], Forbids=list(ROK_FORBIDS),
                      RequiresAnyGroups=[list(g) for g in PENDING] + [[ROK_FAILED, KING_GONE]], MinChapter=5, MaxChapter=5,
                      AnswerLists=[], Dialog="hub",
                      Greeting=("{n}Rokhorn is standing in the lane beyond the curio trader's stall in the lower town, turning a string of "
                                "cheap glass beads through his claws as if pricing them for a girl he dislikes. The trader has "
                                "stopped trying to sell him anything.{/n}")),
}
DISCOVERY_WHERE = {
    ROK_HUB: "{n}Rokhorn puts down the King's wine when he sees you. His smile has gone.{/n}",
    ROK_HUB_ALT: "{n}Rokhorn stops turning the trader's glass beads through his claws when he sees you. His smile has gone.{/n}",
}


def _discovery_scene(hub, suffix):
    twin = H + "chivarro_seen" + ("_stall" if not suffix else "")
    groups = [list(g) for g in PENDING] + ([[ROK_FAILED, KING_GONE]] if suffix else [])
    SCENES.append(scene(H + "chivarro_seen" + suffix, "An unfinished request", "Herrax", 5,
                        '"Why are you still in Drezen, Rokhorn?"', [
        rl("start", DISCOVERY_WHERE[hub] + '''
"I saw who came in with you, hot stuff." {n}He tips his cup toward the door.{/n} "Chivarro. In borrowed wool, drinking your wine, telling your cook the Delights' vintages have gone off since she left. My mistress asked you for that one. 'Can you take care of her for me, my love?' I was standing behind the dais when she said it. And here she is. Taken care of."
"I don't say you lied. Neither will she. You never said you would. But she asked, and her gratitude would have known no bounds, and now I'm to carry home your answer instead." {n}He puts the cup down.{/n} "She doesn't want the lilitu dead any more; she has the chair. She wants her out of the house, and out of the business, forever. What do I tell her?"''',
           c('"She stays out of your mistress\'s house and out of her business. She has my word."', "kept_out", flags=(CONTRACT, KEPT_OUT)),
           c('"She goes where she likes. So do I."', "stood", flags=(CONTRACT, STOOD), alignment=("Chaotic", 1))),
        rl("kept_out", '''"Your word." {n}Rokhorn picks at the edge of his cloak.{/n} "I'll carry it home, hot stuff. If she asks whether you meant it, I'll tell her you looked me in the face."''',
           c("Continue")),
        rl("stood", '''"I'll tell her." {n}He bares his teeth in a brief smile.{/n} "Every word. She pays me to carry answers, not soften them."''',
           c("Continue"))],
        requires=("trickster.ever", STARTED, ASKED_KILL), forbids=(CLOSED, CONTRACT, MC_DEPOSIT, MC_FAVOR, twin), delay=0,
        last=5, optional=True, Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=ROK_UNIT, InteractionHub=hub,
        RequiresAnyGroups=groups))


_discovery_scene(ROK_HUB, "")
_discovery_scene(ROK_HUB_ALT, "_stall")


# --- 8. Epilogue pages (Owner HerraxEpilogue; appended in authored order; no effects). ---------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}She kept Rokhorn. He served her breakfast every morning for the rest of her reign, with the scar the Commander had given him, and still watched her chair when he thought she was not looking. Every smug climber in the house counted it on the way up the stairs.{/n}", requires=(KNIFE_TAKEN,)),
    p("{n}She kept Rokhorn. He served her breakfast every morning for the rest of her reign, with the scar she had given him, and still watched her chair when he thought she was not looking. When guests asked who had made it, she said the favoured guest had handed her the knife, and let them work out what that meant.{/n}", requires=(HANDED,)),
    p("{n}She kept Rokhorn. He served her breakfast every morning for the rest of her reign, with the scar she had given him a night late. She liked to tell guests that the Commander was the only living soul who had ever taken her knife in her own hall, and the only one who had ever given it back.{/n}", requires=(RESTORED,)),
    p("{n}The botched sale became a story in the Upper City, and then a better one: the favoured guest who walked the length of the madam's hall to pay for it. Herrax told it herself, and improved it every year.{/n}", requires=(BLOWN,)),
    p("{n}The Commander kept a thin white line on one cheek, from ear almost to mouth, where an incubus had once read a lie in the blood. Herrax called it the house's mark, and liked to trace it.{/n}", requires=(CHEEK,)),
    p('{n}Without the coin, the Commander had to find the Delights on foot. Herrax still let that guest up her stairs without paying.{/n}', requires=(BLOWN,), forbids=(BAIT, COIN_BACK, COIN_HELD)),
    p("{n}The golden coin never left her bodice. The arches of Alushinyrra never carried the Commander to the Delights again, and the Commander always came anyway, up the stairs, like everyone else, and without paying, like no one else.{/n}", any_groups=((BAIT, COIN_BACK),)),
    p('{n}Herrax\'s answer was one line: "Your word, then, lover. I\'ll bite it first. If she sets one foot on my stairs, I\'ll send you the bill." Chivarro never set foot in the Delights again. Once a year Herrax sent Drezen a bottle of the house\'s worst wine, without a note.{/n}', requires=(KEPT_OUT,)),
    p('{n}Herrax\'s answer was one line, the pen driven through the paper: "Then I\'ll keep a knife for her the way I keep a room for you. Both ready. Neither used, if you\'re clever." The knife stayed where Herrax and Chivarro knew to look for it. Neither made the other reach for it.{/n}', requires=(STOOD,)),
    p("{n}The Commander kept the ram's-head signet. Back at the Delights, the regulars recognised its bent horn and remembered how Herrax had taken it from its last owner. She let them watch the Commander drink beside her, and left them to decide what the gift meant.{/n}", requires=("herrax.house.ring.kept",)),
    p("{n}Nobody ever learned what had burned her eye. She told the priestess story to paladins and the Chivarro story to romantics, and when the Commander was in the room she told the one about the girl with blue hands, and watched the Commander's face while she told it.{/n}", requires=("herrax.house.eye.believed",)),
    p("{n}Nobody ever learned what had burned her eye. The Commander guessed once, aloud, and she never answered, and she never told any of the stories again where the Commander could hear.{/n}", requires=("herrax.house.eye.guessed",)),
    p("{n}The twin of her knife, made by a salamander in the Lower City, stayed at the Commander's belt through the rest of the war. It was never used on anyone. She said that was the point of it.{/n}", requires=("herrax.letters.knife.kept",)),
    p("{n}Rokhorn's offer in the rain, the Commander wrote to her the same night, and she never touched him for it. She kept him instead, bringing her wine with shaking hands, and said it was the finest punishment she had ever been taught.{/n}", requires=("herrax.letters.offer.told_her",)),
    p("{n}The Commander paid the Battlebliss debt the first spring after the war: one night behind her bar in an apron, pouring for her guests and smiling at every one of them. Morevet sold the places at the bar for a month beforehand. Herrax kept the tips, and the apron.{/n}", requires=("herrax.house.arena.bet_lost",)),
    p("{n}Rokhorn waited, as he had promised, for the Commander to sell her to him a second time. He waited the rest of his long life. It was, Herrax said, the only lesson he ever learned properly.{/n}", requires=("herrax.letters.offer.refused",)),
    p("{n}On another night Herrax put the Commander behind her bar. She announced the repayment of her favour from the matter of Chivarro's body to every guest who ordered wine; this shift settled that account alone. She left the Commander pouring until the last guest went, took the tips, and struck the debt through in red.{/n}", requires=(MC_FAVOR,)),
    p("{n}The coin on the Commander's belt still opened the Delights' arch. It could spare a walk through the streets, but the stairs to Herrax's floor still had to be climbed. She let that guest up without paying.{/n}", requires=(BLOWN, COIN_HELD), forbids=(BAIT, COIN_BACK)),
)

SCENES.append(scene(H + "epilogue.reachable", "", "HerraxEpilogue", 6, "", [
    nar("page", '''{n}Herrax kept the Ten Thousand Delights long after the war, through two attempts on her chair and one on her life, and she kept her scars where every climber in the house could count them.{/n}
{n}She was still, as she told every king and demon who asked, the keeper of the house and beyond anyone's reach. Anything under her roof could be bought, and anyone, except her. Everyone in the Upper City knew the exception, and nobody in the Upper City understood it.{/n}
{n}One person came up her stairs without paying and found her there, and she was not for sale to that guest. The house called it the madam's one extravagance. Herrax called it good for business, and never once explained what she meant.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(H + "epilogue.after_hours", "", "HerraxEpilogue", 6, "", [
    nar("page", '''{n}The spring after the Threshold, the Commander went back to the Midnight Isles, walked up the stairs of the Ten Thousand Delights like any other guest, and asked for Herrax by name.{/n}''',
        paragraphs=(
            p("{n}Rokhorn had been waiting all winter for the promised seller. He had paid on account on a Drezen doorstep, and he had never once looked closely at what he had bought. Herrax named the night, and the Commander delivered it to Rokhorn over a cup of the incubus's wine, with a gold coin she had pressed into the Commander's palm for the purpose; every word of it was true except who would be waiting. After midnight the girl who kept the arch took Rokhorn up the back stair carrying the coin. Her people filled the room. Herrax cut Rokhorn from lip to cheekbone; the Commander stood at the front and watched.{/n}", requires=(COST_LATE,), forbids=(BAIT, BLOWN, LESSON)),
            p("{n}Herrax named the night. The Commander sold it to Rokhorn in person, over a cup of the incubus's wine, with a gold coin she had pressed into the Commander's palm for the purpose; every word of it was true except who would be waiting. After midnight the girl who kept the arch took Rokhorn up the back stair carrying the coin. Her people filled the room. Herrax cut Rokhorn from lip to cheekbone; the Commander stood at the front and watched.{/n}", forbids=(BAIT, BLOWN, LESSON, COST_LATE)),
            p("{n}Rokhorn's earnest ring went back onto her tray that night. Herrax counted it with the others, then turned the Commander's palm up to the lamp to look at Rokhorn's claw mark. \"Rokhorn's tasted you,\" she said. \"Good. Now he knows exactly what he lost to.\"{/n}", requires=(LATE_RING,)),
            p('{n}There was nothing left to sell. Rokhorn brought the wine with the scar on show and set it before the Commander without a word. Herrax let him stand there until she had poured for her guest, then sent him away. "This time, lover, you stay for closing."{/n}', any_groups=((BAIT, BLOWN, LESSON),), forbids=(DECLINED,)),
            p("{n}The Commander came up her stairs with her knife and gave it back, hilt first, at the foot of the stair, before the Sinners and anyone else who cared to look, before a word was said. She took it, and then she did her cutting, a season late, and made the Commander stand at the back to watch.{/n}", requires=(DECLINED,), forbids=(RESTORED,)),
            p("{n}Her knife was back at her hip, and Rokhorn's face bore the cut she had been denied. This time the Commander stayed until closing. She had decided long before; she wanted to say it to a face.{/n}", requires=(RESTORED,)),
            p("{n}At closing, in the empty hall, with the lamps burning, she offered the one thing her role forbade: to be reachable, by one person. The Commander said yes.{/n}", requires=(MADAM,)),
            p('{n}At closing, in Herrax\'s rooms, she barred the door against the guests still calling from below. "They\'re not paying for tonight, lover. Neither are you." She offered the Commander a place beside her, without a price. The Commander said yes.{/n}', forbids=(MADAM,)),
            p('{n}She caught the Commander by the belt and drew her guest between her knees. "Everyone else pays to be this close, lover." She set the Commander\'s thumb on the seam in her lip and opened her mouth beneath it. Armour fell at her feet. Her gown had one clasp; she broke it and let the silk slide off, showing every scar. The Commander kissed the torn corner of her mouth. Her ragged wings closed round them, and her claws pressed into the Commander\'s back. With each breath she took a little warmth, a little strength. "Still hungry?" she asked, against the Commander\'s throat. Then she pulled her guest down onto the bed. The lamps burned on.{/n}'),
            p("{n}In the morning Rokhorn brought breakfast and stood holding the tray until Herrax took it from him. He kept his mouth shut. She ate beside the Commander and counted the night's takings, then called one of her girls to collect the dishes. The girl looked from the empty plates to the armour left on the floor. Herrax smiled and let her look. By noon the house knew who slept without paying.{/n}"),
        ))],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMMITTED, CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(H + "epilogue.knife", "", "HerraxEpilogue", 6, "", [
    nar("page", '''{n}Herrax kept the Ten Thousand Delights after the war, and never replaced the knife the Commander had taken off her in her own hall. She wore the empty bone sheath at her hip for years, so that everyone would ask, and told each of them a different story about who had the knife. None of the stories was flattering.{/n}
{n}Rokhorn kept his face, and his ambitions. In the end she chose to deal with him quietly, rather than give the house another performance of the night her wrist was held, and the house said "Rokhorn left", and the next spring somebody else tried her chair, just to see.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(RESTORED, PROMISED, COMMITTED, CLOSED), **EP))

SCENES.append(scene(H + "epilogue.closed", "", "HerraxEpilogue", 6, "", [
    nar("page", '''{n}Herrax kept the Ten Thousand Delights long after the war, and kept herself beyond anyone's reach, as her role required. The Commander was welcome in her house to the end of her reign, and paid at the door, like anybody else.{/n}
{n}She was polite about it. She was always polite about the things she had decided never to mention again.{/n}''')],
    requires=("trickster.ever", STARTED, CLOSED), forbids=(COMMITTED,), **EP))


# --- 9. Reactions: Arueshalae, Regill and Woljif (ledger 05 §3.1 row 20), each on their own hub. ----------------------------

AR_GUARD = dict(forbids=("arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out", "arueshalae.kicked_out_evil"),
                ForbidOverrides={"arueshalae_dead": "arueshalae.trickster.returned",
                                 "arueshalae.evil_dead": "arueshalae.trickster.returned"})
RE_GUARD = dict(forbids=("regill.dead", "regill.kicked_out", "regill.left_plot"))
WO_GUARD = dict(forbids=("woljif.dead", "woljif.kicked_out"))
ARUESHALAE_HUB = "03ebad9587cbea0438d901a0f8df44f1"   # CompanionDialogues/Arueshalae/AnswersList_0003
REGILL_HUB = "2366a8db6481070439fee222c0c52e45"       # CompanionDialogues/Regill/AnswersList_0002
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"       # CompanionDialogues/Woljif/AnswersList_0003

SCENES.append(reaction("Arueshalae", H + "react.arueshalae_morning", ("trickster.ever", MORNING, "herrax.sermon_heard"),
    '''{n}Arueshalae wraps her arms round herself.{/n} "I lived in that house for years. I told you what it is, standing in her hall: pain, filth and lies."
"Rokhorn carried you breakfast with his face sewn shut, after you slept on Herrax's dais." {n}She makes herself look at you.{/n} "Everyone in that hall saw him serve you. I remember what it was like to stand at the back and watch, wondering when I'd be the one on my knees."
"Did she tell you what that breakfast would cost him?"''',
    answer_list=ARUESHALAE_HUB, chapter=4, last=5, entry='"You\'re very quiet this morning."', portrait="Arueshalae", **AR_GUARD))

SCENES.append(reaction("Arueshalae", H + "react.arueshalae_morning_unheard", ("trickster.ever", MORNING),
    '''{n}Arueshalae wraps her arms round herself.{/n} "I lived in that house for years, under Chivarro. I know what it sells: pain, filth and lies."
"Rokhorn carried you breakfast with his face sewn shut, after you slept on Herrax's dais." {n}She makes herself look at you.{/n} "Everyone in that hall saw him serve you. I remember what it was like to stand at the back and watch, wondering when I'd be the one on my knees."
"Did she tell you what that breakfast would cost him?"''',
    answer_list=ARUESHALAE_HUB, chapter=4, last=5, entry='"You\'re very quiet this morning."', portrait="Arueshalae",
    **dict(AR_GUARD, forbids=(*AR_GUARD["forbids"], "herrax.sermon_heard"))))

SCENES.append(reaction("Arueshalae", H + "react.arueshalae_knife", ("trickster.ever", KNIFE_TAKEN),
    '''"You cut his face because she told you where." {n}Arueshalae's voice is very level.{/n}
"I know Rokhorn. He's cruel and stupid and he'd have sold you in a heartbeat. I'm not crying for him." {n}She swallows.{/n} "But I used to stand at the back of that hall on nights like that one, and I used to think, one day it'll be my turn to hold the knife, and then it won't hurt. It still hurts, Commander. It just hurts somebody else."''',
    answer_list=ARUESHALAE_HUB, chapter=4, last=5, entry='"Something on your mind?"', portrait="Arueshalae", **AR_GUARD))

SCENES.append(reaction("Regill", H + "react.regill_night", ("trickster.ever", LESSON),
    '''{n}Regill looks up from his notes without raising his head.{/n}
"The succubus took a challenge to her authority, set the hour herself, used a false seller to draw the offender into the open, and punished him in public before the entire establishment, with a mark whose removal she forbids and punishes." {n}He makes a small note.{/n}
"That is the most orderly thing I have seen in this city. I find it deeply unpleasant that it happened in a brothel, and that you were the false seller. Neither fact will appear in my report."''',
    answer_list=REGILL_HUB, chapter=4, last=5, entry='"About the Delights..."', portrait="Regill", **dict(RE_GUARD, forbids=(*RE_GUARD["forbids"], DECLINED))))

SCENES.append(reaction("Regill", H + "react.regill_wrist", ("trickster.ever", DECLINED),
    '''"You seized the wrist of the ruling authority, in her own hall, before her subordinates, to spare an insubordinate." {n}Regill's voice has no heat in it at all.{/n}
"I do not care about the incubus. I care that every one of those demons watched a stranger overrule their mistress with one hand, and learned that it can be done." {n}He closes his notebook.{/n} "You taught a house of demons that order is negotiable, Commander. They are excellent students."''',
    answer_list=REGILL_HUB, chapter=4, last=5, entry='"About the Delights..."', portrait="Regill", **RE_GUARD))

SCENES.append(reaction("Woljif", H + "react.woljif_con", ("trickster.ever", BAIT),
    '''"Chief. Chief." {n}Woljif grabs your sleeve.{/n} "You sold a demon a night alone with his boss. Every word true, except who'd be in the room. Nice. Old trick. My uncle did it to a fence in Kenabres." {n}He squints.{/n}
"Except my uncle got paid. You gave the incubus her gold coin, the one that gets you in anywhere, for a quarter of a house he was never going to hold. So what did you get? A seat at a haircut?" {n}He shakes his head.{/n} "Chief, I love you, but you're a terrible businessman. Next time bring me. I'll make the demon pay for his own ambush."''',
    answer_list=WOLJIF_HUB, chapter=4, last=5, entry='"You look pleased with yourself."', portrait="Woljif", **WO_GUARD))

SCENES.append(reaction("Woljif", H + "react.woljif_cheek", ("trickster.ever", CHEEK),
    '''"Chief, your face." {n}Woljif leans in to look at the claw mark and whistles through his teeth.{/n}
"The incubus did that? Just like that, in the middle of the pitch?" {n}He winces.{/n} "Rule one of the long game, chief: never sell a man a lie if he can taste your blood. Everyone knows that. Well. Everyone who grew up around demons." {n}A crooked grin.{/n} "Still. You walked back into her hall afterwards with that on your cheek. That's either brave or stupid, and in my line of work it's usually both."''',
    answer_list=WOLJIF_HUB, chapter=4, last=5, entry='"What are you staring at?"', portrait="Woljif", **WO_GUARD))






# Authored late return: preparation paid in Ch5 buys no affection. The actual
# return settles any unfinished lesson before Herrax offers the unpaid night.
# The original page/continue exit remains an inert affirmative-history exit.
def _stage_late_return():
    ending = next(s for s in SCENES if s["Id"] == H + "epilogue.after_hours")
    old_page = ending["Nodes"][0]
    paragraphs = old_page["Paragraphs"]
    # The Ch5 letter reports the unwitnessed cuts as completed, not owed.
    paragraphs[3]["Requires"].append(LESSON)
    paragraphs[5]["Requires"].append("herrax.house.a_night_late")
    preparation = [*paragraphs[:6],
        p("{n}The invitation had brought Rokhorn upstairs after the Commander left the Isles. Herrax had described the cutting in her letter. Now he brought the wine with that scar on show. She made him wait while she looked her returning guest over. \"You missed my performance, lover. Stay for closing this time.\"{/n}", requires=(BAIT,), forbids=(LESSON, DECLINED)),
        p("{n}Rokhorn had exposed the sale before the Commander left the Isles. Herrax had cut him anyway, before the whole house, as her letter promised to remind the absent seller. Now she caught the Commander by the chin and inspected the mark Rokhorn's claw had left. \"He was here for his lesson. You ran off to your war. Tonight you stay.\"{/n}", requires=(BLOWN,), forbids=(BAIT, LESSON, DECLINED)),
        p("{n}The blade had been returned before the Commander left the Isles. Herrax had performed her delayed punishment the following night and reported it in her letter. The Commander had missed it. She tapped the bone sheath when her guest came upstairs. \"You gave it back. I used it. This time, lover, you will be here when I decide what I want.\"{/n}", requires=(RESTORED,), forbids=("herrax.house.a_night_late",)),
    ]
    visit_id = H + "epilogue.after_hours.invitation"
    slot_id = H + "epilogue.after_hours.explicit.1"
    visit = scene(visit_id, "", "HerraxEpilogue", 6, "", [
        nar("arrival", old_page["Text"],
            c("Continue", "madam_offer", requires=(MADAM,)),
            c("Continue", "rooms_offer", forbids=(MADAM,)),
            paragraphs=tuple(preparation)),
        n("madam_offer", "Herrax", '{n}At closing she sends the last attendant down the stairs and waits above the empty hall. The lamps stay lit.{/n} "You came back. This time you stay for closing. Now come here because you want to, lover. My accounts are shut for tonight." {n}She holds out her hand.{/n}',
            c('"Yes. By me."', "desire"), c('"No. Keep the night."', "declined", flags=(CLOSED,)), portrait="Herrax"),
        n("rooms_offer", "Herrax", '{n}Herrax bars her own door against the guests calling from below. She lets you see her smile before she takes the key out of the lock.{/n} "The madam gets her share downstairs. I decide who stays in this room. Tonight I want you. No price, lover."',
            c('"Then I am staying."', "desire"), c('"No. Keep the night."', "declined", flags=(CLOSED,)), portrait="Herrax"),
        nar("desire", paragraphs[8]["Text"], c("Continue", slot_id)),
        # Explicit brief: previously unconsummated late alternative, portable room/hall.
        nar(slot_id, "{n}Herrax draws her returning guest down and takes their mouth against the torn corner of her own, and the house below, calling for its madam, gets no answer. She takes a little warmth, a little strength, and is ragged and pleased about it; the door stays barred until morning.{/n}", c("Continue", "morning")),
        nar("morning", '{n}Outside the room, the house begins another morning. Rokhorn brings breakfast and holds the tray until Herrax takes it.{/n} "Your unpaid guest, mistress." {n}She laughs and makes him wait while she feeds you a piece of fruit. An attendant looks at the armour on the floor. Herrax lets her look.{/n} "Tell the others. This one eats with me. The rest still pay."', c("Continue")),
        n("declined", "Herrax", '"Downstairs, then. They will find you a room at the usual rate." {n}She turns the key in her fingers and calls for an attendant.{/n}', c("Continue"), portrait="Herrax"),
    ], requires=("trickster.ever", LATE_COMMITTED, "herrax.payoff.partner", "herrax.present_now"),
        forbids=(COMMITTED, CLOSED, "sacrifice", ending["Id"]),
        ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP)
    SCENES.append(visit)
    ending["EpilogueAfter"] = "scene:" + visit_id
    old_page["Text"] = "{n}Herrax's returning guest stayed at closing, after her lesson was finished and her own invitation answered. By noon the house knew who slept without paying. The Commander went back to the crusade's unfinished business; the next journey to the Isles ended at her door again.{/n}"
    old_page["Paragraphs"] = [
        p("{n}Herrax collected the Battlebliss thousand in service: a night behind her bar, an apron, and a smile for every guest. The girl who kept the arch sold places in advance. Herrax kept the tips and the apron.{/n}", requires=("herrax.house.arena.bet_lost",)),
        p("{n}On a separate night she put the Commander behind the bar for the favour owed over Chivarro's body. She named that debt to the drinkers, kept the tips, and struck the account through only when the last guest left.{/n}", requires=(MC_FAVOR,)),
    ]


_stage_late_return()


def _senior_bid():
    event = next(s for s in SCENES if s["Id"] == H + "late.next_move")
    earnest = next(n for n in event["Nodes"] if n["Id"] == "earnest")
    senior = deepcopy(earnest)
    senior["Id"] = "earnest_senior"
    earnest["Text"] = earnest["Text"].replace("A quarter of what I take from her rooms and her guests", "A quarter of the house, the night I hold it")
    senior["Choices"][0]["Text"] = '[Bluff] "Spring. Her rooms, her night, your quarter. Give me the ring."'
    event["Nodes"].append(senior)
    for node in event["Nodes"]:
        for answer in list(node["Choices"]):
            if answer.get("Next") == "earnest":
                alternate = deepcopy(answer)
                answer["Requires"].append(MADAM)
                alternate["Forbids"].append(MADAM)
                alternate["Next"] = "earnest_senior"
                node["Choices"].append(alternate)


_senior_bid()

def morevet_variants(scenes):
    """Authored absence staging; the native kill is persistent and has no return."""
    for event in scenes:
        if event["Id"] in ("herrax.house.honeyed_tongue", "herrax.house.morevet_laughs"):
            event["Forbids"].append(MOREVET_DEAD)
            continue
        swaps = {}
        for node in list(event["Nodes"]):
            def absent(text):
                text = text.replace("Morevet Honeyed Tongue with her lips parted;", "an attendant with her lips parted;").replace("Morevet with her lips parted,", "an attendant with her lips parted,").replace("Morevet", "the girl who keeps the arch")
                # Preserve sentence openings, including quoted and paragraph starts.
                import re
                return re.sub(r'(^|[.!?]\s+|\n|["“])the girl who keeps the arch', r'\1The girl who keeps the arch', text)
            if "Morevet" in node["Text"]:
                if node is event["Nodes"][0]:
                    node["Text"] = absent(node["Text"])
                else:
                    variant = deepcopy(node)
                    variant["Id"] += ".morevet_absent"
                    variant["Text"] = absent(node["Text"])
                    swaps[node["Id"]] = variant["Id"]
                    event["Nodes"].append(variant)
            for paragraph in list(node.get("Paragraphs", [])):
                if "Morevet" in paragraph["Text"]:
                    variant = deepcopy(paragraph)
                    paragraph["Forbids"].append(MOREVET_DEAD)
                    variant["Requires"].append(MOREVET_DEAD)
                    variant["Text"] = absent(variant["Text"])
                    node["Paragraphs"].append(variant)
        for node in event["Nodes"]:
            for answer in list(node["Choices"]):
                if answer.get("Next") in swaps:
                    variant = deepcopy(answer)
                    variant["Next"] = swaps[answer["Next"]]
                    answer["Forbids"].append(MOREVET_DEAD)
                    variant["Requires"].append(MOREVET_DEAD)
                    node["Choices"].append(variant)
                elif "Morevet" in answer["Text"]:
                    variant = deepcopy(answer)
                    answer["Forbids"].append(MOREVET_DEAD)
                    variant["Requires"].append(MOREVET_DEAD)
                    variant["Text"] = absent(variant["Text"])
                    node["Choices"].append(variant)


morevet_variants(SCENES)


# --- Registration -------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the relationship's own native keys (the coin, Rokhorn's two answers, Willodus's cue), the coin as removable,
    its derived keys and its portrait fallbacks. Scenes are added by expansion.py; world keys the matrix already verified
    (herrax.madam, herrax.met, herrax.asked_kill_chivarro...) bind on demand."""
    _bind(payload, "Etudes", ETUDES)
    payload["PermanentEtudes"] = sorted(set(payload.get("PermanentEtudes", [])) | {MOREVET_DEAD})
    _bind(payload, "SelectedAnswers", SELECTED_ANSWERS)
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "InventoryItems", INVENTORY)
    for key, value in PRESENCES.items():
        have = payload.setdefault("Presences", {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting presence: " + key)
        payload["Presences"][key] = dict(value)
    items = payload.setdefault("RemovableItems", [])
    if COIN not in items:
        items.append(COIN)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    # The units' own BlueprintPortraits (Herraxa m_Portrait BCT_Herraxa, Rokhorn m_Portrait BCT_Incubus) until custom
    # art ships; a custom PNG always wins.
    fallbacks = payload.setdefault("PortraitFallbacks", {})
    fallbacks.setdefault("Herrax", "1a63ad5b91e147aa8ea787206ced8faf")
    fallbacks.setdefault("Rokhorn", "f6fcea15a88d4fb29a407502bf7431f9")
