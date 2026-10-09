"""Konomi's romance: personal choices that do not purchase political agreement.

Dialogue root: World/Crusade/RankUps/Diplomacy/Diplomacy_Officer/AnswersList_0003.
Incomplete assembled route; native-outcome coverage, art and runtime verification remain pending.
"""
from story_format import c, n, scene

RELATIONSHIP = dict(
    Title="Letters without a seal",
    Description="Lady Konomi has corrected a report about me. She has also made a point of telling me which criticisms she left intact. Our private correspondence is becoming less easily filed.",
    Objective="Make time for Lady Konomi",
    Guidance="Speak to Konomi in Drezen between meetings while she holds her post. If she is dismissed, a Trickster may find another way to send a personal invitation. After she answers, allow time for letters and private visits, and look for them after resting in Drezen. Her political convictions continue even when the conversation becomes personal.",
    StartedFlag="konomi.started", ClosedFlag="konomi.closed", CommittedFlag="konomi.committed",
    UnavailableFlags=[], FailureFlags=[],
)

DREZEN = "2570015799edf594daf2f076f2f975d8"
SCENES = []


def s(id, title, chapter, entry, nodes, **conditions):
    conditions["requires"] = ("konomi.present", *conditions.get("requires", ()))
    for page in nodes:
        if not page["Portrait"]:
            page["Portrait"] = "Konomi"
    SCENES.append(scene("konomi." + id, title, "Konomi", chapter, entry, nodes,
                        Relationship="konomi", AnswerLists=["0dc8b8604bb33c846a63f3eb62443674"],
                        Areas=[DREZEN], Chapters=[c for c in (3, 5) if c >= chapter], **conditions))


s("margin", "An alteration in the margin", 3, '"You wanted to discuss something outside the council?"', [
    n("start", "Konomi", '''{n}Konomi turns a sheet of paper toward you. One sentence has been struck out so thoroughly that its author would have difficulty defending it.{/n}
"A description of your conduct. The original relied upon a comparison with livestock. I removed it."
{n}She waits while you read what remains.{/n}
"Before you thank me, the paragraph about your judgment is mine."''',
      c('"You defended me while criticizing me. That must have taken some care."', "care", flags=("konomi.candid",)),
      c('"An inaccurate insult makes the accurate ones easier to dismiss."', "accuracy", flags=("konomi.precise",)),
      c('"I would prefer to keep our conversations strictly official."', "official")),
    n("care", "Konomi", '''"It took an inkpot and a little restraint. One was easier to find than the other."
{n}She returns the report to a neat stack, but leaves the chair opposite hers unobstructed.{/n}
"You have made yourself difficult to describe to people who have never met you. They either hear that you will save Mendev or that you will ruin it. Neither opinion prepares them for a conversation."
{n}For the first time, she sounds more interested than irritated by the problem.{/n}
"I thought I might improve my own information."''',
      c('"Then ask me something the council does not need to know."', "question"),
      c('"You could begin by spending an evening with me."', "invitation")),
    n("accuracy", "Konomi", '''{n}Her expression brightens by a small, unmistakable degree.{/n}
"Exactly. I object to being forced to defend you against an argument so poor that it makes my own concerns look foolish."
{n}She gestures toward the chair.{/n}
"And I would prefer to understand what you consider worth defending. We spend a great deal of time discussing what you oppose."''',
      c('"There are things I would rather show you than put in a report."', "invitation"),
      c('"You may ask. I reserve the right to ask something in return."', "question")),
    n("question", "Konomi", '''"What do you want that nobody in this fortress thinks to sell you?"
{n}She asks without consulting her papers. When you hesitate, she taps the fan against her palm, the way a broker counts down an offer.{/n}''',
      c('"Being contradicted by someone who still wants my company afterward."', "answer", flags=("konomi.wants_honesty",)),
      c('"A few hours in which I do not have to be impressive."', "answer", flags=("konomi.wants_rest",))),
    n("answer", "Konomi", '''{n}Konomi looks toward the closed door. A runner passes outside, footsteps quick on the stone.{/n}
"I will not pretend to be harmless company, Commander. I will offer you a concession instead: what you say to me tonight does not travel to Nerosyan. Consider it an opening position."
{n}She takes a blank sheet from the stack and writes an address in Drezen, then a time.{/n}
"A small reception. Attend after the formal speeches, if you would like to discover whether I can discuss something other than your administration."''', c('[Accept the invitation.]', flags=("konomi.invited",))),
    n("invitation", "Konomi", '''"You are inviting me before learning whether I am pleasant company."
{n}She lets you consider that, plainly enjoying herself.{/n}
"There is a reception I must attend. Come after the speeches. If you bore me, I shall have three barons to escape to. If I bore you, the wine is adequate."
{n}She writes the details on a fresh sheet. Her pen pauses before she hands it over.{/n}
"This is not an instruction from the Royal Council."''', c('"I had hoped it was from you."', flags=("konomi.invited", "konomi.direct",))),
    n("official", "Konomi", '''"Very well. It is the cheaper arrangement for both of us."
{n}She files the corrected report. The next document is already waiting.{/n}
"You will still receive my advice, naturally. This arrangement offers no escape from that."''', c('[Keep the relationship professional.]', flags=("konomi.closed",))),
])

s("reception", "After the speeches", 3, '"I have not forgotten your invitation."', [
    n("start", "Konomi", '''{n}The reception occupies a room too small for its guests' opinions. Konomi finds you near the door before someone can begin another speech.{/n}
"I have claimed a quiet corner. Come with me before somebody asks you to improve the occasion."
{n}Her own glass is almost untouched. She has changed out of the clothes she wears to council, but the expression with which she judges the room is familiar.{/n}''',
      c('"Who are we avoiding?"', "room"),
      c('"I came to see you. Would you like to leave?"', "leave")),
    n("room", "Konomi", '''"The woman by the window believes she can arrange marriages by rearranging chairs. The man beside her wishes to explain the entire war to you."
{n}Konomi steers you toward a less crowded corner.{/n}
"Arsinoe helped arrange the collection for the city's bereaved families. If you want a conversation with a purpose, ask her where the money goes. She will know down to the last coin."
{n}Her voice softens just a little.{/n}
"I appreciate that in a person."''',
      c('"I would like to speak to Arsinoe another time. Tonight I am here with you."', "private", flags=("arsinoe.introduced",)),
      c('"You appreciate someone who takes promises seriously."', "private", flags=("konomi.noticed_duty",))),
    n("leave", "Konomi", '''{n}She looks at you over the rim of her glass.{/n}
"I have been here less than an hour. Leaving with you now would be remarked upon."
{n}She sets the glass down.{/n}
"Give me ten minutes to be properly unremarkable. There is a covered walk beyond the door at the back."''', c('[Wait for her at the covered walk.]', "private", flags=("konomi.bold",))),
    n("private", "Konomi", '''{n}You eventually find a little privacy beneath the covered walk. Through the open door, conversation rises and falls around the scrape of chairs.{/n}
"A useful discovery," {n}Konomi says.{/n} "Neither of us has asked the other to approve a proposal for several minutes."
{n}She rests against a pillar, looking toward the lights inside.{/n}
"I receive invitations constantly. Most are addressed to the office I occupy. A few would be withdrawn if I ceased to be useful."
{n}Her attention returns to you.{/n}
"What should I make of yours?"''',
      c('"That I would still want you here after an argument I lost."', "interest", flags=("konomi.respects_difference",)),
      c('"That I am attracted to you, and would rather say so than arrange a dozen excuses."', "interest", flags=("konomi.direct",)),
      c('"I enjoy your company, but I am not certain I want a romance."', "slow", flags=("konomi.unhurried",))),
    n("interest", "Konomi", '''"Good. That saves me the indignity of pretending I thought this was a discussion of charitable accounts."
{n}She smiles openly now. It changes her face more than the different clothes did.{/n}
"I am interested. I am also likely to remain inconvenient. You should consider both facts."
{n}Someone calls her name from the room. She waits a moment before answering.{/n}
"Write to me tomorrow. Something short. I read enough long explanations."''', c('[Promise her a short letter.]', flags=("konomi.attracted",))),
    n("slow", "Konomi", '''{n}She nods, though her expression becomes more careful.{/n}
"Then I will not announce that you have made up your mind. Nor will I pretend I am indifferent."
{n}A burst of laughter comes through the door. She looks back at the reception with something close to reluctance.{/n}
"Write to me if you want another evening. Keep it short and keep it truthful. I read forged enthusiasm for a living, and I bill for it."''', c('[Keep the invitation open.]', flags=("konomi.attracted",))),
], requires=("konomi.margin",), delay=24)

s("letter", "A sentence she keeps", 3, '"Did my letter meet your standards?"', [
    n("start", "Konomi", '''{n}Your letter lies beside Konomi's writing case. It has been folded and opened more often than its short contents require.{/n}
"The opening is good," {n}she says.{/n} "The conclusion attempts to conceal an invitation inside a comment about the weather. I have seen stronger evasions from junior clerks."
{n}She places a finger beside the final line.{/n}
"Would you care to improve it?"''',
      c('"I want to spend an evening alone with you."', "alone", flags=("konomi.plain_words",)),
      c('"I enjoy the part where you find an excuse to read it again."', "tease", flags=("konomi.teasing",))),
    n("tease", "Konomi", '''{n}She lifts her hand from the letter.{/n}
"You should be careful. I might begin saying exactly what I think of you."
{n}The warning contains very little warning.{/n}
"For example, that I have been looking forward to this conversation all morning, and have resented every interruption."''', c('"Then let us make the next conversation harder to interrupt."', "alone")),
    n("alone", "Konomi", '''"I have a room where nobody will mistake your arrival for a summons."
{n}She closes the writing case, leaving your letter outside it.{/n}
"First, the articles. I negotiate nothing without them."
{n}She taps the edge of the writing case with her closed fan, once for each point.{/n}
"Article one: I know perfectly well I may not be the only name in your correspondence. I do not want a register of the others; I can buy one from any clerk in Drezen. Article two: whatever you promise me, you deliver, or I bill you for it. Article three: my evenings are not remainders. I am not to be paid at the end of the day with whatever is left in the purse."
{n}The fan comes to rest against her chin.{/n}
"And I will not make myself cheaper to win the bidding. If that is what you came to buy, the shop is closed."''',
      c('"I can give you that, without promising to agree with you."', "terms", flags=("konomi.honest_terms",)),
      c('"I would like that. I also want us to keep this private for now."', "terms", flags=("konomi.private_first",)),
      c('"I cannot afford those terms."', "stop")),
    n("terms", "Konomi", '''"Agreement would make an implausible promise from either of us."
{n}She gives you the time for your next meeting. Then, with the arrangement settled, she turns your letter over and writes one sentence on its back.{/n}
{n}You read it when you are alone: I have kept the evening free.{/n}''', c('[Keep the evening free yourself.]', flags=("konomi.terms",))),
    n("stop", "Konomi", '''{n}She folds the letter along its old crease.{/n}
"Then we close the negotiation before either of us signs something we cannot honour. It is the only clean way to end one."
{n}She keeps the letter. You do not ask why.{/n}''', c('[End the courtship.]', flags=("konomi.closed",))),
], requires=("konomi.reception",), delay=24)

s("evening", "No business before morning", 3, '"You said you would keep this evening free."', [
    n("start", "Konomi", '''{n}Konomi opens the door herself. The room beyond is modest, with a supper waiting and no official papers in sight. A small dish holds the pins she has taken from her hair.{/n}
"I have been instructed that ordinary hospitality does not require an agenda. You may imagine how difficult this has been for me."
{n}She steps aside to let you enter.{/n}
"What shall we talk about?"''',
      c('"Tell me something you enjoy that you are bad at."', "supper"),
      c('"I was hoping to hear what you think of me when you are not writing a report."', "opinion")),
    n("opinion", "Konomi", '''"You have come here expecting to be interesting. I am tempted to spend the evening discussing my plants just to see how you bear it."
{n}Her eyes move toward an empty pot on the windowsill. She sighs.{/n}
"Unfortunately, the plants would make a rather brief conversation."''', c('"An unsuccessful hobby? Now I want to hear about it."', "supper")),
    n("supper", "Konomi", '''"Gardening," {n}she says.{/n} "I have killed three perfectly respectable plants by following instructions too precisely."
{n}She points toward a bare pot on the windowsill.{/n}
"That one objected to being watered. The previous one objected to the opposite. I have begun to suspect a political motive."
{n}The conversation becomes easier. She describes a journey spoiled by a guide who refused to admit he was lost, then allows you to discover how long she argued before admitting she had chosen him.{/n}
"As for what I think of you," {n}she says,{/n} "I am beginning to think I would miss these evenings even if you ceased to be interesting to anybody else."''',
      c('[Move closer and kiss her.]', "kiss", forbids=("inhuman",)),
      c('"Let me stay tonight."', "stay", forbids=("inhuman",)),
      c('"My transformation makes an ordinary evening difficult. I still want one with you."', "changed", requires=("inhuman",)),
      c('"Tell me how the guide story really ended. I am not leaving until you do."', "quiet")),
    n("kiss", "Konomi", '''{n}She meets your kiss before you have quite stopped moving. For a moment she forgets the careful distance she usually keeps, drawing you nearer by your sleeve.{/n}
{n}When she lets you go, her expression is almost accusing.{/n}
"You have made it rather difficult to return to the subject of gardening."
{n}She does not release your sleeve.{/n}''',
      c('"We can leave the plants to their own devices tonight."', "stay"),
      c('[Kiss her again, then stay to talk until late.]', "quiet", flags=("konomi.kissed",))),
    n("stay", "Konomi", '''"Yes."
{n}No qualification, no counter-offer. She shuts the door with her heel and comes back to you already working at the ties of her outer robe, as if she has been drafting this in her head all through supper.{/n}
"I have wanted you across this table since the margin of that report. Do not make me wait while you hunt for the clasp. It is at the back."
{n}You find it. The silk slides from her shoulders onto the cushions. She catches your mouth before you can look down, her fingers working swiftly through your fastenings. When your hands reach her bare waist, her breath breaks against your lips.{/n}
"Here. I have waited long enough."
{n}She draws you down onto the cushions and pulls you close, her hair spilling over your cheek. The silk is gone, and so is whatever remained of her patience. She lies back with her knees drawn up either side of you, flushed to the collarbone, and drags your hand down her body to show you where she has wanted it all through supper. Her breath breaks on it. She makes no effort to be quiet about that either.{/n}
"Do not make me ask twice, Commander. I never ask twice."
{n}In the morning she borrows your comb, criticizes it, and uses it anyway. Before you leave, she catches you at the door for another kiss.{/n}
"No business until after breakfast," {n}she says.{/n} "I am making that a rule."''', c('[Agree to the rule.]', flags=("konomi.lovers", "konomi.private_night"))),
    n("quiet", "Konomi", '''"Then sit down. The luggage is the worst part, and I have never told it sober."
{n}She brings another lamp closer and settles beside you. At some point she stops trying to repair the impression made by the story of her disastrous guide, and tells you what happened to the luggage.{/n}
{n}When you finally leave, she asks you to come again before either of you has accumulated a plausible official reason.{/n}''', c('[Promise another evening.]', flags=("konomi.lovers", "konomi.quiet_evening"))),
    n("changed", "Konomi", '''{n}Her gaze rests on the supper she prepared. She had arranged it from habit, then spent too long deciding whether removing it would be worse.{/n}
"I planned this supper for somebody else," {n}she says.{/n} "An error in my intelligence. I dislike errors in my intelligence."
{n}She moves the unused place setting aside and puts your letter there instead.{/n}
"So I shall do what I do with any new delegation. Tell me what you still take pleasure in, and I will arrange the next evening around it. I do not repeat a bad reception."
{n}You talk until the lamp needs tending. She reads a few lines aloud at your request, and stops to complain each time she catches you watching her instead of the page. She does not stop reading.{/n}''', c('[Stay with her through the quiet hours.]', flags=("konomi.lovers", "konomi.changed_closeness"))),
], requires=("konomi.letter",), delay=24)

s("disagreement", "The advice she will still give", 3, '"Your latest memorandum was remarkably unsentimental."', [
    n("start", "Konomi", '''"It concerned provisions, not sentiment."
{n}Konomi taps the memorandum once. She recommends retaining a disputed shipment for Drezen. A petition from a smaller settlement asks that it be diverted before winter.{/n}
"There is a reserve the petitioners do not know about. It is smaller than they need and larger than nothing. I have asked for reliable figures."
{n}She looks up.{/n}
"You have read this twice. The first time as Commander, I hope. The second seems to have annoyed you more."''',
      c('"I hoped you would understand why I want to help them."', "mercy", flags=("konomi.aid_priority",)),
      c('"I agree about the reserve. I dislike being treated as if I have not considered it."', "respect", flags=("konomi.reserve_priority",)),
      c('"I am worried that sharing your supper table will make one of us go easy on the other\'s memoranda."', "frank", flags=("konomi.frank_disagreement",))),
    n("mercy", "Konomi", '''"I understand perfectly. Understanding you is not the same as being convinced."
{n}She sets the memorandum on top of the petition, covering its appeal.{/n}
"When Drezen's reserve fails, those petitioners will not answer to the capital. You will. My recommendation will reach Nerosyan with your decision beside it."
{n}She taps the names beneath the appeal.{/n}
"I shall get their figures. If they can spare more than they admit, I intend to find out before you give them ours."''', c('"Get the figures. Then argue with me using them."', "end")),
    n("respect", "Konomi", '''{n}She reads her opening paragraph again, then turns the memorandum toward you.{/n}
"That sentence was written for Nerosyan as well as for you. They will ask whether I warned you. I intend to leave them no doubt."
{n}Her finger rests on the reserve figure.{/n}
"You agree with the recommendation. Excellent. Give me an answer I can send to the capital, and we can spend supper on something more interesting."''', c('"You will have it."', "end")),
    n("frank", "Konomi", '''"You believe I am in danger of becoming too agreeable?"
{n}She nearly smiles, then sees that you mean the question.{/n}
"I am far more likely to overcharge you to prove that I am not. Ask anyone I have ever been fond of."
{n}She pushes the petition toward you.{/n}
"So we do it the dull way. Figures on the table, both of us, and we fight over the grain, not over each other. Begin with the people whose supper this is."''', c('[Return to the petition with her.]', "end")),
    n("end", "Konomi", '''{n}The recommendation goes back into the ordinary channel with both your names on the dispute. Konomi refuses to promise grain she does not hold; you refuse to settle a council matter over supper. Each of you plainly suspects the other of trying.{/n}
{n}The argument is not entirely finished when she puts her papers away.{/n}
"I am still expecting you tomorrow," {n}she says.{/n} "Unless you intend to deprive us both of supper until I become less stubborn."''', c('"Tomorrow. We may need a larger supper."', flags=("konomi.argument_survived",))),
], requires=("konomi.evening",), delay=24)

s("leak", "A letter in the wrong hands", 3, '"You look as though you have received unwelcome news."', [
    n("start", "Konomi", '''{n}Konomi has a copy of one of your private letters. It bears a second person's annotations and a third person's seal.{/n}
"Somebody wishes me to know that my judgment is being discussed. They have chosen an unusually intimate passage to illustrate the concern."
{n}She lays it flat before you. Her anger is controlled, but there is nothing detached about it.{/n}
"I can answer this within the hour. But it is your name on the other half of the page, and I do not sell what I do not own. What do you want said?"''',
      c('"Acknowledge the relationship. We have not sold our decisions to one another."', "public", flags=("konomi.public",)),
      c('"Confirm it privately to those who need to know. The rest is ours."', "discreet", flags=("konomi.discreet",)),
      c('"Tell them the letter was fabricated."', "lie")),
    n("public", "Konomi", '''"They will examine every disagreement for evidence that one of us is being punished. Every agreement will look like a purchase."
{n}She lets the silence run long enough for you to retreat. You do not. She sits down to write.{/n}
"Very well. I will state what is true, and keep documenting my recommendations as I always have. Do the same, or they will say I write your opinions for you."
{n}Her first draft is formidable. Her second is shorter and angrier.{/n}''', c('"May I suggest removing the part about their imaginative deficiencies?"', "together")),
    n("discreet", "Konomi", '''"Sensible. Discretion costs less than a denial, and it is far harder to quote."
{n}She begins a reply to the sender, naming the people authorized to discuss a concern about her work.{/n}
"I resent having to make that distinction in a letter about whom I choose to spend my evenings with."
{n}She looks at you with sudden tiredness.{/n}
"For tonight, I would like one person in this room who is not assessing the consequences."''', c('"Then let me stay after you finish writing."', "together")),
    n("lie", "Konomi", '''"No."
{n}She does not raise her voice.{/n}
"Do not ask me to call a letter false because somebody made us ashamed to have written it. If you want to leave, say so. If you want discretion, we can arrange it."
{n}Her hand rests beside the copied page, rigid against the table.{/n}''',
      c('"You are right. Confirm it privately. We owe them no further details."', "discreet", flags=("konomi.discreet", "konomi.almost_denied",)),
      c('"I am not willing to acknowledge this relationship."', "end")),
    n("together", "Konomi", '''{n}She finishes the letter, then places it beside the door for collection. The copied private page she folds away separately.{/n}
"I dislike that they have seen this," {n}she says.{/n} "I do not regret what it says."
{n}The evening is quieter than either of you planned. When she finally laughs at something you say, it sounds as though she has been holding her breath for hours.{/n}''', c('[Stay until she throws you out.]', flags=("konomi.kept_each_other",))),
    n("end", "Konomi", '''{n}Konomi retrieves your letters from her writing case and ties them together.{/n}
"Then I will acknowledge that it existed, and that it has ended. I will not send them the rest."
{n}She places the bundle in a drawer and closes it.{/n}
"My next memorandum will concern the crusade. Please answer it on those terms."''', c('[Leave.]', flags=("konomi.closed", "konomi.denied",))),
], requires=("konomi.disagreement",), delay=24)

s("reckoning", "The copy she wanted them to read", 3, '"Has there been an answer to your letter?"', [
    n("start", "Konomi", '''{n}Three letters lie open on Konomi's desk. Beside them is the settlement's petition, covered in figures written by several different hands.{/n}
"Two answers. One from Nerosyan, and one from a man who has just discovered that private correspondence can be embarrassing."
{n}She draws a chair closer with her foot, absorbed enough to forget to make the gesture look graceful.{/n}
"Sit down. I have been waiting to tell you."''',
      c('"Start with Nerosyan. What has our public answer cost you?"', "public", requires=("konomi.public",)),
      c('"You sound pleased. Did our discreet answer work?"', "discreet", forbids=("konomi.public",))),
    n("public", "Konomi", '''"A noble household whose couriers I use wants copies of my recommendations. Otherwise I am to find my own messengers. Its secretary calls this reassurance."
{n}She shows you the letter. The household has also withdrawn her invitation to a private policy dinner.{/n}
"That part is meant to hurt. Decisions are made over those dinners before anybody sees a formal proposal. I will have to find another way into the conversation."
{n}She is angry, but her finger has already moved to a name in the margin.{/n}
"Fortunately, the hostess dislikes being told whom she may invite."''',
      c('"Will you challenge the review?"', "audit", flags=("konomi.public_cost",))),
    n("audit", "Konomi", '''"Its scope. The secretary may read my published advice. He will not inspect my bedroom. I have sent a very precise answer, and a second letter to somebody who will enjoy repeating it."
{n}Her smile is sharper than it was a moment ago.{/n}
"Now they must either accept the limit or explain why their reassurance requires a description of my nights. I almost hope they try."''', c('"And the person who copied our letter?"', "source")),
    n("discreet", "Konomi", '''"Our reply went to the officials who needed an answer. The rest received three different, utterly dull accounts of a proposed inspection. Each account named a different day."
{n}She lays a fourth sheet beside them.{/n}
"This arrived from somebody who had no reason to know about any inspection. He complained about the inconvenience of the second day."
{n}She looks up, delighted.{/n}
"People who trade in secrets hate being excluded from an uninteresting one. He had to tell somebody he knew."''',
      c('"You found the channel they used."', "source", flags=("konomi.traced_leak",))),
    n("source", "Konomi", '''"An intermediary who wanted access to my correspondents. I checked which copyist handled my writing case and asked him to account for the work. He preferred naming his buyer to taking responsibility for everything the buyer had done with it."
{n}She closes one letter with a satisfied tap.{/n}
"The copyist will no longer handle my correspondence. I have asked for a hearing about the payment. If I simply threaten the buyer into silence, he will try somebody less inconvenient next time."
{n}For a moment she studies the papers without speaking.{/n}
"I enjoyed finding him. More than I expected. There were three people pretending to help one another, and every one of them believed the other two had missed something."
{n}She glances at you.{/n}
"You need not look so surprised. I do sometimes enjoy my profession."''',
      c('"I was enjoying watching you enjoy it. What happened to the petition?"', "petition")),
    n("petition", "Konomi", '''"Their reserve was spoiled. They were ashamed to admit how much, and our estimate was wrong."
{n}She turns the petition so you can read the correction.{/n}
"I sent the figures to the charitable collection in Nerosyan. They have agreed to purchase grain for the settlement through their own suppliers. It will not come out of the shipment assigned to Drezen."
{n}A second sheet lists the donation and the supplier's receipt.{/n}
"The first delivery is accounted for. I have asked who will check the storehouse before they put the next one in it. Feeding people twice because nobody repaired a roof is an expensive form of generosity."''',
      c('"I am glad you kept asking. They needed help."', "aid", requires=("konomi.aid_priority",)),
      c('"That protects Drezen without leaving them hungry."', "reserve", requires=("konomi.reserve_priority",)),
      c('"We found a better answer by finishing the argument."', "frank")),
    n("aid", "Konomi", '''"Yes. You were right about the urgency. I was irritated enough by your tone that I nearly made you prove it twice."
{n}She leaves the corrected figures where you can see them.{/n}
"I would rather you remembered this admission than made me repeat it in front of the council."''', c('"I intend to remember it very fondly."', "end")),
    n("reserve", "Konomi", '''"It does. Though agreeing with you would have been considerably less work if the original figures had been true."
{n}She stretches her cramped writing hand.{/n}
"Next time, we ask to see the storehouse before congratulating ourselves on our arithmetic."''', c('"Agreed. Put down the pen for a while."', "end")),
    n("frank", "Konomi", '''"We did. Do not grow too fond of that conclusion. Sometimes one of us will simply be wrong."
{n}She places the receipt on top of the petition.{/n}
"But I would like to think we will notice before the grain arrives."''', c('"And say so when we do."', "end")),
    n("end", "Konomi", '''{n}She puts away the papers, still smiling to herself. Then she catches you watching her.{/n}
"What?"''',
      c('"You are enjoying yourself. I find it difficult to look away."', "close", forbids=("konomi.almost_denied",)),
      c('"Before we celebrate, I owe you an apology for asking you to deny our letter."', "repair", requires=("konomi.almost_denied",))),
    n("repair", "Konomi", '''{n}She lets go of the papers.{/n}
"Yes. You do. I keep remembering how quickly you offered to make me an invention."
{n}She looks at the closed drawer that holds your letters.{/n}
"You were frightened. Frightened people ask for forgeries. I have drafted enough of them for other people to know the smell."
{n}Her fan opens a finger's width and closes again.{/n}
"Next time you are frightened, come and say so. I can work with a frightened ally. I cannot work with one who hands me a lie to sign."''',
      c('"I was frightened. It was a poor bargain, and I will not offer it to you again."', "repaired", flags=("konomi.apologized",))),
    n("repaired", "Konomi", '''"Noted. I shall hold you to it the next time a rumour comes through my door."
{n}She hooks the chair beside her with her foot and drags it closer. The argument is not closed; she is simply tabling it.{/n}
"Sit. You are no use to me standing in the doorway looking penitent."''', c('[Stay with her.]', flags=("konomi.petition_resolved", "konomi.scandal_answered"))),
    n("close", "Konomi", '''{n}The compliment holds her attention longer than the letters did.{/n}
"Come here, then. I have been very patient while you admired me from the other side of the desk."''',
      c('[Kiss her, and let her tell you the parts she left out.]', flags=("konomi.petition_resolved", "konomi.scandal_answered"), forbids=("inhuman",)),
      c('[Take the place beside her and stay.]', flags=("konomi.petition_resolved", "konomi.scandal_answered"))),
], requires=("konomi.leak",), delay=48)

SCENES.append(scene("konomi.unsent", "A letter with nowhere to go", "Konomi", 4, "", [
    n("start", "Narrator", '''{n}In the Abyss, a letter can become a bargain before it reaches the person named on its outside. You set aside the idea of finding a courier and take out a fresh sheet instead.{/n}
{n}You begin an account of what you have seen. Halfway through the first page you realize you are explaining yourself to the Royal Council, and cross it out.{/n}
{n}Konomi asked you for something shorter and more difficult.{/n}''',
      c('[Write about something you wish she had been there to see.]', "wonder", flags=("konomi.letter_wonder",)),
      c('[Write about what the Abyss is doing to you.]', "fear", flags=("konomi.letter_fear",))),
    n("wonder", "Narrator", '''{n}You try to describe the light first. That seems safe enough. A reflection in a dark window, a color you could not have named at home. The sentence becomes so elaborate that you can almost hear Konomi asking what, precisely, she is supposed to picture.{/n}
{n}You cross out half of it.{/n}
{n}What you wanted was the moment afterward: turning to make a remark, discovering that the person you wanted to tell was not beside you. You have companions here. That does not make them interchangeable.{/n}
{n}On the paper you write: "You would have disliked my description. I wanted to hear you improve it."{/n}
{n}You hesitate before the next sentence. There are beautiful things here. Writing that does not excuse what happens beneath their light, but you wonder whether she will mistake delight for a favorable report.{/n}''',
      c('[Keep the beauty in the account. Tell her what you wished you could share.]', "write", flags=("konomi.letter_beauty_kept",)),
      c('[Add why enjoying the sight made you uneasy.]', "write", flags=("konomi.letter_beauty_uneasy",))),
    n("fear", "Narrator", '''{n}You begin with "I am afraid," then stop. Konomi would strike that out as unspecific. Afraid of dying? Of failing? Both are true often enough to be useless in a report.{/n}
{n}You turn the sheet over and start again, as though she were reading it across her desk with her pen already uncapped. She would want the fact under the fear, the thing that has actually changed in the person who will bring this letter home.{/n}
{n}It takes longer to write than any account of a demon.{/n}''',
      c('[Write that power might make agreement difficult to distinguish from obedience. Ask her to question one decision when you return.]', "fear_judgment", flags=("konomi.letter_question_me", "konomi.letter_judgment",)),
      c('[Write about that same risk, but tell her you will make your own report first and she may tear it apart after.]', "fear_judgment", flags=("konomi.letter_hear_me", "konomi.letter_judgment",)),
      c('[Write that you fear ordinary pleasures will taste of nothing when you return.]', "fear_ordinary", flags=("konomi.letter_hear_me", "konomi.letter_ordinary",))),
    n("fear_judgment", "Narrator", '''{n}"I do not want to become someone whose certainty comes from never hearing a refusal."{/n}
{n}You read the sentence twice. Konomi refuses people for a living. She will know exactly what you are asking her for, and exactly what to charge. You underline nothing; she despises underlining.{/n}''', c('[Finish the letter.]', "write")),
    n("fear_ordinary", "Narrator", '''{n}"I want to come home and enjoy a ridiculous story without waiting for something dreadful to interrupt it. I am afraid I shall spend the whole evening waiting."{/n}
{n}You nearly ask her to promise that it will pass. She never promises what she cannot deliver, and she would think a little less of you for asking. Instead you write: "Come to supper and prove me wrong."{/n}
{n}The next line comes more easily. You ask her to save a particularly bad story. It need not be one she is willing to put in writing.{/n}''', c('[Finish the letter.]', "write")),
    n("write", "Narrator", '''{n}The letter stays with you. It does not summon an answer or prove that she would approve of what you have done.{/n}
{n}You find room for one ordinary question at the bottom: Did the next plant survive?{/n}
{n}Then you fold it for a journey you still intend to make.{/n}''', c('[Keep the unsent letter.]', flags=("konomi.wrote",))),
], Relationship="konomi", Remote=True, requires=("konomi.evening",), delay=24, last=4, optional=True))

s("return", "An account for her alone", 5, '"There are things about the Abyss I would like to tell you privately."', [
    n("start", "Konomi", '''{n}Konomi closes her writing case when you arrive. Whatever she was working on can wait, though the decision plainly costs her an effort.{/n}
"Three reports about you reached Nerosyan. One says you came out of the Abyss improved. One says you did not come out at all, and that I am taking supper with something wearing your coat. The third was written by a man who owes me money, so I discount it."
{n}She folds her hands on the closed case.{/n}
"I have to answer all three. I would rather answer them with yours. Where do we begin?"''',
      c('[Give her the letter you wrote in the Abyss.]', "letter", requires=("konomi.wrote",)),
      c('"The one I have not put into a report."', "talk", forbids=("konomi.wrote",)),
      c('"First, tell me how you have been."', "hers")),
    n("letter", "Konomi", '''{n}She reads the letter slowly. When she reaches the final question she looks toward the bare pot by the window.{/n}
"No," {n}she says.{/n} "But I have kept the pot. Apparently I remain hopeful."
{n}She folds the sheet along its worn creases.{/n}
"You kept it. Good. A letter written in the Abyss and carried home unposted is worth ten reports to the Council. I intend to keep it somewhere the Council will never think to look."''',
      c('[Tell her the rest in person.]', "talk", forbids=("konomi.letter_wonder", "konomi.letter_fear")),
      c('[Ask what she made of the sight you described.]', "wonder_reply", requires=("konomi.letter_wonder",), forbids=("konomi.letter_fear",)),
      c('[Let her answer the fear you put on the page.]', "fear_reply", requires=("konomi.letter_fear",), forbids=("konomi.letter_ordinary",)),
      c('[Ask about the bad story you requested.]', "ordinary_reply", requires=("konomi.letter_fear", "konomi.letter_ordinary"))),
    n("wonder_reply", "Konomi", '''"I should have liked to see it."
{n}She says this while still looking at the letter. When she notices your expression, she raises an eyebrow.{/n}
"You were expecting a correction? I have several. They need not be my first response."
{n}She moves the lamp between you and lifts an empty glass beside it. The light makes a pale oval on the writing case.{/n}
"Was it anything like that?"
"Not much."
"Then your description has failed magnificently. Try again."
{n}You move the glass and tell her where the light fell. She asks about the edges, the things beyond it, what you could hear while you stood there. For a little while the desk holds an attempted reconstruction of somewhere she has never been.{/n}
"I would have wanted to leave," {n}she says eventually.{/n} "I can still wish I had stood beside you for that moment."''',
      c('"I kept wondering whether liking anything there meant I was becoming used to the rest."', "wonder_uneasy", requires=("konomi.letter_beauty_uneasy",)),
      c('"I wanted you there for yourself. Not to approve the place."', "wonder_personal", forbids=("konomi.letter_beauty_uneasy",))),
    n("wonder_uneasy", "Konomi", '''"Did you stop noticing the rest?"
{n}She asks it the way she asks a quartermaster whether his count includes the spoiled sacks.{/n}
"Not always."
"Then I want those days in the account as well. A report with every pleasant thing cut out of it is a report somebody has edited for my benefit, and I charge extra for reading those."
{n}She puts the glass down. The oval disappears.{/n}
"I have attended delightful evenings in houses whose owners I distrust. The music did not make them honest. Distrusting them did not make the musicians poor. What I agreed to before leaving mattered rather more."
"You make it sound simple."
"I make it sound separable. That is useful when it is not simple."
{n}She turns the page back toward you and taps the margin where she expects the missing days to go.{/n}''', c('[Tell her about what the beautiful account left out.]', "talk", flags=("konomi.wonder_answered",))),
    n("wonder_personal", "Konomi", '''{n}Her hand stops on the base of the glass.{/n}
"Yes. I understood that part. I have read it twice."
{n}She lets you see the pleasure before looking away.{/n}
"While you were gone, I kept hearing things I intended to tell you. A dreadful remark at supper. A particularly accomplished lie. Once, something kind that I would have spoiled by explaining why it surprised me."
"You could tell me now."
"I intend to. You will have to endure several introductions. I have forgotten which names I already explained."
{n}She draws her chair closer to yours. The letter remains open between the lamp and the abandoned work.{/n}''', c('[Ask her to begin with the kindness.]', "kindness", flags=("konomi.wonder_answered",))),
    n("kindness", "Konomi", '''"A guest at supper could not read the names on the place cards. He had forgotten his spectacles and preferred to stand in everyone's way rather than admit it."
"What did you do?"
"Before I did anything, the woman beside him complained that her own card had been put in the wrong place. Asked him to help her find it. Then read every name aloud, as though she were too irritated to keep the search to herself."
{n}Konomi smiles at the recollection.{/n}
"She found his place before finding her own. Naturally."
"Did he realize?"
"I think so. He spent the evening passing her everything before she asked for it. They made a considerable nuisance of themselves over the salt."
{n}She smooths the edge of your letter.{/n}
"I had been looking forward to that dinner for an entirely different reason. There was someone I wanted to corner before he could leave with another invitation unacknowledged. I did manage it. But afterward I kept thinking about those two."
"You wanted to tell me."
"Yes. It was a small thing. It became irritatingly important that you should hear it from me."
{n}Her hand comes to rest against yours.{/n}''', c('[Tell her something you have been keeping for this conversation.]', "talk")),
    n("fear_reply", "Konomi", '''{n}She rereads the part where you told her you were afraid. Her thumb follows the crease beneath it.{/n}
"You have handed me a confession with no figures in it. A lesser woman could make a career of this letter."
{n}She sets the letter down.{/n}
"I know what it is to mistake a room falling silent for a room being persuaded. I also know that discovering the mistake does not oblige me to abandon every recommendation I made in that room."
"What did you do?"
"Asked one of the people who had stopped speaking. I did not enjoy the answer."
{n}Her eyes return to you.{/n}
"You wrote me a request. I read requests closely, Commander. Which one am I answering?"''',
      c('"One question, as I asked in the letter. Make it a hard one."', "fear_question", requires=("konomi.letter_question_me",)),
      c('"My report first, as the letter said. Then tear it apart."', "fear_listen", requires=("konomi.letter_hear_me",)),
      c('"Ask me one question. I will answer it properly."', "fear_question", forbids=("konomi.letter_question_me", "konomi.letter_hear_me")),
      c('"Let me speak first. Then have your opinion. I know you have one."', "fear_listen", forbids=("konomi.letter_question_me", "konomi.letter_hear_me"))),
    n("ordinary_reply", "Konomi", '''"I have several. Choosing the worst will require some thought."
{n}She leaves the letter open on her knee.{/n}
"Do not laugh out of courtesy. I have been paid in polite laughter by three ambassadors and a margrave, and it is counterfeit coin."
"That sounds like a threat."
"A term of trade. I tell the story; you pay in real laughter or none."
{n}She begins with a dinner guest who spent several minutes complimenting an absent hostess's portrait before discovering that it depicted her grandmother. Konomi had watched him decide whether to make the mistake worse by pretending he had known.{/n}
"He chose to continue," {n}she says.{/n} "Courage is not always helpful."
{n}You ask what she did. Her smile becomes distinctly less charitable.{/n}
"Asked which resemblance he found most striking."
{n}She waits for your answer with the letter still on her knee and the fan tapping the arm of her chair, entirely certain you will ask.{/n}''',
      c('"You enjoyed that far too much. Tell me what he said."', "guest_answer", flags=("konomi.fear_answered",)),
      c('"Stay a little. I want to hear it even if I am poor company tonight."', "talk", flags=("konomi.fear_answered",))),
    n("guest_answer", "Konomi", '''"He said the eyes. A sensible retreat. Then he added that he had always admired a woman who could command a room without raising her voice."
"The portrait?"
"The grandmother had been dead for eleven years. Our hostess asked whether he meant the summer she had thrown a magistrate out of her house. He said that was precisely the occasion he had in mind."
{n}Konomi laughs, briefly abandoning any pretense of sympathy.{/n}
"I believe he would have claimed to be the magistrate if it had offered him a way out."
"Did you give him one?"
"Eventually. I asked about his journey. He took so long describing the road that I nearly regretted it."
{n}She folds your letter at last and places it inside her writing case, apart from the official papers.{/n}''', c('[Stay and exchange the stories neither of you put in a report.]', "talk")),
    n("fear_question", "Konomi", '''"Whose objection have you kept thinking about?"
{n}Konomi reaches for her pen, notices what she is doing, and leaves it on the desk.{/n}
"No minutes," {n}she says.{/n} "This goes in no register, not even the one in my head. Speak."
{n}You begin with the objection rather than your answer to it. She interrupts once to ask whether those were the words spoken or the meaning you gave them afterward. You start again.{/n}
{n}When you finish, she gives her verdict without softening it.{/n}
"Go and ask whoever it was whether you heard them right. If you were wrong, you lose a little pride. If you were right, you have a quarrel worth having, which is better than a silence you mistook for agreement."
"And if I cannot ask?"
"Then do not forge their answer so that you can sleep tonight. I would catch it. I catch everyone's."
{n}Her hand comes to rest on the desk beside yours, close enough to touch, and she leaves it there.{/n}''', c('[Stay and continue the account.]', "talk", flags=("konomi.fear_answered",))),
    n("fear_listen", "Konomi", '''"Then speak. I warn you, there is a dispatch on this desk that says otherwise, and I intend to read it to you afterward."
{n}She lays it face down beside the lamp: a captain's report from the Abyss, sealed for Nerosyan and opened, without apology, by her. You give your account. Halfway through she turns the dispatch over and reads one line aloud: that the Commander gave an order below and not one soul present dared to question it.{/n}
"Is that true?"
"Some of it."
"Which part? I must answer this captain, and I would rather not lie on your behalf. I charge a great deal for that, and you cannot afford me this season."
{n}You tell her which part. She writes nothing down. When you finish, she taps the dispatch with one finger.{/n}
"My opinion, since you did not ask for it. You came back with a habit of being obeyed. I watched it in the doorway: you expected me to put down my pen, and I did. I intend to stop doing that. You will find me considerably more irritating from now on."
"I know."
"Good. Move the lamp toward you. I have been watching you pretend that the light is not in your eyes."''', c('[Move the lamp and hear her answer.]', "talk", flags=("konomi.fear_answered",))),
    n("hers", "Konomi", '''"Busy. Angry. Frequently misinformed."
{n}She begins with the work, as you expected. Then she describes the contradictory reports that arrived during your absence, and the awful business of recommending a course of action without knowing which disaster had actually occurred.{/n}
"I learned which correspondents would admit to being frightened. They were generally more useful than the ones determined to sound certain."
{n}She turns her chair toward yours.{/n}
"Now tell me something true."''', c('[Give her an honest account.]', "talk")),
    n("talk", "Konomi", '''{n}You talk until the light changes at the window. Konomi listens like a negotiator, interrupting when a detail does not add up and once, sharply, when something frightens her.{/n}
"I will not like all of it," {n}she says.{/n} "I would rather have the true file on you than the flattering one. The flattering one is what Nerosyan already has."
{n}Before you leave, she asks when you can come again.{/n}''', c('[Choose another evening together.]', flags=("konomi.returned",))),
], requires=("konomi.reckoning",), delay=24)

s("power", "The person beneath the title", 5, '"My power has grown. I expect you have an opinion about it."', [
    n("start", "Konomi", '''"Yes. We should."
{n}Konomi has brought no memorandum. She watches the place where you stand as though expecting the room itself to take sides.{/n}
"I have spent years learning what a promise can accomplish and what it cannot. You have acquired a talent for making the second category embarrassingly small."
{n}She considers you steadily.{/n}
"So I am asking the only question a diplomat asks a stronger party. When I refuse you, am I still a counterpart, or have I become an obstacle you remove?"''',
      c('"I could trick fate into giving us another chance. I would still have to ask you to take it."', "trickster", requires=("trickster",)),
      c('"My transformation has changed me. It has not made your opinion any cheaper."', "transformed", requires=("inhuman",)),
      c('"My duties and loyalties are changing. Name your price for staying anyway."', "limits", forbids=("trickster", "inhuman"))),
    n("trickster", "Konomi", '''"Then do not confuse a second chance with a corrected answer."
{n}She picks up a sheet of discarded correspondence and studies the impression left by its seal.{/n}
"If you reopen a door that circumstances shut, I may choose to walk through it. If you rewrite the woman who refused you, you have arranged a conversation with somebody else."
{n}A little amusement returns to her expression.{/n}
"You may, however, make an exception for whoever keeps losing my requests for a new roof. I would be delighted to discover that they had always been competent."''', c('"I will begin with the roof, and leave your opinions intact."', "choice", flags=("konomi.fate_terms",))),
    n("transformed", "Konomi", '''"Then tell me what is no longer possible, and I will stop arranging suppers around it. I dislike wasting a good menu."
{n}She looks toward the spare place beside her.{/n}
"I miss some of what you were. I shall say so now and then, sharply, because I am not a saint and I will not pretend to be one for your comfort."
{n}Her voice steadies.{/n}
"And I am still here. Do not mistake the complaint for a withdrawal. I withdraw formally or not at all."''', c('"Then complain. I would rather have the complaint than the silence."', "choice", flags=("konomi.transformed_terms",))),
    n("limits", "Konomi", '''"Then here is a test case."
{n}She takes a folded recommendation from her sleeve: the winter levy on the river villages, which you have refused twice.{/n}
"I still think you are wrong about this. I will argue it in council, loudly, and I will lean on every Mendevian noble who owes me a favour to get it. What I will not do is bring it to your bed." {n}She tears the sheet once, neatly, and drops the halves in the grate.{/n} "That copy was for tonight. The real one goes before the council tomorrow."
{n}Outside, a bell marks the hour. She ignores it.{/n}
"Refuse me there, and I shall still be at this door the next evening. That is my offer. Do we have a deal, Commander?"''', c('"We have a deal. Bring your barons."', "choice", flags=("konomi.equal_terms",))),
    n("choice", "Konomi", '''{n}For once she leaves the final question unspoken. Her writing case is closed, the hour has passed, and she is still waiting for your answer.{/n}''',
      c('"I want a life with you in it. Draft the terms."', "commit", flags=("konomi.committed",)),
      c('"I care for you, but I cannot promise a future together."', "part")),
    n("commit", "Konomi", '''"Then there will have to be somewhere for my papers."
{n}You laugh, and she allows herself to look relieved.{/n}
"I mean it. You will otherwise discover them wherever you intended to sit."
{n}The plans that follow are incomplete, practical, and occasionally ridiculous. She objects to one of yours so vigorously that you both stop to laugh again.{/n}''', c('[Begin making those plans.]', flags=("konomi.chosen_future",))),
    n("part", "Konomi", '''{n}She closes her eyes for a moment, then nods.{/n}
"A pity. I had drafted rather a good future for us." {n}Her fan closes with a click.{/n} "Still, a clean refusal is worth more than a signature you meant to break."
{n}She informs you that private conversations are suspended until further notice. The work that still connects you continues through the usual channels, and she makes sure it is not one sheet thinner.{/n}''', c('[Accept the separation.]', flags=("konomi.closed", "konomi.parted_honestly",))),
], requires=("konomi.return",), delay=24)

s("ordinary", "A place for the papers", 5, '"Have we found an evening without an emergency?"', [
    n("start", "Konomi", '''{n}Konomi has arrived with a small potted plant and a stack of papers. She places them at opposite ends of the room as though separating hostile delegations.{/n}
"The grower assures me this one survives neglect. I have decided to believe her."
{n}She notices you looking at the papers.{/n}
"Those can wait. I am capable of improvement."''',
      c('"You promised me honest disagreement. Tell me something I will argue with."', "honesty", requires=("konomi.wants_honesty",)),
      c('"You promised me an evening when I need not impress anybody."', "rest", requires=("konomi.wants_rest",)),
      c('"I would like to hear about something that went well for you."', "news")),
    n("honesty", "Konomi", '''"You are not nearly as good at concealing when you want praise as you imagine."
{n}She waits for your reply with obvious enjoyment.{/n}
"Neither am I. I managed a rather difficult conversation today without once explaining to the other person how difficult they were making it. I expect you to be impressed."
{n}The story takes longer because you interrupt to challenge her account. She objects, then admits that one of your objections is fair.{/n}''', c('[Give her the praise she has earned.]', "end")),
    n("rest", "Konomi", '''"Then we shall each be unremarkable for an hour. I can begin by admitting that I bought this plant because I liked its pot."
{n}She settles comfortably and lets the quiet last. When she eventually speaks, it is to ask whether you would mind moving the lamp, not to extract an account of your day.{/n}
{n}For a while neither of you makes the evening useful.{/n}''', c('[Stay with her in the quiet.]', "end")),
    n("news", "Konomi", '''{n}She tells you about a petition that finally reached somebody who could answer it. Her satisfaction is precise and unguarded.{/n}
"I know. You expected a triumph involving an embassy. This involved a repaired wall and two people who can stop sleeping beneath a leak. I am excessively pleased with myself."
{n}She looks toward the plant.{/n}
"We must hope success does not make me reckless about watering."''', c('[Enjoy her good news with her.]', "end")),
    n("end", "Konomi", '''{n}When the lamp burns low, the papers remain untouched. Konomi looks at them once, considers making an excuse, and leaves them where they are.{/n}
"Tomorrow," {n}she says.{/n}
{n}For tonight, she has somewhere she would rather be.{/n}''', c('[Keep the evening for each other.]', flags=("konomi.at_home",))),
], requires=("konomi.power", "konomi.committed"), delay=24)

s("farewell", "The letter she does not seal", 5, '"Before the final fighting, there is something I want to say."', [
    n("start", "Konomi", '''{n}Konomi has written you a letter and left it unsealed.{/n}
"I disliked the idea of somebody having to break it open if you could not read it. So I decided to give it to you now, while I can object to your interpretation."
{n}The letter is shorter than you expected. It asks for a day without official business, spent together in whatever manner you both find pleasant. Beneath that she has added a more emphatic request: no messengers.{/n}
"You may propose amendments," {n}she says.{/n} "The person sharing the day is not negotiable."''',
      c('"I would like that day. And the one after it."', "promise"),
      c('"Keep a copy. I intend to make you explain the handwriting."', "promise")),
    n("promise", "Konomi", '''{n}Her smile lasts until you are nearly at the door. Then she asks you to wait.{/n}
"Come back if you can. I do not want a beautiful promise that makes you careless. I want you."
{n}You stay a little longer. When you leave, the letter goes with you.{/n}''', c('[Carry her letter into what comes next.]', flags=("konomi.farewell_kept",))),
], requires=("konomi.ordinary",), delay=24)

s("parting", "A different answer", 3, '"We need to speak privately about our relationship."', [
    n("start", "Konomi", '''{n}Konomi puts down her pen.{/n}
"Then speak. I would rather hear the difficult part before I invent something worse to worry about."''',
      c('"I want to end the relationship."', "end"),
      c('"I have been neglecting you. Name an evening and I will keep it."', "stay")),
    n("end", "Konomi", '''{n}She hears you out without taking a single note, which is somehow worse.{/n}
"I shall miss you," {n}she says.{/n} "I shall also be angry about it, probably in writing. Neither will reach the council minutes. I do not let a private loss cost me a public one."
{n}She asks which belongings you would like returned. The small practical question is harder to answer than you expected.{/n}''', c('[End the relationship.]', flags=("konomi.closed", "konomi.parted_honestly",))),
    n("stay", "Konomi", '''"Then choose a time with me now. We are both very good at promising to discover a free evening later."
{n}She opens her appointment book and turns it so that you can read it together.{/n}''', c('[Make a plan and keep the relationship.]', abort=True)),
], requires=("konomi.lovers",), optional=True)


# The copyists' association and its hearing are authored private institutions,
# not a native quest or a statement of Mendevian law.
s("hearing", "The page they are allowed to read", 3, '"When will the complaint about our letter be heard?"', [
    n("start", "Konomi", '''{n}Konomi has wrapped your letter in a sheet of plain paper. The stolen copy is in a second wrapper; she has kept both pages from the adjudicators until you decide what they may read. Beside them lies the receipt for the copyist's payment.{/n}
"Tomorrow morning. Three members of the copyists' association have agreed to hear the complaint. They can refuse the buyer further work through their members. They cannot put him in prison, and I have not asked them to."
{n}She leaves the wrapped letter on her desk.{/n}
"He admits buying a copy. He says he believed it was a memorandum that he was entitled to circulate. The receipt does not say what he bought."
{n}Her finger rests on the wrapping.{/n}
"I want to show them the original. Only the three adjudicators, with no new copy made. But it is your hand on the page, and they will want you to swear to it. Come with me. I do not intend to argue this one alone."''',
      c('[Attend the hearing with her.]', "arrival"),
      c('"I cannot attend tomorrow. Ask them for another date."', abort=True)),
    n("arrival", "Narrator", '''{n}The next morning, you accompany Konomi to a workroom behind a stationer's shop. A woman with silver hair has cleared a table between two drying racks. She introduces herself as the registrar and indicates the two women seated beside her, both working copyists. A chair across from Konomi remains empty.{/n}
{n}"The buyer has sent a written answer," the registrar says. "He will accept our decision about access to our members' services. He will not attend. I thought you should know before we began."{/n}
{n}Konomi takes the chair facing the empty one. You sit beside her.{/n}''',
      c('[Ask what the buyer has submitted.]', "public", requires=("konomi.public",)),
      c('[Ask what the buyer has submitted.]', "discreet", forbids=("konomi.public",))),
    n("public", "Narrator", '''{n}The registrar unfolds the answer. Beneath it is the public acknowledgment Konomi sent after the leak.{/n}
{n}"He says you have made the relationship public yourselves."{/n}
"He bought the page before we answered him," {n}Konomi says.{/n} "And we did not publish the page."
{n}"I agree that these are different acts. I will record the dates." The registrar turns over the answer. "He also suggests that your complaint is part of a dispute over access to a household's couriers."{/n}
{n}Konomi's mouth tightens.{/n}
"The household may choose whose letters it carries. That does not give this man leave to buy mine from somebody entrusted with copying other work. Please record that distinction as well."
{n}The registrar writes it down. Konomi keeps watching the pen until it stops.{/n}''', c('[Let the registrar continue.]', "evidence")),
    n("discreet", "Narrator", '''{n}The registrar places the buyer's answer beside three almost identical notices of an inspection. Konomi points to the date on the second notice.{/n}
"That copy followed the same channel as our letter. He complained about its date to a person who had not sent him an invitation."
{n}"He calls that a practical joke at his expense," the registrar says.{/n}
"It was. He could have avoided it by keeping his hands out of my correspondence."
{n}One of the working copyists looks down to conceal a smile. The registrar does not.{/n}
{n}"It establishes the channel. It does not establish what he believed he was buying the first time."{/n}
"No," {n}Konomi says after a moment.{/n} "It does not. That is why I brought the original."''', c('[Listen to the proposed conditions.]', "evidence")),
    n("evidence", "Narrator", '''{n}The registrar lays a blank wrapper before you.{/n}
{n}"If you both agree, we will compare the original with the disputed copy here. We will make no transcript. Our decision will describe it as private correspondence, without quoting it. You take the original away today."{/n}
{n}She looks from Konomi to you.{/n}
{n}"All three of us will read it. I cannot promise that you will enjoy that, or that we can forget it afterward. If you prefer to conceal the personal passages, we can still consider the unauthorized copying. The buyer's claim about what he thought he bought will be harder to disprove."{/n}
{n}Konomi draws her chair back.{/n}
"A moment, please."
{n}The registrar directs you both to the little courtyard behind the shop. Konomi takes the wrapped letter with her.{/n}''', c('[Speak to Konomi outside.]', "courtyard")),
    n("courtyard", "Konomi", '''{n}A sheet of spoiled paper has blown against the courtyard drain. Konomi moves it aside with her shoe, then looks annoyed at herself for finding something to do.{/n}
"I want him refused work. He used somebody else's employment to reach something he could not have asked me for. If the association accepts his excuse, he can try another copyist."
{n}She turns the packet over in her hands.{/n}
"And I hate the idea of sitting beside you while three strangers read it. I keep wishing you had written a less convincing case for them."
{n}Her smile is brief.{/n}
"That is my recommendation. Give them the whole page. Tell me if yours is different."''',
      c('"Let them read it under those conditions. I want the buyer held responsible."', "whole", flags=("konomi.hearing_whole",)),
      c('"I want him held responsible too. I cannot bear giving more people those words. Cover the private passages."', "covered", flags=("konomi.hearing_covered",))),
    n("whole", "Konomi", '''{n}She nods and starts to fold the wrapper closed. Then she stops.{/n}
"You hold it. If your nerve goes in there, it will be your hand that takes it off the table, not mine."
{n}She hands you the packet. The top corner is soft from the number of times she has held it.{/n}
"I should be pleased. Instead I am thinking of one sentence I particularly wish the registrar would skip."
{n}You return to the workroom together.{/n}''', c('[Place the letter on the table.]', "acknowledge")),
    n("covered", "Konomi", '''{n}She looks toward the shop door.{/n}
"I think we will lose the stronger complaint."
{n}You wait. She unfolds the wrapper, checks how much of the letter would remain visible, and folds it again.{/n}
"You heard the same terms I did. I am not going to repeat them until you answer differently."
{n}Her voice has become more formal. She notices, but does not immediately manage to soften it.{/n}
"Come inside. We will ask them to use slips of paper. I do not want our letter covered in ink."''', c('[Return with her and keep the personal passages covered.]', "acknowledge")),
    n("acknowledge", "Narrator", '''{n}The registrar asks you to confirm that the letter is yours and that you did not authorize the sale. The question is brief. Konomi sits very still beside you.{/n}''',
      c('"I wrote it to Lady Konomi. It was private, and I gave nobody permission to sell it."', "repaired", requires=("konomi.almost_denied",), flags=("konomi.hearing_owned_letter",)),
      c('"I wrote it to Lady Konomi. It was private, and I gave nobody permission to sell it."', "compare", forbids=("konomi.almost_denied",), flags=("konomi.hearing_owned_letter",))),
    n("repaired", "Konomi", '''{n}Konomi turns toward you. For a moment you remember the answer you first proposed when the stolen page arrived: call it a fabrication.{/n}
{n}She does not thank you in front of the registrar. She moves her hand from the edge of the table and lets it rest, open, beside yours.{/n}''', c('[Stay beside her as the hearing proceeds.]', "compare")),
    n("compare", "Narrator", '''{n}The registrar asks one final question about the page before the adjudicators examine it.{/n}''',
      c('[Allow the complete comparison.]', "finding_whole", requires=("konomi.hearing_whole",)),
      c('[Change your mind before they read it. Ask to conceal the personal passages.]', "finding_covered", requires=("konomi.hearing_whole",), flags=("konomi.hearing_withdrew_permission",)),
      c('[Keep the personal passages concealed.]', "finding_covered", requires=("konomi.hearing_covered",))),
    n("finding_whole", "Narrator", '''{n}The three women read in silence. Konomi studies a stain on the table until the registrar looks up. Nobody makes a joke. Somehow the ordinary scrape of a chair is worse than the interruption you had prepared yourself to resent.{/n}
{n}The registrar returns the original before opening the buyer's answer again. She points out the claim that the purchased copy concerned an official recommendation. One copyist shakes her head. The other asks to check the matching first and last lines once more on the disputed copy.{/n}
{n}Their decision is unanimous. The buyer will be refused work through the association for knowingly purchasing private correspondence without permission. The copyist who supplied it must refund the copying fee and will lose access to the association's referrals pending a separate review of his conduct.{/n}
{n}"We cannot make every shop in Drezen refuse him," the registrar tells Konomi. "We can tell our members exactly what we have found. No quotations."{/n}
"Send me that notice before it is circulated," {n}Konomi says.{/n} "I want to check the description."
{n}She takes your letter. It looks unchanged.{/n}''', c('[Leave the workroom together.]', flags=("konomi.hearing_buyer_barred", "konomi.hearing_finished"))),
    n("finding_covered", "Narrator", '''{n}Konomi keeps both versions facing her while she fits loose slips over the private passages, securing them with the corners of the wrappers. You check the visible text together. Only then does she pass the masked pages across for comparison.{/n}
{n}The adjudicators confer. One copyist argues that the buyer's account is too convenient. The other replies that suspicion is what they began with. At last the registrar returns the packet.{/n}
{n}"The copying was unauthorized. We require the copying fee to be returned, and we will suspend the copyist's referrals while we review his conduct. We do not have sufficient evidence to find that the buyer knowingly purchased private correspondence."{/n}
{n}Konomi objects. She lays out the dates, the receipt and the changing explanations once more. The registrar hears her to the end, then declines to change the decision. The buyer will still be able to commission work.{/n}
{n}Konomi gathers her papers carefully. Outside, she pulls the loose slips away from your letter one by one.{/n}
"I would still have shown them," {n}she says.{/n}
{n}She folds the letter and puts it away.{/n}
"I am going home. Walk with me, if you can."''', c('[Walk back with her.]', flags=("konomi.hearing_buyer_unbarred", "konomi.hearing_finished"))),
], requires=("konomi.scandal_answered",), forbids=("konomi.farewell", "konomi.hearing_finished"), delay=48, optional=True)

s("hearing_after", "What came home with the letter", 3, '"How have you been since the hearing?"', [
    n("start", "Konomi", '''{n}Konomi lets you in herself. On the table are the association's written decision and your letter, now in its old wrapper.{/n}
"I have read their wording. They kept our names in the finding and our private sentences out of it."
{n}She leaves the decision on the table.{/n}''',
      c('"Was the decision worth the price?"', "whole", requires=("konomi.hearing_buyer_barred",)),
      c('"We still disagree about the letter."', "covered", requires=("konomi.hearing_buyer_unbarred",))),
    n("whole", "Konomi", '''"Yes. I do not want to pretend it was worthless because I disliked the price."
{n}She takes the original from its wrapper, glances at the first line, and puts it back.{/n}
"I meant to read this last night. Then I wondered what the woman on the registrar's left had thought of it. I was angry enough to put it away."
{n}She pulls out the chair beside hers for you.{/n}
"I wanted the finding. I would make the same choice again. I also want to read a letter from you without having that woman at my elbow. Apparently that takes longer."''',
      c('"It cost me too. I would pay it again."', "together"),
      c('"Keep that one. I would like to write you something new."', "new_letter", flags=("konomi.hearing_new_letter",))),
    n("covered", "Konomi", '''"We do. I keep composing a better argument for the registrar. Every version requires the part of the page we did not show her."
{n}She rubs at an ink mark on her finger, then stops.{/n}
"I was angry on the walk back. You knew that. I am still angry, and I sent for you anyway, which should tell you how little the one has to do with the other."
{n}She gestures toward the chair.{/n}
"There is your invitation. I am still disappointed. Sit down."''',
      c('"I understood the cost. I would still keep those passages between us."', "still_disagree"),
      c('"I may have chosen wrong. I will not argue it again tonight."', "uncertain")),
    n("still_disagree", "Konomi", '''"I know."
{n}For a moment neither of you reaches for the safe subject waiting in the papers.{/n}
"You weighed it and came down on the other side. I have done the same to better people than you and called it statecraft. I can hardly call it treachery when you do it to me."
{n}She draws the decision toward her and folds it.{/n}
"That sounded much more gracious than I feel. You may appreciate the effort."''', c('"I do. I also appreciate being invited."', "trust")),
    n("uncertain", "Konomi", '''"Then do not reopen it tonight. If you change your mind, tell me in daylight, over a desk, where I can hold you to it. Nothing said after supper counts in my ledger."
{n}She folds the finding and lays it aside.{/n}
"I am capable of leaving an argument unfinished. I would prefer not to demonstrate by leaving you standing in the doorway."''', c('[Take the chair beside her.]', "trust")),
    n("together", "Konomi", '''{n}She looks relieved before she can arrange a more composed expression.{/n}
"Good. I have been telling myself that I was the only one making such a business of it. An efficient way to become unbearable."
{n}She puts the letter back in its drawer. This time she does not hurry.{/n}''', c('[Stay beside her.]', "trust")),
    n("new_letter", "Konomi", '''"Here?"
{n}Her eyes go to the inkpot, then back to you.{/n}
"I would be very poor at pretending not to watch. Write it later. I want the pleasure of finding it without having supervised its composition."
{n}She puts the old letter in the drawer, leaving room above it.{/n}
"And do not make it a defense of the first one. Tell me something you wanted to say before the hearing got into everything."''', c('[Promise to write later.]', "trust")),
    n("trust", "Konomi", '''{n}A runner knocks at the outer door. Konomi calls that she will attend to the packet later. She waits until the footsteps have gone, places the finding beneath a book, and turns back to you.{/n}''',
      c('"At least this evening is ours."', "repaired", requires=("konomi.almost_denied",)),
      c('"At least this evening is ours."', "evening", forbids=("konomi.almost_denied",))),
    n("repaired", "Konomi", '''"When the registrar asked whose letter it was, you answered before I could."
{n}She looks directly at you.{/n}
"I had been waiting for that question. I knew what you said when we first found out about the copy. I knew you had apologized. I was still waiting."
{n}Her hand closes over yours briefly, then releases it.{/n}
"I believed you this time. Do not squander it. I extend credit once."''', c('"I am glad I could give you a reason to."', "evening", flags=("konomi.hearing_trust_repaired",))),
    n("evening", "Konomi", '''{n}She takes a small parcel from a cupboard and sets it between you. Inside are two apple pastries, one visibly larger than the other.{/n}
"I bought these this morning. I then spent an unreasonable amount of time deciding whether to offer you the larger one as a peace offering."
{n}She takes the larger pastry.{/n}
"I decided you would see through it."''',
      c('"I would have accepted it very convincingly."', "warm"),
      c('[Take the smaller pastry and move your chair closer.]', "warm", forbids=("inhuman",))),
    n("warm", "Konomi", '''{n}She breaks off a piece of her pastry and sets it on your plate, looking as though she expects to be challenged.{/n}
"There. A concession. Remember this moment."
{n}Her knee rests against yours beneath the table. The finding stays beneath the book; when her glance returns to it, she lets herself look, then returns her attention to you.{/n}''',
      c('[Kiss her, then stay for the evening.]', flags=("konomi.hearing_evening_kept", "konomi.hearing_kissed"), forbids=("inhuman",)),
      c('[Stay, and let her finish the pastry before anything else.]', flags=("konomi.hearing_evening_kept",))),
], requires=("konomi.hearing_finished",), forbids=("konomi.farewell", "inhuman", "konomi.hearing_evening_kept"), delay=24, optional=True)


s("new_letter", "A contest of no importance", 3, '"I brought the letter I promised you."', [
    n("start", "Konomi", '''{n}Konomi looks at the folded sheet in your hand, then clears a space for it beside her appointment book.{/n}
"You remembered."
{n}She reaches for it, stops, and gives you a suspicious look.{/n}
"You have the expression of somebody who expects an answer before I have finished reading."''',
      c('[Give her a frankly romantic invitation.]', "frank", flags=("konomi.new_letter_frank",)),
      c('[Give her a challenge to an afternoon of useless competition.]', "challenge", flags=("konomi.new_letter_challenge",)),
      c('"I would rather give you this when we have more time."', abort=True)),
    n("frank", "Narrator", '''{n}She unfolds the sheet.{/n}
{n}"When you look up and catch me watching you, I sometimes forget what I meant to say. I have remembered it now: I would like to kiss you. I would also like to take you somewhere that gives us a reason to be late coming home. There is a woman in the market offering prizes for throwing rings. Meet me there this afternoon, if you would enjoy either invitation."{/n}
{n}Konomi reads the last line twice.{/n}
"You have put the more interesting proposal first."
{n}She folds the letter carefully and slips it into her writing case.{/n}
"I have decided to accept in reverse order."''', c('"Then I will meet you in the market."', "market")),
    n("challenge", "Narrator", '''{n}She unfolds the sheet.{/n}
{n}"I have found a contest with no worthy cause attached to it. The prizes are useless and the rules fit on a small board. I think you would dislike losing. I would enjoy finding out. Meet me at the ring-throwing stall in the market this afternoon. I will try to be a gracious winner. I promise nothing if you win."{/n}
{n}Konomi's gaze rises from the page.{/n}
"You wrote this knowing I would have to answer it."
{n}She opens her appointment book, moves one note to another page, and closes it again.{/n}
"This afternoon. I will make a point of enjoying the prize."''', c('[Agree to meet her at the stall.]', "market")),
    n("market", "Narrator", '''{n}Later that afternoon, Konomi joins you beside a cloth merchant's awning. The neighboring stall consists of a plank, three wooden pegs and a row of small prizes. Its owner, a broad-shouldered woman with gray in her hair, demonstrates by dropping a ring neatly over the nearest peg.{/n}
{n}"Behind the line to throw. Three rings each. Near peg gets the ribbon, middle gets the bell, far gets the painted bird. No leaning over the line."{/n}
{n}Konomi examines the prizes. The bird is a garish little rooster. She turns it around to inspect its unevenly painted back.{/n}
"How splendidly unnecessary."
{n}She pays for two sets of rings and hands one to you.{/n}
"You invited me. I have purchased the means of defeating you. We should be ready."''', c('[Join her behind the throwing line.]', "first_throw")),
    n("first_throw", "Konomi", '''{n}Her first ring passes the far peg and skitters beneath the stall. The owner retrieves it with a hooked stick.{/n}
"That was information," {n}Konomi says.{/n}
{n}Her second falls short. She studies the third for a moment, then looks at the owner's hand on the hooked stick.{/n}
"How many times a day do you make that first throw?"
{n}"Enough to stop thinking about it, my lady."{/n}
{n}Konomi turns the ring in her fingers.{/n}
"An irritating answer. It may even be the right one."''',
      c('"Try the middle peg. Give your wrist less work to do."', "advice", flags=("konomi.rings_advised",)),
      c('"I want to see what you do with the last one."', "watch", flags=("konomi.rings_watched",))),
    n("advice", "Konomi", '''"You have discovered my limits already?"
{n}She looks at the painted rooster, then at the middle peg. This time the ring lands flat enough to catch. It rattles down around the peg.{/n}
{n}The owner places a small brass bell on the plank.{/n}
"I have discovered one of them myself," {n}Konomi says.{/n} "I dislike how pleased you look."
{n}She picks up the bell and rings it beside your ear, lightly enough to make the offense deliberate.{/n}''', c('"My turn, then."', "your_turn", flags=("konomi.rings_bell",))),
    n("watch", "Konomi", '''{n}She considers the far peg, then turns her attention to the point where her last ring struck the plank. Her third throw reaches the rooster's peg, catches its top and spins away.{/n}
{n}She makes a small, furious sound. The owner retrieves the ring without offering advice.{/n}
"Almost," {n}Konomi says.{/n} "A word of very little practical assistance."
{n}She steps back to give you the line.{/n}
"Go on. Be impressive. I have prepared several objections."''', c('[Take your place.]', "your_turn", flags=("konomi.rings_empty_handed",))),
    n("your_turn", "Narrator", '''{n}You have three rings. Konomi watches with far more attention than the prizes deserve.{/n}''',
      c('[Aim all three at the distant rooster.]', "rooster", flags=("konomi.rings_commander_rooster",)),
      c('[Aim for the nearest peg and its ribbon.]', "ribbon", flags=("konomi.rings_commander_ribbon",))),
    n("rooster", "Narrator", '''{n}The first ring goes wide. The second clips the peg. On the third throw, the ring settles around it and stays.{/n}
{n}Konomi exhales through her nose. The owner hands you the rooster.{/n}
"It is even worse at this distance," {n}Konomi says.{/n} "You must display it somewhere your visitors cannot avoid it."
{n}She takes it from you long enough to inspect the brushwork again, then returns it.{/n}
"I congratulate you. There, that is done."''', c('[Leave the stall with her.]', "walk")),
    n("ribbon", "Narrator", '''{n}The first ring bounces away. The second drops over the nearest peg. You miss with the third, but the owner has already taken a length of blue ribbon from its hook.{/n}
{n}Konomi holds out her hand for it. You let her wind it once around your wrist and tie a conspicuously neat bow.{/n}
"There. A distinction awarded for a modest, achievable ambition."
{n}Her fingers linger beneath the knot.{/n}
"I may have chosen badly."''', c('[Leave the stall with her.]', "walk")),
    n("walk", "Konomi", '''{n}The market thins as you leave the stalls behind. Konomi slows where an awning casts a long patch of shade across the street.{/n}
"I spent the first half of that thinking I ought to be better at it. Then I became annoyed that I was thinking about myself when I could have been watching you."
{n}She looks at you sidelong.{/n}
"You are very easy to watch when you have decided that something ridiculous matters."''',
      c('"I was hoping you would enjoy being out with me."', "pleasure"),
      c('"I meant what I wrote in the first part of the letter."', "frank_reply", requires=("konomi.new_letter_frank",)),
      c('"I promised nothing if you won. Fortunately, I am spared that test."', "challenge_reply", requires=("konomi.new_letter_challenge", "konomi.rings_commander_rooster")),
      c('"Your bell outranks my ribbon. How gracious a winner are you?"', "challenge_winner", requires=("konomi.new_letter_challenge", "konomi.rings_commander_ribbon", "konomi.rings_bell")),
      c('"We have made an excellent case for leaving that rooster where it is."', "challenge_draw", requires=("konomi.new_letter_challenge", "konomi.rings_commander_ribbon", "konomi.rings_empty_handed"))),
    n("pleasure", "Konomi", '''"I did. I am."
{n}She looks back toward the stall. The owner is showing another customer the easy throw, landing her ring as smoothly as before.{/n}
"Do not pretend I was secretly very good at it. I wanted that rooster. I did not get it. I am staying out with you anyway, which should tell you which prize I value."
{n}She takes your arm.{/n}
"There is another street before we have to decide where we are going."''', c('[Walk on with her.]', "keepsake")),
    n("frank_reply", "Konomi", '''{n}She stops beneath the edge of the awning. For once, you see her consider an answer and discard it without speaking.{/n}
"Then stop making me wait for it."
{n}She draws you toward her by the front of your sleeve. The kiss is warm and unhurried; when somebody passes behind you, she shifts nearer and lets them pass.{/n}
"You can forget your next sentence," {n}she says.{/n} "I am quite content with that one."''', c('[Stay close as you continue walking.]', "keepsake", flags=("konomi.new_letter_kissed",))),
    n("challenge_reply", "Konomi", '''"You are not spared the consequences of being insufferable about it."
{n}She moves close enough that the warning loses some of its force.{/n}
"I may choose our next contest. I may spend an unreasonable amount of time practicing. You will be obliged to look surprised."
{n}Her hand finds your arm.{/n}
"But that can wait. I was promised an afternoon, and I have no intention of letting three wooden pegs consume all of it."''', c('[Continue walking with her.]', "keepsake")),
    n("challenge_winner", "Konomi", '''{n}She lifts the bell and gives it one small, triumphant shake.{/n}
"I shall be unbearable for a few minutes. You may remind yourself that you invited this."
{n}She hooks one finger beneath the ribbon on your wrist.{/n}
"Then I shall recover my manners. I would like to be invited again."''', c('"I can endure a few minutes."', "keepsake")),
    n("challenge_draw", "Konomi", '''"I would have made an excellent case for keeping it, had I won it. You should know that about me."
{n}She looks toward the stall once more, then gives a short laugh.{/n}
"Perhaps we have both been spared. Come away before I decide I require more evidence."''', c('[Leave the rooster to another customer.]', "keepsake")),
    n("keepsake", "Narrator", '''{n}You pause at the next crossing. Konomi glances at the prize you brought from the stall.{/n}''',
      c('[Give her the painted rooster.]', "give_rooster", requires=("konomi.rings_commander_rooster",)),
      c('[Keep the rooster as a reminder of the afternoon.]', "keep_rooster", requires=("konomi.rings_commander_rooster",)),
      c('[Ask whether she would like to wear the ribbon.]', "give_ribbon", requires=("konomi.rings_commander_ribbon",)),
      c('[Keep the ribbon tied around your wrist.]', "keep_ribbon", requires=("konomi.rings_commander_ribbon",))),
    n("give_rooster", "Konomi", '''{n}She accepts the rooster with an expression of elaborate resignation.{/n}
"You are giving me evidence of my defeat. I shall keep it where you have to look at it when you visit."
{n}She adjusts her grip so that its painted crest will not rub against her sleeve.{/n}
"Somewhere prominent."''', c('[Spend the rest of the afternoon together.]', flags=("konomi.new_letter_outing", "konomi.keeps_rooster"))),
    n("keep_rooster", "Konomi", '''"Good. I expect to find it in a position of honor. If it disappears behind a book, I will know you have begun to regret your victory."
{n}She turns down the quieter street, waiting for you at the corner.{/n}
"Come along. You can decide where to put it later."''', c('[Spend the rest of the afternoon together.]', flags=("konomi.new_letter_outing", "konomi.commander_keeps_rooster"))),
    n("give_ribbon", "Konomi", '''{n}She considers the bow on your wrist, then holds out her own.{/n}
"You may attempt to tie it as neatly."
{n}Your knot does not quite match hers. She examines it, makes no correction, and lowers her hand.{/n}
"It will do."
{n}She keeps her fingers threaded through yours as you leave the crossing.{/n}''', c('[Spend the rest of the afternoon together.]', flags=("konomi.new_letter_outing", "konomi.keeps_ribbon"))),
    n("keep_ribbon", "Konomi", '''{n}She smooths one end of the bow against your wrist.{/n}
"Leave it there for a while. I would like to know I have spoiled the gravity of your next important gesture."
{n}She watches your hand as you offer it, then takes it with a smile.{/n}''', c('[Spend the rest of the afternoon together.]', flags=("konomi.new_letter_outing", "konomi.commander_keeps_ribbon"))),
], requires=("konomi.hearing_new_letter", "konomi.hearing_evening_kept"), forbids=("konomi.farewell", "inhuman", "konomi.new_letter_outing"), delay=24, optional=True)


# An authored first step after the native dismissal, not restored contact.
# The completed officer state is separate from the earlier selected-answer record.
SCENES.append(scene("konomi.fate_post", "No longer at this address", "Konomi", 3, "", [
    n("start", "Narrator", '''{n}The clerk who brings you the record of Konomi's dismissal has ruled a line through her old office address. Beneath it, he has written that further correspondence requires a new destination.{/n}
{n}You remember the words you used when you dismissed her and the Royal Council. Apparently they make a poor postal instruction.{/n}
{n}As you study the sheet, its ruled line lengthens. It runs off the edge of the paper, across the table and up the wall, where it ends in a small rectangle. A door, drawn in ink. Someone on the other side turns a key.{/n}
{n}A narrow slot opens in the drawing. Through it protrudes a card: PERSON NO LONGER AT THIS ADDRESS.{/n}''',
      c('[Take the card and examine the impossible door.]', "door"),
      c('[Set the record aside. Leave the matter for now.]', abort=True)),
    n("door", "Narrator", '''{n}The card is addressed to Lady Konomi, diplomatic officer. You cover the final two words with your thumb. The slot opens again.{/n}
{n}Another card emerges: INSUFFICIENT OFFICIAL BUSINESS.{/n}
{n}When you uncover the title, the first card returns. You repeat the experiment. The unseen clerk repeats the objection. Somewhere beyond the painted door, a stamp strikes a desk with mounting irritation.{/n}
{n}Your power has found a very small piece of the world's certainty: a woman who no longer holds an office cannot be reached through it. It appears quite prepared to spend the evening agreeing with itself.{/n}''',
      c('"You have confused a person with a vacancy."', "distinction"),
      c('[Draw a second slot beneath the first and label it PRIVATE LETTERS.]', "second_slot")),
    n("distinction", "Narrator", '''{n}The stamp pauses.{/n}
{n}A form slides through the slot. In the space for the recipient, someone has written LADY KONOMI, FORMER OFFICEHOLDER. You cross out everything except her name. In the space for the purpose of the letter, you write PRIVATE.{/n}
{n}The form returns with an objection to the new category. You turn it over and write that the objection, too, is private correspondence and must therefore be delivered before it can be considered.{/n}
{n}For a while nothing happens. Then a small brass label appears beneath the slot: PERSONAL POST. The stamp has become remarkably quiet.{/n}''', c('[Prepare the letter.]', "letter", flags=("konomi.post_argument",))),
    n("second_slot", "Narrator", '''{n}Your pen catches on the wall as though it has struck a latch. The lower slot opens. The upper one closes with a snap.{/n}
{n}A hand in an ink-stained glove reaches through the new opening and points reproachfully at your label. You add BY PERSONAL INVITATION beneath it. The finger taps the empty space where the sender's name ought to be.{/n}
{n}You sign your own name. The hand withdraws. A moment later it returns to leave a single blank envelope on the table.{/n}''', c('[Prepare the letter.]', "letter", flags=("konomi.post_new_slot",))),
    n("letter", "Narrator", '''{n}You lay out a clean sheet and an envelope. The old dismissal remains on the table. The line through Konomi's office address has not moved. Whatever goes through this slot will not give her back that office or make her agree with the decision that took it away.{/n}
{n}There is room on the new sheet to say what you actually want from her.{/n}''',
      c('[Ask to meet the woman you were becoming close to.]', "lover", requires=("konomi.lovers",)),
      c('[Ask whether she would consider a conversation outside official business.]', "first", forbids=("konomi.lovers",))),
    n("lover", "Narrator", '''{n}"Konomi, I dismissed your advice and the office through which you gave it. A letter will not buy that back; I know your rates. I would like to see you anyway. I miss your company, and I have earned whatever you want to say to me without a council table between us. Name a place and a time, or burn this. I will not send an order after it."{/n}
{n}You read it again before folding it.{/n}''', c('[Sign the invitation.]', "send")),
    n("first", "Narrator", '''{n}"Lady Konomi, I am writing privately. I stand by my decision about the Royal Council, and I will not dress up a plea to reverse it as an invitation. I would like to hear what you intend for yourself now. If a conversation outside official business interests you, name a place and a time. I am asking for your company, not your office. You owe me nothing, and you have never been shy of saying so."{/n}
{n}You leave the invitation at that.{/n}''', c('[Sign the invitation.]', "send")),
    n("send", "Narrator", '''{n}The envelope fits the lower edge of the slot. As you push it through, the word DELIVERY appears on its flap. You hold it still long enough to add one word: OFFER.{/n}
{n}The stamp sounds once beyond the wall. A receipt drops onto the table, acknowledging a single attempt to place the invitation in Lady Konomi's hands. It promises neither an answer nor another visit from the impossible post office.{/n}
{n}The ink door folds into the receipt. The ruled line contracts until it ends where the clerk left it, through the old office address.{/n}
{n}You keep the receipt beside the dismissal.{/n}''', c('[Keep the receipt and wait for an answer.]', flags=("konomi.post_sent",))),
], Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
    requires=("trickster", "konomi.dismissed", "konomi.office_completed"),
    forbids=("konomi.present", "inhuman", "konomi.farewell"), optional=True))


SCENES.append(scene("konomi.fate_reply", "An answer in her own hand", "Konomi", 3, "", [
    n("start", "Narrator", '''{n}Konomi's answer arrives with an ordinary carrier. The woman waits while you check the name on the envelope, then agrees on an hour to return for your reply. She leaves you to read it. She shows no sign of being able to fit through a slot in a painted door.{/n}
{n}Inside, Konomi has enclosed your invitation. A small note is pinned to it: "Your letter arrived beneath my cup. It came with a form requesting my signature, with enough boxes to suggest that you had established another ministry. I signed for the paper. The answer below is mine."{/n}
{n}"I intended to leave for Nerosyan at once. The two carriers arranging the journey disagreed about their terms, and I have accepted a fee to help settle the matter. My departure will wait a little. I would rather reach the capital with a workable arrangement than send two more people there to quarrel."{/n}
{n}The second sheet gives an address in Drezen, in a house with a covered courtyard let to travelers. Beneath it is a proposed afternoon and a correction to the directions: the entrance is beside the cooper's yard, not through it.{/n}''',
      c('[Read the rest of her answer.]', "lover", requires=("konomi.lovers",)),
      c('[Read the rest of her answer.]', "first", forbids=("konomi.lovers",))),
    n("lover", "Narrator", '''{n}"I read your letter twice. Once looking for the request you had concealed in it, and once because I wanted to believe there was none. I will meet you. I have missed you, which has made being angry with you considerably less convenient."{/n}
{n}"Come to the address above at a time we agree upon. I have the use of the courtyard for the afternoon. You need not bring an explanation of every decision you have ever made. You will have to hear what I have to say about the one that brought us here."{/n}''', c('[Consider your answer.]', "answer")),
    n("first", "Narrator", '''{n}"Your invitation was unexpected. So was the means of delivery. I would prefer not to discover whether your next piece of correspondence can pursue me into the bath."{/n}
{n}"I will meet you. You have asked what I intend for myself, and I find that I would like to tell you. I am also curious what you say when there is no audience to say it for."{/n}
{n}"The address above is where I am staying. Send your answer with the carrier who brought this. She knows the actual door."{/n}''', c('[Consider your answer.]', "answer")),
    n("answer", "Narrator", '''{n}The carrier returns at the hour she gave you. She has a little book open to a page of collection times and is already calculating where your answer will fit among them.{/n}
{n}Konomi has left room to agree on another afternoon if the proposed one is impossible.{/n}''',
      c('[Confirm an afternoon for the meeting.]', "accepted"),
      c('[Write that the war will not spare you this week, and ask her to hold the courtyard.]', abort=True),
      c('[Write that you have reconsidered and will not pursue a personal relationship.]', "declined")),
    n("accepted", "Narrator", '''{n}You send back the time you can keep. The carrier repeats it aloud before closing her book.{/n}
{n}When she leaves, Konomi's directions remain on your desk. You read the correction about the cooper's yard once more. Beneath it she has added, in smaller writing: "If you arrive smelling of barrel pitch, I shall know you ignored me."{/n}''', c('[Keep the appointment.]', flags=("konomi.private_appointment",))),
    n("declined", "Narrator", '''{n}You write a short answer. You thank her for offering the conversation and tell her not to reserve the courtyard for you.{/n}
{n}The carrier takes the sealed page. Your receipt from the impossible post office remains where you left it.{/n}''', c('[Let the personal invitation end here.]', flags=("konomi.closed", "konomi.private_declined"))),
], Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
    requires=("konomi.dismissed", "konomi.office_completed", "konomi.post_sent"),
    forbids=("konomi.present", "inhuman", "konomi.farewell"), delay=48, optional=True))

SCENES.append(scene("konomi.private_meeting", "The courtyard she chose", "Konomi", 3, "", [
    n("start", "Narrator", '''{n}The entrance beside the cooper's yard leads through a narrow passage to a covered courtyard. A woman carrying folded linen checks your name and directs you to the far end, where Konomi is fastening a shutter against a persistent rattle.{/n}
{n}She finishes before turning toward you. There are two chairs beneath the roof, with enough space between them that neither looks like an afterthought.{/n}
"You found the door. That is a promising beginning."
{n}She indicates the chair facing hers. You sit. Beyond the passage, somebody rolls a barrel over uneven stones; the noise passes and leaves the courtyard quiet.{/n}''',
      c('"Thank you for agreeing to see me."', "lover", requires=("konomi.lovers",)),
      c('"Thank you for agreeing to see me."', "first", forbids=("konomi.lovers",)),
      c('[Explain that you cannot stay and ask to arrange another afternoon.]', abort=True)),
    n("lover", "Konomi", '''"I nearly did not."
{n}Her hand rests on the empty chair arm beside her. You remember occasions when she would have reached across the space without thinking about it.{/n}
"I kept remembering what you said in front of the others. Then I remembered that you had asked me to spend an evening with you, once, and had seemed quite pleased that I came."
{n}She looks at you steadily.{/n}
"I have been trying to decide which person I would find here. It would help if you did not begin by telling me they are entirely different people."''',
      c('"They are both me. I wanted your company, and I was angry enough to drive you away."', "cost"),
      c('"I made a political decision, and I announced it in a voice meant to humiliate you."', "cost")),
    n("first", "Konomi", '''"I wanted to know what you would say when I could simply leave if it displeased me."
{n}She lets that rest between you for a moment, then gives a small, reluctant smile.{/n}
"That is an ungracious answer to an invitation. It is also the true one. I have had rather enough of composing a more useful version of what I think."
{n}She moves her chair slightly so that she can see the passage without turning her head.{/n}
"You asked what I intend for myself. Before I answer, you will hear what your decision cost me. I keep accounts."''', c('[Listen.]', "cost")),
    n("cost", "Konomi", '''"The morning after the dismissal, a woman brought me a request to introduce her to a grain factor. She had come a long way. I explained that I no longer held the office she had expected to find."
{n}Konomi rubs the edge of the chair arm with her thumb.{/n}
"She asked whether I had forgotten the factor's name. It was an excellent question."
{n}Her smile this time has more life in it.{/n}
"I wrote the introduction. I made it quite clear whose name stood behind it. Then I spent the rest of the morning deciding which of my correspondents would still want to hear from me without a title on the outside."
{n}She glances toward the house.{/n}
"I took these rooms while I settle the carriers' agreement. Nerosyan is still where I intend to go. I can pay for the delay. I would prefer you not to make my ability to do so the subject of a generous offer."''',
      c('"I stand by ending the role of the Council. I regret the way I spoke to you."', "stand_by", flags=("konomi.private_stands_by",)),
      c('"I let my anger at the Council decide how I treated your arguments. That was a mistake."', "mistake", flags=("konomi.private_admits_mistake",))),
    n("stand_by", "Konomi", '''"I thought you might."
{n}She folds her hands, then unfolds them again, plainly irritated by the gesture.{/n}
"You found their demands intolerable. I thought you underestimated what it meant for Mendev to place so much of its future in your hands. I still think that."
{n}She waits before continuing.{/n}
"An apology for the insult would be welcome. I will not pretend it settles the other matter."''',
      c('"Then accept it for what it is. I should not have spoken to you that way."', "apology"),
      c('"I am not asking you to stop arguing for Mendev. I am asking whether we can know one another despite this."', "despite")),
    n("mistake", "Konomi", '''{n}She begins to answer quickly, then stops herself.{/n}
"I have rehearsed a very satisfying reply to that admission. It is considerably less attractive now that I have the chance to say it."
{n}She leans back.{/n}
"Accepted. I shall collect on it at our next argument. You listen beautifully when you want something from a person, Commander; I have watched you do it to Mendevian barons. Do it when somebody brings you something inconvenient, and I will call us square."''', c('"Collect, then."', "plans")),
    n("apology", "Konomi", '''"I accept it."
{n}She lets the answer stand without adding a correction. Only after a moment does she continue.{/n}
"I was afraid I would be so pleased to hear it that I would agree to things I had not considered. I have brought a formidable collection of objections to prevent that."
{n}A little of her familiar amusement returns.{/n}
"You may be relieved to learn that none of them concerns the chair you are sitting in."''', c('[Ask what she intends to do next.]', "plans")),
    n("despite", "Konomi", '''"Perhaps. Understand that I intend to be troublesome in every way you have already found inconvenient, and a few new ones."
{n}She looks toward the passage, where the woman with the linen has stopped to speak to a tenant. When she looks back, her voice is quieter.{/n}
"I did not invite you here because I had become indifferent to the argument. I invited you because I wanted something besides it."''', c('"Tell me what that is."', "plans")),
    n("plans", "Konomi", '''"I have been asked to look over a proposed partnership between two carriers. One has wagons and no reliable introduction to the people she wants to serve. The other has introductions and a talent for describing borrowed wagons as though they were already hers."
{n}Konomi's expression sharpens with interest.{/n}
"They each believe the other is the one who needs assistance. I expect to earn my fee."
{n}She gives you a searching look.{/n}
"It is not an embassy. I know that. I am not going to explain it to you as a secret promotion. It is work I can choose while I decide what comes next."
{n}A breath, then:{/n}
"I enjoy discovering what somebody actually wants before they have decided how to ask for it. I would miss that if I spent all my time writing dignified accounts of how badly I had been treated."''',
      c('"Which of the two has interested you more?"', "carriers"),
      c('"And have you discovered what I actually want?"', "want")),
    n("carriers", "Konomi", '''"The one with the wagons. She knew exactly what they cost her and became very vague when I asked why she wanted this particular partner."
{n}Konomi smiles.{/n}
"I suspect an old obligation. I have asked for another meeting. If I am wrong, I will learn something else."
{n}She catches your attention resting on her face rather than the account.{/n}
"What?"''',
      c('"I like hearing you enjoy your work."', "want"),
      c('"You look pleased. It suits you."', "want")),
    n("want", "Konomi", '''{n}She considers you without the papers, the audience or the office that once gave the conversation its shape.{/n}
"You have been very attentive, Commander. People are attentive when they want something. What is it?"
{n}The wind catches the shutter again. This time she ignores it.{/n}''',
      c('"I want to begin seeing you privately, with the intention of becoming more than acquaintances."', "interest", forbids=("konomi.lovers",)),
      c('"I want you back. I know one afternoon will not buy that."', "return", requires=("konomi.lovers",)),
      c('"Another conversation first. I want to see the rest of your terms before I sign anything."', "slow")),
    n("interest", "Konomi", '''{n}She looks down for a moment. When she looks up, her expression is more openly curious.{/n}
"Yes. I would like to discover whether we are as interesting to one another without the help of an audience."
{n}She draws her chair a little closer and does not pretend the wind moved it.{/n}
"You may invite me again. Somewhere I have not hired for the express purpose of disagreeing with you."''', c('[Ask her to choose an evening with you.]', "arrange", flags=("konomi.private_interest", "konomi.attracted"))),
    n("return", "Konomi", '''"I have missed you. I was determined to say something more composed than that."
{n}Her mouth tightens into a smile that is not entirely happy.{/n}
"I can imagine being glad to see you at my door again. I can also imagine remembering the dismissal at a moment when you had hoped I would be thinking about something else."
{n}She reaches across the space between the chairs and rests her hand over yours.{/n}
"I would like another afternoon anyway."''', c('[Stay close and make another plan with her.]', "arrange", flags=("konomi.private_interest",))),
    n("slow", "Konomi", '''"So would I."
{n}She seems relieved by the smallness of the request, though she does not pretend it is all she has considered.{/n}
"The woman who brought the linen has heard two of my explanations for why I reserved the courtyard. She believed neither of them. I would like to have a better answer for myself before I give her a third."
{n}She moves her chair enough to quiet its uneven leg.{/n}
"Another conversation, then."''', c('[Arrange to speak again.]', "arrange", flags=("konomi.private_unhurried",))),
    n("arrange", "Konomi", '''{n}You agree to send future notes through the carrier who brought her reply. Konomi gives you the times at which the woman calls, then opens the gate into the passage herself.{/n}
"Use the proper door next time," {n}she says.{/n} "I would prefer to decide whether to admit you without first having an argument with the architecture."
{n}At the entrance she pauses, still holding the gate.{/n}
"I am glad you came."
{n}She lets you hear it without turning it into a joke.{/n}''',
      c('[Leave with the means to arrange another private visit.]', flags=("konomi.reconnection_open",), requires=("konomi.disagreement",)),
      c('[Leave with the means to arrange another private visit.]', flags=("konomi.reconnection_open", "konomi.private_history_ready"), forbids=("konomi.disagreement",))),
], Relationship="konomi", Remote=True, Areas=[DREZEN], Chapters=[3, 5],
    requires=("konomi.dismissed", "konomi.office_completed", "konomi.private_appointment"),
    forbids=("konomi.present", "inhuman", "konomi.farewell"), delay=24, optional=True))


def ending(id, text, requires=(), forbids=(), owner="Epilogue"):
    if id in ("public", "private", "apart", "unfinished"):
        forbids = (*forbids, "konomi.private_future")
    if id == "apart":
        forbids = (*forbids, "konomi.private_declined")
    SCENES.append(scene("konomi.ending_" + id, "Letters without a seal", owner, 5, "", [
        n("start", "Narrator", text, c(), portrait="Konomi"),
    ], Relationship="konomi", last=99, requires=requires, forbids=forbids))


ending("public", '''{n}Lady Konomi never became a reliable source of agreement with the Commander. Their arguments were so well known that visitors sometimes arrived prepared to discover a relationship on the point of ending.{/n}
{n}Instead they found two people who had made room for one another without giving up the occupations and opinions that made them difficult company. Konomi continued to write formidable letters. The few she left unsealed were read more often than all the rest.{/n}''', requires=("konomi.committed", "konomi.public"), forbids=("konomi.closed", "inhuman", "ascended"))
ending("private", '''{n}There were people who confidently explained the nature of the Commander's relationship with Lady Konomi. Their accounts disagreed, and neither of the people involved proved helpful in settling the matter.{/n}
{n}Konomi kept her own work, her own convictions, and a place in her appointments that she defended with particular determination. In the rooms they shared, an undistinguished plant finally survived an entire winter.{/n}''', requires=("konomi.committed",), forbids=("konomi.closed", "konomi.public", "inhuman", "ascended"))
ending("changed", '''{n}The Commander's transformation made their shared life difficult to describe. Konomi refused to offer a convenient description. There were meetings, arguments, familiar words spoken in unfamiliar ways, and losses neither of them pretended not to feel.{/n}
{n}She continued to choose those meetings. When questioned, she sometimes asked why everybody found a promise comprehensible only when it resembled one they had made themselves.{/n}''', requires=("konomi.committed", "inhuman"), forbids=("konomi.closed", "ascended"))
ending("ascended", '''{n}Divinity did not spare the Commander Lady Konomi's correspondence. She regarded silence as a poor answer from a ruler and saw no reason to lower her standards for a god.{/n}
{n}Among the formal letters were smaller pages without seals. In them she described an ordinary day, asked an impertinent question, or left an invitation. When an answer arrived, she put her work aside to read it alone.{/n}''', requires=("konomi.committed", "ascended"), forbids=("konomi.closed",))
ending("apart", '''{n}Konomi and the Commander eventually spoke through official channels more often than private ones. She did not deny what had passed between them, and did not make it available for other people's entertainment.{/n}
{n}A small bundle of letters remained among her possessions. She knew their contents well enough that she rarely opened them.{/n}''', requires=("konomi.lovers", "konomi.closed"))
ending("dismissed_apart", '''{n}After the Commander declined her private invitation, Konomi made no further attempt to arrange a meeting. The end of her appointment had already given her reasons to pursue work elsewhere; the answer settled what place the Commander would have in those plans.{/n}
{n}She continued toward Nerosyan when her work allowed. Whatever she thought of the extraordinary delivery that had briefly reopened their correspondence, she did not ask it to carry another letter.{/n}''', requires=("konomi.private_declined", "konomi.closed"), forbids=("konomi.private_future",))
ending("unfinished", '''{n}The war left Lady Konomi and the Commander with more things unsaid than either had intended. For a time, each new letter seemed likely to contain the invitation that would change that.{/n}
{n}Konomi kept one evening free longer than she admitted to anybody. Eventually she filled it, though she never quite lost the habit of glancing up when a messenger arrived.{/n}''', requires=("konomi.attracted",), forbids=("konomi.committed", "konomi.closed"))
ending("aeon", '''{n}In a history where the Worldwound had never opened, Konomi had other offices to pursue and other arguments to win. Once, while correcting a letter, she stopped over a sentence about an ordinary day she could not remember having planned.{/n}
{n}She left it in the margin. Years later, she still could not explain why she had not crossed it out.{/n}''', requires=("konomi.committed",), forbids=("konomi.closed",), owner="AeonEpilogue")
