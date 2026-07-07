class vehicle:
    def __init__(self):
        pass
    def display(self):
        print("vehicle")
class car(vehicle):
    # overriding
    def display(self):
     print("fuel type car")

class bike(vehicle):
    def display(self):
     print("this is a bike")

#object
c1 = car()
c1.display()

#object
d1 = bike()
d1.display()