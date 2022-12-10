'''
------------------
Difficulty: Medium
------------------

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

'''
------------------------------------------------------------------------
Solution 1: Negative Marking (NOT A SOLUTION)
Time: O(n)
Space: O(1)

Runtime: 607 ms
Memory: 25.3 MB

This is not a feasible solution since it temporarily modifies the input array,
but could be a useful technique. Since we have n+1 integers in the input
array, it is guaranteed that for any number in the array, nums[number] will
exist.

Therefore, whenever we see a number, if we mark nums[number] as negative,
there will be a point where nums[number] is already negative. That will be
our duplicate number.
------------------------------------------------------------------------
'''
class Solution(object):
    def findDuplicate(self, nums):
        for num in nums:
            curr = abs(num)
            if nums[curr] < 0:
                duplicate = curr
                break
            nums[curr] = -nums[curr]
        
        # restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return duplicate

'''
------------------------------------------------------------------------
Solution 2: Binary Search
Time: O(nlogn)
Space: O(1)

Runtime: 910 ms
Memory: 25.2 MB

This is a binary search solution that utilizes the characteristics of
the input array. If there are no duplicates in the array, the count of
integers that are smaller than or equal to a number will be the number itself.
For example, [1,2,3,4,5] will have count of [1,2,3,4,5].

Thus, if there is a duplicate, the count will be larger than the number,
and this applies to all the numbers thereafter.
For example, [1,2,3,3,4] will have count of [1,2,4,4,5].

Using this intuition, we are going to use a binary search algorithm to
find the first number whose count is bigger than itself. The most important
thing to know here is that low and high bounaries represent the range of
values of the target. We are not searching for an element in the array
but rather looking for the smallest number with a bigger count.
------------------------------------------------------------------------
'''
class Solution(object):
    def findDuplicate(self, nums):
        #low and high represent the range of values of the target
        low, high = 1, len(nums)-1
        
        while low <= high:
            cur = low + (high-low)//2
            
            #count how many numbers are less than or equal to cur
            count = sum(num <= cur for num in nums)
            
            if count > cur:
                duplicate = cur
                high = cur-1
            else:
                low = cur+1
        
        return duplicate
