"""S26: authored Wintersun account; fixed antagonism, no authorized remedy.

Native anchors and blocked inputs are documented in the row's review pack.
Registration deliberately publishes incident witnesses, never household attitudes.
"""
import copy

from story_format import c, n, scene
from storylines.gesmerha_trickster import DREZEN, UNIT, CLAN_DESTROYED
from storylines.jerribeth_trickster import RETURNED, TENANT, HOST

P = "household.docket.gesmerha_jerribeth."
REPLY = P + "tenant_reachable"
REMEDY = P + "remedy.authorized"
WITNESSES = (P + "account.seen", P + "unsettled", P + "gesmerha_account_named")


def account():
    return scene(P + "account", "The people of Wintersun", "Gesmerha", 5,
        '"What would you have said to Jerribeth?"', [
        n("start", "Gesmerha", '''{n}Gesmerha's chisel stops above a wooden face. Beyond the smith's yard, a cart rattles toward the crusade's stores. She waits until its wheels have passed.{/n}
"You have brought demons into your company. Then hear what one of them did to mine. I will not have Wintersun called her collection."
{n}Her thumb finds the figure's cheek. The eyes are still uncut.{/n}''',
          c('[Present the existing quest or item remedy.]', "remedy_reserved", requires=(REMEDY,)),
          c('"Name what was done to your clan. I won\'t call it settled."', "account"),
          c('[Later.]', abort=True),
          c('[Ask the voice behind your eye to answer.]', "tenant", requires=(REPLY,))),
        n("account", "Gesmerha", '''"Marhevok cut out my eyes. He saw my carving and punished the hands that made it by taking something else. Jerribeth made demons look like our own people, and strangers look like monsters. She gave him that world to rule."
{n}She sets the little face upright, feeling for the edge of the bench.{/n}
"I still know the faces I carved. She does not get to name them toys."''',
          c('"And the clan now?"', "truth", requires=("gesmerha.truth",), forbids=(CLAN_DESTROYED,)),
          c('"And those who still live with the enchantment?"', "illusions",
            requires=("gesmerha.illusions",), forbids=("gesmerha.truth", CLAN_DESTROYED)),
          c('"Your account will stand."', "unresolved", forbids=(CLAN_DESTROYED,)),
          c('"And the carvers who will never return?"', "destroyed", requires=(CLAN_DESTROYED,))),
        n("truth", "Gesmerha", '''"They know what they were looking at. That does not give back what they lost while they were looking."
{n}Her fingers close over the chisel again.{/n}
"The crusade needs wood and iron. My people need roofs, food, work. They will not mend because a demon has found someone else to amuse her."''',
          c('"What can you decide for them?"', "chief", forbids=("gesmerha.marhevok_rules",)),
          c('"And with Marhevok still ruling?"', "marhevok", requires=("gesmerha.marhevok_rules",))),
        n("illusions", "Gesmerha", '''"The warriors have heard the truth. The others still have their dream. I cannot carve the enchantment out of their heads."
{n}She turns the wooden face away from the forge's sparks.{/n}
"Do not tell me a place at your table repays that."''',
          c('"What can you decide for them?"', "chief", forbids=("gesmerha.marhevok_rules",)),
          c('"And with Marhevok still ruling?"', "marhevok", requires=("gesmerha.marhevok_rules",))),
        n("chief", "Gesmerha", '''"I hear what they bring me. I help where I can. I have no use for Jerribeth's blessing."
{n}She draws the chisel through the wood. A narrow shaving falls across her wrist.{/n}''',
          c('"Then I will record what you have said."', "unresolved")),
        n("marhevok", "Gesmerha", '''"He still holds authority. You know that. My voice is mine, even when the clan is not mine to command."
{n}The chisel bites into the wood.{/n}''', c('"Then I will record what you have said."', "unresolved")),
        n("tenant", "Jerribeth", '''{n}The answer comes behind your left eye. Gesmerha hears only the forge.{/n}
"Wintersun. Yes, I know its name. Such eager little faces! They smiled at things that would have eaten them raw. And Marhevok was very pleased with himself."
{n}The laughter buzzes against your skull.{/n}
"She wants me to be sorry. How tiresome. Tell her I remember every one."''',
          c('"Jerribeth remembers. She is not sorry."', "answered"),
          c('[Keep the demon\'s reply to yourself.]', "account")),
        n("answered", "Gesmerha", '''{n}Gesmerha's hand stops. She cannot see the thing answering you, and she does not turn toward it.{/n}
"Marhevok took my eyes. Her enchantment made our people bow to demons. Neither of them has taken my hands. I am working. Tell her that."
{n}She lifts the unfinished face toward your footsteps.{/n}
"Set that down beside me, stranger. Not in the shavings. We have heard enough of her."''',
          c('[Set the carving safely beside her.]', flags=(*WITNESSES, P + "jerribeth_reply_heard"))),
        n("unresolved", "Gesmerha", '''"Write Wintersun. Write Marhevok's knife and Jerribeth's enchantment. Leave room for our people's names."
{n}She holds out the carving. When you put it beside her cup, she finds it by touch and resumes her work.{/n}''',
          c('"Your account is recorded. No remedy has been delivered."', flags=WITNESSES)),
        n("remedy_reserved", "Gesmerha", '"There is still work to be done."', c('[Leave the account unsettled.]', flags=WITNESSES)),
        n("destroyed", "Gesmerha", '''{n}Gesmerha feels the uncut eyes of the wooden face.{/n}
"The carvers are dead. There is no journeyman waiting to finish what I cannot finish. I brought my hands back to an empty bench."
{n}She takes the chisel up again.{/n}
"This face is mine to remember. Jerribeth can keep her pretty monsters."''',
          c('"Their names belong in the account."', "unresolved")),
        ], requires=("trickster", "trickster.now", "foresight.page_taken",
                     "gesmerha.wintersun_resolved", "gesmerha.trickster.returned",
                     "gesmerha.presence.route_open", "gesmerha.present_now"),
        forbids=(P + "account.seen", "gesmerha.closed", "gesmerha.presence.failed",
                 "gesmerha.epoch_unavailable", "trickster.failed", "fool_king.gone"),
        last=5, Relationship="gesmerha", Chapters=[5], Areas=[DREZEN],
        ContactUnit=UNIT, InteractionHub="gesmerha.presence",
        RestAllowance="household.protected", HouseholdCategory="protected",
        HouseholdWitness=P + "account.seen")


def register(payload, scenes, refs):
    """Append S26 to the final payload; all respondent gates are channel-local."""
    if any(s["Id"] == P + "account" for s in payload["Scenes"]):
        return
    payload.setdefault("PendingHooks", []).append(REMEDY)  # Unimplemented; never set.
    payload.setdefault("Derived", {})[REPLY] = [[RETURNED, TENANT, "jerribeth.present_now"]]
    payload.setdefault("DerivedOpenRoutes", {})[REPLY] = ["jerribeth"]
    payload.setdefault("DerivedForbids", {})[REPLY] = [HOST, "jerribeth.epoch_unavailable", "jerribeth.trickster.parted"]
    payload["Scenes"].append(copy.deepcopy(account()))
    # Preserve the builder's shared dictionary: household registrations follow
    # the row-discovery call and must remain visible through this same object.
    payload.setdefault("ForesightConsumers", {})[P + "account"] = "foresight.page_taken"
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None:
        ledger["Entries"].append(dict(Id=P + "account", Section="Debts", Portrait="Gesmerha",
            Title="Wintersun: an unsettled account",
            Text="{n}Gesmerha named what was done to Wintersun. Marhevok blinded her; Jerribeth bewitched the clan. No remedy was delivered.{/n}",
            Requires=[P + "account.seen"], Forbids=[], AnyGroups=[], Lines=[]))
