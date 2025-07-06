import fitz  # PyMuPDF

def extract_text_from_pdf(file) -> str:
    resume_text = ""
    pdf_bytes = file.file.read()
    doc = fitz.open("pdf", pdf_bytes)
    
    for page in doc:
        resume_text += page.get_text()

    return resume_text.strip()
