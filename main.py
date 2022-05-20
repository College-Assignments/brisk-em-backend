import uvicorn
from fastapi import FastAPI
from routes.ai import router as ai_router
from fastapi.middleware.cors import CORSMiddleware


def run_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(ai_router, prefix="/api/ai")

    return app


if __name__ == "__main__":
    uvicorn.run(run_app, host="127.0.0.1", port=3000, log_level="info")
