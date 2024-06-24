# Define a class called 'Car'
class Car:
    # Constructor method to initialize the car object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method to start the car
    def start(self):
        print(f"The {self.make} {self.model} has started.")

    # Method to accelerate the car
    def accelerate(self, speed):
        self.speed += speed
        print(f"The car is now moving at {self.speed} km/h.")

    # Method to brake the car
    def brake(self, speed):
        self.speed -= speed
        if self.speed < 0:
            self.speed = 0
        print(f"The car is now moving at {self.speed} km/h.")

    # Method to stop the car
    def stop(self):
        self.speed = 0
        print("The car has stopped.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Accessing object attributes
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

# Calling object methods
my_car.start()
my_car.accelerate(50)
my_car.brake(20)
my_car.stop()