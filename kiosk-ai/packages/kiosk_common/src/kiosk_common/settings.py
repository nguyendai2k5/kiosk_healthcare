from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str = os.getenv("APP_ENV", "local")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    service_name: str = os.getenv("SERVICE_NAME", "unknown")
    mqtt_broker: str = os.getenv("MQTT_BROKER", "mqtt://localhost:1883")
    postgres_dsn: str = os.getenv("POSTGRES_DSN", "postgresql://kiosk:kiosk@localhost:5432/kiosk")
    qdrant_url: str = os.getenv("QDRANT_URL", "http://localhost:6333")
