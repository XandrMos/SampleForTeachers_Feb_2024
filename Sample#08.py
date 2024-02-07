from pprint import pprint
class Mammals:
    def __init__(self) -> None:
        self.paws = 4
    def eat(self):
        print("I like eat")

class Dog(Mammals):
    def __init__(self) -> None:
        Mammals.__init__(self)
        self.name = "Jack"
        self.breed = "Labrador"
    
    def can_woof(self) -> None:
        print("I like bark out")
    
    def eat(self):
        print("I like eat bones and meat.")

class Cat(Mammals):
    def __init__(self, name, breed) -> None:
        Mammals.__init__(self)
        self.name = name
        self.breed = breed
    
    def can_sleep(self) -> None:
        print("I like sleep")
    
    def eat(self):
        print("I like eat meat")

class Sphynx_cat(Cat):
    def __init__(self, name, breed) -> None:
        Cat.__init__(self, name, breed)
        self.fur = False
    
    def eat(self):
        print(" like eat Whiskas")

animal_one = Dog()
pprint(animal_one.__dict__)

animal_two = Cat("Puh", "Pers")
pprint(animal_two.__dict__)

animal_three = Sphynx_cat("Asya", "Sphynx")
pprint(animal_three.__dict__)