---
name: quranic-vocab
description: Audit or enforce an opinionated English naming convention for Quranic concepts in prose and code. Use for terminology such as Surah, Ayah, Juz, Mushaf, and Riwayah. Excludes Arabic vocabulary and orthography.
---

# Quranic Vocabulary

Read [references/vocabulary.md](references/vocabulary.md) in full before each pass. Its names, definitions, and typed alternatives govern the result; repository usage and provider preferences do not override them. Read [references/naming-policy.md](references/naming-policy.md) when explaining choices or proposing revisions.

## Modes

| Mode | Trigger | Mutates |
| --- | --- | --- |
| `audit` | Bare invocation; audit, evaluate, diagnose, review, check | No |
| `enforce` | Explicitly fix, correct, rename, update, apply, enforce | Yes |

Default to `audit`; never edit without clear `enforce` intent. Audit English prose and code only. Never audit Arabic words, spelling, articles, or diacritics. Localized UI labels may differ while sharing a stable concept key.

## Names and number

Use the listed canonical singular and `+s` plural. Match spelling, transliteration, and legacy alternatives only when they name the same concept. Replace a gloss only when used as that concept's name; preserve explanations. Related terms are never aliases.

Preserve grammatical number: `Riwayat` becomes `Riwayahs`, not `Riwayah`. Where a canonical plural exists, consider mechanical `+s` forms of singular alternatives with their original type: `Kalimah` → `Kalimahs` → `Words`; naming use of `Verse` → `Verses` → `Ayahs`. Explicit number entries take precedence; never derive aliases from related terms.

`Qira'at` appears in both number columns. Use grammar, types, and usage to resolve number, including punctuation-free identifiers such as `qiraat`. A single reading maps to `Qira'ah`, multiple readings to `Qira'ahs`; insufficient context means ambiguous and unchanged.

When the plural column is `—`, do not invent a plural, and report plural usage as unsupported. Report absent Quranic English concepts as uncovered, without inventing replacements.

## Matching

Match complete words and identifier tokens case-insensitively, using longest-match precedence. Canonical singulars and plurals protect shorter forms inside them: `Sura` in `Surah`, `Aya` in `Ayah`, `Riwaya` in `Riwayah`, `Word` in `Word Root`, and `Recitation` in `Murattal Recitation`. Do not match arbitrary substrings.

Recognize snake_case, camelCase, PascalCase, kebab-case, and SCREAMING_SNAKE_CASE in code, schemas, and filenames. Preserve identifier style: remove apostrophes and modifier punctuation within words, split spaces and hyphens into tokens, then apply the target's casing and separators. Prose retains exact table spelling; code renderings are not additional prose spellings.

- `verse_count` → `ayah_count`
- `VerseRange` → `AyahRange`
- `kalimah_count` → `word_count` (orthographic words)
- `SafhahRange` → `PageRange` (a Mushaf layout)
- `HARF_COUNT` → `LETTER_COUNT` (alphabetic letters)
- `qiraat_id` → `qiraah_id` only for a documented single reading
- `GRAMMATICAL_ANALYSIS` → `IRAB`
- `Rub al-Hizb` → `rub_al_hizb` or `RubAlHizb`

## Classification

Inspect surrounding prose, symbols, types, and schema descriptions against the definitions. A Quran-related file alone does not establish a term's meaning. Generic web `page`, book `chapter`, and ordinary `word` uses are valid. Do not rename characters, glyphs, morphological segments, or other senses of harf to Word, Page, or Letter.

- **Confirmed inconsistency:** a noncanonical name for the same Quranic concept.
- **Ambiguous:** meaning or number is unclear; never treat it as confirmed.
- **Intentional mention:** a proper name, brand, quotation, research comparison, explanatory gloss, URL, command, or immutable external contract literal. Preserve it, including `An Ayah is often translated as “verse”.` Owned names around external literals still follow the convention.
- **Uncovered:** a distinct Quranic English concept absent from the table; report without replacement.

## Audit

Resolve the requested text, files, directories, or changes. Search typed alternatives, eligible derived `+s` forms, and identifier forms using tools such as `rg`; exclude related terms from alias matching. Inspect and classify each candidate without editing.

For confirmed inconsistencies, report location, concept key, alternative type, found form, and replacement. List ambiguous, intentional, and uncovered occurrences separately. Report when no confirmed inconsistency remains; claim conformity only if no ambiguous, uncovered, or unsupported plural usage remains.

## Enforce

Audit first, then correct confirmed inconsistencies while preserving meaning, grammar, number, and style. In code, rename owned symbols across declarations, references, schemas, tests, and relevant filenames. Do not blind-replace text or mutate intentional literals; leave ambiguous and uncovered occurrences unchanged.

Run relevant validation and re-audit, then report changed files and unresolved findings.
