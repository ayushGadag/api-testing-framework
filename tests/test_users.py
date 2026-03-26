import pytest
import allure
from jsonschema import validate
from utils.api_client import get_users, create_user, update_user, delete_user


# 🔥 Schema for validation
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"}
    },
    "required": ["id"]
}


@allure.feature("User API")
@allure.story("GET Users")
def test_get_users():
    with allure.step("Send GET request"):
        response = get_users()

    with allure.step("Validate status code"):
        assert response.status_code == 200

    json_data = response.json()

    with allure.step("Validate response data"):
        assert "users" in json_data
        assert len(json_data["users"]) > 0


@allure.feature("User API")
@allure.story("Create User")
@pytest.mark.parametrize("name, job", [
    ("Ayush", "QA Engineer"),
    ("Rahul", "Developer"),
    ("Aman", "Tester")
])
def test_create_user(name, job):

    payload = {
        "name": name,
        "job": job
    }

    with allure.step("Send POST request"):
        response = create_user(payload)

    with allure.step("Validate status code"):
        assert response.status_code == 201

    json_data = response.json()

    with allure.step("Validate response structure"):
        assert "id" in json_data
        validate(instance=json_data, schema=user_schema)


@allure.feature("User API")
@allure.story("Update User")
def test_update_user():
    user_id = 1

    payload = {
        "name": "Shravan",
        "job": "Developer"
    }

    with allure.step("Send PUT request"):
        response = update_user(user_id, payload)

    with allure.step("Validate status code"):
        assert response.status_code == 200

    json_data = response.json()

    with allure.step("Validate response structure"):
        assert "id" in json_data
        validate(instance=json_data, schema=user_schema)


@allure.feature("User API")
@allure.story("Delete User")
def test_delete_user():
    user_id = 1

    with allure.step("Send DELETE request"):
        response = delete_user(user_id)

    with allure.step("Validate status code"):
        assert response.status_code == 200

    json_data = response.json()

    with allure.step("Validate response structure"):
        assert "id" in json_data
        validate(instance=json_data, schema=user_schema)