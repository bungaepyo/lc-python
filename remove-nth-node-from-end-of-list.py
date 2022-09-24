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

'''
------------------------------------------------------------------------
Solution 2: two pointer method, dummy head
Time: O(n)
Space: O(1)

Runtime: 38 ms
Memory: 13.3 MB

This is a two pointer technique solution that basically has the same idea
as above solution, but instead uses a dummy head. The reason we want a dummy
node is because we do not want to specifically accomodate for the edge
case of removing the first node of the linked list. If we do everything the same
way but return dummy.next, we shall be good because if we wanted to remove
the first node, slow.next = slow.next.next will do it because slow was initially
assigned as dummy.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next

'''
------------------------------------------------------------------------
Solution 2: two pass
Time: O(n)
Space: O(1)

Runtime: 21 ms
Memory: 13.4 MB

This solution takes a different approach using a two pass method, although it
does use the dummy head. First pass is for measuring the length of the linked list.
Then we subtract n from length, and until remaining length runs out, we
would advance first. We will be pointing at the previous node of the node that
we want to delete since we subtracted n from length. Thus skip the next node
and return dummy.next.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length = 0

        first = head
        while first != None:
            length += 1
            first = first.next
        
        length -= n
        
        while length > 0:
            length -= 1
            first = first.next
            
        first.next = first.next.next
        return dummy.next