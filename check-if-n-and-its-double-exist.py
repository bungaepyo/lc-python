'''
------------------
Difficulty: Easy
------------------

Given an array arr of integers, check if there exist two indices i and j such that:

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 
Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
'''

'''
------------------------------------------------------------------------
Solution 1 - One Pass (map/array/set)
Time: O(N)
Space: O(1)

Runtime: 45 ms
Memory: 13.3 MB

This is a one-pass solution using anything among these: map, array, set.
Since the array is not sorted, in order to check if the double of N exists,
we need to check if N*2 exists or N/2 exists. If it doesn't simply add N.

Checking N*2 is relatively simple since all positive integers except for 0
will become an even integer when doubled. However, we need to check if N
is an even integer when checking N/2 because odd integer / 2 will be a float,
not an int.
------------------------------------------------------------------------
'''
class Solution(object):
    def checkIfExist(self, arr):
        li = []
        
        for num in arr:
            if num*2 in li or num%2 == 0 and num/2 in li:
                return True
            li.append(num)

        return False