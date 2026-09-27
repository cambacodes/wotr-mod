# Devarra partnership and missed-cart development

This is an author handoff for independent review.
It does not approve the prose, certify the timing repair in Unity or declare the route complete.

Frozen progression SHA-256: `3FB5F4425E94412399F3AA310859EB66B34EF22203F25E4A7766C57429C2F206`.
The unchanged opening remains `E8BA4C20B2AF06ADC733E2AAA636F1123249AF583206F8C2908531B055833455`.
Only `storylines/devarra_trickster_progression.py` and this report were edited for this task.

## Timing defect and repair

Before editing, I reproduced the reviewed failure using the actual retry predicates and the engine's minimum-delay rule.
With matching history and retreat prerequisites, the old retry was available after 1, 24 and 168 hours.
Its first page still described an approaching cart one hour after withdrawal at every tested interval.
The source cannot be exercised as a real player encounter because it is unregistered and its actor and custom state producers do not exist.
That source traversal was the closest available reproduction; no live E2E run is claimed.

The supported `Scene` schema has a minimum `DelayHours`, but no maximum time window.
I did not introduce a fictional expiry field or modify shared engine files outside this task's ownership.
Instead, withdrawal now commits the player to a missed opening.
The cart leaves when the hour ends, taking the prisoners, Serevin and her ledger away from the original kiln.
The original scene remains blocked by retreat history.
The later scene always starts after that departure, even if the player waits several days to select it.

The delayed return follows the workers to a quarry sorting shed through a weighhouse record.
They are held there as labor, rather than riding in a cart which inexplicably waits for the player.
A one-shot Perception check identifies the correct shed; failure leads through a warned overseer and a worker injured during the harder rescue.
Neither result captures Serevin or obtains her ledger.
Both leave the lower vault warned and preserve the missed-departure consequence.
Abandoning the search deliberately leaves the rescue and route unfinished.

The return uses the existing `KILN_TRIED` attempt flag for this new inspection and retains the minimum one-hour delay.
It no longer replays the original receipt trap, lamp inspection or capture branch.
Only Vey's settlement and the later evening are shared with the original kiln continuation.
The shared departure page is replaced in the copied return template so it describes the sorting-shed rescue and return by the orchard, rather than breaking lamps which have already been removed.
The opening and entry wording need independent review for how clearly they communicate that choosing retreat forfeits the original meeting.

## Partnership continuation

Five new main scenes follow the rooftop invitation.

| Scene | Required milestone | Resulting milestone |
|---|---|---|
| `the_house_above_the_road` | `vault_evening_complete` and `home_inspection_planned` | `ledge_inspected` |
| `the_man_who_owned_the_rain` | `ledge_inspected` | `ledge_claim_heard` |
| `the_weight_of_the_wall` | `ledge_claim_heard` | `ledge_storm_ended` |
| `a_roof_is_not_a_rein` | `ledge_storm_ended` | `ledge_settled` |
| `what_she_comes_back_for` | `ledge_settled` | `partnership_chosen`, or refusal |

All IDs and flags use the `devarra.trickster.` prefix.
The weather-and-repair scene has zero additional minimum delay after preparation.
The others use 24, 12, 24 and 24 hours respectively.
None introduces a further fixed expiry which those fields cannot enforce.

The desired western platform sits above occupied rooms and a blocked drainage channel.
Mareth, Oren, Talvren and Iven are authored adult characters.
Their household, mill right, documents and repairs are authored developments, not unused native quests or claims about canon NPCs.

The earlier inquiry, force and visits-only intentions select different arrival passages.
Devarra wants the ledge and objects to being treated as a solution somebody else can own.
The Commander can investigate the estate's claim, obtain payment by intimidation, or prepare a Trickster delivery using the owner's stated claim to the obstructing stones.
The prepared intervention needs a named empty receiving yard, marked stones and an opened outlet.
Its Arcana failure leaves ordinary work, a broken tool and additional strain on Devarra holding the wall.
The hand-work alternative remains available without a roll or mythic shortcut.

The claim check uses supported `SkillKnowledgeWorld`, DC 34.
The prepared delivery uses `SkillKnowledgeArcana`, DC 35.
Both are Commander-only and set their attempt flags before the result.
They affect evidence and repair consequences, not consent or attraction.

The settlement reads the earlier success, disputed claim, coercive payment or prepared-delivery history.
Talvren offers a home with an expandable military-service clause.
Devarra refuses to let the house become a claim on her future enemies.
The player can support a fixed purchase, an openly disputed seizure or leaving the ledge behind.
The tenants' lodging is separated first so that they are not held hostage to a romantic answer.
The coercive choice remains coercive, and claiming the platform does not declare its surviving ownership dispute resolved.

The final conversation reads the home result and kept-versus-destroyed targeting-map history.
It offers a deliberate partnership, separate lives with continued romance, or ending courtship without erasing practical consequences.
An accepted future does not require kissing or staying that night.
The farewell has distinct close, quiet and immediate-departure terminals.
The dialogue explicitly permits other lovers and requires discussion of conflicting promises rather than exclusivity or jealousy flags.
No other route's history is changed.

## Recollections and delivery

Two new `Epilogue` templates recall the chosen partnership or separate-lives arrangement.
They describe an earlier evening and leave the crusade's actual outcome to native decisions.
They do not restore a clutch, guarantee survival, assign a new household actor or replace a native ending.
They remain unregistered supplementary recollections, not working native ending integration.
No altered-history Aeon recollection, native ending suppression or live once-only delivery is supplied by this draft.

There are now fourteen main progression templates, one delayed-return template and two recollection templates.
Each has two exact-history delivery variants, giving thirty-four progression definitions.
The separate opening still has its two variants.
These duplicates are delivery guards and receive no extra content credit.

The history-variant builder still supplies readable interaction labels and starts from the intended `Nodes[0]`.
Recollections are remote and require no physical contact actor.
Other variants retain the proposed physical Devarra contact.
The old opening relationship's commitment metadata has not been rewritten; registration work must distinguish early courtship from the new `partnership_chosen` milestone.

## Selected length

A separate carried-state solver traversed the matching opening and every available main progression scene from `Nodes[0]`.
It applies scene and choice requirements, forbids, requirement groups and effects; explores both skill outcomes; excludes refused and closed results; and visits the delayed return only after the corresponding retreat.
It counts one selected recollection using `tools/measure-story-content.py` normalization and tokenization.
Minimum and maximum prefixes are merged only when equivalent under future predicates.
It assumes the current Trickster path, available actor and positively verified native history, rather than demonstrating acquisition.

| Completed current draft with one recollection | Saved brood | Lost clutch |
|---|---:|---:|
| Minimum with direct kiln progression | 14,107 | 14,148 |
| Minimum allowing the missed-cart route | 14,053 | 14,094 |
| Maximum, direct or allowing missed-cart route | 19,714 | 19,714 |

The longest witness chooses the direct kiln progression.
The new five-scene arc and one recollection contribute 4,547 selected words on that witness.
The result does not add both recollections, both brood variants, failed and successful rolls, or the original kiln encounter again after retreat.
Allowing the missed-cart route slightly lowers the minimum because its different rescue can be shorter than a direct outcome.
It is not used to inflate a maximum with repeated inspection text.

The shortest completed manuscript remains 6,947 words below 21,000.
Even the maximum remains 1,286 words below that floor.
Further meaningful continuation is required; these figures do not establish the project's quantity gate or independent literary quality.

## Checks and remaining work

`python -m storylines.devarra_trickster_progression`, compilation and whitespace checks pass.
The module validates targets, cycles, narration tags, supported attempt patterns, exact-history delivery and carried continuation outcomes through the new partnership choice.
Additional source checks cover home-result callbacks, mutually exclusive recollections, refusal blocking, nonphysical farewell terminals and the impossibility of obtaining Serevin or her ledger from the delayed rescue.
At 1, 24 and 168 elapsed hours the delayed scene still opens, but now truthfully opens after the departure at all three times.

No full C# suite was run against a regenerated export, and no shared export was changed.
There is no Unity, save, ToyBox or headless actor-delivery result from this task.
Damage, custody, money, property, drainage and repairs remain narrated consequences with custom history flags, not implemented world mutations.
The body remains a dragon throughout; no humanoid transformation or image assignment was added.

Independent review must assess the missed-opportunity communication, its destination rescue, the chronology of repairs and correspondence, the estate conflict's character credibility, and whether the partnership develops enough beyond another argument about ownership.
The separate native brood histories remain intact, but acquisition, resurrection, DLC-to-campaign continuity and actor persistence remain unresolved.
The larger retained-map threat, possible exposed buyers and taken-platform dispute are not claimed as completed quests.
The route needs further content, a broader ending design and runtime integration before readiness review.
