'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1] 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n) -> recursive call stack (not using any extra space for variables since res is output array)

Runtime: 19 ms
Memory: 13.4 MB

This is a straightforward dfs preorder traversal of a binary tree.
Remember that, in preorder traversal, you need to visit the root node first
before going forward with visiting the left and right nodes. If we add the
root node values recursively in that order to a result array, the result
array will have all node values in preorder.
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):

        def dfs(root):
            if root is None:
                return root
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return res
        
        res = []
        dfs(root)
        return res

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n)
Space: O(n)

Runtime: 19 ms
Memory: 13.5 MB

This is an iterative solution for preorder traversal. The intuition is
similar to the recursive solution, but in the iterative approach we use a
stack data structure in order to imitate the recursive stack.

One thing to note here is to add the right child first to the stack
in order to access the left child first (FILO). We pop() starting from the last
element added to the stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        
        return res