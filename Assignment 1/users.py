from database import db
from booking import Booking

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Customer(User):
    def view_available_cars(self):
        cars = db.get_available_cars()
        if not cars:
            print("No cars available at the moment.")
            return
        print("\n=== Available Cars ===")
        for car in cars:
            print(f"ID:{car[0]} | {car[1]} {car[2]} | Year:{car[3]} | Mileage:{car[4]} | Price/day:${car[8]:.2f} | Available:{'Yes' if car[5] else 'No'}")

    def book_car(self, car_id, start_date, end_date):
        car_list = [c for c in db.get_all_cars() if c[0] == car_id]
        if not car_list:
            print("Car not found.")
            return
        car = car_list[0]
        total_cost = Booking.calculate_total_cost(car[8], start_date, end_date)
        user_data = db.get_user(self.username)
        db.add_booking(user_data[0], car_id, start_date, end_date, total_cost)
        print(f"Booking successful! Total cost: ${total_cost:.2f}")

class Admin(User):
    def add_car(self, make, model, year, mileage, min_rent_days, max_rent_days, price_per_day):
        from car import Car
        car = Car(make, model, year, mileage, min_rent_days, max_rent_days, price_per_day)
        car.save()
        print(f"Car {make} {model} added successfully!")
