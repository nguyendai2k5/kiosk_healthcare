FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1             PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --system app && useradd --system --gid app --create-home app

COPY pyproject.toml ./
COPY src ./src
COPY tests ./tests

USER app

CMD ["python3", "-m", "pytest", "-q"]
