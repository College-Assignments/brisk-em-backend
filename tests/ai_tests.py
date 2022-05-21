from fastapi.testclient import TestClient
import tests.results.ai as ai_results


def ai_tests(client: TestClient):
    test_ai(client)


def test_ai(client: TestClient):
    response = client.get("/api/ai/topicsearch")
    assert response.status_code == 200
    assert response.json() == ai_results.topicSearch
