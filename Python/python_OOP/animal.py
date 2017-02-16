class Animal(object):
    def __init__ (self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name, self.health
        return self

animal = Animal("Cow")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self). __init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

animal2 = Dog("Dog")
animal2.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self). __init__(name)
        self.health = 170

    def displayHealth(self):
        print "This is a dragon!", self.name, self.health
        return self

    def fly(self):
        self.health -= 10
        return self

animal3 = Dragon("Dragon")
animal3.walk().walk().walk().run().run().fly().fly().displayHealth()
