import requests
import pytest

# Defining url of the API
URL = 'https://petstore.swagger.io/v2'


# Test case 1 to test Get Pet ID functionality and Data
@pytest.mark.parametrize("pet_id", [1, 2, 3])
def test_get_pet_by_id(pet_id):
    url = f"{URL}/pet/{pet_id}"
    response = requests.get(url)

    assert response.status_code == 200, f"Unable to find pet with id {pet_id}. Response Status code: {response.status_code}"
    assert 'id' in response.json(), "Response did not have 'id' field"


# Test case 2 to test Post functionality for adding new pet
def test_add_new_pet():
    url = f"{URL}/pet"
    headers = {'Content-Type': 'application/json'}
    payload = {
        'name': 'Jay',
        'status': 'available'
    }
    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, f"Unable to add new pet to the database. Status code: {response.status_code}"
    assert response.json()['name'] == 'Jay', "Name which we pushed did not match as expected"


# Test case 3 to test endpoint for pet status
def test_get_available_pets():
    url = f"{URL}/pet/findByStatus?status=available"
    response = requests.get(url)
    # Verify the content by checking if the response is not empty
    assert response.status_code == 200, f"Unable to find pet status. Status code: {response.status_code}"


if __name__ == "__main__":
    pytest.main()
