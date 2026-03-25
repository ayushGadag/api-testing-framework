from utils.api_client import get_users, create_user, update_user, delete_user


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


def test_update_user():
    user_id = 1   # existing user

    payload = {
        "name": "Shravan",
        "job": "Developer"
    }

    response = update_user(user_id, payload)

    assert response.status_code == 200

    json_data = response.json()

    assert json_data["name"] == "Shravan"
    assert "id" in json_data   # strong validation


def test_delete_user():
    user_id = 1

    response = delete_user(user_id)

    assert response.status_code == 201

    json_data = response.json()

    assert "id" in json_data   # confirm response contains id
    