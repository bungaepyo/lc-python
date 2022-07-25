'''
------------------
Difficulty: Hard
------------------
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
 
Example 1:

Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 
Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1 - Hash Table
Time: O(n)
Space: O(1) => how is this not O(n)?

Runtime: 705 ms
Memory: 67.5 MB

This is a solution using hash table that I thought would not meet the
space complexity constraint of the problem O(1). Essentially, this solution
performs executes iterations. First, we initialize a hashmap and set each number
in nums as key, and mark them as True to denote that they are present in nums.
Second, we iterate through numbers from 1 to len(nums)+1 and see if each number
exists. The key here is to realize two things:
  - we can skip zero, and negative numbers since they won't affect smallest missing positive integer.
  - smallest missing positive integer can only be an integer from 1 to len(nums)+1 since
    it always starts counting from 1 and the max number is len(nums)+1
If we see a missing integer from 1 to len(nums)+1, we return that value.
Otherwise, return len(nums)+1 because all positive integers smaller than len(nums) exists.
------------------------------------------------------------------------
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        hashmap = {}

        for number in nums:
            hashmap[number] = True
        
        for i in range(len(nums)):
            spi = i+1
            if spi not in hashmap:
                return i+1
        
        return len(nums)+1

'''
------------------------------------------------------------------------
Solution 1 - array in place
Time: O(n)
Space: O(1)

Runtime: 906 ms
Memory: 52 MB

This solution uses an in-place sorting technique in order to meet the
problem's space complexity constraint. There are four major steps.
(1) you need to sort the array in place so that only positive integers
    exist on the first half. This way, we are going to only iterate the first
    half of the array and see if any pos int are missing.
(2) for every element in first half, you make nums[int-1] a negative
    value by multiplying -1. This is so that we mark which positive integer
    exists in our nums list.
(3) for every element in first half, see if anything is still positive.
    If there was any duplicate, zero, or negative integer, there should be
    at least 1 value that is still positive. The only case in which
    all values of this iteration can be negative is when there are no
    missing positive integer in the nums list.
(4) If we could not find any, return length of list + 1
------------------------------------------------------------------------
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        #1 sort the array in-place so that posivie integers on first half
        j = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[j] = nums[i]
                j+=1
        
        #2 for every positive int, mark nums[pos int -1] to negative
        for i in range(j):
            a = abs(nums[i])
            if a <= j and nums[a-1]>0:
                nums[a-1] = -nums[a-1]
                
        #3 iterate the array and return anything that is still positive
        #  need to +1 still since indices are diff from integers
        for i in range(j):
            if nums[i]>0:
                return i+1
        
        #4 return list length+1 if couldn't find any (list length +1)
        return j+1