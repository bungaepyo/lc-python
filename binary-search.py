'''
------------------
Difficulty: Easy
------------------

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

'''
------------------------------------------------------------------------
Solution 1 - Classic Binary Search
Time: O(logn)
Space: O(1)

Runtime: 200 ms
Memory: 14.6 MB

This is a classic way of implementing the binary search algorithm. Binary
search is oftentimes preferred to linear search "when the input is sorted"
because of its logarithmic time complexity. Basically, it improves the time
complexity for finding the target from O(n) to O(logn) by reducing the
search space by half every iteration.
  - (1) calculate the midpoint
  - (2) if the midpoint is target, return target
  - (3) if the midpoint is larger than target, we should only focus on the left half
  - (4) if the midpoint is smaller than target, we should only focus on the right half

Note on calculating "mid":
  - There are three ways of calculating mid
    (1) (low + high) / 2
    (2) low + ((high - low) / 2)
    (3) (low + high) >>> 1
    One might think that the first approach is good enough since it's basically
    getting the average of the low and high. However, it might be erroneous when
    we're dealing with large integers such as 2^31, which is the maximum positive int value.
    When doing a binary search with, say low = 1 high 2^31, this exceeds
    the maximum positive int value after being added and stays negative.
    Dividing this by 2 will throw an error. Thus, (2) and (3) are safer ways
    to calculcate "mid" because they prevent overflow.

https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

Also, if there are even number of elements, we may choose to use the lower/upper mid.
  - lower: low + ((high - low) / 2)
  - upper: low + ((high - low + 1) / 2)
------------------------------------------------------------------------
'''
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

'''
------------------------------------------------------------------------
Solution 2 - Binary Search with no mid comparison
Time: O(logn)
Space: O(1)

Runtime: 282 ms
Memory: 14.7 MB

This is a variation of the classic binary search where it does not compare
mid in the while loop condition. This method is typically used when you're
finding a pivot, not evaluating the existence of a target number.
------------------------------------------------------------------------
'''
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        # at this point our search space has shrinked to 
        # only one element if current element is the target element
        # then return its index else we can safely assume that element was not found
        
        return left if nums[left] == target else -1