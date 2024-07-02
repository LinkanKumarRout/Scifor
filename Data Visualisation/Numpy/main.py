import numpy as np # importing numpy module

# Creation of 0-D array
arr = np.array(24)
print(arr) # prints the array
print('Datatype: ',arr.dtype) # prints the data type of elements in the array
print('Total no of elements: ',arr.size) # prints the total number of elements in the array
print('Dimension of array: ',arr.ndim) # prints dimension of the array
print('Shape of array(row & column): ',arr.shape) # prints shape of the array (rows and columns)

# Creation of 1-D array
arr = np.array([10,20,30,40,50])
print(arr)
print('Datatype: ',arr.dtype)
print('Total no of elements: ',arr.size)
print('Dimension of array: ',arr.ndim)
print('Shape of array(row & column): ',arr.shape)

# Creation of 2-D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print('Datatype: ',arr.dtype)
print('Total no of elements: ',arr.size)
print('Dimension of array: ',arr.ndim)
print('Shape of array(row & column): ',arr.shape)

# Creation of 3-D array
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(arr)
print('Datatype: ',arr.dtype)
print('Total no of elements: ',arr.size)
print('Dimension of array: ',arr.ndim)
print('Shape of array(row & column): ',arr.shape)

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

# Iterating on Array

# iterating on 1-D array
arr = np.array([1,2,3,4,5])
for i in arr:
  print(i)

#iterating on 2-D array
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
  for j in i:
    print(j)

# iterating on 3-D array
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in arr:
  for j in i:
    for k in j:
      print(k)

# Functions in numpy

import numpy as np

# numpy.array(): Create an array from a Python list or tuple
arr1 = np.array([1, 2, 3])
print(arr1)

# numpy.zeros(): Create an array filled with zeros
arr2 = np.zeros((2, 3))
print(arr2)

# numpy.ones(): Create an array filled with ones
arr3 = np.ones((3, 2))
print(arr3)

# numpy.arange(): Create an array with evenly spaced values within a specified range
arr4 = np.arange(0, 10, 2)
print(arr4)

# numpy.linspace(): Create an array with evenly spaced values over a specified interval
arr5 = np.linspace(0, 1, 5)
print(arr5)

# numpy.random.rand(): Create an array of random numbers from a uniform distribution
arr6 = np.random.rand(2, 3, 4)
print(arr6)

# numpy.random.randn(): Create an array of random numbers from a standard normal distribution
arr7 = np.random.randn(2, 3, 5)
print(arr7)

# numpy.random.randint(): Create an array of random integers within a specified range
arr8 = np.random.randint(0, 10, size=(2, 3))
print(arr8)

# numpy.reshape(): Reshape an array
arr = np.arange(12)
reshaped_arr = np.reshape(arr, (3, 4))
print(reshaped_arr)

# numpy.concatenate(): Concatenate arrays along a specified axis
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7,8]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print(concatenated_arr)

# numpy.vstack(): Stack arrays vertically (row-wise)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked_arr = np.vstack((arr1, arr2))
print(stacked_arr)

# numpy.hstack(): Stack arrays horizontally (column-wise)
arr1 = np.array([[1], [2], [3]])
arr2 = np.array([[4], [5], [6]])
stacked_arr = np.hstack((arr1, arr2))
print(stacked_arr)

# numpy.split(): Split an array into multiple sub-arrays
arr = np.arange(10)
split_arr = np.split(arr, [3, 7])
print(split_arr)

# numpy.transpose(): Transpose an array
arr = np.array([[1, 2], [3, 4]])
transposed_arr = np.transpose(arr)
print(transposed_arr)

# numpy.flip(): Reverse the order of elements along a specified axis
arr = np.array([1, 2, 3, 4, 5])
flipped_arr = np.flip(arr)
print(flipped_arr)

# numpy.roll(): Roll array elements along a specified axis
arr = np.array([1, 2, 3, 4, 5])
rolled_arr = np.roll(arr, 2)
print(rolled_arr)

# numpy.sum(): Compute the sum of array elements
arr = np.array([1, 2, 3])
sum_arr = np.sum(arr)
print(sum_arr)

# numpy.mean(): Compute the mean of array elements
arr = np.array([1, 2, 3])
mean_arr = np.mean(arr)
print(mean_arr)

# numpy.median(): Compute the median of array elements
arr = np.array([1, 2, 3])
median_arr = np.median(arr)
print(median_arr)

# numpy.min(), numpy.max(): Compute the minimum and maximum values of an array
arr = np.array([1, 2, 3])
min_val = np.min(arr)
max_val = np.max(arr)
print(min_val, max_val)

# numpy.std(): Compute the standard deviation of array elements
arr = np.array([1, 2, 3])
std_dev = np.std(arr)
print(std_dev)

# numpy.var(): Compute the variance of array elements
arr = np.array([1, 2, 3])
variance = np.var(arr)
print(variance)

# numpy.dot(): Compute the dot product of two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
dot_product = np.dot(arr1, arr2)
print(dot_product)

# numpy.cross(): Compute the cross product of two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
cross_product = np.cross(arr1, arr2)
print(cross_product)