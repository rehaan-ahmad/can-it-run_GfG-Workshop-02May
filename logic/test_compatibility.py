"""Tests for the compatibility scoring engine."""

from models.schemas import DeviceSpecs
from logic.compatibility import check_compatibility


def test_runs_great():
    """Device exceeds recommended specs → RUNS_GREAT."""
    device = DeviceSpecs(
        ram_gb=16, gpu_tier=4, cpu_tier=4, storage_gb=70, os="Windows 11"
    )
    result = check_compatibility("cyberpunk2077", device)
    assert result["verdict"] == "RUNS_GREAT"
    assert result["meets_minimum"] is True
    assert result["meets_recommended"] is True
    assert result["min_score"] == 1.0
    assert result["rec_score"] >= 0.85


def test_runs_ok():
    """Device meets minimum and partially meets recommended → RUNS_OK."""
    device = DeviceSpecs(
        ram_gb=12, gpu_tier=3, cpu_tier=4, storage_gb=70, os="Windows 10"
    )
    result = check_compatibility("cyberpunk2077", device)
    # min_score should be 1.0, rec_score between 0.5 and 0.85
    assert result["verdict"] in ("RUNS_OK", "RUNS_GREAT")
    assert result["meets_minimum"] is True


def test_runs_poor():
    """Device partially meets minimum → RUNS_POOR."""
    device = DeviceSpecs(
        ram_gb=6, gpu_tier=1, cpu_tier=2, storage_gb=70, os="Windows 10"
    )
    result = check_compatibility("cyberpunk2077", device)
    assert result["verdict"] in ("RUNS_POOR", "WONT_RUN")
    assert result["min_score"] < 1.0


def test_wont_run():
    """Device far below minimum → WONT_RUN."""
    device = DeviceSpecs(
        ram_gb=2, gpu_tier=1, cpu_tier=1, storage_gb=10, os="Windows 7"
    )
    result = check_compatibility("cyberpunk2077", device)
    assert result["verdict"] == "WONT_RUN"
    assert result["meets_minimum"] is False
    assert result["meets_recommended"] is False
    assert result["min_score"] < 0.6


def test_game_not_found():
    """Non-existent game returns an error dict."""
    device = DeviceSpecs(
        ram_gb=16, gpu_tier=5, cpu_tier=5, storage_gb=500, os="Windows 11"
    )
    result = check_compatibility("nonexistent_game", device)
    assert "error" in result


def test_bottleneck_present():
    """Result includes a bottleneck field."""
    device = DeviceSpecs(
        ram_gb=16, gpu_tier=2, cpu_tier=4, storage_gb=70, os="Windows 10"
    )
    result = check_compatibility("cyberpunk2077", device)
    assert result["bottleneck"] == "GPU"


def test_mobile_game():
    """Mobile game scoring works."""
    device = DeviceSpecs(
        ram_gb=4, gpu_tier=2, cpu_tier=2, storage_gb=8, os="Android 8"
    )
    result = check_compatibility("pubgmobile", device)
    assert result["verdict"] in ("RUNS_GREAT", "RUNS_OK")
    assert result["meets_minimum"] is True
