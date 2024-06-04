# Code Quality Check using pylint
#1. Here arguments should be vertically aligned
def add(a,b,
        c,d):
    '''a function which returns addition of 4 numbers'''
    return a + b + c + d

def sub(a, b):
    '''a function that perform subtraction of 2 numbers'''
    return a - b

def mul(a, b):
    '''
    a function to perform multiplication between two numbers
    '''
    return a * b

def div(a, b):
    '''
    function to perform division between two number
    '''
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Please provide a value of b other than 0"
print(add(1, 2, 3, 4))
print(sub(10, 5))
print(mul(10, 4))
print(div(10, 0))

#2. Operators
# a space should be given before and after each operator

print(5 == 4)

if 5 in [1, 2, 3, 4, 5]:
    print("It is present inside the list")
else:
    print("It is not present inside the list")

#3. a space should be given after a comma, colon
# list
numbers = [1,2,3,4,5] # this is bad syntax
# dictionary - holding students and grades
grades = {'Ram':10, "Anna":9.6, "Linkan":9.3}

#4. no space between brackets
# bad syntax
print( 'Hello world' )
numers = [ 1, 2, 3, 4, 5 ]
prices = { 'apple':100, 'orange':120 }

# good syntax
print('Hello world')
numers = [1, 2, 3, 4, 5]
prices = {'apple':100, 'orange':120}

#5. no space should be given after = when using keyword arguments

def area_of_circle(radius):
    '''Area of a circle'''
    return 3.141 * radius * radius
area_of_circle(radius=5)

#6. when using exception handling particular exception should be mentioned

# exception handling
# bad practice
def int2hex(integer):
    '''
    converting an integer value to hexadecimal value
    '''
    try:
        hexadecimal = hex(integer)
        return hexadecimal
    except: # here we should provide which type of error we are handling like- except TypeError:
        return "An integer should be provided."

# calling the function
int2hex('5')

#7. not using == when comapring anything with boolean values in if statement

ISPRESENT = True # capital letter naming for boolean values
if ISPRESENT: # bad syntax, good one is- if ISPRESENT:
    print("Present")
else:
    print("Not Present")

#8. importing modules

'''
While importing modules a order should be maintained

importing standard_library

importing third_party_module

importing local_files
'''
import tkinter

import numpy

import main
