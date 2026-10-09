#!/usr/bin/env bash
# review.sh <policy|all> [parallel] [--runs PATH] [--manifest PATH]
set -euo pipefail
exec python "$(dirname "${BASH_SOURCE[0]}")/review.py" "$@"
