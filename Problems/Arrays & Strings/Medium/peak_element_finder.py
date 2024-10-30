"""
Find a peak element which is not smaller than its neighbours.
Example:
Input: array[]= {5, 10, 20, 15}
Output: 20
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 or 90
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.
"""

# Time complexity: O(n)
# Auxiliary Space: O(1)


def findPeak(arr, n):
    peak_values = []

    # first or last element is peak element
    if n == 1:
        peak_values.append(arr[0])
    if arr[0] >= arr[1]:
        peak_values.append(arr[0])
    if arr[n - 1] >= arr[n - 2]:
        peak_values.append(arr[n - 1])

    # check for every other element
    for i in range(1, n - 1):

        # check if the neighbors are smaller
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            peak_values.append(arr[i])

    return peak_values


arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)
peak_values = findPeak(arr, n)
print("Peak elements are", peak_values)
