from fastapi import FastAPI

app = FastAPI(
    title = "DOCUMIND AI",
    description = "AI powered Docuement Intelligence Engine",
    version = '1.0.0'
)

@app.get("/")
def root():
    return{
        "message": "Welcome to DOCUMIND AI ",
        "Success": 200
    }
