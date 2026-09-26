# Expansion development package verification

The current package is `dist/expansion-20260926-193512-4a81ee50`, containing 533 scenes.
Its [integration checkpoint](konomi-missed-contact-integration-checkpoint.md) records the exact hashes, successful full checks, independent payload verification and remaining requirements.
The 527-scene builds below are retained historical packaging evidence.

The existing `build.ps1` invokes `story.py`, and the original package contains thirty-four scenes with no Konomi route.
The new `build-expansion.ps1` provides a separate build target that generates `development/Story.json` and stages matching binaries and portrait files under a fresh `dist/` directory.
It does not invoke the original story generator or install files into the game.
The incomplete-package instructions are maintained in `development/PLAYTEST-PACKAGE.md`.

Root executed the new build with the explicit interpreter `C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64/python.exe`.
Source, narrator and managed-test builds passed with zero warnings and errors.
The packaged expansion passed 24,107,203 Rules assertions, 949 native binding uses and 64,462 managed construction assertions.
Managed construction covered 527 scenes and 18,853 generated blueprints.

Output: `dist/expansion-20260926-185932-feed305b`.
Packaged Story SHA256: `0CB9BDDB2BA353FED08E2C43A58A63BE798C0A73356D46367CFBC73BD1FE7387`.
Rebuilt and tested DLL SHA256: `C82DEA6C519D5E47B5D101947181CC60CD765A06E0ECB63031C356DDDF667687`.
This is the binary tested by this build, superseding the earlier binary hash for this artifact only.

The generated manifest lists twenty-one payload files, their hashes, the story hash, scene count and missing portrait keys.
Root independently reopened the package, verified every listed hash, counted all 527 scenes and confirmed that all sixty-four Konomi entries and both staged Konomi images are present.
The manifest itself is an additional file and is not recursively hashed inside its own file list.

Missing requested image keys are Aivu, Aranka, Arsinoe, Ember, Gesmerha, Ista, Jerribeth-Guise, Kiana, Seelah, Soana, Tovin and Vellexia.
These are portrait lookup keys, not twelve additional characters.
Approved `ArsinoeShop` and `GesmerhaWorkshop` files remain distinct unassigned keys rather than silent replacements for every setting.
The report exposes missing assets without claiming that staged images have all passed scene and runtime review.

Both the original package Story and installed addon Story retained SHA256 `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4` after execution.
The script restores its temporary reader environment variables and uses a new output directory each time, avoiding old-package residue.
No installed files or saves were changed.

This establishes local packaging of the expansion, not a completed character release.
The ordinary Konomi campaign can be selected for a future manual test after deliberate deployment preparation.
Missing bespoke access, scene artwork and actual Unity/save/ToyBox verification remain separate requirements.

## Revalidation after independent packaging review

Independent static review identified that a concurrently regenerated Story could be staged after a different version had passed validation.
The build now pins the generated Story hash before checks and rejects changed input after validation or changed staged output before writing a successful manifest.
This finding was static; no concurrent failure was claimed as reproduced.
The amended build completed with the same 527-scene Story hash and the same successful assertion totals above.
Its output is `dist/expansion-20260926-190356-2036160c`.
Its rebuilt, tested assembly hash is `3FD90EBB20942AC89A67BE78DAD36C14E771AE2896233B48C32FD478D9067197`.
Root independently verified all twenty-one payload hashes against the new manifest.
The installed Story still has the original `3176BB0102324BAB5BAF664D6956D5DEB3A4FB638029789D74F0EFCDF73DC6D4` hash.
