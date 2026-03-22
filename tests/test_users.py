from utils.api_client import get_users

def test_get_users():
    response = get_users()

    assert response.status_code == 200
    
    json_data = response.json()
    assert "users" in json_data   