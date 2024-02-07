class Student:
    pass

var_a = 12

var_obj = Student()
# Виводимо тип змінної var_a
print('Тип зміної var_a: ', type(var_a))
# Перевіряємо чи є змінна var_a екземпляром класу int
# print('Змінна var_a є екземпляром класу int: ', isinstance(var_a, int))
# Виводимо тип змінної var_obj
# print('Тип зміної var_obj: ', type(var_obj))
# Перевіряємо чи є змінна var_obj екземпляром класу Student
# print('Змінна var_obj є екземпляром класу Student: ', isinstance(var_obj, Student))

# print('Змінна var_a є обʼ єктом', isinstance(var_a, object))
# print('Змінна var_obj є обʼєктом', isinstance(var_obj, object))
# print('Чи правда, що Student є обʼєктом', isinstance(Student, object))
# print('Чи правда, що int є обʼєктом', isinstance(int, object))
# print(isinstance(type, object))
# print(isinstance(object, type))