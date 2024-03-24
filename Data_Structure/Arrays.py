"""An array is a collection of items of the same variable type that are stored at contiguous memory locations. 
Each item in an array is indexed starting with 0."""

arr1 = [10, 20, 30]  # This array will store integer
arr2 = ["c", "d", "e"]  # This array will store characters
arr3 = [28.5, 36.5, 40.2]  # This array will store floating elements

from numpy import *

# add 5 to each element
arr = array([1, 2, 3, 4, 5])
arr = arr + 5
print(arr)

# Adding to array
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 2, 3, 4, 5])
arr3 = arr1 + arr2
print(arr3)

# Sin of the array
arr1 = array([1, 2, 3, 4, 5])
print(sin(arr1))

# Cos of the array
arr1 = array([1, 2, 3, 4, 5])
print(cos(arr1))

# Log of the array
arr1 = array([1, 2, 3, 4, 5])
print(log(arr1))

# Sqrt of the array
arr1 = array([1, 2, 3, 4, 5])
print(sqrt(arr1))

# Sum of the array
arr1 = array([1, 2, 3, 4, 5])
print(sum(arr1))

# To find min value
arr1 = array([1, 2, 3, 4, 5])
print(min(arr1))

# To find max value
arr1 = array([1, 2, 3, 4, 5])
print(max(arr1))

# concatenate array
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 2, 9, 4, 5])

print(concatenate([arr1, arr2]))


# Shallow copy
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.view()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

# deep copy
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.copy()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

# matrix array

arr1 = array(
    [
        [1, 2, 3, 6],
        [4, 5, 6, 3],
    ]
)

# This can print type of data (int32) arr1
print(arr1.dtype)

# Count dim on array
print(arr1.ndim)

# Give row and col (2,4)
print(arr1.shape)

# Give the size of matrix (8)
print(arr1.size)

# convert 2d array in to 1d
arr2 = arr1.flatten()
print(arr2)
arr2 = arr1.flatten()

# Convert the matrix has given (2,4)
arr4 = arr2.reshape(2, 4)
arr3 = arr2.reshape(2, 4)
print(arr3)
print("")
print(arr4)

# Martices (don't need arr1)
m = matrix("1 2 3; 6 4 5; 6 7 9")

# print diagonal of matrix
print(diagonal(m))

# print max val of matrix
print(m.max())
print(m)

# Add matrix and multiply it
m1 = matrix("1 2 3; 6 4 5; 6 7 9")
m2 = matrix("1 4 3; 6 2 5; 5 7 9")

m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)
