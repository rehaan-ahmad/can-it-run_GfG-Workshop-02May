import pytest
from models import schemas as model_schemas
from data import games as games_data
from logic.compatibility import score_device


def get_game_by_id(game_id: str):
    for g in games_data.GAMES:
        if g["id"] == game_id:
            return g
    raise ValueError(f"Game {game_id} not found")


def test_score_minimum_met():
    game = get_game_by_id("cyberpunk2077")
    device = model_schemas.DeviceSpecs(
        ram_gb=8,
        gpu_tier=2,
        cpu_tier=3,
        storage_gb=70,
        os="Windows 10",
    )
    result = score_device(device, game)
    assert result.compatible is True
    # Recommended not met because gpu_tier=2 < 4 and cpu_tier=3 < 4
    assert result.recommendation_met is False
    assert 50 <= result.score < 80  # marginal range
    assert result.verdict == "Marginal"


def test_score_recommended_met():
    game = get_game_by_id("cyberpunk2077")
    device = model_schemas.DeviceSpecs(
        ram_gb=16,
        gpu_tier=4,
        cpu_tier=4,
        storage_gb=70,
        os="Windows 11",
    )
    result = score_device(device, game)
    assert result.compatible is True
    assert result.recommendation_met is True
    assert result.score >= 80
    assert result.verdict == "Excellent"


def test_score_fail_minimum():
    game = get_game_by_id("cyberpunk2077")
    device = model_schemas.DeviceSpecs(
        ram_gb=4,
        gpu_tier=1,
        cpu_tier=1,
        storage_gb=30,
        os="Windows 7",
    )
    result = score_device(device, game)
    assert result.compatible is False
    assert result.recommendation_met is False
    assert result.score < 50
    assert result.verdict == "Fail"
