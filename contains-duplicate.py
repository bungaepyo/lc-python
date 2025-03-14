'''
------------------
Difficulty: Easy
------------------

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
------------------------------------------------------------------------
Solution 1 - Hash Table
Time: O(n) -> search and insert for n times
Space: O(n) -> space used by hash table is linear

Runtime: 573 ms
Memory: 23.7 MB

This is a solution using a set data structure, which is implemented with a hash table.
While iterating the input array, we check if the element is already in the
set and return True if it is.

We can use an array to perform the same operation, but it exceeds time limit
because array's search time complexity is O(n) while a set's search time complexity
is O(1) in average case because it's implemented with a hash table.
(note: worst case time complexity for hash table is still O(n))
------------------------------------------------------------------------
'''
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False

class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        return False

'''
------------------------------------------------------------------------
Solution 2 - Sorting
Time: O(nlogn)
Space: O(1)

Runtime: 663 ms
Memory: 22.3 MB

This is a solution using the built in sorting function, which is an improvement
from the naive brute force solution but still is not optimized in terms of
time complexity. Basically, it sorts the array and compares each element with
the element after it.
Sorting function's time complexity is O(nlogn).
------------------------------------------------------------------------
'''
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False