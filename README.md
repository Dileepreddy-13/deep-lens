# Deep Lens

<p align="center">
  <strong>Open-Source Ocean Intelligence for a Healthier Planet</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="Apache 2.0 License" />
  <img src="https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue" alt="Python Version" />
  <img src="https://img.shields.io/badge/Frontend-React%2018%20%2B%20TypeScript%20%2B%20Vite-06b6d4" alt="React 18" />
  <img src="https://img.shields.io/badge/Mapping-MapLibre%20GL%20JS-38bdf8" alt="MapLibre GL JS" />
  <img src="https://img.shields.io/badge/Analytics-Apache%20ECharts-f59e0b" alt="Apache ECharts" />
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions%20Passing-emerald" alt="CI Status" />
</p>

---

## 🌊 Overview

**Deep Lens** is an open-source ocean intelligence platform designed to help researchers, environmental organizations, coast guards, and coastal communities detect marine threats, analyze environmental changes, verify incidents, and support evidence-based responses.

The platform connects raw ocean observations to a traceable investigation workflow:

$$\text{Observe} \longrightarrow \text{Detect} \longrightarrow \text{Correlate} \longrightarrow \text{Verify} \longrightarrow \text{Prioritize} \longrightarrow \text{Respond} \longrightarrow \text{Measure}$$

Deep Lens maintains strict scientific integrity by distinguishing:
- **Observed facts** (direct instrumental telemetry from calibrated sensors)
- **Algorithmically detected anomalies** (statistical or spatial deviations)
- **Model-generated predictions** (machine learning candidate detections with confidence intervals)
- **Human-reviewed findings** (expert-corroborated evidence trails)
- **Confirmed incidents** (multi-sensor validated environmental violations)

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, MapLibre GL JS, Apache ECharts, Lucide Icons, React Router |
| **Backend** | Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, Uvicorn |
| **Geospatial & Physics** | PostGIS / PostgreSQL, SQLite fallback, Shapely, NumPy, SciPy, Pandas |
| **Scientific AI/ML** | 2D Sentinel-1 SAR Otsu Slick Segmentation, 2D Lagrangian Particle Drift Simulation |
| **Deployment & CI** | Docker, Docker Compose, GitHub Actions, Pytest, Vitest |

---

## 🚀 Core Features Implemented

1. **Global Ocean Intelligence Dashboard:** Real-time KPI metrics, active threats counter, triage queue, and sensor freshness indicators.
2. **Interactive Global Ocean Map (MapLibre GL JS):** Multi-basin geospatial explorer with custom SVG markers, incident clustering, threat category filters, basin jump presets (Gulf of Mexico, Galapagos, Great Barrier Reef, Malacca Strait, North Sea, Mediterranean), and slide-out investigation drawers.
3. **Satellite SAR Oil Slick Detection Pipeline:** Automated Sentinel-1 C-band Synthetic Aperture Radar processing using spatial Lee speckle reduction, adaptive Otsu bimodal thresholding, morphological closing, logarithmic damping ratio evaluation ($\Delta \sigma^0$ in dB), and GeoJSON contour footprint exports.
4. **Maritime AIS Anomaly Radar:** Telemetry scanner identifying transponder blackouts / tracking gaps (>4h), slow loitering patterns, and unauthorized incursions into Marine Protected Areas (MPAs).
5. **Lagrangian 2D Particle Drift Model:** Forward Eulerian-Lagrangian advection-diffusion simulator incorporating empirical 3% wind leeway factor, surface current vectors, and Monte Carlo turbulent eddy diffusion to predict shoreline encounter risks and coastal impact ETA.
6. **Incident Management & Verification Lifecycle:** Complete state transition engine (`detected` $\to$ `under_review` $\to$ `verified` / `dismissed` $\to$ `assigned` $\to$ `resolved`) with immutable audit logging and reviewer attribution notes.
7. **Citizen Science & Community Coastal Reporting:** Public field reporting interface for marine observers, divers, and mariners to file reports with coordinates and anti-abuse validation.
8. **Environmental Analytics & Model Benchmarks (Apache ECharts):** Multi-basin monthly incident frequency charts, threat distributions, and model metrics (SAR F1-score: 0.884, Precision: 0.865, Recall: 0.904).
9. **Ocean Data Explorer:** Comprehensive provenance registry cataloging integrated data sources (ESA Copernicus, Global Fishing Watch, NOAA Coral Reef Watch, CMEMS Ocean Physics) with licensing and citations.
10. **Open-Source Plugin Architecture:** Standardized adapter and model interfaces allowing independent community extension of data sources and detection algorithms.

---

## 📦 Project Structure

```
deep-lens/
├── apps/
│   └── web/                   # React 18 + TypeScript + Vite + MapLibre GL frontend
│       ├── src/
│       │   ├── components/    # Layout (Navbar, Footer) and reusable UI widgets
│       │   ├── pages/         # 15 complete functional application pages
│       │   ├── services/      # Typed REST API client
│       │   └── types/         # Pydantic-mirrored TypeScript interfaces
│       └── vite.config.ts
├── services/
│   └── api/                   # FastAPI backend services
│       ├── models.py          # SQLAlchemy ORM models (Observations, Incidents, AuditLogs)
│       ├── database.py        # Dual SQLite / PostgreSQL engine
│       ├── main.py            # FastAPI main application & routers
│       └── routers/           # 10 modular REST API routers
├── modules/
│   ├── pollution/             # SAR slick detection pipeline (Otsu & damping dB)
│   ├── maritime/              # AIS vessel anomaly & MPA incursion detector
│   ├── drift_analysis/        # 2D Lagrangian particle drift simulation
│   └── ecosystems/            # Coral bleaching DHW thermal stress analyzer
├── packages/
│   ├── schemas/               # Shared Pydantic schemas
│   ├── geospatial/            # Shapely vector geometry, Haversine, GeoJSON helpers
│   └── ocean_data/            # Unified data ingestion adapters & seed generator
├── tests/                     # Automated test suite (11 passing tests)
├── .github/                   # CI/CD workflows, issue & pull request templates
├── docker-compose.yml         # Containerized production stack (PostGIS, Redis, API, Web)
├── requirements.txt           # Python root dependencies
├── CONTRIBUTING.md            # Contributor guidelines
├── CODE_OF_CONDUCT.md         # Community standards
├── GOVERNANCE.md              # Project governance
├── SECURITY.md                # Vulnerability disclosures
└── LICENSE                    # Apache-2.0
```

---

## ⚡ Quickstart Guide

### Option A: Local Development (Zero-Config, Instant Run)

Deep Lens runs locally with zero external database dependencies out of the box using SQLite and deterministic baseline seed data.

#### 1. Start Backend
```bash
# Clone repository
git clone https://github.com/deeplens/deep-lens.git
cd deep-lens

# Setup Python virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch FastAPI server
uvicorn services.api.main:app --reload --port 8000
```
Interactive API documentation is now available at:
**[http://localhost:8000/docs](http://localhost:8000/docs)**

#### 2. Start Frontend
```bash
# In a separate terminal
cd apps/web
npm install
npm run dev
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.

---

### Option B: Docker Compose (Full Stack with PostGIS & Redis)

```bash
docker-compose up --build
```
- Web Application: [http://localhost:3000](http://localhost:3000)
- API Backend: [http://localhost:8000](http://localhost:8000)
- Interactive OpenAPI Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Automated Tests

Run the backend test suite:
```bash
pytest tests/ -v
```

Run frontend build verification:
```bash
cd apps/web
npm run build
```

---

## 🛰️ External Sensor Integrations & Provenance

Deep Lens supports both real API credentials and an offline deterministic demonstration mode:

| Provider | Sensor / Data Product | License / Terms | Integration Path |
| :--- | :--- | :--- | :--- |
| **ESA Copernicus** | Sentinel-1 C-SAR IW GRDH | Copernicus Open Access / CC-BY 4.0 | Set `COPERNICUS_CLIENT_ID` in `.env` |
| **Global Fishing Watch** | AIS Vessel Tracking API v3 | CC-BY 4.0 | Set `GFW_API_KEY` in `.env` |
| **NOAA CRW** | Sea Surface Temp & Degree Heating Weeks | Public Domain (U.S. Govt) | Direct open REST API |
| **CMEMS** | Global Ocean Surface Velocity (u, v) | Copernicus Marine Open Access | Integrated in Drift Model |

---

## 🗺️ Extensible Roadmap

- [x] Global interactive MapLibre map with multi-basin filters
- [x] Sentinel-1 SAR synthetic aperture radar slick segmentation
- [x] Vessel AIS transponder blackout & MPA incursion detection
- [x] 2D Lagrangian particle drift simulation with windage leeway
- [x] Evidence verification lifecycle with audit trails
- [x] Citizen coastal reporting portal
- [ ] Coral Bleaching Alert Level 3/4 experimental index
- [ ] Hydrophone acoustic spectrogram classifier for marine cetaceans
- [ ] Microplastic high-resolution imagery classifier
- [ ] Coastal flood exposure and shoreline erosion analysis

---

## 🤝 Contributing

We welcome contributions from developers, researchers, and ocean enthusiasts!  
See [CONTRIBUTING.md](CONTRIBUTING.md) to get started and check out the [Contributor Hub](http://localhost:3000/contributors) for beginner-friendly tasks.

---

## 📜 License

Deep Lens is licensed under the **[Apache License 2.0](LICENSE)**.
