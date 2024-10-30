"""
Given an array arr. Find the majority element in the array. If no majority exists, return -1. A majority element in an array is an element that appears strictly more than arr.size() / 2 times in the array.

Examples : 

Input : arr[] = {1, 1, 2, 1, 3, 5, 1}
Output : 1
Explanation: Note that 1 appear 4 times which is more than  7 / 2 times 


Input : arr[] = {3, 3, 4, 2, 4, 4, 2, 4}
Output :  -1 
Explanation: There is no element whose frequency is greater than the half of the size of the array size.


Input : arr[] = {3}
Output : 3
Explanation: Appears more than n/2 times
"""

# Time Complexity: O(n^2)
# Auxiliary Space Complexity: O(1)


def majorityElement(arr):
    n = len(arr)

    # Iterate through each element in the array
    for i in range(n):
        count = 0

        # Compare the current element with every other element
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        # Check if count is greater than half the size of the array
        if count > n // 2:
            return arr[i]

    return -1


arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(majorityElement(arr))
