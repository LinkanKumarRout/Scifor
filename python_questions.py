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