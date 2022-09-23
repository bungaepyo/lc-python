'''
------------------
Difficulty: Easy
------------------

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list. 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pointers - Floyd's Cycle Finding Algorithm
Time: O(n)
Space: O(1)

Runtime: 39 ms
Memory: 20.3 MB

This is a two pointer approach to finding whether there is a cycle in a
linked list. Base idea is that, if there is a cycle, you should be able
to detect it by using two pointers that move in different speeds (one 1, the other 2).

While fast, fast.next, fast.next.next exists, if fast and slow are pointing
to the same node after an update, it means there is a loop. Thus, return true.
------------------------------------------------------------------------
'''
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

'''
------------------------------------------------------------------------
Solution 2: Hash Table
Time: O(n)
Space: O(n)

Runtime: 35 ms
Memory: 21.2 MB

This is a very intuitive solution using a hash table (namely, a set).
While iterating the linked list, we append the current node's memory address
to a set if we have not seen it before. If we encounter a node that we've
seen before, we return True. Otherwise, False.
------------------------------------------------------------------------
'''
class Solution(object):
    def hasCycle(self, head):
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False