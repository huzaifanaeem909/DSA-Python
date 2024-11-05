"""
Given a array arr[] of integers and an integer sum. You mainly need to return the left and right indexes of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

Examples: 

Input: arr[] = { 15, 2, 4, 8, 9, 5, 10, 23}, sum = 23
Output: 1 4
Explanation: Sum of elements between indices 1 and 4 is 2 + 4 + 8 + 9 = 23


Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Output: 1 4
Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7


Input: arr[] = {1, 4}, sum = 0
Output: -1
Explanation: There is no subarray with 0 sum
"""


# Time complexity: O(n)
# Auxiliary Space: O(1)
def find_subarray(arr, n, sum):

    start, last = 0, 0  # Initialize pointers for start and end of subarray
    curr_sum = 0
    res = []
    flag = False

    # Loop through the array
    for i in range(n):
        curr_sum += arr[i]

        # Check if current sum is greater than or equal to given number
        if curr_sum >= sum:
            last = i

            # Start from starting index till current index
            while sum < curr_sum and start < last:
                curr_sum -= arr[start]  # Subtract element at start
                start += 1

            # If current sum becomes equal to given number
            if curr_sum == sum:
                res.append(start)
                res.append(last)
                # res = arr[start:last + 1]  # To return the SubArray with required Sum
                flag = True
                break

    # If no subarray is found, return -1
    if not flag:
        res.append(-1)

    return res


arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23
print(find_subarray(arr, n, sum))
