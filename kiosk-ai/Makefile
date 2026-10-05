.PHONY: setup lint typecheck test contract-export up down e2e-mock

setup:
	uv sync --all-packages --dev

lint:
	uv run ruff check packages services

typecheck:
	uv run mypy --strict packages services

test:
	uv run pytest -q

contract-export:
	uv run --package kiosk-contracts python -m kiosk_contracts.schema_export

up:
	docker compose up -d

down:
	docker compose down -v

e2e-mock:
	python3 -m http.server 8000 --directory mocks
