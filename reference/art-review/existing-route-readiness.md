# Existing-route readiness audit

The retroactive full-route requirement is not satisfied by any currently inventoried character arc.
Every measured relationship group is below the provisional 21,000-word floor even before evaluating meaningfulness, reachability, or individual character ownership.
This is a focused evidence audit, not a fresh review of all writing.

## Inputs and independent verification

The actual `development/Story.json` SHA-256 is `52E0A3418B3BE3CA7AC754829751083D94978C7A8D31D3322C1C468A2573E48E`.
It exactly matches `development/content-volume-inventory.json` at the time of this review.
I independently read the story, collected each node's prose and choice text by relationship, and reproduced every raw and exact normalized-segment word count without running the inventory generator.
The inventory has 117 scenes across six relationship groups.
It correctly leaves integrated external words and attainable playthrough words null and marks every group `full_route_approved: false`.

The tokenizer removes brace and angle markup, normalizes whitespace, and counts Unicode alphanumeric words with internal apostrophes retained.
Hyphens split words and underscores do not count.
Exact distinct segments remove only identical whole normalized strings.
Repeated sentences inside different paragraphs, paraphrased repetition, generic choice padding, mutually exclusive branches and inaccessible scenes can all remain in the distinct-segment count.
Consequently, neither raw nor distinct-segment words establish meaningful attainable content.

## Per-route verdict

| Resulting character or relationship | Scenes | Raw words | Distinct-segment words | Raw gap to 21,000 | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| Anevia, within shared Tirabade | 34 shared | 15,912 shared | 15,849 shared | At least 5,088 before individual attribution | Unapproved; shared text is below one character's floor and individual ownership is unresolved. |
| Irabeth, within shared Tirabade | 34 shared | 15,912 shared | 15,849 shared | At least 5,088 before individual attribution | Unapproved; these are the same shared words, not a second independent route inventory. |
| Seelah | 25 | 7,969 | 7,580 | 13,031 | Unapproved; authored volume falls short and any native-content credit remains unmeasured. |
| Konomi | 20 | 6,016 | 6,010 | 14,984 | Unapproved; authored volume falls short of the full-route requirement. |
| Jerribeth | 18 | 4,710 | 4,699 | 16,290 | Unapproved; authored volume falls short of the full-route requirement. |
| Kiana | 17 | 3,927 | 3,909 | 17,073 | Unapproved; authored volume falls short of the full-route requirement. |
| Ember friendship | 3 | 1,168 | 1,163 | 19,832 | Unapproved; this is an opening, not a completed friendship arc. |

The gaps are arithmetic raw-word deficits, not instructions to add that many filler words or estimates of the final meaningful-content deficit.
The Tirabade rows deliberately display the same joint total twice to expose the ownership problem; they must never be summed as two independent bodies of writing.
Joint scenes can develop both women, but that requires an explicit account of each woman's agency, choices, consequences and sustained arc.
No automatic full credit to both women or automatic fifty-fifty allocation is justified by this inventory.
Aivu and other roster characters absent from the inventory have no authored-volume evidence here and remain unapproved; their absence does not prove there is no relevant native content.

## Installed Tirabade versus development

I separately inspected `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/Mods/RanRomanceTirabade/Story.json`.
Its SHA-256 is `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4`.
Its 34 scene objects are structurally identical to the 34 Tirabade scene objects in the reviewed development story.
An independent installed-story count gives the same 15,912 raw words and 15,849 distinct-segment words.
The installed `RanRomance.Tirabade.dll` SHA-256 is `E44115E37170946318CA3BAF1A3BE03CAD65C09318E305313481A43C55AD0F50`.
The installed baseline and development expansion are therefore distinct deliverables, even though the baseline story is included in development.
Development construction tests or newly reviewed scenes do not establish that expansion behavior is installed.
Conversely, the baseline's prior delivery status does not exempt Anevia and Irabeth from the user's new retroactive content and quality requirement.
This inspection makes no fresh claim about installed gameplay functioning.

## Benchmark limits and missing evidence

`reference/art-review/ran-route-word-inventory.json` maps the largest RanRomance initializer, Targona, to 19,004 keyed words or 18,359 exact normalized-text deduplicated words.
Another 1,138 configured helper words and 218 words outside the loader walk remain individually unallocated.
The deliberately overinclusive largest-initializer-plus-all-unallocated envelope is 20,360 words, supporting the provisional 21,000-word planning floor recorded in `ROSTER.md`.
It is not an actual completed Targona route attribution or a single-playthrough benchmark.
RanRomance source counts include referenced titles and journal text, while this development inventory excludes those categories.
The tokenizer is comparable, but the counted content categories are not identical.
The final comparison needs a matched content scope, helper ownership, branch exclusions and meaningful route content rather than an unsupported equality between these totals.

Each resulting arc still needs a scene-level account of character-owned development, meaningful repetition handling, attainable progression and endings, and any specifically integrated native or RanRomance text claimed toward the floor.
External content cannot receive credit merely because the character has dialogue elsewhere in the base game.
Credit requires evidence that the material is actually available, relevant and integrated into the resulting arc under the intended route conditions.
Exceptional Trickster access, route-specific restrictions, ToyBox compatibility and contact/restoration behavior remain separate gates from length and writing quality.
The present inventory does not establish any of those gates.

Earlier writing and canon scores apply only to the named source revision and reviewed passages or scene set.
An above-90 score on an opening or a short campaign draft cannot be promoted into approval of a complete 21,000-word character route.
Source-art scores similarly cover only observable illustration criteria and do not approve crops, runtime presentation, writing or the full character campaign.
Construction and rule tests can support specific implemented behavior but cannot establish prose quality or turn an incomplete arc into a complete one.
Full-route approval requires the completed revision to meet the content floor and receive a new scope-appropriate quality review, with critical defects resolved regardless of numerical score.
