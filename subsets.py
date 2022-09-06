'''
------------------
Difficulty: Medium
------------------

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]] 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n*2^n) => generate all subsets and then copy them into output list.
Space: O(n) => We are using O(N) space to maintain arr. Worst case, arr == nums.

Runtime: 30 ms
Memory: 13.8 MB


This is a recursive function using a helper function to deal with the depths.
The base idea here is:
  - we iterate through every individual elements, and add elements on top of that
    in order to generate all subsets and add unique ones to the result list.
For each individual element in nums, you run the helper function and pass the index
of the element that you should add.
Within the helper function, (1) you generate the subset you're trying to add,
(2) check if it already exists. if not, add it to res (3) recursively call the 
helper function with indices ranging from idx+1 to len(nums). -> this way we only
add elements of bigger index in nums.
This algorithm will add the subsets in the following way:
  - [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
------------------------------------------------------------------------
'''
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        
        for i in range(len(nums)):
            self.helper([], i, nums, res)

        return res
    
    def helper(self, arr, idx, nums, res):
        arr.append(nums[idx])
        if arr in res:
            return
        res.append(arr)

        for j in range(idx+1, len(nums)):
            self.helper(arr[:], j, nums, res)

'''
------------------------------------------------------------------------
Solution 2: Cascading, DP?
Time: O(n*2^n) => generate all subsets and then copy them into output list.
Space: O(n*2^n) => exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.

Runtime: 26 ms
Memory: 13.6 MB

This is a dynamic programming style solution, in which the base idea is cascading.
Cascading means the following:
  - as we consider new elements in nums, we may just want to add the
    new element to existing lists of the result list to generate
    new unique subsets with the new element we're considering.
Line 91-92 exactly portrays this logic, and this solution sacrifices
enormous space complexity.
------------------------------------------------------------------------
'''
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output

'''
------------------------------------------------------------------------
Solution 3: Backtracking
Time: O(n*2^n) => generate all subsets and then copy them into output list.
Space: O(n) => We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking.

Runtime: 26 ms
Memory: 13.6 MB

This is a recursive solution using the backtracking technique. The base idea
is not too different from solution 1, but the way it implements the
recursive depths is different. First, we set the huddle for number of integers in each list to k.
k indicates the length of each list that gets appended to output, which is also the depth.
For each k, we add elements to curr until its length is equal to k (depth/length).
After adding curr to output, we generate all available variations by
using backtracking => for loop(first, n) + curr.pop()
------------------------------------------------------------------------
'''
class Solution(object):
    def subsets(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

'''
------------------------------------------------------------------------
Solution 4: Backtracking, simplified
Time: O(n*2^n) => generate all subsets and then copy them into output list.
Space: O(n) => We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking.

Runtime: 30 ms
Memory: 13.7 MB

This is a simplified version of the backtracking solution. This solution gets
rid of the for loop around the backtrack function, making it more similar
to the recursive solution #1.
------------------------------------------------------------------------
'''
class Solution(object):
    def subsets(self, nums):
        def backTrack(start, cur_list):
            ans.append(cur_list[:])

            for j in range(start, n):
                cur_list.append(nums[j])
                backTrack(j+1, cur_list)
                cur_list.pop()

        n = len(nums)
        ans = []

        backTrack(0, [])

        return ans