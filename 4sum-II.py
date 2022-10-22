'''
------------------
Difficulty: Medium
------------------

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-2^228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^228
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(n^2)
Space: O(n^2)

Runtime: 503 ms
Memory: 13.7 MB

This is a solution using a hashmap that cleverly reduces the time complexity
to O(n^2) from the brute force solution's time complexity of O(n^4). The base
idea is that, if you store every combination of nums1 and nums2, it would take
O(n^2). If you lookup every combination of nums3 and nums4, that would also
take O(n^2) time. Thus, we store all a+b and look for -(c+d).

One thing to note specificially in this solution is that you should initialize
the hashmap using collections.defaultdict(int) or otherwise you will get a
KeyError.
------------------------------------------------------------------------
'''
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        hashmap = collections.defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                hashmap[a+b] += 1
        
        for c in nums3:
            for d in nums4:
                count += hashmap[-(c+d)]
        
        return count

'''
------------------------------------------------------------------------
Solution 2 - kSum II
Time: O(n^(k/2))
Space: O(n^(k/2))

Runtime: 994 ms
Memory: 13.9 MB

This is a more generalizable solution that may apply to k lists. The best we
can do in terms of time complexity is O(n^(k/2)), so we get O(N^2) if we have 4 lists.
Base idea is pretty similar with solution 1, where we divide the input lists
into two groups in order to half the time complexity.
We get the left and right group of the lists with the point k = len(lsts) // 2.

Once we get the left and right group, we use a helper function to calculate
the frequency of sums in each group using a Counter (hashmap). If we add up
all the (counts in left group)*(-count in right group) we are able to get all
possible 4sums that add up to 0.

In this process, we initialize a cumulative counter whose key is sum and value is count of that sum.
For each list, we need to be able to iterate and see if adding the list's elements
would create a new sum. Thus, a temporary counter is required.
After updating the temp counter by temp[total+a] += res[total],
we replace res with temp so that we can use the cumulative count for the next
list.
------------------------------------------------------------------------
'''
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        def sum_count(lsts):
            res = Counter({0:1})
            for lst in lsts:
                temp = Counter()
                for a in lst:
                    for total in res:
                        temp[total+a] += res[total]
                res = temp
            return res
        
        lsts = [nums1, nums2, nums3, nums4]
        k = len(lsts) // 2
        left, right = sum_count(lsts[:k]), sum_count(lsts[k:])
        return sum(left[s]*right[-s] for s in left)