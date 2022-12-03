'''
------------------
Difficulty: Medium
------------------

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6. 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 32 ms
Memory: 13.8 MB

This is a binary search solution that can reduce time complexity to O(logn).
Binary search works even though the array is not sorted because
  - (1) we are allowed to return any peak
  - (2) elements are always ascending or decending

While updating the search space using left and right, there could be two scenarios. (compare mid vs mid+1)
  - (1) mid is on the ascending slope -> we know that peak is on the right side of mid
  - (2) mid is on the decending slope -> we know that peak is on mid or left of mid
We will proceed until one element is left a.k.a terminating condition is left = right.
Once while loop has been terminated, left will be pointing at the peak element.
------------------------------------------------------------------------
'''
class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)/2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
            
        return left

'''
------------------------------------------------------------------------
Solution 2 - Linear Scan
Time: O(n)
Space: O(1)

Runtime: 41 ms
Memory: 13.8 MB

This is a linear apporach, which is not acceptible because of its time complexity.
However, the intuition is similar. The first element you find whose value
is greater than the next one is guaranteed to be a peak.
------------------------------------------------------------------------
'''
class Solution(object):
    def findPeakElement(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1