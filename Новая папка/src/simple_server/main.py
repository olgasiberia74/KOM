from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .interfaces.api import router

app = FastAPI(
    title="Simple Full-Stack Python App",
    description="A minimal full-stack app with FastAPI backend and static frontend",
    version="0.1.0"
)

app.include_router(router)

static_dir = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def root():
    return FileResponse(static_dir / "index.html")


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()