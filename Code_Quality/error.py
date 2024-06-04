# a normal exception handling program
a = 10
b = 0
try:
    c = a/b
    print(c)
except:
    print('Error Raised')

# we can modify this for better error handling
a = 10
b = 2

try:
    c = a/b
    print(c)
except NameError:
    print("Please use a defined name only")

except TypeError:
    print("Please use proper type of data")

except ValueError:
    print("Please use proper values")

except ZeroDivisionError:
    print("Don't use 0 in denominator")

except:
    print("Error Raised")

else:
    print("Try Executed")

finally:
    print("Thank You")

# user-defined exception

class LessThanZeroMarkError(Exception):
    pass

class MoreThanHundredMarkError(Exception):
    pass

marks = eval(input("Enter your marks: "))
if marks >= 0 and marks <= 34:
    print("Failed")
elif marks >= 35 and marks <= 100:
    print("Passed")
elif marks < 0:
    raise LessThanZeroMarkError("You have given less than 0 marks")
elif marks > 100:
    raise MoreThanHundredMarkError("You have given more than 100 marks")
else:
    print("No Error Raised")
