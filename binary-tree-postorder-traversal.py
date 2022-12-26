'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1] 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n)

Runtime: 15 ms
Memory: 13.2 MB

This is a straightforward recursive solution to traverse a binary tree
in postorder. This has the same intuition as the preorder and inorder
problems, where we breakdown the subtrees into subproblems.

Just note that, in postorder traversal, you will have to add the value
of root after traversing and processing the left subtree and the right subtree.
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        def dfs(root):
            if root is None:
                return root
            
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
            
        res = []
        dfs(root)
        return res

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n)
Space: O(n)

Runtime: 10 ms
Memory: 13.4 MB

This is a much more complicated iterative solution to traverse a binary tree
in postorder. In order to traverse in postorder, we should be able to add the
values of the left child and right child before the root node.

The way we're going to do that is by appending a tuple to the stack, where
the first element of the tuple is the root node and the second one is whether
it's been visited or not. We're always going to mark the root node as visited
and add to the stack before left and right. This way, when we're adding
the visited nodes to the result array, left nodes will be added first, then right
nodes, and then finally the parent node.
------------------------------------------------------------------------
'''
class Solution(object):
    def postorderTraversal(self, root):
        res, stack = [], [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    res.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res