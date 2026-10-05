from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ErrorCode(StrEnum):
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    EXTERNAL_TIMEOUT = "EXTERNAL_TIMEOUT"
    NOT_FOUND = "NOT_FOUND"
    UNSUPPORTED_FORMAT = "UNSUPPORTED_FORMAT"


class Envelope(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message_id: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1)
    source: str = Field(..., min_length=1)
    timestamp: datetime
    correlation_id: str | None = None
    data: dict[str, Any] = Field(default_factory=dict)


class Vitals(BaseModel):
    model_config = ConfigDict(extra="forbid")

    heart_rate_bpm: float | None = Field(default=None, ge=0.0, le=300.0)
    systolic_bp_mmhg: int | None = Field(default=None, ge=20, le=260)
    diastolic_bp_mmhg: int | None = Field(default=None, ge=20, le=220)
    spo2_percent: float | None = Field(default=None, ge=0.0, le=100.0)
    temperature_c: float | None = Field(default=None, ge=25.0, le=45.0)


class VisionEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    image_uri: str = Field(..., min_length=1)
    camera_id: str | None = None
    frame_index: int | None = Field(default=None, ge=0)


class AudioEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    audio_uri: str = Field(..., min_length=1)
    sample_rate_hz: int | None = Field(default=None, ge=1)
    duration_ms: int | None = Field(default=None, ge=0)


class IdOcrEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document_type: str = Field(..., min_length=1)
    image_uri: str = Field(..., min_length=1)
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class TriageRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    patient_id: str = Field(..., min_length=1)
    vitals: Vitals | None = None
    vision: VisionEvent | None = None
    audio: AudioEvent | None = None
    id_ocr: IdOcrEvent | None = None


class TriageResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    patient_id: str = Field(..., min_length=1)
    status: str = Field(default="received", min_length=1)
    risk_level: str | None = None
    message: str | None = None
    next_step: str | None = None


class PrintJob(BaseModel):
    model_config = ConfigDict(extra="forbid")

    print_id: str = Field(..., min_length=1)
    patient_id: str = Field(..., min_length=1)
    document_type: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    priority: str = Field(default="normal", min_length=1)
