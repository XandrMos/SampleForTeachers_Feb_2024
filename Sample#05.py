from pprint import pprint
class Student:
    def __init__(self, age:int, name:str) -> None:
        self.age = age
        self.name = name
    
    def learn(self) -> None:
        print(["Ukrainian", "Algebra", "Geometry", "English"])

person = Student(12, "Oleh")
pprint(person.__dict__)
person.learn()