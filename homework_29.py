# Exercise.1

# class Car:
#     def __init__(self, car_id):
#         self.car_id = car_id
#
#     def __str__(self):
#         return f"Car({self.car_id})"
#
#
# class ParkingLot:
#     def __init__(self, total_spots):
#         self.total_spots = total_spots
#         self.parked_cars = {}
#         self.total_cash = 0
#
#     def park(self, car):
#         if car.car_id in self.parked_cars:
#             print(f"{car} is already parked.")
#         elif len(self.parked_cars) >= self.total_spots:
#             print("Parking lot is full.")
#         else:
#             self.parked_cars[car.car_id] = car
#             print(f"{car} parked successfully.")
#
#     def release(self, car):
#         if car.car_id not in self.parked_cars:
#             print("Car not found in the parking lot.")
#             return
#
#         hours = int(input(f"How many hours was {car} parked? "))
#         if hours <= 0:
#             print("Hours must be positive.")
#             return
#
#         fee = hours * 500
#         self.total_cash += fee
#         del self.parked_cars[car.car_id]
#         print(f"{car} released. Fee: {fee} AMD.")
#
#     def spots_left(self):
#         return self.total_spots - len(self.parked_cars)
#
#     def cash_register(self):
#         return self.total_cash
#
# lot = ParkingLot(2)
# car1 = Car("Bentley")
# car2 = Car("Alfa Romeo")
# car3 = Car("Changan")
#
# lot.park(car1)
# lot.park(car2)
# lot.park(car3)
#
# lot.release(car1)
# print("Spots left:", lot.spots_left())
# print("Total cash:", lot.cash_register())

# Exercise.2

# class Animal:
#     def eat(self):
#         return "Animal is eating..."
#
#     def sleep(self):
#         return "Animal is sleeping..."
#
#
# class Bird(Animal):
#     def eat(self):
#         return "Bird is pecking at its food..."
#
#     def fly(self):
#         return "Bird is flying..."
#
#
# class Fish(Animal):
#     def swim(self):
#         return "Fish is swimming..."
#
#
# a = Animal()
# b = Bird()
# f = Fish()
#
# print(a.eat())
# print(b.eat())
# print(b.fly())
# print(f.sleep())
# print(f.swim())