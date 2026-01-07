from datetime import datetime

class Reservation:
    def __init__(self, user_id: str, reservation_date: datetime):
        self.user_id = user_id
        self.reservation_date = reservation_date

    def to_json(self) -> dict[str, str]:
        return {
            "user_id": self.user_id,
            "reservation_date": self.reservation_date.strftime("%d/%m/%y")
        }