'''
------------------
Difficulty: Easy
------------------

Given an integer array nums, move all the even integers at
the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0] 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pointers
Time: O(n)
Space: O(1)

Runtime: 103 ms
Memory: 14.3 MB

This is an intuitive two pointers solution that tries a swap whenever the
left pointer finds an odd element and the right pointer finds an even element.
Since the original relative order does not matter in this problem, there is
less complication in the solution logic. We just need to try the swap, and
increase left or decrease right depending on the remainder (%2) of their value.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums)-1
        
        while left < right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 != 0:
                right -= 1

        return nums