# Job Manager Service - FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid

app = FastAPI(title="Job Manager Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE = {"jobs": []}

class CreateJobRequest(BaseModel):
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

@app.post("/jobs")
def create_job(req: CreateJobRequest):
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
    # TODO: Call Flux server here and update job status/image_url
    return {"job_id": job_id, "status": "pending"}

@app.get("/jobs")
def list_jobs():
    return {"jobs": DATABASE["jobs"]}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    for job in DATABASE["jobs"]:
        if job["job_id"] == job_id:
            return job
    return {"error": "Job not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
