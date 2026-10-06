"""Authored Konomi situations, round 2; native anchors and limits in route_packs/plans.

The atlas reservation remains bargain / attaché office after recess / sealed letters
and public Crown dissent. This pass changes only Konomi's entries. Shared Last Call
and household consumers remain coordinator work. No page grants her affection.
"""
import copy

from story_format import c, n, p, scene

K = "konomi.trickster."
ROAD_SENT = K + "road_sent"
REPORT_SENT = K + "report_sent"
SECOND = K + "second_supper_invited"
DREZEN = "2570015799edf594daf2f076f2f975d8"
UNIT = "ca2d58c5c65723945857e04fb85d30ce"
HUB = "0dc8b8604bb33c846a63f3eb62443674"


def integrate(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}

    def page(sid):
        return by["konomi." + sid]

    def node(sid, nid):
        return next(x for x in page(sid)["Nodes"] if x["Id"] == nid)

    def text(sid, nid, value):
        node(sid, nid)["Text"] = value.strip()

    def retire(answer):
        # The source answer, its index, effects and destination survive old saves.
        answer["Forbids"].append("trickster.ever")

    def add(sid, nid, value, *answers):
        result = n(nid, "Konomi", value, *answers, portrait="Konomi")
        page(sid)["Nodes"].append(result)
        return result

    # SP4 access: dispatch now, physical arrival after the purchased journey.
    sid = "trickster.dismissed.late"
    page(sid)["DelayHours"] = 0
    text(sid, "start", '''{n}Konomi's carriage waits below the east wall, at the lodging where her driver has been seeking the missing Crown escort. Highwaymen have made the capital road expensive. Nerosyan's pennant hangs above curtains she has kept shut since leaving the citadel.{/n}
{n}The gate sergeant has sent word: the driver is watering his horses before taking the unescorted road. There is still time to reach him.{/n}''')
    text(sid, "minute", '''{n}The curtain stirs at your shout, then falls shut. At the council table the attaché's chair is empty. The clerk has the minute of her dismissal before him.{/n}''')
    text(sid, "record", '''{n}The clerk puts the dismissal beside a fresh sheet, unwilling to erase either record.{/n}
"A further audience, Commander? She has not agreed to one."
{n}His pen waits above the page.{/n}''')
    text(sid, "driver", '''{n}The rider carries an invitation to conclude the adjourned audience. The dismissal remains on the previous sheet.{/n}
{n}At the post-house the driver shows you the charcoal road: two days through the hills, returning to Drezen. He will offer her the detour at the fork. She can dismiss him and hire another carriage; your silver buys his offer and the journey, whichever road she chooses.{/n}''')
    driver = node(sid, "driver")
    retire(driver["Choices"][2])
    driver["Choices"].append(c('[Pay for the detour] "Offer her the charcoal road. Tell her whose silver bought it."',
        crusade=("Finances", -150), flags=(K + "primed", K + "cost.late", "konomi.started", K + "cost.driver_paid", ROAD_SENT)))
    # Legacy gate remains reachable only from a save already inside the old setup.
    text(sid, "gate", '''{n}The gate sergeant's receipt records her carriage coming back two days after the driver's departure. Konomi chose the charcoal road. She has asked to see the council minute before answering the invitation.{/n}''')
    text("trickster.dismissed.arrival", "start", '''{n}Two days after you paid the driver, the gate sergeant sends a note: the Nerosyan carriage has returned. At the fork the driver admitted who bought his detour. Lady Konomi told him to take it, then spent the journey questioning him. She has gone to inspect the minute. He has gone to find a priest.{/n}''')
    text("trickster.dismissed.recess", "start", '''{n}The carriage has just returned by the east gate. Konomi stands in her former office, travelling cloak still on. The two council minutes lie together on the desk: dismissal, then an invitation to conclude an adjourned audience.{/n}
{n}She lays her fan across them and watches you enter.{/n}''')
    text("trickster.dismissed.recess", "price", '''"The driver told me at the fork. A paid road back to the Commander who dismissed me. I could have hired another carriage."
{n}She brushes charcoal dust from her sleeve onto your minute.{/n}
"I wanted to see what you expected to accomplish. Now I have seen it. You will tell me it was chance."''')
    text("trickster.dismissed.recess", "truth", '''"Yes. He confessed before I could ask why the horses were facing west."
{n}She folds the fan against her palm.{/n}
"I chose to come and collect. You may begin regretting the invitation."''')
    terms = '''"Very well, let us talk price."
{n}She lifts your invitation by one corner.{/n}
"The Chancellor will receive both minutes: a dismissal followed by a paid invitation back. I could leave tonight. Instead I shall put that eagerness to use. My capital needs influence here more than it needs my attendance at another quarrel."
"I stay until we have settled the political account. Do not mistake that for an answer to any other question."'''
    for nid in ("read", "read_outfoxed"):
        text("trickster.dismissed.recess", nid, terms)
    text("trickster.dismissed.recess", "outfoxed", '''"Chance. How tiresome."
{n}She sits behind the desk.{/n}
"The driver showed me the road and your purse at the fork. I came to watch you work, not to hear you lie badly afterwards. Now I set the price."''')

    # Both Dorgelinda siblings consume the actual outcome, never merely 'primed'.
    audit = "dorgelinda.trickster.cost.audit"
    abyss = "dorgelinda.trickster.cost.abyss_signed"
    books = "dorgelinda.trickster.cost.tribunal_books"
    for suffix, effects in (("", (K + "recessed", K + "cost.debt_owed")),
                            ("_outfoxed", (K + "recessed", K + "cost.debt_owed", K + "cost.outfoxed"))):
        root = node("trickster.dismissed.recess", "read" + suffix)
        root["Choices"][0]["Forbids"] = [audit, abyss, books]
        root["Choices"][1]["Requires"] = [audit]
        root["Choices"][1]["Forbids"].extend([abyss, books])
        text("trickster.dismissed.recess", "read" + suffix + "_ledger", '''{n}She taps the folded minute with her fan.{/n}
"Your quartermaster tells me the tribunal put a warehouse into your personal account. I shall want to know whose account holds the grain before I recommend spending it."''')
        root["Choices"].extend([
            c("Continue", "read" + suffix + "_abyss", requires=(abyss,), forbids=(books,)),
            c("Continue", "read" + suffix + "_books", requires=(books,))])
        add("trickster.dismissed.recess", "read" + suffix + "_abyss", '''"Your quartermaster sent the signed shortage into the Abyss. An ingenious destination for a disputed account. Unfortunately, my capital will still expect its deliveries."
{n}She opens her fan.{/n} "Let us keep this price on a road both of us can use."''', c('"Name it."', flags=effects))
        add("trickster.dismissed.recess", "read" + suffix + "_books", '''"Your quartermaster has promised the tribunal a later review of the books. I shall read the result when there is one. Until then, I will bargain over what you actually hold."''', c('"Name it."', flags=effects))

    # SP4 political price: existing debit buys the reserve, not a fictional embargo.
    for nid in ("paid", "paid_envoy"):
        text("trickster.dismissed.terms", nid, '''{n}She reads your endorsement, corrects its grammar and seals it. Beside it lies the quartermaster's receipt for the provision reserve: five hundred Finances, covering deliveries now disputed by the Crown's opponents.{/n}
"Your nobles will call this surrender. Nerosyan will call it overdue. The reserve buys time while they argue; it does not buy their agreement."
"My name remains on the recommendation. You will find me very hard to dismiss twice."''')
    text("trickster.dismissed.terms", "price", '''{n}She sets one sheet beside the quartermaster's estimate.{/n}
"An endorsement in your hand for restoring the Royal Council your nobles arrested. Five hundred Finances for a provision reserve against the deliveries that endorsement will put in dispute. The letter buys Nerosyan an argument; the reserve keeps that argument from emptying Drezen's stores."
"Or offer me a favour of your own. Not a promise made on the army's behalf."''')
    text("trickster.dismissed.supper", "letter", '''"The endorsement is sealed, and your quartermaster has the reserve money. You have paid the political price."
{n}She moves the bottle within your reach.{/n}
"Tonight I want the answer you kept out of the letter."''')
    text("trickster.dismissed.supper", "favour", '''"I still hold your favour. I shall choose its occasion."
{n}She sets the cup down and looks directly at you.{/n}
"This evening was my invitation. Why did you want me back?"''')

    # SP4 turning point: all romantic answers hear and accept the original debt.
    privacy = '''"My letters travel under my seal. Nobody in your chancery opens them: not your clerks, not your spymaster, not you. My council chair is mine, not a place at your pleasure. If you want me gone again, you tell me behind a closed door."'''
    for nid in ("answer", "courted"):
        original = node("trickster.dismissed.private", nid)
        original["Text"] = ('''{n}She lays the fan across the closed ledger. Below the window the watch changes; she waits until the boots have passed.{/n}
"I stay on my own account. I wanted that supper, and I want another evening with you. First, hear what you are agreeing to."
''' + privacy)
        original["Choices"][0]["Text"] = '[Take her hand] "Your seal, your chair, a private door. All of it."'
    text("trickster.dismissed.private", "morning", '''{n}At dawn she wears your shirt at the desk. A dispatch to Nerosyan lies beside a separate sheet folded inward. She moves the private sheet under her fan when you approach.{/n}
"The Chancellor gets my assessment of Drezen's reserve and your endorsement. That will keep him occupied."
{n}She leans back against you, briefly, before finishing the official dispatch.{/n}
"The other is yours. Break its seal after breakfast. I want to see your face."''')
    text("trickster.dismissed.a_season", "price", privacy + '''
"And once at the council table you will hear my refusal. Put the winter levy to me. I oppose it; I will tell the lords why. You will take the answer and move to the next business, with no joke to swallow it."''')
    node("trickster.dismissed.a_season", "price")["Choices"][0]["Text"] = '"Your sealed letters, your chair, a private door. And the public refusal."'
    page("trickster.dismissed.a_season")["DelayHours"] = 72
    text("trickster.dismissed.a_season", "council", '''{n}She rejects the winter levy in four crisp sentences: the frontier's stores cannot absorb it. You thank her and move to the next business. Three lords keep staring.{/n}
{n}She backs the provision reserve instead, reading the quartermaster's actual figures. Under the table her foot rests against your boot. Her recommendation does not change.{/n}''')

    # SP2 accredited access: the report goes out now. It cannot bring her now.
    sid = "trickster.never_arrived.accredited"
    page(sid)["DelayHours"] = 0
    text(sid, "bow", '''{n}At the council recess the steward sets a cup beside the unused chair. The report slip waits in his pocket. You have time to give him a better item for it.{/n}''')
    text(sid, "nerosyan", '''{n}The jug receives your bow. The steward watches without smiling. In the dovecote you find him fastening his report to a bird's leg.{/n}
{n}He takes back the slip you found. It is in the same hand as the capital's reports. There is room beneath tonight's council business for an invitation.{/n}''')
    dispatch = node(sid, "nerosyan")
    for answer in dispatch["Choices"]:
        retire(answer)
    dispatch["Choices"].append(c('[Pay for the invitation] "Add my bow to the jug. Ask Lady Konomi to judge the welcome herself."',
        "dispatch_receipt", crusade=("Finances", -100), flags=(K + "primed", K + "cost.accredited", "konomi.missed_letter_sent", "konomi.started", K + "cost.steward_paid", REPORT_SENT)))
    add(sid, "dispatch_receipt", '''{n}He names his price and adds the line. The bird goes out over the lower town. The empty chair stays empty.{/n}
"She may answer," {n}he says.{/n} "She may send you the jug's credentials in return."''', c('"Then we wait for her answer."'))
    text("trickster.never_arrived.arrival", "start", '''{n}Four days after the dispatched invitation, the chancery clerk sends a note. Lady Konomi has arrived with her credentials. The capital's register accepted your reported bow; she crossed out its presumption that she had already travelled, then chose to come and present the papers herself.{/n}
{n}She has asked for tea and for you, in that order.{/n}''')
    page("trickster.never_arrived.arrival")["DelayHours"] = 96
    fallback = page("trickster.never_arrived.audience_letter")
    fallback["DelayHours"] = 96
    fallback["Forbids"].append("konomi.trickster.never_arrived.audience")
    text("trickster.never_arrived.audience", "start", '''{n}Lady Konomi stands beside the office's unused chair. She puts her credentials over the dovecote's report, covering the line about the jug.{/n}
"Lady Konomi, attaché of Nerosyan. You may receive these from me now."
{n}She lifts the report from under the scroll.{/n}
"The register accepted your reported bow. I corrected its entry before leaving: an invitation is not an arrival. Then I came to see who could find our postman and waste his services on crockery."
{n}She takes the cup the chancery boy brings without looking away from you.{/n}
"My journey and the reception I left cost two hundred Finances. Drezen also owes the stipend transferred here: fifty. You may pay the journey now or settle the whole account later. I shall keep the credit."
"Your invitation made me curious, Commander. Do not confuse that with being obliged."''')

    # SP2 account arithmetic; no additional obligation or surcharge.
    rooms = "trickster.never_arrived.rooms"
    node(rooms, "start")["Choices"][0]["Crusade"]["Amount"] = -250
    node(rooms, "haggle")["Choices"][0]["Crusade"]["Amount"] = -225
    text(rooms, "start", '''{n}She turns the account toward you: journey and missed reception, two hundred; transferred stipend, fifty. Any sum paid at her audience is struck through.{/n}
"Two hundred and fifty in all. Or fifty remaining, if you paid the journey. You may argue over the stipend. I have left room for the argument."
{n}The chancery boy waits beyond the door with supper. She has ordered two places.{/n}''')
    text(rooms, "haggle", '''"My line, Commander. I should charge for its use."
{n}She concedes twenty-five from the stipend and keeps the two hundred for travel and the missed reception. Two hundred and twenty-five in all. She draws a line under the sum.{/n}''')
    text(rooms, "haggle_rest", '''"You have paid the two hundred. That stays struck through."
{n}After an argument she concedes twenty-five from the stipend. You owe twenty-five more. She writes the agreed total beside the credit.{/n}''')
    text(rooms, "supper_who", '''"That takes longer than a journey account."
{n}She refills your cup and tells you what she missed at the reception: a rival's promise of deliveries nobody had secured. She means to enjoy the rival's explanation when the next dispatch arrives.{/n}
"You can have that news at another supper, if you want it."''')
    text(rooms, "stay", '''{n}The boy collects the plates. Konomi opens the door herself, then comes back for her fan.{/n}
"Another supper. Two evenings from now. I shall have a dispatch to laugh at, and you may have learned a better answer."
{n}She catches your sleeve as you stand.{/n}
"I am inviting you, Commander. The political account is closed."''')
    old = node(rooms, "stay")["Choices"][0]
    retire(old)
    node(rooms, "stay")["Choices"].extend([
        c('"Two evenings from now."', flags=(SECOND,)),
        c('"Keep the next meeting to business."', "business", flags=(K + "envoy",)),
        c('"Write when we can arrange it."', flags=(SECOND,))])
    # Reuse the old accept/morning IDs and their receipts, now after a later choice.
    later = copy.deepcopy(page(rooms))
    later.update(Id="konomi.trickster.never_arrived.second_supper", Title="The second invitation", Entry='"You promised me news."',
        Requires=["trickster.ever", K + "returned", K + "cost.accredited", SECOND, "konomi.present_now"],
        Forbids=["konomi.closed", "inhuman", K + "envoy", K + "rooms_kept", "konomi.private_departed", "konomi.dead.unreturned", "konomi.presence.failed"],
        DelayHours=48, Nodes=[])
    later["Nodes"].append(n("start", "Konomi", '''{n}The dispatch lies open beside supper. The promised wagons never left the capital; Konomi has written her rival a question with no polite escape in it. She reads it to you, delighted, then folds the sheet away.{/n}
"That is for tomorrow's post. This evening is for me."
{n}She sends the boy away, sets her fan aside and catches the front of your coat.{/n}
"I want you to stay. You may spend another hour talking if you must. I have spent two days thinking about doing something else."''',
        c('[Stay with her.]', "accept", flags=(K + "rooms_kept",)),
        c('"Keep this to business, Konomi."', "business", flags=(K + "envoy",)),
        c('"Another evening. I want to have time for you."', abort=True), portrait="Konomi"))
    # Copies retain old destination identities locally; slot uses the planned full ID.
    later["Nodes"].extend(copy.deepcopy(node(rooms, nid)) for nid in ("accept", "morning", "business"))
    payload["Scenes"].append(later)
    by[later["Id"]] = later
    for target in (rooms, "trickster.never_arrived.second_supper"):
        text(target, "morning", '''{n}At dawn your coat hangs over her chair. Konomi holds the supper account and a dispatch to Nerosyan apart.{/n}
"The boy put our dinner against council hospitality. I caught it before collection. The wine goes on the private supper account we agreed. The Council does not pay for my evenings."
{n}She corrects the line, then reaches inside your open coat and draws you down for a kiss.{/n}
"Next week. Bring a better argument, and do not make me wait for the kiss."''')

    # SP1 invitation and SP3 political near-discovery/inspection, copied histories too.
    text("reception", "private", '''{n}Konomi takes you beneath the covered walk. Her nearly untouched glass stays inside; the guests are still disputing the winter deliveries.{/n}
"Ten minutes is enough for them to decide I am speaking to somebody useful. They may keep the explanation."
{n}She turns toward you, close enough that her sleeve touches your coat.{/n}
"I wanted to hear you without an audience. What did you want?"''')
    for sid in ("leak", "private_leak"):
        if "konomi." + sid in by:
            opening = node(sid, "start")
            opening["Text"] = '''{n}A clerk reaches for the enclosure among Konomi's council dispatches. She takes it first. The copied passage has your familiar seal beneath somebody else's annotations.{/n}
"The dispatch concerns the reserve. This concerns what I did after supper. Somebody has decided Nerosyan should receive both."
{n}She waits until the clerk leaves.{/n}
"They mean to make my advice look bought. We shall answer the accusation. They do not get the rest of my letters."'''
    for sid in ("reckoning", "private_reckoning"):
        if "konomi." + sid in by:
            text(sid, "audit", '''"Its scope. The secretary gets my published recommendation and the figures behind it. He has received them. They show the reserve I actually advised, not the cheaper figure he preferred."
{n}She lays his request for the private enclosures beneath her refusal.{/n}
"My hostess has agreed to repeat that distinction at her next dinner. He can challenge my figures there. Let him explain what he expected to learn from my bedroom."''')
    for sid in ("political_account", "private_political_account"):
        if "konomi." + sid in by:
            if sid == "political_account":
                text(sid, "start", '''{n}Konomi puts her recommendation to Nerosyan beside your chair.{/n}
"Keep the frontier reserve here until the road deliveries are confirmed. I sent that to the capital's provisioning office. The recipient wanted the opposite answer."
{n}She sets a second cup beside it.{/n}
"Read it before supper. I would rather hear your objection than have you discover it in somebody else's dispatch."''')
    text("power", "limits", '''"The winter levy. I oppose it. Drezen cannot strip its reserve while highwaymen decide which wagons reach the frontier. I will argue that in council, and lean on every noble who owes me a favour."
{n}She tears the supper copy in half. The signed recommendation stays in her writing case.{/n}
"Tonight I want you here. Tomorrow I want the levy defeated. You may give me a worse argument then."''')

    # SP5 real travel, remembered separation and an earned bodily reunion.
    for sid, hours in (("capital_letter", 120), ("return_offer", 72), ("private_reunion", 96)):
        page(sid)["DelayHours"] = hours
    text("private_departure", "kiss", '''{n}She puts her bag on the wagon step and kisses you again. Behind her Vanna checks the harness; Selis calls the driver over to a loose strap. Konomi keeps her hand inside your collar until the fastening is done.{/n}
"Now I really must go. Write to the address I gave you. I want an answer waiting when I arrive."''')
    for sid in ("private_reunion", "private_absence_catchup"):
        if "konomi." + sid in by:
            text(sid, "absence_kiss", '''{n}She catches your sleeve and kisses you with an impatience absent from her letters. Afterwards she straightens your collar, then smooths her own sleeve before reaching for the fan.{/n}
"I had a very good opening prepared. You may hear it when I remember it."''')
    text("the_courtyard_introduction", "lover", '''{n}She draws your joined hands down between you, out of the courtyard's view.{/n}
"I nearly declined your invitation. Then I remembered how many things I still wanted to say to you. Begin by listening."''')
    plans = node("the_evening_she_kept", "plans")
    plans["Text"] = plans["Text"].replace("Her hand settles at the back of your neck.",
        "She hooks a finger under your collar and pulls you away from the desk.")
    text("chosen_evening", "morning", '''{n}At breakfast her travelling case is still open. Konomi takes bread from your hand, then sets the plate between you.{/n}
"I leave after the next post. I want you here before it, if the council does not swallow the morning."
{n}She writes the date of her next intended visit on a separate sheet and puts it by your cup.{/n}
"Answer before I buy the fare. I have clients who pay enough to deserve a refusal in good time. So do you."''')
    text("trickster.dismissed.react_kyado", "start", '''{n}Kyado has heard the driver's confession. He puts the man's offering aside when you mention Konomi.{/n}
"I warned you about your tricks in the temple. This one needed horses."
"He told her whose silver bought the detour. She took it anyway. Erastil keeps roads for honest travellers; I told him he ought to begin by telling the passenger where he means to go. He says she asked worse questions than I did."''')
    text("trickster.never_arrived.react_regill", "start", '''"You found Nerosyan's informer and paid him to carry an invitation. Lady Konomi has presented her credentials herself. That part is settled."
{n}Regill folds the report.{/n}
"The informer remains. I want to know what else passes through that dovecote. You have bought a message, Commander, not the man's loyalty."''')
    text("trickster.dead_retained.react_regill", "start", '''{n}Regill closes the report when the envoy's name is mentioned.{/n}
"The attaché is alive. I accept the correction. Four unidentified civilians held a rite in your council chamber while its clerk was outside. I do not accept the unguarded door. Double its watch, or I will."''')

    # SP6 the postwar offer comes from her house, after an actual homeward journey.
    text("trickster.epilogue.commit", "offer", '''{n}After the war Konomi returned to her house in Nerosyan. Her official reports continued to argue the capital's interests. A separate courier brought the Commander a personal proposal, sealed in her own wax.{/n}
{n}She asked for another season of visits and evenings, with neither permitted to cancel the other's work by command. Below it she had added: 'I intend to see your answer. Send a date with it.'{/n}''')
    text("trickster.epilogue.commit", "signed", '''{n}The Commander rode to her house in Nerosyan and answered at the door. Konomi laughed and drew the visitor inside before the greeting was finished. Her waiting secretary lowered his unopened appointment book.{/n}
{n}Her next journey to Drezen was arranged before breakfast. She kept her rooms, seal and council opinions; the Commander received a sharp recommendation two days before the visit and an impatient private note the day after it.{/n}''')
    text("trickster.epilogue.commit", "terms", '''{n}The Commander returned the proposal with a clause: neither could recall the other from a promised visit. Konomi sent her answer and a departure date. Several days later her carriage reached Drezen.{/n}
{n}She read the clause aloud in the doorway, put her case down and asked when supper would be ready. On her next return to Nerosyan she took the agreed copy. The visits continued; so did the political arguments.{/n}''')
    refused = page("trickster.epilogue.refused")
    refused["Forbids"].append("konomi.closed")
    # Preserve the old Continue's exact identity/effects. New postwar exits append.
    start = node("trickster.epilogue.refused", "start")
    start["Choices"][0]["Id"] = "continue"
    for earned, excluded in ((K + "supper_asked", ()), ("konomi.lovers", (K + "supper_asked",))):
        start["Choices"].append(c('[Ask again, granting her seal, chair and private door.]', "postwar_price",
            requires=(K + "terms_settled", K + "recessed", earned),
            forbids=(K + "envoy", "konomi.dead.unreturned", *excluded)))
    add("trickster.epilogue.refused", "postwar_price", '''{n}Her reply arrived in her own sealed hand. She accepted the privacy terms and kept her demand for a public refusal.{/n}
"My seal, my chair, a private door. And once, in council, you will hear me reject the winter levy and move to the next business. Without a joke to make the lords laugh at the answer. I still oppose it, Commander."
"Agree to that, and I shall be in Drezen for the next session."''',
        c('[Agree to the privacy terms and the public refusal.]', "postwar_council"),
        c('[Leave the personal negotiation open.]', "postwar_open"))
    add("trickster.epilogue.refused", "postwar_council", '''{n}Several days later her carriage reached Drezen. At the council she rejected the winter levy on the reserve figures. The Commander took the refusal and moved on. Afterwards, in the attaché's office, she laid her fan across the closed ledger.{/n}
"That was the answer I wanted. I should like another supper now. Will you come?"''',
        c('[Accept her personal invitation.]', "postwar_visit"),
        c('[Keep the political agreement; leave the courtship open.]', "postwar_open"))
    add("trickster.epilogue.refused", "postwar_visit", '''{n}She chose the evening herself. They resumed their private letters, and visits followed when the road and their work allowed. Her official recommendations continued to arrive with her own seal and inconvenient conclusions. At each departure she named the next date she meant to return.{/n}''', c())
    add("trickster.epilogue.refused", "postwar_open", '''{n}She kept the privacy agreement and the council chair. The personal invitation remained unanswered. Her next dispatch ended, in her own hand, 'Still negotiating.'{/n}''', c())
    for nid in ("postwar_visit", "postwar_open"):
        node("trickster.epilogue.refused", nid)["Paragraphs"] = copy.deepcopy(node("trickster.epilogue.refused", "start").get("Paragraphs", []))

    text("ending_lost", "start", '''{n}Lady Konomi did not see the war's end. Her clerk sent her ledger and sealed private letters home to Nerosyan. Her titles were spelled correctly; he knew she would have checked.{/n}
{n}The Commander received the letters back unopened. One named an evening they would never have. It remained folded at that invitation, beside the fan she had left in Drezen.{/n}''')

    # No universal invoice for a dead lover; no 'unnamed for years' after collection.
    for item in payload["Scenes"]:
        if item.get("Relationship") != "konomi" or item.get("Owner") != "Epilogue":
            continue
        for paragraph_node in item["Nodes"]:
            for paragraph in paragraph_node.get("Paragraphs", []):
                if "unnamed favour for years" in paragraph["Text"]:
                    paragraph["Forbids"].append("konomi.lastcall.called")
            if any("unnamed favour for years" in x["Text"] for x in paragraph_node.get("Paragraphs", [])):
                paragraph_node["Paragraphs"].append(p('''{n}The Threshold summons brought her held favour due. The political terms of its collection went into Nerosyan's correspondence; her private letters remained under her own seal.{/n}''', requires=(K + "favour_owed", "konomi.lastcall.called")))

    # Humanized art direction, all heat/morning/council siblings; not racial anatomy.
    replacements = {
        "Her ears tip back and her tail uncurls behind her as she loosens": "She watches you as she loosens",
        ", tail curled round the leg of the chair": "",
        "Her ears tip back, a fraction, before she has them upright again.": "Her smile falters before she lets it widen.",
        "Her ears tip back, pleased, and this time she lets them.": "She smiles, pleased, and makes no effort to conceal it.",
        "Her tail sweeps the floor as she leans in to kiss you": "She leans in to kiss you",
        "Her ears come up, very slightly.": "She raises her chin, very slightly.",
        "She sweeps the ledger aside with her tail": "She pushes the ledger aside with her forearm",
    }
    for item in payload["Scenes"]:
        if item.get("Relationship") == "konomi":
            for part in item["Nodes"]:
                for old, new in replacements.items():
                    part["Text"] = part["Text"].replace(old, new)
                # History copies carry the same narrow inspection without reopening
                # the finished hearing or changing its result.
                if item["Id"] == "konomi.private_history" and part["Id"] in ("public", "missed_public"):
                    part["Text"] += '''
"The secretary received the published recommendation and its figures. He wanted my enclosures as well. I refused. My hostess repeated that distinction at dinner; he had to object to my advice where somebody could answer him."'''

    # Seven authored slot defaults. Old payoff effects stay on their original answers.
    def slot(sid, nid, default, continuation, split=None, slot_id=None):
        original = node(sid, nid)
        full_id = slot_id or "konomi." + sid + ".explicit.1"
        if split:
            before, after = original["Text"].split(split, 1)
            original["Text"] = before.strip()
            after_node = n(nid + "_after", original["Speaker"], split + after,
                *copy.deepcopy(original["Choices"]), portrait=original.get("Portrait", "Konomi"))
            # Keep receipts on the existing answer. The new aftermath exit is neutral.
            after_node["Choices"] = [c()]
            page(sid)["Nodes"].append(after_node)
            continuation = after_node["Id"]
        for answer in original["Choices"]:
            if not answer.get("Abort"):
                answer["Next"] = full_id
        page(sid)["Nodes"].append(n(full_id, "Narrator", default, c("Continue", continuation), portrait="Konomi"))

    # Brief: renewed or first invited intimacy; default cuts before explicit acts.
    slot("evening", "stay", "{n}She pulls you down onto the cushions, her loosened robe beneath your hands, and kisses you until the supper is forgotten.{/n}", None, split="{n}In the morning")
    # Brief: her separate personal invitation after two suppers, not bought access.
    cut = "{n}She pushes the account into the drawer and pulls you close across the cleared desk. The supper ends when she decides it does.{/n}"
    slot(rooms, "accept", cut, "morning")
    slot("trickster.never_arrived.second_supper", "accept", cut, "morning")
    # Brief: the closed political account; private desire, useful Crown dispatch after.
    slot("trickster.dismissed.private", "threshold", "{n}She draws you against the desk and kisses you hard. The fan stays on the closed ledger; neither of you reaches for it again tonight.{/n}", "morning")
    # Brief: both privacy and public dissent accepted; morning collects the latter.
    slot("trickster.dismissed.a_season", "yes", "{n}She catches your lower lip between her teeth, then pulls you back into the chair. The argument can wait until morning.{/n}", "a_season_morning")
    # Brief: chosen distance evening with travel and next visit still hers.
    slot("chosen_evening", "night", "{n}She pulls you onto the bed by your collar and sheds her robe, impatient with everything still between you.{/n}", "morning")
    # Brief: later night; political/work consequences survive in the original aftermath.
    slot("the_evening_she_kept", "night", "{n}She draws your hands to her bare sides and pulls you down with her. The waiting yard can wait.{/n}", None, split="{n}Afterward")
    after_night = node("the_evening_she_kept", "night_after")
    after_night["Text"] = after_night["Text"].replace("Nothing more needs arranging before morning.",
        "The watch bell sounds outside. She keeps your arm where she has put it and closes her eyes.")
    # Brief: farewell intimacy followed by real war fears and dawn departure.
    slot("private_last_visit", "night", "{n}She lets her robe fall beside the travelling case, pulls you onto the bed, and kisses you as though she resents every hour the war has taken.{/n}", None, split="{n}Much later")

    # SP2 morning: actual private dinner charge; existing receipt and exit untouched.
    after = node("evening", "stay_after")
    after["Text"] += '''
{n}The runner knocks with the council's supply dispatch and a supper receipt. She takes the dispatch, strikes 'council hospitality' from the receipt and writes her own supper account beneath it.{/n}
"The food was good. The bookkeeping was ambitious. This stays private."'''
    payload["Relationships"]["konomi"]["Guidance"] = (
        "Speak to Lady Konomi at the Diplomatic Council in Drezen. Keep the evenings you arrange. "
        "On Trickster, after dismissal, pay for the driver's offer and allow two days for her chosen road back; "
        "then hear her terms at the office. If she never came, send the council-chair invitation through the chancery "
        "report and allow four days for her arrival; a failed office meeting has a later letter substitute. "
        "An accredited first supper earns another invitation, with her personal answer two evenings later. "
        "If recalled by her people's rite, meet her for the prepaid consultation after twelve hours. "
        "Old private letters and map replies continue only where already arranged."
    )
