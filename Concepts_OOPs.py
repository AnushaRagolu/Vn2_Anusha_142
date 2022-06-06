'''
OPPs Concepts:
----------------
* class
* Object
==> Pillars of OOPs are :  * Abstaction
                           * Encapsulation
                           * Inheritance
                           * Polymorphism
Class :
--------
A Class is a user defined blueprint or prototype from which the objects are created.

Object:
--------
Object is the instance of a class

instance - an instance is a copy of the class with actual values.

Note:
-->  method is associated with the class
-->  Self is a argument which associates the given method with class
-->  Self usage is to create the instance variable
-->  Attributes and behaviours are not mandatory in class but it should be present in it.
-->  "pass" doesn't have any attribute

Ex:
'''
class Dog:                             #class name
    def __init__(self, name, Breed):  #Calling Constructor of class name
        self.name = name              #instance variables
        self.Breed = Breed
    def bark(self):                   #method
        print("{} is barking".format(self.name))
    def run(self):                    #method
        print("{} is running".format(self.name))
# if __name__ == "__main__":
dog1 = Dog("Dhunnu", "Black Retriever")
dog1.run()
dog2 = Dog("Cupper", "Golden Retriever")
dog2.bark()
print(type(dog1))
'''
Encapsulation:
----------------
Encapsulation is one of the most important aspects of object-oriented programming.
The binding or wrapping of code and data together into a single cell is called encapsulation.
Encapsulation in Python is mainly used to restrict access to methods and variables.

--> Private attribute is marked by __ at the biginning of the parameter.
super() function is used for accessing the all methods and all properties of the class either parent class or child class.

Ex:
'''
class Teacher:
    def __init__(self, name, experience, salary):   #constructor
        self.__name = name
        self.experience = experience
        self.salary = salary
    def profile(self):              #method/behaviour
        print("Teacher name is {}, {} of experience and salary is {}".format(self.__name, self.experience, self.salary))
        print(f"Teacher name is {self.__name}, {self.experience} and salary is {self.salary}")

Anu = Teacher("Rani", "7 Years", "10 LPA")
Anu.profile()
Anu.__name="Meghana"
'''
EX:
'''
class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature
    def to_fahrenheit(self):
        return 1.8 * self.temperature + 32

cel = Celsius(10)
print("To Fahrenheit {}".format(cel.to_fahrenheit()))
cel.temperature = 100
print("To Fahrenheit {}".format(cel.to_fahrenheit()))
'''
class method:
--------------
@classmethod function also callable without instantiating the class but its definition follows
sub class, not parent class, via inheritance.

Ex:
'''
from datetime import date
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def display_info(self):
        print(f'Name {self._name} Age {self._age}')           # using fstring method
        print("Name {} age {}".format(self._name, self._age))     # using format method
    @classmethod
    def DOB(cls, name, year_of_birth):
        age = date.today().year - year_of_birth
        return cls(name, age)

obj = Person.DOB("Anusha", 1998)
obj.display_info()
'''
Example of OOPs Concept:
'''
class School:
    school_name = "NRI"
    def __init__(self, name, contact, address):
        self.name = name
        self.contact = contact
        self.address = address

A = School("Anusha", 7995370698, "Vizag")
# print(A.name, A.contact, A.address)
B = School("Anshu", 8904402561, "Jaipur")
print(A.__dict__)
print(B.__dict__)  #stored in dictionary
'''
Ex:
'''
class pow:
    def __init__(self):
        self.value = int(input("Enter the value: "))
        self.power = int(input("Enter the power"))
    def output(self):
        return self.value ** self.power
obj = pow()
print(obj.output())
