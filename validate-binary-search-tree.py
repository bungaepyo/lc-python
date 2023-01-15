'''
------------------
Difficulty: Medium
------------------

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1: Recursive Traversal with Valid Range

Time: O(n)
Space: O(n) -> recursion stack holds all nodes in worst case

Runtime: 28 ms
Memory: 18.2 MB

This is the most standard way of validating a BST using the recursive method.
The most important characteristic of a BST is that "all" nodes to the right
must be greater than root and same for left. Thus, it's not only the direct child
node that should consider the root node's value.
Hence, we will use a recursive helper function to set up the boundaries for each call.

Base case: return True if root is None -> this means we've reached the leaf node
           without encountering any invalid nodes.
Constraint: if root.val is lower than or equal to the lower limit, return False.
            if root.val is greater than or equal to the higher limit, return False.

Key here is to update the low & high limits in the recursive call.
When we're making a call to root.left, we need to update the higher limit to root.val,
and if we're making ca call to root.right, we should update the higher limit to root.val.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidBST(self, root):
        def helper(root, low, high):
            if not root:
                return True
            if (low is not None and root.val <= low) or (high is not None and root.val >= high):
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root, None, None)

'''
------------------------------------------------------------------------
Solution 2: Iterative Traversal with Valid Range

Time: O(n)
Space: O(n) -> stack

Runtime: 34 ms
Memory: 17.9 MB

This is an iterative version of Solution 1, using a stack to track the nodes.
First, we initiate the stack with infinite boundaries, check validity, and
add root.right and root.left to the stack to perform the same.
Since the loop runs until the stack is empty (which means we've checked all nodes),
whether we add left or right first does not matter, and we return True at the end.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidBST(self, root):

        stack = [(root, None, None)]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            val = root.val
            if (low != None and val <= low) or (high != None and val >= high):
                return False
            stack.append((root.left, low, val))
            stack.append((root.right, val, high))

        return True

'''
------------------------------------------------------------------------
Solution 3: Recursive Inorder Traversal

Time: O(n)
Space: O(n)

Runtime: 33 ms
Memory: 18.4 MB

Inorder traversal is actually the perfect way to validate a BST since its
traversal order perfectly overlaps with BST's number value hierarchy.
Therefore, if we're doing an inorder traversal, we only need to check if
the current node is greater than the previous node (global variable).
First, we dig in to the left.
Second, we do a validity check for current node, and update prev.
Third, we go ahead and return the result of root.right recursive call to wrap up the recursive stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidBST(self, root):
        def helper(node):
            if not node:
                return True
            if not helper(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return helper(node.right)
        
        self.prev = float('-inf')
        return helper(root)

'''
------------------------------------------------------------------------
Solution 4: Iterative Inorder Traversal

Time: O(n)
Space: O(n)

Runtime: 29 ms
Memory: 17.7 MB

This is an iterative version of the inorder traversal solution, using a stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidBST(self, root):
        stack = []
        prev = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev != None and root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True