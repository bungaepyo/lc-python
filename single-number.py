'''
------------------
Difficulty: Easy
------------------

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

'''
------------------------------------------------------------------------
Solution 1 - List Operation
Time: O(n^2) -> iteration O(n) * operation O(n)
Space: O(n)

Runtime: 1029 ms
Memory: 15.5 MB

This is the most naive approach that takes O(n^2) time to complete.
Simply add everything and remove everything that have been seen. There will be one left.
------------------------------------------------------------------------
'''
class Solution(object):
    def singleNumber(self, nums):
        no_duplicate = []
        for num in nums:
            if num not in no_duplicate:
                no_duplicate.append(num)
            else:
                no_duplicate.remove(num)
        return no_duplicate[0]

'''
------------------------------------------------------------------------
Solution 2 - Hash Table
Time: O(n)
Space: O(n)

Runtime: 126 ms
Memory: 16.2 MB

This is a solution using a HashMap, counting how many times each number has
been seen in nums. In second pass, if we see anything that's only been seen
once, we return that number.
------------------------------------------------------------------------
'''
class Solution(object):
    def singleNumber(self, nums):
        hashmap = {}
        for i in nums:
            if hashmap.get(i):
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in nums:
            if hashmap[i] == 1:
                return i

'''
------------------------------------------------------------------------
Solution 3 - Math
Time: O(n)
Space: O(n)

Runtime: 142 ms
Memory: 16 MB

Pretty smart solution using the characteristics of the input array.
If we simply double the sum of input array's set and subtract the sum of
input array's unique number set, only thing left will be an integer, which
is the answer.
------------------------------------------------------------------------
'''
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

'''
------------------------------------------------------------------------
Solution 3 - Bit Manipulation
Time: O(n)
Space: O(1)

Runtime: 102 ms
Memory: 15.7 MB

- If we take the XOR of zero and some bit, it will return that bit
- If we take XOR of two same bits, it will return 0
Thus, we can XOR all bits together and fine the unique number.
------------------------------------------------------------------------
'''
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a