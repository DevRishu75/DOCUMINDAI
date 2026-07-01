from fastapi import FastAPI

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

