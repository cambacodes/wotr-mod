# Iomedae round 2 implementation

Branch: `claude/r2-iomedae`. Uncommitted, as requested.

## CHANGES

All added memories, sendings, platform encounters and vigil staging are authored R6 elaborations. Native evidence is cited in the copied set-piece sheet; the Herald outcome GUIDs, execution answer and court testimony were checked directly against `/wrath/blueprints.zip` and `enGB.json`. No canon partner is assigned to Iomedae; no partner stance, rival, echo, affection magic or replacement premise was introduced.

| File | Situation / findings addressed |
| --- | --- |
| `storylines/iomedae_banner.py` | S1: experienced cloak-burning knowledge gates the private disclosure; public Acts questions remain. Herald does not promise love or invent previous lovers. Abyssal longing remains separate from the counterfeit. P5 / F5; heat H1. |
| `storylines/iomedae_banner.py` | S2: Heaven audience, exile, unresolved heart restoration, mercy/fight and spite have separate responses. Spite requires owning cruelty and keeping it out of victory boasts; dismissal closes. The personal questions occur before commitment; a professional exit earns no courtship. Her chosen return, rather than rescue or war reports, supplies the personal receipt. P1–4 / F1–3; H2. |
| `storylines/iomedae_trickster.py`, `storylines/iomedae_banner.py` | S3: `courted` reads the completed personal exchange, or postponed concession plus the played eve answer. Every roof life-plan entrance and Threshold pickup is checked. No courtship leaves rescue available. Eve orders imagine hidden survival conditionally; the rest and recovery-night wording have no invented Iz tent, fixed interval or mandatory pre-Threshold camp. Dream kiss stays forceful; she keeps the waking-world invitation. P3–10 / F1–2,9,20–21; H3. |
| `storylines/iomedae_trickster.py` | S4: the key still dies; embodied power burns unconditionally. Anonymous H2 recovery no longer depends on Areelu's report. Rescue-only carries relic destruction or burned palm, mortality, divine liability and the same miracle obligation. Soul testimony is distinguished from returned bodily powers. P17,21–23,26 / F39; H4. The native final answers and their mechanics are untouched. |
| `storylines/iomedae_trickster.py` | S5: ordinary-survivor reunion invites the platform rather than summarizing a competing first night. Her plain-steel arrival carries actual open-Wound, madness or theft disagreement. Desire, reciprocal undressing and initiation lead to Slot A. Existing morning masks distinguish bridge burial, flask burial and public survival. Appended refusal goes to a clothed, nonsexual dawn. Seelah's existing presence-qualified reaction is a blunt, unsettled paladin response. P10–11,14–16 / F20–21; H5,H7. |
| `storylines/iomedae_trickster.py` | S6: familiar touch and an actual return survive the duty departure. The ninth-year dying-knight truth vigil collects the miracle in both bridge outcomes. Only the committed return offers Slot B; rescue receives no lover's reward. Madness care, theft, cathedral oath and the accountable Herald answer carry forward. Public-title, sock memorial, banner/flask and roof/rift recalls have history-specific variants. P12–17,26 / F20; H6. |
| `tests/test_iomedae_round2.py` | Six executable route tests: war-talk/argument-only negatives, both personal producers and professional refusals, Herald outcome/counter-move, private memory omission, slot/morning/refusal graph walks, both rescue cost and collection accounts, and unreturned-sacrifice negatives. All reached nodes must retain a selectable choice. |
| `tests/IomedaeTricksterTests.cs` | Existing positive romance fixtures now earn the personal exchange; epilogue audit locators follow the added variants. The frozen save baseline was not edited. |
| `tools/route_packs/plans/iomedae-setpieces.md`, `iomedae-tp.md` | Copied the requested planning inputs. The set-piece sheet supersedes the TP sheet's proposed pursuit registration. Implementation retains the fixed `another_character_intervenes` reservation: Drezen bare banner platform after the Threshold bridge and Pharasma's verdict; rescue judgment separate from the plain-steel private return and anonymous mortal's debt. |
| `tools/route_packs/explicit_slots/iomedae/*.json` | Copied both briefs unchanged. Nodes are `iomedae.trickster.epilogue.platform.explicit.1` and `iomedae.trickster.epilogue.after.explicit.1`; both ship the exact heated-cut defaults and final lines. No explicit prose was generated. |

The original terminal `epilogue.after/page` exit retains the explicit `continue` suffix, its empty effects and its unrestricted terminal mechanics; the new vigil option follows it. Existing scene/node order and old choice positions remain; new nodes and choices append. Existing source CRLF is preserved byte-for-byte as the newline convention.

## CLASS SWEEP

- Courtship producers and every entrance to roof/Threshold personal concession, including argument-only pickup; no kiss/rescue derives courtship.
- Herald heart restoration, Heaven, exile, mercy/fight and spite; no returned/exiled Herald attendee or free absolution.
- Optional Summit/roof/relic memories across objections, eve, dream, bridge, lived, respect and unanswered siblings. Already repaired F4,6–8,10–19 formulations were retained where applicable.
- True/fallback banner costs, both return families, power testimony/body distinction, public/buried identity, open rift/closed scar and actual banner/no-banner memories.
- First-night summary, every buckle path, all three mornings, refusal and later vigil; no duplicate first night, slot flags or rescue-only intimacy.
- Shared generated presence/flask/heroic readers inspected, but prohibited files and unrelated entries remain untouched.

## GATE

Every export, log, verifier report and .NET build artifact is placed in system temporary storage, then removed. `RRT_STORY_OUTPUT` and `RRT_TEST_STORY` redirect the export; lints, verifier and rules runner receive that same path. `PYTHONHASHSEED=0`, explicit UTF-8 and the build script's existing parent-binding manifest list are supplied.

- `PYTHONHASHSEED=0 python expansion.py` with temporary output: PASS, 3,755 scenes. Re-exported after the explicit legacy-exit suffix fix.
- `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io tests.test_iomedae_round2 -q`: PASS, 18 tests. The route-only/UTF-8 subset also passed independently (7 tests).
- `python tools/savecompat.py --story <temporary export>`: PASS, 0 hard failures. No baseline edit.
- `python tools/payoff_lint.py --strict --story <temporary export>`: PASS, 42 routes, 0 hard failures; only existing other-route REVIEW notices.
- `python tools/departure_lint.py --strict --story <temporary export>`: PASS, 43 women, 0 hard failures; existing Mielarah REVIEW notice.
- `dotnet build tests/RulesTests.csproj -c Release` with intermediate/output paths in system temporary storage: PASS, 0 errors; 8 existing DeliveryInventory2 CS0649 warnings.
- Temporary rules executable `--suites=IomedaeTricksterTests <temporary export>`: PASS, 166 assertions. The corrected spine actually plays the private questions before the roof; negative walks reject war-talk and argument-only commitment.
- Full `python -m unittest discover -s tests -p "test_*.py" -q` attempts terminated with exit 143 (SIGTERM), without a test-result summary. Full rules DLL and direct-executable runs likewise terminated before a summary. These are not recorded as passes. The `dotnet run` launcher initially expected `tests/bin` despite relocated build output, so the same compiled executable is used directly.
- The full strict verifier completed in 501.5 seconds: all mechanical/structural/native/presence/contract checks passed; one player-text hard finding matched “Commander in his” in a sentence about the canon's prayers. Reworded to “In prayer the canon still blamed the late Commander.” The full report had no Iomedae all-path-unreachable diagnostics.
- Final `python tools/rrt_verify.py --strict --gate-only --quiet --story <temporary export> --game /wrath`: PASS, **0 hard failures**. This rerun retained every strict check and deferred only report-only analyses already completed by the full run. Final savecompat/payoff/departure checks and the 166-assertion Iomedae suite also passed against this export.
- `git -c core.whitespace=cr-at-eol diff --check`: PASS. Both route sources and the existing C# test retain CRLF throughout. Only the requested route sources, tests and route-pack files changed. All task-owned temporary files were removed; no commit or generated development export was made.

## ESCALATE

These are outstanding union findings, not claimed fixes:

- P18–20 / F35–38: generated `crossroute.nocticula.unavailable` still gates the native Summit entry and historical Summit/eve sendings on Nocticula's romance closure. `dream.herald` no longer has that generated guard in this export. The shared presence transformer needs historical-versus-live handling.
- P23: generated bridge `sleep` coercion paragraph still receives `crossroute.nocticula.available`, although coercion is historical. The independent bridge fire and anonymous H2 recovery no longer mention a live Areelu and remain unconditional apart from their actual outcomes.
- P24–25 / F22,40: `lastcall_partners.py` Iomedae coda needs neutral/banner-specific memories and bridge/empty-flask settlement separated from Areelu's presence-qualified measurement; its paragraph still requires `crossroute.areelu.available`.
- P27–34 / F23–32: existing `integrate_joint` edits Elyanka/collectors/bottle entries using KEPT alone; broadening to `buried_alive`, Camellia's empty-flask reaction and Areelu's lien/not-burned variants changes other-route or shared entries not named as editable. Those changes were not made.
- P35–37 / F33–34: shared Last Call heroic recovery still needs the anonymous bridge/Pharasma settlement, private toast and final-appointment mortality variants for both returns. Do not publicly restore the dead-to-world Commander.
- Shared Last Call coda still needs the return and private encounter consistent with this single first night. The route-local gate/after encounters implement the played return; they do not certify the shared coda.
- F41's complete generated shared flask/presence matrix remains for coordinator integration. The new tests cover the route-local negative walks and debt collection; existing shared tests were not weakened to hide these residuals.
- Broad Python and rules execution repeatedly terminated with SIGTERM before totals; no termination reason was supplied. Coordinator milestone validation remains required. Filtered Iomedae validation and all quick Python checks completed successfully.

Engine round 3's report lists Iomedae as `0/0`, with no additional residual row. No shared source, generated development export, other route or save-baseline file was edited.

## PROPOSE

None beyond the already planned shared fixes listed under ESCALATE. No additional mechanics, costs, attraction threshold, partner stance or reconciliation condition implemented.

## RISKS

The outstanding shared readers prevent certification of the requested 91+ across all dimensions. Independent prose scores are not self-certified. The export generator labels this environment's output an incomplete development export; it is an authoring/validation artifact, not an installed game build. No harness, game or build-expansion script was run. No commit was made, following the user's final instruction.
