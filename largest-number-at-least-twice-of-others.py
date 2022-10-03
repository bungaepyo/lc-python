'''
------------------
Difficulty: Easy
------------------

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pass
Time: O(n)
Space: O(1)

Runtime: 24 ms
Memory: 13.5 MB

This is an intuitive two pass solution. Edge case: if length of nums is less than
2, there will be no second largest element to compare, thus return -1.

In our first pass, we find the maxmimum value and its index.
In our second pass, we seek for a counterexample where number*2 would exceed maximum.
If we find a counterexample, return -1.
------------------------------------------------------------------------
'''
class Solution(object):
    def dominantIndex(self, nums):
        if len(nums) <= 1:
            return -1
        
        # one pass -> find largest
        idx = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
                idx = i
        
        # two pass -> seek counterexample
        for j in range(len(nums)):
            if j == idx:
                continue
            if maximum < nums[j]*2:
                return -1
        
        return idx

'''
------------------------------------------------------------------------
Solution 2: One Pass
Time: O(n)
Space: O(1)

Runtime: 42 ms
Memory: 13.3 MB

This is a one pass solution that slightly improves the first two pass solution.
Using the build in max() functino for python arrays, we can easily find
what is the maximum number in nums.

In our one pass:
  - if we find the maximum value, we record its index
  - otherwise, we constantly compare val*2 > maximum to find counterexamples.
------------------------------------------------------------------------
'''
class Solution(object):
    def dominantIndex(self, nums):
        if len(nums) <= 1:
            return -1
        
        maximum = max(nums)
        maxIndex = -1
        
        for idx, val in enumerate(nums):
            if val == maximum:
                maxIndex = idx
                continue
            if val*2 > maximum: return -1 
        
        return maxIndex