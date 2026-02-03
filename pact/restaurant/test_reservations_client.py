from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from reservation import Reservation
from reservations_client import ReservationClient
import requests

TEST_DATE = "2026-12-25"

def test_get_reservations(monkeypatch):
    # ARRANGE
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', get_stub)
    reservation_client = ReservationClient()

    # ACT
    reservations = reservation_client.get_reservations()

    # ASSERT
    assert len(reservations) == 1
    test_reservation = reservations[0]
    assert test_reservation.user_id == "test_user_id"

def test_book_reservations(monkeypatch):
    # ARRANGE
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    # This replaces any call to requests.post with our own function
    monkeypatch.setattr(requests, 'post', post_stub)
    reservation_client = ReservationClient()
    reservation = Reservation("Test User", datetime.strptime(TEST_DATE, "%Y-%m-%d"))

    # ACT
    reservation_client.book_reservation(reservation)

    # ASSERT
    pass # Nothing to check - ensure no errors

class StubResponse():
    def __init__(self, fake_response_data = {}):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data
    
    def raise_for_status(self):
        pass

    @property
    def status_code(self):
        return 200

def get_stub(url, params={}):
    if url == f'http://fake-reservations:5000/reservations':
        fake_response_data = [{
            "user_id": "test_user_id",
            "reservation_date": TEST_DATE
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Test did not expect URL "{url}"')

def post_stub(url, data={}, headers={}):
    if url == f'http://fake-reservations:5000/reserve':
        return StubResponse()

    raise Exception(f'Test did not expect URL "{url}"')