from fastapi.testclient import TestClient

# Test the Get user endpoint without auth - GET /api/v1/user
def test_get_user_auth_required(client: TestClient):
    response = client.get("/api/v1/user")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data

# Test the Delete user endpoint without auth - DELETE /api/v1/user
def test_delete_user_auth_required(client: TestClient):
    response = client.delete("/api/v1/user")
    assert response.status_code == 403
    response_data = response.json()
    assert "detail" in response_data