'''
------------------
Difficulty: Medium
------------------

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1] 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n) -> call stack

Runtime: 15 ms
Memory: 13.6 MB

This is a recursive solution to swap linked list nodes in pairs. Once
you get the intuition, it is pretty straightforward.

Since we're swapping nodes in pairs, we need at least two nodes in order
to swap the two adjacent nodes. Therefore, the base case would be when
head or head.next does not exist.

After this, we swap the first two nodes that we encounter.
Then, recursion kicks in. The next pointer of the latter node we swapped
should point to the result of recursion with original head.next.next as input.
------------------------------------------------------------------------
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        dummy = head.next
        tmp = head.next.next
        head.next.next = head
        head.next = self.swapPairs(tmp)
        
        return dummy
        
'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n)
Space: O(1)

Runtime: 23 ms
Memory: 13.4 MB

This is an iterative solution to swap the linked list nodes in pairs.
The intuition is basically same with the recursive approach, but here we
swap nodes on the go.

In order to make this iterative solution work, we need a variable prevNode
that acts like a linker between two swapped pairs in each iteration.

First, we define which nodes should be swapped.
Second, we swap the nodes.
Thirs, we reinitialize prevNode and head so that we can reuse the same logic in the nex iteration.
------------------------------------------------------------------------
'''
class Solution(object):
    def swapPairs(self, head):
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head
        
        prevNode = dummy
        
        while head and head.next:
            
            # Nodes to be swapped
            firstNode = head
            secondNode = head.next
            
            # Swap nodes
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            # Reinitialize the head and prevNode for next swap
            prevNode = firstNode
            head = firstNode.next
            
        return dummy.next