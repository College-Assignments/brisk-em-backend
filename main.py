import uvicorn
from fastapi import FastAPI
from routes.ai import router as ai_router


def run_app() -> FastAPI:
    application = FastAPI()
    print("Starting application...")

    # Routes
    application.include_router(ai_router, prefix="/api")

    return application


if __name__ == "__main__":
    uvicorn.run("main:run_app", host="127.0.0.1", port=3000, log_level="info")
