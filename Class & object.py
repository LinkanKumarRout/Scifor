# Class - class is a collection of variables and methods
# Object  - object is an instance of a class
# the variables and methods which are defined in a class are called as class members and are used by object.

# class - blueprint for an object
# object - instance of a class

"""
class StudentsData: # creating a class
    name = "Linkan"  
    fee = 10000
    loc = 'Odisha'
    def learning(self):
        print("He is learning Python")
    def practicing(self):
        print("He is practicing programs")
obj = StudentsData() # creating object 

# calling class atributes using an object
print(obj.name)
print(obj.fee)
print(obj.loc)
obj.learning()
obj.practicing()
"""
# Class and object variables
"""
class EmpData:
    company = "Google" # class variable
    location = "Hyderabad"
    def __init__(self, name, salary): # constructor
        self.name = name # object variable
        self.salary = salary
    def display(self):
        print("Emp Name:",self.name) # object/instance variable
        print("Emp salary:", self.salary)
        print("Emp Company:", EmpData.company) # accessing class variable
        print("Emp Location:", EmpData.location)

obj1 = EmpData("Linkan", 100000)
obj2 = EmpData("Sagar",50000)

obj1.display()
print()
obj2.display()
"""
# Constructor and methods
'''
class MyClass:
    def __init__(self):
        print("Constructor is calling")

    def display(self):
        print("Method is calling")

obj = MyClass() # constructor get called automatically whenever we create an object
obj.display() # manually calling a method
'''
# Types of methods
'''
class StudentsData:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
        
    def display(self): # instance method
        print(f"{self.name} got {round(self.percentage)}%")
    
    @classmethod
    def findingPercentage(cls, name, marks): # class method
        return cls(name, (marks/600)*100)
    
    @staticmethod
    def playting(): # object method
        print("He plays everyday")

name = "Linkan"
marks = 499

obj = StudentsData.findingPercentage(name, marks)
obj.display()
obj.playting()
'''