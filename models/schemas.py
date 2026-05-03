from typing import List, Optional

from pydantic import BaseModel, Field


class DeviceSpecs(BaseModel):
    """Hardware specifications for a device.

    - ``ram_gb``: Amount of RAM in gigabytes.
    - ``gpu_tier``: GPU performance tier (1‑5).
    - ``cpu_tier``: CPU performance tier (1‑5).
    - ``storage_gb``: Available storage in gigabytes.
    - ``os``: Operating system name.
    - ``device_type``: Optional descriptor, e.g., "PC", "Laptop", "Mobile".
    """

    ram_gb: int = Field(..., description="RAM in GB")
    gpu_tier: int = Field(..., ge=1, le=5, description="GPU tier (1‑5)")
    cpu_tier: int = Field(..., ge=1, le=5, description="CPU tier (1‑5)")
    storage_gb: int = Field(..., description="Storage in GB")
    os: str = Field(..., description="Operating system")
    device_type: Optional[str] = Field(None, description="Device type, e.g., PC, Laptop, Mobile")


class Game(BaseModel):
    """Definition of a game entry in the database."""

    id: str = Field(..., description="Unique identifier used in the API")
    name: str = Field(..., description="Human readable name")
    genre: str = Field(..., description="Game genre")
    image_url: str = Field(..., description="URL to a placeholder image")
    release_year: int = Field(..., description="Year the game was released")
    platform: List[str] = Field(..., description="Supported platforms, e.g., [\"PC\"]")
    min: DeviceSpecs = Field(..., description="Minimum hardware requirements")
    recommended: DeviceSpecs = Field(..., description="Recommended hardware requirements")


class CompatibilityRequest(BaseModel):
    """Payload submitted by the front‑end when checking compatibility."""

    device: DeviceSpecs = Field(..., description="User's device specifications")
    game_id: str = Field(..., description="ID of the game to evaluate")


class CompatibilityResult(BaseModel):
    """Result returned to the front‑end after scoring a device against a game."""

    game_id: str = Field(..., description="ID of the evaluated game")
    compatible: bool = Field(..., description="True if the device meets the *minimum* requirements")
    recommendation_met: bool = Field(
        ..., description="True if the device meets the *recommended* requirements"
    )
    score: int = Field(..., ge=0, le=100, description="Overall compatibility score (0‑100)")
    verdict: str = Field(..., description="Human readable verdict, e.g., 'Excellent', 'Marginal', 'Fail'")
