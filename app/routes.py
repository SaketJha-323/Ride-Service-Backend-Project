from flask import Blueprint, request, jsonify
from app.models import Ride, Rider, Driver, db
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/create_ride', methods=['POST'])
def create_ride():
    data = request.json
    ride = Ride(
        rider_id=data['rider_id'],
        pickup_lat=data['pickup_lat'],
        pickup_lng=data['pickup_lng'],
        drop_lat=data['drop_lat'],
        drop_lng=data['drop_lng'],
    )
    db.session.add(ride)
    db.session.commit()
    return jsonify({"ride_id": ride.id, "status": ride.status})
