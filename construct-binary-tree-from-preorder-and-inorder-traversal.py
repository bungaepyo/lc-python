'''
------------------
Difficulty: Medium
------------------

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1] 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion, using deque
Time: O(n)
Space: O(n)

Runtime: 32 ms
Memory: 18 MB

This recursive solution has the same intuition as the inorder & postorder
problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

However, we are using a double ended queue data structure because of the
way preorder traversal stores data. We need a way to access the elements
from the left, not from the right.
------------------------------------------------------------------------
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = queue.popleft()
            root = TreeNode(val)
            
            index = hashmap[val]
            root.left = helper(in_left, index-1)
            root.right = helper(index+1, in_right)
            
            return root
        
        queue = deque(preorder)
        hashmap = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)

'''
------------------------------------------------------------------------
Solution 2: Recursion, using global variable
Time: O(n)
Space: O(n)

Runtime: 26 ms
Memory: 18.8 MB

This solution is an alternative version of solution 1, using a global
variable instead of using a double ended queue. Essentially, we only need
a way to access elements of the preorder array from the left.
------------------------------------------------------------------------
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = preorder[self.root_index]
            root = TreeNode(val)
            
            self.root_index += 1
            
            index = hashmap[val]
            root.left = helper(in_left, index-1)
            root.right = helper(index+1, in_right)
            
            return root
        
        self.root_index = 0
        hashmap = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)