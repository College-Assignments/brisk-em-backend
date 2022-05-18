from ai import router as ai_router
from fastapi import FastAPI

app = FastAPI()


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ai_router, prefix="/ai")
    return application

@app.get("/")
def root():
    return {"200": "Welcome to BriskES"}
