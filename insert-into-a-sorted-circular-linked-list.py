'''
------------------
Difficulty: Medium
------------------

Given a Circular Linked List node, which is sorted in non-descending order,
write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node.
Otherwise, you should return the originally given node.

Example 1:
 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. 
You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. 
After the insertion, the list should look like this, and we should still return node 3.

Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-106 <= Node.val, insertVal <= 106
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pointers
Time: O(n)
Space: O(1)

Runtime: 39 ms
Memory: 14 MB

Two pointers technique is probably the most intuitive way to solve this problem.
Since we are basically inserting a new node in between existing nodes depending on their values,
we need two pointers to compare prev and curr nodes' values.

There are three scenarios we need to consider:
  - (1) insertVal fits within bounds - head <= insertVal <= tail
  - (2) insertVal is out of bounds - head >= insertVal or inserVal >= tail
  - (3) all existing nodes have the same value

There is one edge case we need to consider:
  - empty linked list

Once we catch these scenarios and the edge case, iterating through the linked list
should not be too complicated. Whenever we find a position where it meets
the scenario conditions, we insert the node between prev and curr.

If we can't find anything while iterating, that is scenario 3. In this case,
we can just insert the new node wherever.
------------------------------------------------------------------------
'''
class Solution(object):
    def insert(self, head, insertVal):
        newNode = Node(insertVal)

        # when list is empty
        if head is None:
            newNode.next = newNode
            return newNode
        
        #get the length
        count = 1
        slow = fast = head
        slow = slow.next
        while slow != fast:
            slow = slow.next
            count += 1

        prev = head
        curr = head.next

        while count != 0:
            #scenario 1 -> within bounds
            if prev.val <= insertVal <= curr.val:
                prev.next = newNode
                newNode.next = curr
                return head
            #scenario 2 -> out of bounds
            elif curr.val < prev.val and (insertVal >= prev.val or insertVal <= curr.val):
                prev.next = newNode
                newNode.next = curr
                return head
            prev = prev.next
            curr = curr.next
            count -= 1
        
        #scenario 3 -> all nodes have uniform value
        if newNode.next is None:
            prev.next = newNode
            newNode.next = curr
        
        return head

'''
------------------------------------------------------------------------
Solution 2: Two Pointers - Optimized
Time: O(n)
Space: O(1)

Runtime: 43 ms
Memory: 13.8 MB

This solution uses the same intuition and technique as in the first solution,
but is more optimized as it does not use another pass to calculate the length of the linked list.
The while loop condition is simply True, and only stops when prev == head,
which means we have looped through every node in the list => thus, scenario 3.
------------------------------------------------------------------------
'''
class Solution(object):
    def insert(self, head, insertVal):
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next

        while True:
            if prev.val <= insertVal <= curr.val:
                prev.next = Node(insertVal, curr)
                return head
            elif prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break

        prev.next = Node(insertVal, curr)
        return head