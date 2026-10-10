"""S17, authored RRT public contest; canon anchors and integration limits in s17.md.

Pair answers publish deed witnesses only. The shared controller owns first-wins
enmity, attitudes and reconciliation; this row never writes those states.
"""
import copy

from story_format import c, n, scene
from storylines import household, foresight

P = "household.pair.vellexia_shamira."
PAIR = ["vellexia", "shamira"]
BODY = ["vellexia.present_now", "shamira.present_now",
        "vellexia.trickster.in_person", "shamira.trickster.embodied"]
ELIGIBLE = [woman + ".harem.eligible" for woman in PAIR]
BLOCKED = ["household.closed", "fool_king.gone", "trickster.failed",
           "engine.l12.commander_unreturned", "vellexia.closed", "shamira.closed",
           "vellexia.trickster.kept_as_mirror", "shamira.trickster.cost.kept_captive",
           "shamira.trickster.cast_out"]
ENMITIES = ["vellexia.harem.enmity.shamira", "shamira.harem.enmity.vellexia"]
DEED = [P + suffix for suffix in (
    "stage.held", "vellexia.counterheard", "shamira.counterheard",
    "cost.vellexia.last_word_yielded", "cost.shamira.ridicule_borne",
    "cost.commander.boast_lost")]
# Read-only stage witnesses for the integration-owned attitude controller.
STAGES = {"rival": [[P + "ready"]], "respect": [DEED[:-1]]}
FINAL_FAILURE = P + "retry.failed"
FAILURE_CLAIMANT = ("shamira", "vellexia")
# Native bodies for the coordinator's Table contact attachment. Table scenes
# currently reject ContactUnit; do not turn this inventory into fake flags.
BODY_CONTACTS = ["a32a07903e428d34cb0e98a804d40569", "66e12264eaf6bf74196e20a9d7619cd2"]


def terminal(step, outcome, *extra):
    return c(flags=(P + step + ".seen", P + step + "." + outcome, *extra))


START = '''{n}A dispatch bearer waits beside the tavern door, mud drying on her boots. The Fool King's court has turned its chairs toward two women who have not touched their wine.{/n}
"Darling, you have brought a throne to a beer table." {n}Vellexia taps Shamira's chair with one pointed nail.{/n} "Will you clean His Majesty's latrines as well?"
"And you have brought an audience. Let us see which of us keeps it." {n}Shamira rises. The nearest courtiers stop laughing; Vellexia takes their silence for applause.{/n}
"Do sit down. You are spoiling the view."'''

FLOOR = '''{n}You put the dispatch on the King's table and hold back the next toast. Vellexia inclines her head, accepting the first turn.{/n}
"Our Lady in Shadow trusted me with her nobility. Shamira was given the mess they leave behind. An excellent arrangement — until the cleaner mistook the broom for a scepter."
{n}Shamira catches a laugh from the back of the room and waits for it to finish.{/n}
"Your nobles crawled through my doors whenever they wanted my lady's ear. You kept them amused. I decided which of them she heard, and which of them went home without a tongue."
"And such dreary requests!" {n}Vellexia smiles, but Shamira keeps her feet.{/n}
"Sit down, cow. You have had your turn. I have not finished."'''

FLOOR_END = '''{n}Vellexia opens her mouth. You bow extravagantly between them, drawing the court's laughter onto yourself. She closes it and gestures for Shamira to continue.{/n}
"I did not come here to serve your friend." {n}Shamira points at the waiting dispatch bearer.{/n} "Or to have her decide when I am done speaking."
"Then do try to be interesting." {n}Vellexia lifts her glass. Shamira finishes her answer before sitting; no one dares toast over it.{/n}
"Now, Commander," {n}Vellexia says,{/n} "that splendid bow of yours. Were you announcing a victory, or begging us to overlook the performance?"
{n}The court roars. Your prepared boast dies under it. Shamira smiles at Vellexia over her cup, showing teeth. The dispatch bearer steps forward.{/n}'''

PERFORMANCE = '''{n}You drag a stool into the open and kneel on it like a courtier begging for favor. Vellexia walks around you, inspecting the ridiculous petitioner's posture.{/n}
"Too upright. A courtier should look as though the queen has already stepped on the spine."
{n}You fold lower. Shamira catches the stool's back before it tips.{/n}
"And too eager to answer. Let the supplicant finish. Then decide what to tear out."
"His Majesty's cleaner has opinions about court manners!" {n}Vellexia turns toward the room. The laughter swells.{/n}
{n}Shamira lets it run. Then she turns the stool to face her.{/n}
"I heard yours. Now hear mine. The petitioner came to me. You may watch."'''

PERFORMANCE_END = '''{n}Vellexia steps into Shamira's path. You offer her your imaginary crown. She takes it, studies your bowed head, and laughs.{/n}
"No, darling. I have no wish to rule this dreadful little court. You may keep the crown — and the headaches."
{n}She returns it and steps aside. Shamira turns you back toward the audience.{/n}
"There. Your noblewoman has declined. Your audience is still waiting. Get up and deliver your dispatch."
"How industrious." {n}Vellexia has another retort ready. She drinks instead, leaving Shamira the end of the performance.{/n}
{n}You climb down to laughter that will follow you through Drezen. Shamira sits without silencing a single laugher. Vellexia raises her cup to her rival; Shamira answers with a shallow, disdainful nod. The dispatch bearer finally has the floor.{/n}'''


def success_nodes(step):
    return [n("performance", "Narrator", PERFORMANCE, c(next="performance_end")),
            n("performance_end", "Narrator", PERFORMANCE_END, terminal(step, "kept", *DEED))]


def build_scene(step, nodes):
    retry = step == "retry"
    return scene(P + step, "The queen's cleaner on the King's stage", "Vellexia", 5,
                 "[Vellexia and Shamira: the King's stage]", nodes,
                 requires=("trickster", "trickster.now", "foresight.page_taken",
                           "household.stance_eligible", "household.table.kept",
                           P + "ready", *ELIGIBLE, *BODY,
                           *((P + "settle.failed",) if retry else ())),
                 forbids=(*BLOCKED, *ENMITIES, P + step + ".seen",
                          *((P + "settle.kept", P + "settle.declined") if retry else ())),
                 delay=48 if retry else 0, last=5, Relationship="household", Chapters=[5],
                 Areas=[household.DREZEN], InteractionHub=household.TABLE_HUB,
                 Pair=PAIR[:], Participants=PAIR[:], RestAllowance="household.protected",
                 ForbidOverrides={ENMITIES[0]: "vellexia.harem.reconciled.shamira",
                                  ENMITIES[1]: "shamira.harem.reconciled.vellexia"},
                 HouseholdCategory="protected", HouseholdWitness=P + step + ".seen")


SCENES = [build_scene("settle", [
    n("start", "Narrator", START,
      c('"Your Majesty, give them the floor in turn."', check=dict(
          Skill="CheckDiplomacy", DC=22, Success="floor", Failure="botched", CommanderOnly=True)),
      c('"I\'ll play the courtier. You may both correct me."', "performance"),
      c('"Enough. The court has crusade business."', "declined"),
      c("[Later.]", abort=True)),
    n("floor", "Narrator", FLOOR, c(next="floor_end")),
    n("botched", "Narrator", '''{n}You raise your voice over the toast. The King raises his mug higher. Vellexia takes the interruption as a dismissal and waves Shamira back into her chair.{/n}
"There, darling. His Majesty has heard enough."
{n}Shamira remains standing until the laughter stops.{/n}
"He has heard you. Do not mistake that for hearing me."
{n}She leaves the wine untouched. The dispatch bearer squeezes past the courtiers.{/n}''',
      terminal("settle", "failed", P + "stage.answer_cut_off")),
    success_nodes("settle")[0],
    n("declined", "Shamira", '''"Then put your court to work."
{n}Shamira takes her chair. Vellexia beckons the dispatch bearer forward with a bored flick of her fingers.{/n}
"Do hurry. Apparently this mud is more interesting than we are."
{n}Neither woman drinks to the other.{/n}''', terminal("settle", "declined"), portrait="Shamira"),
    n("floor_end", "Narrator", FLOOR_END, terminal("settle", "kept", *DEED)),
    success_nodes("settle")[1],
]), build_scene("retry", [
    n("start", "Narrator", '''{n}The courtiers recognize the stool you drag out. Vellexia smiles; Shamira sets her cup down hard enough to splash wine on the King's cloth. Outside, soldiers unload a wounded patrol from a cart.{/n}
"Another performance?" {n}Vellexia asks.{/n} "You were so convincing as a fool."
"This time," {n}Shamira says,{/n} "I finish my answer."''',
      c('"Use my part. Finish your answers before the court."', "performance"),
      c('"Vellexia has already spoken for you both."', "failed"),
      c('"Leave the performance unfinished."', "declined"),
      c("[Later.]", abort=True)),
    success_nodes("retry")[0],
    n("failed", "Shamira", '''"For me?"
{n}Shamira looks from you to Vellexia. Vellexia settles comfortably into her chair.{/n}
"A tiresome office, darling, but someone must do it."
"Keep your little audience." {n}Shamira pushes her cup away.{/n} "You will not speak for me again. The next mouth in this city that tries it, I keep in a jar."
{n}The court's laughter falters. The soldiers outside call for a healer.{/n}''',
      terminal("retry", "failed", P + "stage.answer_cut_off"), portrait="Shamira"),
    n("declined", "Vellexia", '''"What a waste of a perfectly good fool."
{n}Vellexia pushes the stool beneath the table. Shamira ignores her and beckons a soldier in from the door. The wounded patrol needs the room more than this unfinished quarrel does.{/n}''',
      terminal("retry", "declined"), portrait="Vellexia"),
    success_nodes("retry")[1],
])]


def register(payload, scenes, refs):
    """Append only this row; safe to call on either initial or assembled payloads."""
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [[*ELIGIBLE, *BODY]]
    payload.setdefault("DerivedForbids", {})[P + "ready"] = BLOCKED[:]
    payload.setdefault("DerivedOpenRoutes", {})[P + "ready"] = PAIR[:]
    # Match household.integrate's reserved controller references for this new
    # pair. Declaring a pending hook does not produce an enmity or a pardon.
    pending = payload.setdefault("PendingHooks", [])
    for flag in (*ENMITIES, "vellexia.harem.reconciled.shamira", "shamira.harem.reconciled.vellexia"):
        if flag not in pending:
            pending.append(flag)
    existing = {s["Id"] for s in scenes}
    for row_scene in SCENES:
        if row_scene["Id"] not in existing:
            scenes.append(copy.deepcopy(row_scene))
        household.CONSUMERS[row_scene["Id"]] = household.PAGE_TAKEN
        foresight.CONSUMERS[row_scene["Id"]] = household.PAGE_TAKEN
