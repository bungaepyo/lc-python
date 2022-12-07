'''
------------------
Difficulty: Medium
------------------

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.  

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 26 ms
Memory: 13.7 MB

This is a simple binary search solution to find the value at the inflection
point. Inflection point in a rotated sorted array is a point where the
value before it is larger than the value after it, and this question asks
to find the value right after the inflection point (min).

Even though, strictly speaking, the input array is not sorted we are able
to perform a binary search if we keep this concept in our minds:
  - Since there is one inflection point and the subarray to the left and
    right of it are both sorted, we just need to know whether we're on the
    left side or the right side of the inflection point.

One way of knowing whether we're on left or right is seeing if nums[mid]
is greater than nums[-1].
  - If mid is on the left side, it will always be nums[mid] > nums[-1]
    -> this means we need to update left = mid + 1

  - If mid is on the right side, or array was rotated n times, it will
    always be nums[mid] < nums[-1]
    -> this means we need to update right = mid (include mid since it could be the minimum)
------------------------------------------------------------------------
'''
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)/2
            if nums[mid] > nums[-1]:
                left = mid+1
            else:
                right = mid
        
        return nums[left]

'''
------------------------------------------------------------------------
Solution 2 - Binary Search (alternative)
Time: O(logn)
Space: O(1)

Runtime: 34 ms
Memory: 13.8 MB

This is an alternative binary search solution.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2

            # if the mid element is greater than its next element then mid+1 element is the smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the first element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1