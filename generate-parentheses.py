'''
------------------
Difficulty: Medium
------------------

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
'''

'''
------------------------------------------------------------------------
Solution 1 - Backtracking / Recursion
Time: O((4^n)/(n^1/2))
Space: O((4^n)/(n^1/2))

Runtime: 20 ms
Memory: 13.8 MB

The backtracking solution is most commonly used to solve this problem.
We need to acknowledge 2 concepts in order to understand this solution.
(1) we can start an opening bracket as long as we still have one (of n) left to place.
(2) we can start a closing bracket if it wouldn't exceed the number of opening brackets.

In this problem, since there is only 1 type of bracket, you can add as many opening brackets
as long as total number is under n, and as many closing as long as current number doesn't
exceed the number of opening brackets.
List S is used as a staging list whose value (parentheses combination) gets appended to ans
when the length reaches 2*n, meaning there are no  more brackets to add.

Because of the order of the recursive calls + S.pop() on the line right below,
the backtracking logic generates all valid parentheses combinations while
adding to ans whenever a full combination has been reached.
------------------------------------------------------------------------
'''
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
        