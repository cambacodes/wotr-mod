# Native skill-check integration

The parent implemented initial native skill-check construction in `src/Main.cs`, with schema and validation in `src/Story.cs`.
`story_format.c` now accepts an optional `check` object.
No authored romance encounter in the main development export uses it yet.
Independent technical review and actual Unity execution remain pending.

## Authoring contract

Example: `c('[Look for the concealed mark.]', check=dict(Skill="SkillPerception", DC=25, Success="found", Failure="missed", CommanderOnly=True))`.
The success and failure fields name distinct nodes in the same scene.
A check choice cannot also specify Next, Abort or Revive.
Success and failure pages must each offer a playable continuation; failure does not inherently close the relationship.
The choice may record a decision before the roll, but outcome-specific flags belong on the corresponding outcome branch.
Selecting the check does not complete the scene.
Existing scenes and choice indices must be retained when adding checks to delivered content.
Difficulty must be justified against the chapter and encounter, not copied from this mechanical fixture.

The supported skills are Athletics, Mobility, Stealth, Trickery (`SkillThievery`), Knowledge Arcana, Knowledge World, Lore Nature, Lore Religion, Perception, Use Magic Device, Diplomacy, Bluff and Intimidation.
Use the exact native StatType names listed in `Rules.CheckSkills`.
Generic SkillPersuasion is rejected because the native BlueprintCheck validator calls for a specific persuasion mode.
CommanderOnly defaults to true and supplies a PlayerCharacter evaluator while disabling party substitution in camp.
False leaves actor selection to the native dialogue controller; it does not guarantee that the entire party rolls, because the native controller may have an ActingUnit.
Checks are visible and award no experience in this initial implementation, avoiding unintended repeatable experience from optional courtship activities.
The native game has no-experience romance-check examples; encounter-specific experience rewards are not currently supported by this schema.

## Native evidence

`reference/canon-review/native-romance-check-examples.json` contains extracted original-game checks, including Camellia, Arueshalae and Sosiel scenes.
The male companion examples are mechanical reference only and do not add candidates to the female roster.
`reference/game-BlueprintCheck.cs` and `reference/game-DialogController.cs` provide the installed API and native execution path.
PlayCheck uses native RuleStatCheck or RulePartyStatCheck, records the result and dispatches the success or failure cue.
The expansion constructs those native objects instead of implementing its own random number generator or success calculation.
Whether the intended DC/skill preview appears correctly in the actual book UI remains under review.

## Verification checkpoint

The production DLL built without warnings or errors.
DLL SHA256 is `033D97FA8ABCF9D2F0C069905878F06D88937FF967F7E8C679D926B53CDE798F`.
The staged Konomi letter review story passed 2,252,431 rules assertions with the new skill-check contract tests.
`managed-tests/write-check-fixture.py` generates an isolated 175-scene mechanical fixture from the unchanged main development export.
It adds 26 checks covering all 13 supported native stats and both actor-selection policies.
The fixture SHA256 is `81D1C22868F169B9FD5C15C205226016218BE0D2176BA38867B3B45A5406B985`.
Managed construction passed 18,029 assertions over 5,479 generated blueprints, including exact native check types, DCs, success/failure references, actor policy and absence of premature scene completion.
Rule graph traversal explores both possible results; it does not simulate native probabilities or prove dice execution.
No installed mod files were changed.
Do not credit these fixtures as authored story content or as proof of in-game skill-roll, save or ToyBox behavior.

## Corrections after independent technical review

Native answer UI derives the check preview from BlueprintCheck in NextCue; ShowCheck must retain its empty default because it is a separate visibility roll.
The parent added continuation conditions on the check cue itself, because a stale answer selection can proceed to its next cue even if the action refuses to record effects.
The guard uses contact eligibility rather than reapplying authored choice forbids after attempt flags may have changed.
Validation now rejects checks on Epilogue and AeonEpilogue scenes, whose builder intentionally creates a plain Continue answer.
The revised fixture includes contact-gated checks and verifies their cue-level conditions.
The revised DLL SHA256 is `44AC3111E4D5625C472773665477C69E701B78BC23CC90E249F73FCD25915461`.
The revised fixture SHA256 is `A3B81E3D912A17F6C48268F08BF29711833A8FD89356CB24CB07B2D70624FC7E`.
Managed construction passed 18,067 assertions over 5,482 generated blueprints; rules against the Konomi letter review story passed 2,252,433 assertions.
Native cue scheduling still introduces a timing boundary between selection and later execution; actual game interruption and save behavior require runtime verification.
