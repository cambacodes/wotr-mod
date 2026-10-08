# Art pass 1: missing book portraits (2026-09-28)

One fast pass under memory `rrt-art-direction`. Every candidate image copied here was viewed before it was accepted.
Result: missing portrait keys went from **53 to 15**, and letter senders with art from 6/27 to **26/27** (the one left, "Memory", is an abstract sender).
No new images were generated: native portraits, reviewed candidates and aliases covered every character key.

**How the key resolves** (in order): `Scenes/<key>.png`, then `PortraitFallbacks[key]`. The fallback is a native BlueprintPortrait GUID (half-length, then full-length, then small) or an alias to another key. See `storylines/rrt_portraits.py` and `Main.FallbackPortrait`.

## Copied candidates (source: `main`, read-only)

| Key | Source | Inspection |
|---|---|---|
| Aranka | candidate main art/candidates/aranka/portrait-v1.png | PASS: strong likeness to native (braids, blue eyes, blue dress); attractive adult; clean hands |
| Chadali | candidate chadali/council-cookie-v2.png | PASS: recognizable, attractive adult, cookie motif; old review hold was drape/gloss polish (accepted for fast pass) |
| Eritrice | candidate eritrice/council-minutes-v4.png | PASS: humanized lioness, attractive, canon minutes motif; chosen over council-address-v1 (harsher, older-reading face) |
| Devarra | candidate art/candidates/Devarra-v1.png | PASS: humanoid red-dragon woman, attractive adult, dragon cues; the dragon-form scene candidates were rejected as the default portrait |
| Dorgelinda | candidate dorgelinda/dorgelinda-logistics-v1.png | PASS (improve later): recognizable (grey bob, eyepatch, officer coat), adult; plain rather than glamorous |
| Hepzamirah | candidate hepzamirah/living-nephilim-portrait-v1.png | PASS: native nephilim cues humanized, powerful, attractive; non-explicit |
| Kiana | candidate kiana/rehearsal-start-v1.png | PASS: native blue crystalline oread look, readable face, letter in hand |
| Minagho | candidate minagho/minagho-released-glove-v1.png | PASS: eyeless lilitu (canon), horns, attractive, character-true action; non-explicit |
| Chivarro | candidate chivarro/chivarro-native-inspired-v1.png | PASS: eyeless lilitu, warm blond hair, alluring, non-explicit; full-length (small face at book size) |
| Herrax | candidate herrax/herrax-madam-v1.png | PASS: scarred succubus madam offering a coin; recognizable, non-explicit |

## Native portraits (the character's own in-game art)

| Key | BlueprintPortrait | Note |
|---|---|---|
| Seelah | `0ebca33b0e5eb514aa75d9989a565f2f` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Camellia | `d227d31233aa2494fba89cb715afbb87` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Daeran | `16456c362f6535c4a81c625d917b30dd` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Lann | `b9fea9f24838d43469948aa54088d600` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Regill | `ea0e28ad6b566444885ef21357f76a87` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Sosiel | `d721e6b0cf0634e41a070531bcfd1f92` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Woljif | `cd965f50af3cfba4c81b55c9951e7afa` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Ulbrig | `1faff0d995004389a6638388d6d4b5f2` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Wenduag | `c883d02a0d8a4b54f903d351c8fd6af7` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Greybor | `c542695eee15988478d4fa07a1eddb0e` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Ember | `0b3d046086ea25b4bad5d5306e6a7612` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Aivu | `1f5bfefa49a8aa2449ad94b1f4f61788` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Galfrey | `a3ba06b4723c7a74fb5054ccb2289efb` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Areelu | `1d19be67a5a2458dacc608493ea4d6b2` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Nurah | `4409935f79a11c24980c1c8f70b328f6` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Nenio | `2b4b8a23024093e42a5db714c2f52dbc` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Finnean | `945a5699771b53c46978009ef8075622` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Storyteller | `ca7e9df2ad3b43843894e3a393a5d08d` | proper portrait; canon look; matches the brief (in-game outfit, recognizable) |
| Baphomet | `88e4b1b15bf04633b971ca80ef7605bd` | initiative image only (184x244, soft at book size); non-romance NPC, correct face |
| Socothbenoth | `5bc3985a76b94ae3ad133a2cd2e765af` | initiative image only (184x244, soft at book size); non-romance NPC, correct face |
| Kyado | `efcd57ef238d483391bf5360b2821ba9` | initiative image only (184x244, soft at book size); non-romance NPC, correct face |
| Mutasafen | `fbbe968abe1d4cdabc31af520526cc8b` | initiative image only (184x244, soft at book size); non-romance NPC, correct face |

## Aliases to art already shipped in the mod

| Key | Uses |
|---|---|
| Arsinoe | `ArsinoeShop.png` |
| Gesmerha | `GesmerhaWorkshop.png` |
| Soana | `SoanaForest.png` |
| Targona | `TargonaCorrespondence.png` |
| Vellexia | `VellexiaManorSpeaker.png` |

## Still missing (15): keep the native book picture

Generic or minor NPCs with no native portrait: Chaplain, Court clerk, Crusade general, Golem, Ista, Mendevian woman, Nerath, Oswin, Rasen, Sava, Sivane, Smith, Tovin.
Also Ramisa (only a generic marilith monster icon exists) and Jerribeth-Guise (a disguise; aliasing Jerribeth would spoil it).

## Follow-ups for a later pass

- **Dorgelinda:** a more glamorous default portrait within her character.
- **Chivarro:** a closer bust crop for book size.
- **Initiative-only natives** (Baphomet, Socothbenoth, Kyado, Mutasafen): upscale or repaint if they look soft in game.
- **Wenduag and Nenio** use native art. If the humanized-redesign brief should apply to them for their romance routes, their route passes should add custom art.
- **Not yet verified live:** that native portrait sprites render as book pictures. Include one letter from Seelah and one from Nurah in the next live harness run.
