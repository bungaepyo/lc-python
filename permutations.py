'''
------------------
Difficulty: Medium
------------------

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
 
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(∑ P(N,k)) -> k=1 ~ N (???)
Space: O(N!) -> needs to keep N! solutions

Runtime: 43 ms
Memory: 13.9 MB

This is a solution using the recursion method. Whenever the length of nums
is 1 or 0, there is no further permutations. Thus, return [nums].
The recursive backtracking is implemented using a helper function.

Main logic is here: iterate through initial list and pass in each element as
arrays, and rest of nums as well.

Using curr (initial array) and leftover (rest of nums), we add it to the
results if there is no leftover. Otherwise, we keep doing the main logic until
there is no leftover. This way, we can cover all permutations.
------------------------------------------------------------------------
'''
class Solution(object):
    def permute(self, nums):
        if(len(nums) == 0 or len(nums) == 1):
            return [nums]

        res = []
        
        def helper(curr, leftover):
            if len(leftover) == 0:
                res.append(curr)
                return

            for index, number in enumerate(leftover):
                s = curr[:]
                s.append(number)
                helper(s, [j for i,j in enumerate(leftover) if i != index])

        for idx, num in enumerate(nums):
            helper([num], [y for x, y in enumerate(nums) if x != idx])

        return res

'''
------------------------------------------------------------------------
Solution 2: Backtracking
Time: O(∑ P(N,k)) -> k=1 ~ N (???)
Space: O(N!) -> needs to keep N! solutions

Runtime: 49 ms
Memory: 13.7 MB

This is a solution using the backtracking method. Slightly less straightforward
than the normal recursive approach. Before we run the backtrack subfunction,
we create a result array.
The key to this backtracking solution is the following:
- During the backtrack function, if "first" is equal to length of nums
  (meaning there is was more possible swaps in the recursive call one level above),
  add the current nums[:] (hard copy) to the result array.
- In the for loop ("first" to n), we temporarily swap i with "first" to
  give a chance to calculate all permutations when i is the first element.
  (backtrack first+1)
- We swap back (backtrack) the temporarily swapped i and "first" in order to 
  do the same thing with the next i in the for loop. Remember we are using
  nums in place to add permuted lists to result array.
------------------------------------------------------------------------
'''
class Solution(object):
    def permute(self, nums):
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output