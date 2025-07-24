# Backend Setup - FluxPortrait

This backend consists of two main components:

## 1. vLLM Server
- **Purpose:** Fast LLM inference
- **Tech:** FastAPI, vLLM
- **Endpoints:**
  - `GET /health` — Health check
  - `POST /generate` — Generate LLM output
- **Run:**
  ```bash
  cd vllm_server
  pip install -r requirements.txt
  python main.py
  # Or: uvicorn main:app --host 0.0.0.0 --port 8001
  ```

## 2. Flux Server
- **Purpose:** Image generation (Flux/SDXL)
- **Tech:** FastAPI
- **Endpoints:**
  - `GET /health` — Health check
  - `POST /generate` — Generate image
- **Run:**
  ```bash
  cd flux_server
  pip install -r requirements.txt
  python main.py
  # Or: uvicorn main:app --host 0.0.0.0 --port 8002
  ```

## Development Notes
- Each server is independent and exposes a REST API.
- Add your model loading and inference logic in `main.py` for each server.
- See requirements.txt for dependencies. Add your model-specific packages as needed.

## Next Steps
- Integrate vLLM and Flux model code
- Add authentication, logging, and error handling as needed
- Containerize with Docker for production

---
Made with ❤️ for APEX Portrait Generator
