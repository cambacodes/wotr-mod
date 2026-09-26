import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).parent
version = json.loads((ROOT / "package/Info.json").read_text())["Version"]
dist = ROOT / "dist"
dist.mkdir(exist_ok=True)
with ZipFile(dist / f"ThreeAtTheTable-{version}.zip", "w", ZIP_DEFLATED) as archive:
    for file in (ROOT / "package").iterdir():
        if file.is_file():
            archive.write(file, "Mods/RanRomanceTirabade/" + file.name)
    for file in (ROOT / "art/CustomNpcPortraits").rglob("*.png"):
        archive.write(file, "Mods/CustomNpcPortraits/" + file.relative_to(ROOT / "art/CustomNpcPortraits").as_posix())
    archive.write(ROOT / "release-install.ps1", "Install-ThreeAtTheTable.ps1")
    archive.write(ROOT / "README.md", "README.md")
with ZipFile(dist / f"ThreeAtTheTable-source-{version}.zip", "w", ZIP_DEFLATED) as archive:
    for folder in ("src", "narrator", "tests", "managed-tests", "storylines", "data", "art"):
        for file in (ROOT / folder).rglob("*"):
            if file.is_file() and not any(part in ("bin", "obj", "__pycache__") for part in file.parts):
                archive.write(file, file.relative_to(ROOT))
    for filename in ("story.py", "story_format.py", "expansion.py", "build.ps1", "install.ps1", "prepare-portraits.ps1", "release-install.ps1", "package-release.py", "README.md", "EXPANSION.md", "ROSTER.md", ".gitignore", ".gitattributes"):
        archive.write(ROOT / filename, filename)
    for file in (ROOT / "tools").glob("*.py"):
        archive.write(file, file.relative_to(ROOT))
    archive.write(ROOT / "reference/canon-review/targona-parent-bindings.json", "reference/canon-review/targona-parent-bindings.json")
    archive.write(ROOT / "reference/canon-review/aranka-parent-bindings.json", "reference/canon-review/aranka-parent-bindings.json")
    archive.write(ROOT / "reference/canon-review/expansion-parent-bindings.json", "reference/canon-review/expansion-parent-bindings.json")
    archive.write(ROOT / "reference/expansion/etudes.json", "reference/expansion/etudes.json")
    archive.write(ROOT / "package/Info.json", "package/Info.json")
for archive in dist.glob("*.zip"):
    with ZipFile(archive) as opened:
        assert opened.testzip() is None
    print(archive, f"{archive.stat().st_size:,} bytes")
