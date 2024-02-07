from pprint import pprint
class Student:
    def __init__(self, age:int, name:str, mark:int) -> None:
        self.age = age #Public variable
        self.name = name #Public variable
        self._faculty = "Faculty of Physics and Mathematics" #Protected variable
        self.__mark = mark #Private variable
    def show_mark(self):
        return self.__mark
    
person = Student(18, "Oleh", 90)

print("Public attr name: ", person.name)
# print("Public attr age: ", person.age)
# print("Protected attr _faculty:", person._faculty)
# print("Return value of the private attr: ", person.show_mark())
#print("Private attr __mark", person.__mark)

pprint(dir(person))
print(" Access to a private attribute of an object. __mark = ", person._Student__mark)

    
        