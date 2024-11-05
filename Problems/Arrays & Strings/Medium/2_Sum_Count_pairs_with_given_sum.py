"""
Given an array arr[] of n integers and a target value, the task is to find the number of pairs of integers in the array whose sum is equal to target.

Examples:  

Input: arr[] = {1, 5, 7, -1, 5}, target = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input: arr[] = {1, 1, 1, 1}, target = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).

Input: arr[] = {10, 12, 10, 15, -1}, target = 125
Output:  0

"""

# Method 1:

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


def count_pairs(arr, target):
    n = len(arr)
    count = 0

    # Iterate through each element in the array
    for i in range(n):

        # For each element arr[i], check every other element
        for j in range(i + 1, n):

            # If the sum of arr[i] and arr[j] is equal to target, increment the count
            if arr[i] + arr[j] == target:
                count += 1

    return count


arr = [1, 5, 7, -1, 5]
target = 6
print(count_pairs(arr, target))


# Method 2:

# Time Complexity: O(n)
# Auxiliary Space: O(1)


def countpairs(arr, target):
    freq = {}
    cnt = 0
    n = len(arr)

    for i in range(n):
        
        if (target - arr[i]) in freq:
            cnt += freq[target - arr[i]] 
        
        freq[arr[i]] = freq.get(arr[i], 0) + 1 

    return cnt

arr = [1, 5, 7, -1, 5]
target = 6
print(countpairs(arr, target))
