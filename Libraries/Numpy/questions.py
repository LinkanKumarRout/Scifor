#1. What is Numpy and what are it's main feature ?
'''
Numpy is a python library for numerical computing. it provide's support of large, multi-dimensional arrays and matrices, along with a collection of mathematical functions. it is widely used in scientific computing, data analysis, machine learning etc.
'''
#2. Explain a difference between a python list and a numpy array ?
'''
Python lists and NumPy arrays are both used to store collections of elements, but they have some key differences:
- Homoginity: python list can have homogeneous or heterogeneous elements but numpy array can only contain homogeneous elements.

- Memory efficiency: python list are generally slower as comapred to numpy array for mathematical computation for large data set.
'''
#3. How do you create numpy array ?
'''
There are several functions for creating numpy arrays.

- array()
- zeros()
- ones()
- linspace()
- arange()
- random.randn()
- random.randint() etc.
'''
#4. What is the purpose of braodcasting in numpy ?
'''
Broadcasting in NumPy is a powerful mechanism that allows arrays with different shapes to be combined or operated on together in element-wise operations. It simplifies the syntax for performing arithmetic, comparison, and other operations on arrays of different shapes without the need for explicit looping or reshaping.
Example - 
import numpy as np

# Create a 3x3 array
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Create a 1x3 array
y = np.array([10, 20, 30])

# Perform element-wise addition between the arrays using broadcasting
result = x + y

print("Array x:")
print(x)
print("\nArray y:")
print(y)
print("\nResult of broadcasting:")
print(result)
'''
#5. How do you perform element wise operation in numpy ?
'''
In NumPy, element-wise operations are performed by applying a function or operator to each element of one or more arrays independently.

- Using Arithmetic Operators:

import numpy as np
# Create NumPy arrays
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
# Element-wise addition
result_addition = x + y
# Element-wise subtraction
result_subtraction = x - y
# Element-wise multiplication
result_multiplication = x * y
# Element-wise division
result_division = x / y

- Using NumPy Functions:

import numpy as np
# Create NumPy arrays
x = np.array([1, 2, 3, 4])
# Element-wise square root
result_sqrt = np.sqrt(x)
# Element-wise exponential
result_exp = np.exp(x)
# Element-wise sine
result_sin = np.sin(x)

- Using Comparison Operators:

import numpy as np
# Create NumPy arrays
x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])
# Element-wise comparison (greater than)
result_greater_than = x > y
# Element-wise comparison (less than)
result_less_than = x < y
# Element-wise comparison (equal)
result_equal = x == y

- Using Broadcasting:

import numpy as np
# Create NumPy arrays
x = np.array([[1, 2, 3],
              [4, 5, 6]])
# Element-wise addition with broadcasting
result_broadcasting = x + 10
'''
#6. Explain the difference between np.zeros, np.ones, and np.empty functions in NumPy ?
'''
import numpy as np

- np.zeroes()
- it wll create an array filled with zeroes
- arr = np.zeroes(shape)

- np.ones()
- This will create an array filled with ones.
- np.ones(shape)

- np.empty()
- This will create an array without intializing its value.
- np.empty(shape)
'''
#7. Describe the difference between slicing and indexing in numpy array ?
'''
In numpy indexing means fething only one element using its index number while slicing means fething multiple elements at a time usinf start and end index number.

import numpy as np
# Indexing of Array

# Indexing is not possible in 0-D array
# Indexing in 1-D array
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[-1])

#Indexing in 2-D array
arr = np.array([[1,2,3],[4,5,6]])
print(arr[0, 0])
print(arr[1,2])
print(arr[-1, -1])

# indexing in 3-D array
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(arr[1,0,2])
print(arr[0,1,0])
print(arr[-1,-1,-1])

# Slicing of Array

# slicing is not possible in 0-D array
# slicing in 1-D array
arr = np.array([10,20,30,40,50])
print(arr[1:3])
print(arr[-1:])
print(arr[2:])

# slicing in 2-D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0][1:3])
print(arr[1][-1::-1])
print(arr[-1][1:])

# slicing in 3-D array
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(arr[0][0][1:])
print(arr[1][1][:2])
'''
#8. How do you perform matrix multiplication usingnumpy ?
'''
In NumPy, we can perform matrix multiplication using the numpy.dot() function or the @ operator. The numpy.dot() function can perform both dot product and matrix multiplication, while the @ operator is specifically designed for matrix multiplication.

import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Perform matrix multiplication using numpy.dot()
result_dot = np.dot(A, B)
print("Result of matrix multiplication using numpy.dot():")
print(result_dot)

# Perform matrix multiplication using @ operator
result_operator = A @ B
print("Result of matrix multiplication using @ operator:")
print(result_operator)
'''
#9. What is the purpose of np.random() in numpy ?
'''
numpy.random module is used to create an array where elements are randomly picked from a distribution or a list.

# numpy.random.rand(): Create an array of random numbers from a uniform distribution
arr6 = np.random.rand(2, 3, 4)
print(arr6)

# numpy.random.randn(): Create an array of random numbers from a standard normal distribution
arr7 = np.random.randn(2, 3, 5)
print(arr7)

# numpy.random.randint(): Create an array of random integers within a specified range
arr8 = np.random.randint(0, 10, size=(2, 3))
print(arr8)
'''
#10. How do you save and load numpy array from the disk ?
'''
There are several functions that we can use to save our numpy array into our disk.

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

np.save('array.npy', arr1) # save an array in .npy format
np.savez('array.npz', arr1 = arr1, arr2 = arr2) # save multiple array in .npz format
np.savetxt('array.txt',arr1) # save array as a text file

# Load an array
data = np.load('array.npz')
arr1 = data['arr1']
arr2 = data['arr2']
print(arr1, arr2)
or
data = np.load('array.npy)
print(data)
or
data = np.loadtxt('array.txt')
print(data)
'''