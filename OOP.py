class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

c = Cat("Yasmin", 2)
c2 = Cat("Ruby", 4)
print(c.get_age())
 

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade 
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

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
 
s1 = Student("Aminatu", 22, 86)
s2 = Student("Sadiya", 23, 88)
s3 = Student("Basirah", 24, 85)
s4 = Student("Hanifa", 22, 85)
s5 = Student("Shafi'i", 25, 89)

course = Course("Pharmacology", 3)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].name)
print (course.get_average_grade())
 

class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def show(self):
        print (f"I am {self.name}, I am {self.age} years old and I am {self.color} in color")
    
    def speak(self):
        print("I don't know what to say")

class Parrot(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)         #super references the parent class
        self.color = color
    
    def speak (self):
        print("Mimick")

class Dog(Pet):
    def speak (self):
        print("Bark")

p = Pet("Olive", 5, "Nude")
p.speak()
p.show()

s= Parrot("Sparrow", 10, "Green and Ash")
s.speak()
s.show()

d = Dog("Jack", 7, "Cream")
d.speak()
d.show()

#using class attributes
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    #using class methods
    @classmethod
    def number_of_persons(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people =+ 1

p1 = Person("Hassanah")
print(Person.number_of_people)
p2 = Person("Abubakar")
print(Person.number_of_people)
p3 = Person("Aminah")
print(Person.number_of_people)