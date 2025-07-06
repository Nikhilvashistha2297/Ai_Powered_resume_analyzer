from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_parser import extract_text_from_pdf
from app.services.ai_analyzer import analyze_resume

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file)

    # Analyze text using OpenAI (dummy function for now)
    analysis = analyze_resume(resume_text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }
