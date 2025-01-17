# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Football Player Performance Predictor" in response.data

def test_predict(client):
    payload = {"features": [25, 80, 50, 3, 65, 70, 60, 75, 1, 2, 2, 3, 0, 0, 1, 0, 0, 0]}
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    assert "prediction" in response.get_json()