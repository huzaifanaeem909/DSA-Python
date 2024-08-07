""" Given an array arr[] of size N and a number K, where K is smaller than the size of the array. 
Find the K'th smallest element in the given array. Given that all array elements are distinct.
Examples:  
Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
Output: 10 """

# Time Complexity: O(N log N)
# Auxiliary Space: O(1)


def Kth_Smallest(arr, N, k):
    # Sort the given array
    arr.sort()
    # Return k'th element in the sorted array
    return arr[k - 1]


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    N = len(arr)
    k = 3
    print("K'th smallest element is", Kth_Smallest(arr, N, k))
