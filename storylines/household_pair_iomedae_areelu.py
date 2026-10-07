"""S41: authored name reconstruction, HAREM-SHEETS-36-41 row 41.

The annex, cases, salvage and relatives are RRT additions. Native anchors are
voice evidence only; no native victim or soul is reassigned. Fixed X hostility
has no stage producer. Both women speak through existing earned channels.
"""
from story_format import c, n, scene

PREFIX = "household.pair.iomedae_areelu."
PAIR = ("iomedae", "areelu")
FORM = "a name reconstruction"
BANNER = ("iomedae.banner_in_hand", "iomedae.trickster.order_banner")


def P(flag):
    return PREFIX + flag


def done(*flags):
    return c("Continue", flags=tuple(P(flag) for flag in flags))


def io(node, text, *choices):
    return n(node, "Iomedae", text, *choices, portrait="Iomedae")


def ar(node, text, *choices):
    return n(node, "Areelu", text, *choices, portrait="Areelu")


def docket(step, title, nodes, trigger=None, forbids=(), delay=0, respondent=True):
    # Ordinary Table attachment, not table_entry(): its enmity suppression and
    # reconciliation overrides must never silence a protected X demand.
    # The Commander handles records here and takes them to the banner platform;
    # neither channel is presented as a woman sitting in the tavern.
    requires = ["trickster", "trickster.now", "foresight.page_taken",
                "household.table.kept", "household.stance_eligible",
                "iomedae.harem.eligible", "iomedae.trickster.first_spoken"]
    if trigger:
        requires.append(P(trigger))
    participants = ["iomedae"]
    if respondent:
        requires += ["areelu.harem.eligible", "areelu.trickster.lens_held"]
        participants.append("areelu")
    return scene(P(step), title, "Iomedae", 5, "[" + title + "]", nodes,
                 requires=requires, forbids=[P(step + ".seen"), *map(P, forbids)],
                 delay=delay, last=5, Relationship="household", Chapters=[5],
                 Areas=["2570015799edf594daf2f076f2f975d8"],
                 InteractionHub="household.table", Participants=participants,
                 **({"Pair": list(PAIR)} if respondent else {}),
                 RequiresAnyGroups=[list(BANNER)], RestAllowance="household.protected",
                 HouseholdCategory="protected", HouseholdWitness=P(step + ".seen"),
                 HouseholdForm=FORM)


ACCOUNT_COSTS = ("account.delivered", "resolved", "cost.iomedae_names_received",
                 "cost.areelu_codes_restored", "cost.areelu_records_opened")

# Code/name/fate pairings are printed on both independent evidence approaches.
# An unknown burial site does not make an identified man's death uncertain.
CASES = '''{n}You copy the reconstructed entries without removing the observations:
K-17 — Odran Vesk, miller. Died during the third infusion; remains incinerated. Burial site: none.
K-22 — Tervan Sorn, drover. Died after extraction; remains transferred out of the annex. Final resting place: unknown.
K-31 — Talaran Dorn, mason. Died during restraint; remains incinerated. Burial site: none.{/n}'''


SCENES = [
    docket("open", "Three cases without names", [
        io("start", '''{n}A quartermaster lays a damaged bundle beside your campaign maps. He has brought it with the laboratory salvage already recovered by the crusade. The cover names a small Sarkorian experiment annex; inside, three men's deaths have been reduced to codes. A separate index survived in the bottom of the salvage chest.
You carry the bundle to the banner platform. The wind drops. Iomedae's voice comes through the veiled cloth.{/n}
"Read the last entry again. 'Restraint continued after respiratory failure.' He was dead, and she was still recording the result."
{n}The cloth draws taut.{/n}
"Find who these men were. Their kin may still be waiting for an answer."''',
           c('"Keep the bundle. I will bring names as well as numbers."', "kept"),
           c('"Burn the cases. There are enough dead already."', "burned"),
           c("[Later.]", abort=True)),
        io("kept", '''"Bring the observations too. I will not have a prettier account substituted for what was done."
{n}You return the leaves to their cover and mark the separate index for comparison. Somewhere beyond Drezen's walls a siege horn sounds; the quartermaster has other salvage to sort.{/n}''',
           done("open.seen", "open.ready", "known.case_bundle")),
        io("burned", '''{n}You feed the case leaves into the brazier. A strip of scorched paper lifts against the banner before crumbling.{/n}
"You have destroyed evidence. Those men do not become less dead because you can no longer bear to read about them."
{n}The quartermaster still holds the separate index. You turn away from it.{/n}''',
           done("open.seen", "open.records_burned", "known.case_bundle", "permanent_refusal")),
    ], respondent=False),
    docket("reconstruction", "Names from the annex", [
        n("start", "Narrator", '''{n}The damaged bundle lies beside the separately preserved index. Outside, Drezen's scouts are mustering for the road toward the Wound. You set aside the evening's dispatches and unwrap Areelu's dark-glass lens.
The banner platform is ready to receive the account. The witch's lens will carry her corrections; the cloth will carry Iomedae's answer. You will address them separately.{/n}''',
          c("[Recover the original case leaves and collate them with the three families' identifiers.]", "originals.work"),
          c("[Complete the survivors' identification job from the preserved index.]", "families.accounts"),
          c('"Replace the observations with an apology. They won\'t read the difference."', "rejected"),
          c("[Later.]", abort=True)),
        ar("originals.work", '''{n}You return to the salvage chest with the quartermaster. Between two warped boards you find the detached intake leaves. Their seals match the bundle; each carries a name, a code and a relative's identifying mark. Back at your desk, you compare the leaves with the index and turn the lens toward the damaged columns.
Frost gathers on its rim. Areelu's corrections appear beside your transcriptions.{/n}
"K-22. That mark means extraction, not release. Do not send his family looking for a man who died on my table."
{n}She rebuilds the three damaged code correspondences, one stroke at a time. The dispatch candles burn down untouched.{/n}''',
           c("[Copy each name beside its case and retain the technical annotations.]", "originals")),
        ar("originals", CASES + '''
"Keep the incineration temperatures. They were recorded for a reason. Your goddess may find them offensive; that does not make them inaccurate."
{n}A second copy appears beneath her hand on the far side of the lens. She keeps it. You take your unabridged copy to the banner and read the names aloud.{/n}
"Odran Vesk. Tervan Sorn. Talaran Dorn," {n}Iomedae repeats through the cloth.{/n} "Their kin will receive these facts. The missing resting place will remain marked unknown."
"And the experiments?" {n}Areelu's letters cut across the glass.{/n}
"I condemn them. You have corrected three records, Areelu. You have not answered for the Wound."''',
           done("reconstruction.seen", "proof.originals_collated", *ACCOUNT_COSTS,
                "cost.commander_evening_spent")),
        n("families.accounts", "Narrator", '''{n}You take the index to the crusade's displaced Sarkorians. Odran's brother, Berun Vesk, opens a tool roll: a brass mill gauge bears the same notch recorded beside K-17. Tervan's son, Merek Sorn, gives you his father's caravan brand and the date he vanished; both match K-22's intake. Talaran's brother, Davor Dorn, shows you a mason's seal and describes the badly healed break in Talaran's left thumb. K-31 records that break.
All three men ask for the fate behind the mark. You write their names and accounts beneath the codes, then return to the lens.{/n}''',
          c("[Give Areelu Berun's, Merek's and Davor's named accounts through the lens.]", "families.match")),
        ar("families.match", '''{n}You read each relative's name and identifying account into the dark glass. Areelu copies them. The witnesses who trusted you can no longer remain anonymous in this inquiry.{/n}
"The brand is sufficient. The disappearance date is not; that column records admission, not capture."
{n}She restores the damaged cross-references and supplies the matching case observations.{/n}
"Your witnesses are useful. They have corrected an intake error. That does not entitle them to the rest of my work."
{n}You retain a copy of the three cases. She retains hers.{/n}''',
           c("[Read the reconstructed names and fates at the banner.]", "families")),
        io("families", CASES + '''
{n}You read the entries through the veiled banner, including the extraction and restraint notes. Iomedae listens to the last word.{/n}
"Tell Berun, Merek and Davor exactly this. Do not invent a grave for Tervan. Do not tell them these deaths served a noble purpose."
{n}Areelu's reply forms in frost on the lens.{/n} "I will not let you replace my purpose with theirs."
"I have asked for their dead. You will receive no pardon for naming them."
{n}You seal the family's copy with the unknown resting place still plainly marked.{/n}''',
           done("reconstruction.seen", "proof.families_identified", *ACCOUNT_COSTS,
                "cost.commander_contacts_exposed")),
        ar("rejected", '''{n}You scratch out the observations and write a confession of remorse in their place. The lens frosts before you finish.{/n}
"That is not my testimony. Restore the extraction notes. You have even left out the cause of death."
{n}At the platform, you read your replacement to Iomedae. The banner snaps hard enough to shake the pole.{/n}
"Whose apology is this? Not hers. You have put a lie between the dead and the people who need to hear of them. Bring the unedited index."
{n}You leave with both rejected copies. The three names remain unconfirmed.{/n}''',
           done("reconstruction.seen", "reconstruction.unsettled", "unsettled",
                "cost.commander_false_apology")),
    ], trigger="open.ready", forbids=("permanent_refusal",), delay=48),
    docket("repair", "Restore the three cases", [
        n("start", "Narrator", '''{n}Your false apology lies beneath the damaged case bundle. The quartermaster has kept the unedited index with the remaining laboratory salvage. The crusade's evening dispatches wait beside it.
You can retrieve the evidence and spend tonight restoring what you removed. Areelu's lens and the banner channel are still available; neither has accepted your account.{/n}''',
          c("[Recover the unedited index and restore the removed case correspondences.]", "restored.work"),
          c('"Leave my edited version in place."', "refused"),
          c("[Later.]", abort=True)),
        ar("restored.work", '''{n}The quartermaster brings out the index. You recover the intake leaves from the salvage chest and compare their family identifiers against it. Through the lens, Areelu rebuilds the damaged codes herself. She makes you recopy the removed observations beside your false apology, line by line.{/n}
"Leave your version attached. Let whoever reads it see where you changed the results."
{n}By midnight, your fingers are stiff with ink and cold. Her technical copy remains on the other side of the glass; the three reconstructed cases are now also in your keeping.{/n}''',
           c("[Deliver the corrected record with your falsification attached.]", "restored")),
        io("restored", CASES + '''
{n}At the banner, you read the correction before the quartermaster who brought the bundle. You name your false apology as your own invention.{/n}
"The correction will go with it," {n}Iomedae answers.{/n} "Their families will receive the facts, including what remains unknown."
{n}Areelu writes across the lens.{/n} "And my observations will remain legible. You have wasted enough of my time."
"Your time? Three men lost their lives. I will hear their names again when their kin have received them."
{n}The witch clears the glass. You carry the corrected copy down from the platform as Drezen's watch changes.{/n}''',
           done("repair.seen", "proof.index_restored", *ACCOUNT_COSTS,
                "cost.commander_evening_spent", "cost.commander_edit_exposed")),
        io("refused", '''{n}You close the bundle over your invented apology.{/n}
"Then the account remains false. I will not pass it to their families under my name."
{n}Areelu's letters appear on the lens.{/n} "Nor mine. Keep your forgery."
{n}You put the index away. The crusade's next dispatch lies unopened beside it.{/n}''',
           done("repair.seen", "repair.declined", "permanent_refusal")),
    ], trigger="reconstruction.unsettled", forbids=("resolved", "permanent_refusal"), delay=48),
]
