'''
------------------
Difficulty: Medium
------------------

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0 

Constraints:
å
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Sliding Window
Time: O(n)
Space: O(1)

Runtime: 239 ms
Memory: 23.6 MB

This is a solution using the sliding window technique, essentially a two pointers approach.
We first initialize a cumulative minimum, current sum, and a left pointer.
The right pointer will just be the index during the for loop iteration.
In our one pass iteration, each time we calculate the current sum by adding the current element
i is pointing to. This is equivalent to expanding the window.
Then, whenever current sum becomes greater than or equal to target, update
the cumulative minimum and start shrinking the window until it becomes
smaller than target eventually.
This way, we are able to cover all possible windows of different sizes
whose sum is >= target.
------------------------------------------------------------------------
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        minimum = len(nums)+1
        curr = 0
        left = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                minimum = min(minimum, i-left+1)
                curr -= nums[left]
                left += 1

        return minimum if minimum <= len(nums) else 0