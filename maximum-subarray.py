'''
------------------
Difficulty: Medium
------------------

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Optimized Brute Force (Not accepted)
Time: O(N^2) -> Exceeds Time Limit
Space: O(1)

Runtime: Exceeds Time Limit ms
Memory: ? MB

This solution is an optimized brute force solution, resulting in N^2 space
complexity instead of N^3. This could be a good starting point for other
optimized methods. Initialize the max_subarray with minimum integer in case
nums is filled only with negative integers.
Iterate through nums so that we can look into cases where each element in nums
is a starting point for the subarray.
Within each iteration of i, initialize curr_subarray so that we can compare with max_subarray.
Within each iteration of j, add nums[j] to curr_subarray and compare with
max_subarray, potentially updating it.
This brute force method allows us to check every possible subarray in an optimized way.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxSubArray(self, nums):
        max_subarray = float('-inf')
        for i in range(len(nums)):
            curr_subarray = 0
            for j in range(i, len(nums)):
                curr_subarray += nums[j]
                max_subarray = max(curr_subarray, max_subarray)
        return max_subarray

'''
------------------------------------------------------------------------
Solution 2: Dynamic Programming, Kadane's Algorithm
Time: O(N)
Space: O(1)

Runtime: 732 ms
Memory: 25.7 MB

This is a solution using a commonly known DP algorithm called Kadane's Algorithm.
Key to this problem is the following:
  - if the sum of a subarray is not positive, it is not worth keeping
    since subarrays have to be included as a whole.
  - we do not need to keep subarrays, just the current subarray and the maximum subarray
  - for each iteration, see if including the previous subarray (curr_subarray that already exists)
    will increase sum of subarrays.
We start with the second element since we use the first one to initialize.
For each element from nums[1] (this wouldn't run if there is ony one element),
update curr_subarray to whatever is greater between num and num+curr_subarray.
If the existing curr_subarray is negative, it will decrease num, thus being thrown away.
This is equivalent to setting curr_subarray to num, and restarting there.
Then, update max_subarray to whatever is greater between curr_subarray and max_subarray.
This will keep our historic maximum sum of subarray even if the current window
of subarray decreases in the local sum.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxSubArray(self, nums):
        curr_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            curr_subarray = max(num, num+curr_subarray)
            max_subarray = max(max_subarray, curr_subarray)
        return max_subarray