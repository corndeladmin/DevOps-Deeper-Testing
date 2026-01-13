from datetime import datetime

from reservation import Reservation


def test_reservation_serialisation():
    # Arrange
    test_date = datetime(2025, 12, 5)
    test_user_id = "Test User ID"

    # Act
    reservation = Reservation(test_user_id, test_date)
    reservation_json = reservation.to_json()

    # Assert
    assert reservation_json["reservation_date"] == "2025-12-05"