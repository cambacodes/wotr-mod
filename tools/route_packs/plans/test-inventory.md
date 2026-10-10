# Test inventory

Static assertion inventory; existing tests are unchanged.

Regenerate with `python -m tools.test_classifier`; add `--bundle-manifest <manifest.json>` to use exact pinned baseline inputs plus new workspace tests.

Parsed 280 Python files; discovered 2231 tests.

| Classification | Tests |
| --- | ---: |
| behavioural | 1239 |
| pinned | 118 |
| mixed | 874 |

## Modules with most pinned assertions

| Module | Pinned assertions |
| --- | ---: |
| tests/test_playthrough_loop.py | 154 |
| tests/test_crossroute_presence.py | 150 |
| tests/test_nidalynn_partner_claim.py | 112 |
| tests/test_arueshalae_round2.py | 56 |
| tests/test_EliandraPolish.py | 49 |
| tests/test_dorgelinda_round3.py | 47 |
| tests/test_dorgelinda_round2.py | 41 |
| tests/test_galfrey_round2.py | 36 |
| tests/test_nidalynn_round2.py | 35 |
| tests/test_horzalah_polish.py | 34 |
| tests/test_chivarro_setpieces.py | 33 |
| tests/test_fix15.py | 33 |
| tests/test_aranka_round2.py | 31 |
| tests/test_endings_job3.py | 31 |
| tests/test_foresight_echo.py | 30 |
| tests/test_refactor_guard.py | 30 |
| tests/test_dorgelinda_polish.py | 28 |
| tests/test_elyanka_round2.py | 28 |
| tests/test_gesmerha_round2.py | 27 |
| tests/test_terendelev_polish.py | 27 |

## Cand-14 failing modules

The supplied failing names identify modules, not individual methods. Every discovered method and pinned line is in JSON. Counts below summarize their assertions; setup errors have no assertion classification.

| Module | Classification | Behavioural | Pinned | Mixed |
| --- | --- | ---: | ---: | ---: |
| test_nidalynn_partner_claim | mixed | 2 | 1 | 18 |
| test_harem_row_s49 | mixed | 8 | 0 | 2 |
| test_contract_j01 | mixed | 9 | 0 | 1 |
| test_kiana_partner | mixed | 6 | 0 | 1 |
| test_iomedae_round2 | mixed | 4 | 0 | 2 |
| test_horzalah_polish | mixed | 1 | 0 | 8 |
| test_herrax_round2 | mixed | 5 | 1 | 7 |
| test_harem_row_registry | mixed | 3 | 0 | 1 |
| test_engine_q5 | mixed | 11 | 0 | 1 |
| test_eng7_l07_contracts | mixed | 5 | 0 | 1 |
| test_endings_job4 | mixed | 2 | 0 | 5 |
| test_earned_presence | behavioural | 31 | 0 | 0 |
| test_crossroute_presence | mixed | 16 | 11 | 28 |
| test_arueshalae_round2 | mixed | 0 | 4 | 13 |
| test_harem_row_s30 | mixed | 6 | 0 | 3 |
| test_chivarro_setpieces | mixed | 1 | 2 | 6 |
| test_harem_row_s42 | mixed | 5 | 0 | 1 |
| test_harem_row_s35 | mixed | 3 | 0 | 7 |
| test_harem_row_s25 | mixed | 5 | 0 | 6 |
| test_harem_row_s24 | mixed | 4 | 0 | 2 |
| test_engine_q7_l12 | mixed | 7 | 0 | 1 |
| test_draft_contract_lint | mixed | 9 | 0 | 1 |

## Known limits

- Static heuristics do not establish whether a literal is actually player-visible; review prose candidates.
- Local aliases, loop targets, same-module helper returns and assertion helpers are traced conservatively; imported helpers and runtime dispatch are opaque.
- Bindings are flow-insensitive unions: reassignment or dynamic field keys can over-classify; unknown assertions default to behavioural.
- Setup failures are not assertions: module summaries classify discovered tests, not the cause of a setUpClass error.
- No tests are executed. Decorator-generated tests, inherited tests defined in other modules and dynamic test factories may be absent.

## Counts by module

| Module | Behavioural | Pinned | Mixed |
| --- | ---: | ---: | ---: |
| tests/build_fixture_story.py | 0 | 0 | 0 |
| tests/harem_row_walk.py | 0 | 0 | 0 |
| tests/story_fixture.py | 0 | 0 | 0 |
| tests/structure.py | 0 | 0 | 0 |
| tests/temp_directory.py | 0 | 0 | 0 |
| tests/temp_fixtures.py | 0 | 0 | 0 |
| tests/test_DelamerePolish.py | 5 | 0 | 4 |
| tests/test_DelamereRound2.py | 4 | 0 | 3 |
| tests/test_DelamereRound4.py | 0 | 0 | 1 |
| tests/test_EliandraPolish.py | 0 | 0 | 14 |
| tests/test_KianaNativeText.py | 2 | 0 | 1 |
| tests/test_anevia_partner_stance.py | 1 | 0 | 5 |
| tests/test_anevia_round2.py | 2 | 0 | 3 |
| tests/test_aranka_round2.py | 2 | 2 | 9 |
| tests/test_areelu_round2.py | 4 | 0 | 2 |
| tests/test_arsinoe_exclusivity.py | 2 | 0 | 1 |
| tests/test_arsinoe_round2.py | 5 | 1 | 2 |
| tests/test_arueshalae_round2.py | 0 | 4 | 13 |
| tests/test_camellia_round2.py | 3 | 0 | 5 |
| tests/test_canary_letters.py | 5 | 0 | 1 |
| tests/test_canon_partner_lint.py | 21 | 1 | 2 |
| tests/test_chadali_round2.py | 9 | 0 | 2 |
| tests/test_chadali_round4.py | 1 | 0 | 3 |
| tests/test_chadali_structure.py | 4 | 0 | 0 |
| tests/test_chapter_zero.py | 5 | 0 | 2 |
| tests/test_character_interactions_ix_a.py | 4 | 0 | 1 |
| tests/test_chivarro_setpieces.py | 1 | 2 | 6 |
| tests/test_contact_windows.py | 3 | 0 | 0 |
| tests/test_contract_j01.py | 9 | 0 | 1 |
| tests/test_crossroute_lint.py | 33 | 2 | 2 |
| tests/test_crossroute_presence.py | 16 | 11 | 28 |
| tests/test_crossroute_solver.py | 13 | 0 | 0 |
| tests/test_delivery_inventory2.py | 8 | 0 | 1 |
| tests/test_devarra_round2.py | 1 | 0 | 9 |
| tests/test_devarra_round3.py | 2 | 0 | 2 |
| tests/test_devarra_round4.py | 0 | 3 | 4 |
| tests/test_dorgelinda_commitment.py | 6 | 0 | 0 |
| tests/test_dorgelinda_polish.py | 0 | 0 | 6 |
| tests/test_dorgelinda_round2.py | 0 | 1 | 9 |
| tests/test_dorgelinda_round3.py | 0 | 1 | 9 |
| tests/test_draft_contract_lint.py | 9 | 0 | 1 |
| tests/test_drezen_placement.py | 5 | 0 | 1 |
| tests/test_drezen_siege_staging.py | 7 | 0 | 0 |
| tests/test_earned_outcomes.py | 11 | 0 | 3 |
| tests/test_earned_presence.py | 31 | 0 | 0 |
| tests/test_edge_lint.py | 5 | 1 | 2 |
| tests/test_eliandra_round2.py | 2 | 0 | 6 |
| tests/test_elyanka_cloud.py | 1 | 1 | 4 |
| tests/test_elyanka_round2.py | 3 | 0 | 7 |
| tests/test_endings_job3.py | 3 | 1 | 9 |
| tests/test_endings_job4.py | 2 | 0 | 5 |
| tests/test_eng7_l07_contracts.py | 5 | 0 | 1 |
| tests/test_engine_clocks.py | 5 | 0 | 0 |
| tests/test_engine_f6c.py | 5 | 0 | 1 |
| tests/test_engine_q5.py | 11 | 0 | 1 |
| tests/test_engine_q7_l12.py | 7 | 0 | 1 |
| tests/test_engine_q8e.py | 3 | 1 | 2 |
| tests/test_eritrice_polish.py | 2 | 0 | 5 |
| tests/test_eritrice_round2.py | 3 | 0 | 5 |
| tests/test_eritrice_round3.py | 0 | 0 | 4 |
| tests/test_eritrice_round4.py | 0 | 0 | 5 |
| tests/test_etude_lifecycle.py | 16 | 0 | 0 |
| tests/test_fix14_a.py | 2 | 0 | 3 |
| tests/test_fix14_b.py | 4 | 0 | 5 |
| tests/test_fix14_c.py | 0 | 0 | 4 |
| tests/test_fix15.py | 5 | 0 | 8 |
| tests/test_foresight_echo.py | 8 | 1 | 6 |
| tests/test_galfrey_round2.py | 1 | 1 | 10 |
| tests/test_galfrey_round4.py | 0 | 0 | 3 |
| tests/test_gameplay_entry_inventory.py | 7 | 0 | 0 |
| tests/test_gate_lint.py | 8 | 0 | 0 |
| tests/test_gesmerha_round2.py | 6 | 1 | 5 |
| tests/test_harem_engine.py | 6 | 0 | 1 |
| tests/test_harem_explicit_scope.py | 0 | 0 | 1 |
| tests/test_harem_inventory_scenarios.py | 8 | 0 | 2 |
| tests/test_harem_rest_sim.py | 4 | 0 | 2 |
| tests/test_harem_row_ensemble_ch5.py | 6 | 0 | 1 |
| tests/test_harem_row_household_knowledge.py | 6 | 1 | 2 |
| tests/test_harem_row_household_mend.py | 8 | 0 | 1 |
| tests/test_harem_row_j02.py | 10 | 0 | 4 |
| tests/test_harem_row_j03.py | 13 | 0 | 4 |
| tests/test_harem_row_j04.py | 1 | 0 | 5 |
| tests/test_harem_row_j05.py | 12 | 0 | 3 |
| tests/test_harem_row_j06.py | 11 | 0 | 1 |
| tests/test_harem_row_registry.py | 3 | 0 | 1 |
| tests/test_harem_row_s01.py | 6 | 0 | 2 |
| tests/test_harem_row_s02.py | 1 | 0 | 7 |
| tests/test_harem_row_s03a.py | 3 | 1 | 4 |
| tests/test_harem_row_s03b.py | 8 | 0 | 2 |
| tests/test_harem_row_s04.py | 5 | 0 | 3 |
| tests/test_harem_row_s05.py | 3 | 0 | 2 |
| tests/test_harem_row_s06.py | 7 | 0 | 1 |
| tests/test_harem_row_s07.py | 2 | 0 | 2 |
| tests/test_harem_row_s08.py | 7 | 0 | 1 |
| tests/test_harem_row_s09.py | 8 | 0 | 3 |
| tests/test_harem_row_s10.py | 9 | 0 | 1 |
| tests/test_harem_row_s11.py | 8 | 0 | 4 |
| tests/test_harem_row_s12.py | 4 | 0 | 3 |
| tests/test_harem_row_s13.py | 6 | 0 | 3 |
| tests/test_harem_row_s14.py | 8 | 1 | 3 |
| tests/test_harem_row_s16.py | 3 | 0 | 2 |
| tests/test_harem_row_s17.py | 5 | 0 | 2 |
| tests/test_harem_row_s18f.py | 1 | 0 | 0 |
| tests/test_harem_row_s18x.py | 4 | 0 | 2 |
| tests/test_harem_row_s19.py | 3 | 0 | 2 |
| tests/test_harem_row_s20.py | 5 | 0 | 2 |
| tests/test_harem_row_s21.py | 3 | 0 | 2 |
| tests/test_harem_row_s22.py | 3 | 0 | 0 |
| tests/test_harem_row_s23.py | 6 | 0 | 1 |
| tests/test_harem_row_s24.py | 4 | 0 | 2 |
| tests/test_harem_row_s25.py | 5 | 0 | 6 |
| tests/test_harem_row_s26.py | 8 | 0 | 1 |
| tests/test_harem_row_s27.py | 4 | 0 | 2 |
| tests/test_harem_row_s28.py | 8 | 0 | 7 |
| tests/test_harem_row_s29.py | 3 | 0 | 3 |
| tests/test_harem_row_s30.py | 6 | 0 | 3 |
| tests/test_harem_row_s34.py | 2 | 0 | 1 |
| tests/test_harem_row_s35.py | 3 | 0 | 7 |
| tests/test_harem_row_s36.py | 9 | 0 | 2 |
| tests/test_harem_row_s37.py | 4 | 0 | 3 |
| tests/test_harem_row_s38.py | 4 | 0 | 3 |
| tests/test_harem_row_s39.py | 2 | 0 | 4 |
| tests/test_harem_row_s40.py | 6 | 0 | 2 |
| tests/test_harem_row_s41.py | 4 | 0 | 3 |
| tests/test_harem_row_s42.py | 5 | 0 | 1 |
| tests/test_harem_row_s43.py | 5 | 0 | 3 |
| tests/test_harem_row_s44.py | 6 | 0 | 3 |
| tests/test_harem_row_s45.py | 4 | 0 | 4 |
| tests/test_harem_row_s47.py | 4 | 0 | 3 |
| tests/test_harem_row_s48.py | 5 | 0 | 4 |
| tests/test_harem_row_s49.py | 8 | 0 | 2 |
| tests/test_harem_row_s50.py | 5 | 1 | 4 |
| tests/test_harem_row_s51.py | 5 | 0 | 2 |
| tests/test_harem_row_s52.py | 7 | 0 | 1 |
| tests/test_harem_row_w3_s44_evil.py | 8 | 0 | 2 |
| tests/test_harem_row_w4_ensemble_ch3.py | 7 | 0 | 1 |
| tests/test_harem_row_w5_readers.py | 7 | 0 | 2 |
| tests/test_harem_row_w5_residence.py | 7 | 0 | 0 |
| tests/test_harem_schedule.py | 16 | 0 | 1 |
| tests/test_harem_smoothing.py | 20 | 2 | 1 |
| tests/test_harem_transactions.py | 6 | 0 | 0 |
| tests/test_harness_evidence.py | 2 | 4 | 0 |
| tests/test_harness_fixture_setup.py | 0 | 0 | 1 |
| tests/test_harness_system_cases.py | 2 | 0 | 0 |
| tests/test_hepzamirah_round2.py | 0 | 1 | 10 |
| tests/test_herrax_round2.py | 5 | 1 | 7 |
| tests/test_herrax_round4.py | 1 | 0 | 1 |
| tests/test_horzalah_polish.py | 1 | 0 | 8 |
| tests/test_horzalah_round2.py | 0 | 0 | 5 |
| tests/test_horzalah_round3.py | 2 | 2 | 2 |
| tests/test_horzalah_round4.py | 0 | 0 | 4 |
| tests/test_household_delay.py | 6 | 0 | 0 |
| tests/test_household_pair_seelah_wenduag.py | 5 | 0 | 13 |
| tests/test_hub_attachment_lint.py | 3 | 0 | 0 |
| tests/test_ideal_run_regression.py | 1 | 0 | 1 |
| tests/test_intimacy_contract_lint.py | 3 | 0 | 0 |
| tests/test_iomedae_round2.py | 4 | 0 | 2 |
| tests/test_iomedae_round3.py | 3 | 1 | 3 |
| tests/test_iomedae_round4.py | 0 | 1 | 4 |
| tests/test_irabeth_partner_stance.py | 4 | 0 | 1 |
| tests/test_irabeth_round2.py | 3 | 0 | 3 |
| tests/test_jannah_round2.py | 6 | 0 | 1 |
| tests/test_jerribeth_partner.py | 6 | 0 | 4 |
| tests/test_jerribeth_round2.py | 7 | 0 | 1 |
| tests/test_jerribeth_scaffolding.py | 12 | 1 | 3 |
| tests/test_kaylessa_round2.py | 4 | 0 | 6 |
| tests/test_kaylessa_round3.py | 3 | 1 | 5 |
| tests/test_kaylessa_round4.py | 0 | 0 | 4 |
| tests/test_kiana_native_reconciliation.py | 5 | 0 | 0 |
| tests/test_kiana_partner.py | 6 | 0 | 1 |
| tests/test_kiana_round2.py | 1 | 0 | 5 |
| tests/test_kiana_round3.py | 5 | 3 | 1 |
| tests/test_kiana_round4.py | 3 | 0 | 2 |
| tests/test_konomi_round2.py | 0 | 2 | 6 |
| tests/test_konomi_round3.py | 1 | 0 | 5 |
| tests/test_lastcall_history_inventory.py | 5 | 0 | 0 |
| tests/test_late_acceptance_inventory2.py | 4 | 0 | 1 |
| tests/test_latest_state_inventory.py | 6 | 1 | 0 |
| tests/test_lc_history_01.py | 2 | 0 | 0 |
| tests/test_lc_history_01_a2.py | 1 | 0 | 2 |
| tests/test_left_trickster_consumers.py | 2 | 1 | 2 |
| tests/test_melazmera_round2.py | 2 | 0 | 7 |
| tests/test_memory_callback_lint.py | 4 | 1 | 6 |
| tests/test_mielarah_round2.py | 5 | 0 | 3 |
| tests/test_mielarah_round4.py | 0 | 0 | 2 |
| tests/test_minachiv_scaffolding.py | 6 | 1 | 4 |
| tests/test_minagho_chivarro_stance.py | 8 | 0 | 5 |
| tests/test_minagho_round2.py | 2 | 0 | 4 |
| tests/test_native_answer_edits.py | 5 | 0 | 0 |
| tests/test_native_cue_policy_inventory.py | 1 | 0 | 1 |
| tests/test_native_facilities.py | 8 | 5 | 1 |
| tests/test_native_fact_inventory.py | 4 | 0 | 2 |
| tests/test_native_inventory.py | 3 | 1 | 2 |
| tests/test_native_world_reconciliation.py | 4 | 1 | 3 |
| tests/test_nenio_polish.py | 0 | 0 | 6 |
| tests/test_nenio_round2.py | 0 | 0 | 4 |
| tests/test_nenio_round3.py | 0 | 0 | 2 |
| tests/test_nidalynn_partner_claim.py | 2 | 1 | 18 |
| tests/test_nidalynn_round2.py | 0 | 2 | 5 |
| tests/test_nidalynn_round4.py | 0 | 0 | 4 |
| tests/test_nocticula_n1.py | 2 | 0 | 6 |
| tests/test_nocticula_partners.py | 7 | 0 | 2 |
| tests/test_nocticula_polish.py | 0 | 0 | 3 |
| tests/test_nocticula_round2.py | 1 | 0 | 6 |
| tests/test_nurah_round2.py | 2 | 0 | 4 |
| tests/test_nurah_round4.py | 2 | 0 | 2 |
| tests/test_obligation_flow_lint.py | 9 | 0 | 0 |
| tests/test_outcome_exits.py | 1 | 1 | 3 |
| tests/test_pacing_lint.py | 12 | 0 | 4 |
| tests/test_parent_bindings.py | 1 | 0 | 1 |
| tests/test_participant_inventory_contracts.py | 5 | 0 | 0 |
| tests/test_payoff_departure_contracts.py | 20 | 0 | 2 |
| tests/test_player_text_baseline.py | 2 | 1 | 1 |
| tests/test_player_text_inventory2.py | 1 | 1 | 4 |
| tests/test_player_text_lint.py | 1 | 0 | 3 |
| tests/test_playthrough_loop.py | 4 | 3 | 30 |
| tests/test_presence_dependency_lint.py | 17 | 0 | 0 |
| tests/test_presence_exception_export.py | 3 | 0 | 0 |
| tests/test_prose_integration.py | 10 | 0 | 3 |
| tests/test_recovery.py | 4 | 0 | 2 |
| tests/test_refactor_guard.py | 17 | 4 | 15 |
| tests/test_remote_allocation_lint.py | 1 | 3 | 4 |
| tests/test_rescue_endpoint_inventory.py | 5 | 0 | 0 |
| tests/test_return_safety.py | 9 | 2 | 1 |
| tests/test_rg_ideal_run.py | 3 | 0 | 0 |
| tests/test_rrt_validate.py | 4 | 0 | 0 |
| tests/test_run_guide_check.py | 13 | 3 | 4 |
| tests/test_savecompat_baseline.py | 11 | 0 | 6 |
| tests/test_seelah_round2.py | 3 | 0 | 5 |
| tests/test_seelah_round3.py | 1 | 2 | 2 |
| tests/test_seelah_round4.py | 0 | 0 | 4 |
| tests/test_shamira_partner_stance.py | 3 | 0 | 5 |
| tests/test_shamira_round2.py | 1 | 0 | 6 |
| tests/test_slot_brief_lint.py | 17 | 0 | 1 |
| tests/test_soana_partner.py | 5 | 0 | 3 |
| tests/test_soana_round2.py | 4 | 0 | 3 |
| tests/test_soana_round3.py | 10 | 2 | 4 |
| tests/test_soana_savecompat_baseline.py | 0 | 0 | 1 |
| tests/test_stance_agency.py | 8 | 0 | 2 |
| tests/test_struct2_02.py | 3 | 1 | 1 |
| tests/test_struct2_03.py | 2 | 0 | 2 |
| tests/test_struct2_04_hosts.py | 2 | 0 | 3 |
| tests/test_struct2_05.py | 3 | 0 | 2 |
| tests/test_struct2_07.py | 1 | 0 | 4 |
| tests/test_struct2_08.py | 3 | 0 | 2 |
| tests/test_struct2_09.py | 5 | 0 | 1 |
| tests/test_struct2_10.py | 0 | 0 | 4 |
| tests/test_struct2_11.py | 1 | 0 | 4 |
| tests/test_struct2_continuity.py | 1 | 0 | 2 |
| tests/test_struct3_a.py | 5 | 0 | 1 |
| tests/test_struct3_b.py | 0 | 0 | 4 |
| tests/test_struct3_c.py | 1 | 0 | 3 |
| tests/test_struct3_d.py | 4 | 0 | 6 |
| tests/test_targona_round2.py | 2 | 0 | 4 |
| tests/test_targona_round3.py | 0 | 0 | 3 |
| tests/test_terendelev_polish.py | 1 | 0 | 4 |
| tests/test_terendelev_reference_contexts.py | 0 | 0 | 2 |
| tests/test_terendelev_round2.py | 2 | 0 | 4 |
| tests/test_test_classifier.py | 0 | 13 | 1 |
| tests/test_test_gate.py | 5 | 2 | 3 |
| tests/test_test_rot_contracts.py | 1 | 1 | 0 |
| tests/test_test_selection.py | 8 | 0 | 1 |
| tests/test_text_structure_lint.py | 1 | 3 | 3 |
| tests/test_timeline_contract_lint.py | 6 | 2 | 2 |
| tests/test_transaction_exit_lint.py | 1 | 1 | 0 |
| tests/test_transaction_inventory2.py | 1 | 0 | 0 |
| tests/test_trickster_interactions_ix_b.py | 1 | 0 | 4 |
| tests/test_utf8_io.py | 1 | 0 | 0 |
| tests/test_vellexia_player_answers.py | 2 | 0 | 2 |
| tests/test_vellexia_round2.py | 2 | 0 | 8 |
| tests/test_vellexia_round3.py | 0 | 0 | 6 |
| tests/test_verifier_tiers.py | 1 | 0 | 0 |
| tests/test_voice_authority.py | 15 | 0 | 4 |
| tests/test_voice_lock_lint.py | 1 | 1 | 0 |
| tests/test_wenduag_echo.py | 1 | 0 | 3 |
| tests/test_wenduag_partner_stance.py | 3 | 0 | 8 |
| tests/test_wenduag_polish.py | 3 | 0 | 7 |
| tests/test_yaniel_round2.py | 2 | 0 | 8 |
| tests/writable_temp.py | 0 | 0 | 0 |
| tests/write-tirabade-bridge-fixture.py | 0 | 0 | 0 |
