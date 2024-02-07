from pprint import pprint
class Student:
    age  = 18
    name = 'Oleh'
    faculty = 'Faculty of Physics and Mathematics' 

print(getattr(Student, 'age', 404)) #Число 404 буде виведено, коли такого атрибуту не існує
setattr(Student, 'course', 1)
pprint(Student.__dict__)
delattr(Student, 'course')
print(getattr(Student, 'course', 404))

person = Student()
print(getattr(person, 'age', 404))