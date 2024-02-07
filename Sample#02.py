from pprint import pprint 
class Student:
    pass

class Pupil:
    age = 12
    school = 7

print('Атрибути та методи класу Student', Student.__dict__)

# print('Атрибути та методи класу Pupil', Pupil.__dict__)

# Jack = Pupil()
# print('Атрибути та методи  обʼєкту Jack', Jack.__dir__())
# pprint(dir(Jack)) # Сортує за алфавітом і не може бути переозначеною
# print('Jack.age = ', Jack.age)
# Jack.age = 13
# print('Jack.age = ', Jack.age)
# print('Pupil.age = ', Pupil.age)
# Jack.grade = 7
# pprint(Jack.__dict__)
# pprint(Pupil.__dict__)