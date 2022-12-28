'''
------------------
Difficulty: Medium
------------------

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1] 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n)

Runtime: 39 ms
Memory: 18.2 MB

It's really hard to come up with a working solution if you've never seen
these types of questions. The key here is to understand the way that each
traversal methods store data.

With regards to inorder and postorder traversal, these are the characteristics:
  - In-order: given a root node value, to the left is the left subtree and
              to the right is the right subtree
  - Post-order: if you iterate from the back, you'll encounter all the
                right nodes first, and then the left nodes

Utilizing these characteristics, we are going to build a binary tree.
Key here is to use postorder array for iteration and inorder array
for identifying the left and right tree.

Base case is when the left and right boundaries given to the inorder array
do not overlap, thus there is no subtree available.

We pop from the postorder array, which is going to be the value of our root node.
We are able to checkout the left and right subtrees of this root by finding
its position in the inorder array. If there are any elements left to it,
it means it has a left subtree. Same with the right elements.

Finally, we construct the right subtree first because, when accessing values
in reverse order of the postorder array, we'll encounter right nodes first.
------------------------------------------------------------------------
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(in_left, in_right):
            #if there is nothing to build
            if in_left > in_right:
                return None
            
            #pop the root node
            val = postorder.pop()
            root = TreeNode(val)
            
            #root splits inorder list into left and right subtrees
            index = hashmap[val]
            
            #left and right subtrees
            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            
            return root
        
        hashmap = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)