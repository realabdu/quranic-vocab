---
name: quranic-vocab
description: Audit or enforce an opinionated English naming convention for Quranic concepts in prose and code using a bundled canonical vocabulary table. Use when reviewing, writing, or standardizing English Quranic terminology such as Surah, Ayah, Juz, Mushaf, or Riwayah. Do not use for Arabic vocabulary or orthography.
---

# Quranic Vocabulary

Standardize English Quranic vocabulary against [references/vocabulary.md](references/vocabulary.md). Read the complete reference, including definitions and typed alternatives, before every pass; it is the sole source of approved names. Repository usage, providers, and preference do not override it during an audit or enforcement pass. For questions about naming choices or proposed vocabulary changes, also read [references/naming-policy.md](references/naming-policy.md).

## Modes

| Mode | Trigger | Mutates |
| --- | --- | --- |
| `audit` | Bare invocation; audit, evaluate, diagnose, review, check | No |
| `enforce` | Explicitly fix, correct, rename, update, apply, enforce | Yes |

Default to `audit`. Never edit without clear `enforce` intent.

## Canonical convention

- Audit English prose and code. Never audit Arabic words, spelling, articles, or diacritics.
- Stable concept keys identify reference entries independently of labels. Localized UI labels may differ; this skill does not require the same string in every language or context.
- The table's canonical singular and canonical `+s` plural are the only standard forms for a concept.
- Map confirmed singular alternatives to the canonical singular and confirmed plural alternatives to the canonical plural. Thus `Riwayat` maps to `Riwayahs`, not `Riwayah`.
- Spelling, transliteration, and legacy alternatives are normalization candidates only for the same concept. A gloss is a candidate only when functioning as that concept's name. Preserve explanatory glosses. Related terms are never replacement aliases.
- When a canonical plural exists, also consider mechanical `+s` forms of singular alternatives, retaining their type: `Kalimah` → `Kalimahs` → `Words`; naming use of `Verse` → `Verses` → `Ayahs`. Do not derive aliases from related terms. Explicit number entries take precedence over derived candidates.
- `Qira'at` occurs in both number columns. Determine number from grammar, types, and use, including punctuation-free identifiers such as `qiraat`. A documented single reading maps to `Qira'ah`; multiple readings map to `Qira'ahs`. Without sufficient context, report ambiguous and leave unchanged.
- When the plural column is `—`, do not invent a plural. Report clearly plural usage as unsupported.
- Report a Quranic English concept absent from the table as uncovered; never invent its replacement.

## Matching

Use longest-match precedence. Every complete canonical singular or plural shields shorter forms inside it: do not flag `Sura` in `Surah`, `Aya` in `Ayah`, `Riwaya` in `Riwayah`, `Word` in `Word Root`, or `Recitation` in `Murattal Recitation`.

Recognize complete words and identifier tokens case-insensitively in prose and inside snake_case, camelCase, PascalCase, kebab-case, SCREAMING_SNAKE_CASE, schemas, and filenames; do not match arbitrary substrings. Preserve the target's identifier style. To render an identifier, remove apostrophes and modifier punctuation inside words, split spaces and hyphens into token boundaries, then apply the target's casing and separators. Retain exact table spelling in prose. Rendered canonical identifiers are valid in code, not additional canonical prose spellings:

- `verse_count` → `ayah_count`
- `VerseRange` → `AyahRange`
- `kalimah_count` → `word_count` (orthographic words)
- `SafhahRange` → `PageRange` (a Mushaf layout)
- `HARF_COUNT` → `LETTER_COUNT` (alphabetic letters)
- `qiraat_id` → `qiraah_id` only when it identifies a single reading
- `GRAMMATICAL_ANALYSIS` → `IRAB`
- `Rub al-Hizb` → `rub_al_hizb` or `RubAlHizb`

## Classification

A match is a confirmed inconsistency only when it names the same Quranic concept. Inspect surrounding prose, symbols, types, and schema descriptions, using the reference definitions where provided. A Quran-related file alone does not establish the meaning of Word, Page, or Letter. Generic uses such as a web `page`, book `chapter`, or ordinary `word` are not violations. Characters, glyphs, morphological segments, and other senses of harf must not be collapsed into the revised concepts; report uncovered only if a distinct Quranic English concept is actually being named.

Use four classifications:

- **Confirmed inconsistency:** noncanonical name for the Quranic concept.
- **Ambiguous:** context or grammatical number is insufficient. Never silently promote it to confirmed.
- **Intentional mention:** the exact string is a proper name, brand, quotation, research comparison, explanatory gloss, URL, command, or immutable external contract literal. For example, preserve `An Ayah is often translated as “verse”.` This is not an alias exemption; owned names around an external literal remain canonical.
- **Uncovered:** Quranic English term absent from the table; report without replacement.

## Audit

1. Resolve the requested text, files, directories, or changes.
2. Search typed alternatives, eligible derived `+s` forms, and identifier forms; exclude related terms from alias matching. Use repository search such as `rg` for codebases.
3. Inspect context and classify each candidate.
4. Report confirmed inconsistencies with location, concept key, alternative type, found form, and canonical replacement. Report ambiguous, intentional, and uncovered occurrences separately.
5. Make no changes.

If no confirmed inconsistency remains, report that result. Say the target conforms only when no ambiguous, uncovered, or unsupported plural usage remains; otherwise state those limits.

## Enforce

1. Audit first.
2. Correct confirmed inconsistencies only.
3. Preserve prose meaning, grammar, number, and style.
4. In code, rename owned symbols coherently across declarations, references, schemas, tests, and relevant filenames. Do not blind-replace text or mutate intentional literals.
5. Leave ambiguous and uncovered occurrences unchanged.
6. Run relevant validation, re-audit, and report changed files plus anything unresolved.
