# Quranic Terminology

A Codex skill that audits and enforces an opinionated English naming convention for Quranic concepts in prose and code.

The vocabulary derives from the 65-concept [verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0), with local revisions following [community feedback](https://community.itqan.dev/d/757) and the maintainer-adopted Word Timestamp addition (66 concepts total). It preserves number. Audits use the adopted English `+s` plurals and exclude Arabic vocabulary.

## Choosing terms

Keep specialized Quranic names when English loses a meaningful distinction; use ordinary English for general concepts. The September 2026 revision replaces `Kalimah`, `Safhah`, and `Harf` with `Word / Words`, `Page / Pages`, and `Letter / Letters`: orthographic words, pages within a Mushaf edition/layout, and alphabetic letters. Former names remain legacy alternatives; other canonical names are unchanged.

Entries have stable keys and typed alternatives: spelling variants, transliterated forms, legacy names, English glosses, and related terms. Explanatory glosses are preserved; related terms are never replacement aliases. Code retains its identifier style, and localized UI labels may differ.

## Usage

`audit` reports inconsistencies without editing and is the default. Use `enforce` to request canonical replacements explicitly.

```text
$quranic-terminology audit <text-or-path>
$quranic-terminology enforce <text-or-path>
```

```sh
git clone https://github.com/realabdu/quranic-terminology.git ~/.codex/skills/quranic-terminology
```

Read [references/vocabulary.md](references/vocabulary.md) for names and definitions, and [SKILL.md](SKILL.md) for behavior.

Previously named `quranic-vocab`. For an existing installation, rename its
skill directory to `quranic-terminology`, update its Git remote to the URL
above, and pull the renamed skill. Avoid keeping both copies installed.

## Automated pre-commit checks

[quranic-terminology-lint](https://github.com/realabdu/quranic-terminology-lint)
provides a separate deterministic CLI and pre-commit hook. It bundles a
180-entry Quran.ws snapshot, not this skill's 66-concept vocabulary; the two
tools do not currently guarantee identical terminology decisions.

Both use `word_timestamp` / `word_timestamps` for word-level audio spans,
with `word_timing` / `word_timings` retained as legacy alternatives.

## Contributions

Follow the [naming policy](references/naming-policy.md): supply a definition, singular/plural names, rationale, sources, typed alternatives, and prose/code examples. Explain compatibility impacts and transliteration exceptions; retain existing concept keys.

Only explicit maintainer adoption makes a proposal canonical. Unlisted concepts remain uncovered, and local revisions do not update the source Sheet or migrate external APIs and consumer repositories.
