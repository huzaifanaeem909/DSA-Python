"""
Given an array arr[] of size n-1 with integers in the range of [1, n], the task is to find the missing number from the first N integers.
Note: There are no duplicates in the list.

Examples: 

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
"""

def find_missing(arr):
    min_val = min(arr)
    max_val = max(arr)
    
    # Expected sum of the sequence from min_val to max_val
    expected_sum = sum(range(min_val, max_val + 1))
    
    # Actual sum of the elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage
arr = [3, 6, 5, 4, 8]
print(f"The missing number is: {find_missing(arr)}")
