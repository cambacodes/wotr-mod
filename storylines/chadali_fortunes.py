"""Chadali: the cauldron, the needle, and what comes after the question (Chapter 5, and after the commit).

Every scene is in the Council hall, on her own private list (Council_Chadali/AnswersList_0003). Canon anchors:
- the cauldron in Cobblehoof's bag and her fear of it: "Oh... Will it... hurt?" (Council_5-1/Cue_0044 ea1508e9); Shyka:
  "It is a terrifying, agonizing experience." (Cue_0045 a6b9f0dc); "No, I wouldn't do that to my friends... Um, we are
  friends, right?" (Cue_0052 61537e58);
- the fair: "Instead of wastelands and battlefields, we'll hold a great big fair! ... I've always wanted to pet a
  cerberi." (Council_5-2/Cue_0003 fa43e0b4), answering Alichino's "Hundreds, thousands of souls will be sold" (Cue_0002);
- the bows for Nocticula: "So cute! Wait, wait, let me tie some bows on you! I have matching ribbons." (Cue_0057 82431dc0);
- "the needle is scary" (Cue_0029 0b95f7d5) and "no one needs your worthless essence!" (Cue_0032 65e5e459);
- after the essence was taken, in the allied branch: "Oh, it was terrible! It hurt so, so much... Chance doesn't always
  bring you honey cookies. Sometimes you get sharp needles." (Council_Chadali/Cue_0033 86822037);
- the yellow silk, the white flowers in her hair, the bracelets, the white-gold ring (Cue_0001 f674c7cf, Cue_0018 51c885e2).
Her home on Elysium and her fears are her own telling in her own voice.
"""
from story_format import c, scene
from storylines.chadali_trickster import (CLOSED, COMMITTED, LIST, LOST, LUCK_LENT, LUCK_OWED, STARTED, ch, nar)
from storylines.chadali_wagers import GUESSED

SCENES = []
F = "chadali.fortunes."

# Canon moments this module reads (SeenCues).
FEARED = "chadali.feared_the_cauldron"       # Council_5-1/Cue_0044: "Oh... Will it... hurt?"
FAIR_SEEN = "chadali.fair_proposed"           # Council_5-2/Cue_0003: the great big fair
BOWS_SEEN = "chadali.bows_for_nocticula"      # Council_5-2/Cue_0057: "let me tie some bows on you"
WORTHLESS = "chadali.worthless_essence"       # Council_5-2/Cue_0032: "no one needs your worthless essence!"
NEEDLED = "chadali.needle_hurt"               # Council_Chadali/Cue_0033: "It hurt so, so much..."

SEEN_CUES = {
    FEARED: ["ea1508e9383290a4dac192b606fdd0d4"],
    FAIR_SEEN: ["fa43e0b471527ec4ea59b268e6fcf36d"],
    BOWS_SEEN: ["82431dc02fb007c4a9bd17f9bd636152"],
    WORTHLESS: ["65e5e45942cacf946b3279cdd6a67af3"],
    NEEDLED: ["86822037eac848943abe4be795037ae7"],
}

BAG = F + "will_it_hurt"
FAIR = F + "a_great_big_fair"
BOWS = F + "matching_ribbons"
MEAN = F + "worthless"
AFTER_NEEDLE = F + "sharp_needles"
NIGHT = F + "honey"
MORNING = F + "burnt_edges"
RIGGED = F + "rigged"
ELYSIUM = F + "the_meadows"
RIBBON = F + "a_yellow_ribbon"
SHARING = F + "sharing"
REPAID = F + "paid_back"

# Outcomes the epilogue reads.
PROMISED_SAFE = F + "promised_no_force"
TOLD_IT_HURTS = F + "told_it_would_hurt"
SAW_THE_FAIR = F + "saw_the_fair_plainly"
FORGAVE_MEAN = F + "forgave_worthless"
HELD_AFTER = F + "held_after_the_needle"
NIGHT_FLAG = F + "night"
NO_MORE_RIGGING = F + "no_more_rigging"
KEPT_RIGGING = F + "kept_rigging"
ELYSIUM_PROMISED = F + "meadows_promised"
RIBBON_WORN = F + "ribbon_worn"
RIBBON_POCKETED = F + "ribbon_pocketed"
NOT_LAST = F + "not_last"


def fortune(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5)):
    """A physical sitting on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Chadali", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="chadali", Chapters=list(chapters), AnswerLists=[LIST]))


# --- 1. Will it hurt? (the cauldron in the bag) -----------------------------------------------------------------------

fortune(BAG, "Will it hurt?", '"You\'ve been quiet since the cauldron."', [
    nar("open", '''{n}The bag Cobblehoof carried lies folded on the Council table, empty. Chadali is sitting as far from it as the table allows, and she has not baked. Her hands are in her lap, turning the white-gold ring round and round.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Shyka smiled at me." {n}She says it to the ring.{/n} "When I asked if it would hurt. They smiled, and said yes, and said it takes a part of your very being, and that they've done it many times before. Cheerfully. Like a recipe."
"And then everyone looked at me. Because I'm the one who says everything will work out." {n}Her voice wobbles.{/n} "I said, is there no other way? I sounded so small. I've never sounded small in this hall in my life."''',
      c('"Nobody will take it from you by force. Not while I\'m here."', "promise", flags=(PROMISED_SAFE,)),
      c('"It will hurt. I won\'t lie to you. But it won\'t be for nothing."', "truth", flags=(TOLD_IT_HURTS,)),
      c('"There might be another way. I\'m looking."', "looking")),
    ch("promise", '''{n}She looks up so fast the flowers shake in her hair.{/n}
"You mean it? You can't mean it. You need them. All of them. I read the Lexicon, or Eritrice read it to me, which is the same thing but slower." {n}Her hands have stopped on the ring.{/n}
"If I say no and you've promised, then you have to choose between me and closing the Wound." {n}A breath.{/n} "Don't promise me that. Promise me something you can keep."''',
      c('"I\'ll keep it. I\'ll find the other way."', "keep"),
      c('"Then I promise to be there, whatever happens."', "there")),
    ch("truth", '''"It will hurt." {n}She repeats it, and nods, slowly, and her chin firms.{/n}
"Thank you. Everyone else is being nice to me, or mean to me. Alichino says it will be 'a formality'. Cobblehoof says 'Phrr'. You just said it will hurt." {n}She lets out a shaky laugh.{/n} "That's the first thing anyone's said about it that I could hold."''',
      c("Continue", "brave")),
    ch("looking", '''"Looking." {n}She seizes the word like a cookie.{/n} "You're always looking. You found the way into the Lexicon when none of us could. You found the orange."
{n}Then her face does something complicated.{/n} "But you put the orange there. You didn't find it." {n}A long silence.{/n} "Are you going to put another way there, too? Make it up? Because if you do, and it's a trick, and it doesn't work, I'll have hoped for nothing, and I'll never forgive you."''',
      c('"No tricks. If there\'s no other way, I\'ll tell you."', "brave", flags=(TOLD_IT_HURTS,))),
    ch("keep", '''{n}She holds your eyes for a long time, measuring. She is chance; she knows odds better than anyone in the multiverse.{/n}
"All right," she says at last. "I'll hope. I'm very good at hoping. You be very good at finding." {n}She takes your hand and puts it on the table between you, and puts hers over it.{/n} "And if you can't, you tell me first. Before the needle. Not after."''',
      c("[Promise that too.]")),
    ch("there", '''"There." {n}She thinks about it.{/n} "Yes. That I can hold. If there's a needle, you'll be there."
{n}She squeezes your fingers so hard her bracelets bite.{/n} "Hold my hand. Don't look at the needle. Tell me a joke. A bad one. I like the bad ones."''',
      c("[Promise.]")),
    ch("brave", '''{n}She straightens up in her chair, the way you have seen soldiers straighten when the horns sound.{/n}
"Then I'll be brave. I don't know how. I've never had to be; everything always just went well." {n}She pulls the folded bag across the table, at last, and looks at it.{/n}
"I'll believe it'll be all right. And then I'll check the oven."''',
      c("[Stay with her.]")),
], requires=(STARTED, "council.cauldron_given"), forbids=(BAG,), chapters=(5,))


# --- 2. A great big fair. ---------------------------------------------------------------------------------------------

fortune(FAIR, "A great big fair", '"About your fair..."', [
    ch("start", '''"Oh, the fair!" {n}She is all lit up again.{/n} "Instead of wastelands and battlefields, a great big fair! With acrobats, and lollipops, and exotic beasts from different planes. I've always wanted to pet a cerberi. I love puppies. A puppy with three heads would be three times the fun!"''',
      c('"Alichino said thousands of souls would be sold there."', "souls"),
      c('"A cerberus would eat you."', "puppy"),
      c('[Flirt] "Save me a lollipop."', "lollipop")),
    ch("souls", '''{n}The light goes out of her face, and comes back, and goes out again, as if she were fighting with a lamp.{/n}
"He said that and then he said something else very fast. I heard the something else. I prefer the something else." {n}She crosses her arms.{/n}
"You're doing it again. You're making me look at things. The bleeding, and the brick, and now the souls." {n}Her voice rises.{/n} "Why can't I have one nice thing without you holding it up to the light and showing me the crack?"''',
      c('"Because you\'d want to know. If it were your fair and your crack."', "know", flags=(SAW_THE_FAIR,)),
      c('"You can. I\'m sorry. Have your fair."', "fair_kept")),
    ch("know", '''{n}She glares at you. It is not a very good glare; she has not had much practice.{/n}
"...Yes." {n}Grudgingly.{/n} "I'd want to know. It's my fair." {n}She uncrosses her arms.{/n}
"Then no souls. No selling. Not one. If Alichino wants a stall, he can sell lollipops." {n}She nods, fiercely.{/n} "I'll tell Eritrice to write it down. She likes rules. She'll write it in red."''',
      c("Continue", "close")),
    ch("fair_kept", '''"Thank you." {n}She sniffs, and then smiles, and then does not smile.{/n}
"No. You were right. You're always right about the cracks. It's horrible." {n}She sighs.{/n} "No souls at my fair. I'll watch the devil's stall myself. With a very big lollipop."''',
      c("Continue", "close", flags=(SAW_THE_FAIR,))),
    ch("puppy", '''"It would not!" {n}Offended.{/n} "I'd bring it a cookie. Nothing eats you when you've brought it a cookie. It's a law."
"...It would eat the cookie first. Then it would think about eating me. And while it was thinking I'd scratch its ears, all three pairs, and it would forget." {n}She beams.{/n} "That's how I've survived everything so far."''',
      c("Continue", "close")),
    ch("lollipop", '''"A red one." {n}Instantly.{/n} "The biggest one. On a stick as long as your arm. And you'll have to carry it round the whole fair and everyone will know it's from me."
{n}She considers you, head tilted.{/n} "You'd look very serious with a giant lollipop. That's why I want to see it."''',
      c("Continue", "close")),
    ch("close", '''"When it's done, you'll come." {n}Not a question.{/n} "You'll come to my fair and hold my hand and pet the puppy. And if anyone tries to sell anything with a soul in it, you'll trick them. You're good at that. I'll allow it, at the fair."''',
      c("[Promise to come.]")),
], requires=(STARTED, FAIR_SEEN), forbids=(FAIR,), chapters=(5,))


# --- 3. Matching ribbons. ----------------------------------------------------------------------------------------------

fortune(BOWS, "Matching ribbons", '"You offered Nocticula ribbons."', [
    ch("start", '''"She looked so cute!" {n}Chadali claps, and then covers her mouth, and then claps again because she cannot help it.{/n}
"The Lady in Shadow, in that outfit! Everybody laughed. I didn't laugh. Well, I did. But then I thought, she's embarrassed, and she's shouting, and nobody's being kind to her, so I offered her bows. I have matching ribbons. I always have matching ribbons."''',
      c('"She\'s a demon lord. She could have killed you."', "killed"),
      c('"Were you trying to help her, or to laugh at her more politely?"', "politely"),
      c('"Socothbenoth and I did that to her."', "did")),
    ch("killed", '''"She could have." {n}Cheerfully.{/n} "She didn't. People mostly don't, when you offer them ribbons. It confuses them."
{n}Then, more slowly:{/n} "I'm not afraid of her. Isn't that strange? I'm afraid of a needle, and I'm not afraid of the Lady in Shadow. I think it's because she's all show, and the needle isn't."''',
      c("Continue", "close")),
    ch("politely", '''{n}She stops clapping. She thinks about it, properly, with her tongue between her teeth.{/n}
"Both," she says at last. "Heads and tails." {n}A small, guilty smile.{/n} "I wanted her to feel better. I also wanted to see what she'd look like with a big yellow bow on her horns. I don't think those are different wants. I think that's just what being kind is, mostly."''',
      c("Continue", "close")),
    ch("did", '''"I know." {n}She looks at you with bright, uncomplicated fondness.{/n} "That was a good trick. A mean one. But she deserved a little meanness; she's been very mean to lots of people for a very long time."
"And then I offered her ribbons, so it came out even." {n}She nods, satisfied with the arithmetic.{/n} "You do the mean part, and I do the ribbons. We're a good pair."''',
      c("Continue", "close")),
    ch("close", '''{n}She pulls a length of yellow ribbon out of her sleeve, where it has apparently been all along, and ties it in a bow round your wrist before you can object.{/n}
"There. In case you meet anyone embarrassed on the way home."''',
      c("[Leave the bow on.]")),
], requires=(STARTED, BOWS_SEEN), forbids=(BOWS,), chapters=(5,))


# --- 4. Worthless. -----------------------------------------------------------------------------------------------------

fortune(MEAN, "Worthless", '"You said no one needs my essence."', [
    nar("open", '''{n}She is on her feet the moment she sees you, and then she does not come any closer. There is a parcel in her hands. It is not wrapped in yellow silk this time; it is wrapped in something grey, as if she had not been able to bear the yellow.{/n}''',
        c("Continue", "start")),
    ch("start", '''"I know what I said." {n}Her voice is tight.{/n} "In front of everyone. You said we all like to talk and none of us want to act, and I said it was easy for you to say, because nobody needs your worthless essence."
"Worthless." {n}She says it again, as if it tasted of something rotten.{/n} "I said that. To my lucky charm. To you."''',
      c('"You were frightened. I know."', "frightened"),
      c('"It hurt."', "hurt"),
      c('"You weren\'t wrong. Nobody wants mine."', "wrong")),
    ch("frightened", '''"I was frightened." {n}She nods, too many times.{/n} "I was so frightened that I went looking for the meanest thing in the room, and it was me." {n}She holds the grey parcel out, stiffly.{/n}
"Everybody thinks I'm only nice. I'm not. I'm nice the way a sunny day is nice: because nothing's gone wrong yet. When something goes wrong, I can be as mean as Alichino. Meaner. He at least means it on purpose."''',
      c('"Everyone has a worst moment. That was yours."', "forgive", flags=(FORGAVE_MEAN,)),
      c('"Then don\'t do it again."', "again")),
    ch("hurt", '''{n}She flinches as if you had thrown something.{/n}
"Good," she says, and then, horrified: "No. Not good. I meant... good that you told me. Not good that it hurt." {n}She presses the grey parcel against her chest.{/n}
"I'm not used to hurting people. I'm used to hurting for them. I don't know what to do with this. I baked. I burnt them. They're in here."''',
      c("[Take the burnt cookies, and eat one.]", "forgive", flags=(FORGAVE_MEAN,))),
    ch("wrong", '''"Don't." {n}The flat no, the raised finger.{/n} "Don't say that. I said it to be cruel, and you're saying it to agree with me, and both of those are lies."
"Your essence is the only one in this whole hall that isn't for sale. That's what makes it worth something." {n}Her finger trembles.{/n} "I knew that when I said it. That's what made it so mean."''',
      c('"Then we\'re even. Your worst moment, and my agreeing with it."', "forgive", flags=(FORGAVE_MEAN,))),
    ch("again", '''"I won't." {n}Instantly, fiercely.{/n} "I'll try not to. I'll be frightened again, I know I will, and when I am, I'll eat a cookie and say something nice about the weather instead."
{n}Her mouth wobbles.{/n} "That's a promise. I don't know if I can keep it. I'm telling you that too, because that's fair."''',
      c("Continue", "close")),
    ch("forgive", '''{n}The cookies are very burnt. You eat one anyway. She watches you with enormous wet eyes.{/n}
"You ate the burnt one." {n}Her voice cracks.{/n} "I told you about the burnt ones. I told you I eat them myself, alone, so nobody knows." {n}She sets the grey parcel down and puts both her hands over her face.{/n} "Now somebody knows."''',
      c("Continue", "close")),
    ch("close", '''{n}When she takes her hands away, her face is blotched and her dimples are back.{/n}
"Next time you're mean to me, I'll forgive you straight away. That's the rule. You went first."''',
      c("[Go.]")),
], requires=(STARTED, WORTHLESS), forbids=(MEAN,), chapters=(5,))


# --- 5. Sharp needles: after the essence (allied branch). --------------------------------------------------------

fortune(AFTER_NEEDLE, "Sharp needles", '"How are you?"', [
    nar("open", '''{n}She is sitting very still in her chair, wrapped in a shawl that is not yellow. Something about her is dimmer than it was, the way a room is dimmer when one lamp in it has gone out, though you could not say which. There is no parcel.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Oh, it was terrible." {n}She says it with a brave little smile that falls apart halfway through.{/n} "It hurt so, so much. But what can you do? Chance doesn't always bring you honey cookies. Sometimes you get sharp needles."
{n}She holds up one hand. It is steady. Then it isn't.{/n} "I can't feel the meadows. I always could. There's a little hole where a bit of Elysium used to be, and the wind goes through it."''',
      c("[Sit beside her. Say nothing.]", "sit", flags=(HELD_AFTER,)),
      c('"It will grow back?"', "grow"),
      c('"I promised you. I\'m sorry."', "sorry", requires=(PROMISED_SAFE,))),
    ch("sit", '''{n}You sit. After a while she leans against you, the whole warm weight of her, and breathes out, long and slow.{/n}
"This is better than any cookie," she says into your shoulder. "Don't tell anyone I said that. It would ruin my whole reputation."
"...Tell me a joke. A bad one."''',
      c("[Tell her a very bad joke.]", "joke")),
    ch("grow", '''"I don't know." {n}She shrugs, and winces.{/n} "Nobody's ever taken any of me before. Shyka says it heals. Shyka also smiled when they said it would hurt, so I don't believe anything Shyka says any more."
"I'll believe it grows back. That's all I can do. And then I'll check." {n}She looks at you.{/n} "Will you check with me? Every time you're here. Just ask. 'Is it growing?' And I'll say yes, even if it isn't, and you'll know I'm lying, and that's all right."''',
      c('"Is it growing?"', "joke", flags=(HELD_AFTER,))),
    ch("sorry", '''"Sorry for what?" {n}Firmly.{/n} "You promised nobody would take it from me by force, and nobody did. Nobody held me down. I sat in the chair and held out my arm."
"You didn't break anything. I gave it, because you needed it, and I'm a lot braver than I look." {n}Her chin wobbles, and lifts.{/n} "I just didn't know brave felt this bad afterwards. Nobody tells you."''',
      c("[Hold her.]", "joke", flags=(HELD_AFTER,))),
    ch("joke", '''{n}She laughs. It is a small laugh, and it catches on something, but it is a real one.{/n}
"That was awful," she says. "That was the worst one yet." {n}She wipes her eyes on the not-yellow shawl.{/n}
"Tomorrow I'll bake. Tomorrow I'll wear yellow. Tonight I'm going to sit here with you and be sad, and it's going to be the luckiest sad I've ever been."''',
      c("[Stay.]")),
], requires=(STARTED, NEEDLED), forbids=(AFTER_NEEDLE,), chapters=(5,))


# --- 6. Honey: the night after the yes (heat up to the cut). ---------------------------------------------------------

fortune(NIGHT, "Honey", '"You sent for me. After dark."', [
    nar("open", '''{n}The hall is lit only by candles, dozens of them, set along the Council table in a crooked, happy line that someone has plainly done without measuring. There is a smell of honey and warm wax. The chairs have been pushed back to the walls, and in the middle of the floor someone has laid out every cushion in the hall, and a few that were not in the hall before.{/n}''',
        c("Continue", "start")),
    ch("start", '''{n}Chadali is standing in the middle of the cushions in a robe of yellow silk so thin the candlelight comes through it. Her hair is down. She has taken every flower out of it but one.{/n}
"I didn't leave anything to chance." {n}She is trying very hard to look serene, and her hands are twisting in the silk.{/n} "Not one thing. I counted the candles. I chose the cushions. I've never planned anything in my whole existence. It's exhausting. I don't know how you do it every day."''',
      c('[Take her hands.] "You did it perfectly."', "hands"),
      c('"You forgot one thing."', "forgot"),
      c('[Kiss her.]', "kiss")),
    ch("forgot", '''"What? What did I forget?" {n}Real alarm. She looks round at the candles as if one of them might have betrayed her.{/n}
{n}You cross the cushions to her, and take the last white flower out of her hair, and put it behind your own ear.{/n}
{n}She stares at you. Then she laughs, low and breathless, nothing like the bright laugh of the Council sessions.{/n} "Oh. That. Yes. I forgot to let you do something."''',
      c("[Kiss her.]", "kiss")),
    ch("hands", '''{n}Her hands are warm and shaking, and they stop shaking when you hold them.{/n}
"Perfectly." {n}She tries the word out.{/n} "Nobody's ever said I did anything perfectly. They say 'lucky'. They say 'what a nice surprise'." {n}She looks up at you, and her eyes in the candlelight are very dark.{/n}
"I wanted it to be on purpose. Tonight. All of it. I wanted you to know I meant it."''',
      c("[Kiss her.]", "kiss")),
    ch("kiss", '''{n}She tastes of honey. Of course she does. She kisses the way she laughs, all at once and with her whole body, up on her toes with both hands knotted in your sleeves, and when she runs out of breath she does not stop so much as pause and begin again.{/n}
{n}Her bracelets are cold against the back of your neck and her mouth is hot, and she makes a small astonished sound, as if something unexpectedly wonderful had happened to her, which, you slowly understand, it has.{/n}''',
      c("Continue", "silk")),
    ch("silk", '''{n}She is soft everywhere your hands go, and warm, and nowhere near as patient as she was trying to look. The yellow silk slides off one round shoulder, and she does not catch it. She is busy with your buckles, and cursing them, sweetly and inventively, in a language that sounds like birdsong and is obviously filthy.{/n}
"Whoever made this armour," she says, "has never been kissed. Not once. I can tell. It's in the straps."''',
      c("[Help her with the straps.]", "look")),
    ch("look", '''{n}When the last of it is off she pulls you down among the cushions, and the candles gutter in the draught you make, and for a moment she simply lies there looking up at you, flushed and dishevelled, one hand spread flat on your chest as if feeling for a heartbeat she had bet on.{/n}
"Lucky me," she whispers, and she does not mean it as a joke.''',
      c("[Lean down to her.]", "cut", flags=(NIGHT_FLAG,))),
    ch("cut", '''{n}She pulls the silk loose the rest of the way and draws you down to her, and her laugh against your mouth is the last thing you hear clearly. Somewhere along the table a candle tips over and goes out, and neither of you notices, and neither of you minds.{/n}''',
      c("[...]")),
], requires=(COMMITTED,), forbids=(NIGHT,), delay=12)


# --- 7. Burnt edges: the morning after. -------------------------------------------------------------------------------

fortune(MORNING, "Burnt edges", '"Is something burning?"', [
    nar("open", '''{n}There is an oven in the hall now. You are fairly sure there was not an oven in the hall yesterday. Chadali is kneeling in front of it in the yellow robe, with her hair in a wild knot and a tray in her mitted hands, and the tray is smoking.{/n}''',
        c("Continue", "secret", requires=(GUESSED,)),
        c("Continue", "start", forbids=(GUESSED,))),
    ch("secret", '''"Don't look!" {n}She tries to hide the tray behind her back and burns her wrist on it.{/n} "You know about these. You're the only one who knows about these."
"I was going to eat them all myself, alone, the way I always do." {n}She looks at the black cookies, and at you, and her mouth twitches.{/n} "And then I thought, I'm not alone. That's the whole point. That's what last night was."''',
      c("[Take one. Eat it.]", "eat")),
    ch("start", '''"Don't look!" {n}She tries to hide the tray behind her back and burns her wrist on it.{/n} "They're not for you. They're burnt. I burn them sometimes. Nobody knows. I eat them myself, alone, the way I always do."
{n}She looks at the black cookies, and at you, and her mouth twitches.{/n} "And now you know. Oh, what a morning."''',
      c("[Take one. Eat it.]", "eat")),
    ch("eat", '''{n}It is truly terrible. It crunches like a cinder and tastes, faintly, underneath the char, of honey and of something that is not like anything at all.{/n}
{n}Chadali watches you chew with her hands pressed to her mouth. When you swallow, she bursts into tears and laughs at the same time.{/n}
"You ate a burnt one on purpose. On the first morning. That's the most romantic thing that's ever happened to me, and I'm an empyreal lord, and I was born under three different skies at once."''',
      c('"They\'re awful. Make more."', "more"),
      c('"Come back to bed. The oven can wait."', "bed")),
    ch("more", '''"I will! I'll make a hundred. I'll burn all of them, and you'll eat all of them, and that's how I'll know." {n}She is still laughing and crying.{/n}
{n}Then, suddenly shy, she tucks her hair behind her ear.{/n} "Was it... last night. Was it lucky?"''',
      c('"It wasn\'t luck."', "not_luck")),
    ch("bed", '''"The oven cannot wait. The oven is on fire." {n}It is, a little. She throws a cushion at it, which does not help, and then a bucket of water she seems to have had ready, which does.{/n}
{n}In the steam she turns round, soot on her nose, and says, very seriously:{/n} "Now the oven can wait."''',
      c('"Was it lucky, last night?"', "not_luck")),
    ch("not_luck", '''{n}She shakes her head, and the knot of hair comes down.{/n}
"No. It wasn't luck. You didn't leave it to chance, and I didn't leave it to chance, and it was still the most surprising thing that's ever happened to me." {n}She pushes the smoking tray away with her foot.{/n}
"I think that's what the other kind of luck is. The kind you make." {n}A pause.{/n} "Don't tell Eritrice I said that. She'll say it's a contradiction and write it down."''',
      c("[Kiss the soot off her nose.]")),
], requires=(NIGHT,), forbids=(MORNING,), delay=6)


# --- 8. Rigged: she finds out. -------------------------------------------------------------------------------------------

fortune(RIGGED, "Rigged", '"Why are you looking at me like that?"', [
    ch("start", '''{n}She is holding a letter from one of her priests. You can see the seal of a little Elysian sun on it. Her face is quite calm, which is how you know you are in trouble.{/n}
"My priests in Drezen had a very lucky month." {n}Calmly.{/n} "Their roof was mended for free. The grain came early. A soldier returned a purse she'd found, and there was twice as much in it as was lost." {n}She folds the letter.{/n}
"And every single lucky thing had a crusade stamp on it somewhere. Your stamp." {n}She looks up.{/n} "You rigged my luck."''',
      c('"I wanted your people to have a good month. Is that so bad?"', "bad"),
      c('"I wanted you to see it work. Your luck. For once."', "see"),
      c('[Trickster] "Someone had to. You\'re always giving it away."', "giving")),
    ch("bad", '''"Yes!" {n}The calm cracks.{/n} "Yes, it's bad! They think it was me. They think their prayers worked. They'll pray harder, and next month you'll be in the Abyss, and nothing will happen, and they'll think I've stopped loving them."
{n}She throws the letter on the table.{/n} "You can't rig somebody's luck because you love them. That's not luck, that's a leash."''',
      c("Continue", "choose")),
    ch("see", '''{n}That stops her. For a moment she looks at you with a kind of helpless tenderness, and then her mouth sets again.{/n}
"That's the sweetest, stupidest thing anyone's ever done for me." {n}She presses the heels of her hands to her eyes.{/n}
"But it wasn't my luck. It was yours, wearing my name. And they can't tell the difference. That's the part that frightens me. If you can do it, and nobody can tell, then what am I for?"''',
      c("Continue", "choose")),
    ch("giving", '''"I'm always giving it away because that's what it's for!" {n}She stamps her foot. Somewhere far away, you are certain, something unlucky happens to someone who deserved it.{/n}
"You don't get to decide where it goes. Not mine. You decide where the army goes, and where the money goes, and where half of Golarion goes. Leave me this."''',
      c("Continue", "choose")),
    ch("choose", '''"Promise me you'll stop." {n}She holds out her little finger, the way she did over the knucklebones.{/n} "Not the tricks. I love the tricks. The tricks where you pretend to be me."''',
      c("[Link fingers.] \"I'll stop.\"", "stopped", flags=(NO_MORE_RIGGING,)),
      c('"I can\'t promise that. If I see your people going hungry, I\'ll act."', "kept", flags=(KEPT_RIGGING,))),
    ch("stopped", '''{n}She shakes on it, once, firmly, and some tension goes out of her shoulders that you had not known was there.{/n}
"Good. Now I'll forgive you. I always do; it's very annoying." {n}She sniffs.{/n} "And you can mend their roof. Openly. With a sign on it that says it was the Commander. That's allowed. That's honest."''',
      c("[Promise to put up a sign.]")),
    ch("kept", '''{n}She looks at your hand, and at her own outstretched little finger, and slowly curls it back into her fist.{/n}
"Then do it with your name on it." {n}Very quietly.{/n} "If you have to act, act. Just don't do it wearing my face. I'll never ask you not to feed them. I'm asking you not to pretend you're me while you do it."
"That's the whole of it. That's all I've got left that's mine."''',
      c('"With my name on it. I promise that much."', "stopped")),
], requires=(MORNING,), forbids=(RIGGED,))


# --- 9. The meadows: Elysium, and a mortal clock. -----------------------------------------------------------------

fortune(ELYSIUM, "The meadows", '"Tell me about home."', [
    ch("start", '''"Home!" {n}She lies back on the cushions she has refused to put away, and stretches, and her bracelets slide down her arms.{/n}
"Meadows. Rivers. A sky that changes colour when it's happy, which is always. The bees I told you about, that have never been stung. Everybody dances, all the time, very badly, and nobody minds." {n}She turns her head to look at you.{/n} "You'd hate it for a week. Then you'd love it. Then you'd start trying to organise it, and they'd throw you in the river."''',
      c('"Would I be allowed to come?"', "allowed"),
      c('"I\'m mortal, Chadali. I\'ll be gone in a blink, to you."', "mortal")),
    ch("allowed", '''"Allowed!" {n}She sits up, scattering cushions.{/n} "You don't need allowing. You're with me. Everybody's allowed with someone."
"After the war. When the Wound's closed and the fair's built. I'll take you to the river and we'll sit in it and I'll feed you cookies until you stop looking at the horizon for enemies." {n}Her voice softens.{/n} "It might take years. I've got years."''',
      c('"Then it\'s a promise."', "promised", flags=(ELYSIUM_PROMISED,)),
      c('"I don\'t know if I have years."', "mortal")),
    ch("mortal", '''{n}She is quiet for a long time. When she speaks, the empyreal lord is in her voice, old and very gentle.{/n}
"I know. I know exactly how long you've got. I'm chance. I can feel the odds on everyone, like weather." {n}She takes your hand.{/n}
"I'm not going to tell you. Don't ask. It isn't bad and it isn't good, it's just a number, and numbers aren't the point."''',
      c('"What is the point?"', "point")),
    ch("point", '''"That you're here now. That the coin stood up." {n}She laces your fingers through hers.{/n}
"And afterwards, when you're gone... I'll bet on seeing you again. Somewhere. Some sky that lines up wrong. I'll keep making the bet for as long as I exist, and I exist for a very long time, and I've never lost a bet I cared about." {n}Her thumb moves over your knuckles.{/n} "That's what I've got instead of a mortal clock. A very long bet."''',
      c('"Then I\'ll bet the same."', "promised", flags=(ELYSIUM_PROMISED,))),
    ch("promised", '''"Done!" {n}She seals it with a kiss, a smacking, entirely unromantic one, on the forehead, the way she seals everything.{/n}
{n}Then she lies back down beside you and is quiet for a long, warm while, and when you look at her, her eyes are closed and she is smiling at something only she can see.{/n}''',
      c("[Let her dream.]")),
], requires=(NIGHT,), forbids=(ELYSIUM,))


# --- 10. A yellow ribbon. ---------------------------------------------------------------------------------------------

fortune(RIBBON, "A yellow ribbon", '"What\'s this for?"', [
    ch("start", '''{n}She has pressed something into your hand: a length of yellow silk ribbon, the same yellow as her robes, tied in a lopsided bow.{/n}
"For luck! Wear it. On your sword, or your sleeve, or your helmet. Somewhere people can see." {n}She beams.{/n} "Then everyone will know you're lucky, and they'll be braver, and that will make you luckier. That's how it works."''',
      c('[Tie it on your sword-hilt.] "Everyone will see it."', "worn", flags=(RIBBON_WORN,)),
      c('"My officers will never let me hear the end of it."', "officers"),
      c('[Put it in your pocket.] "I\'ll keep it close. Not where they can see."', "pocket", flags=(RIBBON_POCKETED,))),
    ch("officers", '''"Good!" {n}She is delighted.{/n} "Let them tease you. Teasing is just jealousy wearing a hat. They'll tease you, and then they'll ask where you got it, and then they'll want one."
"I have hundreds. I'll send a box. A whole regiment in yellow bows!" {n}She claps.{/n} "The demons won't know what to do."''',
      c('[Tie it on your sword-hilt.] "One regiment. Mine."', "worn", flags=(RIBBON_WORN,)),
      c('[Put it in your pocket.] "I\'ll keep it close."', "pocket", flags=(RIBBON_POCKETED,))),
    ch("worn", '''{n}She watches you knot it round the hilt with her hands clasped under her chin.{/n}
"It suits you. It suits the sword. The sword looks happier already." {n}She pats it, as if it were a horse.{/n}
"Now when you swing it, a little bit of me goes with it. The nice bit. I'm keeping the mean bit here, where it can't hurt anyone."''',
      c("[Kiss her.]")),
    ch("pocket", '''{n}Her face falls, very slightly, and then rearranges itself into understanding, which is harder to watch.{/n}
"Close. Yes. That's all right." {n}She reaches out and pats the pocket, through the cloth.{/n} "It works from there too. Luck isn't vain."
"...I am, a bit." {n}A small, honest smile.{/n} "I wanted them to see it. I wanted everyone to know. That's not luck, that's just me. You can have that one for free."''',
      c("[Kiss her.]")),
], requires=(MORNING,), forbids=(RIBBON,))


# --- 11. Sharing. ------------------------------------------------------------------------------------------------------

fortune(SHARING, "Sharing", '"Something\'s on your mind."', [
    ch("start", '''"Eritrice says you are over-committed." {n}She says it lightly, plucking at a cushion.{/n} "She says it as if it were a motion out of order. Socothbenoth says it as if it were a joke. Alichino says it as if it were a price: the whole crusade holds a mortgage on you, he says, and I'm a very late creditor."
"They're right about the numbers. Every one of them." {n}She looks up.{/n} "I don't care about the numbers."''',
      c('"Then what\'s on your mind?"', "mind")),
    ch("mind", '''{n}She hesitates, and the hesitation goes on for long enough that you understand it is serious.{/n}
"I don't want to be last." {n}Small, and very clear.{/n} "Not first. I don't need first. First is for people who count. I just don't want to be the one you come to when there's nothing left of you. The crumbs at the bottom of the parcel."
{n}Her fingers have stopped on the cushion.{/n} "Is that selfish? It feels selfish. I've never wanted anything for myself before. I don't know how to tell."''',
      c('"It isn\'t selfish. You won\'t be last."', "not_last", flags=(NOT_LAST,)),
      c('"Sometimes you will be. The war takes most of me."', "war")),
    ch("not_last", '''"Promise?" {n}The little finger, again.{/n}
{n}You link it. She holds on a while, and her face is very serious, and then it breaks into the brightest smile you have ever seen on it.{/n}
"There. I asked for something for me, and I got it. Oh, that's frightening. That's so much more frightening than luck." {n}She flops back onto the cushions.{/n} "I'm going to do it again. Not often. Just sometimes. To see if I like it."''',
      c("[Lie down beside her.]")),
    ch("war", '''{n}She takes that, and turns it over, the way she turns her ring.{/n}
"Then I'll share with the war too. It can have the most of you. I'll have the best of you." {n}Firmly.{/n} "That's a different thing. The war doesn't know how to tell the difference, and I do."
"Just come to me before you're all crumbs. That's all. Leave one whole cookie in the parcel. For me."''',
      c('"One whole cookie. Always."', "not_last", flags=(NOT_LAST,))),
], requires=(NIGHT,), forbids=(SHARING,))


# --- 12. Paid back: the borrowed luck. ---------------------------------------------------------------------------------

fortune(REPAID, "Paid back", '"You said you always pay back."', [
    ch("start", '''"I do." {n}She sits up very straight and folds her hands on the table, and for once she is every inch the patron whose priests keep her accounts in three temples.{/n} "The day of the coin I borrowed some of your luck and spent it on the Council. On believing."''',
      c("Continue", "owed", requires=(LUCK_OWED,)),
      c("Continue", "lent", requires=(LUCK_LENT,), forbids=(LUCK_OWED,)),
      c("Continue", "lent", forbids=(LUCK_LENT, LUCK_OWED))),
    ch("owed", '''"You said you'd want it back. With interest." {n}She opens her hand. There is nothing in it, and then, somehow, there is a feeling in the air, like the moment before a coin lands.{/n}
"I've been saving it. A little every morning, from the good thoughts I'd have sent the Council. It's all here. With interest." {n}She closes your fingers over her empty palm.{/n}
"Don't spend it on anything silly. Spend it on something you can't make happen yourself. You've got so few of those."''',
      c('"I\'ll save it for the Wound."', "wound"),
      c('"Then I\'ll spend it on you."', "on_you")),
    ch("lent", '''"You said keep it. Bet it on you." {n}She smiles, slow and sly.{/n}
"So I did. Every morning. I've been betting your own luck on you for months, and winning, and betting the winnings again." {n}She wiggles her fingers.{/n}
"You have no idea how much luck you've got now. Neither have I. I lost count. I'm going to keep it for you, invested, until the day you really need it, and then I'm going to give you all of it at once."''',
      c('"When?"', "when")),
    ch("wound", '''"The Wound." {n}She nods, solemn.{/n} "Yes. That's the right place. That's where nobody can make anything happen, not even you."
"When you're standing there, and it's going badly, and you've run out of tricks, feel for it. It'll be there. I'll be there."''',
      c("[Hold her hand closed over nothing.]")),
    ch("on_you", '''{n}She laughs, and swats your arm.{/n} "You can't spend my luck on me! It's circular! Eritrice would have a fit."
{n}Then she stops laughing.{/n} "...You'd really do that? Spend your one bit of luck you can't make yourself, on me?" {n}She leans her forehead against yours.{/n} "Silly lucky charm. Keep it for the Wound. I'll be there anyway."''',
      c("[Keep it for the Wound.]")),
    ch("when", '''"When you've run out of everything else." {n}She says it gently.{/n}
"At the Wound, I think. When you're standing there and all your tricks are used up. You'll feel for it and it'll be there, all of it, everything I've won with it." {n}She taps your chest.{/n} "You won't know it's me. That's fine. I'll know."''',
      c("[Believe her.]")),
], requires=(COMMITTED,), forbids=(REPAID,), delay=48)


# --- Epilogue paragraphs on the committed page (chadali.trickster.epilogue.lucky_night). ------------------------------

EPILOGUE_PARAGRAPHS = [
    (PROMISED_SAFE, "{n}She kept, in the drawer where she kept her ribbons, a note in the Commander's hand from the week of the cauldron: \"Nobody takes it by force.\" She never needed to show it to anyone. She liked to read it anyway.{/n}"),
    (HELD_AFTER, "{n}Every time the Commander came to her, for the rest of their life, the first thing the Commander asked was \"Is it growing?\" and every time she said yes. By the end, it was true.{/n}"),
    (SAW_THE_FAIR, "{n}Her fair was built, in the end, at the edge of what had been the Wound: acrobats, lollipops, and a three-headed puppy that ate nobody. There was a devil's stall. It sold lollipops. Chadali watched it herself, every day, with a very big one.{/n}"),
    (FORGAVE_MEAN, "{n}She was mean to the Commander twice more in all their years together, and both times, before the Commander could say anything, she said, \"You went first,\" and the Commander laughed, and it was over.{/n}"),
    (NO_MORE_RIGGING, "{n}Her priests in Drezen had ordinary luck after that, good months and bad. The Commander mended their roof once more, openly, with a sign. She kept the sign.{/n}"),
    (KEPT_RIGGING, "{n}When her priests went hungry the Commander fed them, with the crusade's stamp on every sack, and she never once complained about it, and once she was seen kissing a sack.{/n}"),
    (ELYSIUM_PROMISED, "{n}The Commander saw the meadows, in the end, and sat in the river, and was fed cookies until they stopped looking at the horizon. It took three years. She had said it might.{/n}"),
    (RIBBON_WORN, "{n}A yellow ribbon hung from the Commander's sword-hilt through every battle that remained. By the war's end half the army wore one, and nobody could remember whose idea it had been.{/n}"),
    (RIBBON_POCKETED, "{n}The yellow ribbon never left the Commander's pocket. She knew it was there. She said that was better, really, and did not quite mean it, and did not mind.{/n}"),
    (NOT_LAST, "{n}There was always one whole cookie left at the bottom of the parcel. Always. She checked.{/n}"),
]


def integrate(payload):
    """Bind this module's own reads, and give the committed page the fortunes' consequences."""
    from story_format import p
    for key, cues in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != cues:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["chadali.trickster.epilogue.lucky_night"]["Nodes"][0]
    page.setdefault("Paragraphs", []).extend(p(text, requires=(flag,)) for flag, text in EPILOGUE_PARAGRAPHS)
