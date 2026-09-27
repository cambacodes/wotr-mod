# Nurah read-only contact evidence

This is an independently reviewed schema and policy change, not Nurah route integration.
The preceding goal turn added reviewed observer code, optional ending attachment and a portrait candidate, so it counts as progress.

The meeting contract defines `nurah.correspondence_available` and `nurah.meeting_arrived` as observations of runtime state.
Root added these keys to the existing derived-contact sets and native-state predicate in `src/Story.cs`.
Story choices, scene completion, relationship progress and aliases to native flags must not manufacture either observation.
The runtime observer remains responsible for producing them; Main does not yet do so.

Before the change, the new focused test failed with `Nurah observation is not checked as live state`.
Afterward the complete Rules runner passed 27,527,097 assertions against the unchanged 612-scene export.
The thirty new assertions use small schema fixtures, not the unapproved Nurah manuscript or a simulated native arrival.
They check missing and present observations, removal of live evidence, the separate actual-contact requirement, and rejection of forged observations through authored effects, scene IDs, relationship progress and all six native-binding collections.

| Input | SHA-256 |
| --- | --- |
| Story.cs | D1CBEEAEF3C79E58BE943ED8875434B5F7120FBB589A10CFE2F352B02714F843 |
| NurahContactEvidenceTests.cs | 046633376BA07019AABE5C2A3F8F8B78602C6AE88F81BD1A0A276A8426BB0A2D |
| Rules Program.cs | FA72ABF25715A809F00455868A3087955814FBA28ED5FCBEA563E664F182F791 |

The independent report `reference/parallel/nurah-contact-evidence-independent-review.md` grants a scoped pass after forty isolated assertions and a reproduced failing live-state mutant.
Its extra cases cover closed and committed relationship forgery and grouped prerequisite removal.
Actual Nurah manuscript traversal, parent acquisition, native dialogue entry, physical placement, save/load and ToyBox execution are separate unfinished work.
No installed files changed.
