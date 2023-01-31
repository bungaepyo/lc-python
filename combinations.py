'''
------------------
Difficulty: Medium
------------------

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order. 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination. 

Constraints:

1 <= n <= 20
1 <= k <= n
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking
Time: O(k*nCk) -> we are doing n Choose k O(nCk), and copying the curr array O(k)
Space: O(nCk) -> keep all the combinations for an output

Runtime: 408 ms
Memory: 15 MB

According to the problem description, we are going to have to return "all"
possible solutions that chooses k numbers from [1,n] range, without duplicates.
These are combinations, not permutations, so [1,2] and [2,1] are considered duplicates.

Since we need to explore "all" possible solutions, we are going to have to
iterate through some numbers but doing it in pure brute force should be inefficient.
Also, it's not really possible because you can't increase/decrease the
number of for loops depending on k.

Therefore, we're going to have to choose a method that allows us to add
numbers to a temporary array one by one, and add that temporary array
to the final array when its length is equal to k. Since this array is
temporary, we should be able to roll back our number selections. This
sounds just like backtracking! Backtracking allows us to advance towards
the final solution one by one, and revert as soon as we discover that
current solution is not valid.

Base case of the backtracking algorithm should be when the current array's
length is equal to k, after which we have no reason to further proceed.
If base case is not met, we're going to have to try adding all possible
numbers from starting number to n, advanding one by one. We append it,
recursively call backtrack(i+1, curr), and backtrack afterwards so we can
reuse the curr array with different combinations.
------------------------------------------------------------------------
'''
class Solution(object):
    def combine(self, n, k):
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()

        res = []
        backtrack()
        return res