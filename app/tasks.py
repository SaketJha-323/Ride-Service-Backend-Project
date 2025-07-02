from celery import Celery
from app import create_app, db
from app.models import Ride, Driver
from datetime import datetime, timedelta
from geopy.distance import geodesic
import os

app = create_app()
celery = Celery(__name__, broker=os.getenv('REDIS_BROKER_URL'))
celery.conf.update(app.config)

@celery.task()
def assign_drivers():
    with app.app_context():
        rides = Ride.query.filter_by(status='create_ride').all()
        for ride in rides:
            nearby_drivers = Driver.query.filter_by(status='available').all()
            for driver in nearby_drivers:
                dist = geodesic((ride.pickup_lat, ride.pickup_lng), (driver.lat, driver.lng)).km
                if dist <= 10:  # mock radius
                    ride.driver_id = driver.id
                    ride.status = 'driver_assigned'
                    ride.driver_assigned_at = datetime.utcnow()
                    driver.status = 'assigned'
                    db.session.commit()
                    break