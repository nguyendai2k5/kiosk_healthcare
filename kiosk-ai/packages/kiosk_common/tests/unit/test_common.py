from kiosk_common.settings import Settings
from kiosk_common.topic_builder import build_topic


def test_common_helpers() -> None:
    settings = Settings(service_name="demo")
    assert settings.service_name == "demo"
    assert build_topic("health", "screen", "vitals") == "health/screen/vitals"
