"""Ember's friendship opening; later outcomes and restored access remain in development."""
from story_format import c, n, scene

RELATIONSHIP = dict(
    Title="An afternoon of her own",
    Description="Ember has asked me to help with something that needs neither a commander nor a miracle. I would like to make time for more afternoons like it.",
    Objective="Spend time with Ember",
    Guidance="While Ember is with the crusade, quiet rests in Drezen offer time to know her outside her public work. Her own wishes matter in these conversations.",
    StartedFlag="ember.started", ClosedFlag="ember.closed", CommittedFlag="ember.trusted_friend",
    UnavailableFlags=["ember_dead", "ember_gone", "ember.absent"], FailureFlags=[],
)
SCENES = []


def s(id, title, nodes, requires=(), delay=24):
    for node in nodes:
        node["Portrait"] = "Ember"
    SCENES.append(scene("ember." + id, title, "Ember", 3, title, nodes,
                        Relationship="ember", Chapters=[3], last=3,
                        ContactUnit="2779754eecffd044fbd4842dba55312c",
                        AnswerLists=["f2a35965e9bc601449498bd022b04d9d"],
                        Areas=["2570015799edf594daf2f076f2f975d8"],
                        requires=("ember.present",) + requires, delay=delay,
                        forbids=("ember.closed", "ember_dead", "ember_gone", "ember.absent")))


s("drawing", "A difficult likeness", [
    n("start", "Narrator", '''{n}Ember has found a sheltered patch of paving in Drezen and a piece of white chalk. Soot watches from the back of a nearby chair.{/n}
{n}The drawing at her feet has wings, a beak, two tails, and rather more legs than a crow requires. She looks from it to Soot with serious attention.{/n}''',
      c('"Is that Soot?"', "bird"),
      c('[Wait to see what she adds.]', "wait"),
      c('[Leave her to finish and return another time.]', abort=True)),
    n("bird", "Ember", '''"It was meant to be. But I think it might be somebody else."
{n}She rubs out one of the legs. The resulting white patch does not improve the likeness.{/n}
"Soot keeps moving. And then I forget which bits I have already drawn."''', c('"Perhaps this bird needs a name of its own."', "name")),
    n("wait", "Ember", '''{n}She starts another tail, notices the two already there, and stops.{/n}
"Oh. I did that part already."
{n}Ember notices you watching and moves so you can see the whole picture.{/n}
"I don't think he's Soot anymore. Do you know what sort of bird he is?"''', c('"Perhaps we have discovered a new one."', "name")),
    n("name", "Ember", '''"Then we ought to name him. It would be rude to keep calling him a mistake."
{n}She holds out the chalk.{/n}
"Would you like to draw something he can stand on? He has a lot of feet to put somewhere."''',
      c('[Draw an enormous branch and call the bird General Manyboots.]', "boots", flags=("ember.manyboots",)),
      c('[Draw a crooked roof and call the bird The Rain Inspector.]', "rain", flags=("ember.rain_inspector",))),
    n("boots", "Ember", '''"General Manyboots. Does he have to go to meetings?"
{n}She adds a second branch, apparently in case the general needs somewhere to put his remaining feet.{/n}
"I hope they let him go outside sometimes. It would be a shame to have all those legs and only use them under a table."''', c('"We will give him the afternoon off."', "afternoon")),
    n("rain", "Ember", '''"He will need a very big hat."
{n}She starts drawing one and stops halfway through.{/n}
"But if he stays dry, how will he know whether the rain is doing its work? Perhaps he can keep one tail outside the hat."''', c('"That must be why he has two."', "afternoon")),
    n("afternoon", "Ember", '''{n}Ember laughs. Soot shifts on the chair, unimpressed by the explanation.{/n}
"I wanted to do something like this today. People have been asking me things, and I don't always know the answers."
{n}She looks down at the drawing.{/n}
"I didn't know how to draw him either. But nobody was going to be hurt if I got it wrong."''',
      c('"May I join you another afternoon?"', "again"),
      c('"I am glad you found time for it."', "again")),
    n("again", "Ember", '''"You can come again. We haven't decided what he eats."
{n}She puts the short piece of chalk on the wall where she can find it later.{/n}
"And I would like to know what you draw when you aren't drawing a bird."''', c('[Make time to return.]', flags=("ember.started",))),
], delay=0)

s("visitor", "Who has the afternoon", [
    n("start", "Narrator", '''{n}You find Ember near the drawing. A woman is speaking to her about an argument at home, returning to the beginning whenever Ember tries to answer.{/n}
{n}At last Ember says she does not know which of the woman's sisters should have kept their mother's cup. The woman looks disappointed.{/n}
{n}She asks whether Ember might pray until an answer comes.{/n}''',
      c('"She has answered you. You should speak to your sisters."', "intervene", flags=("ember.intervened",)),
      c('[Let Ember finish answering for herself.]', "answer", flags=("ember.listened",))),
    n("intervene", "Narrator", '''{n}The woman recognizes you and leaves after an embarrassed apology. Ember waits until she is out of earshot.{/n}''', c('[Listen to Ember.]', "own")),
    n("own", "Ember", '''"I wanted her to stop asking. Thank you."
{n}Ember turns the chalk over between her fingers.{/n}
"But next time, could you ask me first? She went away because you're the Commander. I wanted to tell her that I really didn't know. She might think you stopped me from telling her."''',
      c('"You are right. Next time I will ask what help you want."', "finish", flags=("ember.ask_first",)),
      c('"I thought getting her to leave was what mattered."', "explain")),
    n("explain", "Ember", '''"It mattered. So did the other part."
{n}She says it without raising her voice.{/n}
"If I want somebody to speak for me, I can ask them. I would like you to believe me when I say I can answer."''',
      c('"I will try to remember that."', "finish", flags=("ember.ask_first",))),
    n("answer", "Ember", '''"I can pray with you if you want. But I still won't know who should have the cup. You will have to listen to each other."
{n}The woman asks one more question. Ember gives the same answer. Eventually the woman leaves, looking thoughtful and a little cross.{/n}
"I think she wanted a different answer. I wanted to have one, too."''', c('"You do not have to invent one to make her happy."', "finish", flags=("ember.answer_respected",))),
    n("finish", "Ember", '''{n}Ember crouches beside the chalk bird. Somebody's boot has smudged the end of its beak.{/n}
"Would you like to help me fix this? I know what to do about a beak."
{n}She studies the damage.{/n}
"I think."''', c('[Help with the drawing.]', flags=("ember.afternoon_kept",))),
], requires=("ember.started",))

s("rain", "What the rain left", [
    n("start", "Narrator", '''{n}Rain has washed most of the drawing away. Ember stands over the faint white outline with Soot on the wall beside her.{/n}''',
      c('"General Manyboots appears to have deserted."', "boots", requires=("ember.manyboots",)),
      c('"The Rain Inspector has had a busy night."', "inspector", requires=("ember.rain_inspector",))),
    n("boots", "Ember", '''"Perhaps he went for a walk. We gave him enough feet."
{n}Her gaze follows a chalk streak across the paving.{/n}
"I wish I'd drawn him on paper. I liked him."''', c('"We could draw him again."', "remember")),
    n("inspector", "Ember", '''"He must have gone to tell somebody that it was very good rain."
{n}She looks at the pale mark where the enormous hat used to be.{/n}
"I liked him. I thought he might stay a little longer."''', c('"We could draw him again."', "remember")),
    n("remember", "Ember", '''"He wouldn't be quite the same. We might forget one of the wrong bits."
{n}She takes the chalk from its place on the wall, then pauses before drawing.{/n}
"What would you like to make today? You helped with my bird. It's your turn to choose."''',
      c('"A place I would like to visit when there is time."', "place", flags=("ember.shared_place",)),
      c('"Something I used to be afraid of. Perhaps it will look smaller here."', "fear", flags=("ember.shared_fear",))),
    n("place", "Ember", '''"Tell me what belongs there. I won't put in extra legs unless you ask."
{n}She waits while you describe it. When she does not understand, she asks, and leaves room for the answer instead of filling the space with chalk.{/n}''', c('[Describe the place to her.]', "end")),
    n("fear", "Ember", '''"We don't have to make it smaller. You can stop if you don't like looking at it."
{n}She leaves the chalk between you.{/n}
"Or we could draw something else beside it. I would like you to choose."''', c('[Tell her what you want to draw.]', "end")),
    n("end", "Narrator", '''{n}The new drawing is no more accomplished than the first. Ember studies it for a while.{/n}''',
      c('[Look at the place you have drawn.]', "question_place", requires=("ember.shared_place",)),
      c('[Look at the thing you remembered.]', "question_fear", requires=("ember.shared_fear",))),
    n("question_place", "Ember", '''"Who would you like to show it to when you get there?"
{n}Until she asks, you have been thinking mostly about the journey. She waits while you consider who might enjoy the place itself.{/n}''',
      c('[Tell her whom you would invite.]', flags=("ember.shared_afternoon",))),
    n("question_fear", "Ember", '''"Shall we rub that bit out before we go? Or would you rather leave it for the rain?"
{n}She has kept a little water in a chipped cup. She moves it within reach and waits for your answer.{/n}''',
      c('[Wash the drawing away together.]', flags=("ember.shared_afternoon", "ember.washed_drawing")),
      c('[Leave it for the rain.]', flags=("ember.shared_afternoon",))),
], requires=("ember.afternoon_kept",))
