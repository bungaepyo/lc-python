'''
------------------
Difficulty: Easy
------------------

Given an array arr, replace every element in that array with the greatest element 
among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0. 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1 - One Pass Backwards
Time: O(N)
Space: O(1)

Runtime: 118 ms
Memory: 14.9 MB

This is a one-pass solution that iterates the array backwards. Since we are
updating arr[i] with the biggest element on right side, it is intuitive to
start from the back and keep updating the greatest so far.
One thing to keep in mind here is to save the current arr[i] on a variable
before updating arr[i] with maxRight & updating maxRight, since it might be
overridden.
------------------------------------------------------------------------
'''
class Solution(object):
    def replaceElements(self, arr):
        maxRight = 0
        
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = maxRight
            maxRight = max(maxRight, temp)
        
        return arr