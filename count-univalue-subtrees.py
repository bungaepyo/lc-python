'''
------------------
Difficulty: Medium
------------------

Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.

Example 1:

Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6 

Constraints:

The number of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1: DFS
Time: O(n)
Space: O(h) -> size of dfs recursive stack can't go over tree's height

Runtime: 27 ms
Memory: 13.5 MB

Key intuitions for solving this problem in DFS:
  - (1) all leaf nodes count as univalue subtree
  - (2) all child nodes must be univalue in order to count "subtree starting
        from a node" towards univalue subtree

Given a leaf node as base case that adds up 1 to the total count, it isn't
hard to begin a bottom-up recursive approach. However, the tricky part is
intuition (2) where we need to keep track of whether all child nodes are univalue
or not.

We do this by setting up a is_uni local boolean variable, and letting node.left and
node.right (if there are any) update the boolean. Assuming a subtree has both
node.left and node.right, in order to count as an univalue subtree:
  - (1) both left and right subtrees must be univalue
  - (2) both values of node.left and node.right should be equal to node.val

Thus, we add 1 to the total count in the following scenarios:
  - (1) when it's a leaf node
  - (2) when a node meets all subtree requirements
------------------------------------------------------------------------
'''
class Solution(object):
    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        self.count = 0
        self.helper(root)
        return self.count
    
    def helper(self, node):
        
        if not node.left and not node.right:
            self.count += 1
            return True
        
        is_uni = True
        
        if node.left:
            is_uni = self.helper(node.left) and node.left.val == node.val and is_uni
        if node.right:
            is_uni = self.helper(node.right) and node.right.val == node.val and is_uni
        
        self.count += is_uni
        return is_uni


'''
------------------------------------------------------------------------
Solution 2: DFS, pass parent value
Time: O(n)
Space: O(h) -> size of dfs recursive stack can't go over tree's height

Runtime: 16 ms
Memory: 13.4 MB

This is an alternative dfs solution where we pass the parent's value to
recursively check if it's a valid subtree for the parent. In every recursive
iteration:
  - if leaf node, add 1 and return node.val == parentVal
  - if not leaf node, check if left and right are valid
    - if both valid, add 1 and return node.val == parentVal
    - if not valid, return False
------------------------------------------------------------------------
'''
class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count
    
    def is_valid_part(self, node, parentVal):
        
        if not node:
            return True
        
        left = self.is_valid_part(node.left, node.val)
        right = self.is_valid_part(node.right, node.val)
        
        if not left or not right:
            return False
        
        # At this point, we know it's a valid univalue subtree
        # for node.val. Increment total count, and pass if it's
        # valid subtree for parent's val.
        self.count += 1
        return node.val == parentVal