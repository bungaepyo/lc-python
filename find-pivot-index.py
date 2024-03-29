'''
------------------
Difficulty: Easy
------------------

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to
the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
'''

'''
------------------------------------------------------------------------
Solution 1 - Cumulative Sum
Time: O(n)
Space: O(n)

Runtime: 157 ms
Memory: 14.5 MB

This is a fairly intuitive solution using extra space to make an array that
stores cumulative sum.

In our first pass, we fill the sumList with cumulative sums until the index.
In our second pass, we calculate the leftSum and rightSum for each index
and if they match, return the index.
------------------------------------------------------------------------
'''
class Solution(object):
    def pivotIndex(self, nums):
        carry = 0
        sumList = []
        
        # create cumulative sum list
        for i in range(len(nums)):
            sumList.append(nums[i] + carry)
            carry = sumList[i]
        
        for i in range(len(nums)):
            leftSum = sumList[i] - nums[i]
            rightSum = sumList[len(nums)-1] - sumList[i]
            
            if leftSum == rightSum:
                return i
        
        return -1


'''
------------------------------------------------------------------------
Solution 2 - Cumulative Sum, O(1) space
Time: O(n)
Space: O(1)

Runtime: 269 ms
Memory: 14.7 MB

This solution uses the exact sam intuition as solution 1, but doesn't use linear extra space.
Using the python function sum() to get the totalSum of the list is important here.
Once we have the totalSum, we can update leftSum during our iteration.

RightSum here is same: totalSum - nums[i] - leftSum.
If left and right match, return the index.
Otherwise, update leftSum and proceed.
------------------------------------------------------------------------
'''
class Solution(object):
    def pivotIndex(self, nums):
        totalSum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if leftSum == rightSum: return i
            leftSum += nums[i]

        return -1