'''
Interface: Defines a contract specifying what methods a class should implement.

Abstract method: A method declared in an abstract class or interface that has no implementation and must be implemented by subclasses.

Abstract base class (ABC): A class that defines one or more abstract methods and can't be instantiated directly. It serves as a blueprint for other classes to inherit from and implement its abstract methods.
'''
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method(self):
        pass

class MyClass(Interface):
    def method(self):
        print("Implementing method")

# Instantiate MyClass
obj = MyClass()
obj.method()  # Output: Implementing method
# In this example, Interface defines an abstract method method(). Any class that inherits from Interface must implement method().

# If you try to instantiate a class that doesn't implement the abstract method, you'll get an error:
class AnotherClass(Interface):
    pass

# This will raise an error:
# TypeError: Can't instantiate abstract class AnotherClass with abstract methods method
another_obj = AnotherClass()
