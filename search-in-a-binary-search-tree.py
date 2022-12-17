'''
------------------
Difficulty: Easy
------------------

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null. 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(h) -> h is height of tree. O(logn) average case, O(n) worst case.
Space: O(h) -> same logic for average and worst case.

Runtime: 62 ms
Memory: 17.3 MB

This is a pretty straightforward recursive solution. Always remember
that in recursion, you must expect the recursive call to return the
exact thing you would like to get returned.

Base case is when the current node is None or the target node we were looking for.
It is safe to just return root when root is None because, since this is a
binary tree where we look at root.left when root.val > val and look at right
when root.val < val, if we're reached a leaf node it means the BST does not
have a root with our target value.
------------------------------------------------------------------------
'''
class Solution(object):
    def searchBST(self, root, val):
        if root is None or root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(h)
Space: O(1)

Runtime: 67 ms
Memory: 17.5 MB

This is also a straightforward iterative solution. According to the
while loop condition, the loop will only end when current node is None
or we've found the target node. Until that point, we keep traversing
to either left or right depending on root.val.
------------------------------------------------------------------------
'''
class Solution(object):
    def searchBST(self, root, val):
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        
        return root