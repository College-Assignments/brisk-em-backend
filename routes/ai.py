from http.client import HTTPException
from fastapi import APIRouter

from qgen.quiz import generate_custom_qa, generate_qa
from qgen.quiz import find_topic

router = APIRouter()


@router.get("/topicsearch")
async def search_topic(topic: str):
    return find_topic(topic)


@router.post("/generateqa")
async def gen_qa(article: str):
    generated_json = generate_qa(article)
    return generated_json


@router.post("/generatecustomqa")
async def gen_custom_qa(article: str):
    generated_json = generate_custom_qa(article)
    if generated_json:
        return generated_json
    else:
        return HTTPException(status_code=404, detail="Empty not allowed")
