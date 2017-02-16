class Bike(object):
    def __init__ (self, price, speed):
        self.miles = 0
        self.price = price
        self.speed = speed

    def displayInfo(self):
        print 'The price of you bike is', self.price
        print 'Your bike has a max speed of', self.speed
        print 'Your bike has a total mileage of', self.miles

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles > 0:
            self.miles -= 5

# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
bike1 = Bike("$250", "45 mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike("$1000", "65 mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
