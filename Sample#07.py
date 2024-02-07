class Human:
    def can_speak(self) -> None:
        print("Hello!")

class Student(Human):
    def can_learn(self) -> None:
        print("I like read books!")

class Teacher(Human):
    def can_teach(self) -> None:
        print("I like teach computer sciences!")

print(issubclass(Student, Human))

# person = Student()
# person.can_speak()
# person.can_learn()