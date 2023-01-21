'''
------------------
Difficulty: Easy
------------------

Given a binary tree, determine if it is height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Top-Down Recursion
Time: O(nlogn) <- average/best case, worst case is O(n^2)
Space: O(n)

Time complexity: average case, we stop whenever we find an imbalanced subtree.
                 Thus, we perform O(n) getDepth function logn times. However,
                 in worst case when the tree is completely skewed, we'd have to check
                 all the nodes, therefore making the complexity O(n^2)

Runtime: 42 ms
Memory: 17.8 MB

This is a top-down recursive function. The underlying intuition is that
the current tree starting at root would return False is any of its left/right
subtrees are not balanced, or |leftDepth - rightDepth| > 1. We need a
separate helper function to calculate the height of the subtrees.
------------------------------------------------------------------------
'''
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getDepth(self, root):
        if not root:
            return 0
        left = 1 + self.getDepth(root.left)
        right = 1 + self.getDepth(root.right)
        return max(left, right)

'''
------------------------------------------------------------------------
Solution 2: Bottom-up Recursion
Time: O(n)
Space: O(n)

Runtime: 31 ms
Memory: 18 MB

This is a bottom-up recursive approach that essentially improves the
time complexity of solution 1. In the top-down approach, we had to call
the getDepth helper function on every parent node in order to see if
their left and right subtree depths' difference is greater than 1.

However, in this bottom-up approach we start from the leaf nodes in order
to utilize their depth and add on top of those to compute their parents'
depths. This allows us to get rid of the helper function.
------------------------------------------------------------------------
'''
class Solution(object):
    def helper(self, root):
        # An empty tree is balanced and has height 0
        if not root:
            return True, 0
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.helper(root.left)
        if not leftIsBalanced:
            return False, 1
        rightIsBalanced, rightHeight = self.helper(root.right)
        if not rightIsBalanced:
            return False, 1
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
    
    def isBalanced(self, root):
        return self.helper(root)[0]