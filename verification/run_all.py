"""Run the finite scientific checks; optionally replace their saved report."""

import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

import numpy
import scipy


HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="replace verification/results.json with this run")
    args = parser.parse_args()
    scripts = ("verify_converse.py", "verify_receiver.py")
    results = {}
    for name in scripts:
        completed = subprocess.run(
            [sys.executable, str(HERE / name)],
            check=True, capture_output=True, text=True, cwd=HERE.parent,
        )
        result = json.loads(completed.stdout)
        if result.get("status") != "passed":
            raise RuntimeError(f"{name}: missing successful check status")
        results[name] = result
        print(f"PASS {name}")
    report = {
        "schema_version": 1,
        "purpose": "finite scientific checks, not uniform proof or external review",
        "runtime": {"python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__},
        "source_sha256": {
            name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
            for name in (*scripts, "run_all.py")
        },
        "checks": results,
    }
    if args.write:
        destination = HERE / "results.json"
        destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print("Saved verification/results.json")
    else:
        print("All assertions passed; saved outputs were not modified.")


if __name__ == "__main__":
    main()
