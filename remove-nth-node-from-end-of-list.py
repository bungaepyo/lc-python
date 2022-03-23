'''
------------------
Difficulty: Medium
------------------

Given the head of a linked list, remove the nth node from the end of the list and return its head. 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

'''
------------------------------------------------------------------------
Solution 1: two pointer method
Time: O(n)
Space: O(1)

Runtime: 43 ms
Memory: 13.6 MB

This is a standard solution using the two pointer method: fast & slow.
Since the node we want to delete is Nth from the end, and the two pointers are initialized on head,
advancing fast Nth times prior to advancing slow will leave (size-n-1) space.
After this, all we have to do is advance slow while fast is not pointing null,
and skip the node after slow when the loop ends.
Lastly, since fast & slow are initialized on the first node, we need to account for an edge case
where we actually want to delete the first node of the linked list.
After fast first advances, if fast is pointing to null, it means that n = size.
This means that we want to delete the first node, which is (size)th from the end.
We should simply return head.next in this case.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head