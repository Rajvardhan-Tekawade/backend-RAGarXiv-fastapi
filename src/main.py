# backend/src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.arxiv_routes import router as arxiv_router

app = FastAPI(title="ArXiv Research Paper API", description="Fetch research papers from ArXiv", version="1.0.0")

# CORS middleware to allow frontend requests from other origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust this for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the ArXiv router
app.include_router(arxiv_router, prefix="/api", tags=["arxiv"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI backend! Use /docs for API documentation."}
