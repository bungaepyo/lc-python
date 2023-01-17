'''
------------------
Difficulty: Medium
------------------

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursive Traversal + Iteration
Time: O(n)
Space: O(n)

Runtime: 57 ms
Memory: 21.6 MB

This is a very simple solution where you add all the inorder nodes in an array
and return the next node of p. This solution does pass all test cases, but
won't be accepted in interviews because it doesn't utilize the characteristics
of a BST.
------------------------------------------------------------------------
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node)
            inorder(node.right)
            
        inorder(root)
        
        for i in range(len(res)):
            if res[i].val == p.val:
                if i == len(res)-1:
                    return None
                else:
                    return res[i+1]

'''
------------------------------------------------------------------------
Solution 2: Iteration, Binary Search Style
Time: O(n)
Space: O(1)

Runtime: 57 ms
Memory: 21.7 MB

Think of this problem as a binary search in a sorted list. Since the constraints
of a BST allow it to be a sorted data structure (lower to the left higher to the right),
we are able to easily decide which way we should proceed if we know what
we're looking for.

Comparing the target node p's value and current node's value, we can
update the successor variable whenever we encounter a node whose value is
bigger than the target's value. We only do this because the inorder successor
of the target node should always have a greater value than target.
------------------------------------------------------------------------
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ