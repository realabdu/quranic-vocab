# Quranic Vocab

A Codex skill for auditing and enforcing an opinionated English naming convention for Quranic concepts in prose and code.

The bundled table contains 65 canonical terms normalized from the [verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0). It standardizes forms such as `Surah`, `Ayah`, and `Juz`, uses the verified `+s` plural convention, and does not audit Arabic vocabulary.

## Modes

- `audit` reports noncanonical and ambiguous terms without editing. It is the default.
- `enforce` applies canonical replacements to prose and code, preserves identifier casing, and validates the result.

```text
$quranic-vocab audit <text-or-path>
$quranic-vocab enforce <text-or-path>
```

## Install

Clone the repository into your personal Codex skills directory:

```sh
git clone https://github.com/realabdu/quranic-vocab.git ~/.codex/skills/quranic-vocab
```

## Contents

- `SKILL.md` defines routing and behavior.
- `references/vocabulary.md` contains the canonical 65-term table.
- `agents/openai.yaml` provides Codex UI metadata.
