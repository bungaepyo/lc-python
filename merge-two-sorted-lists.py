'''
------------------
Difficulty: Easy
------------------

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursion
Time: O(n + m)
Space: O(n + m)

Runtime: 32 ms
Memory: 13.4 MB

The recursive solution is the most popular way to solve this problem.
Since the two lists are already sorted, it is guaranteed that the head of the lists
will have the smallest values. Therefore, it is safe to start with comparing the heads.
For the base case for the recursion, we will return the other list if one is empty.

First, create a dummy head so that we can attach nodes to it and return it later.
Second, compare the smallest values, assign to head, and push the pointer to the next node.
Third, assign head.next with the recursive call and return head.
------------------------------------------------------------------------
'''
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = ListNode()
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        head.next = self.mergeTwoLists(list1, list2)
        
        return head

'''
------------------------------------------------------------------------
Solution 2 - Recursion (more concise version)
Time: O(n + m)
Space: O(n + m)

Runtime: 12 ms
Memory: 13.5 MB

Due to its simplicity, runtime of this recursive approach is much shorter.
------------------------------------------------------------------------
'''
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

'''
------------------------------------------------------------------------
Solution 3 - iteration
Time: O(n + m)
Space: O(1)

Runtime: 22 ms
Memory: 13.3 MB

This solution has the same idea, but takes an interative approach.
You would first create a false ListNode to return later, and assign a pointer to it.
While the two given heads are not null, 
(1) compare the values (2) update the pointer's next node (3) move the head to the next node
when the loop ends, attach whatever is left to the end of prev (pointer)
and return the false ListNode created in the beginning. (prehead)
------------------------------------------------------------------------
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next