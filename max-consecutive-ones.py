'''
------------------
Difficulty: Easy
------------------

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

'''
------------------------------------------------------------------------
Solution 1 - One Pass
Time: O(N)
Space: O(1)

Runtime: 592 ms
Memory: 13.6 MB

This is a pretty straightforward one-pass solution to find the max consecutive
ones. We keep a local sum and a global sum to keep track of currently held
consecutive ones, and historically largest number of consecutive ones.
While iterating nums:
  - whenever we encounter 1, we add to current sum and try updating global sum.
  - whenever we encounter non-1, we set current sum to 0.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                res = max(curr, res)
            else:
                curr = 0
        return res

'''
------------------------------------------------------------------------
Solution 2 - One Pass (variation)
Time: O(N)
Space: O(1)

Runtime: 652 ms
Memory: 13.6 MB

This is just a slight variation from the first solution. Instead of updating
the max_count when we find a 1, we do it when we find a non-1. In this case,
you would have to return max(max_count, count) because the last element of the
nums array might not be a non-1, not triggering an update for max_count.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)