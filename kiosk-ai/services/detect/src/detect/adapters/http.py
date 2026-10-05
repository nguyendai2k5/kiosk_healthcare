from __future__ import annotations

from fastapi import FastAPI

from detect.core import ready, service_name


def build_app() -> FastAPI:
    app = FastAPI(title="Detect service")

    @app.get("/health")
    def health() -> dict[str, str | bool]:
        return {"service": service_name(), "ready": ready()}

    return app
