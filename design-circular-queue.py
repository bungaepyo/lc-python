'''
------------------
Difficulty: Medium
------------------

Design your implementation of the circular queue. The circular queue is a linear data structure
in which the operations are performed based on FIFO (First In First Out) principle,
and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
'''

'''
------------------------------------------------------------------------
Solution 1: Fixed Size Array, Two Pointers
Time: O(n)
Space: O(n)

Runtime: 61 ms
Memory: 14 MB

This is a solution using fixed size array + two pointer technique to implement
a circular array. This works, but unfortunately has time complexity of O(n)
because of the for loop in deQueue() function.
------------------------------------------------------------------------
'''
class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [None]*k
        self.start = 1001
        self.end = 1001

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.start = 0
            self.end = 0
            self.queue[self.end] = value
            return True
        self.end += 1
        if self.end == len(self.queue):
            self.end = 0
        self.queue[self.end] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.queue[self.start] = None
        self.start += 1
        if self.start == len(self.queue):
            self.start = 0
        for val in self.queue:
            if val != None:
                return True
        self.start = 1001
        self.end = 1001
        return True

    def Front(self):
        return self.queue[self.start] if not self.isEmpty() else -1

    def Rear(self):
        return self.queue[self.end] if not self.isEmpty() else -1

    def isEmpty(self):
        return self.start == 1001 and self.end == 1001

    def isFull(self):
        return (self.start == 0 and self.end == len(self.queue)-1) or (self.end == self.start-1)

'''
------------------------------------------------------------------------
Solution 2: Fixed Size Array, Two Pointers -> O(1) time complexity
Time: O(1)
Space: O(n)

Runtime: 62 ms
Memory: 14.1 MB

This solution also uses fixed size array and two pointers technique, but
is able to reach O(1) time complexity due to it's usage of count and capacity.
You would only have to compare count and capacity to see if it's full or empty.

Furthermore, this solution calculates tailIndex & which index to enQueue
ever time using this formula:
  - tailIndex = (headIndex + count -1) % capacity

Commented out lines are improvements we can make for multi-threaded scenarios
where potentially we can exceed pre-assigned array limit.
------------------------------------------------------------------------
'''
#from threading import Lock

class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # additional attribute to protect the access of our queue
        # self.queueLock = Lock()

    def enQueue(self, value):
        # automatically acquire the lock when entering the block
        # with self.queueLock:
        if self.count == self.capacity:
            return False
        idxAfterTail = (self.headIndex + self.count) % self.capacity
        self.queue[idxAfterTail] = value
        self.count += 1
        # automatically release the lock when leaving the block
        return True
        
    def deQueue(self):
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        if self.count == 0:
            return -1
        tailIndex = (self.headIndex + self.count-1) % self.capacity
        return self.queue[tailIndex]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

'''
------------------------------------------------------------------------
Solution 3: Singly Linked List
Time: O(1)
Space: O(n)

Runtime: 113 ms
Memory: 13.9 MB

This is a solution using a singly linked list. Implementing a circular queue
using a linked list is more space efficient in average even though worst case is
O(n) because we do not have to pre-allocate k amount of space.
Also, you would not have to worry about calculating head & tail indices
like we did in solution 1 & 2 because head and tail nodes of the linked list
naturally takes care of this.
------------------------------------------------------------------------
'''
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue(object):

    def __init__(self, k):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self):
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

