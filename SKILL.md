---
name: quranic-vocab
description: Audit or enforce an opinionated English naming convention for Quranic concepts in prose and code using a bundled canonical vocabulary table. Use when reviewing, writing, or standardizing English Quranic terminology such as Surah, Ayah, Juz, Mushaf, Riwayah, or related code identifiers, schemas, documentation, and copy. Do not use for Arabic vocabulary or Arabic orthography.
---

# Quranic Vocabulary

Standardize English Quranic vocabulary against the canonical table. Read [references/vocabulary.md](references/vocabulary.md) completely before every audit or enforcement pass; it is the runtime source of truth.

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

## Matching

Match vocabulary case-insensitively, then render the canonical form in the target's existing style.

Apply longest-match precedence. A canonical multiword term or plural shields shorter table forms wholly contained inside it. For example, do not flag `Word` inside canonical `Word Root`, `Letter` inside canonical `Disjointed Letter`, or `Recitation` inside canonical `Murattal Recitation`. When candidate noncanonical forms overlap, classify the longest complete form first.

For code, recognize terms inside snake_case, camelCase, PascalCase, kebab-case, SCREAMING_SNAKE_CASE, and filenames. Preserve the repository's identifier convention while replacing the vocabulary:

- `verse_count` → `ayah_count`
- `VerseRange` → `AyahRange`
- `chapter-id` → `surah-id`
- `VERSE_NUMBER` → `AYAH_NUMBER`

A table match is only a violation when it denotes the Quranic concept. Use surrounding language, nearby identifiers, imports, types, schema descriptions, and domain context to decide. Ordinary uses such as a web `page`, a documentation `chapter`, or a generic `word` are not violations.

Classify uncertain occurrences as ambiguous. Never silently turn an ambiguous match into a confirmed violation.

## Audit

1. Resolve the requested text, files, directories, or current code changes.
2. Find candidate noncanonical forms from the complete table. For codebases, use targeted repository search and inspect enough surrounding context to classify each candidate.
3. Report confirmed inconsistencies with the found form, canonical replacement, and location.
4. Report ambiguous matches separately.
5. Make no changes.

Use this output shape:

```markdown
## Vocabulary Audit

| Location | Found | Canonical | Reason |
| --- | --- | --- | --- |

## Ambiguous Matches

| Location | Found | Why ambiguous |
| --- | --- | --- |

## Summary

- Confirmed inconsistencies: N
- Ambiguous matches: N
- Uncovered Quranic terms: N
```

Omit an empty section. If nothing is wrong, say the target conforms to the table.

## Enforce

1. Run the audit logic first.
2. Correct every confirmed inconsistency.
3. In prose, preserve meaning, grammar, number, and surrounding style.
4. In code, perform a coherent symbol rename across declarations, references, tests, schemas, and relevant filenames. Do not use blind global replacement.
5. Leave ambiguous matches unchanged and report them.
6. Run relevant formatters, tests, type checks, or schema validation available in the target.
7. Re-audit the changed target and report any remaining confirmed inconsistencies.

Return a concise summary of changed files or text, validation performed, unresolved ambiguous matches, and uncovered terms.
