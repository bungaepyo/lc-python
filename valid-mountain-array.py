'''
------------------
Difficulty: Easy
------------------

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: One Pass
Time: O(n)
Space: O(1)

Runtime: 364 ms
Memory: 14.7 MB

This is a one pass solution that basically emulates the mountain climb.
  - (1) first, we climb the mountain and check if index is in bound, and numbers are increasing
  - (2) second, we check if peak is either first or last number
  - (3) third, we climb down the mountain with the same checks as (1)

After the iteration, if it's a valid mountain array, the index should be len(arr)-1
------------------------------------------------------------------------
'''
class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False

        lastIndex = len(arr)-1
        index = 0
        
        #go up
        while index+1 <= lastIndex and arr[index] < arr[index+1]:
            index += 1

        #index cannot be first or last (ever increasing/decreasing)
        if index == 0 or index == lastIndex:
            return False
        
        #go down
        while index+1 <= lastIndex and arr[index] > arr[index+1]:
            index += 1
        
        #index should be len(arr)-1 after full iteration
        return index == lastIndex

'''
------------------------------------------------------------------------
Solution 2: One Pass - simplified
Time: O(n)
Space: O(1)

Runtime: 294 ms
Memory: 14.8 MB

This is an extremely simplified version of the one pass solution above.
Basically, in this solution, we use different index pointers for climbing
up and down, with the same constraints.
At the end of the iterations, we check if i and j are equal to each other
and they are both in bounds (a.k.a checking if peak is first or last).
------------------------------------------------------------------------
'''
class Solution(object):
    def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1