from fastapi import FastAPI
from app.routes.resume_routes import router as resume_router

app = FastAPI(
    title="AI-Powered Resume Analyzer",
    description="Upload resumes and get feedback using OpenAI.",
    version="1.0.0"
)

app.include_router(resume_router, prefix="/resume", tags=["Resume Analysis"])
