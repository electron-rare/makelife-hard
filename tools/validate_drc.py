#!/usr/bin/env python3
"""validate_drc.py — Run KiCad ERC/DRC on design blocks and templates.

Usage:
    python tools/validate_drc.py                    # validate everything
    python tools/validate_drc.py --blocks-only      # only blocks/*.kicad_sch
    python tools/validate_drc.py --templates-only   # only templates/*
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_schematics(directory: str) -> list[Path]:
    """Find all .kicad_sch files recursively."""
    return sorted(Path(ROOT / directory).rglob("*.kicad_sch"))


def find_pcbs(directory: str) -> list[Path]:
    """Find all .kicad_pcb files recursively."""
    return sorted(Path(ROOT / directory).rglob("*.kicad_pcb"))


def run_erc(sch_path: Path) -> tuple[bool, str]:
    """Run kicad-cli sch erc on a schematic. Returns (passed, report)."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        output_path = tmp.name

    try:
        result = subprocess.run(
            ["kicad-cli", "sch", "erc", "--format", "json", "--output", output_path, str(sch_path)],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        return True, "SKIP — kicad-cli not available"
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"

    try:
        with open(output_path) as f:
            report = json.load(f)
        errors = sum(1 for v in report.get("violations", []) if v.get("severity") == "error")
        return errors == 0, f"{errors} errors, {len(report.get('violations', []))} total violations"
    except (json.JSONDecodeError, FileNotFoundError):
        return result.returncode == 0, result.stderr or result.stdout or "No output"


def run_drc(pcb_path: Path) -> tuple[bool, str]:
    """Run kicad-cli pcb drc on a PCB. Returns (passed, report)."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        output_path = tmp.name

    try:
        result = subprocess.run(
            ["kicad-cli", "pcb", "drc", "--format", "json", "--output", output_path, str(pcb_path)],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        return True, "SKIP — kicad-cli not available"
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"

    try:
        with open(output_path) as f:
            report = json.load(f)
        errors = sum(1 for v in report.get("violations", []) if v.get("severity") == "error")
        return errors == 0, f"{errors} errors, {len(report.get('violations', []))} total violations"
    except (json.JSONDecodeError, FileNotFoundError):
        return result.returncode == 0, result.stderr or result.stdout or "No output"


def main():
    parser = argparse.ArgumentParser(description="Validate KiCad design blocks and templates")
    parser.add_argument("--blocks-only", action="store_true", help="Only validate blocks/")
    parser.add_argument("--templates-only", action="store_true", help="Only validate templates/")
    args = parser.parse_args()

    validate_blocks = not args.templates_only
    validate_templates = not args.blocks_only

    total = 0
    passed = 0
    failed = 0
    skipped = 0

    if validate_blocks:
        schematics = find_schematics("blocks")
        print(f"\n=== Blocks ERC ({len(schematics)} schematics) ===")
        for sch in schematics:
            total += 1
            ok, report = run_erc(sch)
            rel = sch.relative_to(ROOT)
            if "SKIP" in report:
                skipped += 1
                print(f"  SKIP  {rel}")
            elif ok:
                passed += 1
                print(f"  PASS  {rel}")
            else:
                failed += 1
                print(f"  FAIL  {rel} — {report}")

    if validate_templates:
        schematics = find_schematics("templates")
        pcbs = find_pcbs("templates")
        print(f"\n=== Templates ERC ({len(schematics)} schematics) ===")
        for sch in schematics:
            total += 1
            ok, report = run_erc(sch)
            rel = sch.relative_to(ROOT)
            if "SKIP" in report:
                skipped += 1
                print(f"  SKIP  {rel}")
            elif ok:
                passed += 1
                print(f"  PASS  {rel}")
            else:
                failed += 1
                print(f"  FAIL  {rel} — {report}")

        print(f"\n=== Templates DRC ({len(pcbs)} PCBs) ===")
        for pcb in pcbs:
            total += 1
            ok, report = run_drc(pcb)
            rel = pcb.relative_to(ROOT)
            if "SKIP" in report:
                skipped += 1
                print(f"  SKIP  {rel}")
            elif ok:
                passed += 1
                print(f"  PASS  {rel}")
            else:
                failed += 1
                print(f"  FAIL  {rel} — {report}")

    print(f"\n=== Summary ===")
    print(f"  Total:   {total}")
    print(f"  Passed:  {passed}")
    print(f"  Failed:  {failed}")
    print(f"  Skipped: {skipped}")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
