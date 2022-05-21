# Tests using pytest library
from fastapi.testclient import TestClient
from main import app
from tests.results.ai import topicSearch
from tests.requests.ai import customQA


client = TestClient(app)


def test_search_topic():
    response = client.get("/api/ai/topicsearch?topic=himalayas")
    assert response.status_code == 200
    assert response.json().sort() == topicSearch.sort()


def test_gen_qa():
    response = client.post("/api/ai/generateqa?article=Great Himalayas")
    assert response.status_code == 200
    assert response.json()


def test_gen_custom_qa():
    response = client.post(f"/api/ai/generatecustomqa?article={customQA}")
    assert response.status_code == 200
    assert response.json()
