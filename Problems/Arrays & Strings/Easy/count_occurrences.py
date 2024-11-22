"""
Count number of occurrences (or frequency) in a sorted array.
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. 
Expected time complexity is O(Logn).
    Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
    Output: 4 // x (or 2) occurs 4 times in arr[]
    Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
    Output: 1 
    Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
    Output: -1 // 4 doesn't occur in arr[]
"""

# Time Complexity: O(n)
# Space Complexity: O(1)


def countOccurrences(arr, n, x):
    result = 0
    for i in range(0, n):
        if x == arr[i]:
            result += 1
    return result


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    n = len(arr)
    x = 2  # Element to be counted in arr[]
    print(x, "occurs", countOccurrences(arr, n, x), "times")
