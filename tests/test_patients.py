import requests
import pytest
from utils.auth import get_auth_token

BASE_URL = "https://api.healthcare-platform.com"

@pytest.fixture(scope="module")
def auth_token():
    return get_auth_token()

def test_get_patient_details(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/patients/1", headers=headers)
    assert response.status_code == 200
    assert "name" in response.json()

def test_create_patient(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": "John Doe", "age": 30, "condition": "Healthy"}
    response = requests.post(f"{BASE_URL}/patients", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["id"] > 0
