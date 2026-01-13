from flask import Flask, json, render_template, request, jsonify
from datetime import datetime
import os

import requests

RESERVATIONS_API_BASE_URL = os.getenv("RESERVATIONS_HOST")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/bookings", methods=["GET"])
def get_bookings():
    reservations_response = requests.get(f"{RESERVATIONS_API_BASE_URL}/reservations")
    reservations_response.raise_for_status()
    reservations_json = reservations_response.json()
    bookings = [
        datetime.strptime(reservation["reservation_date"], "%Y-%m-%d")
        for reservation in reservations_json
    ]

    return jsonify([booking.strftime("%Y-%m-%d") for booking in bookings])


@app.route("/api/book", methods=["POST"])
def book():
    data = request.json
    booking_date = datetime.strptime(data["date"], "%Y-%m-%d")
    request_object = {
        "date": data["date"],
        "user_id": "Test"
    }
    request_body = json.dumps(request_object)
    headers = { 'Content-type': 'application/json' }
    response = requests.post(f"{RESERVATIONS_API_BASE_URL}/reserve", data = request_body, headers = headers)

    response.raise_for_status()

    app.logger.debug(f"Reservation made for date {booking_date}")

    return jsonify({"message": "Booking successful!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
