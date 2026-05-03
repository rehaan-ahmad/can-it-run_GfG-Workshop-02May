from typing import List, Optional

from pydantic import BaseModel, Field


class DeviceSpecs(BaseModel):
    """Hardware specifications for a device.

    - ``ram_gb``: Amount of RAM in gigabytes.
    - ``gpu_tier``: GPU performance tier (1-5).
    - ``cpu_tier``: CPU performance tier (1-5).
    - ``storage_gb``: Available storage in gigabytes.
    - ``os``: Operating system name.
    - ``device_type``: Optional descriptor, e.g., "PC", "Laptop", "Mobile".
    """

    ram_gb: int = Field(..., description="RAM in GB")
    gpu_tier: int = Field(..., ge=1, le=5, description="GPU tier (1-5)")
    cpu_tier: int = Field(..., ge=1, le=5, description="CPU tier (1-5)")
    storage_gb: int = Field(..., description="Storage in GB")
    os: str = Field(..., description="Operating system")
    device_type: Optional[str] = Field(None, description="Device type, e.g., PC, Laptop, Mobile")


class CompatibilityRequest(BaseModel):
    """Payload submitted by the front-end when checking compatibility."""

    game_id: str = Field(..., description="ID of the game to evaluate")
    device: DeviceSpecs = Field(..., description="User's device specifications")


class AdvisorRequest(BaseModel):
    """Payload for the advisor chat endpoint."""

    message: str = Field(..., description="User's question")
    game_id: Optional[str] = Field(None, description="Optional game context")
    device: Optional[DeviceSpecs] = Field(None, description="Optional device context")


class ContactRequest(BaseModel):
    """Payload for the contact form."""

    name: str = Field(..., description="Sender name")
    email: str = Field(..., description="Sender email")
    message: str = Field(..., description="Message body")


class DeviceSubmission(BaseModel):
    """Payload for saving a named device profile."""

    device_name: str = Field(..., description="Friendly name, e.g. 'My Gaming PC'")
    device: DeviceSpecs = Field(..., description="The device specs")
