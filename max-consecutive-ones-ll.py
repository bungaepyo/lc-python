'''
------------------
Difficulty: Medium
------------------

Given a binary array nums, return the maximum number of consecutive 1's
in the array if you can flip at most one 0.

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Follow up: What if the input numbers come in one by one as an infinite stream?
In other words, you can't store all numbers coming from the stream as it's too large to hold in memory.
Could you solve it efficiently?
'''

'''
------------------------------------------------------------------------
Solution 1 - Sliding Window
Time: O(n)
Space: O(1)

Runtime: 318 ms
Memory: 14 MB

This is a O(n) sliding window solution. Essentially, what this problem means
by "flipping at most one 0" is that we allow at most one 0 in our sequence.
Therefore, we will update the left/right indices of our sliding window depending
on how many zeros we currently have in the sequence.
  - Valid: less than 2 zeros
  - Invalid: 2 zeros
While increasing the right pointer, we first check if nums[right] is 0 and add 1
to the count of zeros if it is.
If the number of zero becomes 2 due to the current right pointer, we will increase
left pointer until there is less than 2 zeros.
Once we have less than 2 zeros, we try updating res (longest sequence) and
increase the right pointer again.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        numZero = 0
        res = 0
        
        while right < len(nums):
            if nums[right] == 0:
                numZero += 1
            
            while numZero == 2:
                if nums[left] == 0:
                    numZero -= 1
                left += 1
            
            res = max(res, right-left+1)
            right += 1

        return res