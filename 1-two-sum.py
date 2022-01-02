'''
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

# ------------------------
# Solution 1 - Brute Force
# Time: O(n^2) - Looking through the rest of the array takes O(n) time.
# Space: O(1)
# ------------------------
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# ------------------------
# Solution 2 - Two Pass Hash Table
# Time: O(n) - Look up time in hash table is O(1).
# Space: O(n)
# ------------------------
'''
First pass => put all (value, index) in hashmap
Second pass => define complement, and see if complement already exists in hashmap (while index is different)
'''
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashmap and hashmap[complement] != j:
                return[j, hashmap[complement]]


# ------------------------
# Solution 3 - One Pass Hash Table
# Time: O(n)
# Space: O(n)
# ------------------------
'''
You can even do sigle pass by checking complement before adding (value, index) to hashmap.
This way, you don't have to check for index overlap later.
'''
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i