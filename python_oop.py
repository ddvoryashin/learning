class Dog():
    def __init__(self, name, age):   # this method is called automatically when initializing class instance
        self.name = name        # defining attribute of a class instance
        self.age = age

    def bark(self):
        print('bark')

    def set_age(self, age):
        self.age = age

d = Dog('Tim', 34)
d2 = Dog('Bill', 12)


#################################

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100

    def get_grade(self):
        return self.grade

class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []     # creating list to store objects of Student class

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student('Tom', 15, 93)
s2 = Student('Jack', 14, 67)
s3 = Student('Pete', 15, 74)

course = Course('Computer Science', 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())

################
# Inheritance
################

class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'My name is {self.name} and I am {self.age} years old')

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)          # how to add parents variables to init in child class
        self.color = color

    def show(self):
        print(f'My name is {self.name}, I am {self.age} years old and I am {self.color}')   # all the init variables of parent still work through self

    def speak(self):        # child's function will overwrite parent's one with the same name
        print('Meow')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Bill', 10)
#p.show()
#p.speak()
c = Cat('Helen', 4, 'Brown')
#c.show()
#c.speak()
d = Dog('Josh', 7)
#d.show()
#d.speak()
f = Fish('Mary', 1)
#f.show()
#f.speak()

class Person():
    number_of_people = 0            # this variable belongs to class but not to it's instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_person()

    @classmethod                            # that's how you can create function that is used by class rather than it's instance
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('Tim', 16)
print(Person.number_of_people_())
p2 = Person('Jack', 49)
print(Person.number_of_people_())

################
# Static
################

class Math:

    @staticmethod         # this way you can use class functions without creating it's instances
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

print(Math.add10(5))
