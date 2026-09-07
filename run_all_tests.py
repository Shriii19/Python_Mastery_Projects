from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECTS = [
    ROOT / "02-Hospital-Management",
    ROOT / "03-Banking-System",
    ROOT / "04-Inventory-Management",
    ROOT / "05-CSV Data Analyzer",
]


def run_project_tests(project_dir: Path) -> int:
    print(f"\n=== Running tests for {project_dir.name} ===")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=project_dir,
        check=False,
    )
    return result.returncode


def main() -> int:
    failures: list[str] = []
    for project_dir in PROJECTS:
        if not project_dir.exists():
            failures.append(f"Missing project directory: {project_dir.name}")
            continue
        exit_code = run_project_tests(project_dir)
        if exit_code != 0:
            failures.append(project_dir.name)

    if failures:
        print("\nFailed projects:")
        for name in failures:
            print(f"- {name}")
        return 1

    print("\nAll project test suites passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
