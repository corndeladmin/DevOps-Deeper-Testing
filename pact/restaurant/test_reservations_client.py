from dotenv import load_dotenv, find_dotenv
from reservations_client import ReservationClient
import requests

def test_get_reservations(monkeypatch):
    # ARRANGE
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', stub)
    reservation_client = ReservationClient()

    # ACT
    reservations = reservation_client.get_reservations()

    # ASSERT
    assert len(reservations) == 1
    test_reservation = reservations[0]
    assert test_reservation.user_id == "test_user_id"

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data
    
    def raise_for_status(self):
        pass

    @property
    def status_code(self):
        return 200

def stub(url, params={}):
    if url == f'http://fake-reservations:5000/reservations':
        fake_response_data = [{
            "user_id": "test_user_id",
            "reservation_date": "2026-12-25"
        }]
        return StubResponse(fake_response_data)
    elif url == f'http://fake-reservations:5000/reserve':
        return StubResponse({})

    raise Exception(f'Test did not expect URL "{url}"')