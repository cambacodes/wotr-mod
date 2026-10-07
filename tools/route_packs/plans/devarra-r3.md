# Devarra round 3 — authored audit corrections

Scope: `judging/codex/devarrar2.json`, checked against merge-e source before
editing. This sheet supersedes the round-2 planning deferral of the conqueror
ending and canon-fate page: the round-3 audit explicitly requires them.

## Canon and authored boundary

Read-only verification in `/wrath/blueprints.zip` and native `enGB.json`:

- `StoryTellerAndDragonGoodEnter/Cue_0002`,
  `546738b439bbf064b9dc7499fde143dc`: her predatory appetite and story tariff.
- `Golems_DragonEggs/Cue_0001`, `b8dfb42d03fc931409f2b80614cfa9de`:
  the constructs threaten her eggs under Xanthir's orders, even after her death.
- `KTC_StorytellerIsBack/Cue_0021`, `9fee959d1db05f24b9f8206fbebc3ed8`:
  the Storyteller does not pity her. No sympathetic mourning is invented.
- `RedDragonDead`, `581521b398fb9dd4eb52bbfffb3b5c43`, and
  `RedDragonKilledInIvorySanctum`, `056ba61e04cca104a9c95ac2d4658c67`:
  select the native-death location; returned histories exclude this page.

The existing flight, watchtower, messages and courtship remain authored
additions. New authored situations: her rejection of a proposed new leash;
the Commander returning after 48 hours with a corrected ending; her late
proposal outside Drezen's north gate before Threshold; retrospective pending
and rejected-judgment pages. No new powers, lore, resource prices, affection
checks, native-event changes, partners, Shyka events or echo slots are added.

## Turning point and consequences

Tithe submits a story; it establishes neither romance nor household eligibility.
The existing early verdict still offers the same terms and choices. A conqueror
submission appends at index 3 and receives her own refusal at verdict index 4.
The pending claim and refusal block ridge payoffs until the correction is
answered. The correction preserves the early terms' answer order, tariff and
hard refusal/postponement outcomes; a dead Storyteller has the remote twin.

An otherwise unfinished negotiation gets `after.late_proposal` in Chapter 5,
while the Commander can still meet her outside Drezen, before the final march:
she blocks the supply road, states the existing tower/egg/annual-bite terms, and demands an
answer. Accept sets `devarra.committed`, the existing bite debt and the new
`devarra.trickster.late_accepted` receipt. Refuse closes; delay leaves her hungry.
`devarra.outcome.late_accepted` reads that receipt and commitment together;
the shared contract assembler preserves this route-local outcome guard in
`late_committed`. No fate gate substitutes for her offer or the selected yes.

The accepted late epilogue recalls that played bargain. Its merged proposal
choices remain at their original indices and are retired by gating; its saved
nodes and effect-free exit remain. The standard committed page excludes the
late receipt to avoid duplicate primary endings. A skipped proposal gets the
uncommitted pending page. Outstanding egg claims remain separate from romance.

## Class repairs

- All ridge scenes and the named late/Last Call consumers guard unresolved
  conqueror judgments; the corrected account supplies the override.
- Refused ending remembers stair marks only after an actual first climb.
- Vault entry and cook collection dispatch separately to a public-roof wager;
  both remain meaningful after her earlier private entry.
- Both battle branches keep the legacy `one_battle_sold` effect. Only explicit
  agreement supplies `battle_price_accepted`; the asking branch supplies
  `battle_offered` and receives its own consequence paragraph.
- All native-death location/clutch variants exclude returned Devarra. Egg-fate
  precedence matches the route's accumulated-history dispatch.

## Review and gates

Existing shared fixes verified: Last Call requires accepted ordinary partnership;
its called bill paragraph stages no arrival at Threshold; a refused creditor
has `trickster.lastcall.account.devarra`, which leaves the claim outstanding
without summoning a closed partner. These shared records were not edited.

`DevarraRoundThreeTests.cs` plays the campaign from before the pact with native
escape/golem/egg observations, then executes the relevant answers. Forks cover
skipped late proposal, acceptance/refusal/delay, early/visited refusal,
conqueror rejection/correction, both messengers, vault/cook entry through roof,
and voluntary/purchased battle. Existing broad prerequisite-injection checks
are explicitly labelled predicate fixtures.

Shared registry escalation: the six new scenes need classification in
`tools/departure_contracts.json`. Exact proposed entries are in
`tools/route_packs/devarra-r3-departure-additions.json`; the registry and lint
are outside this implementer's allowlist and remain untouched.

## Final quick gate

- `PYTHONHASHSEED=0 python expansion.py`: success, 3,854 scenes, generated only
  into a system-temporary checkout. Parent bindings matched build-expansion.
- Route Python tests: 14 passed. UTF-8 I/O check: passed.
- Save compatibility: 0 hard failures; existing CRLF/LF styles retained.
- `payoff_lint --strict`: 0 hard failures.
- `rrt_verify --strict --gate-only`: 0 hard failures. This runs all strict checks
  and defers only report-only world/budget analyses. The earlier default run
  was cancelled when the proposal timing changed, before a result was issued.
- `DevarraTricksterTests`: 3,488 assertions passed, including continuous campaign
  witnesses, 44 watchtower beats and 425 predicate-availability fixtures.
- `departure_lint --strict`: exactly 6 unclassified new scenes; the shared
  inventory additions above are escalated, not applied.
- The requested complete Python discovery and complete C# rules/progression
  commands were launched, then terminated by the host `/work/testguard.sh`.
  They are not reported as passing; the guard was not disabled or changed.

No game, harness, full mod build, independent scoring audit or commit was run.
All temporary exports, reports, checkout and dotnet outputs were removed.
