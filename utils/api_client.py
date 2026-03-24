import requests

BASE_URL = "https://dummyjson.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

def get_users():
    return requests.get(f"{BASE_URL}/users?page=2", headers=HEADERS)


def create_user(payload): 
    return requests.post(f"{BASE_URL}/users/add", json=payload, headers=HEADERS)


def update_user(user_id, payload): 
    return requests.put(
        f"{BASE_URL}/users/{user_id}",   
        json=payload,                   
        headers=HEADERS                 
    )


def delete_user(user_id):   
    return requests.delete(
        f"{BASE_URL}/users/{user_id}",   
        headers=HEADERS
    )