# Quranic Vocab

A Codex skill for auditing and enforcing an opinionated English naming convention for Quranic concepts in prose and code.

The bundled table contains 65 canonical terms normalized from the [verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0). It standardizes forms such as `Surah`, `Ayah`, and `Juz`, preserves singular/plural intent, uses the verified `+s` plural convention, and does not audit Arabic vocabulary.

## Modes

- `audit` reports noncanonical and ambiguous terms without editing. It is the default.
- `enforce` applies canonical replacements to prose and code, preserves identifier style, and validates the result.

```text
$quranic-vocab audit <text-or-path>
$quranic-vocab enforce <text-or-path>
```

For a deterministic first pass over a repository:

```sh
python3 scripts/quranic_vocab_scan.py <path> [<path> ...]
```

The scanner finds candidates; the skill then uses context to distinguish violations from ambiguous uses, proper names, quotations, and immutable external literals.
Directory scans exclude generated/data/public-asset trees and lockfiles by default; pass `--include-generated` when those artifacts are intentionally in scope.

## Install

Clone the repository into your personal Codex skills directory:

```sh
git clone https://github.com/realabdu/quranic-vocab.git ~/.codex/skills/quranic-vocab
```

## Contents

- `SKILL.md` defines routing and behavior.
- `references/vocabulary.md` contains the canonical 65-term table.
- `scripts/quranic_vocab_scan.py` performs deterministic candidate discovery.
- `tests/` contains scanner regression coverage.
- `agents/openai.yaml` provides Codex UI metadata.
