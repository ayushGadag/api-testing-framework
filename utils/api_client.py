import requests

BASE_URL = "https://dummyjson.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def get_users():
    return requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)

def create_user(payload):   # ✅ FIXED (added parameter)
    return requests.post(f"{BASE_URL}/users/add", json=payload, headers=HEADERS)