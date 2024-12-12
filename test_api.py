import requests

BASE_URL = "http://localhost:5000/items"

def test_get_items():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_add_item():
    response = requests.post(BASE_URL, json={"name": "Item 1"})
    assert response.status_code == 201

def test_get_item():
    response = requests.get(f"{BASE_URL}/0")
    assert response.status_code == 200

def test_update_item():
    response = requests.put(f"{BASE_URL}/0", json={"name": "Updated Item"})
    assert response.status_code == 200

def test_delete_item():
    response = requests.delete(f"{BASE_URL}/0")
    assert response.status_code == 200

def test_get_nonexistent_item():
    response = requests.get(f"{BASE_URL}/999")
    assert response.status_code == 404

def test_update_nonexistent_item():
    response = requests.put(f"{BASE_URL}/999", json={"name": "Nonexistent"})
    assert response.status_code == 404

def test_delete_nonexistent_item():
    response = requests.delete(f"{BASE_URL}/999")
    assert response.status_code == 404

def test_add_multiple_items():
    for i in range(5):
        response = requests.post(BASE_URL, json={"name": f"Item {i}"})
        assert response.status_code == 201
def test_get_all_items():
    response = requests.get(BASE_URL)
    assert len(response.json()['items']) == 5

if __name__ == "__main__":
    test_get_items()
    test_add_item()
    test_get_item()
    test_update_item()
    test_delete_item()
    test_get_nonexistent_item()
    test_update_nonexistent_item()
    test_delete_nonexistent_item()
    test_add_multiple_items()
    test_get_all_items()
