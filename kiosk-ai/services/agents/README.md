# Agents Service

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
uv run --package agents python -m agents.adapters.cli
```

## Test IDs

| Test ID | Purpose |
| --- | --- |
| AGENTS-SMOKE-001 | smoke startup check |
| AGENTS-INT-001 | integration placeholder |
