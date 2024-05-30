#1. What is Python ? Provide some key features of python .
'''
Python is a high-level, interpreted, and general purpose dynamic programming language.
Some features of python includes-
- Simple and easy to learn
- freeware & open source
- high-level language
- portability
-platform independent
- dynamic
- both procrdural and object oriented
- interpreted
- extensible
- embeded
- rich liabrary support
- automatic memory management
'''
#2. Explain the difference between Python 2 and Python 3
'''
Both Python2 and Python3 are two different versions of Python.
some differences are-

Print Function: In Python 2, the print statement is used without parentheses, while in Python 3, the print function is used with parentheses.

Integer Division: In Python 2, integer division returns an integer, while in Python 3, it returns a float.

Unicode Support: Python 3 has built-in support for Unicode, while Python 2 requires the use of the unicode function.

Input Function: In Python 2, the raw_input() function is used to get user input, while in Python 3, the input() function is used.

Exception Handling: In Python 2, exceptions are caught using the except clause without specifying the exception type, while in Python 3, it is recommended to specify the exception type.

Range Function: In Python 2, the range() function returns a list, while in Python 3, it returns a generator.

String Formatting: In Python 3, the .format() method is used for string formatting, while in Python 2, the % operator is used.

True and False: In Python 2, True and False are not reserved keywords, while in Python 3, they are.

Order of Operations: In Python 3, the order of operations has been changed to be more consistent with other programming languages.

Metaclasses: In Python 3, metaclasses are defined using the metaclass keyword, while in Python 2, they are defined using the __metaclass__ attribute.
'''
#3. How do you comment out multiple lines of code i python .
"""
You can comment out multiple lines of code by using triple single quotes or triple double quotes. '''comment'''
"""
#4. Describe the difference between == and is in python.
'''
The == operator is used to compare the values of two objects. It returns True if the values of the two objects are equal, and False otherwise. For Example:
x = 5
y = 5
print(x == y)  # returns True

On the other hand, the 'is' operator is used to compare the identity of two objects. It returns True if both the variables point to the same object, and False otherwise. For example:
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z)  # returns True
print(x is y)  # returns False
print(x == y)  # returns True
'''
#5. What is PEP8 and why it is important ?
'''
PEP 8 stands for "Python Enhancement Proposal 8." It is a style guide for writing Python code, outlining best practices and conventions to promote code readability and consistency. PEP 8 was authored by Guido van Rossum, Barry Warsaw, and Nick Coghlan, and it has become the de facto standard for Python code style.

PEP 8 is important because it promotes code consistency and readability, which are crucial for collaboration, maintenance, and understanding of codebases—especially in projects involving multiple developers or teams. Consistent code style makes it easier for developers to understand each other's code, reduces cognitive overhead, and helps identify potential errors or issues more quickly.
'''
#6. Explain the concept of dynamic typing in Python.
'''
Dynamic typing is a feature of Python (and other dynamically typed languages) where the type of a variable is determined at runtime rather than at compile time. This means that you don't need to explicitly specify the type of a variable when you declare it; instead, the type is inferred based on the value assigned to it.
'''
#7. What are tuples in python ? How are they different from lists ?
'''
The main difference between tuples and lists is that tuples are immutable, meaning their elements cannot be changed after creation, whereas lists are mutable, meaning their elements can be changed after creation.

Another difference is that tuples are more memory efficient than lists because they are stored in a single memory block, whereas lists are allocated in two blocks, one for the list object and one for the data.

Tuples are also faster than lists when it comes to lookup values.
'''
#8. How do you create a function in python, provide an example ?
'''
We can create a function in python by using the def keyword like below

def function_name(args):
    # function body
    return value
'''
#9. Explain the difference between local and global variables in python.
'''
In Python, variables can be categorized as either local variables or global variables based on their scope, which defines where in the code they can be accessed and modified.

Global Variables:
- Global variables are defined outside of any function or class, typically at the top level of a module.
- They are accessible from anywhere within the module, including inside functions and classes.
- Global variables can be accessed and modified from any part of the code.
- To modify a global variable from within a function, you need to use the global keyword to indicate that you are referring to the global variable rather than creating a new local variable with the same name.

Local Variables:
- Local variables are defined within a function or method and can only be accessed from within that function or method.
- They are created when the function is called and cease to exist once the function completes execution.
- Local variables can have the same name as global variables or variables in other functions without causing conflicts because they exist in separate namespaces
'''
#10. How do youhandle exceptions in python .
'''
In Python, exceptions are handled using try-except blocks. Here's a basic syntax for handling exceptions:
try:
    # Code that may raise an exception
    # For example:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero!")

Additionally, you can include an optional else block after the except block. The code inside the else block will be executed if no exception occurs in the try block:
try:
    # Code that may raise an exception
except SomeException:
    # Code to handle SomeException
else:
    # Code to execute if no exception occurred

Finally, you can use a finally block to specify cleanup code that should always be executed, regardless of whether an exception occurred or not. This block is commonly used for releasing resources like file handles or network connections:
try:
    # Code that may raise an exception
except SomeException:
    # Code to handle SomeException
finally:
    # Cleanup code that always runs, regardless of exceptions
'''
#11. What are decorators in python and how to use them ?
'''
Decorators in Python are a powerful and flexible feature that allows you to modify or extend the behavior of functions or methods without modifying their actual code. Decorators are functions that wrap around other functions or methods, adding additional functionality to them.
Here's a basic example of a decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

Decorators can also take arguments, which allows for more flexibility. Here's an example of a decorator with arguments:
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
'''
#12. Explain the concept of generators in python and how these are different from a regular function.
'''
Generators in Python are a special type of function that allows you to generate a sequence of values lazily, on-the-fly, rather than storing them all in memory at once. They are defined using the yield keyword instead of return, and they produce a series of values one at a time as requested, pausing and resuming execution as needed.

Here's a simple example of a generator function:
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

Generators are different from regular functions in several ways:

- Lazy Evaluation: Generators produce values lazily, meaning they only generate the next value when it is requested. This allows generators to work efficiently with large or infinite sequences because they don't need to generate all the values at once and store them in memory.

- Stateful Execution: Generators maintain their state between calls. When a generator yields a value, its internal state is saved, allowing it to resume execution from where it left off when called again. This is in contrast to regular functions, which start execution from the beginning each time they are called.

- Memory Efficiency: Generators are memory-efficient because they produce values one at a time, consuming only a small amount of memory regardless of the size of the generated sequence. This makes generators well-suited for tasks like processing large datasets or working with streams of data.

- Iterability: Generators are iterable, meaning you can use them in constructs like for loops or pass them to functions that expect iterable objects. Each iteration over a generator calls the generator's __next__() method implicitly, retrieving the next value from the generator.
'''
#13. What is closure in python .
'''
In Python, a closure is a function that retains the bindings of variables from the enclosing scope where it was defined, even after the outer scope has finished executing. This means that the closure can access and manipulate variables from the outer scope, even though the outer scope may no longer exist.

Here's a simple example to illustrate closures:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # Output: 15
'''
#14. How does the GIL affect the multi threaded python programs.
'''
The Global Interpreter Lock (GIL) is a mutex (lock) that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously. In other words, the GIL allows only one thread to execute Python bytecode at a time, even on multi-core systems. This can have several implications for multi-threaded Python programs:

- Limited Concurrency: Due to the GIL, multi-threaded Python programs cannot achieve true parallelism through CPU-bound tasks. Even if you have multiple CPU cores, only one Python thread can execute Python bytecode at a time. This limitation can lead to reduced performance for CPU-bound tasks in multi-threaded programs.

- IO-Bound Tasks: Python threads can still be beneficial for IO-bound tasks (tasks that spend most of their time waiting for I/O operations such as reading/writing files, network communication, etc.). In IO-bound scenarios, threads can perform other tasks while waiting for IO operations to complete, effectively utilizing system resources.

- Reduced Performance for CPU-Bound Tasks: For CPU-bound tasks, where computation is the bottleneck rather than IO, the GIL can lead to reduced performance. Since only one thread can execute Python bytecode at a time, multi-threading does not provide significant performance gains for CPU-bound tasks compared to single-threaded execution.

- Concurrency with External Libraries: The GIL does not prevent native threads from running concurrently in Python when executing code written in C or other compiled languages (such as NumPy operations, certain I/O operations, etc.). In such cases, the GIL is released by the Python interpreter, allowing true concurrency for those portions of the code.

- Alternative Approaches: To achieve true parallelism and utilize multiple CPU cores, Python developers often use multiprocessing or asynchronous programming with libraries like asyncio. These approaches involve running multiple Python processes or using cooperative multitasking (event loops) to achieve concurrency without the limitations of the GIL.
'''
#15. Difference between shallow copy and deep copy ?
'''
Shallow Copy:
A shallow copy creates a new object but does not recursively copy nested objects within the original object. Instead, it copies the references to the nested objects. As a result, changes made to nested objects in the copied object will also affect the original object, and vice versa.

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)

# Modify a nested object in the shallow copy
shallow_copy[0][0] = 0
print(original_list)  # Output: [[0, 2, 3], [4, 5, 6]]

Deep Copy:
A deep copy, on the other hand, recursively copies all objects within the original object, creating completely independent copies. Changes made to nested objects in the copied object will not affect the original object, and vice versa.

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original_list)

# Modify a nested object in the deep copy
deep_copy[0][0] = 0

print(original_list)  # Output: [[1, 2, 3], [4, 5, 6]]
'''
#16. Explain the purpose of __init__() in python classes.
'''
The __init__ method in Python classes is a special method used for initializing objects when they are created. It serves as a constructor for the class and is automatically called when an instance of the class is created. The purpose of the __init__ method is to initialize the attributes (properties) of the object to their initial values or to perform any other setup that needs to be done when the object is created.
'''
#17. What is Metaclasses in python. explain their usage.
'''
Metaclasses are classes that define the behavior of other classes. They are responsible for creating classes, just like classes are responsible for creating objects. In Python, everything is an object, including classes. Therefore, classes themselves are instances of metaclasses. They are often used in advanced scenarios where you need to alter the default behavior of class creation or perform some additional actions during class creation.
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add custom behavior here
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass
'''
#18. Describe the difference between __getattr__ and __getattribute__ in python.
'''
__getattr__(self, name): This method is called when an attribute lookup fails. It is invoked only if the attribute being accessed is not found through the usual lookup process. For example, if you try to access an attribute that does not exist, Python will call __getattr__ with the name of the attribute as an argument.
class MyClass:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

obj = MyClass()
print(obj.some_attribute)  # Output: Attribute 'some_attribute' not found

__getattribute__(self, name): This method is called for every attribute access on an instance of the class. It is invoked before looking at the instance's dictionary, even for existing attributes. This makes it more powerful but also more dangerous to use, as it can override access to all attributes, including built-in ones.
class MyClass:
    def __getattribute__(self, name):
        print(f"Accessing attribute '{name}'")
        # Avoid infinite recursion by using super()
        return super().__getattribute__(name)

obj = MyClass()
obj.some_attribute  # Output: Accessing attribute 'some_attribute'
'''
#19. How does the python manage memory .
'''
Python manages memory dynamically through a mechanism called "automatic memory management" or "garbage collection."
Some techniques involved in memory management are:
- Momory Allocation dynamically from heap
- Reference counting
- Garbage collection
and memory management optimisation
'''
#20. Discuss the concept of namespaces and scope resolution in python.
'''
Namespace is a mapping from names to objects. It serves as a container for variables, functions, classes, and other objects. Namespaces are used to organize and manage the names (or identifiers) used in a Python program, preventing naming conflicts and providing a way to access and reference objects.
- Local Namespace: The local namespace contains names that are defined within a function.
- Global Namespace: The global namespace contains names that are defined at the top level of a module or script.
- Built-in Namespace: The built-in namespace contains names of built-in functions, exceptions, and other objects that are available by default in Python.

Scope resolution refers to the process of determining the namespace in which a name is looked up and the order in which namespaces are searched to find the corresponding object. Python uses the LEGB rule to resolve names:

Local: Names are first looked up in the local namespace (local scope) of the current function.
Enclosing: If the name is not found in the local namespace, Python searches the enclosing namespaces (enclosing scopes) of any enclosing functions, from inner to outer.
Global: If the name is still not found, Python searches the global namespace (global scope) of the module or script.
Built-in: If the name is not found in the global namespace, Python finally searches the built-in namespace.
'''
#21. Explain the concept of decorator in python. Provide an example of how would you use it to measure the execution time of a function.
'''
Decorators in Python are a powerful and flexible feature that allows you to modify or extend the behavior of functions or methods without modifying their actual code. Decorators are functions that wrap around other functions or methods, adding additional functionality to them.
Here is an example of a decorator to measure the time of execution of a function:

import time
def decorator_function(func):
    def wrapper_function(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        duration = end - start
        print(f"Function {func.__name__} took {duration} to execute.")
        return result
    return wrapper_function

@decorator_function
def square(lst):
    res = []
    for i in lst:
        res.append(i**2)
    return res

@decorator_function
def cube(lst):
    res = []
    for i in lst:
        res.append(i**3)
    return res

lst = list(range(1000))
print(square(lst))
print(cube(lst))
'''
#22. What are metaclasses in Python? Provide a practical example where you would use a metaclass.
'''
In Python a metaclass is a class used to create other classes. It is also called as class of a class. It allows us to customize how classes are created and behave.
Suppose we want to create a framework where all subclasses of a particular base class should auto matically register themselves in a registry.

class RegistryMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[cls.__name__] = cls

class BaseClass(metaclass=RegistryMeta):
    pass
class SubClass1(BaseClass):
    pass
class SubClass2(BaseClass):
    pass
    
print(BaseClass.registry)
'''
#23. What is the purpose of the _slots_ attribute in Python classes? How does it affect memory usage and object initialization?
'''
The __slots__ attribute in Python classes is used to explicitly declare which attributes a class instance can have. 
Here's how it affects memory usage and object initialization:

Memory Usage: Without __slots__, each instance of a class in Python has a __dict__ attribute, which is a dictionary that stores all of the instance's attributes and their values. This dynamic nature of attribute storage can consume more memory, especially for instances with a large number of attributes.When you use __slots__, you're essentially preventing the creation of __dict__ for each instance. Instead, memory is allocated only for the attributes specified in __slots__. This can result in significant memory savings, especially when you have a large number of instances.

Object Initialization: When you define __slots__, Python generates more efficient accessor methods for accessing and setting attribute values. This can lead to slightly faster attribute access and modification compared to using __dict__.

few considerations to keep in mind when using __slots__:

You cannot add new attributes to instances at runtime unless they are listed in __slots__.
__slots__ can make code less flexible and harder to maintain if used incorrectly, especially if you need to dynamically add attributes to instances.

Here is an example of using __slot__
class Person:
    __slots__ = ['name', 'age']  # Only 'name' and 'age' attributes are allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Memory usage comparison
import sys

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(sys.getsizeof(p1))  # Size of p1 object
print(sys.getsizeof(p2))  # Size of p2 object

# Accessing attributes
print(p1.name)  # Output: Alice
print(p2.name)  # Output: Bob

# Uncommenting the following line will raise an AttributeError since 'city' is not in __slots__
# p1.city = "New York"
'''
#24. Explain the concept of context managers in Python and provide examples of built-in and custom context managers.
'''
Context managers in Python provide a way to manage resources (such as files, database connections, etc.) efficiently, ensuring that they are properly initialized and cleaned up when they are no longer needed, even in the presence of exceptions. They are commonly used with the 'with' statement.
The context manager protocol involves two methods: __enter__ and __exit__. When an object implements these methods, it can be used as a context manager.

Here's how it works:

__enter__: This method is called when entering the context (i.e., when the with statement is executed). It initializes the resource and returns it. The value returned by __enter__ is bound to the target variable after the as keyword in the with statement.

__exit__: This method is called when exiting the context (i.e., when the block inside the with statement completes execution). It performs any necessary cleanup actions, such as closing files or releasing resources. It also handles exceptions that occur within the context. If an exception is raised within the context, it is passed to __exit__, allowing the context manager to handle it gracefully.

# Using built-in context manager with a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!')

Now, let's create a custom context manager using the contextlib module:

from contextlib import contextmanager

@contextmanager
def my_context():
    # Code executed before entering the context
    print("Entering the context")
    
    try:
        # Yield control back to the caller
        yield
    finally:
        # Code executed after exiting the context
        print("Exiting the context")

# Using the custom context manager
with my_context():
    print("Inside the context")
'''
#25. Discuss the use of the async and await keywords in Python. When would you use asynchronous programming, and what are its benefits?
'''
The async and await keywords in Python are used to define asynchronous functions and manage asynchronous code execution. Asynchronous programming allows you to write code that can perform multiple tasks concurrently without blocking the execution of other code. This is particularly useful when dealing with I/O-bound operations, such as network requests, file I/O, or database queries, where the program would otherwise be waiting for a response.

async: This keyword is used to define a function as asynchronous. It indicates that the function will execute asynchronously and may contain await expressions.

await: This keyword is used inside an async function to await the result of another asynchronous function or coroutine. When await is used, it suspends the execution of the current coroutine until the awaited coroutine is complete and returns its result.

import asyncio

async def async_task():
    print("Task started")
    await asyncio.sleep(3)  # Simulate an asynchronous operation
    print("Task completed")

async def main():
    await async_task()
    print("Main function completed")

# Run the asynchronous main function
asyncio.run(main())
'''
#26. What are some common design patterns used in Python? Provide examples of when you would use each pattern.
'''
Python supports various design patterns that help organize and structure code in a way that enhances readability, maintainability, and reusability.
Here are some common design patterns in Python:

1. Singleton Pattern:
Description: Ensures that a class has only one instance and provides a global point of access to that instance.

Example: Used for logging, database connections, or configuration settings.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

2. Factory Pattern:
Description: Creates objects without exposing the instantiation logic to the client and refers to the newly created object through a common interface.

Example: Used to create instances of different subclasses based on some criteria.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()

factory = AnimalFactory()
dog = factory.get_animal('dog')
cat = factory.get_animal('cat')
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

3. Observer Pattern:
Description: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

Example: Used in event handling systems, GUI frameworks, or publisher-subscriber models.

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, value):
        for observer in self._observers:
            observer.update(value)

class Observer:
    def update(self, value):
        print("Received value:", value)

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify(42)

4. Decorator Pattern:
Description: Allows behavior to be added to objects dynamically without affecting their behavior. It wraps an object to extend its functionality.

Example: Used for adding logging, caching, or authorization to functions or methods.

def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(3, 4))  # Output: Calling add with args: (3, 4), kwargs: {}, 7
'''
#27. Discuss the use of Python's multiprocessing module for parallel computing. How does it differ from the threading module, and when would you choose one over the other.
'''
Python's multiprocessing module provides a way to create processes, which are separate instances of the Python interpreter, to achieve parallelism. Each process runs in its own memory space, allowing true parallel execution of code. This is in contrast to the threading module, which provides threads, which are lighter-weight than processes and share the same memory space.

1. Parallelism vs. Concurrency:
- multiprocessing achieves parallelism by running multiple processes simultaneously, each with its own memory space. This allows CPU-bound tasks to be executed concurrently on multiple CPU cores.

- threading achieves concurrency by running multiple threads within the same process, sharing the same memory space. This is more suitable for I/O-bound tasks where threads can perform non-blocking I/O operations simultaneously.

2. Global Interpreter Lock (GIL):
- Python's Global Interpreter Lock (GIL) restricts the execution of multiple threads within the same process to run concurrently. This means that in a multi-threaded Python program, only one thread can execute Python bytecode at a time. Therefore, threading is not effective for CPU-bound tasks that require true parallelism.

- multiprocessing, on the other hand, bypasses the GIL by running separate processes, allowing true parallel execution of CPU-bound tasks on multiple CPU cores.

3. Memory Overhead:
- Creating processes using multiprocessing incurs more memory overhead compared to creating threads using threading. This is because each process has its own memory space.

- threading is more lightweight in terms of memory usage because threads within the same process share memory.

4. When to Choose:
- Use multiprocessing when you need true parallelism for CPU-bound tasks, such as intensive mathematical computations or data processing tasks that can be split into smaller chunks.
- Use threading when you need concurrency for I/O-bound tasks, such as network requests, file I/O, or database operations, where threads can perform non-blocking I/O operations simultaneously.
'''