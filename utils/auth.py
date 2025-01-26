import requests

BASE_URL = "https://api.healthcare-platform.com"

def get_auth_token():
    payload = {"username": "test_user", "password": "secure_password"}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    response.raise_for_status()
    return response.json().get("token")
