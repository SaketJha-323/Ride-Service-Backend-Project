from datetime import datetime
from app import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    status = db.Column(db.String(20), default='available')
    last_completed = db.Column(db.DateTime)
    cancelled_count = db.Column(db.Integer, default=0)

class Rider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=True)
    status = db.Column(db.String(50), default='create_ride')
    pickup_lat = db.Column(db.Float)
    pickup_lng = db.Column(db.Float)
    drop_lat = db.Column(db.Float)
    drop_lng = db.Column(db.Float)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    driver_assigned_at = db.Column(db.DateTime)
    driver_arrived_at = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    fare = db.Column(db.Float)

class PricingConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True)
    value = db.Column(db.Float)
