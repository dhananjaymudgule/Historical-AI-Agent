# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import chat
from app.core.config import settings


# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION
)


# CORS Middleware (Allows frontend apps to access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routers
app.include_router(chat.router, prefix="/chat", tags=["chat"])

# Root endpoint
@app.get("/", tags=["Health Check"])
def root():
    return {"message": f"Welcome to Historical Monuments!", "status": "OK"}


# Run app only if executed directly (not imported)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, reload=True)


