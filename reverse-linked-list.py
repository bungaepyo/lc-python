'''
------------------
Difficulty: Easy
------------------

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

'''
------------------------------------------------------------------------
Solution 1: Iteration
Time: O(n)
Space: O(1)

Runtime: 22 ms
Memory: 15.4 MB

This is an iterative solution that reverses a linked list in one pass.
Base idea is following: while iterating, if we save the immediate previous
node that we've seen, we are able to update the next pointer of every node.
Since we are reversing the pointer from head, and head's next should be None at
the end of the iteration, we initialize prev as None.

While head is pointing to a valid ListNode, we (1) save current head's next value
for future reference (2) update head's next to prev (reverse) (3) make current head
a prev (4) go to the next step by assigning head as the saved temp next value.

This way, we are able to reverse everything in the linked list. However,
one important thing to notice is that we should return prev at the end of iteration.
Since prev = head and head = temp operation is done at the last node of linked list,
prev is the actual last node and head is None.
Thus, return prev instead of head, which is mot a valid ListNode.
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseList(self, head):        
        prev = None
        curr = head
        
        while head:
            next = head.next
            curr.next = prev
            prev = curr
            head = next
        
        return prev

'''
------------------------------------------------------------------------
Solution 2: Recursion
Time: O(n)
Space: O(n)

Runtime: 19 ms
Memory: 18.8 MB

This is a recursive approach that essentially iterates the linked list backwards.
The base case of the recursion is when head or head.next is not a valid ListNode.
This serves two purposes:
  - (1) when we get a linked list that is either empty or has only one Node, return immediately
  - (2) when we reach the last node, return it (since head.next is None)

One we reach the last node within the recursion, that last node will be saved in the variable p.
Variable p won't change anything until we traverse back to the top level of
the recursive calls because we won't do anything to it. We will essentially use it
as the new head of the reversed linked list.

During each recursion call, we reverse the head and head.next pointers by
head.next.next = head AND head.next = None
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseList(self, head):
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p