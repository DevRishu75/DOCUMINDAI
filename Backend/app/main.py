from fastapi import FastAPI
from app.api.routes.upload import router as upload_router
app = FastAPI(
    title = "DocuMind AI",
    description = "Document Intelligence platform for AI - Powered document analysis.",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to DocuMind AI Backend",
        "status": "Running"
    }
app.include_router(upload_router)
