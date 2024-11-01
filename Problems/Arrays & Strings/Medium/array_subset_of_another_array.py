"""
Given two arrays arr1[] and arr2[] of size m and n respectively, the task is to determine whether arr2[] is a subset of arr1[]. Both arrays are not sorted, and elements are distinct.

Examples: 

Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: Yes

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
Output: Yes

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
Output: No
"""

# Time Complexity: O(m*n)
# Auxiliary Space: O(1)

def is_subset(arr1, arr2):
    m, n = len(arr1), len(arr2)
    for i in range(n):
        found = False
        for j in range(m):
            if arr2[i] == arr1[j]:
                found = True
                break
        if not found:
            return False
    return True


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

if is_subset(arr1, arr2):
    print("Yes")
else:
    print("No")
    