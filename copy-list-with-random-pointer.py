'''
------------------
Difficulty: Medium
------------------

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pass & Hashmap
Time: O(n)
Space: O(n)

Runtime: 42 ms
Memory: 14.5 MB

This is an iterative two pass solution using a hashmap to copy over the original linked list.
The base idea is the following:
  - In first pass, we (1) create new node (2) update next pointer (3) put old -> new in hashmap
    - We know how to handle next pointers, but don't know which new nodes correspond to the old nodes for the random pointer,
      we need a hashmap to store the mappings.
    - After the first pass, we need to manually update prev.next = None since our while loop condition
      does not account for the last node's next pointer.

  - In second pass, we update the random pointers by referencing to the hashmap (old -> new)
------------------------------------------------------------------------
'''
class Solution(object):
    def copyRandomList(self, head):
        # hashmap whose key: idx, value: new node
        hashmap = {}

        # first pass -> copy all the nodes & store them in a map
        prev = ListNode(0)
        dummy = prev
        
        while head is not None:
            newNode = Node(head.val, head.next, head.random)
            prev.next = newNode
            prev = newNode
            hashmap[head] = newNode
            head = head.next
        
        # to account for last node's next pointer
        prev.next = None
        
        # second pass -> iterate and connect random pointers using the map
        dummyHead = dummy.next
        while dummyHead is not None:
            dummyHead.random = hashmap.get(dummyHead.random)
            dummyHead = dummyHead.next

        return dummy.next

'''
------------------------------------------------------------------------
Solution 2: Recursion & Hashmap
Time: O(n)
Space: O(n)

Runtime: 33 ms
Memory: 15.4 MB

This is a recursive solution that copies over the old linked list by treating it like a graph
and traversing the old list once and making two recursive calls (next, random) on each node.

Base case is: (1) when the node is None (2) when the node has been visited

We use a hashmap to mark the nodes that have been visited, and only store the
mapping of old -> when we visit it for the first time.
The node.next recursive call will cover all the next pointer iterations
and the node.random will cover all the random pointer iterations, in a depth first manner.
------------------------------------------------------------------------
'''
class Solution(object):

    visited = {}

    def copyRandomList(self, head):
        
        if head is None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

'''
------------------------------------------------------------------------
Solution 3: Iteration & Hashmap
Time: O(n)
Space: O(n)

Runtime: 84 ms
Memory: 15.4 MB

This is an iterative solution that uses a similar intuition as the previous two
solutions because it uses hashmap. After covering the head == None edge case,
we go ahead and create a copy of the first node since we need somewhere to begin
with.

And while traversing the old linked list, we assign next & random pointers based on
whether they have been visited or not. Since this is an iterative approach,
we are able to account for all the nodes' next and random pointers by
advancing new_node after each assignment. At the end, we simply return the
new head.
------------------------------------------------------------------------
'''
class Solution(object):
    
    visited = {}
    
    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        
        return None

    def copyRandomList(self, head):
        
        if head is None:
            return None
        
        old_node = head
        new_node = Node(head.val, None, None)
        self.visited[old_node] = new_node
        
        while old_node is not None:
            new_node.next = self.getClonedNode(old_node.next)
            new_node.random = self.getClonedNode(old_node.random)
            
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]

'''
------------------------------------------------------------------------
Solution 4: Iteration & O(1)
Time: O(n)
Space: O(1)

Runtime: 78 ms
Memory: 14.2 MB

This is a two pass iteration solution that achieves O(1) space complexity by
using the characteristics of a linked list.

In our first pass, we simply create new nodes and make them the next node of the old nodes.
This will create an interweaved linked list where A -> A' -> B -> B' -> None.

In our second pass, we update the random pointers of the new nodes by referencing
the old nodes' random pointers. Because of the interweaving structure,
ptr.next.random (new_node's random pointer) will always be ptr.random.next (old_node's random pointer's next node).

Once we're done with the two passes, it's time to unwind the interweaved structure.
While iterating the old list, we hop next.next and unweave into two structures.
At the end we will have (1) A -> B -> C -> None (2) A' -> B' -> C' -> None
------------------------------------------------------------------------
'''
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        
        ptr = head
        
        while ptr:
            new_node = Node(ptr.val, None, None)
            
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head
        
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        
        return head_new