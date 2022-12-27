'''
------------------
Difficulty: Medium
------------------

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1: Queue, Iteration
Time: O(n)
Space: O(n)

Runtime: 11 ms
Memory: 13.9 MB

This is an iterative BFS solution using the double-ended queue data structure.
The objective of this problem is pretty straightforward:
  - we should be able to iterate through the binary tree level by level
    and return same-level node values in the same subarray.

The perfect data structure for this is the double-ended queue. Since we can
pop elements from the left, if we are able to add elements in the order we
want them to be processed, adding them to the result array should not be a problem.

In order to achieve the desired order, we are going to (1) process the root node
(2) add the left and right child of root to the queue (3) popleft() from the queue in the future.
When appending to the queue, if we add a (node, level) tuple, we are able
to detect which level the popped node should belong to, and add it to the
corresponding index in the result array.
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) > level:
                    res[level].append(node.val)
                else:
                    res.append([node.val])
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        
        return res

'''
------------------------------------------------------------------------
Solution 2: Recursion
Time: O(n)
Space: O(n)

Runtime: 16 ms
Memory: 14.2 MB

This is a recursive solution that iterates binary tree in level order.
The intuition here is not too different from the iterative solution, but
in fact the visit order is not bfs but is dfs. Therefore, the recursive solution
does not traverse nodes in level order, but produces the same output.

One key thing to remember here is to always check len(res) == level and add an
empty array if it's True, otherwise index would be out of range when res[level].append().
------------------------------------------------------------------------
'''
class Solution(object):
    def levelOrder(self, root):
        def helper(root, level):
            if not root:
                return root
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
            
        
        res = []
        helper(root, 0)
        return res