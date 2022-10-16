'''
------------------
Difficulty: Easy
------------------

Note: this is such a vague problem. An "intersection" does not mean the
actual intersection in terms of a subarray, but means how many characters
in one array appears in the other array.
e.g. [1,2,3,2,4,2] & [2,2,4] => [2,2,4]

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted. 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(n+m)
Space: O(min(n,m))

Runtime: 30 ms
Memory: 13.7 MB

We always make nums1 the larger length in order to fulfill the space complexity of
O(min(n,m)). In first pass, we store how many times each characters have been
seen in nums1. In second pass, we add a char in nums2 to res as long as it
exists in the hashmap as key, and its remaining frequency is > 0.
------------------------------------------------------------------------
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)

        hashmap = {}
        
        for num in nums1:
            if not hashmap.get(num):
                hashmap[num] = 0
            hashmap[num] += 1

        res = []
        for num in nums2:
            if hashmap.get(num) and hashmap.get(num) > 0:
                res.append(num)
                hashmap[num] -= 1
        return res