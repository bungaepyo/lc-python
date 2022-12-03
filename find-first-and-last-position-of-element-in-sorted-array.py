'''
------------------
Difficulty: Medium
------------------

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1] 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(n)
Space: O(1)

Runtime: 148 ms
Memory: 14.6 MB

This is a solution that uses the binary search method, but is not an optimal one.
Worst case scenario in which nums is full of target, this will take linear time, O(n).
The idea of this solution is the following: find the target element in whichever index
and start expanding to the left and to the right until element value != target.
Using a binary search sub-function, we first get the index of a target (if it exists).
Then, we initiate left and right pointers and move them left and right until
num[left] or num[right] is not target anymore. Return [left+1, right-1].
------------------------------------------------------------------------
'''
class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(start, end):
            while start <= end:
                mid = start + (end-start)/2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        end = mid-1
                    else:
                        start = mid+1
            return -1
        
        targetIdx = binarySearch(0, len(nums)-1)

        if targetIdx == -1:
            return [-1,-1]
        
        left, right = targetIdx, targetIdx
        
        while left>=0 and nums[left] == target:
            left -= 1
        while right<=len(nums)-1 and nums[right] == target:
            right += 1
        
        return [left+1, right-1]

'''
------------------------------------------------------------------------
Solution 2 - index()
Time: O(n)
Space: O(1)

Runtime: 44 ms
Memory: 13.6 MB

THis is a solution using python method index() which returns the position
at the first occurrence of the specified value. If target is in nums (which can be simply checked by using "in"),
you find the lowest index of target by using nums.index(target).
Iterate from x+1 to the end of the array and see how many more target values
you can find and add to a variable. Return [x, y].
------------------------------------------------------------------------
'''
class Solution(object):
    def searchRange(self, nums, target):
        if target in nums:
            x=nums.index(target)
            y=x
            for i in range(x+1,len(nums)):
                if nums[i]==target:
                    y+=1
            return x,y
        else:
            return [-1,-1]

'''
------------------------------------------------------------------------
Solution 3 - Binary Search, but better
Time: O(log n)
Space: O(1)

Runtime: 66 ms
Memory: 14.6 MB

This is also a soltion that uses the binary search method, but it's smarter.
The intuition is similar, but the helper function has a parameter isFirst that
indicates whether we're looking for the first or the last occurrence of the target.
Everything else is the same in the binary search function except for two scenarios.
If we find target by nums[mid] == target, we need to check if it's the first/last element.
If isFirst is True:
    We are looking for the first occurrence. Thus, either of the following condition has to be met
    (1) mid == begin - no other element to the left, hence automatically first occurrence
    (2) nums[mid-1] < target - element to the left is smaller than target

If isFirst is False (it's just the opposite):
    We are looking for the last occurrence. Thus, either of the following condition has to be met
    (1) mid == end
    (2) nums[mid+1] > target

If either of the two conditions are met, we just update the end/begin to mid-1/mid+1
and continue with the binary search. If we get -1 for lower_bound, just return [-1,-1].
Otherwise, return [lower_bound, upper_bound]
------------------------------------------------------------------------
'''
class Solution(object):
    def searchRange(self, nums, target):
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums, target, isFirst):
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            if nums[mid] == target:
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    # Search on the right side for the bound.
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1