from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    subprocess.run(
        ["uv", "run", "--package", "kiosk-contracts", "python", "-m", "kiosk_contracts.schema_export"],
        cwd=project_root,
        check=True,
    )


if __name__ == "__main__":
    main()
