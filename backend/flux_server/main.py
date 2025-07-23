# Flux Server - FastAPI Boilerplate
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Flux Server")

# Simulated in-memory database
DATABASE = {
    "jobs": []
}

class GenerateRequest(BaseModel):
    prompt: str
    style: str = "portrait"
    seed: int = None

class JobRecord(BaseModel):
    job_id: str
    prompt: str
    style: str
    seed: int = None
    status: str
    image_url: str = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: GenerateRequest):
    job_id = str(uuid.uuid4())
    job = JobRecord(
        job_id=job_id,
        prompt=req.prompt,
        style=req.style,
        seed=req.seed,
        status="pending",
        image_url=None
    )
    DATABASE["jobs"].append(job.dict())
    # Simulate image generation
    image_url = f"/fake/path/{req.prompt}.png"
    job.status = "completed"
    job.image_url = image_url
    # Update in DB
    for j in DATABASE["jobs"]:
        if j["job_id"] == job_id:
            j["status"] = job.status
            j["image_url"] = job.image_url
    return {"job_id": job_id, "image_url": image_url}

@app.get("/jobs")
def list_jobs():
    return {"jobs": DATABASE["jobs"]}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    for job in DATABASE["jobs"]:
        if job["job_id"] == job_id:
            return job
    return {"error": "Job not found"}

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
