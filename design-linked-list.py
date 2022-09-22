'''
------------------
Difficulty: Medium
------------------

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
If index equals the length of the linked list, the node will be appended to the end of the linked list.
If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 
Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 
Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
'''

'''
------------------------------------------------------------------------
Solution 1: Singly Linked List Implementation
Time:
  - O(1) for addAtHead
  - O(k) for get, addAtIndex, deleteAtIndex -> k is the index
  - O(n) for addAtTail
Space: O(1)

Runtime: 295 ms
Memory: 14 MB

One tricky thing to keep in mind: we have a sentinel node as pseudo-head.
That is why we are iterating index+1 times in get, and index times in addAtIndex.
------------------------------------------------------------------------
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
            
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        
        self.size += 1
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        newNode = ListNode(val)
        newNode.next = pred.next
        pred.next = newNode
        

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        
        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next

'''
------------------------------------------------------------------------
Solution 2: Doubly Linked List Implementation
Time:
  - O(1) for addAtHead, addAtTail
  - O(min(k, N-k)) for get, addAtIndex, deleteAtIndex -> k is the index
Space: O(1)

Runtime: 257 ms
Memory: 15.6 MB

Note that there are sentinel nodes both at the beginning and at the end.
For doubly linked lists, you need to update both prev and next, so the amount
of work you need to do is doubled. Also, for get, addAtIndex, deleteAtIndex,
you should check whether starting from the beginning or the end is faster.
------------------------------------------------------------------------
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        
        return curr.val
        

    def addAtHead(self, val):
        pred, succ = self.head, self.head.next
        
        self.size += 1
        
        newNode = ListNode(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode

    def addAtTail(self, val):
        pred, succ = self.tail.prev, self.tail
        
        self.size += 1
        
        newNode = ListNode(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode
        

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
            
        self.size += 1
        
        newNode = ListNode(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        self.size -= 1
        pred.next = succ
        succ.prev = pred