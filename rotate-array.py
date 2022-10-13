'''
------------------
Difficulty: Medium
------------------

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100] 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
'''

'''
------------------------------------------------------------------------
Solution 1: Brute Force (Exceeds Time Limit)
Time: O(nk)
Space: O(1)

Runtime: Time Limit Exceeded ms
Memory: ??? MB

This is a brute force solution that, for each step in range of k, we move
all the elements to the right by 1. We do this by saving and updating a
variable "previous" in each step. In the beginning, previous would be
the last element. During iteration, we assign that previous to nums[j]
and make nums[j] the previous for the next element.
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

'''
------------------------------------------------------------------------
Solution 2: Extra Array
Time: O(n)
Space: O(n)

Runtime: 172 ms
Memory: 25.2 MB

This is a solution using extra memory to create an array with adjusted positions,
and assign that array to nums[:].
While iterating nums, we assign each element to a[(i+k)%n].
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        a = [0]*n
        for i in range(n):
            a[(i+k)%n] = nums[i]
        nums[:] = a

'''
------------------------------------------------------------------------
Solution 3: Cyclic Replacements
Time: O(n)
Space: O(1)

Runtime: 352 ms
Memory: 25.1 MB

This solution might look complicated, but essentially it is making a cycle to
update the next element with current element while saving the next element to a
temporary variable so that the swap could go on and on until the end.

One thing to be mindful about this solution is when n%k = 0. This means,
while updating elements, there will be a monent where we encounter the index we've
started from. This will block us from finishing the number swap, so we
simply += the index we're pointing to and continue with the loop.
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

'''
------------------------------------------------------------------------
Solution 4: Using Reverse
Time: O(n)
Space: O(1)

Runtime: 181 ms
Memory: 25 MB

This is a really smart solution that reflects the patterns of the result array.

Original List                   : [1 2 3 4 5 6 7]
After reversing all numbers     : [7 6 5 4 3 2 1]
After reversing first k numbers : [5 6 7] [4 3 2 1]
After revering last n-k numbers : [5 6 7] [1 2 3 4] --> Result
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1