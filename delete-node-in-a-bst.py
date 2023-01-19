'''
------------------
Difficulty: Medium
------------------

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(logn) = O(h)
Space: O(h) -> recursion stack

Runtime: 59 ms
Memory: 21.4 MB

3 BST Pro Tips:
  - Inorder traversal of BST is an array sorted in the ascending order.
  - To find a successor, go to the right once and then as many times to the left as you could.
  - To find a predecessor, go to the left once and then as many times to the right as you could.

Deleting a node in BST is more complicated than just searching and inserting a node.
However, if you understand the strategy, it's not as hard as you think.
First, generally there are three cases:
  - (1) target node is a leaf node
  - (2) target node only has one child
  - (3) target node has both children

(1) We simply remove the node
(2) We swap the target node with its child, and delete target node
(3) We swap the target node with its inorder successor, and delete the target node

Using binary search style traversal, we recursively call the deleteNode function
until we find the target node. Again, (1) if it's a leaf node, return None.
(2) if it has a right child, swap with successor and delete it on the right
(2) if it has no right child, and has only left child, swap with predecessor
and delete it on the left
------------------------------------------------------------------------
'''
class Solution:
    # One step right and then always left
    def successor(self, root):
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
    # One step left and then always right
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

'''
------------------------------------------------------------------------
Solution 2: Recursion
Time: O(logn)
Space: O(h)

Runtime: 51 ms
Memory: 21.6 MB

This recursive solution uses the same intuition as solution 1, but
implements the logic more concisely. This is also a binary-search style
recursive traversal until you find the target node.

Once you find the target node, process the 3 cases presented before in
(2)(1)(3) order. To be precise, (1) and (2) are taken care of at the same
time because, for a leaf node, if you return root.left when you don't have
root.right, it's going to return None anyways.

For case (3), we're simply going to find the inorder successor, swap it with
the target node, and delete the original successor node on root.right.
------------------------------------------------------------------------
'''
class Solution(object):
    def deleteNode(self, root, key):
        if not root: return None

        if root.val == key:
            if not root.right: return root.left
            
            if not root.left: return root.right
            
            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root