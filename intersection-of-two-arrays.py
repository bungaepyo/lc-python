'''
------------------
Difficulty: Easy
------------------

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted. 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Sets
Time: O(n+m)
Space: O(n+m)

Runtime: 52 ms
Memory: 13.6 MB

This is a solution using two sets to figure out which elements overlap
between the two input arrays (it was super vague in the problem description
explaining what actually is defined as an "intersection"). We first add
all the elements of each array in the two sets to get rid of duplicates,
we iterate any of the two sets, and see if its elements exist in the other set.
------------------------------------------------------------------------
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        set1 = set()
        set2 = set()
        for num in nums1:
            set1.add(num)
        for num in nums2:
            set2.add(num)
        for num in set1:
            if num in set2:
                res.append(num)
        return res

'''
------------------------------------------------------------------------
Solution 2 - Two Sets (simplified)
Time: O(n+m)
Space: O(n+m)

Runtime: 58 ms
Memory: 13.7 MB

You can actually achieve the goal using the same approach with simplified
built-in features.
------------------------------------------------------------------------
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

'''
------------------------------------------------------------------------
Solution 3 - Two Sets
Time: O(n+m)
Space: O(n+m)

Runtime: 28 ms
Memory: 13.8 MB

This is another solution using two sets.
------------------------------------------------------------------------
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return [x for x in nums1 if x in nums2]