# Canonical English Quranic Vocabulary

Derived from the [Verified Quranic vocabulary Sheet](https://docs.google.com/spreadsheets/d/1PLLtcgwbwtkOfpAZOotUQiZw-ARtZiAQuAkx2Z4D0XA/edit?gid=0#gid=0), normalized on 2026-08-21, with local revisions adopted on 2026-09-07 following [community feedback](https://community.itqan.dev/d/757). This reference retains all 65 concepts; it no longer reproduces the Sheet exactly.

## Identity, provenance, and alternative types

- Concept keys were introduced in this revision, derived from the revised singular names using lowercase snake_case and the identifier rules in the skill. Keys remain stable if display names change later. They are reference metadata, not mandatory names for consumer database keys.
- Canonical singulars and plurals come from the normalized Sheet snapshot except `Kalimah / Kalimahs` → `Word / Words`, `Harf / Harfs` → `Letter / Letters`, and `Safhah / Safhahs` → `Page / Pages`.
- All pre-revision alternatives retain their text and singular/plural column, except `Word`, `Letter`, and `Page`, which are now canonical. Former canonical forms were added as legacy alternatives. Original plural alternatives for these three concepts are also classified as legacy.
- Alternative types are local editorial classifications of the snapshot, not claims about separate fields in the Sheet. The snapshot had combined spelling and literal-translation data. Definitions, concept keys, and related terms below are local additions.
- `spelling`: another Latin-script spelling of the name. `transliteration`: another Arabic-derived name or Arabic plural rendered in Latin script. Neither type establishes equivalence without concept and number context.
- `legacy`: a superseded name or variant of a superseded name. `gloss`: an English translation, explanation, or descriptive label; eligible for replacement only when used as a name for this exact concept, not merely as explanatory prose.
- `Related terms` records distinctions, not aliases. These strings never authorize a replacement or create new canonical entries. No derived plural aliases are generated from this column.
- Singular/plural columns govern replacement number. A label occurring in both requires context. `—` in the canonical plural column means no plural is defined; do not invent one. Existing canonical plurals are explicit values, including shortened multiword forms.
- Arabic labels and orthographic rules remain outside this English enforcement reference. A localized UI may use a different label for the same concept.

## Definitions for revised concepts

- **Word (`word`):** an orthographic word in the referenced Quran text dataset, distinct from a morphological segment. Use the dataset's documented word boundaries; this convention does not prescribe segmentation or word counts. A segment must not be renamed to Word merely because it was called Kalimah.
- **Page (`page`):** a page within a specified Mushaf edition or layout. Interpret page numbers within that edition/layout, not as universal Quran locations. Page belongs to layout, not beneath Letter in a text hierarchy. A screen, web page, or pagination cursor is not this concept.
- **Letter (`letter`):** an alphabetic letter of the Quran text, distinct from a Unicode character or glyph. This entry does not cover other senses of harf. Do not infer an alphabetic-letter meaning from a variable name or a Quran-related file alone; inspect its documentation and use. This convention does not prescribe a letter-counting algorithm.

## Approved vocabulary

| Concept key | Canonical singular | Canonical +s plural | Singular alternatives (typed) | Plural alternatives (typed) | Related terms (not aliases) |
| --- | --- | --- | --- | --- | --- |
| quran | Quran | — | spelling: Qur'an; spelling: Qur’an; spelling: Koran | — | — |
| kitab | Kitab | Kitabs | spelling: Kitaab; spelling: Ketab; gloss: Book | transliteration: Kutub | — |
| mushaf | Mushaf | Mushafs | spelling: Mus'haf; spelling: Muṣḥaf; gloss: Quran Codex | transliteration: Masahif | — |
| mushaf_edition | Mushaf Edition | Mushaf Editions | gloss: Quran Edition; gloss: Mushaf Type; gloss: Edition of the Mushaf | transliteration: Taba'at al-Mushaf | — |
| surah | Surah | Surahs | spelling: Sura; gloss: Chapter | transliteration: Suwar | — |
| ayah | Ayah | Ayahs | spelling: Aya; gloss: Verse | transliteration: Ayat | — |
| fasilah | Fasilah | Fasilahs | spelling: Fasila; gloss: Verse Ending | transliteration: Fawasil | — |
| word | Word | Words | legacy: Kalimah; legacy: Kalima | legacy: Kalimahs; legacy: Kalimat | Morphological Segment |
| letter | Letter | Letters | legacy: Harf | legacy: Harfs; legacy: Huruf | Unicode Character; Glyph |
| basmalah | Basmalah | — | spelling: Basmala; gloss: Bismillah Formula | — | — |
| disjointed_letter | Disjointed Letter | Disjointed Letters | gloss: Separated Letter | transliteration: Huruf Muqatta'ah | — |
| word_root | Word Root | Word Roots | — | — | — |
| juz | Juz | Juzs | spelling: Juzu; gloss: Part | transliteration: Ajza' | — |
| hizb | Hizb | Hizbs | spelling: Hezb; gloss: Group | transliteration: Ahzab | — |
| rub_al_hizb | Rub al-Hizb | Rub al-Hizbs | spelling: Rub' al-Hizb; spelling: Rub el Hizb; gloss: Quarter of a Hizb | transliteration: Arba' al-Ahzab | — |
| thumn | Thumn | Thumns | spelling: Thumun; gloss: Eighth | transliteration: Athman | — |
| manzil | Manzil | Manzils | spelling: Manzel; gloss: Station | transliteration: Manazil | — |
| ruku | Ruku | Rukus | spelling: Ruku'; spelling: Rukūʿ; gloss: Section | transliteration: Ruku'at | — |
| page | Page | Pages | legacy: Safhah; legacy: Safha | legacy: Safhahs; legacy: Safahat | Layout |
| al_sabe_al_tiwal | Al-Sabe al-Tiwal | — | gloss: Seven Long Surahs | — | — |
| al_miun | Al-Miun | — | gloss: Hundred-Verse Surahs | — | — |
| al_mathani | Al-Mathani | — | spelling: Al-Mathaani; spelling: Mathani; gloss: Oft-Repeated Surahs | — | — |
| mufassal | Mufassal | — | spelling: Al-Mufassal; gloss: Shorter Surahs | — | — |
| nuzul | Nuzul | — | spelling: Nuzool; gloss: Descent | — | — |
| makki | Makki | Makkis | spelling: Makkan; spelling: Makkiyy; spelling: Meccan | transliteration: Makkiyyat | — |
| madani | Madani | Madanis | spelling: Madinan; spelling: Madaniyy; spelling: Medinan | transliteration: Madaniyyat | — |
| asbab_al_nuzul | Asbab al-Nuzul | — | spelling: Asbab al-Nozool; spelling: Asbab un-Nuzul; gloss: Occasions of Revelation | — | — |
| revelation_order | Revelation Order | Revelation Orders | gloss: Chronological Order of Revelation; gloss: Order of Revelation | transliteration: Tartib al-Nuzul | — |
| uthmani_rasm | Uthmani Rasm | Uthmani Rasms | spelling: Rasm Uthmani; spelling: Uthmanic Rasm; gloss: Uthmanic Orthography | transliteration: Rusum Uthmaniyyah | — |
| waqf_mark | Waqf Mark | Waqf Marks | gloss: Waqf Sign; gloss: Pause Mark; gloss: Stop Mark | transliteration: Alamat al-Waqf | — |
| waqf_lazim | Waqf Lazim | Waqf Lazims | spelling: Waqf Laazim; gloss: Obligatory Stop; gloss: Mandatory Pause | transliteration: Wuquf Lazimah | — |
| waqf_mamnu | Waqf Mamnu | — | spelling: Waqf Mamnoo; gloss: Prohibited Stop; gloss: Prohibited Pause | — | — |
| waqf_jaiz | Waqf Jaiz | — | gloss: Permissible Pause | — | — |
| wasl | Wasl | — | gloss: Wasl Preferred; gloss: Continuation | — | — |
| waqf | Waqf | — | gloss: Waqf Preferred; gloss: Stopping | — | — |
| waqf_al_muanaqah | Waqf al-Muanaqah | — | transliteration: Waqf al-Muraqabah; gloss: Embrace Pause; gloss: Interchangeable Pause | — | — |
| division_mark | Division Mark | Division Marks | gloss: Section Mark; gloss: Division Sign; gloss: Juz, Hizb, or Quarter Mark | transliteration: Alamat al-Ajza' wa-l-Ahzab wa-l-Arba' | — |
| sajdah_mark | Sajdah Mark | Sajdah Marks | spelling: Sajda Mark; gloss: Sajdah Sign; gloss: Prostration Mark | transliteration: Alamat al-Sajdah | — |
| tilawah | Tilawah | Tilawahs | spelling: Tilawa; gloss: Recitation | transliteration: Tilawat | — |
| tartil | Tartil | — | spelling: Tarteel; gloss: Measured Recitation | — | — |
| tahqiq | Tahqiq | — | spelling: Tahqeeq; gloss: Slow, Precise Recitation | — | — |
| tadwir | Tadwir | — | spelling: Tadweer; gloss: Moderate-Paced Recitation | — | — |
| hadr | Hadr | — | spelling: Hadar; gloss: Rapid Recitation | — | — |
| tajwid | Tajwid | — | spelling: Tajweed; gloss: Rules of Recitation | — | — |
| qiraah | Qira'ah | Qira'ahs | spelling: Qiraat; spelling: Qira'at; spelling: Qiraa; gloss: Reading | transliteration: Qira'at | — |
| riwayah | Riwayah | Riwayahs | spelling: Riwaya; gloss: Transmission | transliteration: Riwayat | — |
| tariq | Tariq | — | spelling: Tareeq; gloss: Transmission Path | — | — |
| rawi | Rawi | Rawis | gloss: Narrator; gloss: Transmitter | transliteration: Ruwat | — |
| qari | Qari | Qaris | spelling: Qaari; gloss: Reciter | transliteration: Qurra' | — |
| muqri | Muqri | Muqris | spelling: Muqree; gloss: Teacher of Recitation | transliteration: Muqri'un | — |
| saktah | Saktah | Saktahs | spelling: Sakta; gloss: Short Pause | transliteration: Saktat | — |
| sujud_al_tilawah | Sujud al-Tilawah | — | transliteration: Sajdah al-Tilawah; transliteration: Sajdat al-Tilawah; gloss: Prostration of Recitation | — | — |
| khatmah | Khatmah | Khatmahs | spelling: Khatma; gloss: Complete Recitation | transliteration: Khatmat | — |
| istiadhah | Isti'adhah | Isti'adhahs | spelling: Istiʿādhah; spelling: Isti'adha; transliteration: Ta'awwudh; gloss: Seeking Refuge | transliteration: Isti'adhat | — |
| recitation_performance_style | Recitation Performance Style | Recitation Performance Styles | gloss: Recitation Style; gloss: Performance Profile; gloss: Style of Recitation Performance | transliteration: Anmat Ada' al-Tilawah | — |
| murattal_recitation | Murattal Recitation | Murattal Recitations | transliteration: Murattal; gloss: Murattal Mushaf | transliteration: Tilawat Murattalah | — |
| mujawwad_recitation | Mujawwad Recitation | Mujawwad Recitations | transliteration: Mujawwad; gloss: Mujawwad Mushaf | transliteration: Tilawat Mujawwadah | — |
| muallim_recitation | Muallim Recitation | Muallim Recitations | transliteration: Muallim; transliteration: Mu'allim; gloss: Muallim Mushaf; gloss: Educational Recitation | transliteration: Tilawat Ta'limiyyah | — |
| instructional_ayah_repetition | Instructional Ayah Repetition | Instructional Ayah Repetitions | gloss: Ayah Repetition; gloss: Educational Repetition; gloss: Repetition of Ayahs for Teaching | transliteration: Tikrarat al-Ayat li-l-Ta'lim | — |
| spoken_translation_of_the_qurans_meanings | Spoken Translation of the Quran's Meanings | Spoken Translations | gloss: Spoken Translation; gloss: Audio Translation | transliteration: Tarjamat Mantuqah li-Ma'ani al-Quran | — |
| ayah_numbering_system | Ayah Numbering System | Ayah Numbering Systems | gloss: Ayah Counting System; gloss: Verse Numbering System; gloss: System of Counting Ayahs | transliteration: Nuzum Add al-Ay | — |
| translation | Translation | Translations | — | transliteration: Tarjamat | — |
| tafsir | Tafsir | Tafsirs | spelling: Tafseer; gloss: Commentary; gloss: Exegesis | transliteration: Tafasir | — |
| transliteration | Transliteration | — | gloss: Romanization; gloss: Letter-by-Letter Transcription | — | — |
| irab | I'rab | — | gloss: Grammatical Analysis | — | — |
