'''
------------------
Difficulty: Medium
------------------

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
'''

'''
------------------------------------------------------------------------
Solution 1: BFS, iteration, queue
Time: O(n)
Space: O(n)

Runtime: 32 ms
Memory: 16.6 MB

This is a classic BFS traversal problem, which can be easily solved using
a double-ended queue data structure. There are 4 steps for it:
  - (1) we need to do a BFS method, using a double ended queue
  - (2) when we put nodes into the queue, insert a tuple (node, level)
  - (3) when we pop nodes from the queue, add value to the corresponding level array
  - (4) levels should start from 0, due to 0-indexed arrays
------------------------------------------------------------------------
'''
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return root
        
        queue = deque([(root, 0)])
        res = []
        
        while queue:
            node, level = queue.popleft()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        
        return res

'''
------------------------------------------------------------------------
Solution 1: BFS, iteration, queue
Time: O(n)
Space: O(logn) average case, O(n) worst case -> runtime stack

Runtime: 37 ms
Memory: 16.5 MB

This is a recursive solution that implements the same intuition using
a recursive helper function.
------------------------------------------------------------------------
'''
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return root
        
        def traverse_nodes(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                traverse_nodes(child, level+1)
        
        res = []
        traverse_nodes(root, 0)
        
        return res