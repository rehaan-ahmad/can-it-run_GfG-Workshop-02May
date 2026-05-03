import json
from typing import List

# Import the Pydantic models
from models import schemas as model_schemas

# Import the GAMES list generated in data/games.py
from data import games as games_data

GAMES = games_data.GAMES


def _os_match(device_os: str, allowed_os: List[str]) -> bool:
    """Return True if the device OS matches any of the allowed OS strings.
    Comparison is case‑insensitive and stripped of surrounding whitespace.
    """
    device_os_clean = device_os.strip().lower()
    return any(device_os_clean == os_str.strip().lower() for os_str in allowed_os)


def _spec_score(device_value: int, required_value: int) -> float:
    """Return a ratio (capped at 1.0) of device spec to required spec.
    Used for scoring; higher is better.
    """
    if required_value == 0:
        return 1.0
    return min(device_value / required_value, 1.0)


def score_device(device: model_schemas.DeviceSpecs, game: dict) -> model_schemas.CompatibilityResult:
    """Calculate compatibility between a device and a game.

    The function returns a ``CompatibilityResult`` model containing:
    - ``compatible`` – meets **minimum** requirements.
    - ``recommendation_met`` – meets **recommended** requirements.
    - ``score`` – an integer 0‑100 reflecting overall fit.
    - ``verdict`` – a human‑readable string (Excellent, Marginal, Fail).
    """
    # Minimum requirements check
    min_req = game["min"]
    rec_req = game["recommended"]

    compatible = (
        device.ram_gb >= min_req["ram_gb"]
        and device.gpu_tier >= min_req["gpu_tier"]
        and device.cpu_tier >= min_req["cpu_tier"]
        and device.storage_gb >= min_req["storage_gb"]
        and _os_match(device.os, min_req["os"])
    )

    # Recommended requirements check
    recommendation_met = (
        device.ram_gb >= rec_req["ram_gb"]
        and device.gpu_tier >= rec_req["gpu_tier"]
        and device.cpu_tier >= rec_req["cpu_tier"]
        and device.storage_gb >= rec_req["storage_gb"]
        and _os_match(device.os, rec_req["os"])
    )

    # Scoring – each of the five specs contributes equally.
    # We give 20 points per spec for meeting the *minimum* requirement.
    # An additional 10 points per spec is awarded if the *recommended* requirement is also met.
    score = 0
    specs = [
        (device.ram_gb, min_req["ram_gb"], rec_req["ram_gb"]),
        (device.gpu_tier, min_req["gpu_tier"], rec_req["gpu_tier"]),
        (device.cpu_tier, min_req["cpu_tier"], rec_req["cpu_tier"]),
        (device.storage_gb, min_req["storage_gb"], rec_req["storage_gb"]),
    ]
    for dev, min_val, rec_val in specs:
        if dev >= min_val:
            score += 20
            if dev >= rec_val:
                score += 10
    # OS handling – treat as a single boolean spec (20 points for min, extra 10 for rec)
    if _os_match(device.os, min_req["os"]):
        score += 20
        if _os_match(device.os, rec_req["os"]):
            score += 10

    # Clamp score to 0‑100 range (should already be within bounds)
    score = max(0, min(int(score), 100))

    # Verdict mapping
    if score >= 80:
        verdict = "Excellent"
    elif score >= 50:
        verdict = "Marginal"
    else:
        verdict = "Fail"

    return model_schemas.CompatibilityResult(
        game_id=game["id"],
        compatible=compatible,
        recommendation_met=recommendation_met,
        score=score,
        verdict=verdict,
    )
