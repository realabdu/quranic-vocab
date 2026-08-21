# Quranic Vocab

A Codex skill for auditing and enforcing one opinionated English naming convention for Quranic concepts in prose and code.

Its 65-term runtime table is normalized from the [verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0). It preserves singular/plural intent, follows the verified `+s` convention, and does not audit Arabic vocabulary.

## Modes

- `audit` reports inconsistencies without editing and is the default.
- `enforce` applies canonical replacements when explicitly requested.

```text
$quranic-vocab audit <text-or-path>
$quranic-vocab enforce <text-or-path>
```

## Install

```sh
git clone https://github.com/realabdu/quranic-vocab.git ~/.codex/skills/quranic-vocab
```

The convention lives in `references/vocabulary.md`; behavior and routing live in `SKILL.md`.
