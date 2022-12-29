'''
------------------
Difficulty: Medium
------------------

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(h) -> average case O(h), worst case O(n)

Runtime: 48 ms
Memory: 25.4 MB

This is a recursive solution to find the lowest common ancestor in a binary tree.
First intuition we should have is that, while searching for p and q, there
could be two scenarios:
  - (1) current node is p or q
  - (2) current node is not p and not q

Case 1: If current node is p or q, it's safe to just return the current node.
        - if the current node is not the lowest common ancestor, we need to return
          current node to make evaluations in the future
  ***** - if the current node is the lowest comon ancestor, we just need to return
          current node because any other route that doesn't involve current node will
          return None. Since python objects evaluate to True, current node will be
          returned at (return left or right) statement

Case 2: If current node is not p and not q, we need to continue our search.
        Since we don't know yet if p or q will be one of the descendents,
        we need to (return left or right) so that if we find one, it will be pased,
        and if we didn't find one, it will evaluate to False.
------------------------------------------------------------------------
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        #root is not p or q after this
        if root == p or root == q:
            return root
        
        #these are either None or TreeNode
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            #python objects are truthy
            return left or right

'''
------------------------------------------------------------------------
Solution 2: Itertative, using parent pointer
Time: O(n)
Space: O(n)

Runtime: 55 ms
Memory: 21.2 MB

This is an iterative solution using the stack data structure. The underlying
intuition of this solution is to add all the {node:parent} pairs to a dictionary
until both {p:parent} and {q:parenr} are added, so that we can later track
them down.

Once all parents are added, we will start adding p's ancestors to a set on
first pass and q's ancestors on the second pass. The first node that we find
already exists in the set is the LCA node.
------------------------------------------------------------------------
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        
        parent = {root: None}
        
        while p not in parent or q not in parent:
            
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        return q