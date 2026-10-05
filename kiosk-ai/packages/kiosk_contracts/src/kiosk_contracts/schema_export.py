from __future__ import annotations

import json
from pathlib import Path

from pydantic import TypeAdapter

from .models import (
    AudioEvent,
    Envelope,
    ErrorCode,
    IdOcrEvent,
    PrintJob,
    TriageRequest,
    TriageResponse,
    VisionEvent,
    Vitals,
)

MODELS = [
    ("Envelope", Envelope),
    ("Vitals", Vitals),
    ("VisionEvent", VisionEvent),
    ("AudioEvent", AudioEvent),
    ("IdOcrEvent", IdOcrEvent),
    ("TriageRequest", TriageRequest),
    ("TriageResponse", TriageResponse),
    ("PrintJob", PrintJob),
    ("ErrorCode", ErrorCode),
]


def export_all() -> None:
    out_dir = Path(__file__).resolve().parents[4] / "contracts" / "schemas"
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, model in MODELS:
        schema = TypeAdapter(model).json_schema()
        path = out_dir / f"{name}.schema.json"
        path.write_text(json.dumps(schema, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    export_all()


if __name__ == "__main__":
    main()
