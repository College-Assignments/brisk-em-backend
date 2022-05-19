from fastapi import APIRouter

from qgen.quiz import generate_mcq
from qgen.quiz import find_topic

router = APIRouter()


@router.get("/topicsearch")
async def search_topic(topic: str):
    return find_topic(topic)


@router.post("/generatemcq")
async def gen_mcq(article: str):
    generated_json = generate_mcq(article)
    return generated_json
