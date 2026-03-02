#!/usr/bin/env python3
"""Build a personalized PRISM authority system launch pack.

Usage:
    python authority-system/system_builder.py \
      --config authority-system/config.example.json \
      --output authority-system/output
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List


DEFAULT_FILES: List[str] = [
    "README.md",
    "positioning-kit.md",
    "landing-page-copy.md",
    "offer-deck.md",
    "outbound-scripts.md",
    "sales-operating-system.md",
    "fulfillment-sop.md",
    "content-engine.md",
    "launch-checklist.md",
    "templates/proposal-template.md",
    "templates/client-intake-form.md",
    "tracking/pipeline-scorecard.csv",
]


REQUIRED_CONFIG_FIELDS: List[str] = [
    "your_name",
    "booking_link",
    "email",
]


@dataclass
class BuildContext:
    authority_root: Path
    output_dir: Path
    replacements: Dict[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a personalized PRISM authority launch pack."
    )
    parser.add_argument(
        "--config",
        required=True,
        type=Path,
        help="Path to JSON configuration file.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Output directory for generated files.",
    )
    parser.add_argument(
        "--source",
        default=None,
        type=Path,
        help="Optional authority-system source directory. Defaults to script directory.",
    )
    return parser.parse_args()


def load_config(config_path: Path) -> Dict[str, str]:
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    missing = [key for key in REQUIRED_CONFIG_FIELDS if not config.get(key)]
    if missing:
        raise ValueError(
            f"Missing required config fields: {', '.join(sorted(missing))}"
        )

    return config


def build_replacements(config: Dict[str, str]) -> Dict[str, str]:
    return {
        "[YOUR_NAME]": config["your_name"],
        "[BOOKING_LINK]": config["booking_link"],
        "[EMAIL]": config["email"],
        "[CASE_STUDY_OR_PROOF_LINK]": config.get(
            "case_study_or_proof_link", "Add-your-proof-link-here"
        ),
        "[CLIENT_NAME]": config.get("default_client_name", "Client Name"),
        "[DATE]": config.get("default_proposal_date", "YYYY-MM-DD"),
        "[START_DATE]": config.get("default_start_date", "YYYY-MM-DD"),
        "[END_DATE]": config.get("default_end_date", "YYYY-MM-DD"),
        "[TOTAL_FEE]": config.get("default_total_fee", "$5,000"),
        "[PAYMENT_TERMS]": config.get("default_payment_terms", "50% upfront, 50% on day 21"),
        "[MONTHLY_FEE]": config.get("default_monthly_fee", "$2,000"),
    }


def apply_replacements(content: str, replacements: Dict[str, str]) -> str:
    updated = content
    for placeholder, value in replacements.items():
        updated = updated.replace(placeholder, value)
    return updated


def unresolved_placeholders(content: str) -> List[str]:
    return sorted(set(re.findall(r"\[[A-Z0-9_]+\]", content)))


def iter_source_files(authority_root: Path) -> Iterable[Path]:
    for relative in DEFAULT_FILES:
        source_file = authority_root / relative
        if not source_file.exists():
            raise FileNotFoundError(f"Expected source file not found: {source_file}")
        yield source_file


def write_file(target_path: Path, content: str) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with target_path.open("w", encoding="utf-8") as file:
        file.write(content)


def build_pack(context: BuildContext) -> Dict[str, List[str]]:
    unresolved_by_file: Dict[str, List[str]] = {}

    if context.output_dir.exists():
        shutil.rmtree(context.output_dir)
    context.output_dir.mkdir(parents=True, exist_ok=True)

    for source_file in iter_source_files(context.authority_root):
        relative = source_file.relative_to(context.authority_root)
        output_file = context.output_dir / relative

        content = source_file.read_text(encoding="utf-8")
        rendered = apply_replacements(content, context.replacements)
        write_file(output_file, rendered)

        unresolved = unresolved_placeholders(rendered)
        if unresolved:
            unresolved_by_file[str(relative)] = unresolved

    return unresolved_by_file


def write_summary(
    output_dir: Path,
    unresolved_by_file: Dict[str, List[str]],
    replacements: Dict[str, str],
) -> None:
    lines: List[str] = []
    lines.append("# Build Summary")
    lines.append("")
    lines.append("## Applied Replacements")
    lines.append("")
    for key, value in replacements.items():
        lines.append(f"- {key} -> {value}")

    lines.append("")
    lines.append("## Files With Remaining Placeholders")
    lines.append("")
    if not unresolved_by_file:
        lines.append("No unresolved placeholders found.")
    else:
        for file_name, placeholders in sorted(unresolved_by_file.items()):
            joined = ", ".join(placeholders)
            lines.append(f"- {file_name}: {joined}")

    summary_path = output_dir / "BUILD_SUMMARY.md"
    write_file(summary_path, "\n".join(lines) + "\n")


def main() -> None:
    args = parse_args()
    script_root = Path(__file__).resolve().parent
    authority_root = args.source.resolve() if args.source else script_root
    output_dir = args.output.resolve()
    config = load_config(args.config.resolve())
    replacements = build_replacements(config)

    context = BuildContext(
        authority_root=authority_root,
        output_dir=output_dir,
        replacements=replacements,
    )

    unresolved = build_pack(context)
    write_summary(output_dir, unresolved, replacements)

    print("Build complete.")
    print(f"Source: {authority_root}")
    print(f"Output: {output_dir}")
    if unresolved:
        print("Unresolved placeholders remain in some files.")
        print("Review BUILD_SUMMARY.md for details.")
    else:
        print("All placeholders resolved.")


if __name__ == "__main__":
    main()
