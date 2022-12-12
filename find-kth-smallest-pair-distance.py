'''
------------------
Difficulty: Hard
------------------

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance
among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search (trial and error algorithm)
Time: O(nlogd + nlogn) -> d = max(nums) - min(nums) = largest distance
Space: O(1)

Runtime: 89 ms
Memory: 14.3 MB

Nice soluution: https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm

Couple important Intuitions:
  - We're trying to find the kth smallest pair distance, so search space
    should be an array of distances
  - Search space is [0, d] where d = max(nums) - min(nums) = largest distance

Coming up with how to approach this problem is the hardest part, but we
could summarize it into two steps:
  - We need to be able to count how many distance pairs are smaller than or
    equal to a given number. Otherwise, we cannot decide whether it's kth or not.
  - We need an efficient algorithm that can traverse through the search space.

If we are able to count how many distance pairs are smaller than or equal to a
given number, we can apply binary search to this problem. Say we have a
midpoint and we calculate how many distance pairs are smaller than or equal to it.

If the count is less than k, we know that the entire left part of midpoint
are useless since they're all smaller than kth smallest distance. Thus, l = m+1
If the count is greater than or equal to k, we know that the midpoint might or might
not be kth smallest distance, so we simply do r = m.

The most important part here is the for loop inside the binary search.
For each i, it increases count by 1 if there is a pair that is smaller than equal to m.
The resulting count is the number of distance pairs that are smaller than or equal to m.
------------------------------------------------------------------------
'''
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        
        n = len(nums)
        left, right = 0, nums[-1]-nums[0]
        
        while left < right:
            mid = left + (right-left)//2
            
            count = j = 0
            
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j-i-1
            
            if count < k:
                left = mid+1
            else:
                right = mid
        
        return left