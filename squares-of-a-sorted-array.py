'''
------------------
Difficulty: Easy
------------------

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointer
Time: O(n)
Space: O(n)

Runtime: 697 ms
Memory: 15.1 MB

This is probably the most intuitive solution using the two pointer technique.
First, you square the nums array to get all the values that you need for comparison.
Then, using two pointers (start, end) to comparing elements staring from the outermost
ones - this is because we're using the characteristics of squared integers.
  - since this is an array sorted in ascending order, we know that outermost elements
    have the largest absolute value, thus should be at the end of the result array.
Therefore, we insert the bigger element to the beginning of the array.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        
        res = []
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] > nums[right]:
                res.insert(0, nums[left])
                left += 1
            else:
                res.insert(0, nums[right])
                right -= 1
        return res

'''
------------------------------------------------------------------------
Solution 2 - Two Pointer (slightly optimized because of one-pass)
Time: O(n)
Space: O(n)

Runtime: 389 ms
Memory: 15.5 MB

This solution uses the same concept of two pointers, but is a bit optimized.
We initialize a result array with 0s and iterate the indices from the back
to fill in the array. The way we do it is using two pointers (start, end) and
comparing their absolute values.
Instead of squaring the elements in a separate pass, we square the values when
we append the elements to the result array.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result