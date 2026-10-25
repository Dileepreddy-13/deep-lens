from fastapi import FastAPI
from services.api.routers import incidents

app = FastAPI(title="Deep Lens API", version="1.0.0")

app.include_router(incidents.router)

@app.get("/")
def root():
    return {"message": "Deep Lens API is running"}
