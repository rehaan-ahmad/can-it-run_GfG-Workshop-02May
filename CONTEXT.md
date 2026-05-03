# CanItRun — Project Context

## Overview
CanItRun is a game compatibility checker designed with a "Dark Terminal / Gaming HUD" aesthetic. It allows users to input their device specifications (RAM, GPU Tier, CPU Tier, Storage, OS) and check if their system can run specific games from a curated database.

## Architecture
- **Backend:** FastAPI (Python)
  - `main.py`: Main entry point and API endpoints.
  - `data/games.py`: Curated list of games with minimum and recommended specs.
  - `models/schemas.py`: Pydantic models for request/response validation.
  - `logic/compatibility.py`: Core logic for scoring hardware against game requirements.
- **Frontend:** Vanilla HTML, CSS, and JavaScript.
  - `static/`: Contains all frontend assets. Served directly by FastAPI.
  - Aesthetic: High-contrast dark mode (`#0D0D0D`), Neon Green accents (`#00FF9C`), and Monospace typography (`JetBrains Mono`).
- **Deployment:** Dockerized for portability, ready for Cloud Run/GCP.

## Technical Scope
- **Compatibility Scoring:** Uses a "Tier" system (1-5) for CPU and GPU to simplify comparison.
- **User Flow:**
  1. User enters device specs on the home page.
  2. User selects a game to check.
  3. System calculates compatibility score.
  4. User is presented with a "System Readout" style result page with animated verdicts.

## Design System
- **Background:** `#0D0D0D`
- **Primary Accent:** `#00FF9C` (Neon Green)
- **Status Colors:** `#FF4C4C` (Fail), `#FFD700` (Marginal)
- **Typography:** `JetBrains Mono` or `IBM Plex Mono`
- **Vibe:** Hardware diagnostic tool, scanlines, blinking cursors, typing effects.

## Development Roadmap
1. **Phase 1:** Define the game database in `data/games.py`.
2. **Phase 2:** Implement Pydantic schemas in `models/schemas.py`.
3. **Phase 3:** Develop the compatibility scoring engine in `logic/compatibility.py`.
4. **Phase 4:** Build the FastAPI endpoints in `main.py`.
5. **Phase 5:** Design and implement the Terminal-themed UI in `static/`.
6. **Phase 6:** Containerization and final polish.
