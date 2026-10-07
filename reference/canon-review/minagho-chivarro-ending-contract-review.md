# Minagho and Chivarro revision 2 ending-contract review

Revision 2 is not ready for integration unchanged.
All 34 proposed cue identities and parent-page memberships are correct, and preserving the original page and cue selectors protects substantially more parent content than wholesale page replacement.
However, the shared invitation trigger claims an earlier reunion before the arrival scene has happened.
The dragon ascension replacement also weakens one established outcome, and actual-loss arbitration still needs a concrete implementation contract.
This review concerns technical and canon integration, not a numerical literary score.

## Frozen evidence

The reviewed manuscript SHA256 is `BAD0191730C8B2EFFB879030AC67245B64C7A8E5ECE58FF8D8D3735E89D3C5C6`.
The installed RanRomance.dll SHA256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
The installed parent LocalizedStrings.json SHA256 is `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`, matching the previous audit's English extraction.
I freshly decompiled Slide0001 through Slide0008, SlideAeon and MinaEpil from that DLL into `C:/Users/Z/AppData/Local/Temp/minachiv-ending-review-d9010692`.
I compared all proposed IDs against their actual CueConfigurator declarations, text keys and AddToCues membership in the declared BookPageConfigurator.
All 34 matched.
The temporary `verified-contract.json` records each cue, page, original text key, proposed edit and exact decompiled condition definitions.
This establishes source construction, not a claim that the parent initializer executed in Unity.

I also extracted the native paired page and cue directly from the installed blueprints.zip into temporary `native-paired.json` and read their shared text from the game's enGB localization.
No game archive, source implementation, shared registration or export was changed.
I authored the separate ParentEndingGuard prerequisite earlier, so this audit does not independently approve that helper.

## Required corrections

1. Split reunion continuity from invitation eligibility.
`minachiv.invitation_kept` is earned in `two_answers/agreement` while Minagho says Chivarro will come by her chosen route.
The next visit, `her_own_arrival`, actually shows the reunion and earns `minachiv.arrival_kept` at its ending.
Thus an interrupted save with invitation_kept and without arrival_kept must not receive the earlier-reunion rewrites of `c47829fba057400c8e0279990be3d25e` or `8399dbc5987b462594b2b4168764e269`.
Use an earned arrival witness for those two replacements, or provide a separately reviewed invitation-only variant that makes no completed-reunion claim.
Do not simply delay every consent edit until arrival, because invitation-only histories still must not automatically give Chivarro a Commander romance.
The invitation-only addon unfinished paragraph also says both women have begun a conversation with the Commander; review that text against the same actual arrival boundary.

2. Preserve the established dragon outcome in `64afcd565e044e53977e1878444f4ee1`.
The original ascension cue says Minagho masters her dragon soul with the Commander's help and describes a female dragon accompanying the Commander.
The proposed text says she continued learning to master it.
This retains training but loses the achieved mastery/transformation outcome.
The neighboring two-woman replacement explicitly says they learned to master their souls and does not have the same omission.
Preserve Minagho's eventual mastery and dragon form without retaining automatic romantic devotion.

3. Make actual-loss precedence explicit before wiring.
The ordinary parent page selectors and many unchanged cues do not test the actual Minagho/Chivarro death etudes.
For example, the Dragon page requires RanRomMinaDragon, and its first cue describes Minagho's living rehabilitation work with no death condition.
Suppressing only the 34 listed relationship cues cannot prevent an unchanged living future beside a new `ending_minagho_lost`, `ending_chivarro_lost` or `ending_both_lost` paragraph.
A reviewed loss branch must suppress the applicable living parent future only when a truthful corresponding replacement is available or already played, or provide survivor-specific cue variants.
A comment saying loss takes precedence does not implement or prove that arbitration.
Do not treat Commander sacrifice as either woman's death: the parent has specific sacrifice consequences that should remain.
Likewise, preserve the separate Aeon page and its native remembrance/redemption selectors instead of feeding pre-rewrite death or invitation facts into its rewritten lives.

## Native paired fallback and localization

The configured parent fallback cue `c47829fba057400c8e0279990be3d25e` belongs to Slide0008 and uses native key `056942f6-32d0-4480-8ff7-29356b43db19`.
The distinct native cue `5787f92575364c1459df8f075676c2db` belongs to native page `5c95d8e3fa4f3b44896914987cb04b0b` and uses that same key.
The original text places the reunion several hundred years after the Fifth Crusade, far from the Abyss and Golarion, with the couple never parting again.
After a played arrival, the parent's original centuries-later first reunion contradicts the extension.
Before arrival, the proposed past-tense earlier reunion invents history.

The parent initializer replaces the native paired-page selector with its existing Book-1/refusal exclusion combined with Chivarro's search etude.
Preserve that entire selector.
Do not globally replace the native localization key, because that would also change unrelated native and parent-only saves.
Use a new localized key on an earned conditional alternate of the intended cue.
If the native paired page remains reachable in an integration fixture with earned addon arrival, either independently apply the same earned continuity alternate to its actual cue or prove why that state is excluded by the retained parent selector.
The 34-entry metadata currently names only the configured parent copy, not the native cue.

## Verified page scopes

Every table row below is a BlueprintCue declared in the named parent slide class and explicitly inserted in that slide's BlueprintBookPage.
The condition column names the exact ConditionsBuilder variable in the freshly decompiled class; it is not a replacement interpretation of that condition.
The full expressions, including nested negated AND groups and all EtudeStatus arguments, are in the temporary evidence.
Keep those original checkers intact.

| Slide | Page GUID | Existing page selector |
| --- | --- | --- |
| 0001 | `951e4432cf844a36a8a222b27589fb43` | Banner and either parent group-ascension etude; nested OR is material. |
| 0002 | `6db8635856e74b6cac46330bd82b4ff5` | Redemption and neither group-ascension etude. |
| 0003 | `8df5edb6f69040c69d7da78d2bf20cb6` | Parent evil-epilogue etude and cult. |
| 0004 | `5a5865ceca0e42049288351a76b18ba9` | Cult and not parent evil-epilogue etude. |
| 0005 | `126762ac92364ac5bdec69c6e3fdfd1a` | Demon service and not cult. |
| 0006 | `01677da8df6e42c6b4803ceef524b1fe` | Dragon development. |
| 0007 | `9c5c5825bf3245d0ae763c6e69ecdc38` | Legend development. |
| 0008 | `3792457f35734d75a4d4b53055f7f5d0` | Parent Book 1 seen and specific pre-brand refusal not selected. |
| Aeon | `6bf016f775734c3eb4f287c29c59e9f9` | Parent Book 1/refusal selector in its separate rewritten-timeline sequence. |

Within the ordinary pages, search etude `71f85264d9064074f9cf74999ecbffa9` selects pair versus solo variants.
Romance-specific cues additionally test the parent romance etude.
Ascension is `c6935ff7cbfd4aed8ac479e94e66918d`; Commander sacrifice is `381a296094804761af0893d2e70dc2df`.
Redemption also distinguishes the Heaven departure `4a78282987fd432595c8a62d363730d7`.
These selectors must remain native conditions, not approximations using addon romance flags.

## All 34 proposed edits

S means suppress the original relationship cue after an earned applicable replacement.
R means show a conditional alternate text under the original cue's conditions and the additional earned scope.
Neither means changing the shared original text or applying edits to an untouched parent save.

| Cue GUID | Slide/cue | Existing condition | Proposed operation |
| --- | --- | --- | --- |
| `c47829fba057400c8e0279990be3d25e` | 0008Cue0004 | `conditions5` | R |
| `819314e916514a498a8e336371b4788e` | 0001Cue0003 | `conditions5` | S |
| `9bfbb3f217ca476cadbeffc4d389717d` | 0001Cue0004 | `conditions6` | S |
| `d6b960c14e37492682de6284af1c5417` | 0001Cue0007 | `conditions9` | S |
| `19fd9027465f4cbebe949b26d04a2826` | 0001Cue0008 | `conditions10` | S |
| `59cf28c3824944fd88547bc61bc5cf62` | 0001Cue0011 | `conditions13` | S |
| `92162854b221413984468d2663ffcffb` | 0001Cue0012 | `conditions14` | S |
| `cce5f180fbe7455989544c1c81428463` | 0002Cue0007 | `conditions8` | S |
| `829c837c76f6429fa01d3d2583069b35` | 0002Cue0008 | `conditions9` | S |
| `51104e1c8755436e8aa290a6cedfcb3a` | 0002Cue0011 | `conditions12` | S |
| `fb32a8f9c464496abe90307c68ec271e` | 0002Cue0012 | `conditions13` | S |
| `5ab5c6a3c62b4f2ba88053cbbbc47737` | 0003Cue0003 | `conditions4` | S |
| `dc14cdafb9fa43e8bc3b0816626b3dbe` | 0003Cue0004 | `conditions5` | S |
| `f37b7a5fcff84551b86ecbba823e2fa5` | 0003Cue0007 | `conditions8` | S |
| `982627a0bbd34fe4b16b5b078e56355a` | 0003Cue0008 | `conditions9` | S |
| `784575a522e64ad58f2171abcb073d0c` | 0004Cue0003 | `conditions4` | S |
| `5db846019acd46ef83f12be220727f50` | 0004Cue0004 | `conditions5` | S |
| `9e3bd8247f0c40eba62368fe2912bb84` | 0004Cue0007 | `conditions8` | S |
| `18d22b6258a24fe29dd9d0ea4235432e` | 0004Cue0008 | `conditions9` | S |
| `8009e775a3a343c79ef4e40d72bc5e6a` | 0005Cue0007 | `conditions8` | S |
| `5b0a132d97404072b3d664899871d7b7` | 0005Cue0008 | `conditions9` | S |
| `d6714bd8d48e425d862f854018cb123c` | 0007Cue0003 | `conditions3` | S |
| `ff2042ad95e14b73a5f75f2cfd84b5e4` | 0007Cue0004 | `conditions4` | S |
| `a875684118e64d7ab29f70ca3460c365` | 0002Cue0003 | `conditions4` | R |
| `9a5eb7aff04943c28da2260aac68874e` | 0002Cue0004 | `conditions5` | R |
| `a1774d0a9fb34fd2ac58abc1c6db55bd` | 0005Cue0002 | `conditions3` | R |
| `d47984953fc74c488ef0a02588bde92b` | 0005Cue0003 | `conditions4` | R |
| `b474eb4460cb42729be2717d05e7d42b` | 0005Cue0004 | `conditions5` | R |
| `2cd9538f67f7414d808d9032386f6be9` | 0005Cue0006 | `conditions7` | R |
| `64afcd565e044e53977e1878444f4ee1` | 0006Cue0003 | `conditions3` | R |
| `b9e2550bc7244f6c8480106b41667d96` | 0006Cue0004 | `conditions4` | R |
| `bb49f54dc0a547c287238b5d7d8489b3` | 0006Cue0005 | `conditions5` | R |
| `5831af75932d43ed902a2d8def2adf3d` | 0006Cue0006 | `conditions6` | R |
| `8399dbc5987b462594b2b4168764e269` | 0007Cue0002 | `conditions2` | R |


The 22 suppressed cues concern Commander romance, sexual service or its social use.
Calling every one pure romance is imprecise: the cult cues also describe using intimacy to legitimate the cult or control followers, and the divine negotiation cues describe diplomatic access.
Removing those mechanisms after a declined relationship is a reasonable authored change, while the unchanged base cues still retain cult infiltration, rival-cult murder, shadow-church control and divine portfolios.
Do not claim that every subordinate political detail remains verbatim.

The 12 text replacements retain church leadership, Chivarro's church role, Minagho's service and schemes, draconic development and the couple's own history, subject to the specific corrections above.
The service replacements explicitly make Chivarro's relationship to the Commander separately negotiated instead of automatically binding her through Minagho.
That is an authored alternate development justified by the extension's choices, not a fact found in the original parent text.
The unchanged pair cues preserve Chivarro as herald, colleague, lover and companion in their respective parent branches.
The untouched sacrifice cues retain the parent's seclusion, cult redirection and return-to-Abyss outcomes.
The three actual Aeon cues retain their original political activity, remembered Kenabres concern and possible joint departure.

## Concrete integration and checks

For each reviewed S entry, retain the original cue and checker and add only the earned-replacement guard.
For each corrected R entry, retain the original cue for unplayed histories and insert an alternate at the same place in its parent page list using a distinct addon localization key.
The alternate needs the same original condition semantics plus its earned replacement scope; the original needs the complementary scope.
Neither path should execute the other's actions or mark the original cue seen artificially.
Preserve original element ownership and page order, including the parent's ordinary page OnShow that marks all eight ordinary pages seen.
Do not copy that page action onto replacement cues or run it during condition evaluation.
No parent romance, quest, etude or selected-answer history needs to be rewritten.

Main integration should snapshot cue/page structures and verify these cases against the actual reviewed records:

- Unplayed addon save retains every original cue text, condition result, list position, action and native paired fallback selector.
- Invitation-only interruption removes automatic new romance without claiming Chivarro already arrived.
- Earned arrival switches earlier-reunion continuity while preserving the couple's attachment without requiring Commander romance.
- Declined Chivarro, Minagho-only, Chivarro-only, group and closed-group outcomes cannot fall through to an old automatic group intimacy cue.
- Available replacement and already-played replacement both prevent duplicate contradictory relationship paragraphs.
- Redemption/Heaven, each cult branch, divine portfolios, service, Dragon and Legend retain their applicable nonrelationship outcomes.
- Commander sacrifice retains its original parent consequences while true Minagho/Chivarro loss cannot display an unchanged living future.
- Aeon uses only its separate applicable replacement and retains the parent rewritten-history outcomes.
- Failed replacement observation falls back to the original ending, and no condition evaluation runs MarkCuesSeen or other actions.

The source map and native archive checks prove declared identities and selectors.
They do not prove actual parent initialization, a conditional replacement implementation, Unity cue selection, save persistence or rendered epilogue behavior.
Those remain unverified until the corrected contract is implemented and exercised.
