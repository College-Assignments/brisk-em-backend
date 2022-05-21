from fastapi.testclient import TestClient
from main import app
from tests.results.ai import topicSearch


client = TestClient(app)


def test_search_topic():
    response = client.get("/api/ai/topicsearch?topic=himalayas")
    assert response.status_code == 200
    assert response.json().sort() == topicSearch.sort()
