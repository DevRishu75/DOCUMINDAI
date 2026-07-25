from fastapi import FastAPI
from app.api.routes.upload import upload_router
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
# print(upload_router.routes)
# for route in app.routes:
#     print(route.path, route.methods)
app.include_router(upload_router)