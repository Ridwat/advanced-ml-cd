from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_positive_sentiment():
    response = client.post("/predict", json={"text": "I love this product"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_negative_sentiment():
    response = client.post("/predict", json={"text": "This is a bad experience"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"

def test_empty_input():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 400

def test_long_input():
    response = client.post("/predict", json={"text": "a" * 2000})
    assert response.status_code == 400

def test_malicious_input():
    response = client.post("/predict", json={"text": "<script>alert('hack')</script>"})
    assert response.status_code == 200