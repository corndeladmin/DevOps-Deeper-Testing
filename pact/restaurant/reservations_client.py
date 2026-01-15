from datetime import datetime
import json
import requests
import os

from reservation import Reservation


class ReservationClient:
    def __init__(self):
        self.RESERVATIONS_API_BASE_URL = os.getenv("RESERVATIONS_HOST")

    def get_reservations(self) -> list[Reservation]:
        reservations_response = requests.get(
            f"{self.RESERVATIONS_API_BASE_URL}/reservations"
        )
        reservations_response.raise_for_status()
        reservations_json = reservations_response.json()

        return [
            Reservation(
                reservation_json["user_id"],
                datetime.strptime(reservation_json["reservation_date"], "%Y-%m-%d"),
            )
            for reservation_json in reservations_json
        ]

    def book_reservation(self, reservation: Reservation):
        request_body = json.dumps(reservation.to_json())
        headers = {"Content-type": "application/json"}
        response = requests.post(
            f"{self.RESERVATIONS_API_BASE_URL}/reserve",
            data=request_body,
            headers=headers,
        )

        response.raise_for_status()
