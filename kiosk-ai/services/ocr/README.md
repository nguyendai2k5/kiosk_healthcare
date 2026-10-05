# Ocr Service

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
uv run --package ocr python -m ocr.adapters.cli
```

## Test IDs

| Test ID | Purpose |
| --- | --- |
| OCR-SMOKE-001 | smoke startup check |
| OCR-INT-001 | integration placeholder |
