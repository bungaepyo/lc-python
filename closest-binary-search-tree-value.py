'''
------------------
Difficulty: Easy
------------------

Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.

Example 1:

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:

Input: root = [1], target = 4.428571
Output: 1 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursive inorder traversal + lienar search
Time: O(n)
Space: O(n)

Runtime: 80 ms
Memory: 17.1 MB

This is a simple stupid 3 liner solution that tries to identify the closest
element to target by generating a sorted array (of node values).
In tree problems like these, you wouldn't be able to access all the node
values at once to compare because you are only given the root node.

However, using the characteristics of a inorder traversal that will return
binary search tree nodes in ascending order, we are able to generate a sorted array.
Within this sorted array, we can simply find the element with minimum absolute
distance to the target.

Although this solution could be intuitive, the time and space complexity isn't optimal
because we are doing linear search and using up space for the linear data structure.
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        return min(inorder(root), key = lambda x: abs(x-target))

'''
------------------------------------------------------------------------
Solution 2 - Iterative inorder traversal
Time: O(k) -> O(k) in average case and O(k+h) in worst case. k is index of closest element.
Space: O(h) -> worst case non-balanced tree

Note: time complexity is O(k) on average case because you would be pushing k
      elements into the stack and popping k elements out of the stack O(2k).
      Time compl is O(k+h) on worst case if it is a completely unbalanced tree (only left child)
      where you would have to push h elements into the stack and pop k elements out.

Runtime: 33 ms
Memory: 17.6 MB

This is a iterative inorder traversal solution using a stack that optimizes
the recursive version in solution 1 in two ways:
  - (1) this merges two steps of traversing the tree and finding the closest value
  - (2) since inorder traversal allows you to traverse values in ascending order,
        you would be able to stop once you find that nums[i] <= target < nums[i + 1].
        The closest value will be either nums[i] or nums[i+1].
------------------------------------------------------------------------
'''
class Solution(object):
    def closestValue(self, root, target):
        stack = []
        pred = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target-x))
            
            pred = root.val
            root = root.right
        
        return pred

'''
------------------------------------------------------------------------
Solution 3 - Binary Search
Time: O(h) -> h is tree height
Space: O(1)

Runtime: 21 ms
Memory: 17.3 MB

This is a solution using the binary search algorithm. Basically, the intuition
is that we keep track of the closest value using a global variable, and
proceed only towards the side (left or right) that could possibly be closer to target.

For example, [4,2,5] & target = 3.7
  - (1) we set root as the initial closest value
  - (2) we update the closest var by comparing root.val and current closest
  - (3) we proceed to left if target is smaller than current root, and proceed
        to the right otherwise.
This makes sense because, if the target is smaller than current root value,
it is more probable that left side of BST (with smaller values) are closer to it.
The right side nodes are not eligible anymore because, again if target is
smaller than root, root will be closer to target than any other right side node.
------------------------------------------------------------------------
'''
class Solution(object):
    def closestValue(self, root, target):
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest