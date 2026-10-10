"""Wenduag: cloud voice-owner pass (villain-route-wenduag, design-first).

Applied last for her text, at the end of endings_job3.wenduag (after the partner
stance, echo, native-variant and Last Call layers have all written their copies).
Text and flag-gated paragraphs only: no scene, node or choice id, choice
position, Next, Set, gate, check, cost or GuidFor changes. Paragraphs are only
appended after existing ones (tools/payoff_contracts.json registers some of
them by index). Household pair rows get text only (J03: no paragraphs).
Review and truth table: tools/route_packs/redesign/wenduag/cloud-review.md.

Structure fixed here (read-only consumers of flags the route already sets):
  * promises with no reader: the ch3 south-gate answer (gate_early.*), the
    ch5 gate answer she said Brask would pay for (gate.*), "I'll be the first
    to tell you" (early.teeth.stare), the orchard scar and the late offer
    (cost.bled_outside, cost.late), "I'll see which of you is standing"
    (crystal_both), the Isles grave-stone (stone.kept/pocket), "Am I only
    strong while I'm pointed at your enemies?" (gongs.stronger), "you don't
    warn anyone first" (yaniel.rival), Rusk hanged or kept as bait;
  * harem gap: her epilogue never read her household lovers (Seelah,
    Arueshalae) or the Vellexia hunt once Vellexia was gone (two existing
    paragraphs both require and forbid participant.vellexia.available);
  * court.claim(_in_person):partner_secret answered the wash choice before the
    player made it;
  * the partner-state continuity lines read as designer notes ("none was put
    in his mouth", "nothing proved where he was now") on every epilogue,
    native variant and the Last Call page; same gates and indices, re-voiced;
  * household.pair.seelah_wenduag: the prisoner rule was a moral conversion in
    her mouth and the debt was paid in paperwork; she now keeps Rusk alive as
    bait, for her own reasons, on screen (same flags).

Canon used (enGB): 829669e9, 001cd911, ca9624d7, f58c7c9a, f97b4b9a, bf5fe56d,
8115c490, 7f91ab57, daefc78b, b88d1768, 627bdc70, 52df72bc, 8eb9aa1e.
Authored, no canon claim: Brask, Rusk, Tuhk, the cairns, the Isles stone.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, overlay_node, record
from story_format import p

from pathlib import Path

from tools import prose_pending_lint, voice_authority

PENDING = "[PROSE PENDING:"
W = "wenduag.trickster."
PAIR = "household.pair.seelah_wenduag."
TWINS = ("", ".native_visit")


def when(requires, body, forbids=(), any_groups=()):
    return p(body, requires=requires, forbids=forbids, any_groups=any_groups)


# ---------------------------------------------------------------------------
# Whole-node text (scene, node) -> text. Twins listed explicitly.
# ---------------------------------------------------------------------------
NODES = {}

NODES[(W + "court.vellexia", "remembered")] = '''"The blond one from the Isles." {n}Wenduag sniffs at the dark window.{/n} "The slut with the fake hair and the dozen stupid admirers. Gone, and I never once got her outside your roof." {n}She spits over the parapet into the yard.{/n} "Somebody else's meat now. Shame. I'd have made her squeal."'''

for _sid in (PAIR + "restraint", PAIR + "restraint.after_stood"):
    NODES[(_sid, "result_0")] = '''{n}Wenduag lets go of Rusk’s finger slowly, one knuckle at a time, so he feels every one of them leave. Then she turns to her hunters before Seelah can speak.{/n}
"Look at him. Dead, he’s meat for crows. Alive, he’s bait. His archers ran and left him, and they’ll come back for him, because uplanders always come back for their own. So he lives. Whole. Nobody cuts him, nobody takes a trophy off him, and nobody does me a favour in the dark and calls it an escape. Bait that can’t scream for its friends is no use to anybody."
{n}She shoves Rusk at the guards hard enough to put him on his knees.{/n} "Take him. Feed him. Keep him loud."
"I’ll keep the first watch," {n}Seelah says.{/n}
"You do that, paladin." {n}Wenduag watches her lead away the revenge she caught, and licks her lips.{/n} "I’ll be close."'''

NODES[(PAIR + "debt_repayment", "result_0")] = '''{n}That night Rusk’s archers come for him, the way she said they would. Wenduag’s hunters let them into the yard and shut it behind them. Seelah holds Rusk’s door with her shield while the screaming goes on outside it; he hears every one of his friends die, and so does she. By dawn the cultists in the yard are dead, the prisoner behind the door is breathing, and the hunting ground Wenduag baited for herself lies untouched.{/n}
{n}Wenduag wipes her knife on a dead archer’s sleeve and holds it up so the paladin can see it.{/n} "There. Your watch, paid in full. Tell your god I counted."
"It was paid," {n}Seelah answers. She does not look at the yard.{/n}'''

NODES[(PAIR + "debt_repayment", "result_1")] = '''"You think I need you to arrange an accident for me?"
{n}Wenduag bares her teeth.{/n} "When I want him dead he’ll be dead, and everyone on the wall will know whose hand did it. I told my hunters he lives. If they watch me sneak it, they’ll start sneaking things on me."
{n}She spends the night in the yard with her hunters, and Rusk’s rescuers die in it one by one while Seelah guards his door. Her own hunt is lost; the bait lives.{/n}
"You heard her," {n}Seelah says to you, and does not sound as though she enjoyed any of it.{/n}'''

NODES[(PAIR + "morning", "start")] = '''{n}Seelah finishes her morning prayer beside the tower’s narrow window. Below, Wenduag’s hunters drag Rusk back from questioning: alive, both hands whole, and grey to the lips. Whatever they asked him, they asked it close, and loud.{/n}
"Still praying after last night?" {n}Wenduag leans in the doorway with her shirt half laced.{/n} "Your god must have heard all of it."
"Yes. And I’m still watching your prisoners," {n}Seelah says.{/n}
{n}Seelah catches her belt again and pulls her close for a kiss.{/n} "You can complain on the stairs. The watch is waiting."
"My hunters know what he’s for." {n}Wenduag bites her lip on the way out of the kiss.{/n} "Bait. Not meat. Not yet."'''

# Substring edits inside an existing node text: (scene, node) -> (old, new).
SUBS = {}
for _sid in (W + "court.claim", W + "court.claim_in_person"):
    SUBS[(_sid, "partner_secret")] = (
        '\n"Cold water before dawn, then. No wearing my smell like a trophy. I liked the thought of him catching it."',
        '\n"Or wash it off. Cold water before dawn, every time, and you go back to him smelling of nothing." {n}She grins against your throat.{/n} "I\'d rather he caught it."')

# ---------------------------------------------------------------------------
# Re-voiced copies of existing paragraphs (same gates, same index). The same
# text is also baked into the native replacement variants' node Text and the
# Last Call page, so it is replaced wherever it occurs in her scenes.
# ---------------------------------------------------------------------------
REVOICE = {
    # Lann's current state (wenduag_partner_stance.ending_paragraphs, both copies of the first).
    "{n}Lann remained in the Commander's company. His old nights with Wenduag in Neathholm had bound neither of them to one bed.{/n}":
        "{n}Lann stayed in the Commander's company. He and Wenduag had shared a bed in Neathholm whenever it suited her, and nobody who heard them snarl at each other afterwards would have called it love.{/n}",
    "{n}Lann remained with the company. His nights with Wenduag in Neathholm belonged to their old life; serving beside her had promised no return to her bed.{/n}":
        "{n}Lann stayed in the Commander's company. He and Wenduag had shared a bed in Neathholm whenever it suited her, and nobody who heard them snarl at each other afterwards would have called it love.{/n}",
    "{n}Lann was dead. Whatever claims had been made over Wenduag's bed, there would be no answer from the hunter who had shared it in Neathholm.{/n}":
        "{n}Lann was dead. Wenduag said he had died the way he lived, trying to be better than he was, and ate his share of the supper that night without being asked.{/n}",
    "{n}The Commander had dismissed Lann. He was outside the company now; his old place beside Wenduag bought him no invitation back.{/n}":
        "{n}The Commander had thrown Lann out. Wenduag laughed about it for a week, called him the weak one to anyone who would listen, and never once went to see where he had gone.{/n}",
    "{n}Lann was away from the company. His place in Wenduag's old cave life remained, but nobody could answer for his present wishes.{/n}":
        "{n}Lann was away from the company. Wenduag noticed only at supper, when there was nobody left at the table worth needling.{/n}",
    "{n}There was no word of Lann. Wenduag had named him as a lover in Neathholm; nothing proved where he was now.{/n}":
        "{n}There was no word of Lann. Wenduag never asked for any. If he was alive, she said, he would turn up whining; if he was dead, something stronger had wanted him.{/n}",
    "{n}Lann lived, but was outside the Commander's company. His old nights with Wenduag in Neathholm had never bought either lover a promise to return.{/n}":
        "{n}Lann lived, but outside the Commander's company. Wenduag had taken him to bed in Neathholm and never promised him a second night; she did not start now.{/n}",
    "{n}Lann was outside the company. Even the reports of his absence offered no news of the hunter who had once shared Wenduag's bed.{/n}":
        "{n}Lann was gone from the company and nobody knew where. Wenduag said a hunter who could not keep his place by the fire did not deserve anyone looking for him.{/n}",
    # Her claim on the Commander and what Lann heard of it.
    "{n}The Commander had accepted sharing Wenduag. Lann had heard the invitation and refused a contest over her bed. His bow stayed with the crusade; his nights were still his to choose. Wenduag kept inviting him to hunt.{/n}":
        "{n}The Commander shared Wenduag, and Lann knew it, and would not fight anyone for her bed. She left her door open to him and the Commander's smell on her skin, and asked him out hunting every week, mostly to watch him decide.{/n}",
    "{n}The Commander had accepted sharing Wenduag, but Lann had been absent from that bargain. His answer was still his to give.{/n}":
        "{n}The Commander had agreed to share her, but Lann had never been there to hear it. Wenduag saved the news for the day he came back, so she could watch his face when she told him.{/n}",
    "{n}At the Commander's demand, Wenduag had ended her nights with Lann. Lann had heard it from her own mouth. Lann still followed the Commander. He never knocked at her door after the watch.{/n}":
        "{n}At the Commander's demand, Wenduag had shut her door on Lann and told him so to his face. He still followed the Commander. He never knocked after the watch, and she never missed a chance to remind him that he didn't.{/n}",
    "{n}The Commander had demanded Wenduag alone. Her answer had bought no word from him; none was put in his mouth.{/n}":
        "{n}The Commander had claimed Wenduag alone, and she kept the claim. Lann never heard it from her. She was saving that too.{/n}",
    "{n}Wenduag had refused the exclusive claim. The Commander insisted and lost her bed. Lann's place remained his to accept; she had promised him no new loyalty.{/n}":
        "{n}Wenduag had refused to be anybody's alone. The Commander pushed, and lost her bed for it. Lann got no promise out of her either; she said she was done handing claims to people who thought they had earned them.{/n}",
    "{n}The Commander had hidden the claim on Wenduag from Lann. He caught her scent after their night together and ended his own nights with her. Lann still fought beside the Commander, but would share no private jokes with either lover.{/n}":
        "{n}The Commander had hidden the claim from Lann, and Lann smelled it on the cellar stair anyway. He ended his nights with her that morning. He still fought beside the Commander, but he stopped laughing at anything either of them said, and Wenduag called that the best joke of the lot.{/n}",
    "{n}The Commander's claim on Wenduag was still concealed from Lann. No accusation had reached the lovers; no pardon had been asked or given.{/n}":
        "{n}Lann never caught the Commander's smell on her, or never said so. Wenduag decided he was either blind or a coward, and liked the secret better for not knowing which.{/n}",
    "{n}Lann had discovered the concealed claim and refused Wenduag's bed. His later absence did not undo that parting.{/n}":
        "{n}Lann had smelled the hidden claim and walked away from Wenduag's bed. Leaving the company afterwards changed nothing; she said he had been running from her since Neathholm.{/n}",
    "{n}Lann had heard Wenduag end their nights together. Wenduag kept to the Commander's exclusive claim after Lann left.{/n}":
        "{n}Lann had heard Wenduag shut her door on him before he left the company. She kept the Commander's claim after he was gone, and made sure everyone in the cellars knew who had lost.{/n}",
    "{n}Lann had answered the offer to share Wenduag while he was still with the company. With no word of him now, neither lover could say whether he would seek her out again.{/n}":
        "{n}Lann had heard the offer to share her while he was still with the company. There was no word of him now. Wenduag left her door unbarred anyway, and said that if he came back he could beg on the step.{/n}",
    "{n}Lann had heard Wenduag end their nights together. There was no word of Lann now. Wenduag kept to the Commander's exclusive claim.{/n}":
        "{n}Lann had heard Wenduag shut her door on him. There was no word of him now, and she kept the Commander's claim the way she kept a kill: with her teeth.{/n}",
    "{n}Lann had discovered the concealed claim and refused Wenduag's bed. There was no word of him now, and no reconciliation.{/n}":
        "{n}Lann had smelled the hidden claim and walked away from her bed. There was no word of him now. Wenduag never went looking; she said hunters who sulk in the dark get eaten.{/n}",
    "{n}Lann had answered the offer to share Wenduag. After he left the company, there was no news of another visit to her bed.{/n}":
        "{n}Lann had heard the offer to share her. He left the company afterwards, and nobody saw him at her door again. Wenduag said he had always been better at leaving than at staying.{/n}",
    "{n}With Lann dead, the Commander's offer to share Wenduag could remain only an offer. Their nights in Neathholm were over.{/n}":
        "{n}The Commander had offered to share her, and Lann died before it came to anything. Wenduag kept the Commander's bed and did not mourn the other where anyone could see.{/n}",
    "{n}Lann was dead now. Wenduag had answered the exclusive demand herself; no new answer could come from her former lover.{/n}":
        "{n}Lann was dead. Wenduag had given the Commander the claim with her own mouth; nobody was left to dispute it, and she said she would have liked somebody to try.{/n}",
    "{n}The Commander had concealed the claim on Wenduag. Lann was dead now; neither lover had received a pardon from him.{/n}":
        "{n}The Commander had kept the claim from Lann, and Lann died not knowing, or pretending not to. Wenduag said the dead keep secrets better than anyone, and that was the end of it.{/n}",
    "{n}The Commander made no new bargain about Lann. Wenduag's old cave lovers had never promised each other exclusivity.{/n}":
        "{n}Nobody ever made Wenduag promise anything about Lann. In the caves nobody promised anybody one bed, and she was not going to start for an uplander.{/n}",
    "{n}They had spoken of Lann, but the Commander had never accepted Wenduag's claim. There were no nights with the Commander to share or conceal.{/n}":
        "{n}They had argued about Lann once, with a bleeding sergeant on the floor between them, and then it had come to nothing. There were no nights to share or hide after that.{/n}",
    "{n}Lann had heard the proposed arrangement and answered for himself. The Commander then refused Wenduag's gift; the invitation to share her bed went no further.{/n}":
        "{n}Lann had been fetched to hear the arrangement and had answered for himself. Then the Commander set Wenduag's catch on its feet and sent it home, and the bed nobody was to fight over stayed cold.{/n}",
    # The killing she was promised (stance layer, every non-native epilogue).
    "{n}Savamelekh was dead. The Commander had never brought Savamelekh's stinger down the stair, or answered Wenduag's demand to do the killing herself.{/n}":
        "{n}Savamelekh died, and the Commander never brought her his stinger, or his throat. She had been promised the killing. She brought it up whenever the Commander looked comfortable.{/n}",
    # Lann and the cairn (her epilogue pages).
    "{n}The Commander told Lann the truth before anyone in the cellars could. Lann stayed through the war and after. The confession kept this quarrel from swallowing their friendship. His people and the war still needed him. Lann never quite forgave the Commander.{/n}":
        "{n}The Commander told Lann the truth before anyone in the cellars could. He stayed through the war and after, because his people needed him and so did the war, and he never quite forgave the Commander. Wenduag called the confession the stupidest thing the Commander ever did, and the bravest, and told Lann so to watch him squirm.{/n}",
    "{n}A woman in the cellars told Lann that Wenduag lived. Lann asked the Commander and got the truth, late. Lann stayed through the war and after, but every doubtful answer brought another question. The Commander had to meet Lann's eyes while answering.{/n}":
        "{n}An old woman in the cellars told Lann that Wenduag lived. He asked the Commander and got the truth, late. He stayed through the war and after, and from then on he asked every question twice and watched the Commander's eyes for the answer.{/n}",
    # Last Call page copies.
    "{n}At the Commander's funeral, Wenduag kept to the shadow of the cellar stair. Wenduag listened to it from the cellar stair and said the rhymes were worse than Lann's speech beside her cairn. Then she went down to the catacombs and packed the head end of a niche with loose stones, very carefully, and waited, because she knew how these things were done.{/n}":
        "{n}At the Commander's funeral, Wenduag kept to the shadow of the cellar stair and said the rhymes were worse than Lann's speech over her own body. Then she went down to the catacombs, packed the head end of an empty niche with loose stones, very carefully, and sat down beside it to wait, because she knew how these things were done.{/n}",
    "{n}At the Commander's funeral, Wenduag kept to the shadow of the cellar stair. Wenduag complained about the rhymes, then found a quiet place to wait for the news they had got wrong.{/n}":
        "{n}At the Commander's funeral, Wenduag kept to the shadow of the cellar stair and complained about the rhymes. Then she went to find a dark place to wait for the news that they had buried the wrong thing.{/n}",
}

# ---------------------------------------------------------------------------
# New read-only consumers, appended after the node's existing paragraphs.
# ---------------------------------------------------------------------------
ADD = {}


def add(scene, node, *paras):
    ADD.setdefault((scene, node), []).extend(paras)


for _t in TWINS:
    # ch3 early.gate: three answers to Brask, each promising something. The ch5 gate reads them.
    add(W + "court.gate" + _t, "gate",
        when((W + "gate_early.fought_for",),
             "{n}Months ago she told you she would wait until he forgot. He has forgotten. She has not.{/n}"),
        when((W + "gate_early.let_her",),
             "{n}The sleeves of the new coat have been sewn back on since she cut them off him. Badly. You can see the stitches from here, and so can she.{/n}"),
        when((W + "gate_early.rebuked",),
             "{n}Since you told her to walk past him, she has walked past this gate every morning with her eyes on her boots. Tonight she has stopped walking.{/n}"))
    # early.teeth.stare: "When you stop being strong, I'll tell you. I'll be the first to."
    add(W + "court.trial" + _t, "her",
        when((W + "early.teeth.stare",),
             '"In Kenabres I said I\'d be the first to tell you, the day you stopped being strong." {n}The edge turns a hair against your skin.{/n} "I\'ve come to see if it\'s today."'))
    # exile.ch5_hunt found_you: the cut under the ear "so that you will remember it".
    add(W + "court.trial" + _t, "which_orchard",
        when((W + "cost.bled_outside",),
             "{n}Her thumb finds the little scar under your ear, the one she gave you in the orchards, and presses until it stings.{/n}"))
    # crystal.bid both/nothing: "I'll see which of you is standing, and I'll be on that side."
    add(W + "court.trial" + _t, "reckoning",
        when((W + "crystal_both",),
             '"I told you I\'d stand with whoever was still standing. I meant every word." {n}Her lip curls.{/n} "I just counted wrong."'))
    # ch4.stone: the three-scratched stone from her grave, put in your pack before the Isles.
    add(W + "court.morning" + _t, "stone",
        when((W + "stone.pocket",),
             "{n}It clicks against the other one when you move: the stone scratched with three lines that she left in your pack before the Isles. Two pieces of two graves, both of them hers.{/n}"),
        when((W + "stone.kept",),
             "{n}The first one, scratched with three lines, is still at the bottom of your pack where you buried it. This one she put where you could not miss it.{/n}"))

# ch5 court.gate: "He's going to pay for that, and not to you" / "You'll see how". The claim is the payment.
for _sid in (W + "court.claim", W + "court.claim_in_person"):
    add(_sid, "her",
        when((W + "gate.rebuked",),
             '"You sent me back to the cellars in front of him. I told you he\'d pay for that, and not to you." {n}She puts her heel on the back of his neck and leans until he stops making noise.{/n} "He\'s paying."'),
        when((W + "gate.hers",),
             '"You let me answer him at the gate." {n}She grins down at him.{/n} "This is the rest of the answer."'),
        when((W + "gate.struck",),
             '"You broke his nose for me." {n}She prods the swollen ruin of it with one finger, and he squeals through the gag.{/n} "I took what was left."'))

# ch4.stone pocket without the morning stone: Last Call still knows what is in the Commander's hand.
add("wenduag.lastcall.call", "call",
    when((W + "stone.pocket",),
         "{n}Your other hand is in your pocket, closed round a flat stone scratched with three lines: the mark the neathers cut on a tunnel wall to say *this way is mine*.{/n}",
         forbids=(W + "morning.pocket",)))

PACK = (
    # The two existing Vellexia "window" paragraphs both require and forbid
    # participant.vellexia.available, so neither can show. Readers for that history:
    when((W + "vellexia.hunted",),
         "{n}Vellexia's window went dark before the hunt was finished. Wenduag kept the red ribbon the succubus had dropped her and tied off her snares with it, and told anyone who asked that it had come off a throat.{/n}",
         forbids=("participant.vellexia.available",)),
    when((W + "vellexia.left",),
         "{n}Vellexia's window went dark before Wenduag ever got her outside the Commander's roof. She said it was the only hunt anyone had ever stolen from her, and she meant to collect on it.{/n}",
         forbids=("participant.vellexia.available", W + "vellexia.hunted")),
    # court.gongs stronger: "Or am I only strong while I'm pointed at your enemies?"
    when((W + "gongs.stronger",),
         "{n}Once a year or so she asked the Commander again whether she was only strong while she was pointed at the Commander's enemies. She never waited for the answer. She went and found an enemy instead, and came back with it.{/n}"),
    # exile.ch5_hunt: "You're late with it. You'll pay for that, one day."
    when((W + "cost.late", W + "orchard_return"),
         "{n}She never let the Commander forget the season she spent snaring hares outside the walls. Every year, on the night the Commander had come out to the orchards, she vanished until dawn, came back with something dead, and said the Commander was late.{/n}"),
    # early/court.yaniel rival: "I'll remember that you know how. And that you don't warn anyone first."
    when((W + "yaniel.rival",),
         "{n}She remembered the paladin in the Fane. When she settled a rival in the cellars after the war, she did it the Commander's way: early, and without a word of warning first.{/n}"),
    # Household: Rusk (household.pair.seelah_wenduag) and her lovers in the household.
    when((PAIR + "restraint.execution_ordered",),
         "{n}Rusk, the cult scout captain who had left her bleeding in a ditch, hanged at sunset on the Commander's order. Before they cut him down, Wenduag took the smallest finger of his right hand, the one she had been holding when the paladin stopped her, and wore it on a thong until it rotted.{/n}"),
    when((PAIR + "boundary.kept",),
         "{n}Rusk sat in the paladin's cells for the rest of the war, alive and whole and loud, and every cultist who came to get him out died in the yard under his window. Wenduag called him the best snare she ever set.{/n}",
         forbids=(PAIR + "captive.rusk_dead",)),
    when((PAIR + "choice.both_yes", "seelah.present_now"),
         "{n}Some nights she was not in the cellars at all but up in the paladin's tower, and at dawn she came down the stair with her hand hooked in Seelah's belt and a grin she would not explain. The Commander never got a straight answer about which of them had won.{/n}"),
    when(("household.pair.wenduag_arueshalae.choice.both_yes", "participant.arueshalae.available"),
         "{n}The fallen succubus kept finding excuses to inspect her routes, and Wenduag kept letting her. They fought over every map in the citadel and finished the arguments somewhere with a door. Neither ever admitted who had started it.{/n}"),
)
add(W + "epilogue.pack", "page", *PACK)


def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}


def _node(scenes, sid, nid):
    return overlay_node(scenes, sid, nid)


HAREM_REVOICE = {
    "{n}Wenduag never disowned her advice on the Fellows. The Commander's stores for the surviving sick did not change her opinion of the thieves. She still thought they had deserved the rope.{/n}":
        "{n}The Commander's blankets kept some of the Fellows' sick alive. Wenduag called it a waste of good wool. She still said the thieves had earned the rope, and said it to the quartermaster's face whenever the wards came up.{/n}",
}
REVOICE.update(HAREM_REVOICE)

def _owned(sid):
    return sid.startswith("wenduag.")


def integrate(payload, *, include_harem=True):
    scenes = _scenes(payload)
    for (sid, nid), body in NODES.items():
        if not include_harem and sid.startswith(PAIR):
            continue
        with overlay_item():
            _node(scenes, sid, nid)["Text"] = body.strip()
    for (sid, nid), (old, new) in SUBS.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            if node["Text"].count(old) != 1:
                raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=str(old)[:70])
            node["Text"] = node["Text"].replace(old, new)
    used = dict.fromkeys(REVOICE, 0)
    for sid, scene in scenes.items():
        if not _owned(sid):
            continue
        for node in scene["Nodes"]:
            for old, new in REVOICE.items():
                if old in node.get("Text", ""):
                    used[old] += node["Text"].count(old)
                    node["Text"] = node["Text"].replace(old, new)
            for para in node.get("Paragraphs", []) or []:
                if para["Text"] in REVOICE:
                    used[para["Text"]] += 1
                    para["Text"] = REVOICE[para["Text"]]
    stale = [old for old, count in used.items()
             if not count and (include_harem or old not in HAREM_REVOICE)]
    for old in stale:
        record("overlay.text_mismatch", detail=old[:70])
    for (sid, nid), paras in ADD.items():
        with overlay_item():
            node = _node(scenes, sid, nid)
            node["Paragraphs"] = list(node.get("Paragraphs", []) or []) + [dict(x) for x in paras]
    touched = {key[0] for key in NODES} | {key[0] for key in SUBS} | {key[0] for key in ADD}
    # Registered integration placeholders belong to Claude's work queue.
    # The shared validator still rejects missing, stale or unregistered targets.
    owned = touched | {sid for sid in scenes if _owned(sid)}
    pending = voice_authority.read_json(Path(__file__).resolve().parents[1] /
                                       "tools/route_packs/plans/prose-pending.json")
    pending = {"version": pending["version"],
               "pending": [entry for entry in pending["pending"] if entry["scene"] in owned]}
    errors = prose_pending_lint.check({"Scenes": [scenes[sid] for sid in sorted(owned) if sid in scenes]}, pending,
                                     integration=True)
    for error in errors:
        record("overlay.validation", detail=error)
