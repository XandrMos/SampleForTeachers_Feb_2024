from pprint import pprint
class Student:
    def __init__(self) -> None:
        self.age = 18
        self.course = 1
        self.name = "Oleh"

# class Pupil:
# #cls це жорстко визначена назва змінної у Python
#     def __new__(cls,  *args, **kwargs) -> object:
#         print("Крок 1. Створення самого обʼєкта")
#         obj = super().__new__(cls) 
#         #super - команда доступу до батькіської структури і використання його метода 
#         #__new__
#         print(type(obj))
#         return obj
#     def __init__(self, name:str, age:int) -> None:
#         self.name = name
#         self.age = age
#         print("Крок 2. ініціалізація обʼєкта завершена")

person_one = Student()
pprint(person_one.__dict__)

# person_two = Pupil("Jack", 12)
# pprint(person_two.__dict__)