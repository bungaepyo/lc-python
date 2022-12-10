'''
------------------
Difficulty: Medium
------------------

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
 
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 
Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointers
Time: O(n)
Space: O(1)

Runtime: 87 ms
Memory: 14.5 MB

This is a solution using the two pointer technique to find the pair that matches the target integer.
Once you understand the problem constraints, it's pretty straightforward
to implement the two pointers method.
First, to optimize before we actually compare the two pointers, we decrease
the right pointer until the sum of numbers pointed by left and right is greater than target.
Since the left pointer is the smallest number in input array, it's guaranteed that
we don't need numbers right to the index that gives a sum larger than target.
Then, we update the left and right pointers.
Since it's given that there will be at least one pair, we simply decrease right
if target - nums[right] is smaller than nums[left] and increase left if
target - nums[right] is larger than nums[left].
------------------------------------------------------------------------
'''
class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        
        #decrease right if sum is larger than target
        while nums[left] + nums[right] > target:
            right -= 1

        res = []
        #two pointers method to find the indices of the pair
        #add left+1 and right+1 to res and return it
        while left < right:
            if target - nums[right] < nums[left]:
                right -= 1
            elif target - nums[right] > nums[left]:
                left += 1
            else:
                res.append(left+1)
                res.append(right+1)
                return res

'''
------------------------------------------------------------------------
Solution 2 - Two Pointers
Time: O(n)
Space: O(1)

Runtime: 107 ms
Memory: 14.3 MB

This is a much more concise two pointers solution.
------------------------------------------------------------------------
'''
class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left < right:
            add = nums[left] + nums[right]
            if add == target:
                return [left+1, right+1]
            elif add > target:
                right -= 1
            else:
                left += 1

'''
------------------------------------------------------------------------
Solution 3 - Binary Search
Time: O(nlogn)
Space: O(1)

Runtime: 172 ms
Memory: 14.8 MB

We could also solve this problem using binary search - perform a O(logn)
binary search for each element, but this has way worse time complexity
than the two pointers solution.
------------------------------------------------------------------------
'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            tmp = target - nums[i]
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == tmp:
                    return [i+1, mid+1]
                elif nums[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1