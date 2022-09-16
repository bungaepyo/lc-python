'''
------------------
Difficulty: Easy
------------------

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1] 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

REFERENCE:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

'''
------------------------------------------------------------------------
Solution 1: Recursive Approach
Time: O(n) -> recursive function is T(n) = 2⋅T(n/2) + 1
Space: O(n) -> worst case n & average logn, n is number of nodes

Runtime: 18 ms
Memory: 13.4 MB

This is the most intuitive recursive approach to traverse a binary tree inorder.
At first, traversing a tree might sound very unintuitive, but seeing through
the lens of recursion makes it easier to understand.
Using a helper function (to pass in a list to return at the end),
you make recursive calls in this order:
  - LEFT -> ROOT -> RIGHT (this is typical of inorder traversal)
This call would first add the leftmost node, then its root, then root's right,
then root of root, then right of root of root, and so on.
------------------------------------------------------------------------
'''
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root != None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

'''
------------------------------------------------------------------------
Solution 2: Iterative Approach using Stack
Time: O(n)
Space: O(n)

Runtime: 40 ms
Memory: 13.2 MB

This is an iterative solution using a stack, which is slightly more complicated.
res is a result array, and stack is where we keep nodes that we need to use as
root later on.
In the while loop, we keep traversing to left while adding roots to stack until we reach an end (a.k.a curr == None).
Once we reach an end, we pop from the stack and add to result array, and then update
current node to the right of current node.
  - If right is empty, it will automatically pop from the stack
  - If right is not empty, it will go through that inner while loop to add all the leftmost nodes.
------------------------------------------------------------------------
'''
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res

'''
------------------------------------------------------------------------
Solution 3: Morris Traversal
Time: O(n)
Space: O(1)

Runtime: 26 ms
Memory: 13.3 MB

This is a solution using a method called the Morris Traversal, and this uses
a new data structure called the threaded binary tree.
In this scenario, threaded binary tree is achieved by re-shaping the original
binary tree. If there is a left node to the current root, you make current root
the rightmost child of the left node's subtree.
Thus, we will get something that looks like this:
         2
        / \
       4   5
            \
             1
              \
               3
              /
             6
Do wrap up, you do the same to node 4 resulting in something like:
        4
         \
          2
           \
            5
             \
              1
               \
                3
               /
              6
While adding nodes to the result array because they don't have curr.left,
you will encounter node 3, and will run the else statement once more to
swap the order of 3 and 6 so that inorder traversal is complete.
------------------------------------------------------------------------
'''
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        curr = root
        
        while curr != None:
            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right != None:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return res