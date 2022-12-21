'''
------------------
Difficulty: Medium
------------------

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order. 

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]] 

Constraints:

1 <= n <= 8
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(nGn) -> Gn is Catalan number explained in I version of this problem, and it's executed n times
Space: O(nGn) -> as we need to construct all possible trees

Runtime: 52 ms
Memory: 16.3 MB

Nice solution: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/929000/Recursive-solution-long-explanation

This is a solution that recursively constructs all possible trees, given n.
Coming up with this type of recursive solution is really hard but the concept
itself should not be that hard once you understand the underlying logic.

The main intuition we're using in this solution is the following:
  - given a root number i (among 1 ~ n, inclusively), all the numbers
    in the left subtree should be coming from (start, i-1) and all the numbers
    in the right subtree should be coming from (i+1, end).

Therefore, starting from the top-level and using the recurring relationship,
we need to iterate through the given range (since all integers in the range
should be able to become a root node) and:
  - (1) select a root
  - (2) recursively get all left subtrees
  - (3) recursively get all right subtrees
  - (4) in a nested for loop, connect all left and right subtrees to the root
  - (5) return the list of all connected subtrees
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        return self.helper(1, n)
    
    def helper(self, start, end):
        # base & edge case when (start, start-1) or (end+1, end)
        if start > end:
            return [None]
        
        all_trees = []
        for rootVal in range(start, end+1):
            left_trees = self.helper(start, rootVal-1)
            right_trees = self.helper(rootVal+1, end)
            
            for left in left_trees:
                for right in right_trees:
                    curr = TreeNode(rootVal)
                    curr.left = left
                    curr.right = right
                    
                    all_trees.append(curr)
        
        return all_trees