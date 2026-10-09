#!/usr/bin/env bash
# review.sh <policy|all> [parallel]: Luna (gpt-6-luna, medium) reviews every checkpoint dossier under the strict
# reviewer contract; then the investigator (gpt-6.1-sol, medium: Terra's role - no Terra model on this account)
# re-checks only dossiers with "uncertain" findings. Read-only; outputs runs/<policy>/review/<dossier>.{luna,terra}.json.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")"
policies=${1:-all}; par=${2:-4}
[ "$policies" = all ] && policies="trickster_all_romance trickster_villain nontrickster_good hostile"
KNOW=${RRT_KNOWLEDGE:-C:/Users/Z/Documents/Projects/Writer/knowledge}
LUNA=${RRT_LUNA:-gpt-6-luna}; TERRA=${RRT_TERRA:-gpt-6.1-sol}
ROOT=$(cd ../.. && pwd)

luna() {  # $1 = dossier path relative to tools/playthrough
  d=$1; out=$(dirname "$d")/review/$(basename "$d" .md).luna.json
  [ -s "$out" ] && python -c "import json,sys;json.load(open(sys.argv[1],encoding='utf-8'))" "$out" 2>/dev/null && return 0
  mkdir -p "$(dirname "$out")"
  { cat reviewer-contract.md
    printf '\n\nTASK: review ONE dossier: tools/playthrough/%s (repo root = current directory).\n' "$d"
    printf 'Knowledge base (read-only): %s/characters/<id>/ (canon.md, voice.md, states.md, relationships.md, decisions.md, native-lines.json).\n' "$KNOW"
    printf 'Read the whole dossier first, then the knowledge files of every woman in its appendix before any character finding.\n'
    printf 'Work scene by scene through checklist items 1-8, then the chapter as a whole. Prefer fewer, well-evidenced findings over many vague ones.\n'
    printf 'Mark "certainty":"uncertain" whenever you cannot verify a claim from the dossier and knowledge files alone.\n'
    printf 'Output ONLY the JSON object required by the contract (schema: tools/playthrough/reviewer-schema.json). No prose before or after.\n'
  } | codex exec -m "$LUNA" -s read-only -C "$ROOT" --skip-git-repo-check --ephemeral \
      -c 'model_reasoning_effort="medium"' -o "$out.tmp" - > "$out.log" 2>&1
  python - "$out.tmp" "$out" <<'PY'
import json, re, sys
raw = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'\{.*\}', raw, re.S)
obj = json.loads(m.group(0))
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(json.dumps(obj, ensure_ascii=False, indent=1) + '\n')
PY
  rm -f "$out.tmp"; if [ -s "$out" ]; then rm -f "$out.log"; echo "luna ok $d"; else echo "luna FAILED $d (see $out.log)"; fi
}

terra() {  # re-check uncertain findings of one dossier
  d=$1; base=$(dirname "$d")/review/$(basename "$d" .md); in=$base.luna.json; out=$base.terra.json
  [ -s "$in" ] || return 0
  n=$(python -c "import json,sys;o=json.load(open(sys.argv[1],encoding='utf-8'));print(sum(1 for f in o.get('findings',[]) if f.get('certainty')=='uncertain'))" "$in")
  [ "$n" -gt 0 ] || return 0
  [ -s "$out" ] && return 0
  { cat reviewer-contract.md
    printf '\n\nTASK (investigator): re-check ONLY the findings marked uncertain in tools/playthrough/%s against the dossier tools/playthrough/%s, the knowledge base %s and development/Story.json.\n' "$in" "$d" "$KNOW"
    printf 'Focus on motivation, cause and effect and subtle contradictions. For each uncertain finding: keep it as certain (with better evidence), revise it, or drop it.\n'
    printf 'Output ONLY a JSON object {"findings":[...kept or revised findings, same schema, certainty set to certain...], "dropped":[{"id":...,"reason":...}]}.\n'
  } | codex exec -m "$TERRA" -s read-only -C "$ROOT" --skip-git-repo-check --ephemeral \
      -c 'model_reasoning_effort="medium"' -o "$out.tmp" - > "$out.log" 2>&1
  python - "$out.tmp" "$out" <<'PY'
import json, re, sys
raw = open(sys.argv[1], encoding='utf-8').read()
obj = json.loads(re.search(r'\{.*\}', raw, re.S).group(0))
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(json.dumps(obj, ensure_ascii=False, indent=1) + '\n')
PY
  rm -f "$out.tmp"; [ -s "$out" ] && rm -f "$out.log"; echo "terra ok $d ($n uncertain)"
}
export -f luna terra; export KNOW LUNA TERRA ROOT

for p in $policies; do ls runs/$p/chapter-*.md; done | sed "s#^#./#; s#^\./##" > /tmp/rrt-dossiers.txt
echo "dossiers: $(wc -l < /tmp/rrt-dossiers.txt)"
xargs -a /tmp/rrt-dossiers.txt -P "$par" -I{} bash -c 'luna "$@"' _ {} < /dev/null
xargs -a /tmp/rrt-dossiers.txt -P "$par" -I{} bash -c 'terra "$@"' _ {} < /dev/null
echo "review done"
