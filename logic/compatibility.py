"""Compatibility scoring engine.

GPU Tiers: 1=Intel UHD/Iris, 2=GTX 1050/RX 560, 3=GTX 1660/RX 5600, 4=RTX 3070/RX 6800, 5=RTX 4090/RX 7900XTX
CPU Tiers: 1=Dual-core <2GHz, 2=i3/Ryzen 3 budget, 3=i5/Ryzen 5 mid, 4=i7/Ryzen 7, 5=i9/Ryzen 9/Threadripper
"""

from typing import List

from models.schemas import DeviceSpecs
from data.games import GAMES


# ---------------------------------------------------------------------------
# Tier label lookups (used in upgrade tips)
# ---------------------------------------------------------------------------
GPU_TIER_LABELS = {
    1: "Intel UHD / Iris",
    2: "GTX 1050 / RX 560",
    3: "GTX 1660 / RX 5600",
    4: "RTX 3070 / RX 6800",
    5: "RTX 4090 / RX 7900 XTX",
}

CPU_TIER_LABELS = {
    1: "Dual-core < 2 GHz",
    2: "i3 / Ryzen 3",
    3: "i5 / Ryzen 5",
    4: "i7 / Ryzen 7",
    5: "i9 / Ryzen 9 / Threadripper",
}


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------

def _score_device_against(device: DeviceSpecs, threshold: dict) -> float:
    """Score a device against a set of requirements (min or rec).

    Weights:
        RAM     – 25
        GPU     – 40  (most important)
        CPU     – 25
        Storage – 10
    Returns a float between 0.0 and 1.0.
    """
    score = 0
    max_score = 100  # 25 + 40 + 25 + 10

    # RAM (weight 25)
    if device.ram_gb >= threshold["ram_gb"]:
        score += 25
    elif device.ram_gb >= threshold["ram_gb"] * 0.75:
        score += 15

    # GPU (weight 40)
    gpu_diff = device.gpu_tier - threshold["gpu_tier"]
    if gpu_diff >= 0:
        score += 40
    elif gpu_diff == -1:
        score += 20
    elif gpu_diff == -2:
        score += 5

    # CPU (weight 25)
    cpu_diff = device.cpu_tier - threshold["cpu_tier"]
    if cpu_diff >= 0:
        score += 25
    elif cpu_diff == -1:
        score += 12

    # Storage (weight 10)
    if device.storage_gb >= threshold["storage_gb"]:
        score += 10

    return score / max_score


def _find_bottleneck(device: DeviceSpecs, threshold: dict) -> str:
    """Return the name of the component furthest below the threshold."""
    gaps = {
        "RAM": threshold["ram_gb"] - device.ram_gb,
        "GPU": threshold["gpu_tier"] - device.gpu_tier,
        "CPU": threshold["cpu_tier"] - device.cpu_tier,
        "Storage": threshold["storage_gb"] - device.storage_gb,
    }
    # Normalise GPU/CPU gaps (tier range 1-5) vs GB gaps for fair comparison
    normalised = {
        "RAM": gaps["RAM"] / max(threshold["ram_gb"], 1),
        "GPU": gaps["GPU"] / 5,
        "CPU": gaps["CPU"] / 5,
        "Storage": gaps["Storage"] / max(threshold["storage_gb"], 1),
    }
    return max(normalised, key=normalised.get)


def _upgrade_tip(bottleneck: str, device: DeviceSpecs, rec: dict) -> str:
    """Generate a human-readable upgrade suggestion."""
    if bottleneck == "GPU":
        target = rec["gpu_tier"]
        label = GPU_TIER_LABELS.get(target, f"Tier {target}")
        diff = target - device.gpu_tier
        return f"Your GPU is {diff} tier(s) below recommended. Consider upgrading to {label} or higher."
    if bottleneck == "CPU":
        target = rec["cpu_tier"]
        label = CPU_TIER_LABELS.get(target, f"Tier {target}")
        diff = target - device.cpu_tier
        return f"Your CPU is {diff} tier(s) below recommended. Consider upgrading to {label} or higher."
    if bottleneck == "RAM":
        return f"You have {device.ram_gb} GB RAM but {rec['ram_gb']} GB is recommended. Consider adding more memory."
    if bottleneck == "Storage":
        return f"You have {device.storage_gb} GB free but {rec['storage_gb']} GB is needed. Free up or add more storage."
    return "Your system is looking good!"


def _settings_suggestion(min_score: float, rec_score: float) -> str:
    """Suggest in-game settings based on scores."""
    if rec_score >= 0.85:
        return "High-Ultra settings at 1440p or higher. Expect 60+ FPS."
    if rec_score >= 0.5:
        return "Medium-High settings at 1080p. Expect 45-60 FPS."
    if min_score >= 0.8:
        return "Low-Medium settings at 1080p. Expect 30-40 FPS."
    if min_score >= 0.6:
        return "Low settings at 720p. Expect 25-35 FPS."
    return "This game may not run playably on your current hardware."


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def check_compatibility(game_id: str, device: DeviceSpecs) -> dict:
    """Evaluate a device against a game and return a full result dict."""

    # Look up the game
    game = None
    for g in GAMES:
        if g["id"] == game_id:
            game = g
            break
    if game is None:
        return {"error": f"Game '{game_id}' not found"}

    min_req = game["min"]
    rec_req = game["recommended"]

    min_score = _score_device_against(device, min_req)
    rec_score = _score_device_against(device, rec_req)

    # Verdict
    if min_score >= 1.0 and rec_score >= 0.85:
        verdict = "RUNS_GREAT"
        verdict_label = "Runs Great 🚀"
    elif min_score >= 1.0 and rec_score >= 0.5:
        verdict = "RUNS_OK"
        verdict_label = "Runs OK ⚠️"
    elif min_score >= 0.6:
        verdict = "RUNS_POOR"
        verdict_label = "Runs Poorly 🐌"
    else:
        verdict = "WONT_RUN"
        verdict_label = "Won't Run ❌"

    meets_minimum = min_score >= 1.0
    meets_recommended = rec_score >= 1.0

    bottleneck = _find_bottleneck(device, rec_req)
    upgrade = _upgrade_tip(bottleneck, device, rec_req)
    settings = _settings_suggestion(min_score, rec_score)

    return {
        "game_id": game["id"],
        "game_name": game["name"],
        "game_image": game["image_url"],
        "game_genre": game["genre"],
        "verdict": verdict,
        "verdict_label": verdict_label,
        "min_score": round(min_score, 2),
        "rec_score": round(rec_score, 2),
        "bottleneck": bottleneck,
        "upgrade_tip": upgrade,
        "settings_suggestion": settings,
        "meets_minimum": meets_minimum,
        "meets_recommended": meets_recommended,
        "device": {
            "ram_gb": device.ram_gb,
            "gpu_tier": device.gpu_tier,
            "cpu_tier": device.cpu_tier,
            "storage_gb": device.storage_gb,
            "os": device.os,
        },
        "min_req": min_req,
        "rec_req": rec_req,
    }
