import os
import datetime
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

from db import init_database
from routes.auth import router as auth_router
from routes.cases import router as cases_router
from routes.files import router as files_router
from routes.logs import router as logs_router
from routes.blockchain import router as blockchain_router
from routes.persons import router as persons_router

load_dotenv()

PORT = int(os.getenv("PORT", 5000))


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing Database...")
    try:
        init_database()
    except Exception as e:
        print(f"[DB WARNING] Startup initialization warning: {e}")
    yield


app = FastAPI(title="SI-PALMS Python Backend", version="1.0.0", lifespan=lifespan)

# Enable CORS for all origins (matching Express cors())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(auth_router)
app.include_router(cases_router)
app.include_router(files_router)
app.include_router(logs_router)
app.include_router(blockchain_router)
app.include_router(persons_router)


@app.get("/api/health")
def health_check():
    return {
        "status": "OK",
        "message": "SI-PALMS Python Backend Operational",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }


# Serve Frontend Static Assets and SPA fallback when built
dist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dist"))
if os.path.exists(dist_dir):
    assets_dir = os.path.join(dist_dir, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="API endpoint not found")
        file_path = os.path.join(dist_dir, full_path)
        if full_path and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(dist_dir, "index.html"))


if __name__ == "__main__":
    print("===============================================")
    print(f"  SI-PALMS Python Backend Running on Port {PORT}")
    print(f"  Health Check: http://localhost:{PORT}/api/health")
    print("===============================================")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True, app_dir=os.path.dirname(__file__))
