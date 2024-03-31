"""
Program to find the minimum (or maximum) element of an array.
Given an array, write functions to find the minimum and maximum elements in it. 
"""

# Time Complexity: O(n)
# Auxiliary Space: O(1)


# We can also use in-built max() and min() function.
# Maximum Function
def getMax(arr, n):
    max_element = 0
    for i in range(0, n):
        if max_element < arr[i]:
            max_element = arr[i]
    return max_element


# Minimum Function
def getMin(arr, n):
    min_element = arr[0]
    for i in range(1, n):
        if min_element > arr[i]:
            min_element = arr[i]
    return min_element


arr = [128, 1234, 45, 67, 1]
n = len(arr)
print("Maximum element of array:", getMax(arr, n))
print("Minimum element of array:", getMin(arr, n))


# Another Solution:

# Time complexity : O(n log(n))
# Auxiliary Space : O(1)

a = [1, 423, 6, 46, 34, 23, 13, 53, 4]

# Sort the array using the built-in sorted() function
a_sorted = sorted(a)
print(a_sorted)

min_value = a_sorted[0]
max_value = a_sorted[-1]

print(f"min-{min_value}, max-{max_value}")
