'''
------------------
Difficulty: Medium
------------------

You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5] 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
'''

'''
------------------------------------------------------------------------
Solution 1: Iteration
Time: O(h) -> height of the tree, can also be noted as O(logn)
Space: O(1)

Runtime: 107 ms
Memory: 17.5 MB

This is an iterative solution insert a new node into the BST. We keep
track of the parent node while doing the binary search within the tree,
so that we can later use it to decide whether the new node should be
added to its left or right. Since it's guarenteed that the node values
are unique, it will always be the case that there is a specific location
the new node should be added under the existing tree structure.
------------------------------------------------------------------------
'''
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        parent = None
        curr = root
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root

'''
------------------------------------------------------------------------
Solution 2: Recursion
Time: O(h)
Space: O(h) -> recursion stack

Runtime: 117 ms
Memory: 17.5 MB

This is a recursive solution that essentially does the same thing but
by calling the function recursively. It's way more concise but sacrifices
space complexity due to the recursive call stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root