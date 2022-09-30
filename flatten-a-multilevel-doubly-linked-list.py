'''
------------------
Difficulty: Medium
------------------

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer.
This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that
all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list.
The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null. 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Example 3:

Input: head = []
Output: []
Explanation: There could be empty list in the input.

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 105
 

How the multilevel linked list is represented in test cases:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. 

The serialization becomes:

[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
'''

'''
------------------------------------------------------------------------
Solution 1: DFS by recursion
Time: O(n) -> DFS visits each node once
Space: O(n) -> recursion stack, worst case when all nodes are only connected with child pointers.

Runtime: 35 ms
Memory: 14.5 MB

This is a DFS solution which should be the most intuitive way to approach this problem.
In our recursive function, the base case is when we reach the leaf node,
which is a node that does not have a child nor a next node.

What we need to do if we find a node with a child is the following:
  - Get the flattened linked list starting with the child node
  - Connect the list's head with the current node
  - Find the list's tail
  - Connect the list's tail with the current node's next node, if there is one (varialbe succ)

If the current node has a next node:
  - (1) connect child list's tail with next node
  - (2) proceed with the flattening by self.flatten(succ)

One important thing to note here is that all the nodes in the resulting linked list
should have child set to null.
------------------------------------------------------------------------
'''
class Solution(object):
    def flatten(self, head):
        if head is None:
            return None

        curr = head
        succ = curr.next
        prev = None

        #base case - leaf node
        if succ is None and curr.child is None:
            return head
        
        #if have child, get child list via recursion
        if curr.child is not None:
            #connect child head
            child = self.flatten(curr.child)
            curr.next = child
            child.prev = curr
            
            #find child tail
            while child.next is not None:
                child = child.next
            prev = child
            
        #if have next, (1) connect child tail (2) flatten next elements
        if succ is not None:
            if prev is not None:
                prev.next = succ
                succ.prev = prev
            self.flatten(succ)

        #return
        head.child = None
        return head

'''
------------------------------------------------------------------------
Solution 2: DFS by recursion
Time: O(n) -> DFS visits each node once
Space: O(n) -> recursion stack, worst case when all nodes are only connected with child pointers.

Runtime: 46 ms
Memory: 14.4 MB

This is also a different recursive DFS approach to solve the question.
------------------------------------------------------------------------
'''
class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)

'''
------------------------------------------------------------------------
Solution 3: DFS by iteration
Time: O(n)
Space: O(n)

Runtime: 47 ms
Memory: 14 MB

This is a pretty intuitive iterative DFS solution using a stack. By using
a pseudoHead, we are able to cover edge cases in the beginning. Also, by
adding next Nodes first, child Nodes next, and poppoing the current node
from the stack, we are able to flatten the linked list by always processing
child nodes first if there are any.
------------------------------------------------------------------------
'''
class Solution(object):
    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next