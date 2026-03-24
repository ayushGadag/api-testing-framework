from utils.api_client import get_users, create_user   # ✅ FIXED

def test_get_users():
    response = get_users()

    assert response.status_code == 200
    
    json_data = response.json()
    assert "users" in json_data  


def test_create_user():
    payload = {
        "name": "Ayush",
        "job": "QA Engineer"
    }

    response = create_user(payload)

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["name"] == "Ayush"