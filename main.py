from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"200": "Welcome to BriskES"}