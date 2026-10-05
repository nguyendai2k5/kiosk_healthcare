from ocr.core import ready, service_name


def test_smoke() -> None:
    assert ready() is True
    assert service_name() == "ocr"
