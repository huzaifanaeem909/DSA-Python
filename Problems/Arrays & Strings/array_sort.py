"""
Given a random set of numbers, Print them in ascending sorted order.
Example 1:
Input:
n = 4
arr[] = {1, 5, 3, 2} --> Output: {1, 2, 3, 5}
"""

# Time Complexity: O(n2)
# Auxiliary Space: O(1)


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # keep track of swapping
        swapped = False

        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


def print_sorted_numbers(arr):
    bubble_sort(arr)
    print("Output:", arr)


arr = [1, 5, 3, 10, 8, 4, 9, 2]
print("Input:", arr)
print_sorted_numbers(arr)
