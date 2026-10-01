"""Earned future conversations and explicit catch-up for existing Seelah saves."""
from story_format import c, n, scene


def reckoning(prefix, destination):
    """Read the current native outcome at this conversation, without saving a readiness alias."""
    return [
        n(prefix + "_quest", "Seelah", '''"Before you clear a shelf for my things, remember I've still got work to do for my friends. My sword won't be hanging over the hearth just to look pretty."
{n}She sits forward, resting her hands on her knees.{/n}
"You should hear the trouble before you find my boots under your table."''',
          c('"Tell me where things stand now."', prefix + "_unfinished", forbids=("seelah.souls_returned",)),
          c('"Tell me where things stand now."', prefix + "_bad", requires=("seelah.souls_returned", "seelah.ending_bad")),
          c('"Tell me where things stand now."', prefix + "_moderate", requires=("seelah.souls_returned", "seelah.ending_moderate"), forbids=("seelah.ending_bad",)),
          c('"Tell me where things stand now."', prefix + "_returned", requires=("seelah.souls_returned",), forbids=("seelah.ending_bad", "seelah.ending_moderate"))),
        n(prefix + "_unfinished", "Seelah", '''"There are people I still haven't helped. I don't know how many I can bring home. But when the fighting ends, I'm going to keep looking."
{n}She looks at you steadily.{/n}
"I want to live with you. But if someone's still missing, I'll pull on my boots and go after them. I'll tell you where I'm going. And I'll come back."
{n}Her mouth twists.{/n}
"Hah. That sounded better before I said it. I'm asking you to keep a place for me, not handing you a list of reasons to run."''', c('"Tell me who still needs finding."', destination)),
        n(prefix + "_bad", "Seelah", '''"We brought the souls back. Thank the gods for that. But everything else didn't mend itself. Tell me I ought to be satisfied, and some days I'll shout your ears off."
{n}She presses her palms together, then lets them fall apart.{/n}
"When I can, I may take to the road alone. For how long? I don't know. But I won't keep snapping 'none of your business' until you stop asking. You'll hear from me, even if the news is rotten."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_moderate", "Seelah", '''"I thought I knew what I was doing. Now? I've got questions. We brought people back, but I still lie awake wondering where I went wrong."
{n}She gives a small, rueful smile.{/n}
"Someone must have wrestled with this before me. I may go looking for them. I'll write to you, even if the whole letter says my boots are soaked and I'm still an idiot."
"You may complain about the rain. I intend to."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_returned", "Seelah", '''"We brought them back! I'd like us all around a table again, making enough noise to wake the neighbors. Whether they'll come is another question."
{n}She catches herself smiling at the thought.{/n}
"I'll ask anyway. If I start counting chairs before anyone answers, kick me under the table."
"And I've got plenty of plans for you and me. Go on, tell me yours before I spend all our coin on mine."''', c('"And Elan?"', prefix + "_elan")),
        n(prefix + "_elan", "Seelah", '''{n}Seelah takes a moment before answering.{/n}''',
          c('[Listen.]', prefix + "_elan_dead", requires=("seelah.elan_dead",)),
          c('[Listen.]', prefix + "_elan_other", forbids=("seelah.elan_dead",))),
        n(prefix + "_elan_dead", "Seelah", '''"I miss him. Sometimes I remember something he said and begin an argument he isn't here to finish."
{n}Her voice catches, and she waits until she can trust it.{/n}
"I miss him. You can't mend that. But I want to tell you about him, then stay here with you over supper. I've laughed at his jokes and cried over them in the same evening before."''', c('"You can tell me."', destination)),
        n(prefix + "_elan_other", "Seelah", '''"You'll have to ask him. I'd dearly like to hear his answer, but I can't drag it out of him."
{n}She rubs a thumb along the edge of her chair.{/n}
"If we talk again, he'll have plenty to say, I'm sure. No use settling it here with his chair empty."''', c('"All right. What do you want?"', destination)),
    ]


def future_gate_nodes(destination="start", migration=False):
    """Gate developed plans through played history; every postponement remains replayable."""
    title = "I remember our promise. Now I'd like a few days with you before we start packing our things together." if migration else "I'd like that. But let's spend a few days together before we start arguing over where the hearth goes."
    activity_choices = [c('"We have had those days together. What comes next?"', "future_quest", requires=("seelah.late_race_kept",)),
                        c('"What shall we do first?"', "future_visits", forbids=("seelah.late_race_kept",))]
    if not migration:
        activity_choices.append(c('"I want to see you again. But I cannot promise whole days together before the war ends."', "short_quest", forbids=("seelah.late_race_kept",)))
    nodes = [
        n("future_entry", "Seelah", title, c('"Tell me."', "future_abyss"), c('"Tell me another evening."', abort=True)),
        n("future_abyss", "Seelah", '''"First, have we left anything hanging? Drawing a hearth on a scrap of paper won't make it go away."''',
          c('"Nothing hanging. What shall we do together?"', "future_activity", forbids=("seelah.letter_unsettled",)),
          c('"We talked, and we went back to the copyist. I have not forgotten."', "future_activity", requires=("seelah.letter_unsettled", "seelah.copyist_followed")),
          c('"We talked about the copyist here in Drezen. I remember."', "future_activity", requires=("seelah.letter_unsettled", "seelah.letter_return_addressed"), forbids=("seelah.copyist_followed",)),
          c('"The copyist. We still need to speak about her."', "future_copyist", requires=("seelah.letter_unsettled",), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed"))),
        n("future_copyist", "Seelah", '''"Yes. The copyist first. We left that in a fine mess."
{n}Seelah stays beside you, her smile gone.{/n}
"Come and sit with me when you aren't rushing off. I've got something to show you."''', c('[Return to the conversation about the copyist before making future plans.]', abort=True)),
        n("future_activity", "Seelah", '''"I want an afternoon to beat you at something and crow about it. You might regret encouraging me."
{n}She smiles.{/n}
"And when we try to help someone and make a mess of it, I want you there for the cleaning up. We won't win every afternoon."''', *activity_choices),
        n("future_visits", "Seelah", '''"Let's start with an outing. The grand speeches can wait."''',
          c('"Then let us begin with the washing-yard invitation."', "future_saw", forbids=("seelah.saw_arranged",)),
          c('"We should see how the repair turned out."', "future_platform", requires=("seelah.saw_arranged",), forbids=("seelah.platform_kept",)),
          c('"You asked me to find you after the repair."', "future_faith", requires=("seelah.platform_kept",), forbids=("seelah.faith_spoken",)),
          c('"You promised me an evening with a view."', "future_roof", requires=("seelah.faith_spoken",), forbids=("seelah.aftermath_ready",)),
          c('"Let us make time for the course and the race."', "future_race", requires=("seelah.aftermath_ready",))),
        n("future_saw", "Seelah", '''"The washing yard, then. Mera and Orsa won't be short of things to tell us. Come and get me when you can go."''', c('[Keep the future conversation open and ask about the washing yard.]', abort=True)),
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
            n("short_choice", "Seelah", '''"Then come and see me. I want you here. A whole life together? I won't swear to that yet."
{n}She rests her hand on the table, close to yours.{/n}
"Maybe we'll be arguing over a hearth one day. Maybe we won't get that far. For now, I'd like another evening with you."''',
              c('"I will come back for another evening. That much I can promise."', "short_end"),
              c('"I cannot promise to keep coming back."', "no")),
            n("short_end", "Seelah", '''"All right. An evening at a time."
{n}She smiles at you across the table.{/n}
"Come and see me when there isn't an emergency. I would like to discover what you complain about on an ordinary day."''',
              c('[Agree to keep seeing each other, one evening at a time.]', flags=("seelah.committed", "seelah.chosen_future", "seelah.short_future_chosen"))),
        ])
    return nodes


def farewell_gate_nodes():
    return [
        n("farewell_entry", "Seelah", '''"Before we say our last goodbyes to Drezen, are there invitations we still mean to keep? I don't want us to remember them only when the gates are behind us."''',
          c('[Review the time still available together.]', "farewell_pending"),
          c('[Keep the farewell now, leaving any remaining Drezen meetings unfinished.]', "start")),
        n("farewell_pending", "Seelah", '''{n}Seelah sits down beside you and counts your unfinished outings on her fingers.{/n}''',
          c('"We still owe each other a talk about the copyist. Before we leave."', "farewell_copyist", requires=("seelah.letter_unsettled",), forbids=("seelah.copyist_followed", "seelah.letter_return_addressed")),
          c('"We still have outings to catch up on before the race. I want to go with you."', "farewell_activity", forbids=("seelah.late_race_kept",)),
          c('"You asked me for an evening after the race. I want to keep it."', "farewell_evening", requires=("seelah.late_race_kept",), forbids=("seelah.late_evening_kept",)),
          c('"We planned something after that evening. Let us try it before we leave."', "farewell_step", requires=("seelah.late_evening_kept",), forbids=("seelah.late_campaign_kept",)),
          c('[Keep the farewell now, leaving any remaining Drezen meetings unfinished.]', "start")),
        n("farewell_copyist", "Seelah", '"Yes. Ask me about her while we still have a quiet place to sit."', c('[Postpone the farewell and return to the copyist conversation.]', abort=True)),
        n("farewell_activity", "Seelah", '"So do I. Come and find me between the things we cannot put off. We can make a few days out of it."', c('[Postpone the farewell and continue the earlier invitations.]', abort=True)),
        n("farewell_evening", "Seelah", '"Good. I was hoping you had not forgotten. Give me time to find a room and I will be very pleased to see you."', c('[Postpone the farewell and keep the after-race evening.]', abort=True)),
        n("farewell_step", "Seelah", '"Then let\'s go! We\'ve spent enough time talking about it to have gone twice already."', c('[Postpone the farewell and keep the next outing.]', abort=True)),
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


s("future_followup", "The days inside the promise", '"We promised each other a life together. How shall we spend it?"', [
    *future_gate_nodes("kept_promise", migration=True),
    n("kept_promise", "Seelah", '''"I remember our promise. You don't have to swear it all over again."
{n}She reaches across the table, her fingers brushing yours.{/n}
"We've had a few days to try it. I want more. Even after all that trouble I've just told you about."''',
      c('"I still want a life with you. Unfinished work, muddy boots and all."', "renewed"),
      c('"Let me sleep on it. My promise still stands."', abort=True)),
    n("renewed", "Seelah", '''"Good! I'll keep making plans. Shout if you see a hole in one before I fall through it."
{n}She laughs softly.{/n}
"Not all of them. I am bound to get one right without assistance eventually."''',
      c('[Keep your promise of a life together.]', flags=("seelah.developed_commitment",))),
], requires=("seelah.road", "seelah.committed"), forbids=("seelah.developed_commitment", "seelah.farewell"))

s("farewell_catchup", "Time before the gates", '"We said goodbye, but the gates are still ahead of us. Shall we take that outing we missed?"', [
    n("start", "Seelah", '''"Yes! I was starting to think saying goodbye meant we had to sit around looking solemn until someone saddled the horses."
{n}She looks toward the street, then back at you.{/n}
"I meant every word. But we're still here, and there's an outing we haven't taken. Let's go while we can."''',
      c('"Then let us take those outings we missed."', "yes"),
      c('"Not now. I am glad I asked."', abort=True)),
    n("yes", "Seelah", '''"Come and get me when you can stay a while. We'll see which outing we can squeeze in before we leave."
{n}She gives you a pleased, almost conspiratorial smile.{/n}
"No need to polish the farewell. I thought the first one was rather good."''',
      c('[Keep your farewell, and take another outing together before leaving Drezen.]', flags=("seelah.catchup_requested",))),
], requires=("seelah.farewell", "seelah.committed"), forbids=("seelah.catchup_requested",))
