# Quranic Vocab

A Codex skill for auditing and enforcing one opinionated English naming convention for Quranic concepts in prose and code.

Its 65-concept vocabulary is derived from the [verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0), with local revisions following [community feedback](https://community.itqan.dev/d/757). It preserves singular/plural intent, follows the adopted English `+s` convention, and does not audit Arabic vocabulary.

## Naming choices

Retain specialized Quranic terms when an English equivalent loses a meaningful distinction; prefer ordinary English for general concepts. The September 2026 revision adopts `Word / Words`, `Page / Pages`, and `Letter / Letters` in place of `Kalimah`, `Safhah`, and `Harf`. These mean an orthographic word, a page within a Mushaf edition/layout, and an alphabetic letter respectively. Former names remain legacy alternatives; other canonical names are unchanged.

Each entry has a stable concept key and distinguishes spelling variants, transliterated alternatives, legacy names, English glosses, and related terms. Related terms are never replacement aliases, and explanatory glosses are preserved. Code renders approved names in its existing identifier style; localized UI labels may differ.

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

The approved names and definitions live in [references/vocabulary.md](references/vocabulary.md); behavior and routing live in [SKILL.md](SKILL.md).

## Contributing

Use the [naming policy](references/naming-policy.md) to propose a definition, singular/plural names, rationale, sources, typed alternatives, and prose/code examples. Identify compatibility impacts and transliteration exceptions. Keep existing concept keys stable when changing labels. Proposals become canonical only after explicit maintainer adoption; the skill reports absent concepts as uncovered.

Updating this local vocabulary does not update the source Sheet or migrate external APIs and consumer repositories.
