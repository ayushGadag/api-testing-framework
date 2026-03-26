import pytest
from jsonschema import validate
from utils.api_client import get_users, create_user, update_user, delete_user


#  Schema for validation
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"}
    },
    "required": ["id"]
}


def test_get_users():
    response = get_users()

    assert response.status_code == 200
    
    json_data = response.json()

    assert "users" in json_data
    assert len(json_data["users"]) > 0   # bonus validation


#  Data-driven testing (multiple inputs)
@pytest.mark.parametrize("name, job", [
    ("Ayush", "QA Engineer"),
    ("Rahul", "Developer"),
    ("shravani", "Tester")
])
def test_create_user(name, job):

    payload = {
        "name": name,
        "job": job
    }

    response = create_user(payload)

    assert response.status_code == 201

    json_data = response.json()

    assert "id" in json_data

    # Schema validation
    validate(instance=json_data, schema=user_schema)


def test_update_user():
    user_id = 1

    payload = {
        "name": "Shravan",
        "job": "Developer"
    }

    response = update_user(user_id, payload)

    assert response.status_code == 200

    json_data = response.json()

    assert "id" in json_data

    # Schema validation
    validate(instance=json_data, schema=user_schema)


def test_delete_user():
    user_id = 1

    response = delete_user(user_id)

    assert response.status_code == 200

    json_data = response.json()

    assert "id" in json_data

    # Schema validation
    validate(instance=json_data, schema=user_schema)