"""
Given an array of n integers. The task is to find all elements that have more than one occurrences. The output should only one occurrence of a number irrespective of number of occurrences in the input array.

Examples: 

Input: {2, 10, 10, 100, 2, 10, 11, 2, 11, 2}
Output: {2, 10, 11}

Input: {5, 40, 1, 40, 100000, 1, 5, 1}
Output: {5, 40, 1}

"""

# Time Complexity: O(n^2)
# Space Complexity: O(n)

def find_duplicates(arr):
    res = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in res:
                    res.append(arr[i])
                break  

    return res


arr= [2, 10, 10, 100, 2, 10, 11, 2, 11, 2]

print(find_duplicates(arr)) 
