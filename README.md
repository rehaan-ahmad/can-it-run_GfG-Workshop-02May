<div align="center">
  <h1>🎮 CanItRun?</h1>
  <p><strong>The Ultimate PC & Mobile Game Compatibility Checker</strong></p>

  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0+-00a393.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Google Cloud Run](https://img.shields.io/badge/Deployed_on-Google_Cloud_Run-4285F4.svg?logo=googlecloud&logoColor=white)](https://cloud.google.com/run)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
</div>

<br/>

**CanItRun** is a sleek, high-performance web application designed to answer the eternal gamer question: *"Can my device run this game?"*. Featuring a custom compatibility scoring engine, bottleneck detection, and an AI-style advisor, wrapped in a premium "Dark Terminal / Gaming HUD" aesthetic.

---

## 🚀 Live Demo

**Check it out live:** [https://canitrun-244479174966.asia-south1.run.app](https://canitrun-244479174966.asia-south1.run.app)

---

## ✨ Features

- **⚡ Instant Compatibility Scoring**: Select a game, input your device specs (RAM, CPU, GPU, Storage), and get an instant, dramatic verdict (`RUNS_GREAT`, `RUNS_OK`, `RUNS_POOR`, `WONT_RUN`).
- **🔍 Bottleneck Detection**: Identifies the weakest link in your hardware (e.g., "Your GPU is holding you back").
- **🤖 Advisor Chat**: A built-in terminal assistant that provides hardware upgrade advice and game optimization tips.
- **🎨 Premium Gaming UI**: A glassmorphic, neon-accented dark mode interface with smooth micro-animations.
- **📱 Fully Responsive**: Looks stunning on desktops, tablets, and mobile devices.

---

## 🛠️ Technology Stack

**Backend**
- **[FastAPI](https://fastapi.tiangolo.com/)**: High-performance asynchronous Python web framework.
- **Uvicorn**: Lightning-fast ASGI server.
- **Pytest**: Comprehensive automated testing suite.

**Frontend**
- **HTML5 & Vanilla CSS3**: Custom design system, CSS variables, and flexbox/grid layouts. No heavy CSS frameworks.
- **Vanilla JavaScript (ES6+)**: DOM manipulation and asynchronous API calls using the `fetch` API.

**DevOps & Deployment**
- **Docker**: Containerized application environment.
- **Google Cloud Build**: Automated CI/CD pipeline (`cloudbuild.yaml`).
- **Google Cloud Run**: Serverless, scalable production hosting.

---

## 💻 Local Development

Want to run the platform on your own machine? Follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/rehaan-ahmad/can-it-run_GfG-Workshop-02May.git
cd can-it-run_GfG-Workshop-02May
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Development Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
*Open your browser and navigate to `http://localhost:8000` to see the app!*

### 5. Run Tests
```bash
pytest
```

---

## ☁️ Deployment (Google Cloud)

This project is fully configured for zero-downtime deployment on Google Cloud Run.

1. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   gcloud config set project can-it-run
   ```
2. Submit the build & deploy via Cloud Build:
   ```bash
   gcloud builds submit --config cloudbuild.yaml .
   ```
3. *(Optional)* Ensure public access:
   ```bash
   gcloud run services add-iam-policy-binding canitrun \
       --member="allUsers" --role="roles/run.invoker" --region=asia-south1
   ```

---

<div align="center">
  <i>Built with ❤️ for gamers everywhere.</i>
</div>
