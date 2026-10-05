from __future__ import annotations

from collections import defaultdict


class MetricsRegistry:
    def __init__(self) -> None:
        self._counters: dict[str, float] = defaultdict(float)

    def counter(self, name: str, value: float = 1.0, labels: dict[str, str] | None = None) -> None:
        key = self._compose_key(name, labels)
        self._counters[key] += value

    @staticmethod
    def _compose_key(name: str, labels: dict[str, str] | None = None) -> str:
        if not labels:
            return name
        return f"{name}|{'|'.join(f'{k}={v}' for k, v in sorted(labels.items()))}"
