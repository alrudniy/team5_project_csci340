from fastapi.testclient import TestClient

# Test the Get user endpoint without auth - GET /api/v1/user
def test_get_user_auth_required(client: TestClient):
    response = client.get("/api/v1/user")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data

 def test_get_user(client: TestClient, create_test_user_auth_header):
    response = client.get("/api/v1/user", headers=create_test_user_auth_header)
    assert response.status_code == 200, response.text
    response_data = response.json()
    assert "data" in response_data
    user_data = response_data["data"]["user"]
    assert "buckets" in response_data["data"]
    buckets_data = response_data["data"]["buckets"]
    assert "id" in user_data
    assert "email" in user_data
    assert "created_at" in user_data
    assert isinstance(buckets_data, list)
