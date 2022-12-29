'''
------------------
Difficulty: Medium
------------------

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL. 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate
each next pointer to point to its next right node, just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space
does not count as extra space for this problem.
'''

'''
------------------------------------------------------------------------
Solution 1: Level Order Traversal
Time: O(n)
Space: O(n)

Runtime: 36 ms
Memory: 16.1 MB

Given that the provided binary tree is not necessaily perfect, we need to
take a BFS approach rather than a DFS approach, processing all the nodes
on the same level before we go on to the next level.

In order to take the BFS approach, we should be able to (1) iterate all levels
(2) iterate all nodes in each level. A typical data structure used in BFS
context that allows FIFO is a double ended queue. With a deque, we should be
able to achieve both (1) and (2) by using a nested loop. The first loop would
iterate each levels, and the second loop would iterate all the nodes within that level.

Starting with the initial queue with only root in it, each time we process a new level,
we measure the size of the queue so that we can only iterate the size amount
of nodes in the queue. We'll be appending children nodes at the end of the queue
so this process is necessary.

Each time we process a node, if it's smaller than size-1, we direct its next
pointer to the first element in the queue, which should be the next node
in the same level.
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

        queue = deque([root])
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size-1:
                    node.next = queue[0]                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return root

'''
------------------------------------------------------------------------
Solution 2: Usig previously established next pointers
Time: O(n)
Space: O(1)

Runtime: 32 ms
Memory: 16 MB

Although the first solution is great, we should be able to reduce on space
complexity according to the problem description. If we use previously established
next pointers (establish next pointers on N+1 while in N), we are able to
reduce space complexity by not having to use a queue.
------------------------------------------------------------------------
'''
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root 

    def processChild(self, childNode, prev, leftmost):
        if childNode:
            
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:    
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode 
        return prev, leftmost