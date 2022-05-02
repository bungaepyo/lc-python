'''
------------------
Difficulty: Medium
------------------

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(log n)
Space: O(1)

Runtime: 51 ms
Memory: 13.5  MB

This is a solution using the binary search technique. Since the input array
of this problem is sorted and possibly rotated, finding the pivot index is
the single most important thing that needs to be done. Once you find the
pivot index, you would be able to easily find the target using binary search.
First, find the pivot index using a search sub-function (pivotSearch).
  Case 1: target is at pivot index => return pivot index
  Case 2: there is no rotation (pivot==0) => find answer using entire array binarySearch(0, len(nums)-1)
  Case 3: target is smaller than nums[0]
          this means that target belongs to the un-rotated (smaller) side
          => you only need to binarySearch(pivot, len(nums)-1)
  Case 4: target is larger than nums[0]
          this means that target belongs to the rotated (larger) side
          => you only need to binarySearch(0, pivot)

For case 3,4 you are performing binary search for either:
  smaller part => un-rotated part
  larger part => rotated part
so the input arrays for the binary search should already be sorted
------------------------------------------------------------------------
'''
class Solution(object):
    def search(self, nums, target):

        # binary search sub-function
        def binarySearch(left, right):
            while left <= right:
                mid = left + (right-left)/2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        right = mid-1
                    else:
                        left = mid+1
            return -1

        # binary search function that finds pivot index
        def pivotSearch(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = left + (right-left)/2
                if nums[pivot] > nums[pivot+1]:
                    return pivot+1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot -1
                    else:
                        left = pivot + 1

        #check edge case where len(nums) is 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        #find pivot index
        pivot = pivotSearch(0, len(nums)-1)
        
        #if int at pivot index is target, return pivot
        if nums[pivot] == target:
            return pivot
        
        #if no rotation, do binary search for entire array
        if pivot == 0:
            return binarySearch(0, len(nums)-1)
        
        #if target is smaller than first element, do binary search from pivot to end
        if target < nums[0]:
            return binarySearch(pivot, len(nums)-1)
        #if target is bigger than first element, do binary search from start to pivot
        return binarySearch(0, pivot)

'''
------------------------------------------------------------------------
Solution 2 - One-Pass Binary Search
Time: O(log n)
Space: O(1)

Runtime: 46 ms
Memory: 13.9  MB

This is a solution using binary search, but simplified because it's only one-pass.
The key to this solution is understanding:
  (1) two diff scenarios => nums[mid] is larger than nums[start] AND nums[mid] is smaller than nums[start]
  (2) we need to keep looking for a sorted part where it contains target
In a while loop where end index is always greater than or equal to start index,
every iteration we get a new mid and see if nums[mid] is equal to target, just like normal binary search.
However, we start looking if current mid is in the un-rotated part or the rotated part.
If current mid is in the rotated part (nums[start] <= nums[mid]):
    this means we can see if target is between start and mid, which is sorted
If current mid is in the un-rotated part (nums[start] > nums[mid]):
    this means we can see if target is between mid and end, which is also sorted

In either cases, if we successfully find the sorted part that contains target,
it decreases the time for rest of the process becuase now it's straigforward doing normal binary search.
------------------------------------------------------------------------
'''
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1