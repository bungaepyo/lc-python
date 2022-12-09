'''
------------------
Difficulty: Hard
------------------

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible. 

Example 1:

Input: nums = [1,3,5]
Output: 1

Example 2:

Input: nums = [2,2,2,0,1]
Output: 0 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.


Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates.
Would this affect the runtime complexity? How and why?
'''

'''
------------------------------------------------------------------------
Solution 1 - Linear Search (naive brute force)
Time: O(n)
Space: O(1)

Runtime: 44 ms
Memory: 14 MB

This is a naive linear seach approach that simly compares every element
with the element right before it. Even with duplicates, there will be a
point where the current element will be smaller than the element before
if the array has been rotated less than N times.

If we cannot find it, we simply return nums[0] because it either means
the array was rotated N times or the array is full of duplicates.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMin(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        
        return nums[0]

'''
------------------------------------------------------------------------
Solution 2 - Variant of Binary Search
Time: O(logn) -> on average case, worst case O(n) when array only contains duplicates
Space: O(1)

Runtime: 34 ms
Memory: 13.8 MB

This is a variant to the binary search solution from 153. Find Minimum in Rotated Sorted Array,
in that it adds the case where nums[mid] == nums[right].
Among >, <, ==, the first two cases are straightforward and is already
covered in the binary search solution in problem 153.
  - if nums[mid] is bigger, the minimum element must be on the right side
    of mid, so left = mid + 1
  - if nums[mid] is smaller, the minimum element could be nums[mid] or to
    the left of it. Thus, right = mid.

For the third case where nums[mid] == nums[right], we do not know which side
the minimum element would be located. Therefore, the only way to safely proceed
with the search is to exclude one of the duplicates we've found, which is
by updating the pointer.

Since we're looking for the minimum element, we can't reduce the left pointer.
So, we decrease the right pointer by one. If we go with this approach,
we may or may not have eliminated all duplicates every time we update the right
pointers. Therefore, in the worst case where the array is full of same numbers,
the time complexity would be O(n).
------------------------------------------------------------------------
'''
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]