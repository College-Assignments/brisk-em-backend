from fastapi import APIRouter

router = APIRouter()


@router.post("ai")
async def generate_mcq(topic: str, topic_title: str):
    print(topic, "\n\n", topic_title)
    return "OK"
