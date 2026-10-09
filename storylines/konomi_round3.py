"""Authored audit repairs: settlement, physical receipts and continuous staging.

No new price or appointment. Anevia's existing Drezen contact hosts the two
invitation setups and arrival receipts. Recovery retains its required runtime
delivery mode, leaving each complete history within its chapter mailbag budget.
Native contact: AneviaTirabade_DrezenCapital b5e867e13503c6f41bb1316705efb4a2,
NPC_Common/Anevia/AnswersList_0003 33960c7f7af40cd43b7f801a76c87a0b.
"""
import copy

from story_format import c, p

K = "konomi.trickster."


def integrate(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}

    def page(sid):
        return by["konomi." + sid]

    def node(sid, nid):
        return next(n for n in page(sid)["Nodes"] if n["Id"] == nid)

    def text(sid, nid, value):
        node(sid, nid)["Text"] = value.strip()

    # A paid reserve and an outstanding personal favour are different histories.
    morning = node("trickster.dismissed.private", "morning")
    morning["Choices"][0]["Text"] = '"After breakfast, then. I want to read your letter with you."'
    favour = copy.deepcopy(morning)
    favour["Id"] = "morning_favour"
    favour["Text"] = '''{n}At dawn she wears your shirt at the desk. A dispatch to Nerosyan lies beside a separate sheet folded inward. She moves the private sheet under her fan when you approach.{/n}
"The Chancellor gets my assessment of Drezen's stores. He would have preferred your endorsement. I shall explain why he has not got it."
{n}She leans back against you before finishing the dispatch.{/n}
"Your favour is still mine to name. The other sheet is yours. Break its seal after breakfast. I want to see your face."'''
    page("trickster.dismissed.private")["Nodes"].append(favour)
    cut = node("trickster.dismissed.private", "konomi.trickster.dismissed.private.explicit.1")
    cut["Choices"][0]["Requires"].append(K + "debt_paid")
    cut["Choices"].append(c("Continue", "morning_favour", forbids=(K + "debt_paid",)))

    # The check concerns his motive, which the driver cannot establish. Failure
    # exposes the pretence; it does not increase the already identical price.
    bluff = next(ch for ch in node("trickster.dismissed.recess", "price")["Choices"] if ch.get("Check"))
    bluff["Text"] = '[Lie] "I expected you to refuse the detour. You surprised me."'
    node("trickster.dismissed.recess", "price")["Choices"][1]["Text"] = '[Tell her the truth] "I hoped you would take the road. I wanted you back."'
    text("trickster.dismissed.recess", "price", '''"The driver told me at the fork. A paid road back to the Commander who dismissed me. I could have hired another carriage."
{n}She brushes charcoal dust from her sleeve onto your minute.{/n}
"I wanted to see what you expected to accomplish. Well?"''')
    text("trickster.dismissed.recess", "truth", '''"That was plain enough at the fork. I wanted to hear you say it."
{n}She folds the fan against her palm.{/n}
"I chose to come and collect. You may begin regretting the invitation."''')
    text("trickster.dismissed.recess", "outfoxed", '''"You expected me to refuse? With an invitation already waiting at the council table?"
{n}She sits behind the desk.{/n}
"You wanted me here badly enough to buy the road. At least have the courage to admit it. Nerosyan will have the same account either way; this foolishness is between us."''')
    # Success and admission converge on the same political bargain deliberately.
    node("trickster.dismissed.recess", "read")["Text"] = node("trickster.dismissed.recess", "read")["Text"].replace(
        '"Very well, let us talk price."', '"Whether you expected me or not, I am here. Very well, let us talk price."')

    # Keep elapsed travel and all original arrival/recovery receipts. The existing
    # spymaster contact can report an arrival before Konomi's actor is unhidden.
    entries = {
        "trickster.dismissed.arrival": '"Any news from the east gate?"',
        "trickster.never_arrived.arrival": '"Has Nerosyan answered the invitation?"',
        "trickster.dismissed.late": '"Is Lady Konomi\'s carriage still at the gate?"',
        "trickster.never_arrived.accredited": '[Ask about the unused chair at the council.]',
    }
    for sid, entry in entries.items():
        host = page(sid)
        host.update(Remote=False, Entry=entry,
                    ContactUnit="b5e867e13503c6f41bb1316705efb4a2",
                    AnswerLists=["33960c7f7af40cd43b7f801a76c87a0b"])
    text("trickster.dismissed.arrival", "start", '''{n}At the citadel, Anevia hands you the gate sergeant's receipt. Two days after you paid the driver, the Nerosyan carriage has returned. She points out the driver's account beneath the arrival time: at the fork he admitted who bought his detour. Lady Konomi told him to take it, then spent the journey questioning him.{/n}
{n}Anevia sends the sergeant back to his watch. Konomi has gone to inspect the council minute. Her driver has gone to find a priest.{/n}''')
    text("trickster.never_arrived.arrival", "start", '''{n}Four days after the dispatched invitation, a chancery clerk brings Konomi's arrival receipt to Anevia's briefing. Anevia checks the east-gate time before handing it to you. Lady Konomi has arrived with her credentials.{/n}
{n}The capital's register accepted your reported bow; she crossed out its presumption that she had already travelled, then chose to come and present the papers herself. The clerk has been sent for tea and for you, in that order.{/n}''')
    setup = node("trickster.dismissed.late", "start")
    setup["Text"] = ('{n}As the citadel briefing ends, Anevia hands you the gate sergeant\'s report. She points out the hour beside the driver\'s name.{/n}\n' + setup["Text"])
    setup = node("trickster.never_arrived.accredited", "start")
    setup["Text"] = ('{n}Anevia brings you into the council chamber, then takes the watch reports back to her desk.{/n}\n' + setup["Text"])

    # Journey duration and the informer choice must agree with their setup clocks.
    for host in payload["Scenes"]:
        if host.get("Relationship") == "konomi":
            for part in host["Nodes"]:
                part["Text"] = part["Text"].replace("three days of charcoal smoke", "two days of charcoal smoke")
    node("trickster.never_arrived.accredited", "slip")["Choices"][0]["Text"] = '[Let him go up to his dovecote. At the recess, give him something worth sending.]'

    # The rival's dispatch is already folded away. Her coat-grip initiates the
    # encounter; there is no account in the Commander's hand or counting exercise.
    approach = '''{n}She keeps her grip on your coat and walks you backward to the desk. Her rings come off into the inkwell lid, one at a time. You loosen her robe.{/n}
"Two days. I shall not spend another evening waiting."
{n}She seats you on the cleared wood. Her hands slide inside your coat, then tug it from your shoulders. She settles across your lap and kisses you until she has to stop for breath.{/n}
"There. A much better use of your mouth."
{n}The robe hangs open now, and under it she is bare and warm and quick-breathing, the silk gathered round her hips. She guides your hands up her ribs herself and holds them there, and when your thumbs find her she shuts her eyes and says a word no chancery would ever have minuted. When she opens them the careful envoy is gone.{/n}
"Do not stop to be clever," {n}she says, unsteady.{/n} "I will know, and I shall be unbearable about it."
{n}Her hand grips the back of your neck. She presses you back onto the desk and follows, her mouth still on yours.{/n}'''
    text("trickster.never_arrived.second_supper", "accept", approach)
    # Retained rooms/accept is reachable from an older in-flight answer. It must
    # also keep continuous staging, without taking away its original receipts.
    text("trickster.never_arrived.rooms", "accept", approach.replace("Two days. I shall not spend another evening waiting.", "Supper is over. I have something else in mind."))

    # Each slot starts where its approach actually ends, and stops at act onset.
    defaults = {
        "evening": "{n}On the cushions she keeps you close, her hand firm at the back of your neck. She breaks the kiss to catch her breath, then reaches between you.{/n}",
        "trickster.never_arrived.rooms": "{n}Above you on the desk, she releases your mouth and looks down into your face. Her hand slips to your hip; she draws closer.{/n}",
        "trickster.never_arrived.second_supper": "{n}Above you on the desk, she releases your mouth and looks down into your face. Her hand slips to your hip; she draws closer.{/n}",
        "trickster.dismissed.private": "{n}She keeps your wrists against the desk. Her hair brushes your cheek as she bends to kiss you again, then pauses close enough that you feel her unsteady breath.{/n}",
        "trickster.dismissed.a_season": "{n}Still astride your lap, she works the belt free and lets it fall beside the chair. She braces a hand on your shoulder and draws closer.{/n}",
        "chosen_evening": "{n}She stays over you on the bed, her loose hair against your chest. When you draw her closer, she answers with a breathless kiss and an impatient hand at your hip.{/n}",
        "the_evening_she_kept": "{n}She stays over you, watching your face as your hands move along her bare sides. Her fingers tighten on your shoulder; she bends to kiss you and draws closer.{/n}",
        "private_last_visit": "{n}Astride your hips, she leans down to kiss you again. Her hand closes over yours on her waist. For once she has no remark ready; she draws closer instead.{/n}",
    }
    for sid, value in defaults.items():
        slot = next(n for n in page(sid)["Nodes"] if ".explicit." in n["Id"])
        slot["Text"] = value
    node("evening", "stay")["Choices"][0]["Text"] = '[Stay close to her.]'

    # Sweep every epilogue copy, including the appended postwar retry. An envoy
    # offer, not a failed check, earns appointment language. Preserve corrections.
    for host in payload["Scenes"]:
        if host.get("Relationship") != "konomi" or host.get("Owner") != "Epilogue":
            continue
        for part in host["Nodes"]:
            for paragraph in part.get("Paragraphs", []):
                if "new envoy to Drezen had been appointed" in paragraph["Text"]:
                    if K + "envoy" not in paragraph["Requires"]:
                        paragraph["Requires"].append(K + "envoy")
                    part["Paragraphs"].append(p(
                        "{n}In Nerosyan they heard how the Commander had paid for Konomi's return and then claimed to have expected a refusal. She supplied the driver's account when anyone asked. She had chosen the road herself.{/n}",
                        requires=(K + "recessed", K + "cost.outfoxed"), forbids=(K + "envoy",)))
                if "column four still reads" in paragraph["Text"]:
                    paragraph["Text"] = "{n}The Royal Council's register kept the dovecote's mistaken entry, 'credentials presented, Drezen', beside Konomi's signed correction: invitation received, credentials presented four days later. Every spring an auditor copied the first line without the second. She returned the query with the correction underlined.{/n}"
                if "billed the crown for three days" in paragraph["Text"]:
                    paragraph["Text"] = "{n}Lady Konomi reached Nerosyan when her work in Drezen allowed it. Her account distinguished the two days on the charcoal road from the days she had chosen to stay. The Chancellor received both council minutes.{/n}"
                if "political terms of its collection" in paragraph["Text"]:
                    paragraph["Requires"] = [K + "favour_owed", "konomi.lastcall.terms_accepted"]
                    part["Paragraphs"].append(p(
                        "{n}Her Threshold dispatch named the price of the favour: a permanent seat for Nerosyan. The Commander had not accepted it. The favour remained outstanding; she kept the demand with her official correspondence and her personal letters under a separate seal.{/n}",
                        requires=(K + "favour_owed", "konomi.lastcall.called"),
                        forbids=("konomi.lastcall.terms_accepted",)))
