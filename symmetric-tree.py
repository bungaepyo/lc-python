'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''

'''
------------------------------------------------------------------------
Solution 1 - Iteration
Time: O(n)
Space: O(n)

Runtime: 15 ms
Memory: 13.6 MB

This is an iterative solution to check if a binary tree is symmetrical to its center.
Since we want to test symmetry from the higher levels, we'd like to process
the nodes in FIFO order, thus we have to use a queue (double ended queue).

We're going to have to compare two nodes in each iteration of the while loop (one from left one from right),
so we pop two nodes from the queue and check the validity of the given level.
If only one of the two nodes are None, or if their values don't match, we know
it's not a symmetry anymore.

One key thing to note is that we need to add nodes to the queue in the order
we want to compare. node1.left -> node2.right -> node1.right -> node2.left
------------------------------------------------------------------------
'''
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        queue = deque([root.left, root.right])
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        return True

'''
------------------------------------------------------------------------
Solution 2 - Recursion
Time: O(n)
Space: O(n)

Runtime: 29 ms
Memory: 13.5 MB

The base intuition of the recursive function is the same as that of the
iterative function. However, we recursively call the helper function
with the nodes we want to compare (node1.left, node2.right) & (node1.right, node2.left)
------------------------------------------------------------------------
'''
class Solution(object):
    def isSymmetric(self, root):
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return helper(node1.left, node2.right) and helper(node1.right, node2.left)
        
        return helper(root, root)