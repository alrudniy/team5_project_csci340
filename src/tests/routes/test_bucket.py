from fastapi.testclient import TestClient

# Test the Bucket creation endpoint without auth - POST /api/v1/bucket
def test_create_bucket_auth_required(client: TestClient):
    response = client.post("/api/v1/bucket")
    assert response.status_code == 403  # Forbidden
    response_data = response.json()
    assert "detail" in response_data

# Test the Bucket update endpoint without auth - PUT /api/v1/bucket/{bucket_id}

def test_update_bucket_auth_required(client: TestClient):