'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Create vechile class and show the Speed and Mileage.'''
class Vehicle:

    # Instance Attribute
    def __init__(self, speed, mileage):
        self.Speed = speed
        self.Mileage = mileage

    # Instance Method
    def printto(self):
        print(self.Speed, self.Mileage)
        return self.Speed, self.Mileage

speed = int(input())
mileage = int(input())
a = Vehicle(speed, mileage)
a.printto()