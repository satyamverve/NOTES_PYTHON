""" Class: It is a blueprint of attributes(data) and methods(functions) of the object,
           which we have talking.
           We use camel case to name the class.
    >> objects: It is the instance of the class.
    >> To create objects of the class we call constructor i.e, __init__ method.
    >> When we use self parameter in a function then the function is called Method.
"""

# class School:
#     # def __init__(self,name, age):
#     #     self.name=name
#     #     self.age=age
#     #     print(f'{name} is {age} years Old.')
    
        
#     def add(self,x,y): 
#         return x+y
    
#     def bark(self):
#         print("Bark")

# # School('Satyam', 23)
# s=School()
# print(s.add(4,5))

# s.bark()


# class Student():
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self,age):
#         self.age=age
#     def set_name(self,name):
#         self.name=name
    
# d=Student('Satyam',23)
# print(d.get_name())
# print(d.get_age())
# d.set_age(22)
# d.set_name('Kumar')
# print(d.get_age())
# print(d.get_name())



# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self,course_name,max_students):
#         self.course_name=course_name
#         self.max_students=max_students
#         self.students=[]
    
#     def add_student(self,student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def get_avg_grade(self):
#         value=0
#         for student in self.students:
#             value+=student.get_grade()
#         return value/len(self.students)
 
# s1=Student('Satyam',23,84)
# s2=Student('Rahul',22,89)
# s3=Student('Ravi',18,74)
# s4=Student('Shaurya',21,62)


# course=Course('IT',12)
# print(course.add_student(s1))
# print(course.add_student(s2))
# print(course.add_student(s3))
# print(course.students[0].name)
# print(course.students[0].age)
# print(course.students[0].grade)

# course=Course('Science',10)
# print(course.add_student(s2))
# print(course.students[0].name)
# print(course.students[0].age)
# print(course.students[0].grade)

# print(course.add_student(s3))
# print(course.students[1].name)
# print(course.students[1].age)
# print(course.students[1].grade)

# course=Course('Commerce',3)
# print(course.add_student(s4))
# print(course.students[0].name)
# print(course.students[0].age)
# print(course.students[0].grade)

# print(course.get_avg_grade())




""" Inheritence: When we ctreate new class from an existing class to use their properties without modifying it 
    then this method is called Inheritence.
"""
# class Pet:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old.")
#     def speak(self):
#         print("I don't know , what to speak?")

# class Dog(Pet):
#     def speak(self):
#         print('Bark')
        
# class Cat(Pet):
#     def __init__(self, name, age,color):
#         self.color=color
#         super().__init__(name, age)  # "super()" is used to reference the super class or upper level parent class i.e, parent class 
#     def speak(self):
#         print('Meow')    
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}.")
        
# class Fish(Pet):
#     pass
    
# p=Pet('Shera',4)
# p.show()
# p.speak()

# d=Dog('Tafi',3)
# d.show()
# d.speak()

# c=Cat('Ramy',2,'black')
# c.show()
# c.speak()

# f=Fish('Bubbles',1)
# f.speak()

# f=Fish('Bubbles',1)
# f.speak()


""" Classes and their Attributes """

# class Person:
#     # number_of_people=0
#     # def __init__(self,name):
#     #     self.name=name
#     #     print(f"My name is {name}")
#     def me(data):
#         # self.data=data
#         print(data)
# # p1=Person('Jill')
# # p2=Person('Tom')
# # Person.number_of_people=7
# # print(p1.number_of_people)
# # Person.number_of_people=8
# # print(p2.number_of_people)

# p3=Person()
# p3.me("Satyam Kumar")

# Person("Satyam Kumar")

""" CLASS METHODS """

""" NOTE: Using "self" keyword we can access both the instance variables and class attributes ,
while by using "cls" we cannot access instance variables in a class, we can only access the 
attributes of the class"""


        
""" @classmethod, @staticmethod:- These are called "DECORATORS in Python: When we declare that
decorators before any method then we not need to add self as a parameter in that method. After
using decorators it not a instance of the class that's why are not using "self".
    "cls" refers to the class   """
# class Person:
#     number_of_people=0
#     GRAVITY=-9.8
#     def __init__(self,name):
#         self.name=name
#         Person.add_person()
                       
#     @classmethod                   
#     def number_of_peopl(cls):    
#         return cls.number_of_people
    
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people+=1
        
# p1=Person("Tom")
# # print(Person.number_of_people)
# p2=Person("Jerry") 
# # print(Person.number_of_people)

# print(Person.number_of_peopl())


""" STATIC METHODS: Staic Methods means not changed that means staying the same i.e,
they do something but they do not change anything .For adding two functions together we use 
Static Method """


# class Math:
#     @staticmethod
#     def add(x):
#         return x+5
    
#     @classmethod
#     def sub(y):
#         return y-1

# m=Math()
# print(Math.add(6))


""" Method Overriding in python """
# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog barks")

# my_animal = Dog()
# my_animal.make_sound()  # Calls the overridden method in Dog class

# a=Animal()
# a.make_sound()


# """ use of @property  """

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute with underscore prefix
# 
    @property
    def radius(self):
        print("Getting radius")  # Optional: You can include some logic here
        return self._radius
# 
    @radius.setter
    def radius(self, new_radius):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius cannot be negative")
# 
    @property
    def area(self):
        return 3.14159265359 * self._radius**2
# 
    @property
    def circumference(self):
        return 2 * 3.14159265359 * self._radius
# 
# 
# Creating a Circle object
circle = Circle(5)
# 
# Accessing the radius attribute using the property (getter)
print(circle.radius)  # Output: Getting radius 5
# 
# Accessing the area attribute using the property (getter)
print(circle.area)  # Output: 78.539816339745
# 
# Accessing the circumference attribute using the property (getter)
print(circle.circumference)  # Output: 31.4159265359
# 
# Modifying the radius attribute using the property (setter)
circle.radius = 7
print(circle.radius)  # Output: Getting radius 7
# 
# Trying to set a negative radius, which raises a ValueError
# circle.radius = -3  # Raises a ValueError



