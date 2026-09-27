"""Check exported page portrait keys against staged PNGs, without claiming Unity verification."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import struct


def portrait_key(node):
    return node.get("Portrait") or ("Together" if node["Speaker"] == "Narrator" else node["Speaker"])


def audit(story, folder):
    references = defaultdict(list)
    for scene in story["Scenes"]:
        for node in scene["Nodes"]:
            references[portrait_key(node)].append({"scene": scene["Id"], "node": node["Id"]})
    records = []
    for key, pages in sorted(references.items()):
        record = {"key": key, "pages": len(pages), "first_use": pages[0]}
        if not key or any(part in key for part in ("/", "\\", ":")) or key in (".", ".."):
            record["status"] = "invalid_key"
        else:
            path = folder / (key + ".png")
            if not path.is_file():
                record["status"] = "missing"
            else:
                raw = path.read_bytes()
                if len(raw) < 33 or raw[:8] != b"\x89PNG\r\n\x1a\n" or raw[12:16] != b"IHDR":
                    record["status"] = "invalid_png_header"
                else:
                    width, height = struct.unpack(">II", raw[16:24])
                    record.update(status="present" if width and height else "invalid_dimensions",
                                  width=width, height=height, sha256=hashlib.sha256(raw).hexdigest().upper())
        records.append(record)
    return records


def self_test():
    import tempfile
    assert portrait_key({"Speaker": "Narrator"}) == "Together"
    assert portrait_key({"Speaker": "Areelu", "Portrait": ""}) == "Areelu"
    assert portrait_key({"Speaker": "Narrator", "Portrait": "Study"}) == "Study"
    story = {"Scenes": [{"Id": "scene", "Nodes": [
        {"Id": "one", "Speaker": "Narrator"},
        {"Id": "two", "Speaker": "Areelu"},
        {"Id": "three", "Speaker": "Areelu", "Portrait": "../escape"},
    ]}]}
    with tempfile.TemporaryDirectory() as directory:
        folder = Path(directory)
        (folder / "Together.png").write_bytes(b"broken")
        result = {item["key"]: item["status"] for item in audit(story, folder)}
        assert result == {"Together": "invalid_png_header", "Areelu": "missing", "../escape": "invalid_key"}
    print("PASS: portrait selection, missing assets, invalid headers and unsafe keys")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story", type=Path, default=Path("development/Story.json"))
    parser.add_argument("--assets", type=Path, default=Path("art/CustomNpcPortraits/RanRomance-Tirabade/Scenes"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    raw = args.story.read_bytes()
    records = audit(json.loads(raw), args.assets)
    report = {"story_sha256": hashlib.sha256(raw).hexdigest().upper(),
              "scope": "Exported page keys and staged PNG headers only; no image decoding, visual approval or Unity execution.",
              "assets": str(args.assets.resolve()), "portraits": records}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    failed = [record for record in records if record["status"] != "present"]
    print(f"{len(records)} portrait keys; {len(records) - len(failed)} present; {len(failed)} unresolved")
    for record in failed:
        print(f"{record['key']}: {record['status']} ({record['pages']} pages)")
    raise SystemExit(bool(failed))


if __name__ == "__main__":
    main()
