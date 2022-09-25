'''
------------------
Difficulty: Medium
------------------

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4] 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''

'''
------------------------------------------------------------------------
Solution 1: Odd and Even Lists
Time: O(n)
Space: O(1)

Runtime: 52 ms
Memory: 16.9 MB

The intuition of this solution might be straightforward, but the actual
implentation might be tricky because of the edge cases. The idea is to
separately store even and odd nodes by using different pointers and link
tail of odd list to head of even list.

In order to do that, we need to store even head before iteration, and
make sure we do odd.next = evenHead at the end before returning head.

After taking care of edge cases where head is None or linked list is of length 1,
we iterate while even and even.next exists. This is because we are going to
assign even.next to odd.next and odd.next to even.next. We need to check
both even and even.next are not None in order to break out of the loop
as soon as we reach the last node.
------------------------------------------------------------------------
'''
class Solution(object):
    def oddEvenList(self, head):
        if (not head) or (not head.next):
            return head
        
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        
        return head