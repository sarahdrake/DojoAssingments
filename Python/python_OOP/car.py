class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price:   ", self.price
        print "Speed:   ", self.speed
        print "Fuel:    ", self.fuel
        print "Mileage  ", self.mileage
        print "Tax:     ", self.tax

car1 = Car(50000, "70mph", "Full", "15mpg")
car2 = Car(5000, "40mph", "Full", "30mpg")
car3 = Car(80000, "75mph", "Full", "25mpg")
car4 = Car(10000, "50mph", "Full", "40mpg")
car5 = Car(700, "10mph", "Full", "11mpg")
car6 = Car(12000, "60mph", "Full", "35mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
