from __future__ import annotations

from ocr.core import ready, service_name


def main() -> str:
    return f"{service_name()} ready={ready()}"
