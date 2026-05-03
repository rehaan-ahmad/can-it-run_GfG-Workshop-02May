/* =====================================================
   CanItRun — Global JavaScript
   State management, API calls, UI interactions
   ===================================================== */

// ── Global State ──────────────────────────────────────
const STATE = {
  selectedGame: null,
  deviceSpecs: null,
  lastResult: null,
};

function saveState() {
  localStorage.setItem("canitrun", JSON.stringify(STATE));
}

function loadState() {
  const stored = localStorage.getItem("canitrun");
  if (stored) {
    const parsed = JSON.parse(stored);
    Object.assign(STATE, parsed);
  }
  return STATE;
}

// ── GPU / CPU tier labels ─────────────────────────────
const GPU_TIERS = {
  1: "Integrated — Intel UHD / Iris",
  2: "Entry — GTX 1050 / RX 560",
  3: "Mid — GTX 1660 / RX 5600",
  4: "High — RTX 3070 / RX 6800",
  5: "Ultra — RTX 4090 / RX 7900 XTX",
};

const CPU_TIERS = {
  1: "Low — Dual-core < 2 GHz",
  2: "Budget — i3 / Ryzen 3",
  3: "Mid — i5 / Ryzen 5",
  4: "High — i7 / Ryzen 7",
  5: "Flagship — i9 / Ryzen 9",
};

// ── Fetch & Render Games ──────────────────────────────
async function loadGames(platform = null) {
  const url = platform ? `/api/games?platform=${platform}` : "/api/games";
  try {
    const res = await fetch(url);
    const games = await res.json();
    renderGameGrid(games);
  } catch (err) {
    console.error("Failed to load games:", err);
  }
}

function renderGameGrid(games) {
  const grid = document.getElementById("game-grid");
  if (!grid) return;
  grid.innerHTML = "";

  games.forEach((game, i) => {
    const card = document.createElement("div");
    card.className = "card game-card reveal";
    card.style.transitionDelay = `${Math.min(i * 0.05, 0.5)}s`;
    if (STATE.selectedGame && STATE.selectedGame.id === game.id) {
      card.classList.add("selected");
    }
    card.innerHTML = `
      <img src="${game.image_url}" alt="${game.name}" loading="lazy" />
      <div class="game-name">${game.name}</div>
      <div class="game-meta">${game.genre} · ${game.platform.join(", ")}</div>
    `;
    card.addEventListener("click", () => selectGame(game, card));
    grid.appendChild(card);
  });

  // Trigger reveal
  requestAnimationFrame(() => {
    grid.querySelectorAll(".reveal").forEach((el) => el.classList.add("visible"));
  });
}

function selectGame(game, cardEl) {
  // Deselect previous
  document.querySelectorAll(".game-card.selected").forEach((c) => c.classList.remove("selected"));
  cardEl.classList.add("selected");
  STATE.selectedGame = game;
  saveState();

  // Enable run button
  const btn = document.getElementById("run-btn");
  if (btn) btn.disabled = false;
}

// ── Device Specs Collection ───────────────────────────
function collectDeviceSpecs() {
  const ram = parseInt(document.getElementById("ram")?.value || "8");
  const gpu = parseInt(document.getElementById("gpu")?.value || "1");
  const cpu = parseInt(document.getElementById("cpu")?.value || "1");
  const storage = parseInt(document.getElementById("storage")?.value || "50");
  const os = document.getElementById("os")?.value || "Windows 10";
  const deviceType = document.querySelector(".toggle-btn.active")?.dataset.value || "PC";

  return { ram_gb: ram, gpu_tier: gpu, cpu_tier: cpu, storage_gb: storage, os, device_type: deviceType };
}

// ── Toggle Buttons ────────────────────────────────────
function initToggleButtons() {
  document.querySelectorAll(".toggle-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".toggle-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      updateOSOptions();
    });
  });
}

function updateOSOptions() {
  const type = document.querySelector(".toggle-btn.active")?.dataset.value;
  const osSelect = document.getElementById("os");
  if (!osSelect) return;

  const pcOptions = ["Windows 10", "Windows 11", "Windows 7", "Windows 8", "Windows XP", "macOS", "Linux"];
  const mobileOptions = ["Android 5", "Android 7", "Android 8", "Android 9", "Android 10", "iOS 9", "iOS 11", "iOS 12", "iOS 13", "iOS 14"];

  const options = type === "Mobile" ? mobileOptions : pcOptions;
  osSelect.innerHTML = options.map((o) => `<option value="${o}">${o}</option>`).join("");
}

// ── Run Diagnostic ────────────────────────────────────
async function runDiagnostic() {
  if (!STATE.selectedGame) {
    alert("Please select a game first!");
    return;
  }

  STATE.deviceSpecs = collectDeviceSpecs();
  saveState();

  // Show loading overlay
  const overlay = document.getElementById("loading-overlay");
  if (overlay) overlay.classList.add("active");

  try {
    const res = await fetch("/api/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        game_id: STATE.selectedGame.id,
        device: STATE.deviceSpecs,
      }),
    });
    const result = await res.json();
    STATE.lastResult = result;
    saveState();
    window.location.href = "/result.html";
  } catch (err) {
    console.error("Diagnostic failed:", err);
    if (overlay) overlay.classList.remove("active");
    alert("Something went wrong. Please try again.");
  }
}

// ── Result Page Rendering ─────────────────────────────
function renderResult() {
  loadState();
  const r = STATE.lastResult;
  if (!r) {
    window.location.href = "/";
    return;
  }

  // Game header
  const gameImg = document.getElementById("result-game-img");
  const gameName = document.getElementById("result-game-name");
  const gameGenre = document.getElementById("result-game-genre");
  if (gameImg) gameImg.src = r.game_image;
  if (gameName) gameName.textContent = r.game_name;
  if (gameGenre) gameGenre.textContent = r.game_genre;

  // Verdict banner
  const banner = document.getElementById("verdict-banner");
  if (banner) {
    banner.className = `verdict-banner ${r.verdict}`;
    const verdictTitle = banner.querySelector("h2");
    if (verdictTitle) {
      // Typing animation
      typeText(verdictTitle, r.verdict_label, 60);
    }
  }

  // Score bars
  animateScoreBars(r.min_score, r.rec_score, r.verdict);

  // Spec table
  renderSpecTable(r);

  // Bottleneck
  const bottleneckEl = document.getElementById("bottleneck-text");
  if (bottleneckEl) bottleneckEl.textContent = `Weakest component: ${r.bottleneck}`;

  // Upgrade tip
  const tipEl = document.getElementById("upgrade-tip-text");
  if (tipEl) tipEl.textContent = r.upgrade_tip;

  // Settings suggestion
  const settingsEl = document.getElementById("settings-text");
  if (settingsEl) settingsEl.textContent = r.settings_suggestion;
}

function typeText(el, text, speed) {
  el.textContent = "";
  let i = 0;
  const interval = setInterval(() => {
    el.textContent += text[i];
    i++;
    if (i >= text.length) clearInterval(interval);
  }, speed);
}

function animateScoreBars(minScore, recScore, verdict) {
  const colorClass =
    verdict === "RUNS_GREAT" ? "great" : verdict === "RUNS_OK" ? "ok" : verdict === "RUNS_POOR" ? "poor" : "fail";

  const minBar = document.getElementById("min-score-bar");
  const recBar = document.getElementById("rec-score-bar");
  const minLabel = document.getElementById("min-score-label");
  const recLabel = document.getElementById("rec-score-label");

  if (minBar) {
    minBar.className = `score-bar-fill ${colorClass}`;
    setTimeout(() => (minBar.style.width = `${Math.round(minScore * 100)}%`), 300);
  }
  if (recBar) {
    recBar.className = `score-bar-fill ${colorClass}`;
    setTimeout(() => (recBar.style.width = `${Math.round(recScore * 100)}%`), 500);
  }
  if (minLabel) minLabel.textContent = `${Math.round(minScore * 100)}%`;
  if (recLabel) recLabel.textContent = `${Math.round(recScore * 100)}%`;
}

function renderSpecTable(r) {
  const tbody = document.getElementById("spec-tbody");
  if (!tbody) return;

  const specs = [
    { name: "RAM", yours: `${r.device.ram_gb} GB`, min: `${r.min_req.ram_gb} GB`, rec: `${r.rec_req.ram_gb} GB`, pass: r.device.ram_gb >= r.min_req.ram_gb },
    { name: "GPU Tier", yours: GPU_TIERS[r.device.gpu_tier] || `Tier ${r.device.gpu_tier}`, min: `Tier ${r.min_req.gpu_tier}`, rec: `Tier ${r.rec_req.gpu_tier}`, pass: r.device.gpu_tier >= r.min_req.gpu_tier },
    { name: "CPU Tier", yours: CPU_TIERS[r.device.cpu_tier] || `Tier ${r.device.cpu_tier}`, min: `Tier ${r.min_req.cpu_tier}`, rec: `Tier ${r.rec_req.cpu_tier}`, pass: r.device.cpu_tier >= r.min_req.cpu_tier },
    { name: "Storage", yours: `${r.device.storage_gb} GB`, min: `${r.min_req.storage_gb} GB`, rec: `${r.rec_req.storage_gb} GB`, pass: r.device.storage_gb >= r.min_req.storage_gb },
    { name: "OS", yours: r.device.os, min: r.min_req.os.join(", "), rec: r.rec_req.os.join(", "), pass: true },
  ];

  tbody.innerHTML = specs
    .map(
      (s) => `
    <tr>
      <td>${s.name}</td>
      <td class="${s.pass ? "pass" : "fail"}">${s.yours}</td>
      <td>${s.min}</td>
      <td>${s.rec}</td>
    </tr>
  `
    )
    .join("");
}

// ── Games Page (Browse) ───────────────────────────────
let allGames = [];

async function loadGamesPage() {
  try {
    const res = await fetch("/api/games");
    allGames = await res.json();
    renderGameGrid(allGames);
  } catch (err) {
    console.error("Failed to load games:", err);
  }
}

function filterGames(filter) {
  // Update active tab
  document.querySelectorAll(".filter-tab").forEach((t) => t.classList.remove("active"));
  event.target.classList.add("active");

  let filtered = allGames;
  if (filter === "PC") filtered = allGames.filter((g) => g.platform.includes("PC"));
  else if (filter === "Mobile") filtered = allGames.filter((g) => g.platform.includes("Mobile"));
  else if (filter === "LowEnd") filtered = allGames.filter((g) => g.min.gpu_tier <= 1 && g.min.ram_gb <= 4);

  renderGameGrid(filtered);
}

function searchGames() {
  const query = document.getElementById("game-search")?.value.toLowerCase() || "";
  const filtered = allGames.filter(
    (g) => g.name.toLowerCase().includes(query) || g.genre.toLowerCase().includes(query)
  );
  renderGameGrid(filtered);
}

// ── Chat System ───────────────────────────────────────
function openChat() {
  document.getElementById("chat-window")?.classList.add("open");
}

function closeChat() {
  document.getElementById("chat-window")?.classList.remove("open");
}

async function sendChat(message) {
  if (!message || !message.trim()) return;

  const input = document.getElementById("chat-input");
  if (input) input.value = "";

  appendChatMessage("user", message);

  try {
    loadState();
    const res = await fetch("/api/advisor", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message,
        game_id: STATE.selectedGame?.id || null,
        device: STATE.deviceSpecs || null,
      }),
    });
    const data = await res.json();
    appendChatMessage("advisor", data.response);
  } catch (err) {
    appendChatMessage("advisor", "Connection error. Please try again.");
  }
}

function appendChatMessage(role, text) {
  const container = document.getElementById("chat-messages");
  if (!container) return;
  const div = document.createElement("div");
  div.className = `chat-msg ${role}`;
  div.textContent = text;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function handleChatKeypress(e) {
  if (e.key === "Enter") {
    sendChat(document.getElementById("chat-input")?.value);
  }
}

// ── Contact Form ──────────────────────────────────────
async function submitContact(e) {
  e.preventDefault();
  const name = document.getElementById("contact-name")?.value;
  const email = document.getElementById("contact-email")?.value;
  const message = document.getElementById("contact-message")?.value;

  try {
    const res = await fetch("/api/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, message }),
    });
    const data = await res.json();
    alert(data.message);
    e.target.reset();
  } catch (err) {
    alert("Failed to send. Please try again.");
  }
}

// ── FAQ Accordion ─────────────────────────────────────
function initFAQ() {
  document.querySelectorAll(".faq-question").forEach((q) => {
    q.addEventListener("click", () => {
      q.parentElement.classList.toggle("open");
    });
  });
}

// ── Intersection Observer for .reveal ─────────────────
function initRevealObserver() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) e.target.classList.add("visible");
      });
    },
    { threshold: 0.1 }
  );
  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
}

// ── Init on DOM ready ─────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  loadState();
  initRevealObserver();
  initToggleButtons();
  initFAQ();

  // Chat enter key
  const chatInput = document.getElementById("chat-input");
  if (chatInput) chatInput.addEventListener("keypress", handleChatKeypress);
});
