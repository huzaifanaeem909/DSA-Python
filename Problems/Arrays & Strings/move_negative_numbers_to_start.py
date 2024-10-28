"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Move all negative numbers to beginning and positive to end with constant extra space

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""


# Time Complexity: O(n)
# Space Complexity: O(1)

def reArrange(array, n):
    low,high = 0, n - 1
    while(low<high):
        if(array[low] < 0):
            low += 1
        elif(array[high] > 0):
            high -= 1
        else:
            array[low],array[high] = array[high],array[low]

    return array

array = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(array)
print(reArrange(array, n))


# Alternative Solution
def Re_Arrange_Array(arr, left, right):

    # Loop until the two pointers meet
    while left <= right:

        # Both elements are negative, move the left pointer
        if arr[left]<0 and arr[right]<0:
            left += 1

        # Left is positive and right is negative, swap them and move both pointers
        elif arr[left]>0 and arr[right]<0:
            arr[left], arr[right] = arr[right],arr[left]
            left += 1
            right -= 1

        # Both elements are positive, move the right pointer
        elif arr[left]>0 and arr[right]>0:
            right-=1

        # Properly placed negative at left and positive at right, move both pointers
        else:
            left+=1
            right-=1

    return arr
        
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
print(Re_Arrange_Array(arr, 0, n-1))
