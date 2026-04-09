from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import router as sample_router
from app.api.survey import router as survey_router
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title="Python UV Server",
        description="A minimal clean-architecture Python server with FastAPI, Uvicorn, and Swagger.",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.include_router(sample_router, prefix=settings.api_prefix)
    app.include_router(survey_router, prefix=settings.api_prefix)
    app.mount("/", StaticFiles(directory="../static", html=True), name="static")
    return app


app = create_app()
