from fastapi.testclient import TestClient

from tests.ai_tests import ai_tests

from main import app

client = TestClient(app)

ai_tests(client)
