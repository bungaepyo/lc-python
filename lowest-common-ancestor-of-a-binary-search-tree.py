'''
------------------
Difficulty: Medium
------------------

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion, Binary Tree
Time: O(n)
Space: O(h) -> average case, worst case O(n)

Runtime: 70 ms
Memory: 21.6 MB

This is a recursive solution that does not utilize the characteristics of
BST, so it is applicable to normal binary trees as well.

The base case is when root is None, which could either represent an empty BST
or a leaf node, in which case we should both return None.

During our recursive search, there are two scenarios:
  - Scenario 1: current node is either p or q. We should return the current
                node because (1) if the other target node is on the other
                side of the tree, they're both gonna bubble up and meet at LCA
                (2) if both target nodes are under subtree starting from current
                node, current node is LCA. Python objects are truthy so they
                will bubble up and will be returned at the last "return left or right"
                statement when it reaches the root node.
  - Scenario 2: current node is not p or q. This means we need to continue
                searching towards the left and right side, recursively.
------------------------------------------------------------------------
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left or right

'''
------------------------------------------------------------------------
Solution 2: Recursion, Binary Search (BST)
Time: O(h) -> average case, worst case O(n)
Space: O(h) -> average case, wrost case O(n)

Runtime: 63 ms
Memory: 21.3 MB

This is a recursive solution that utilizes the characteristics of BST.
Finding LCA is BST is different from finding in a normal binary tree because,
given a target node, you know which way to proceed in order to find that node.

Therefore, we can simplify the logic a little further.
  - (1) if both p and q are smaller than current node, it's obvious that
        current node is not their LCA, so simply return the recursive result
        on root.left
  - (2) if both p and q are larger than current node, do the opposite of
        scenario 1.
  - (3) if one of p and q is larger than current node and the other is smaller,
        we've found a split. No matter where p or q is located on either sides,
        their LCA will be the current node because it will be the first node they
        meet when bubbling up. Return current node.
------------------------------------------------------------------------
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

'''
------------------------------------------------------------------------
Solution 3: Iteration, Binary Search (BST)
Time: O(h) -> average case, worst case O(n)
Space: O(1)

Runtime: 63 ms
Memory: 21.3 MB

This is a binary search style iterative solution, which is basically an
alternative version of solution 2.
------------------------------------------------------------------------
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root