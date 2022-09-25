'''
------------------
Difficulty: Easy
------------------

Given the head of a linked list and an integer val, remove all the nodes
of the linked list that has Node.val == val, and return the new head. 

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []

Example 3:

Input: head = [7,7,7,7], val = 7
Output: [] 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

'''
------------------------------------------------------------------------
Solution 1: Sentinel (dummy) Node
Time: O(n)
Space: O(1)

Runtime: 103 ms
Memory: 20.2 MB

This is a solution using the sentinel node technique (initialize dummy whose
next pointer is head, and return dummy.next at the end).
Since we just have to skip whatever node whose value is equal to val, we iterate
the linked list while curr exists, and do the following:
  - (1) prev.next = curr.next (2) curr = curr.next if values match
    skip the curr node, and only move curr because we aren't ready to update prev
  - (1) prev = curr (2) curr = curr.next if values don't match
    update prev because now we're safe to drag prev to where curr is now
    and advance curr as well.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next