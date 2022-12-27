'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths. 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursion
Time: O(n)
Space: O(n) -> worst case O(n) when completely unbalanced, average case O(logn)

Runtime: 20 ms
Memory: 15.5 MB

Finding a root-to-leaf path that has a pathSum that equals to the targetSum
can be implemented by using a recursive method that passes (targetSum - currentSum)
as a parameter going down each level of the binary tree.

The base case in this scenario is, whenever we encounter a leaf node, checking
whether or not the given leaf node has the same value as the remaining targetSum.

The edge case here is when the root node does not exist, thus cannot add up
anything towards the targetSum.
------------------------------------------------------------------------
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        targetSum -= root.val
        
        if (not root.left and not root.right):
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


'''
------------------------------------------------------------------------
Solution 2 - Iteration
Time: O(n)
Space: O(n) -> worst case O(n) when completely unbalanced, average case O(logn)

Runtime: 36 ms
Memory: 15.1 MB

This is an iterative solution that uses a stack data structure to imitate
the recursion stack. The underlying intuition is not different.
------------------------------------------------------------------------
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        stack = [(root, targetSum-root.val)]
        
        while stack:
            node, currSum = stack.pop()
            if not node.left and not node.right and currSum == 0:
                return True
            if node.left:
                stack.append((node.left, currSum-node.left.val))
            if node.right:
                stack.append((node.right, currSum-node.right.val))
        
        return False