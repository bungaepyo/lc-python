'''
------------------
Difficulty: Easy
------------------

Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits. 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1 - One Pass, String representation
Time: O(N)
Space: O(1)

Runtime: 39 ms
Memory: 13.6 MB

This is a fairly straightforward one pass solution using the list() technique.
The most intuitive way to see if each number in the nums array has even number of digits is,
transforming the number into a string (since an integer is not iterable) and see if the length is an even number.
If remainder is 0 when using %2, add 1 to the result count.
------------------------------------------------------------------------
'''
class Solution(object):
    def findNumbers(self, nums):
        res = 0
        
        for num in nums:
            li = list(str(num))
            digits = len(li)
            isEven = digits % 2 == 0
            if isEven:
                res += 1

        return res