# struct-harem-hosts implementation evidence

Pinned base: `8c50d2bbedb253d16d61db3fae62a6807e79c963`.
Input manifest SHA-256: `06e590491e8721e8ef0f2aaf0e0741283ebc9cbe274f5b62f20bb5418aea75c1`.

## Fixed structure

S25 company, desire, choice and morning no longer forbid the readiness flag they require. Each now has InteractionHub=household.table, replacing Remote/ManualOnly dispatch. Current-body and departure gates, earned deeds, mutual answers, successor targets and 48/48/48/8-hour delays are unchanged. No runtime text was added or changed. The existing brief remains editorially blocked on body-window certification; static brief lint passes independently of that certification.

## Own checks (not runner gate receipts)

- `python -m unittest tests.test_harem_row_s25`: exit 137, no output; failed, attribution unknown. No baseline receipt exists.
- Focused `python -` source-construction check: exit 0. Registered S25 into a minimal payload; checked all four sibling gates for required/forbidden intersections, table placement, original body requirements and departure vetoes. Called tools.slot_brief_lint.lint for the canonical Camellia/Vellexia brief: zero hard findings. Imported pinned base S25 through a system-temporary file and compared all six scene IDs and complete node dictionaries, including text, choices and targets: equal. UTF-8 decode and existing LF/CRLF counts checked.
- Sibling `python -` inspection: exit 0. Constructed S05/S25/S28 and called slot_brief_lint.lint on the four assigned briefs. Remaining hard findings: missing Jerribeth/Vellexia host, missing Shamira/Arueshalae host, missing Nocticula/Shamira host, and Nocticula/Shamira missing example. S44 metadata_ready() returned false. S28 retains four non-emitted OPTIONAL_CANDIDATES. S05 emits only precedence.
- `git diff --check`: exit 0.

Required regeneration, committed-save-ID and save-compatibility/encoding gates are unrun here (exit null). The wrapper owns gates, receipts and export sealing. This record does not certify a delivered export or profile/environment digests.

## Escalations and sibling coverage

- S25 campaign delivery: Vellexia route/shared presence owner must certify a current overlapping 152-hour body window. Removal of a contradictory gate and table placement do not extend presence. Evidence: pinned inputs/sources/28-s25.py, existing EXCLUSIONS and canonical brief's body-window blocker. All four continuations retain their presence/departure checks.
- S28: Jerribeth/Vellexia route owners and shared household coordinator must resolve the explicitly withheld overlapping one-visit body window, reconciliation/stage/Marhevok/cap readers. Evidence: pinned S28 source through its manifest bundle_path, BODY_REQUIRES/BODY_FORBIDS and OPTIONAL_CANDIDATES; canonical brief build_contract. All four company/invitation/choice/morning candidates inspected. No stay or reconciliation producer invented.
- S44: schedule coordinator owns tools/harem-schedule.json, outside allow_paths. Existing metadata_ready requires the corrupted-only lover ceiling and four-step optional arc allocation; it is false. Evidence: w3_s44_evil.metadata_ready, register and optional_nodes; s44 REQUIRES/FORBIDS. Reviewed redeemed/corrupted settlement siblings and four held extension steps. No ceiling bypass.
- S05: Nocticula/Shamira route owners must verify a shared Chapter 5 bodily venue/channel and personal answers; the pinned source explicitly allows only history and withholds live replies/coup reconciliation. Evidence: pinned inputs/sources/8-s05.py, BLOCKED_SLOT, historical_scene, canonical blocked brief. Inspected precedence and zzz_nocticula_pairs transformations. The voice owner also owes the brief example after the host contract is resolved.
- Evidence owner/coordinator: requested Writer judging/rubric1 JSON and mod tools/playthrough/runs/verified-findings.json are absent from this checkout and not supplied as pinned audit inputs. No external audit attribution claimed.

No additional hosts or prose placeholders were created because their activation contracts remain unresolved. Existing authored nodes were preserved. Structural work is partial; prose quality and in-game reachability remain unverified.
