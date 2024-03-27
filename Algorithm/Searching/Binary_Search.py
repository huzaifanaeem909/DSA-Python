"""Binary Search is a searching algorithm for finding an element's position in a sorted array.
In this approach, the element is always searched in the middle of a portion of an array.
Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.

Binary Search Algorithm can be implemented in two ways which are discussed below.
1. Iterative Method
2. Recursive Method
The recursive method follows the divide and conquer approach.
"""

""" 
Time Complexities:
# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)

Space Complexity: O(1).
"""

# Binary Search in python (Iterative Method):


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


# Binary Search in python (Recursive Method):


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low) // 2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
