# Voice pack: Areelu Vorlesh

Binding: `handoffs/CHARACTER-TRUTH.md`. Evidence: `plans/edge-audit.md` §7; `plans/edge-fix-design.md` §3.5. Architect of the Worldwound, a Sarkorian witch grafted to the Abyss, the Commander's maker. Keys checked against enGB.

## Native lines (enGB)
- `9d626d22`: "Regret poisons the will and the mind. I've long since forgotten what regret feels like."
- `6bf6939c`: "I will not regret what I did. Not for a moment."
- `670f8e52`: she gives a condescending look, "as if you were a child throwing a tantrum." "How very mortal of you!"
- `4489282b`: "I'm interested in neither praise nor reproach... Keep your adulation to yourself."
- `f644c7d2`: "Loyalty is for fools. Shared interest — that is what rational minds rely upon. That, and fear."
- `45ce19b9`: "You are my creation. Your power was my gift."
- `fb3a79c7`: "Betrayal is too strong a word. I opened the path to Golarion for those two... That will suffice."

## In-house targets (Trickster)
- `areelu.trickster.lens.watched:alive`: "A vessel that breaks too early is useless. You wanted me to say something softer. I do not have anything softer."
- `areelu.trickster.rift.odds:romantic`: "Every hour I spend on you is an hour I do not spend on my child. I resent the expense. I have not yet decided to stop paying it."
- `areelu.trickster.wager.struck:terms`: "It was my mistake. I do not leave my mistakes to strangers."
- `areelu.trickster.wager.at_threshold:name`: "that is the only mercy I am prepared to show you. Take the terms, or leave them."
- `areelu.trickster.report.cult:sold` (narration): "You took their gold and I took their lives... You undercharged."
- `areelu.trickster.report.sarkoris:sorry` (narration): "I am not sorry. I would do it again, and I would do it better."

## Appetite, cravings, agenda
- **Appetite:** knowledge won through experiment (`4166d46e`), and the elegance of a working.
- **Craves:** her child's soul. Canon has a child's soul in a vessel (`dbef5f8d`), and her "single, deeply personal purpose" (`4489282b`). She craves to beat death and the gods.
- **Agenda:** the Second Opening and the rift (`7b577417`). She serves only shared interest: she sold Baphomet and Deskari the crystals (`fb3a79c7`) and belongs to Nocticula (`b5556dcf`).
- **Strengths:**
  - Soul-grafting (`c9641cfd`, `070103a5`); souls into vessels (`dbef5f8d`); decades of patience; self-command.
- **Weaknesses:**
  - Her child; her mortal birth (`fd411a8f`); contempt that underestimates love; Threshold's hunters (`3f42bec4`).

## Cruelty, humiliation, desire, power
- **Cruelty is clinical,** and comes without anger:
  - demons "simply sewn together", demon limbs grafted onto people (`15dcff70`);
  - a burned witch kept for her blood (`93676605`);
  - an angel kept in her laboratory (`320f6703`, `db0ba6c5`).
- **Humiliation is condescension:** "How very mortal of you!" The Commander is a child or an experiment.
- **Desire is attention:** she watches, measures and keeps notes ("Yes, I have been watching. You should know that by now," `areelu.trickster.rivalry.lens:reply`). Wanting is an expense she resents.
- **Power is authorship.** She made the Commander, and states terms instead of arguing.

## Mouth
- **Profanity: zero (prim).** Even "damned" is rare.
- **Her edge:** contempt, short declaratives, refusal of comfort. She uses technical words of her craft (vessel, graft, essence, working). She never uses words from a clinic or an accountant.
- **Example register:** "The convict lasted nine days. The last three were the useful ones. Fund the next batch, Commander, or stop reading my notes."

## She never says
- "Is that what you want? Not what you're measuring. What you want."
- "Write that down: I have not killed anyone." That is the sobriety-witness frame.
- A renunciation of the dagger.
- "Opening the door is still your choice."
- Anything about restitution, healing the world, or reading victims' names all night, outside the native redeemed ending (`590bcea2`).
- That she is afraid, except in a single earned cellar beat.
- A request for forgiveness, or for praise.

## Canon guardrails
- **Origins:** a Sarkorian witch hunted by Threshold (`3f42bec4`, `42f8731c`); her old laboratory (`520837ab`).
- **Her makings:** she made the Commander's power from a Nahyndrian crystal (`fff1eebb`, `de996400`). The Deskari dagger (`72bb0cc4`).
- **Softening is gated:**
  - Atonement only under `Ending_AreeluRedeemed` (`590bcea2`).
  - Company only under `TE_AscendAreelu` (`7b429f6b`): "every moment is priceless if it is spent with the one who matters most to you."
  - The Trickster wager earns company. It does not earn restitution.
- **Report pages:** pay Pharasma the minimum and keep the best vessels ("I intend to keep what I spent so long making"). Add two or three entries that show her still at work: paid experiments on convicts, a graft project the Commander funds, a rival scholar ruined.

## DO NOT INVENT
- Her child's name, age or story beyond "the soul of a child" (`dbef5f8d`). A husband.
- Sarkorian victims' rolls on page (the penance tour). New Pharasma theology.
- Remorse outside `590bcea2`. Opon beyond `279401c8` and `4bef4509`.

## Falling for the Commander
She falls for her best work. The Commander is the one experiment that answered back and was right.

What she does:
- Keeps the Commander under observation and calls it company.
- Pays for the Commander in hours she resents ("I resent the expense").
- Says something soft at most once per act, then takes it back with a term.
- Offers love as a share in her work, and keeps her vessels.

What does not change:
- No regret and no penance. She is still doing it in every epilogue.
- "Do not mistake that for sentiment."
