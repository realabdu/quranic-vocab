from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from quranic_vocab_scan import (  # noqa: E402
    VocabularyScanner,
    iter_files,
    load_vocabulary,
    render_identifier,
)


class QuranicVocabularyScannerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.entries = load_vocabulary()
        cls.scanner = VocabularyScanner(cls.entries)

    def scan(self, text: str, filename: str = "sample.md"):
        return self.scanner.scan_text(text, Path(filename))

    def test_loads_all_sheet_rows_and_preserves_number(self) -> None:
        self.assertEqual(len(self.entries), 65)
        riwayah = next(
            entry for entry in self.entries if entry.canonical_singular == "Riwayah"
        )
        self.assertEqual(riwayah.canonical_plural, "Riwayahs")
        self.assertIn("Riwaya", riwayah.noncanonical_singular)
        self.assertIn("Riwayat", riwayah.noncanonical_plural)

    def test_every_complete_canonical_form_shields_shorter_candidates(self) -> None:
        text = (
            "Surah Ayah Riwayah Word Root Disjointed Letter Murattal Recitation "
            "surah_name ayahId RIWAYAH_ID qiraah_id word_root"
        )
        self.assertEqual(self.scan(text), [])

    def test_singular_explicit_plural_and_derived_plus_s_mapping(self) -> None:
        candidates = self.scan("Verse Verses Riwaya Riwayat")
        actual = {candidate.found: candidate.canonical for candidate in candidates}
        self.assertEqual(actual["Verse"], ("Ayah",))
        self.assertEqual(actual["Verses"], ("Ayahs",))
        self.assertEqual(actual["Riwaya"], ("Riwayah",))
        self.assertEqual(actual["Riwayat"], ("Riwayahs",))

    def test_same_surface_in_both_number_columns_keeps_both_options(self) -> None:
        candidates = self.scan("Qira'at")
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].canonical, ("Qira'ah", "Qira'ahs"))

    def test_does_not_derive_when_no_canonical_plural_exists(self) -> None:
        self.assertEqual(self.scan("Qurans Basmalahs"), [])

    def test_longest_candidate_wins(self) -> None:
        candidates = self.scan("The Verse Numbering System is documented.")
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].found, "Verse Numbering System")
        self.assertEqual(candidates[0].canonical, ("Ayah Numbering System",))

    def test_code_styles_and_punctuation_safe_rendering(self) -> None:
        text = "\n".join(
            [
                "verse_count = 1",
                "class VerseRange: pass",
                "chapter-id: 1",
                "VERSE_NUMBER = 1",
                "qiraat_id = 1",
                "QiraatReader = object",
                "GRAMMATICAL_ANALYSIS = True",
                "rub_el_hizb = 1",
            ]
        )
        candidates = self.scan(text, "sample.py")
        actual = {(candidate.found, candidate.suggested) for candidate in candidates}
        self.assertIn(("verse", ("ayah",)), actual)
        self.assertIn(("Verse", ("Ayah",)), actual)
        self.assertIn(("chapter", ("surah",)), actual)
        self.assertIn(("VERSE", ("AYAH",)), actual)
        self.assertIn(("qiraat", ("qiraah", "qiraahs")), actual)
        self.assertIn(("Qiraat", ("Qiraah", "Qiraahs")), actual)
        self.assertIn(("GRAMMATICAL_ANALYSIS", ("IRAB",)), actual)
        self.assertIn(("rub_el_hizb", ("rub_al_hizb",)), actual)

    def test_identifier_renderer_removes_internal_punctuation(self) -> None:
        self.assertEqual(render_identifier("Qira'ah", "snake"), "qiraah")
        self.assertEqual(render_identifier("I'rab", "pascal"), "Irab")
        self.assertEqual(render_identifier("Isti'adhah", "camel"), "istiadhah")
        self.assertEqual(render_identifier("Rub al-Hizb", "camel"), "rubAlHizb")

    def test_context_sensitive_names_remain_candidates_for_skill_review(self) -> None:
        candidates = self.scan("Al-Ahzab, Al-Qaari'a, and Tarteel AI")
        self.assertEqual(
            {candidate.found for candidate in candidates}, {"Ahzab", "Qaari", "Tarteel"}
        )

    def test_directory_scan_skips_generated_trees_but_direct_target_does_not(
        self
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "src" / "sample.py"
            generated = root / "data" / "sample.json"
            source.parent.mkdir()
            generated.parent.mkdir()
            source.write_text("verse = 1", encoding="utf-8")
            generated.write_text('{"verse": 1}', encoding="utf-8")

            self.assertEqual(list(iter_files([root])), [source.resolve()])
            self.assertEqual(
                set(iter_files([root], include_generated=True)),
                {source.resolve(), generated.resolve()},
            )
            self.assertEqual(list(iter_files([generated])), [generated.resolve()])


if __name__ == "__main__":
    unittest.main()
