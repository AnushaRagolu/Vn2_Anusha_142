'''
If statement:
---------------
In Python, If statement is a conditional statement wherein a set of statements execute based on the result of a condition.
An "if statement" is written by using the if keyword.
Indentation:
--------------
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
Other programming languages often use curly-brackets for this purpose.

Syntax:
if expression:
    statement
else:
    statement

Example:
'''
a = 123
b = 100
if a>b:
    print("a is greater than b")
'''
Elif:
-------
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

Syntax:
if expression:
    statement
elif expression:
    statement

Ex:
'''
a = 1
b = 9
if a>b :
    print("a is greater than b")
elif a<b:
    print("a is less than b")
'''
else:
------
The else keyword catches anything which isn't caught by the preceding conditions. Here, it can't accept the expressions.

Ex:
'''
a = 9
b = 9
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
'''
using else without elif condition:

Ex:
'''
a = 5
b = 9
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")
'''
Ex-1
'''
fruit_store = ["mango", "Banana", "strawberry", "apple"]
x = fruit_store[3]
if x[0] == "a":
    print("lets not take this fruit")
'''
Ex-2:
'''
raining = True
if raining == False:
    print("stay in home")
else:
    print("Lets go outside")
'''
Ex-3:
'''
x = input("Enter what you want ")
cake = x
if cake == "Baverage":
    print("Yes! its a Baverage")
else:
    print("It's not a baverage")
'''
Ex-4:
'''
fruit_store = ["Mango", "Banana", "Apple", "Cherry"]
if "Dragon fruit" in fruit_store:
    print("Yahoo! its there")
else:
    print("Better luck next time")
'''
Ex:
'''
number = -12
if number == 0:
    print("Number is Zero! Hurray!")
elif number > 0:
    print("Number is positive")
else:
    print("Number is negative")
'''
--->  for multiple conditions, we use if elif.

Ex:
'''
num = 10.36
if isinstance(num, float): #if type(num) == float:
    print("number is float value")
else:
    print("Other than a float value")



