# OOPs Techniques

# data abstraction
'''
class EmpData:
    name = "Linkan"
    company = "Google"
    __salary = 100000 # private variable
    __age = 25 # private variable
    def display(self):
        print(f"He works fullday and got {EmpData.__salary}") # we can use private variable like this

obj = EmpData()
print(obj.name)
print(obj.company)
obj.display()
print(obj.__salary) # Attribute Error
'''
# Encapsulation
'''
It is the process of binding all atributes ( variables and methods ) into a single entity ( class )
'''
# Inheritance
# Single level inheritance
'''
class Parent:
    var1 = "Parent Variable"
    def Parent_Method(self):
        print("Accessing Parent Method")

class Child(Parent):
    var2 = "Child Variable"
    def Child_Method(self):
        print("Accessing Child Method")

obj = Child()
print(obj.var1)
print(obj.var2)
obj.Parent_Method()
obj.Child_Method()
'''
# Multilevel inheritance
'''
class Parent1:
    var1 = "Parent1 variable"
    def Parent1_Method(self):
        print("Accessing Parent1 method")
class Parent2(Parent1):
    var2 = "Parent2 variable"
    def Parent2_Method(self):
        print("Accessing Parent2 method")
class Parent3(Parent2):
    var3 = "Parent3 variable"
    def Parent3_Method(self):
        print("Accessing Parent3 method")

obj = Parent3()      
print(obj.var1)
print(obj.var2)
print(obj.var3)
obj.Parent1_Method()
obj.Parent2_Method()
obj.Parent3_Method()
'''
# Multiple inheritance
'''
class Parent1:
    var1 = "Parent1 variable"
    def Parent1_Method(self):
        print("Accessing Parent1 method")
class Parent2:
    var2 = "Parent2 variable"
    def Parent2_Method(self):
        print("Accessing Parent2 method")
class Parent3:
    var3 = "Parent3 variable"
    def Parent3_Method(self):
        print("Accessing Parent3 method")
class Child(Parent1, Parent2, Parent3):
    var4 = "Child variable"
    def Child_Method(self):
        print("Accessing child method")

obj = Child()
print(obj.var1)
print(obj.var2)
print(obj.var3)
print(obj.var4)
obj.Parent1_Method()
obj.Parent2_Method()
obj.Parent3_Method()
obj.Child_Method()
'''
# Hierarchical inheritance
'''
class Parent:
    var1 = "Parent variable"
    def Parent_Method(self):
        print("Accessing Parenet method")

class Child1(Parent):
    var2 = "Child1 variable"
    def Child1_Method(self):
        print("Accessing child1 nethod")
class Child2(Parent):
    var3 = "Child2 variable"
    def Child2_Method(self):
        print("Accessing child2 nethod")
class Child3(Parent):
    var4 = "Child3 variable"
    def Child3_Method(self):
        print("Accessing child3 nethod")

obj1 = Child1()
print(obj1.var1)
print(obj1.var2)
obj1.Child1_Method()
obj1.Parent_Method()

obj2 = Child2()
print(obj2.var3)
print(obj2.var1)
obj2.Child2_Method()
obj2.Parent_Method()

obj3 = Child3()
print(obj3.var4)
print(obj3.var1)
obj3.Child3_Method()
obj3.Parent_Method()
'''

# Polymorphism

# Method Overloading (methods having same name but different signature in a single class)
'''
class MyClass:
    def display(self):
        print("First method")
    def display(self, a):
        print("Second method")
    def display(self, a, b):
        print("Third method")
    def display(self, a, b, c):
        print("Fourth method")

obj = MyClass()
obj.display(10, 20, 30)
'''
# Method overriding (methods having same name but same signature in parent and child class)
'''
class Parent:
    def display(self):
        print("Parent method")

class Child(Parent):
    def display(self):
        print("Child method")
        super().display()
obj = Child()
obj.display()
'''