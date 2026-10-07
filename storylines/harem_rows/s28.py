"""S28: authored patronage audience; optional bodily arc withheld pending owner review.

Canon: Velexia_Third_Date/Cue_0055, e0ee422a413a5f94ea90bede3096ee56,
enGB ecc42853-d2e6-4613-95c2-de90a01dbfd5. Jerribeth defects from HER
patron Vellexia. This module supplies deeds, never central attitude/enmity,
client-overlay or reconciliation producers. See the row's implementation note.
"""
import copy

from story_format import c, n, scene

P = "household.pair.jerribeth_vellexia."
DEFECTION = "jerribeth.harem.vellexia_defection_seen"
PAIR = ["jerribeth", "vellexia"]
COMMON = ["trickster", "trickster.now", "foresight.page_taken",
          "household.stance_eligible", "household.table.kept",
          "jerribeth.harem.eligible", "vellexia.harem.eligible",
          "jerribeth.reachable_by_letter", "vellexia.reachable_by_letter"]
LOSSES = ["jerribeth.closed", "vellexia.closed", "jerribeth.epoch_unavailable",
          "vellexia.epoch_unavailable", "sacrifice"]


def flags(*names):
    return tuple(P + name for name in names)


def spoken(id, woman, text, *answers):
    return n(id, woman, text, *answers, portrait=woman)


def entry(step, nodes, *, requires=(), forbids=(), delay=0, category="protected"):
    return scene(P + step, "The patron's audience", "Jerribeth", 5,
                 "[Jerribeth and Vellexia: the patron's audience]", nodes,
                 requires=COMMON + list(requires), forbids=LOSSES + list(forbids),
                 delay=delay, last=5, Relationship="household", Chapters=[5],
                 Areas=["2570015799edf594daf2f076f2f975d8"],
                 InteractionHub="household.table", Participants=list(PAIR), Pair=list(PAIR),
                 RestAllowance="household." + category, HouseholdCategory=category,
                 HouseholdArc="S28", HouseholdWitness=P + step.split(".")[0] + ".seen",
                 ForbidOverrides={"sacrifice": "trickster.commander_back"})


def settlement(defected, retry=False, mind=False):
    step = "retry" if retry else "settle"
    history = "defected" if defected else "client"
    kept = flags(step + ".seen", step + ".kept", "account.kept",
                 "jerribeth.position_owned", "vellexia.reply_owned",
                 "cost.jerribeth.patronage_account_owned", "cost.vellexia.summons_yielded",
                 "cost.commander.separate_audiences")
    kept += flags("defection.answered", "vellexia.resumed_business") if defected else flags("client.account_named")
    opening = ('{n}Jerribeth speaks behind your eye. Her answer must be carried in your own voice; '
               'there is no second woman at the table.{/n}' if mind else
               '{n}Jerribeth\'s reply awaits you at the corner table. Vellexia\'s arrived separately. '
               'Between them lies the order recalling your scouts to the Worldwound.{/n}')
    opening += ('\n"Tell her I chose against her. I have not forgotten whom I struck. '
                'But I have something she wants, and she will hear it from me."' if defected else
                '\n"Tell my patron I have something for her. Not a tribute. '
                'She may hear the offer before deciding what to call it."')
    answers = ([c('"Both accounts, separately. I will bring the answers back."', "heard"),
                c('"Call the ' + ('betrayal' if defected else "patron's account") +
                  ' settled without her answer."', "muddled")] if retry else
               [c('"I\'ll carry the account as each of you states it."',
                  check=dict(Skill="CheckDiplomacy", DC=22, Success="heard", Failure="muddled",
                             CommanderOnly=True)),
                c('"I\'ll wait for both replies. Business first."', "heard")])
    answers += [c('"Leave it unanswered."' if retry else
                  '"Leave the patronage account where it stands."', "declined"),
                c('"Later."', abort=True)]
    j = ('"I chose my side. You know that. I am not going to crawl back and pretend '
         'otherwise. I will bring you what I find beyond the crusaders\' lines. '
         'You still have ears in places I cannot reach. Let us see which of us brings '
         'back the better prey."' if defected else
         '"Your patronage did not buy every hour I have. I have hunting of my own '
         'beyond the crusaders\' lines. What I find there may interest you. '
         'But send for me as though I were a pet, and you will wait."')
    v = ('"Oh, I remember your choice, darling. I should have pulled your wings off '
         'before you made it. Bring me something worth the disappointment. '
         'I will hear your offer — business can resume. Your betrayal remains yours."'
         if defected else
         '"My little client has acquired teeth. How charming. Bring me something '
         'worth hearing and I shall answer. I can amuse myself without tugging '
         'your leash every evening. There are still plenty of dull creatures '
         'who look better as furniture."')
    nodes = [spoken("start", "Jerribeth", opening, *answers),
             n("heard", "Narrator", '{n}You carry Jerribeth\'s words without polishing away '
               'the threat. Then you wait for Vellexia\'s answer. The scouts march '
               'before the second reply comes.{/n}', c("Continue", "jerribeth")),
             spoken("jerribeth", "Jerribeth", j, c("Continue", "vellexia")),
             spoken("vellexia", "Vellexia", '{n}Vellexia\'s reply arrives separately. '
                    'One phrase has been underlined hard enough to tear the paper.{/n}\n' + v,
                    c("Continue", "account")),
             n("account", "Narrator", '{n}You send back Vellexia\'s actual answer. '
               'Jerribeth keeps her offer; Vellexia keeps the right to judge it. '
               'Neither has promised anything beyond this ' +
               ('resumed business' if defected else 'business') + '.{/n}', c("Continue", flags=kept)),
             spoken("muddled", "Vellexia", '"You put words in her mouth, darling. '
                    'How tiresome. If I wanted a puppet show I would use the real thing." '
                    '{n}The second reply never comes. You have carried neither account intact.{/n}',
                    c("Continue", flags=flags(step + ".seen", step + ".failed", "account.muddled"))),
             n("declined", "Narrator", '{n}You leave the two replies apart. '
               'The crusade calls you back before either offer is answered.{/n}',
               c("Continue", flags=flags(step + ".seen", step + ".declined")))]
    req = [P + "ready"] + ([DEFECTION] if defected else [])
    no = list(flags(step + ".seen")) + ([] if defected else [DEFECTION])
    req += ["jerribeth.trickster.returned"] if mind else []
    no += ["jerribeth.trickster.cost.host"] if mind else ["jerribeth.trickster.returned"]
    if retry:
        req += list(flags("settle.failed"))
        no += list(flags("account.kept", "settle.declined"))
    return entry(step + "." + history + (".mind" if mind else ""), nodes,
                 requires=req, forbids=no, delay=48 if retry else 0)


SCENES = tuple(settlement(d, r, m) for r in (False, True)
               for d in (True, False) for m in (False, True))

# These are implementation candidates, deliberately not emitted by register().
# A one-visit flag is not a 152h bodily window. No invented stay gate or quest.
BODY_REQUIRES = ["jerribeth.present_now", "vellexia.present_now",
                 "jerribeth.trickster.visit_due", "vellexia.trickster.in_person"]
BODY_FORBIDS = ["jerribeth.trickster.returned", "jerribeth.trickster.visited",
                "vellexia.trickster.visited", "vellexia.trickster.kept_as_mirror"]


def candidate(step, nodes, deed, delay, forbids=()):
    body = entry(step, nodes, requires=BODY_REQUIRES + [P + deed],
                 forbids=BODY_FORBIDS + list(flags(step + ".seen")) + list(forbids),
                 delay=delay, category="pair")
    body["Forbids"] += ["jerribeth.harem.enmity.vellexia", "vellexia.harem.enmity.jerribeth"]
    body["ForbidOverrides"].update({"jerribeth.harem.enmity.vellexia": "jerribeth.harem.reconciled.vellexia",
                                   "vellexia.harem.enmity.jerribeth": "vellexia.harem.reconciled.jerribeth"})
    return body


def optional_candidates():
    company = candidate("company", [
        spoken("start", "Jerribeth", '"She did not send for me. I came because '
               'I found something amusing on the crusaders\' frontier. I want to '
               'see whether she laughs."',
               c('"I\'ll finish the audience business and leave you to it."', "company"),
               c('"Keep this to patronage."', "declined"), c('"Later."', abort=True)),
        spoken("company", "Jerribeth", '"One of your spies tried to buy my news. '
               'I sent him back with enough lies to keep him frightened for a week. '
               'The truth is for you." {n}She leans toward Vellexia rather than you.{/n}',
               c("Continue", "reply")),
        spoken("reply", "Vellexia", '"He cried. I wondered who had improved him. '
               'Come again, darling, when there is no audience to bore us. '
               'I have missed having a friend with such a nasty imagination."',
               c("Continue", flags=flags("company.seen", "company.both_friends",
                 "jerribeth.private_view_entrusted", "vellexia.personal_reply_kept",
                 "cost.jerribeth.unsummoned_visit_owned", "cost.vellexia.private_attention"))),
        n("declined", "Narrator", '{n}The private conversation ends with the business. '
          'Both women return to their own hunting.{/n}',
          c("Continue", flags=flags("company.seen", "company.declined")))], "account.kept", 48)
    company["HouseholdArcStart"] = True
    company["RequiresAnyGroups"] = [[P + "settle.kept", P + "retry.kept"]]
    invitation = candidate("invitation", [
        spoken("start", "Vellexia", '"Business first, darling. Then tell me why '
               'you stayed." {n}The audience has ended. Jerribeth remains beside '
               'Vellexia\'s chair, looking down at her.{/n}',
               c('"I\'ll leave you the private audience."', "stay"),
               c('"End the audience here."', "declined"), c('"Later."', abort=True)),
        spoken("stay", "Jerribeth", '"Because I wanted to. Do not spoil it by '
               'trying to summon me now." {n}Her hand settles on Vellexia\'s shoulder.{/n}',
               c("Continue", "invited")),
        spoken("invited", "Vellexia", '"Then stay. This invitation is for you, '
               'not for your discoveries beyond the Worldwound. I have had quite '
               'enough business tonight." {n}She turns her face toward the hand on her shoulder.{/n}',
               c("Continue", flags=flags("invitation.seen", "invitation.both_interested",
                 "business.audience_ended", "jerribeth.personal_stay_chosen",
                 "vellexia.personal_invitation_named"))),
        n("declined", "Narrator", '{n}The audience ends before a personal invitation '
          'is answered.{/n}', c("Continue", flags=flags("invitation.seen", "invitation.declined")))],
        "company.both_friends", 48)
    choice = candidate("choice", [
        spoken("start", "Vellexia", '"Your crusaders are waiting, Commander. '
               'Must I have someone throw you out?" {n}Jerribeth has moved behind '
               'her chair. Vellexia catches her wrist and draws it against her cheek.{/n}',
               c('"I\'ll clear the audience room."', "jerribeth_answer"),
               c('"Jerribeth, you have your own appointment."', "jerribeth_no"),
               c('"Vellexia, leave the personal invitation for another evening."', "vellexia_no"),
               c('"Keep this evening between friends."', "friends_only"), c('"Later."', abort=True)),
        spoken("jerribeth_answer", "Jerribeth", '"I know exactly what you want. '
               'For once, it happens to be what I want." {n}She bends and kisses '
               'Vellexia. Her grip tightens when Vellexia tries to pull her closer.{/n}',
               c("Continue", "vellexia_answer")),
        spoken("vellexia_answer", "Vellexia", '"Then stop making me wait." '
               '{n}She rises against Jerribeth\'s mouth, pulling her away from the '
               'audience chair. The door closes behind them.{/n}', c("Continue", "mutual")),
        n("mutual", "Narrator", '{n}Their audience is over. Neither woman follows '
          'the Commander out.{/n}', c("Continue", "explicit.1",
                                    flags=flags("choice.seen", "choice.both_yes", "choice.audience_cleared"))),
        n("explicit.1", "Narrator", '{n}The business audience is over. Jerribeth '
          'stays for the personal invitation.{/n}', c("Continue", "appointment")),
        spoken("appointment", "Jerribeth", '"I have an appointment of my own." '
               '{n}Her discarded things wait by the door. She leaves them there for now.{/n}'),
        spoken("jerribeth_no", "Jerribeth", '"Yes. My collection will not wait '
               'while she invents another reason to keep me. Another evening, Vellexia."',
               c("Continue", flags=flags("choice.seen", "choice.jerribeth_no"))),
        spoken("vellexia_no", "Vellexia", '"Quite. I am tired of entertaining '
               'people. Even you, darling. Come when I have had time to miss you."',
               c("Continue", flags=flags("choice.seen", "choice.vellexia_no"))),
        spoken("friends_only", "Jerribeth", '"We still have that spy to laugh at. '
               'Sit down, Vellexia. I have not told you what he offered me."',
               c("Continue", flags=flags("choice.seen", "choice.friends_only")))],
        "invitation.both_interested", 48)
    choice["Requires"] += list(flags("company.both_friends"))
    morning = candidate("morning", [
        spoken("start", "Jerribeth", '"My appointment, remember? The crusaders '
               'are marching again. I intend to reach my quarry before they do." '
               '{n}She gathers her things. Vellexia watches from the bed.{/n}',
               c('"Leave her to her appointment."', "end"), c('"Later."', abort=True)),
        spoken("end", "Vellexia", '"Go, then. Bring me the amusing parts. '
               'Keep the rest for yourself — I would hate you to become predictable." '
               '{n}Jerribeth brushes her mouth with a last kiss and leaves. '
               'Vellexia does not call her back.{/n}',
               c("Continue", flags=flags("morning.seen", "morning.appointment_kept")))],
        "choice.both_yes", 8)
    return (company, invitation, choice, morning)


OPTIONAL_CANDIDATES = optional_candidates()


def register(payload, scenes, refs):
    """Append only the separate-channel settlement; do not activate bodily candidates."""
    derived = payload.setdefault("Derived", {})
    derived[P + "ready"] = [["jerribeth.harem.eligible", "vellexia.harem.eligible",
                              "jerribeth.reachable_by_letter", "vellexia.reachable_by_letter"]]
    ids = {s["Id"] for s in scenes}
    scenes.extend(copy.deepcopy(s) for s in SCENES if s["Id"] not in ids)
    # The engine owns the SeenCue, eligibility, epochs, allowances and all attitudes.
    # Registering into a completed payload also supplies the historical Ledger reader.
    ledger = payload.get("Books", {}).get("trickster.ledger")
    if ledger is not None and not any(e["Id"] == P + "account" for e in ledger["Entries"]):
        ledger["Entries"].append(dict(
            Id=P + "account", Section="Seating Notes", Portrait="Jerribeth",
            Title="Vellexia and her client", Text="{n}Vellexia is the patron; Jerribeth is her client.{/n}",
            Requires=["foresight.page_taken"], Forbids=[], AnyGroups=[], Lines=[
                dict(Text="{n}Jerribeth named her defection; Vellexia answered the resumed business.{/n}",
                     Requires=list(flags("account.kept", "defection.answered")), Forbids=[], AnyGroups=[]),
                dict(Text="{n}The patron's account was answered. There had been no defection to pardon.{/n}",
                     Requires=list(flags("account.kept", "client.account_named")), Forbids=[], AnyGroups=[]),
                dict(Text="{n}I failed to carry both accounts accurately.{/n}",
                     Requires=list(flags("account.muddled")), Forbids=list(flags("account.kept")), AnyGroups=[]),
                dict(Text="{n}The patronage account was left standing.{/n}", Requires=[], Forbids=[],
                     AnyGroups=[list(flags("settle.declined", "retry.declined"))]),
                dict(Text="{n}The patron and her client have not answered the present account.{/n}",
                     Requires=[], Forbids=list(flags("settle.seen")), AnyGroups=[])]))
