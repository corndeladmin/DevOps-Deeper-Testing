from flask import Flask, render_template, request, jsonify
from datetime import datetime

from pact.reservations.reservation import Reservation

app = Flask(__name__)

MAX_BOOKINGS_PER_DAY = 3
frequent_user_id = "0f06e8c2-7561-42b1-bdff-1fb352f01843"
todays_date = datetime.now()
default_reservations = [
    Reservation(frequent_user_id, todays_date),
    Reservation(frequent_user_id, todays_date),
    Reservation(frequent_user_id, todays_date),
]

reservations = [*default_reservations]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reservations", methods=["GET"])
def get_bookings():
    return jsonify([reservation.to_json() for reservation in reservations])


@app.route("/reserve", methods=["POST"])
def book():
    data = request.json
    new_reservation_date = datetime.strptime(data["date"], "%d/%m/%y")
    user_id = data["user_id"]

    reservations_on_date = [
        reservation
        for reservation in reservations
        if reservation.reservation_date.date() == new_reservation_date.date()
    ]

    if (len(reservations_on_date) < MAX_BOOKINGS_PER_DAY):
        return jsonify({"message": "Booking successful!"}), 200
    else:
        return jsonify({"message": "Date already fully booked!"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=8400)
