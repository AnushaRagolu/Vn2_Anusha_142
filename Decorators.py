'''
Decorator:
A Decorator is a function that takes another function as an argument adds some
kind of functionality and then returns another function.

using decorator, you can add extra features in the existing function.
'''
def my_decor(func):
    def my_decoration(a, b):
        print("anusha")
        return func(a, b)
    return my_decoration
def my_function(a, b):
    print("Anusha")
    print(a, b)
my_function = my_decor(my_function)
my_function("Anshu", "5")
'''
Ex:
'''
def fruit(func):

    def apple(*args, **kwargs):
        print("Apple is a Fruit")
        return func(*args, **kwargs)

    return apple

def veg(str1, str2):
    print("Vegetarian")
    print(str1 + " are " +  str2)

Anu = fruit(veg)

veg("Apples", "not vegetarians")
'''
Ex:
'''
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("I am listening their voice")
    print(greeting)

greet(shout)
greet(whisper)







