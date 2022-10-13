'''
------------------
Difficulty: Easy
------------------

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0] 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointer
Time: O(n)
Space: O(1)

Runtime: 141 ms
Memory: 15 MB

This is a solution using the two pointer method. One pointer would be iterating
through the array and the other pointer would only be pointing at zero elements.
For every iteration in the loop, we would check the following conditions and
try a swap:
  - nums[i] != 0 (non-zero element)
  - nums[zeroPointer] == 0 (zero element)
  - zeroPointer < i (since we are pusing zeroes towards the end)
Whether or not a swap happens, we update the zeroPointer if nums[zeroPointer] != 0
------------------------------------------------------------------------
'''
class Solution(object):
    def moveZeroes(self, nums):
        zeroPointer = 0
        
        for i in range(len(nums)):
            if nums[i] != 0 and nums[zeroPointer] == 0 and zeroPointer < i:
                temp = nums[i]
                nums[i] = nums[zeroPointer]
                nums[zeroPointer] = temp
            if nums[zeroPointer] != 0:
                zeroPointer += 1
            
        return nums

'''
------------------------------------------------------------------------
Solution 2 - Two Pointer (optimized)
Time: O(n)
Space: O(1)

Runtime: 136 ms
Memory: 14.5 MB

This is an optimized version of the two pointers method. We initialize two
pointers (1) one that always points at leftmost zero (2) one that points at each element.
While iterating the array with the second pointer, we always update the zero
pointer so that it meets its condition. Then, if the second pointer points
at a non-zero element and its index is larger than zero, swap.
This way, we are able to keep all the zeros towards the right side of the original array.
------------------------------------------------------------------------
'''
class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        
        for i in range(len(nums)):
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            if nums[i] != 0 and i > zero:
                nums[zero], nums[i] = nums[i], nums[zero]