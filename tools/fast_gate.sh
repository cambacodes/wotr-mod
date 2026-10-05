#!/usr/bin/env bash
set -euo pipefail
repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
exec "${RRT_PYTHON:-python3}" "$repo/tools/test_gate.py" "$@"
