from fastapi import FastAPI
from app.api.routes.upload import upload_router
from app.api.routes.document import document_router
from app.api.routes.auth_router import auth_router
from app.db.init_db import init_db
app = FastAPI(
    title = "DOCUMIND AI",
    description = "AI powered Docuement Intelligence Engine",
    version = '1.0.0'
)
init_db()

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
app.include_router(document_router)
app.include_router(auth_router)