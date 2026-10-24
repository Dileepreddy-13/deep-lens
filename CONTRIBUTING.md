# Contributing to Deep Lens

Thank you for your interest in contributing to Deep Lens! This open-source platform is designed to unite geospatial developers, AI/ML engineers, marine scientists, and conservationists.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/<your-username>/deep-lens.git
   cd deep-lens
   ```
3. **Set up the Python backend**:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```
4. **Set up the React web application**:
   ```bash
   cd apps/web
   npm install
   ```

## Running the Application Locally

1. **Start the FastAPI backend**:
   ```bash
   # From repository root
   uvicorn services.api.main:app --reload --port 8000
   ```
   Open [http://localhost:8000/docs](http://localhost:8000/docs) to test the interactive OpenAPI Swagger UI.

2. **Start the Vite dev server**:
   ```bash
   cd apps/web
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000) to view the Deep Lens interface.

## Running Tests

- **Backend tests**:
  ```bash
  pytest tests/ -v
  ```
- **Frontend build test**:
  ```bash
  cd apps/web
  npm run build
  ```

## Writing Ingestion Adapters

All ocean data adapters must inherit from `BaseDataIngestionAdapter` in `packages/ocean_data/base_adapter.py`.

```python
from packages.ocean_data.base_adapter import BaseDataIngestionAdapter
from packages.schemas.observation import ObservationBase, ObservationType

class MyAdapter(BaseDataIngestionAdapter):
    def fetch_raw_data(self, **kwargs):
        # Fetch from remote API or local file
        pass

    def normalize_record(self, raw_record: dict) -> ObservationBase:
        # Map to common ObservationBase schema
        pass
```

## Pull Request Guidelines

1. Create a feature branch: `git checkout -b feature/my-new-adapter`.
2. Ensure tests pass before pushing: `pytest tests/` and `npm run build`.
3. Adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).
4. Clearly declare whether changes involve simulated data or live provider APIs.
