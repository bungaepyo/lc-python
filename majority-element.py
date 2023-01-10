'''
------------------
Difficulty: Easy
------------------

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array. 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

'''
------------------------------------------------------------------------
Solution 1: Hashmap
Time: O(n)
Space: O(n)

Runtime: 127 ms
Memory: 15 MB

This is a straightforward solution using a hashmap. We first store the
numbers and their frequencies in a hashmap, and later iterate through it
to find which element has the largest frequency.
------------------------------------------------------------------------
'''
class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        
        for num in nums:
            if not hashmap.get(num):
                hashmap[num] = 0
            hashmap[num] += 1
        
        maxCount = float('-inf')
        maxNum = None
        for k, v in hashmap.iteritems():
            if v > maxCount:
                maxCount = v
                maxNum = k
        
        return maxNum

'''
------------------------------------------------------------------------
Solution 1.1: Hashmap - simple version
Time: O(n)
Space: O(n)

Runtime: 140 ms
Memory: 15.1 MB

This is a very pythonic but more simple version of the hashmap solution.
------------------------------------------------------------------------
'''
class Solution(object):
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

'''
------------------------------------------------------------------------
Solution 2: Boyer-Moore Voting Algorithm
Time: O(n)
Space: O(1)

Runtime: 127 ms
Memory: 15.3 MB

This is a solution based on the the Boyer-Moore Voting Algorithm, where
the intuition is the following:
  - if we had some way of counting instances of the majority element as +1
    and instances of any other element as -1, summing them would make it
    obvious that the majority element is indeed the majority element.

What this tells us is that, given that the input array always has a majority
element, the sum of majority elements (+1) and non-majority elements (-1)
will always be positive. Therefore, if we cross out each majory-nonmajority
pair, the last one standing will always be the majority element.

In worst case scenario [1,1,1,2,2,2,2] where it looks like 1 is the majority
element until index 4, crossing out will eventually leave the majority element.
*** Also, since it's impossible to discard more majority elements than minority
elements, we are safe to discard the prefix and attempting to recursively solve the
majority element problem for the suffix.
  - [1,2,3,3,4,1,1,4,1,1] => (1,2) (3,3,4,1) (1,4,1,1)
------------------------------------------------------------------------
'''
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate