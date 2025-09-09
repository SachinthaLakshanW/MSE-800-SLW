from database import db

class Car:
    def __init__(self, make, model, year, mileage, min_rent_days, max_rent_days, price_per_day):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.min_rent_days = min_rent_days
        self.max_rent_days = max_rent_days
        self.price_per_day = price_per_day

    def save(self):
        db.add_car(self.make, self.model, self.year, self.mileage, 1, self.min_rent_days, self.max_rent_days, self.price_per_day)
