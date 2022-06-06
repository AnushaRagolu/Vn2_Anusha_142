'''
Exception:
An Exception is an occurrence in a code. it is basically an error with disturbs the normal flow of the execution of a program.
Any logical error in python is called as exception.
we use try: except: block to handle the exception.

Examples:
'''
try:
    result = 100/0
    print("Divisible by Zero: {}".format(result))
except ZeroDivisionError:
    print("Error while execution")
result = 100*0
print("Multiplication: {} ".format(result))
'''
Ex:
'''
def validate_name(name):
    if name > 0:
        raise Exception("Name can't be compare with zero")
    print(f"Name is valid {name}")
try:
    validate_name("Anusha")
except Exception:
    print("There was an exception raised")
'''
Ex:
'''
try:
    dividend = int(input("Enter divided value: "))
    divisor = int(input("Enter divided value: "))
    result = dividend / divisor
    print("Division1: {}".format(result))
except ValueError:
    print("Error While division")
except IOError:
    print("IO Error")
else:
    print("Optional Block: There is no Exception")
finally:   #finally block is executed everytime
    print("Executed everytime")

result = int(10/2)
print("Division2: {}".format(result))








