class Dog:
    def walk(self):
        print("I like walk with my human")

class Cat:
    def sleep(self):
        print("I like sleep near my human")

class Pet(Dog, Cat):
    pass

animal = Pet()
animal.walk()
animal.sleep()
