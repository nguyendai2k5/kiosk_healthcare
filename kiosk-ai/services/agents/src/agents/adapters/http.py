from __future__ import annotations

from fastapi import FastAPI

from agents.core import ready, service_name


def build_app() -> FastAPI:
    app = FastAPI(title="Agents service")

    @app.get("/health")
    def health() -> dict[str, str | bool]:
        return {"service": service_name(), "ready": ready()}

    return app
