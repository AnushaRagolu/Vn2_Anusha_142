'''
Function:
A function is a group of related statements that can perform specific tasks.
there are two types of functions are there:
---> built-in functions
---> User defined functions

Built-in Functions:
--------------------
int()   help()     print()    max()
chr()   range()    input()    type()
ord()   len()      min()      zip()

user defined functions:
-----------------------

ex:
'''
count = 0
for i in [1, 2, 3, 4, 5]:
    count += i
print(count)
'''
Ex:
'''
def person_names(n1, n2):    #defining the function
    name = n1 + n2
    return name
x = person_names("Anu", "sha")   #calling function
print(x)
'''
Ex:
'''
def func():
    x = 20
    print("Hey, I'm from inside of function", x)
x=35
func()
print("Hey, I'm from outside of function", x)
'''
Ex:
'''
def my_function(name):
    print(name+"referance")
my_function("Anusha ")
my_function("Jamuna ")
my_function("Peter ")
'''
EX:
'''
val = 10
def func():
    val = 5
    print(val)
print(val)
func()
'''
Ex:
'''
def sum_of_list(list1):
    return sum(list1)
l= [1, 2, 3, 4, 5]
print(sum_of_list(l))
'''
Ex:
'''
def len(l):
    count = 0
    for i in l:
        count += 1
    return str(count) + " is the length of the iterations"
def func3(list1):
    s = len(list1)
    return s
s = "gyoyvucthjkvityctygkgvh"
print(func3(s))
'''
examples of using built-in funtions:
Ex:
'''
def add(a, b):
    print(a+b)
add(4, 5)
'''
Ex:
'''
def sum(a, b):
    print(a+b)
sum(5, 4)
'''
Ex:
'''
def My_function(*Anusha):
    print("Anusha likes", Anusha[0])
My_function("cakes", "chocolates", "clothes")