import json
import logging


def configure_logging(level: int = logging.INFO) -> None:
    logger = logging.getLogger()
    logger.setLevel(level)
    logger.handlers.clear()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)


class JsonLogger(logging.Logger):
    def emit(self, record: logging.LogRecord) -> None:
        payload = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        print(json.dumps(payload, separators=(",", ":"), default=str))
