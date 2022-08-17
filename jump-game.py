'''
------------------
Difficulty: Medium
------------------

You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking
Time: O(2^n)
Space: O(n)

Runtime: Excceeds time limit ms
Memory: ? MB

This is an initial recursive backtracking solution that works, but exceeds time limit.
Starting from the first element of nums, we use the recursive helper function
to check every posibility and see if any of them can reaach the last element.
Base case: return if current position is last index.
From next element to the furthest jump (either furthest it can go or last element),
we recursively check if any route takes us to the last element.
------------------------------------------------------------------------
'''
class Solution(object):
    def canJump(self, nums):
        return self.canJumpFromPosition(0, nums)
    
    def canJumpFromPosition(self, position, nums):
        if position == len(nums)-1:
            return True
        
        furthestJump = min(position + nums[position], len(nums)-1)
        for nextPosition in range(position+1, furthestJump+1):
            if(self.canJumpFromPosition(nextPosition, nums)):
                return True

'''
------------------------------------------------------------------------
Solution 2: Dynamic Programming Top-down (Memoization)
Time: O(n^2)
Space: O(n)

Runtime: ? ms
Memory: Exceeds space limit MB

This is a slightly optimized DP solution using memoization. Using a list of
'Unknown', 'Bad', or 'Good' we are able to start from the end and memo
if the element at a certain position is Good (can reach last element) or Bad.
This way, we are able to save on time complexity because we do not have to
redo the computation for elements at positions that are already known.
------------------------------------------------------------------------
'''
class Solution(object):
    def canJump(self, nums):
        memo = len(nums)*['U']
        memo[-1] = 'G'
    
        def canJumpFromPosition(position, nums):
            if memo[position] != 'U':
                return True if memo[position] == 'G' else False

            furthestJump = min(position + nums[position], len(nums)-1)
            for nextPosition in range(position+1, furthestJump+1):
                if(canJumpFromPosition(nextPosition, nums)):
                    memo[position] = 'G'
                    return True

            memo[position] = 'B'
            return False
        
        return canJumpFromPosition(0, nums)

'''
------------------------------------------------------------------------
Solution 3: Dynamic Programming Bottom-up
Time: O(n^2)
Space: O(n)

Runtime: ? ms
Memory: ? MB

This is a more optimized solution using bottom-up DP, but still exceeds time limit.
Essentially, the key here is to understand that as long as you find an
element that is 'Good' between your next position and furthest jump you can make from your current position,
you simply would not have to continue with the loop.
If you find an element that is reachable and 'Good', your current element is 'Good' as well.
Therefore, continue this until the first index and see if the first element
is 'Good' as well.
------------------------------------------------------------------------
'''
class Solution(object):
    def canJump(self, nums):
        memo = len(nums)*['U']
        memo[-1] = 'G'
    
        for i in range(len(nums)-2, -1, -1):
            furthestJump = min(i+nums[i], len(nums)-1)
            for j in range(i+1, furthestJump+1):
                if memo[j] == 'G':
                    memo[i] = 'G'
                    break

        return memo[0] == 'G'

'''
------------------------------------------------------------------------
Solution 4: Greedy
Time: O(n)
Space: O(1)

Runtime: 353 ms
Memory: 14.7 MB

Key concept: current position is 'Good' as long as it can reach another 'Good' position or the end of the array
Using the same concept from solution 3 (key concept above), we are able to
further optimize the algorithm to O(n) time and O(1) space complexity.
In our one pass starting from the end of the array, we check if the current
position can reach lastPos, which initially is set to the last position.
If we can reach, update lastPos to current position and continue with loop.
At the end of the loop, if there is a jump path from beginning to end,
lastPos will be 0.
------------------------------------------------------------------------
'''
class Solution(object):
    def canJump(self, nums):
        lastPos = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lastPos:
                lastPos = i
        
        return lastPos == 0