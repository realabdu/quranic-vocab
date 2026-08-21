---
name: quranic-vocab
description: Audit or enforce an opinionated English naming convention for Quranic concepts in prose and code using a bundled canonical vocabulary table. Use when reviewing, writing, or standardizing English Quranic terminology such as Surah, Ayah, Juz, Mushaf, Riwayah, or related code identifiers, schemas, documentation, and copy. Do not use for Arabic vocabulary or Arabic orthography.
---

# Quranic Vocabulary

Standardize English Quranic vocabulary against the canonical table. Read [references/vocabulary.md](references/vocabulary.md) completely before every audit or enforcement pass; it is the runtime source of truth. Repository usage, common practice, provider terminology, and personal preference never override the table.

## Routing

| Mode | Use when | Mutates the target |
| --- | --- | --- |
| `audit` | Bare invocation, or requests to audit, evaluate, diagnose, review, or check vocabulary | No |
| `enforce` | Explicit requests to fix, correct, rename, update, apply, or enforce the convention | Yes |

A bare invocation always defaults to `audit`. Do not edit unless the user's request clearly routes to `enforce`.

## Scope

- Evaluate English prose and code, including identifiers, types, schema fields, comments, documentation, tests, and filenames when relevant.
- Do not audit Arabic words, Arabic spelling, articles, or diacritics.
- Treat the canonical singular and the listed canonical plural as the only standard English forms for that concept.
- Treat every populated alternative in the table as noncanonical when it denotes the Quranic concept.
- If the plural column is `—`, no canonical plural exists. Do not invent one; flag a clearly pluralized use as unsupported and rewrite around the singular only in `enforce` mode.
- If a Quranic English concept is not represented in the table, report it as uncovered. Do not invent a canonical replacement.

## Number

- Map a listed noncanonical singular form to the canonical singular.
- Map a listed noncanonical plural form to the canonical plural. For example, `Riwayat` maps to `Riwayahs`, not `Riwayah`.
- When a canonical plural exists, also detect the mechanical `+s` form of each listed noncanonical singular as a noncanonical plural candidate. For example, `Verse` produces `Verses`, which maps to `Ayahs`. This detection rule does not create new canonical vocabulary.
- Do not derive a plural candidate when the canonical plural is `—`.
- When one spelling appears in both noncanonical number columns, use grammar and code context to determine number. If number is unclear, classify it as ambiguous.

## Matching and shielding

Match vocabulary case-insensitively, then render the canonical form in the target's existing style.

Apply longest-match precedence. Every complete canonical singular or plural shields shorter candidate forms wholly contained inside it, whether the canonical form is one word or multiple words. This prevents false matches such as `Sura` inside `Surah`, `Aya` inside `Ayah`, `Riwaya` inside `Riwayah`, `Word` inside `Word Root`, `Letter` inside `Disjointed Letter`, and `Recitation` inside `Murattal Recitation`. When candidate noncanonical forms overlap, classify the longest complete form first.

For code, recognize terms inside snake_case, camelCase, PascalCase, kebab-case, SCREAMING_SNAKE_CASE, and filenames. Preserve the repository's identifier convention while replacing the vocabulary:

- `verse_count` → `ayah_count`
- `VerseRange` → `AyahRange`
- `chapter-id` → `surah-id`
- `VERSE_NUMBER` → `AYAH_NUMBER`

In identifiers, remove apostrophes and modifier punctuation that occur inside a canonical lexical word; do not turn them into separators. Keep spaces and hyphens between lexical words as identifier word boundaries:

- `qiraat_id` → `qiraah_id`
- `QiraatReader` → `QiraahReader`
- `GRAMMATICAL_ANALYSIS` → `IRAB`
- `rub_el_hizb` → `rub_al_hizb`

In prose, use the table's exact spelling, including punctuation: `Qira'ah`, `I'rab`, and `Isti'adhah`.

A table match is only a violation when it denotes the Quranic concept. Use surrounding language, nearby identifiers, imports, types, schema descriptions, and domain context to decide. Ordinary uses such as a web `page`, a documentation `chapter`, or a generic `word` are not violations.

Classify uncertain occurrences as ambiguous. Never silently turn an ambiguous match into a confirmed violation.

## Intentional mentions

Classify a noncanonical form as an intentional mention—not a vocabulary violation—only when the text must identify that exact string rather than use it as the project's name for the concept. Typical cases are:

- a proper name, Surah title, organization, product, or brand such as `Al-Ahzab`, `Al-Qaari'a`, or `Tarteel AI`;
- a quotation, citation, research comparison, migration note, or metalinguistic example discussing the spelling itself;
- an immutable third-party protocol token, exact serialized key, URL segment, command, or externally defined field shown literally.

This is not an alias exemption. An owned identifier, schema field, label, or prose term remains subject to the canonical convention even when it sits near provider code. Preserve only the literal external string that must remain exact; use canonical vocabulary for owned names around it. Never mutate a proper name, quotation, URL, or external contract literal merely because it contains a table form.

## Deterministic candidate scan

For repository-sized targets, run the bundled scanner before contextual review:

```sh
python3 scripts/quranic_vocab_scan.py <path> [<path> ...]
```

Use `--format json` for machine-readable results. The scanner reads the runtime table, derives eligible `+s` candidates, shields complete canonical forms, applies longest-match precedence, and renders code-safe suggestions. Its output is a candidate list, not the final audit: inspect context and classify each result as a confirmed inconsistency, ambiguous match, or intentional mention. Find uncovered Quranic spellings separately; because they are absent from the source of truth, the scanner cannot assign them a canonical replacement.

Directory scans skip dependency, build, generated, data, public-asset, resource, and lockfile trees by default. Inspect the repository layout before relying on that default: target an excluded file directly or pass `--include-generated` when an excluded tree contains hand-authored vocabulary, schema, or contract content that is in scope.

## Audit

1. Resolve the requested text, files, directories, or current code changes.
2. Find candidate noncanonical forms from the complete table. For codebases, run the deterministic scanner, supplement it with targeted repository search for uncovered spellings, and inspect enough surrounding context to classify each candidate.
3. Report confirmed inconsistencies with the found form, canonical replacement, and location.
4. Report ambiguous matches and intentional mentions separately.
5. Report uncovered Quranic English terms without inventing replacements.
6. Make no changes.

Use this output shape:

```markdown
## Vocabulary Audit

| Location | Found | Canonical | Reason |
| --- | --- | --- | --- |

## Ambiguous Matches

| Location | Found | Why ambiguous |
| --- | --- | --- |

## Intentional Mentions

| Location | Found | Why it must remain exact |
| --- | --- | --- |

## Uncovered Quranic Terms

| Location | Found | Context |
| --- | --- | --- |

## Summary

- Confirmed inconsistencies: N
- Ambiguous matches: N
- Intentional mentions: N
- Uncovered Quranic terms: N
```

Omit an empty section. If nothing is wrong, say the target conforms to the table.

## Enforce

1. Run the audit logic first.
2. Correct every confirmed inconsistency.
3. In prose, preserve meaning, grammar, number, and surrounding style.
4. In code, perform a coherent symbol rename across declarations, references, tests, schemas, and relevant filenames. Do not use blind global replacement.
5. Leave ambiguous matches, intentional mentions, and uncovered terms unchanged and report them.
6. Run relevant formatters, tests, type checks, or schema validation available in the target.
7. Re-audit the changed target and report any remaining confirmed inconsistencies.

Return a concise summary of changed files or text, validation performed, unresolved ambiguous matches, and uncovered terms.
