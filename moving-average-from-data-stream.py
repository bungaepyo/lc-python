'''
------------------
Difficulty: Easy
------------------

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 
Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
'''

'''
------------------------------------------------------------------------
Solution 1 - Array / List
Time: O(n)
Space: O(n)

Runtime: 125 ms
Memory: 16.7 MB

This is a pretty straightforward array implementation solution. We simply
initialize an array that functions as a FIFO queue. While the length of
queue is lower than self.size, we append and return average. Otherwise,
we pop the first element, append, and return average.
------------------------------------------------------------------------
'''
class MovingAverage(object):

    def __init__(self, size):
        self.queue = []
        self.size = size

    def next(self, val):
        if len(self.queue) < self.size:
            self.queue.append(val)
        else:
            self.queue.pop(0)
            self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)

'''
------------------------------------------------------------------------
Solution 2 - Double-ended Queue (Deque)
Time: O(1)
Space: O(n)

Runtime: 80 ms
Memory: 16.6 MB

This is a deque (double-ended queue) implementaion solution that brilliantly
uses a couple other values to reduce time complexity to O(1).
  - we keep track of self.window_sum by adding the newest element and removing the oldest element
    - deque provides add/remove from both ends with O(1) time complexity.
------------------------------------------------------------------------
'''
from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        self.queue = deque()
        self.size = size
        self.window_sum = 0

    def next(self, val):
        self.queue.append(val)
        tail = self.queue.popleft() if len(self.queue) > self.size else 0
        self.window_sum = self.window_sum - tail + val
        
        return float(self.window_sum) / min(len(self.queue), self.size)

'''
------------------------------------------------------------------------
Solution 3 - Circular Queue with Array
Time: O(1)
Space: O(n)

Runtime: 71 ms
Memory: 16.7 MB

Circular queue: basically a queue with a circular shape => tail = (head + 1) % size
  - The major advantage of circular queue is that by adding a new element to a full circular queue,
    it automatically discards the oldest element. Unlike deque, we do not need to explicitly remove the oldest element.
  - Another advantage of circular queue is that a single index suffices to keep track of both ends of the queue,
    unlike deque where we have to keep a pointer for each end.

So basically, this data structure proceeds by head eating up the position of
previous tail and updating it.
------------------------------------------------------------------------
'''
class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = [0]*size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val):
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return float(self.window_sum) / min(self.count, self.size)