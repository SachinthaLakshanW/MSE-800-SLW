from database import db
from datetime import datetime

class Booking:
    def __init__(self, booking_id, user_id, car_id, start_date, end_date, total_cost, status="Pending"):
        self.id = booking_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.status = status

    def approve(self):
        db.update_booking_status(self.id, "Approved")
        self.status = "Approved"

    def reject(self):
        db.update_booking_status(self.id, "Rejected")
        self.status = "Rejected"

    @staticmethod
    def calculate_total_cost(car_price_per_day, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        rental_days = (end - start).days + 1
        return rental_days * car_price_per_day
