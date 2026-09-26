"""Earned future conversations and explicit catch-up for existing Seelah saves."""
from story_format import c, n, scene


def reckoning(prefix, destination):
    """Read the current native outcome at this conversation, without saving a readiness alias."""
    return [
        n(prefix + "_quest", "Seelah", '''"Before we start deciding where to put my things, there's something I want to be clear about. My work with my friends is part of what I would be bringing with me."
{n}She sits forward, resting her hands on her knees.{/n}
"I don't want to give you the easy version and leave you to discover the rest."''',
          c('"Tell me where things stand now."', prefix + "_unfinished", forbids=("seelah.souls_returned",)),
          c('"Tell me where things stand now."', prefix + "_bad", requires=("seelah.souls_returned", "seelah.ending_bad")),
          c('"Tell me where things stand now."', prefix + "_moderate", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
          c('"Tell me where things stand now."', prefix + "_returned", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate"))),
        n(prefix + "_unfinished", "Seelah", '''"There are people I still haven't helped. I don't know yet how much I can put right. When the fighting ends, I won't suddenly stop wanting to find out."
{n}She looks at you steadily.{/n}
"I want a life with you. I may also need to leave a comfortable room because somebody is still missing from theirs. If I say I'll come back, I want you to know why I went."
{n}Her mouth twists.{/n}
"That sounded less like a warning in my head. I'm trying to tell you what you can expect, not frighten you into choosing someone with fewer problems."''', c('"We can speak honestly about what is still unfinished."', destination)),
        n(prefix + "_bad", "Seelah", '''"We brought back souls. That matters. It didn't undo everything that happened, and there are days when being told it ought to be enough makes me want to shout."
{n}She presses her palms together, then lets them fall apart.{/n}
"I may need to travel on my own when I can. I don't know how long. I can promise to tell you what I know instead of calling every difficult day a private matter until you give up asking."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_moderate", "Seelah", '''"I still have questions about what I did, and what I thought I knew. Bringing people back didn't answer all of them."
{n}She gives a small, rueful smile.{/n}
"I'd like to hear how other people live with that. I may go looking for them. I want to write to you while I'm away, even when all I have to report is that the road is wet and I haven't become wiser."
"You may complain about the rain. I intend to."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_returned", "Seelah", '''"I'm glad we brought them back. I want to keep finding reasons to be glad. But I don't get to arrange what everybody does next just because I want us all together again."
{n}She catches herself smiling at the thought.{/n}
"I will probably suggest it anyway. You can remind me that an invitation is supposed to wait for an answer."
"With you, too. I have a great many plans. I want to hear yours before I start calling them ours."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_elan", "Seelah", '''{n}Seelah takes a moment before answering.{/n}''',
          c('[Listen.]', prefix + "_elan_dead", requires=("seelah.elan_dead",)),
          c('[Listen.]', prefix + "_elan_other", forbids=("seelah.elan_dead",))),
        n(prefix + "_elan_dead", "Seelah", '''"I miss him. Sometimes I remember something he said and begin an argument he isn't here to finish."
{n}Her voice catches, and she waits until she can trust it.{/n}
"I don't want you to fill that space. I want to be able to tell you when I miss him, and still have a good evening with you afterward. Sometimes both happen."''', c('"You can tell me."', destination)),
        n(prefix + "_elan_other", "Seelah", '''"I can't promise you what he'll choose. I have enough trouble speaking for myself when I want an answer badly."
{n}She rubs a thumb along the edge of her chair.{/n}
"If there is another conversation to have with him, it will have to be his as well as mine. I won't plan it here and pretend he's already agreed."''', c('"Then let us speak for ourselves."', destination)),
    ]


def future_gate_nodes(destination="start", migration=False):
    """Gate developed plans through played history; every postponement remains replayable."""
    title = "We have made a promise already. I still want to give it some actual days together." if migration else "I'd like to talk about that. I also want us to have something to make plans from besides how much we like the idea."
    activity_choices = [c('"We have shared those days. Let us talk about what comes next."', "future_quest", requires=("seelah.late_race_kept",)),
                        c('"What would you like us to make time for first?"', "future_visits", forbids=("seelah.late_race_kept",))]
    if not migration:
        activity_choices.append(c('"I want to keep seeing you, but I cannot promise those days before the war ends."', "short_quest", forbids=("seelah.late_race_kept",)))
    nodes = [
        n("future_entry", "Seelah", title, c('"Tell me."', "future_abyss"), c('"Let us find a better time for this conversation."', abort=True)),
        n("future_abyss", "Seelah", '''"First, is there something we've been leaving unsaid? I don't want to step over it because planning a house sounds nicer."''',
          c('"Let us talk about the days we can share."', "future_activity", forbids=("seelah.letter_unsettled",)),
          c('"We talked, and we went back to the copyist. I have not forgotten."', "future_activity", requires=("seelah.letter_unsettled", "seelah.copyist_followed")),
          c('"We addressed the copyist after we came back. I remember what we said."', "future_activity", requires=("seelah.letter_unsettled", "seelah.letter_return_addressed"), forbids=("seelah.copyist_followed",)),
          c('"The copyist. We still need to speak about her."', "future_copyist", requires=("seelah.letter_unsettled",), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed"))),
        n("future_copyist", "Seelah", '''"Yes. I want to finish that conversation before we make another promise."
{n}She stays beside you, but leaves the imagined house for another evening.{/n}
"Ask me about her when you can stay. I have something here that I need to show you."''', c('[Return to the conversation about the copyist before making future plans.]', abort=True)),
        n("future_activity", "Seelah", '''"I wanted us to have an afternoon where I could be ridiculous about winning, and you could discover whether that was a terrible mistake."
{n}She smiles.{/n}
"And a few days when helping someone didn't turn out quite as neatly as we hoped. I want to know what we do with those days too."''', *activity_choices),
        n("future_visits", "Seelah", '''"Something we can actually do. We can return to the grand promises afterward."''',
          c('"Then let us begin with the washing-yard invitation."', "future_saw", forbids=("seelah.saw_arranged",)),
          c('"We should see how the repair turned out."', "future_platform", requires=("seelah.saw_arranged",), forbids=("seelah.platform_kept",)),
          c('"You asked me to find you after the repair."', "future_faith", requires=("seelah.platform_kept",), forbids=("seelah.faith_spoken",)),
          c('"You promised me an evening with a view."', "future_roof", requires=("seelah.faith_spoken",), forbids=("seelah.aftermath_ready",)),
          c('"Let us make time for the course and the race."', "future_race", requires=("seelah.aftermath_ready",))),
        n("future_saw", "Seelah", '''"The washing yard, then. Mera and Orsa will have plenty to say without us imagining it in advance. Ask me when you have time to go."''', c('[Keep the future conversation open and ask about the washing yard.]', abort=True)),
        n("future_platform", "Seelah", '''"Yes. We arranged a repair. I want to see what came of it before I begin congratulating anyone."''', c('[Keep the future conversation open and ask how the repair went.]', abort=True)),
        n("future_faith", "Seelah", '''"I did. I meant it. Come and find me when we can finish a conversation without either of us rushing away."''', c('[Keep the future conversation open and keep that meeting.]', abort=True)),
        n("future_roof", "Seelah", '''"Food, sky, and no grand plan. I can manage that. Give me the time to arrange it."''', c('[Keep the future conversation open and arrange the roof evening.]', abort=True)),
        n("future_race", "Seelah", '''"I intend to enjoy that afternoon whether I win or not. You may have to remind me of that immediately after the race."
{n}She laughs.{/n}
"We have the course, the lesson, and my little page of plans to work through. Find me between meetings; I will tell you what comes next."''', c('[Keep the future conversation open and continue the activity meetings.]', abort=True)),
    ]
    nodes.extend(reckoning("future", destination))
    if not migration:
        for page in nodes:
            for answer in page["Choices"]:
                if answer["Next"] == destination:
                    answer["Set"].append("seelah.future_reviewed")
    if not migration:
        nodes.extend(reckoning("short", "short_choice"))
        nodes.extend([
            n("short_choice", "Seelah", '''"Then let us promise what we can mean now. I want to keep seeing you. I won't pretend we have already learned how to build a whole life together."
{n}She rests her hand on the table, close to yours.{/n}
"There can be more later. Or there may be less than we hope. I'd rather begin honestly."''',
              c('"I want to keep choosing our evenings. That is the promise I can make now."', "short_end"),
              c('"I cannot offer even that honestly."', "no")),
            n("short_end", "Seelah", '''"All right. An evening at a time."
{n}Her smile is warm, though she leaves the grander plans unspoken.{/n}
"Come and see me when there isn't an emergency. I would like to discover what you complain about on an ordinary day."''',
              c('[Agree to keep seeing each other, one evening at a time.]', flags=("seelah.committed", "seelah.chosen_future", "seelah.short_future_chosen"))),
        ])
    return nodes


def farewell_gate_nodes():
    return [
        n("farewell_entry", "Seelah", '''"Before we say our last goodbyes to Drezen, are there invitations we still mean to keep? I don't want us to remember them only when the gates are behind us."''',
          c('[Review the time still available together.]', "farewell_pending"),
          c('[Keep the farewell now, leaving any remaining Drezen meetings unfinished.]', "start")),
        n("farewell_pending", "Seelah", '''{n}Seelah waits while you consider what the two of you have actually done, and what you have only promised.{/n}''',
          c('"We still need to address the copyist. Let us do that before leaving."', "farewell_copyist", requires=("seelah.letter_unsettled",), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed")),
          c('"I want time for the invitations we have not kept, before the race is behind us too."', "farewell_activity", forbids=("seelah.late_race_kept",)),
          c('"You asked me for an evening after the race. I want to keep it."', "farewell_evening", requires=("seelah.late_race_kept",), forbids=("seelah.late_evening_kept",)),
          c('"We planned something after that evening. Let us try it before we leave."', "farewell_step", requires=("seelah.late_evening_kept",), forbids=("seelah.late_campaign_kept",)),
          c('[Keep the farewell now, leaving any remaining Drezen meetings unfinished.]', "start")),
        n("farewell_copyist", "Seelah", '"Yes. Ask me about her while we still have a quiet place to sit."', c('[Postpone the farewell and return to the copyist conversation.]', abort=True)),
        n("farewell_activity", "Seelah", '"So do I. Come and find me between the things we cannot put off. We can make a few days out of it."', c('[Postpone the farewell and continue the earlier invitations.]', abort=True)),
        n("farewell_evening", "Seelah", '"Good. I was hoping you had not forgotten. Give me time to find a room and I will be very pleased to see you."', c('[Postpone the farewell and keep the after-race evening.]', abort=True)),
        n("farewell_step", "Seelah", '"Then let us keep it. We have time for something we wanted, if we stop spending it saying we ought to."', c('[Postpone the farewell and keep the next outing.]', abort=True)),
    ]


SCENES = []


def s(id, title, entry, nodes, requires, forbids=()):
    for page in nodes:
        page["Portrait"] = "Seelah"
    SCENES.append(scene("seelah." + id, title, "Seelah", 5, entry, nodes,
                        Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
                        Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[5],
                        requires=requires, forbids=("seelah.closed", "seelah_dead", "seelah_gone", "inhuman", *forbids),
                        ForbidOverrides={"seelah.farewell": "seelah.catchup_requested"} if "seelah.farewell" in forbids else {},
                        delay=0, optional=True))


s("future_followup", "The days inside the promise", '"We made a promise. I want to talk about the days inside it."', [
    *future_gate_nodes("kept_promise", migration=True),
    n("kept_promise", "Seelah", '''"I haven't forgotten what we promised. I don't need you to say the old words again as though they only begin counting now."
{n}She reaches for your hand, then leaves the invitation between you.{/n}
"We've had some of those days together. I know more about what I want with you. I wanted you to hear it with the difficult parts included."''',
      c('"I still want that life with you. With room for what you have told me."', "renewed"),
      c('"I need time to think. I am not taking back our promise tonight."', abort=True)),
    n("renewed", "Seelah", '''"Good. Then I will keep making plans, and you can keep telling me which ones need work."
{n}She laughs softly.{/n}
"Not all of them. I am bound to get one right without assistance eventually."''',
      c('[Keep making room for the life you have promised each other.]', flags=("seelah.developed_commitment",))),
], requires=("seelah.road", "seelah.committed"), forbids=("seelah.developed_commitment", "seelah.farewell"))

s("farewell_catchup", "Time before the gates", '"We said our goodbyes, but we are still here. Can we keep another invitation?"', [
    n("start", "Seelah", '''"We can. I was beginning to think we had made a rule against enjoying the time before we actually left."
{n}She looks toward the street, then back at you.{/n}
"We have already said what we meant. I won't ask you to forget it. If we still have time for something we missed, I'd like to use it."''',
      c('"Then let us return to the invitations we left unfinished."', "yes"),
      c('"Not now. I am glad I asked."', abort=True)),
    n("yes", "Seelah", '''"Find me when you can stay. We'll take up the next thing we can actually do here."
{n}She gives you a pleased, almost conspiratorial smile.{/n}
"No need to polish the farewell. I thought the first one was rather good."''',
      c('[Make time for the remaining Drezen meetings without erasing the farewell.]', flags=("seelah.catchup_requested",))),
], requires=("seelah.farewell", "seelah.committed"), forbids=("seelah.catchup_requested",))
