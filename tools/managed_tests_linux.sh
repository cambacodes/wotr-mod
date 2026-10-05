#!/usr/bin/env bash
# Construction preflight against real game assemblies; no game process is started.
set -euo pipefail

repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
game=$(realpath -- "${1:-/wrath}")
story=$(realpath -- "${2:-$repo/development/Story.json}")
python=$(command -v -- "${RRT_PYTHON:-python3}")
export RRT_PYTHON=$python
export RRT_TEST_REPO_ROOT=$repo
export RRT_GAME_DIR=$game
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

# Match build-expansion.ps1, including the optional Terendelev parent manifest.
bindings=()
for name in expansion-parent-bindings nurah-parent-bindings nurah-parent-runtime-cue-bindings terendelev-parent-bindings; do
    file="$repo/reference/canon-review/$name.json"
    if [[ -f "$file" ]]; then bindings+=("$file"); fi
done
export RRT_PARENT_BINDINGS=$(IFS=:; echo "${bindings[*]}")
# These select different suites/negative fixtures and must not leak into this run.
unset RRT_TEST_LOAD RRT_TEST_MISSING_ETUDE RRT_TEST_NATIVE_RETURN

scratch=$(mktemp -d /tmp/rrt-managed-linux.XXXXXX)
trap 'rm -rf -- "$scratch"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
export RRT_TEST_MOD_DIR="$scratch/mod"
cd -- "$repo"

dotnet build src/Tirabade.csproj -c Release --nologo -v quiet \
    "-p:GameDir=$game/" "-p:BaseIntermediateOutputPath=$scratch/src-obj/" \
    "-p:OutputPath=$RRT_TEST_MOD_DIR/"
dotnet build managed-tests/ManagedBuildTests.csproj -c Release --nologo -v quiet \
    "-p:GameDir=$game/" "-p:BaseIntermediateOutputPath=$scratch/tests-obj/" \
    "-p:OutputPath=$scratch/tests/" "-p:ModAssemblyPath=$RRT_TEST_MOD_DIR/RanRomance.Tirabade.dll"

for mode in 0 1 wrong-type; do
    echo "Managed construction fixture: RRT_TEST_EXPANDED_EPILOGUE=$mode"
    RRT_TEST_EXPANDED_EPILOGUE=$mode mono "$scratch/tests/ManagedBuildTests.exe" "$game" "$story"
done
