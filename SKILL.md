---
name: quranic-vocab
description: Audit or enforce an opinionated English naming convention for Quranic concepts in prose and code using a bundled canonical vocabulary table. Use when reviewing, writing, or standardizing English Quranic terminology such as Surah, Ayah, Juz, Mushaf, or Riwayah. Do not use for Arabic vocabulary or orthography.
---

# Quranic Vocabulary

Standardize English Quranic vocabulary against [references/vocabulary.md](references/vocabulary.md). Read the complete table before every pass; it is the sole source of truth. Repository usage, providers, and preference do not override it.

## Modes

| Mode | Trigger | Mutates |
| --- | --- | --- |
| `audit` | Bare invocation; audit, evaluate, diagnose, review, check | No |
| `enforce` | Explicitly fix, correct, rename, update, apply, enforce | Yes |

Default to `audit`. Never edit without clear `enforce` intent.

## Canonical convention

- Audit English prose and code. Never audit Arabic words, spelling, articles, or diacritics.
- The table's canonical singular and canonical `+s` plural are the only standard forms for a concept.
- Map listed singular alternatives to the canonical singular and listed plural alternatives to the canonical plural. Thus `Riwayat` maps to `Riwayahs`, not `Riwayah`.
- When a canonical plural exists, also treat the mechanical `+s` form of each singular alternative as a plural candidate: `Verse` → `Verses` → `Ayahs`.
- When the plural column is `—`, do not invent a plural. Report clearly plural usage as unsupported.
- Report a Quranic English concept absent from the table as uncovered; never invent its replacement.

## Matching

Use longest-match precedence. Every complete canonical singular or plural shields shorter forms inside it: do not flag `Sura` in `Surah`, `Aya` in `Ayah`, `Riwaya` in `Riwayah`, `Word` in `Word Root`, or `Recitation` in `Murattal Recitation`.

Recognize forms case-insensitively in prose and inside snake_case, camelCase, PascalCase, kebab-case, SCREAMING_SNAKE_CASE, schemas, and filenames. Preserve the target's identifier style. Remove apostrophes and modifier punctuation inside canonical lexical words when rendering identifiers, but retain exact table spelling in prose:

- `verse_count` → `ayah_count`
- `VerseRange` → `AyahRange`
- `qiraat_id` → `qiraah_id`
- `GRAMMATICAL_ANALYSIS` → `IRAB`

## Classification

A match is a confirmed inconsistency only when it names the Quranic concept. Inspect surrounding prose, symbols, types, and schema descriptions. Generic uses such as a web `page`, book `chapter`, or ordinary `word` are not violations.

Use four classifications:

- **Confirmed inconsistency:** noncanonical name for the Quranic concept.
- **Ambiguous:** context or grammatical number is insufficient. Never silently promote it to confirmed.
- **Intentional mention:** the exact string is a proper name, brand, quotation, research comparison, URL, command, or immutable external contract literal. This is not an alias exemption; owned names around an external literal remain canonical.
- **Uncovered:** Quranic English term absent from the table; report without replacement.

## Audit

1. Resolve the requested text, files, directories, or changes.
2. Search all table alternatives, eligible derived `+s` forms, and identifier forms. Use repository search such as `rg` for codebases.
3. Inspect context and classify each candidate.
4. Report confirmed inconsistencies with location, found form, and canonical replacement. Report ambiguous, intentional, and uncovered occurrences separately.
5. Make no changes.

If no confirmed inconsistency remains, say the target conforms to the table.

## Enforce

1. Audit first.
2. Correct confirmed inconsistencies only.
3. Preserve prose meaning, grammar, number, and style.
4. In code, rename owned symbols coherently across declarations, references, schemas, tests, and relevant filenames. Do not blind-replace text or mutate intentional literals.
5. Leave ambiguous and uncovered occurrences unchanged.
6. Run relevant validation, re-audit, and report changed files plus anything unresolved.
