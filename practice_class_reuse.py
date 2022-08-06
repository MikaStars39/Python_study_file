class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('initialize school member as:', self.name)

    def say(self):
        print('My name is {}, and my age is {}.'.format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Here is a teacher {}'.format(self.name))

    def tell(self):
        print('The salary of this teacher is {}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
        print('Here is a student {}'.format(self.name))

    def tell(self):
        print('The score of this student is {}'.format(self.score))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
