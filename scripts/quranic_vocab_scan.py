#!/usr/bin/env python3
"""Find noncanonical English Quranic vocabulary candidates.

This scanner is intentionally context-free. It discovers candidates and renders
possible canonical replacements; the quranic-vocab skill classifies each result.
"""

from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TABLE = SKILL_ROOT / "references" / "vocabulary.md"

SKIP_DIRECTORIES = {
    ".git",
    ".hg",
    ".idea",
    ".mypy_cache",
    ".next",
    ".nuxt",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".yarn",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

GENERATED_DIRECTORIES = {
    "data",
    "generated",
    "out",
    "public",
    "resources",
    "work",
}

SKIP_FILENAMES = {
    "bun.lockb",
    "cargo.lock",
    "composer.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
}

TEXT_SUFFIXES = {
    ".c",
    ".cc",
    ".conf",
    ".cpp",
    ".cs",
    ".css",
    ".csv",
    ".dart",
    ".env",
    ".go",
    ".graphql",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".kt",
    ".kts",
    ".md",
    ".mdx",
    ".php",
    ".proto",
    ".py",
    ".rb",
    ".rs",
    ".rst",
    ".scss",
    ".sh",
    ".sql",
    ".svelte",
    ".swift",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".vue",
    ".xml",
    ".yaml",
    ".yml",
    ".zsh",
}

PROSE_SUFFIXES = {".md", ".mdx", ".rst", ".txt"}
TEXT_FILENAMES = {
    "dockerfile",
    "gemfile",
    "license",
    "makefile",
    "procfile",
    "readme",
}
INTERNAL_MARKS = "'’‘ʼʿʾʻʼ"
DASH = "—"


@dataclass(frozen=True)
class VocabularyEntry:
    canonical_singular: str
    canonical_plural: str | None
    noncanonical_singular: tuple[str, ...]
    noncanonical_plural: tuple[str, ...]


@dataclass(frozen=True)
class CandidateSpec:
    form: str
    canonical: str
    source: str


@dataclass(frozen=True)
class Span:
    start: int
    end: int


@dataclass(frozen=True)
class Candidate:
    path: str
    line: int
    column: int
    found: str
    canonical: tuple[str, ...]
    suggested: tuple[str, ...]
    sources: tuple[str, ...]
    context: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _split_forms(cell: str) -> tuple[str, ...]:
    if not cell or cell in {DASH, "-"}:
        return ()
    return tuple(part.strip() for part in cell.split(";") if part.strip())


def load_vocabulary(path: Path = DEFAULT_TABLE) -> list[VocabularyEntry]:
    """Load the four-column runtime Markdown table."""

    rows: list[VocabularyEntry] = []
    in_table = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("| Canonical singular |"):
            in_table = True
            continue
        if not in_table:
            continue
        if raw_line.startswith("| ---"):
            continue
        if not raw_line.startswith("|"):
            if rows:
                break
            continue

        cells = [cell.strip() for cell in raw_line.strip().strip("|").split("|")]
        if len(cells) != 4:
            raise ValueError(
                f"expected four vocabulary columns, got {len(cells)}: {raw_line}"
            )

        singular, plural, noncanonical_singular, noncanonical_plural = cells
        rows.append(
            VocabularyEntry(
                canonical_singular=singular,
                canonical_plural=None if plural in {DASH, "-", ""} else plural,
                noncanonical_singular=_split_forms(noncanonical_singular),
                noncanonical_plural=_split_forms(noncanonical_plural),
            )
        )

    if not rows:
        raise ValueError(f"no vocabulary rows found in {path}")
    return rows


def _identifier_words(term: str) -> tuple[str, ...]:
    cleaned = term.translate(str.maketrans("", "", INTERNAL_MARKS))
    return tuple(re.findall(r"[^\W_]+", cleaned, flags=re.UNICODE))


def _identifier_variants(term: str) -> set[str]:
    words = _identifier_words(term)
    if not words:
        return set()

    lowered = [word.lower() for word in words]
    titled = [word[:1].upper() + word[1:].lower() for word in words]
    return {
        "_".join(lowered),
        "-".join(lowered),
        lowered[0] + "".join(titled[1:]),
        "".join(titled),
        "_".join(word.upper() for word in words),
    }


def _is_left_boundary(text: str, start: int) -> bool:
    if start == 0:
        return True
    previous = text[start - 1]
    current = text[start]
    return not previous.isalnum() or (previous.islower() and current.isupper())


def _is_right_boundary(text: str, end: int) -> bool:
    if end == len(text):
        return True
    previous = text[end - 1]
    following = text[end]
    return not following.isalnum() or (previous.islower() and following.isupper())


def _compile_literal_trie(literals: Iterable[str]) -> re.Pattern[str]:
    terminal = ""
    root: dict[str, dict] = {}
    for literal in literals:
        node = root
        for character in literal:
            node = node.setdefault(character, {})
        node[terminal] = {}

    def emit(node: dict[str, dict]) -> str:
        branches = [
            re.escape(character) + emit(child)
            for character, child in sorted(node.items())
            if character != terminal
        ]
        if terminal in node:
            branches.append("")
        if len(branches) == 1:
            return branches[0]
        return "(?:" + "|".join(branches) + ")"

    return re.compile(emit(root))


class _SurfaceMatcher:
    """Match every source form with one prefix-factored regular expression."""

    def __init__(self, forms: Iterable[tuple[str, object]]):
        self.values: dict[str, set[object]] = {}
        for form, payload in forms:
            surfaces = {form, *_identifier_variants(form)}
            for surface in surfaces:
                self.values.setdefault(surface.lower(), set()).add(payload)
        self.pattern = _compile_literal_trie(self.values)

    def find(self, text: str) -> dict[Span, set[object]]:
        found: dict[Span, set[object]] = {}
        searchable = text.lower()
        position = 0
        while position < len(searchable):
            match = self.pattern.search(searchable, position)
            if match is None:
                break
            span = Span(match.start(), match.end())
            if _is_left_boundary(text, span.start) and _is_right_boundary(
                text, span.end
            ):
                found.setdefault(span, set()).update(self.values[match.group()])
                position = span.end
            else:
                position = span.start + 1
        return found


def _plus_s(form: str) -> str | None:
    stripped = form.rstrip()
    if not stripped or stripped.casefold().endswith("s"):
        return None
    return f"{stripped}s"


def _build_candidate_specs(entries: Sequence[VocabularyEntry]) -> list[CandidateSpec]:
    specs: set[CandidateSpec] = set()
    canonical_forms = {
        form.casefold()
        for entry in entries
        for form in (entry.canonical_singular, entry.canonical_plural)
        if form
    }

    for entry in entries:
        for form in entry.noncanonical_singular:
            if form.casefold() not in canonical_forms:
                specs.add(
                    CandidateSpec(form, entry.canonical_singular, "sheet-singular")
                )

            if entry.canonical_plural:
                derived = _plus_s(form)
                if derived and derived.casefold() not in canonical_forms:
                    specs.add(
                        CandidateSpec(derived, entry.canonical_plural, "derived-plus-s")
                    )

        if entry.canonical_plural:
            for form in entry.noncanonical_plural:
                if form.casefold() not in canonical_forms:
                    specs.add(
                        CandidateSpec(form, entry.canonical_plural, "sheet-plural")
                    )

    return sorted(
        specs, key=lambda spec: (-len(spec.form), spec.form.casefold(), spec.canonical)
    )


def _is_shielded(candidate: Span, canonical_spans: Iterable[Span]) -> bool:
    return any(
        canonical.start <= candidate.start and canonical.end >= candidate.end
        for canonical in canonical_spans
    )


def _line_and_column(newlines: Sequence[int], offset: int) -> tuple[int, int]:
    line_index = bisect.bisect_right(newlines, offset)
    previous_newline = newlines[line_index - 1] if line_index else -1
    return line_index + 1, offset - previous_newline


def _code_style(found: str) -> str:
    letters = "".join(character for character in found if character.isalpha())
    if "_" in found:
        return "screaming" if letters and letters.isupper() else "snake"
    if "-" in found:
        return "kebab"
    if letters and letters.isupper():
        return "screaming-compact"
    first_alpha = next((character for character in found if character.isalpha()), "")
    if first_alpha.isupper():
        return "pascal"
    if any(character.isupper() for character in found[1:]):
        return "camel"
    return "lower"


def render_identifier(canonical: str, style: str) -> str:
    """Render canonical vocabulary as a punctuation-safe code identifier."""

    words = _identifier_words(canonical)
    lowered = [word.lower() for word in words]
    titled = [word[:1].upper() + word[1:].lower() for word in words]

    if style == "snake":
        return "_".join(lowered)
    if style == "kebab":
        return "-".join(lowered)
    if style == "camel":
        return lowered[0] + "".join(titled[1:])
    if style == "pascal":
        return "".join(titled)
    if style == "screaming":
        return "_".join(word.upper() for word in words)
    if style == "screaming-compact":
        return "".join(word.upper() for word in words)
    return "".join(lowered)


class VocabularyScanner:
    def __init__(self, entries: Sequence[VocabularyEntry]):
        self.entries = tuple(entries)
        self.specs = tuple(_build_candidate_specs(entries))
        canonical_forms = (
            (form, form)
            for entry in entries
            for form in (entry.canonical_singular, entry.canonical_plural)
            if form
        )
        self.canonical_matcher = _SurfaceMatcher(canonical_forms)
        self.candidate_matcher = _SurfaceMatcher(
            (spec.form, spec) for spec in self.specs
        )

    def scan_text(
        self, text: str, path: Path, *, prose: bool | None = None
    ) -> list[Candidate]:
        if prose is None:
            prose = path.suffix.lower() in PROSE_SUFFIXES

        canonical_spans = set(self.canonical_matcher.find(text))
        grouped = {
            span: list(specs)
            for span, specs in self.candidate_matcher.find(text).items()
            if not _is_shielded(span, canonical_spans)
        }

        # The prefix-factored matcher emits the longest complete surface and
        # advances beyond it, so its candidate spans are already non-overlapping.
        accepted = sorted(grouped, key=lambda item: item.start)

        newlines = [index for index, character in enumerate(text) if character == "\n"]
        lines = text.splitlines()
        candidates: list[Candidate] = []
        for span in sorted(accepted, key=lambda item: item.start):
            specs = grouped[span]
            found = text[span.start : span.end]
            canonical = tuple(sorted({spec.canonical for spec in specs}))
            if prose:
                suggested = canonical
            else:
                style = _code_style(found)
                suggested = tuple(
                    render_identifier(value, style) for value in canonical
                )
            line, column = _line_and_column(newlines, span.start)
            context = lines[line - 1].strip() if line <= len(lines) else ""
            candidates.append(
                Candidate(
                    path=str(path),
                    line=line,
                    column=column,
                    found=found,
                    canonical=canonical,
                    suggested=suggested,
                    sources=tuple(sorted({spec.source for spec in specs})),
                    context=context,
                )
            )
        return candidates


def _is_text_file(path: Path) -> bool:
    return (
        path.suffix.lower() in TEXT_SUFFIXES or path.name.casefold() in TEXT_FILENAMES
    )


def iter_files(
    paths: Sequence[Path], *, include_generated: bool = False
) -> Iterator[Path]:
    seen: set[Path] = set()
    for requested in paths:
        path = requested.resolve()
        if path.is_file():
            if path not in seen:
                seen.add(path)
                yield path
            continue
        if not path.is_dir():
            print(f"warning: target does not exist: {requested}", file=sys.stderr)
            continue

        for root, directories, filenames in os.walk(path):
            excluded_directories = SKIP_DIRECTORIES
            if not include_generated:
                excluded_directories = SKIP_DIRECTORIES | GENERATED_DIRECTORIES
            directories[:] = sorted(
                directory
                for directory in directories
                if directory not in excluded_directories
                and not directory.startswith(".")
            )
            for filename in sorted(filenames):
                candidate = Path(root) / filename
                if (
                    filename.casefold() not in SKIP_FILENAMES
                    and _is_text_file(candidate)
                    and candidate not in seen
                ):
                    seen.add(candidate)
                    yield candidate


def scan_paths(
    paths: Sequence[Path],
    *,
    table: Path = DEFAULT_TABLE,
    max_bytes: int = 2_000_000,
    include_generated: bool = False,
) -> tuple[list[Candidate], list[str]]:
    scanner = VocabularyScanner(load_vocabulary(table))
    candidates: list[Candidate] = []
    skipped: list[str] = []

    for path in iter_files(paths, include_generated=include_generated):
        try:
            if path.stat().st_size > max_bytes:
                skipped.append(f"{path}: larger than {max_bytes} bytes")
                continue
            payload = path.read_bytes()
            if b"\x00" in payload:
                skipped.append(f"{path}: binary data")
                continue
            text = payload.decode("utf-8")
        except (OSError, UnicodeDecodeError) as error:
            skipped.append(f"{path}: {error}")
            continue
        candidates.extend(scanner.scan_text(text, path))

    return candidates, skipped


def _print_text(candidates: Sequence[Candidate], skipped: Sequence[str]) -> None:
    for candidate in candidates:
        canonical = " or ".join(candidate.canonical)
        suggested = " or ".join(candidate.suggested)
        source = ", ".join(candidate.sources)
        print(
            f"{candidate.path}:{candidate.line}:{candidate.column}: "
            f"{candidate.found!r} -> {canonical!r} "
            f"(suggested: {suggested!r}; {source})"
        )
    for message in skipped:
        print(f"skipped: {message}", file=sys.stderr)
    print(f"Candidates: {len(candidates)}")


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="+", type=Path, help="files or directories to scan"
    )
    parser.add_argument(
        "--table",
        type=Path,
        default=DEFAULT_TABLE,
        help=f"runtime vocabulary table (default: {DEFAULT_TABLE})",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--max-bytes", type=int, default=2_000_000)
    parser.add_argument(
        "--include-generated",
        action="store_true",
        help="include data, public, resources, generated, out, and work directories",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        candidates, skipped = scan_paths(
            args.paths,
            table=args.table,
            max_bytes=args.max_bytes,
            include_generated=args.include_generated,
        )
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(
            json.dumps(
                {
                    "vocabulary_table": str(args.table.resolve()),
                    "candidates": [candidate.to_dict() for candidate in candidates],
                    "skipped": list(skipped),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        _print_text(candidates, skipped)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
