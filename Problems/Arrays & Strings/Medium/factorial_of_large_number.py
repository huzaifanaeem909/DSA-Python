"""
Given an array containing intergers write a function to find and return the factorial of the highest number in the array.
"""

# Time Complexity: O(n+m)
# Auxiliary Space: O(1)


def factorial_of_highest(arr):
    if not arr:
        return None  # Handle empty array case

    # Find the highest number in the array
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num

    # Calculate the factorial of the highest number
    fact = 1
    for i in range(1, max_num + 1):
        fact *= i

    return fact


# Example array
arr = [2, 4, 6, 1, 5, 3]
print(
    f"The factorial of the highest number in the array is: {factorial_of_highest(arr)}"
)
