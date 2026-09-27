# Minagho and Chivarro revision 3 ending-contract review

The revised metadata resolves the previously reported invitation, single-dragon outcome and death-precedence defects.
It is suitable as the contract for implementation after one additional paired-dragon correction recorded below.
This review does not approve an installed epilogue implementation or the complete routes.
Root reviewed the contract independently of the manuscript author and the prior contract reviewer.

## Evidence and correction

The author froze revision 3 at `6A2D00C5F30E42C5E54E5D16FE338491E39F63784C46CB3DD8695D3814165E49`.
The independent literary reviewer then identified an omitted consequence in paired ascension cue `b9e2550bc7244f6c8480106b41667d96`.
Its revised text preserved achieved draconic mastery but omitted the parent's subsequent two female dragons accompanying the Commander.
Root verified that consequence in the original text and added a neutral sentence preserving the sighting without restoring compulsory romance or permanent inseparability.
The resulting manuscript SHA256 is `BD12627BB8F5BA80DAB93746388BC714E34B058AF76D2F65D6D64CFCC6EAF7FF`.
Only that alternate's text changed after the author freeze; scene graphs, conditions and credited word allocations did not change.
The independent literary reviewer is reviewing this corrected hash separately.

Installed parent DLL SHA256 remains `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Installed parent localization SHA256 remains `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
These were freshly hashed and match the source extraction used by the earlier audit.
Root inspected the extracted Slide0005, Slide0006, Slide0007, Slide0008, SlideAeon and MinaEpil methods, the native paired page and cue, and the full 73-cue evidence map.
The extraction is in `C:/Users/Z/AppData/Local/Temp/minachiv-ending-review-d9010692`.
The earlier review records its extraction provenance and all original page selectors.

## Earned ordinary changes

The metadata now contains 35 ordinary cue entries.
Both parent and native copies of the centuries-later reunion require `minachiv.arrival_kept`, as does the Legend reunion rewrite.
An invitation alone therefore cannot assert that the women have already reunited during the campaign.
The other relationship edits retain their invitation scope so an interrupted invitation does not award Chivarro a Commander romance.
The unfinished addon ending now describes forwarding an answer rather than claiming a completed physical arrival.

Each entry has a private addon localization key.
The two cues that share the native reunion key receive distinct private keys, leaving the shared original text unchanged.
Every ordinary edit forbids either woman's actual death and belongs only to the ordinary epilogue.
The parent page and cue conditions remain requirements in addition to these addon conditions.
The single and paired divine-dragon alternatives now retain achieved mastery and their respective dragon accompaniment outcomes.

## Loss and survivor selection

The three loss rules require earned invitation history and exact native death observations.
Each explicitly lists the interrupted and completed addon ending that must be available or already seen before an original future is suppressed.
Merely reaching a death flag is not permission to leave a blank replacement.
Observation failure must preserve the original behavior until the replacement can be established.

Both-loss and Minagho-loss rules suppress the eight ordinary parent pages and native paired page behind their corresponding replacement.
The Chivarro-loss rule preserves the eight ordinary parent pages, suppresses the pair-only native page, and names 35 original Chivarro-dependent cues for suppression.
Four of those mixed cues gain Minagho survivor alternatives at the same positions under their original conditions.
They preserve church leadership, mortal schemes, divine dragon mastery and dragon flight while removing claims that Chivarro survived.
Every survivor target is also in the suppression set, preventing simultaneous original and replacement text.

An independent scan of all ordinary texts in the 73-cue evidence map found no remaining named Chivarro claim outside that suppression set.
Root also inspected the four original mixed passages beside their survivor alternatives.
No parent selector is replaced with an approximation based on addon romance flags.
No native death, relationship, quest or selected-answer state is rewritten by this contract.

Commander sacrifice alone does not satisfy any of the loss rules.
Existing sacrifice consequences remain under their original conditions when both women survive.
Actual death can still take precedence when independently observed; sacrifice is not being used as proof of that death.
Aeon's distinct page and rewritten lives are excluded from all ordinary loss and reunion changes.

## Structural checks and implementation requirements

Root independently checked all ordinary parent text keys against the evidence map, every suppression target's membership, all 39 private localization keys for uniqueness, and the six listed loss endings against their actual owner and death prerequisites.
The added native paired cue was checked against the extracted native page membership and shared original key.
All checks passed.
These are metadata and source checks, not execution of native condition evaluators or the parent initializer.

MinaEpil assigns the same OnShow action to the eight parent pages, marking their competing pages seen.
Preserve that arbitration, page order, original checkers, cue behavior and localization objects.
Do not copy page actions onto alternate cues or artificially mark original cues seen.
The original parent cues and pages use ShowOnce; the native paired cue and page do not.
The eventual alternate helper must preserve those distinctions and avoid replaying an original under a new alternate GUID.

Native page evaluation can run an earlier cue's actions before checking later cues.
Independent predicates must not allow both an original and its alternate to play if those actions change eligibility.
The helper implementation and its integration hook therefore need separate review of evaluation ordering, stable selection within an evaluation and exception fallback.
No such helper or hook is approved by this metadata review.
Actual parent initialization, epilogue playback, save persistence and ToyBox behavior remain unverified.
