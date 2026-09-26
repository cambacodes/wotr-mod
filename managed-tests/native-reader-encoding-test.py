"""Reproduce Windows text decoding failure and check the actual native reader.

Usage: python managed-tests/native-reader-encoding-test.py path/to/blueprints.zip
"""
import codecs
import json
import os
from pathlib import Path
import subprocess
import sys

guid = "b5f301fbc4c44535a6309d610d5bd28a"
request = json.dumps([guid]).encode("utf-8")
environment = dict(os.environ, PYTHONIOENCODING="cp1252")
old = subprocess.run([sys.executable, "-c", "import json,sys; json.load(sys.stdin)"],
                     input=codecs.BOM_UTF8 + request, capture_output=True, env=environment)
assert old.returncode != 0 and b"Expecting value: line 1 column 1" in old.stderr, old.stderr
reader = Path(__file__).with_name("read-native.py")
for payload in (request, codecs.BOM_UTF8 + request):
    result = subprocess.run([sys.executable, str(reader), sys.argv[1]],
                            input=payload, capture_output=True, env=environment)
    assert result.returncode == 0, result.stderr
    assert list(json.loads(result.stdout)) == [guid], result.stdout[:200]
print("PASS: old text-reader failure reproduced; actual archive reader accepts plain and BOM-prefixed UTF-8 under cp1252.")
