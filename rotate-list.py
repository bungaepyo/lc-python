'''
------------------
Difficulty: Medium
------------------

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

'''
------------------------------------------------------------------------
Solution 1: Cycle
Time: O(n)
Space: O(1)

Runtime: 46 ms
Memory: 13.5 MB

This is a solution that takes advantage of the linked list's cyclable nature.
Once you find out that you can make the original linked list into a cycle,
the intuition behind this problem becomes pretty straightforward.

In our first pass, we find the tail and connect its next pointer to the head.
This will allow us to easily rotate the linked list by moving the head & tail pointers.

Now, how many steps we need to advance the head & tail pointers is the key here.
If this were a doubly linked list, we would just update head & tail backwards k times.
However, since this is rotating a singly linked list, need to know how many times
we need to advance the pointers so that the new head is points to the first
node after k times rotation.

There are two cases:
  - k < length => you simply move length - k times
  - k >= length => you move length - (k & length) times
But, we can simply apply moveRight = length - (k % length) for both cases.
------------------------------------------------------------------------
'''
class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head
        
        # make the linked list a cycle
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        # line 64,65 are slight improvements - you can include them or not
        if k % length == 0:
          return head
        tail.next = head

        # rotate the linked list k times
        moveRight = length - (k % length)
        while moveRight > 0:
            head = head.next
            tail = tail.next
            moveRight -= 1
        
        # make tail.next = None
        tail.next = None
        
        # return new head
        return head
