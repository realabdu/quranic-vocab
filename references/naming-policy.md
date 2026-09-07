# Naming policy

Use this policy when explaining naming choices or proposing vocabulary revisions. Audit and enforce use the approved vocabulary, not fresh naming decisions made from these guidelines.

## Choosing a name

Retain specialized Quranic terminology when an English equivalent loses a meaningful distinction. Prefer ordinary English for general concepts whose meaning it conveys accurately. This allows `Surah`, `Ayah`, `Qira'ah`, and `Riwayah` alongside `Translation`, `Word Root`, `Word`, `Page`, and `Letter`.

Define the concept before choosing its label. Explain what the term includes and what nearby concepts it excludes. Developer familiarity and established usage are useful evidence, but neither substitutes for checking meaning. The three revised definitions and all approved names live only in [vocabulary.md](vocabulary.md).

These criteria guide additions and reviews; they do not imply that every inherited entry has been reconsidered. This revision changes only the three approved names. Other canonical names remain binding until explicitly revised.

## Practical transliteration and identifiers

This is a practical English naming convention, not a reversible scholarly transliteration system. The approved spellings are authoritative; the following describes their conventions and exceptions:

- Standalone names with the familiar `-ah` ending retain `h`, as in `Surah`, `Ayah`, and `Riwayah`. Do not apply this mechanically within compounds or to forms absent from the table.
- Established plain-vowel spellings are preferred over doubled vowels or macrons where the table lists that mapping: `Tajweed` → `Tajwid`, `Tarteel` → `Tartil`, and `Nuzool` → `Nuzul`. This is not a rule to shorten every doubled vowel in arbitrary text.
- Prose keeps the punctuation in approved names such as `Qira'ah`, `Isti'adhah`, and `I'rab`. Existing names such as `Quran`, `Juz`, and `Ruku` omit punctuation; do not add it to force uniformity. Identifier rendering is defined in the skill entrypoint.
- Compounds retain their approved spaces, hyphens, article forms, and capitalization, such as `Rub al-Hizb` and `Al-Mathani`. Do not add articles or generate alternative compound spellings automatically.
- Canonical plurals are explicit table values following the adopted English `+s` convention, including established shortened multiword plurals. Arabic plurals remain typed alternatives. Missing plurals stay undefined.

## Identity and contributions

Keep a concept's reference key stable across label changes. Prose uses the approved English label; code renders that label in its existing identifier style. A localized interface can display another label for the same concept without changing its identity. Arabic labels are not audited by this skill.

For an addition or revision, provide the concept definition, proposed singular and plural (or no plural), selection rationale, supporting sources, and a prose/code example. Separate spelling variants, Arabic-derived alternatives, legacy names, explanatory glosses, and related concepts, retaining grammatical number. Explain any spelling exception and any compatibility impact on existing consumers.

Compare the proposal with existing entries before adding a concept. A maintainer's explicit adoption updates the authoritative vocabulary and its provenance; naming guidance alone does not grant canonical status. During ordinary audits, absent concepts remain uncovered. Review uncertain semantic relationships before classifying them as aliases.

Renaming the reference's canonical label does not authorize changes to external API contracts or consumer repositories. Old names can remain as typed legacy alternatives for deliberate migration. This repository remains an opinionated convention, not a claim of community-wide ratification.
