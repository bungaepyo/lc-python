'''
------------------
Difficulty: Easy
------------------

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples) 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n)

Runtime: 28 ms
Memory: 16.5 MB

This is a recursive solution to preorder traverse all of the nodes in a
n-ary tree.
  - Base case would be when the root does not exist
  - We initiate a new array with root's value in every call, and add all
    the children's recursive outputs to that array, and return it.
  - Note that we add the root.val before we process any of the children
    in order to keep the traversal preorder.
------------------------------------------------------------------------
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        if not root:
            return root
        
        res = [root.val]
        
        for child in root.children:
            res += self.preorder(child)
        
        return res

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n)
Space: O(n)

Runtime: 28 ms
Memory: 16.5 MB

This is an iterative solution that uses a stack, which is the convention
for a DFS traversal. Unlike BFS, where you use a queue to FIFO, we need
to implement so that nodes in the stack are FILO.

Therefore, we pop from the right and add the value to result array,
and add extend the stack by adding its children in reverse order (so that
we can pop children from left to right).
------------------------------------------------------------------------
'''
class Solution(object):
    def preorder(self, root):
        if not root:
            return root
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        
        return res