'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursion
Time: O(n)
Space: O(n)

Runtime: 23 ms
Memory: 15.9 MB

This is a simple recursive solution. Base case is when current node does
not exist, and we always return 1 + bigger of left and right result.
Note that this could lead to a stack overflow issue when recursive depth
is large, but tail recursion optimization is not supported by Python.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''
------------------------------------------------------------------------
Solution 1.1 - Recursion
Time: O(n)
Space: O(n)

Runtime: 28 ms
Memory: 16.1 MB

This is a variation of the recursive solution, where we use a global
variable to keep track of the maximum depth of the binary tree.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxDepth(self, root):
        self.res = 0
        self.helper(root, 1)
        return self.res
    
    def helper(self, node, depth):
        if node is None:
            return None
        
        if node.left is None and node.right is None:
            self.res = max(self.res, depth)
        
        self.helper(node.left, depth+1)
        self.helper(node.right, depth+1)

'''
------------------------------------------------------------------------
Solution 2 - Iteration
Time: O(n)
Space: O(n)

Runtime: 21 ms
Memory: 15.8 MB

This is an iterative solution that uses the stack data structure to mimic
the process of a recursive call stack. Note that we are using a global variable
"depth" to keep track of the maximum depth in the binary tree.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        stack = []
        if root is not None:
            stack.append((1, root))
        
        while stack:
            curr_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, curr_depth)
                stack.append((curr_depth+1, root.left))
                stack.append((curr_depth+1, root.right))
        
        return depth