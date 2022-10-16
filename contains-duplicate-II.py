'''
------------------
Difficulty: Easy
------------------

Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k. 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(n)
Space: O(n)

Runtime: 678 ms
Memory: 24.5 MB

This is a solution using a hashmap. While iterating nums, we check if for every number
these two conditions:
  - if it already exists in the hashmap
  - if so, abs(i-j) <= k
It it meets these two conditions, return True. If not, simply add/swap
hashmap[number] to its index. This way, any previous indices (which are useless)
can be ignored - in cases where there are more than 2 occurrences.
------------------------------------------------------------------------
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        for i, j in enumerate(nums):
            if j in hashmap and abs(i-hashmap[j]) <= k:
                return True
            hashmap[j] = i
        return False

'''
------------------------------------------------------------------------
Solution 2 - HashSet, Sliding Window
Time: O(n)
Space: O(min(n,k)) -> extra space required depends on the number of items
                      stored in the set, which is size of sliding window min(n,k)

Runtime: 534 ms
Memory: 21.8 MB

This is an alternative solution using a hashset. This essentially mimics
the FIFO sliding window. You essentially add all the numbers you see in nums
to the set, and if you find one already exists before you add, that means
there is already a same number within the sliding window, which fulfills abs(i-j) <= k.
The condition of removing nums[i-k] if len(hashset) > k keeps the condition throughout
the iteration because it gets rid of the elements from the beginning if i-j exceeds k.
------------------------------------------------------------------------
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            if len(hashset) > k:
                hashset.remove(nums[i-k])
        return False