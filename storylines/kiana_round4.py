"""Authored D29/D30 staging: letters and Elan's delivery take elapsed time.

No new partner policy. Keep the old graphs and answer positions; only split
their existing correspondence at the dispatch and delivery boundaries.
"""
import copy

from story_format import c, n
from storylines import kiana_partner as kp

SHARE_SENT = "kiana.partner_late.share_sent"
BREAKUP_SENT = "kiana.partner_late.breakup_sent"
DELIVERY_WAIT = "kiana.partner_late.delivery_wait"
PENDING = (SHARE_SENT, BREAKUP_SENT)
EARLY_SHARE_SENT = "kiana.partner_early.share_sent"
EARLY_BREAKUP_SENT = "kiana.partner_early.breakup_sent"
EARLY_DELIVERY_WAIT = "kiana.partner_early.delivery_wait"
HOSTS = ("kiana.trickster.late_question", "kiana.trickster.late_question_letter")
ALL_HOSTS = (*HOSTS, "kiana.morning")


def reserve_scenes(scenes):
    """Register IDs before the final outcome pass freezes its scene index.

    The partner appender supplies their graphs later. These are authored new
    scenes, never player-facing placeholders in the completed export.
    """
    books = {s["Id"]: s for s in scenes}
    from storylines import kiana
    books.update({s["Id"]: s for s in kiana.SCENES})
    for sid in ALL_HOSTS:
        for suffix in (".elan_reply", ".elan_parting", ".after_delivery"):
            result = copy.deepcopy(books[sid])
            result["Id"] = sid + suffix
            result["Nodes"] = [n("start", "Kiana", "", c())]
            scenes.append(result)


def integrate(payload):
    books = {s["Id"]: s for s in payload["Scenes"]}
    for sid in ALL_HOSTS:
        if sid not in books:
            continue
        host = books[sid]
        nodes = {n["Id"]: n for n in host["Nodes"]}
        early = sid == "kiana.morning"
        if not early and "promise_accepted" not in nodes:
            continue
        share_sent, breakup_sent, delivery_wait = ((EARLY_SHARE_SENT, EARLY_BREAKUP_SENT, EARLY_DELIVERY_WAIT)
                                                   if early else (SHARE_SENT, BREAKUP_SENT, DELIVERY_WAIT))
        postal = bool(host.get("Remote"))

        def followup(suffix, title, clock, names, delay):
            # Retain the host's path, chapter, presence, closure and outcome
            # guards. The postal host still requires failed physical placement.
            result = copy.deepcopy(host)
            result.update(Id=sid + suffix, Title=title, Entry=title,
                          Nodes=[copy.deepcopy(nodes[name]) for name in names if name in nodes],
                          DelayHours=delay)
            result["Requires"].append(clock)
            presence = "kiana.reachable_by_letter" if result.get("Remote") else "kiana.present_now"
            if presence not in result["Requires"]:
                result["Requires"].append(presence)
            # The source living-partner choices already exclude witnessed
            # death. Carry that guard across the newly separated interactions.
            result["Forbids"].append(kp.DEAD)
            if early:
                result["Forbids"].extend(("kiana.closed", "kiana.committed"))
            if result.get("Remote"):
                result["Kind"] = "letter"
            target = books.get(result["Id"])
            if target is None:
                payload["Scenes"].append(result)
                return result
            target.clear()
            target.update(result)
            return target

        shared = followup(".elan_reply", "Elan's answer", share_sent,
                          ("partner_elan_terms", "partner_share_yes", "partner_stop", "promise_accepted"), 48)
        shared["Nodes"][0]["Text"] = (
            "{n}A later courier brings Kiana's packet. Elan's reply is on top, its ink pressed through the paper.{/n}\n"
            if postal else
            "{n}When you return to the ward, Kiana has Elan's answer beside the unsigned page. His ink has pressed through the paper.{/n}\n"
        ) + nodes["partner_elan_terms"]["Text"].split("\n", 1)[1]

        # His reply arrives first. The player then leaves the requested meeting
        # to them; the final invitation cannot arrive in the same interaction.
        breakup = followup(".elan_parting", "Elan's last letter", breakup_sent,
                           ("partner_breakup", "partner_elan_breakup", "partner_exclusive_yes", "promise_accepted"), 48)
        breakup["Remote"] = True
        breakup["Kind"] = "letter"
        breakup["Requires"] = [key for key in breakup["Requires"] if key != "kiana.present_now"]
        if "kiana.reachable_by_letter" not in breakup["Requires"]:
            breakup["Requires"].append("kiana.reachable_by_letter")
        for key in ("ContactUnit", "InteractionHub"):
            breakup.pop(key, None)
        breakup["Nodes"][0]["Text"] = nodes["partner_breakup"]["Text"]
        last = breakup["Nodes"][1]
        for old in last["Choices"]:
            old["Requires"].append("trickster.now")
            old["Forbids"].append("trickster.now")
        last["Choices"].append(c('[Leave their meeting to them. Wait for her next invitation.]',
                                   flags=(delivery_wait,)))

        followup(".after_delivery", "The case at her door", delivery_wait,
                 ("partner_exclusive_yes", "promise_accepted"), 24)

        # Shipped late-yes pages had a generated [Leave.] at index 2. The
        # staging split no longer triggers its generator; retain the saved
        # position explicitly, retired without changing the promise edges.
        for name in ("partner_share_yes", "partner_exclusive_yes"):
            nodes[name]["Choices"].append(c("[Leave.]", requires=("trickster.now",),
                                             forbids=("trickster.now",), abort=True))

        # Neither dispatch grants a stance, separation, late yes or commitment.
        # Existing nodes and old targets remain present for saved references.
        for name, flag, label in (
            ("partner_share", share_sent, '[Let her send the letter. Wait for Elan\'s answer.]'),
            ("partner_breakup", breakup_sent, '[Let her write to Elan. Wait for his reply.]'),
        ):
            node = nodes[name]
            for old in node["Choices"]:
                old["Requires"].append("trickster.now")
                old["Forbids"].append("trickster.now")
            node["Choices"].append(c(label, flags=(flag,)))

        nodes["partner_share"]["Text"] = (
            '"Then he gets a letter without a princess in it. Desna help me, that will be the difficult part."\n'
            + ('{n}Kiana encloses a copy of what she is sending Elan: what she wants, what she has done, and the promise still awaiting your signature. One excuse is crossed out. Your page comes back unsigned.{/n}'
               if postal else
               '{n}Kiana writes beside you. She tells Elan what she wants, what she has done and the promise you have not yet made. She crosses out an excuse, folds the letter and seals it. The page of the play stays unsigned.{/n}')
        )
        nodes["partner_breakup"]["Text"] = (
            ('{n}Kiana sends a copy of the letter she is dispatching to Elan. Your promise is still unsigned.{/n}\n'
             if postal else
             '{n}Kiana draws a fresh sheet toward her and writes to Elan. She crosses out the first sentence and starts again. Your promise is still unsigned.{/n}\n')
            + '"Elan, I am not coming home as your wife. Or waiting to become one."\n'
              '{n}Below it, she writes:{/n}\n'
              '"I wanted to make you laugh before telling you. What a rotten little coward I can be. I want the Commander. I am ending this."'
        )
        if not postal:
            nodes["partner_answer"]["Text"] = (
                '{n}Kiana looks at the script, then at the case by her chair.{/n}\n'
                '"My answer? You. But Elan gets his letter before you get this page."'
            )
        else:
            nodes["partner_answer"]["Text"] = (
                '"My answer? You. But Elan gets his letter before you get this page."\n'
                '{n}The promise comes back unsigned.{/n}'
            )
        # A dispatched decision cannot be restarted through the twin host.
        host["Forbids"].extend((share_sent, breakup_sent))
        if early:
            def pending(nid, brief):
                return '[PROSE PENDING: ' + sid + '/' + nid + ' - ' + brief + ']'
            shared['Nodes'][0]['Text'] = pending('partner_elan_terms',
                'Stage the delayed Elan reply at a later visit; retain his existing terms and motives')
            for nid, brief in (
                ('partner_share', 'Send the request now; Elan has not answered; commitment waits for the delayed reply'),
                ('partner_breakup', 'Announce her earned decision and send the breakup letter now; no reply or physical delivery yet'),
                ('partner_answer', 'Preserve Kiana choosing only on the existing earned histories; the letter and later delivery are still pending'),
            ):
                nodes[nid]['Text'] = pending(nid, brief)
            # New exits are held text; their existing Set/Next/Abort fields carry the staging.
            for record in (nodes['partner_share'], nodes['partner_breakup'], breakup['Nodes'][1]):
                record['Choices'][-1]['Text'] = pending(record['Id'], 'End this interaction and wait for the correspondence or delivery already requested')
            # Morning never shipped the late-host generated exit at index 2.
            for nid in ('partner_share_yes', 'partner_exclusive_yes'):
                nodes[nid]['Choices'].pop()
