from fastapi import FastAPI
from app.routers import users, cases

app = FastAPI(
    title="Skin Diagnosis API",
    version="1.0.0",
    description="AI-powered Skin Diagnosis API for case management and doctor/patient workflows.",
)

app.include_router(users.router)
app.include_router(cases.router)


@app.get("/")
def root() -> dict:
    return {"message": "Skin Diagnosis API is running"}
