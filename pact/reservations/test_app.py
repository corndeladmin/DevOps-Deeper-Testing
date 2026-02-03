from dotenv import load_dotenv, find_dotenv
import app
import pytest

TEST_DATE = "2026-12-25"

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_get_reservations(client):
    # Arrange
    pass # Do nothing

    # Act
    response = client.get("/reservations")
    reservations_json = response.json

    # Assert
    assert len(reservations_json) == 3


def test_book_reservation(client):
    # Arrange
    payload = {
        "user_id": "Test User",
        "reservation_date": TEST_DATE
    }

    # Act
    response = client.post("/reserve", json=payload)

    # Assert
    assert response.status_code == 200
