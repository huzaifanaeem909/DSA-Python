""" Given an array (or string), the task is to reverse the array/string.
Input: original_array[] = {4, 5, 1, 2}
Output: array_reversed[] = {2, 1, 5, 4} """

# Array Reverse Using an Extra Array:

# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n) --> (Additional space is used to store the new array.)


def reverse_array(original_arr):
    reverse_array = []
    for i in range(len(original_arr) - 1, -1, -1):
        reverse_array.append(original_arr[i])
    return reverse_array


original_arr = [4, 5, 1, 2, 8, 9]
reversed_arr = reverse_array(original_arr)
print("Original Array:", original_arr)
print("Reversed Array:", reversed_arr)


# Array Reverse Using a Loop (In-place):


# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1) --> (In-place reversal, meaning it doesn’t use additional space.)


def reverse_arr(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5]
reverse_arr(arr)
print(arr)


# Recursive python program to reverse an array:


def reverse_arr(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_arr(arr, start + 1, end - 1)


arr = [4, 5, 1, 2, 8, 9]
reverse_arr(arr, 0, 5)
print("Reversed Array is", arr)
