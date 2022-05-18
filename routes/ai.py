from fastapi import APIRouter

router = APIRouter()


@router.post("/ai")
async def generate_mcq(topic: str, topic_title: str):
    return "OK"
