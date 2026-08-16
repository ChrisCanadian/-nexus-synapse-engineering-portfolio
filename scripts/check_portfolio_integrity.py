#!/usr/bin/env python3
"""Validate structural integrity of the public engineering portfolio.

Checks only repository-local, publication-safe properties:
- Markdown relative links resolve to files/directories in the checkout.
- JSON files parse successfully.
- Local evidence-ledger source paths exist.

External URLs are deliberately not fetched so CI stays deterministic and does not
turn third-party availability into a repository failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}


def normalize_markdown_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None

    # Markdown permits optional titles after a whitespace separator.
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]

    if target.startswith("#"):
        return None

    parts = urlsplit(target)
    if parts.scheme.lower() in EXTERNAL_SCHEMES or parts.netloc:
        return None

    path = unquote(parts.path)
    return path or None


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw = match.group(1)
            target = normalize_markdown_target(raw)
            if target is None:
                continue

            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{md.relative_to(ROOT)}: link escapes repository boundary: {raw}"
                )
                continue

            if not candidate.exists():
                errors.append(
                    f"{md.relative_to(ROOT)}: missing relative link target: {raw}"
                )
    return errors


def check_json_files() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    return errors


def check_evidence_sources() -> list[str]:
    ledger = ROOT / "evidence" / "claims-and-evidence.json"
    if not ledger.exists():
        return ["evidence/claims-and-evidence.json: missing evidence ledger"]

    data = json.loads(ledger.read_text(encoding="utf-8"))
    errors: list[str] = []
    for claim in data.get("claims", []):
        claim_id = claim.get("id", "<unknown>")
        for source in claim.get("sources", []):
            if not isinstance(source, str):
                errors.append(f"{claim_id}: non-string evidence source: {source!r}")
                continue
            if source.startswith(("http://", "https://")):
                continue
            target = (ROOT / source).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{claim_id}: evidence source escapes repository: {source}")
                continue
            if not target.exists():
                errors.append(f"{claim_id}: missing local evidence source: {source}")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_markdown_links())
    errors.extend(check_json_files())
    errors.extend(check_evidence_sources())

    if errors:
        print("Portfolio integrity check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    md_count = len(list(ROOT.rglob("*.md")))
    json_count = len(list(ROOT.rglob("*.json")))
    print("Portfolio integrity check: PASS")
    print(f"- Markdown documents checked: {md_count}")
    print(f"- JSON documents checked: {json_count}")
    print("- Relative Markdown links resolve")
    print("- Evidence-ledger local sources resolve")
    print("- External URLs intentionally not fetched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
