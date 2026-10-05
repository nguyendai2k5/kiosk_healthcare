from __future__ import annotations

from fastapi import FastAPI

from ocr.core import ready, service_name


def build_app() -> FastAPI:
    app = FastAPI(title="Ocr service")

    @app.get("/health")
    def health() -> dict[str, str | bool]:
        return {"service": service_name(), "ready": ready()}

    return app
