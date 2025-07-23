# vLLM Server - FastAPI with Virtual DB Logic
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI(title="vLLM Server")

# Simulated in-memory database
DATABASE = {
    "jobs": []
}

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 128
    user_id: Optional[str] = None

class JobRecord(BaseModel):
    job_id: str
    user_id: Optional[str]
    prompt: str
    max_tokens: int
    status: str
    result: Optional[str] = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: GenerateRequest):
    # Create a new job record
    job_id = str(uuid.uuid4())
    job = JobRecord(
        job_id=job_id,
        user_id=req.user_id,
        prompt=req.prompt,
        max_tokens=req.max_tokens,
        status="pending",
        result=None
    )
    DATABASE["jobs"].append(job.dict())
    # Simulate LLM output
    output = f"[LLM output for: {req.prompt}]"
    # Update job record
    job.status = "completed"
    job.result = output
    # Update in DB
    for j in DATABASE["jobs"]:
        if j["job_id"] == job_id:
            j["status"] = job.status
            j["result"] = job.result
    return {"job_id": job_id, "output": output}

@app.get("/jobs")
def list_jobs():
    return {"jobs": DATABASE["jobs"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
