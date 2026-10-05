from datetime import UTC, datetime

from kiosk_contracts.models import Envelope, ErrorCode, TriageRequest, Vitals
from pydantic import ValidationError


def test_contract_models_are_valid() -> None:
    request = TriageRequest(
        patient_id="p-001",
        vitals=Vitals(heart_rate_bpm=72.5, spo2_percent=98.0),
    )
    assert request.patient_id == "p-001"
    assert request.vitals is not None

    envelope = Envelope(
        message_id="msg-1",
        event_type="triage.request",
        source="kiosk",
        timestamp=datetime(2024, 1, 1, tzinfo=UTC),
        data={"code": ErrorCode.VALIDATION_ERROR.value},
    )
    assert envelope.event_type == "triage.request"

    try:
        TriageRequest(patient_id="", vitals=None)
    except ValidationError:
        pass
    else:
        raise AssertionError("Expected validation error")
