from flask import Flask, render_template, request, jsonify
from datetime import datetime

from reservation import Reservation
from reservations_client import ReservationClient

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/bookings", methods=["GET"])
def get_bookings():
    reservations_client = ReservationClient()

    reservations = reservations_client.get_reservations()

    bookings = [
        reservation.reservation_date
        for reservation in reservations
    ]

    return jsonify([booking.strftime("%Y-%m-%d") for booking in bookings])


@app.route("/api/book", methods=["POST"])
def book():
    data = request.json
    booking_date = datetime.strptime(data["date"], "%Y-%m-%d")
    reservation = Reservation("Test", booking_date)

    reservations_client = ReservationClient()

    reservations_client.book_reservation(reservation)

    app.logger.debug(f"Reservation made for date {booking_date}")

    return jsonify({"message": "Booking successful!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
