"""Linear search is a sequential searching algorithm where we start from one end and check every element of the list
until the desired element is found. It is the simplest searching algorithm."""

# Linear Search in Python

# Time Complexity: O(n)
# Space Complexity: O(1)


def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)
