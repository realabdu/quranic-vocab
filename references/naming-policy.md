# Naming policy

Retain specialized Quranic terms when English loses a meaningful distinction, and use ordinary English where it conveys a general concept accurately: `Surah`, `Ayah`, `Qira'ah`, and `Riwayah` alongside `Translation`, `Word Root`, `Word`, `Page`, and `Letter`.

Define the concept first. Developer familiarity and established usage can inform the name, but neither replaces a definition that distinguishes the concept from nearby meanings. [vocabulary.md](vocabulary.md) holds all approved names and the three revised definitions. This revision changes only those three names; other entries remain binding until explicitly revised.

## Transliteration

The table governs spelling. This practical convention is not a reversible scholarly system:

- Retain `h` in standalone `-ah` endings such as `Surah`, `Ayah`, and `Riwayah`. Do not extend this mechanically to compounds or unlisted forms.
- Follow listed plain-vowel mappings: `Tajweed` → `Tajwid`, `Tarteel` → `Tartil`, and `Nuzool` → `Nuzul`. Do not simplify doubled vowels or macrons elsewhere by analogy.
- Keep approved prose punctuation: `Qira'ah`, `Isti'adhah`, and `I'rab`. Do not add punctuation to `Quran`, `Juz`, or `Ruku` for uniformity; the skill entrypoint defines code rendering.
- Preserve compound spacing, hyphens, articles, and capitalization, as in `Rub al-Hizb` and `Al-Mathani`. Do not generate alternate compounds or add articles automatically.
- Use explicit `+s` plurals, including shortened multiword forms. Arabic plurals remain typed alternatives, and missing plurals stay undefined.

## Identity

Keep concept keys stable through label changes. Prose uses the approved English label; code follows its existing identifier style. Localized interfaces may use other labels for the same concept, and Arabic labels are outside the audit's scope.

## Contributions

Propose a definition, singular and plural (or no plural), rationale, sources, and a prose/code example. Type alternatives by spelling, Arabic-derived form, legacy name, explanatory gloss, or related concept, preserving number. Explain spelling exceptions and compatibility impacts.

Check existing entries before adding a concept, and review uncertain relationships before treating them as aliases. Naming rules guide proposals. Only explicit maintainer adoption changes the vocabulary and its provenance; ordinary audits report unlisted concepts as uncovered.

Old labels may remain as legacy alternatives for migration. A vocabulary revision does not authorize edits to external API contracts or consumer repositories, nor imply community-wide ratification of this opinionated convention.
