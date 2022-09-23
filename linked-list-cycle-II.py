'''
------------------
Difficulty: Medium
------------------

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

'''
------------------------------------------------------------------------
Solution 1: Hash Table
Time: O(n)
Space: O(n)

Runtime: 64 ms
Memory: 20 MB

This is a pretty intuitive solution using a hash table (namely, a set).
While the pointer is not None (if None, we reached the end so return None),
we check if we have seen it before, and add the node to a set and update it
to the next node. This way, we can check if we encounter a memory address
we've already visited.
------------------------------------------------------------------------
'''
class Solution(object):
    def detectCycle(self, head):
        visited = set()
        
        slow = head
        
        while slow != None:
            if slow in visited:
                return slow
            visited.add(slow)
            slow = slow.next

        return None

'''
------------------------------------------------------------------------
Solution 2: Two Pointers - Floyd's Tortoise and Hare
Time: O(n)
Space: O(1)

Runtime: 50 ms
Memory: 19.5 MB

This is a two-level tortoise and hare solution, based in a mathematical proof.
  - step 1: find the intersection, if there is none return none
  - step 2: move two pointers of equal speed from head & intersection -> node they meet is pos

Assumption:
  - from head to pos: F
  - from pos to intersection: a
  - from intersection to pos: b
  - entire cycle: C

Proof:
  - 2Tortoise = Hare
  - 2(F + a) = F + nC + a
  - 2F + 2a = F + nC + a
  - F + a = nC
  - F + a = n(a + b) <- because C = a + b
  - F + a = n*a + n*b 
  - F = n*a + n*b - a
  - F = (n-1)*a + n*b
  - F = (n-1)*a + (n-1)*b + b 
  - F = (n-1)*C + b
  - Hence, F = however many cycles + b
------------------------------------------------------------------------
'''
class Solution(object):
    def getIntersect(self, head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        
        return None

    def detectCycle(self, head):
        if head is None:
            return None

        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1