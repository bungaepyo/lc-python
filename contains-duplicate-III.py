'''
------------------
Difficulty: Hard
------------------

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false. 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
'''

'''
------------------------------------------------------------------------
Solution 1: Naive Linear Search (TLE)
Time: O(n*min(n,k)) -> costs min(n,k) to do linear search for each element
Space: O(1)

Runtime: ? ms
Memory: ? MB

This is a naive linear search & comparison approach, which exceeds time limit.
However, it is a good starting point to figure out what the bottleneck is.
------------------------------------------------------------------------
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        for i in range(len(nums)):
            for j in range(max(i-indexDiff, 0), i, 1):
                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True
        return False

'''
------------------------------------------------------------------------
Solution 2: Binary Search Tree
Time: O(n*log(min(n,k)))
Space: O(min(n,k))

Runtime: 4095 ms
Memory: 28.6 MB

Java uses its TreeSet class to easily implement this, but you need to implement
the class if using Python.

https://leetcode.com/problems/contains-duplicate-iii/discuss/174416/Python-balanced-BST-solution
------------------------------------------------------------------------
'''

'''
------------------------------------------------------------------------
Solution 3: Buckets
Time: O(n)
Space: O(min(n,k))

Runtime: 888 ms
Memory: 40.5 MB

This is a linear time solution using a technique called Bucket Sort, which
uses buckets of custom range as windows for search/comparison.

Bucket sort is basically putting elements in a bucket of custom size (in this case it's indexDiff),
so that we can truncate the search window and perform search in constant time.
To use an analogy, say you think your friend's birthday is in June but you
might be wrong by 30 days. This allows us to only look at the buckets May, June, and July
instead of looking for all of the months.

Basically, what we want to find for each element x is, if there is an element y
in the array whose:
  - index is within [x's index - indexDiff, x's index + indexDiff]
  - value is within [x - valueDiff, x + valueDiff]

Using buckert sort allows us to simplify both conditions because we're
only going to have to check the current bucket and its neighboring buckets.
The buckets are going to only contain the most recently checked element (we're iterating
and updating at the same time), so we can lookup in O(1).

If current bucket is seen and it's within the given index range (we don't
have to check valueDiff because we've already done that when assigning the bucket),
we return it. Furthermore, if bucket+1 or bucket-1 is seen and it's in both index range and value range,
return it.

Except for the part where it assigns and bucket and checks the 3 buckets,
this solution is essentially similar to Contains Duplicate II.
------------------------------------------------------------------------
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
          return False

        seen = {}
        for i, x in enumerate(nums): 
            bucket = x//(valueDiff+1)
            if bucket in seen and i - seen[bucket][0] <= indexDiff:
                return True 
            if bucket-1 in seen and i - seen[bucket-1][0] <= indexDiff and abs(x - seen[bucket-1][1]) <= valueDiff:
                return True
            if bucket+1 in seen and i - seen[bucket+1][0] <= indexDiff and abs(x - seen[bucket+1][1]) <= valueDiff:
                return True 
            seen[bucket] = (i, x)
        return False 