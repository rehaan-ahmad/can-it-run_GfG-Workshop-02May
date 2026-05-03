"""CanItRun — FastAPI backend.

Serves the REST API and static frontend files.
"""

import asyncio

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional

from data.games import GAMES
from models.schemas import (
    CompatibilityRequest,
    AdvisorRequest,
    ContactRequest,
    DeviceSubmission,
)
from logic.compatibility import check_compatibility

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(title="CanItRun API")

# CORS — required for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# API endpoints
# ---------------------------------------------------------------------------


@app.get("/api/games")
async def get_games(platform: Optional[str] = None):
    """Return the full game list, optionally filtered by platform."""
    if platform:
        filtered = [g for g in GAMES if platform in g["platform"]]
        return filtered
    return GAMES


@app.get("/api/games/{game_id}")
async def get_game(game_id: str):
    """Return a single game by its ID."""
    for g in GAMES:
        if g["id"] == game_id:
            return g
    raise HTTPException(status_code=404, detail=f"Game '{game_id}' not found")


@app.post("/api/check")
async def check(request: CompatibilityRequest):
    """Run compatibility check. Includes a small delay for dramatic effect."""
    await asyncio.sleep(1.5)
    result = check_compatibility(request.game_id, request.device)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/advisor")
async def advisor(request: AdvisorRequest):
    """Simple keyword-matching advisor chat."""
    msg = request.message.lower()

    keywords = {
        "upgrade": "Based on your specs, upgrading your GPU will give the biggest performance boost. GPU is the most heavily weighted component in our scoring.",
        "settings": "For your hardware, I recommend starting at Medium settings and adjusting from there. Monitor your FPS and lower shadow quality first if needed.",
        "fps": "Frame rate depends heavily on GPU tier. A Tier 3 GPU (GTX 1660 class) typically delivers 60 FPS at 1080p Medium in most titles.",
        "best game": "Given your specs, you'll get the best experience with games that match or fall below your GPU and CPU tiers. Use the checker to find your sweet spot!",
        "can i run": "Enter your device specs above and select a game to get an instant verdict!",
        "mobile": "Mobile compatibility depends on RAM and SoC generation. Most mobile games run well with 3+ GB RAM and Android 8 or iOS 12+.",
        "cheap": "Great performance per dollar: try Valorant, CS2, or Minecraft — all run on low-end hardware.",
        "ram": "RAM is important but not the biggest factor. 8 GB is the sweet spot for most modern games; 16 GB is ideal.",
        "storage": "Storage affects load times, not FPS. An SSD will dramatically improve loading but won't change in-game performance.",
    }

    for keyword, response in keywords.items():
        if keyword in msg:
            return {"response": response}

    return {
        "response": "I'm the CanItRun advisor! Ask me about upgrades, settings, FPS, game recommendations, or mobile compatibility."
    }


@app.post("/api/contact")
async def contact(request: ContactRequest):
    """Receive a contact form submission."""
    return {"status": "received", "message": "We'll get back to you shortly."}


@app.post("/api/submit-device")
async def submit_device(request: DeviceSubmission):
    """Save a named device profile (stub — no persistence yet)."""
    return {"status": "saved", "device_name": request.device_name}


# ---------------------------------------------------------------------------
# Static file serving (critical for Cloud Run)
# ---------------------------------------------------------------------------

# Serve index.html at root
@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")


# Catch-all for other HTML pages (e.g., /result.html, /games.html, /about.html)
@app.get("/{page_name}.html")
async def serve_page(page_name: str):
    return FileResponse(f"static/{page_name}.html")


# Mount static files (CSS, JS, images) — must be AFTER the catch-all route
app.mount("/static", StaticFiles(directory="static"), name="static")
