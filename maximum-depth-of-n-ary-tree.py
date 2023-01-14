'''
------------------
Difficulty: Easy
------------------

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:

The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(logn) average case -> height of the tree, O(n) worst case -> completely unbalanced

Runtime: 27 ms
Memory: 16.5 MB

This is a straightforward recursive solution that updates the global variable
res (maximum depth) in each recursive call. Basically, we want to traverse
all the nodes in the tree like we did in other problems, but this time
we want to try updating the max depth in each call with the level parameter
we pass.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxDepth(self, root):
        self.res = 0
        
        def traverse_nodes(node, level):
            self.res = max(self.res, level)
            for child in node.children:
                traverse_nodes(child, level+1)
        
        if not root:
            return self.res
        else:
            traverse_nodes(root, 1)
        return self.res

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n)
Space: O(n)

Runtime: 20 ms
Memory: 16.4 MB

This is an iterative solution that basically mimics the recursive stack in
solution 1 by explicitly using the stack data structure. Otherwise, the
underlying intuition is the same.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        stack = [(root, 1)]
        res = 0
        
        while stack:
            node, level = stack.pop()
            res = max(res, level)
            for child in node.children:
                stack.append((child, level+1))
        
        return res