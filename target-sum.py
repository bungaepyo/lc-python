'''
------------------
Difficulty: Medium
------------------

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of
the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1: Brute Force
Time: O(2^n) -> n is size of nums array
Space: O(n) -> depth of decursion tree goes up to n

Runtime: ? ms
Memory: ? MB

This is a recursive brute force approach to calculate all possible combinations
of building the target number, and adding 1 to count each time we find one.
The brute force approach is relatively intuitive but has poor time complexity
because it always doubles the recursion depth for each element in nums.
Therefore, in order to avoid repetitive recursions, we may improve this algorithm
with the memoization technique.
------------------------------------------------------------------------
'''
class Solution(object):
    
    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums, target):
        self.calculate(nums, 0, 0, target)
        return self.count

    def calculate(self, nums, i, total, target):
        if i == len(nums):
            if total == target:
                self.count += 1
        else:
            self.calculate(nums, i+1, total+nums[i], target)
            self.calculate(nums, i+1, total-nums[i], target)

'''
------------------------------------------------------------------------
Solution 2: DFS + Memoization
Time: O(nm) -> n refers to sum of nums, m refers to length of nums
Space: O(nm)

Note: time complexity is O(nm) because worst case [1,1,1,..1,1] target = m
      each index will have to store a sum, and that sum is the result of
      an operation that is adding previous sum + 1. (0,1) (1,2) ...
      Thus, since hashmap has to be filled up once, it's O(nm)

Runtime: 350 ms
Memory: 42.9 MB

This is a solution using the combination of the DFS approach and the memoization technique.
If we were to only perform DFS, it would merely be a brute force solution since
it will eventually + and - for every index we proceed with, resulting in O(2^n)
in time complexity. Therefore, memoization is key here.

In order to do the memoization, we need a hashmap that has (index, total) as key
and number of ways to reach target from that index as value. The reason
we include the index in the key is because there could be many different cases
in which the same total could be calculated in different indices.
Thus, using the if/else logic in line 73-76, we proceed with the DFS.
------------------------------------------------------------------------
'''
class Solution(object):
    def findTargetSumWays(self, nums, target):
        
        hashmap = {}

        def dfs(index, total):
            key = (index, total)

            if key not in hashmap:
                if index == len(nums):
                    return 1 if total == target else 0
                else:
                    hashmap[key] = dfs(index+1, total+nums[index]) + dfs(index+1, total-nums[index])

            return hashmap[key]

        return dfs(0, 0)
