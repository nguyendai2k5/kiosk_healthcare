# Audio Service

## Goal

Skeleton service for the kiosk healthcare platform.

## Input and output

Input: environment variables and shared contract payloads.
Output: structured event payloads or HTTP health responses.

## Environment variables

- APP_ENV
- LOG_LEVEL
- SERVICE_NAME
- MQTT_BROKER
- POSTGRES_DSN
- QDRANT_URL

## Run

```bash
uv run --package audio python -m audio.adapters.cli
```

## Test IDs

| Test ID | Purpose |
| --- | --- |
| AUDIO-SMOKE-001 | smoke startup check |
| AUDIO-INT-001 | integration placeholder |
