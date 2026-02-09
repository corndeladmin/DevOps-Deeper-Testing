from datetime import datetime
import json
import requests
import os

from reservation import Reservation


class ReservationsClient:
    def __init__(self, reservations_host_url = None):
        if (reservations_host_url is not None):
            self.reservations_host_url = reservations_host_url
        else:
            self.reservations_host_url = os.getenv("RESERVATIONS_HOST")

    def get_reservations(self) -> list[Reservation]:
        reservations_response = requests.get(
            f"{self.reservations_host_url}/reservations"
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
            f"{self.reservations_host_url}/reserve",
            data=request_body,
            headers=headers,
        )

        response.raise_for_status()
