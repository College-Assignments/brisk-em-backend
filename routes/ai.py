from http.client import HTTPException
from fastapi import APIRouter
from pydantic import BaseModel

from generator.quiz import generate_custom_qa, generate_qa
from generator.quiz import find_topic

router = APIRouter()

# -----------------------------------------------------------------------------
# ---------------------------------- TYPES ------------------------------------
# -----------------------------------------------------------------------------


class Article(BaseModel):
    article: str


# -----------------------------------------------------------------------------
# ---------------------------------- ROUTES -----------------------------------
# -----------------------------------------------------------------------------

# 1
@router.get("/topicsearch")
async def search_topic(topic: str):
    return find_topic(topic)


# 2
@router.post("/generateqa")
async def gen_qa(article: str):
    generated_json = generate_qa(article)
    return generated_json


# 3
@router.post("/generatecustomqa")
async def gen_custom_qa(request: Article):
    try:
        if request.article == "":
            return ValueError("Empty not allowed")

        generated_json = generate_custom_qa(request.article)
        return generated_json
    except (HTTPException):
        print(request)
        return HTTPException(status_code=404, detail="Empty not allowed")
