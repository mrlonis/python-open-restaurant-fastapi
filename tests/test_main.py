from fastapi.testclient import TestClient


def test_root_path(test_client_module: TestClient):
    client = test_client_module
    response = client.get("")
    assert response.status_code == 200
    response_json: dict[str, str] = response.json()
    result = response_json.get("Hello")
    assert result == "World"
