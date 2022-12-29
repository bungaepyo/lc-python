'''
------------------
Difficulty: Medium
------------------

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node,
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000


Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion, use existing pointer
Time: O(n)
Space: O(n) -> O(1) if excluding recursion stack

Runtime: 35 ms
Memory: 16.4 MB

This is a recursive solution, that could be easily implemented once you get
the intuition that you need to use the existing next pointer, if there are any.

If you connect the root's left to right and root's right to root's next's left,
the recursive structure will cover all the next pointers.

"We only move on to the level N+1 when we are done establishing the next pointers
for the level N. Since we have access to all the nodes on a particular level
via the next pointers, we can use these next pointers to establish the connections
for the next level or the level containing their children."
------------------------------------------------------------------------
'''
#Definition for a Node.
#class Node(object):
#    def __init__(self, val=0, left=None, right=None, next=None):
#        self.val = val
#        self.left = left
#        self.right = right
#        self.next = next
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        
        if not root.left:
            return root
        
        if root.next:
            root.right.next = root.next.left

        root.left.next = root.right
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root

'''
------------------------------------------------------------------------
Solution 2: Iteration, use existing pointer
Time: O(n)
Space: O(1)

Runtime: 46 ms
Memory: 16.2 MB

This iterative solution has the same underlying intution as the recursive
solution, but establishes connections in a BFS style while the recursive
solution establishes in a DFS style.

Here, since a perfect binary tree is given, we iterate the BFS style loop
by using leftmost.left (this will be None after final level).

Then, starting from the leftmost node, we establish two connections:
  - (1) left.next = right
  - (2) right.next = next.left -> only if there is next

After this, we update head to head.next so that we can cover all other
nodes on the same level.
------------------------------------------------------------------------
'''
class Solution:
    def connect(self, root):
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root