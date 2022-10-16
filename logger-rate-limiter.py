'''
------------------
Difficulty: Easy
------------------

Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds
(i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
 
Example 1:

Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21

Constraints:

0 <= timestamp <= 109
Every timestamp will be passed in non-decreasing order (chronological order).
1 <= message.length <= 30
At most 104 calls will be made to shouldPrintMessage.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(1)
Space: O(n)

Runtime: 120 ms
Memory: 20.1 MB

This is an intuitive solution using the hasmap (dict) data structure.
We initialize the hashmap upon class initialization to keep track of the
incoming messages' latest valid timestamp.
There could be three scenarios:
  - if message not in hashmap -> True -> add to hashmap
  - if message in hashmap
    - if timestamp is valid -> True -> update hashmap
    - if timestamp is not valid -> False (don't update because not sent)
------------------------------------------------------------------------
'''
class Logger(object):

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp, message):
        res = True
        
        if message in self.hashmap and self.hashmap.get(message) + 10 > timestamp:
            res = False
        else:
            self.hashmap[message] = timestamp
        
        return res

'''
------------------------------------------------------------------------
Solution 2 - Queue + Set
Time: O(n) -> n is size of queue
Space: O(n) -> n is size of queue

Runtime: 271 ms
Memory: 20 MB

This is an alternative solution using a combination of queue and set.
We are using queue to keep track of the timestamps that are still blocking
the addition of a new input message. We are using the hashset to keep track
of what messages are still blocking the addition of a new message.

Once we receive a new input new ts, msg pair, we remove all the timestamps
that are not blockers anymore from the queue and their corresponding messages
from the set. After this step, we ensure that messages in the set are the ones
limiting the log rate.

If the input message is not in the set, it means we can log the message.
Thus, add to hashset, add to queue, and return True. If already in set,
return False.
------------------------------------------------------------------------
'''
from collections import deque

class Logger(object):

    def __init__(self):
        self.hashset = set()
        self.queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        while self.queue:
            msg, ts = self.queue[0]
            if timestamp - ts >= 10:
                self.queue.popleft()
                self.hashset.remove(msg)
            else:
                break
        
        if message not in self.hashset:
            self.hashset.add(message)
            self.queue.append((message, timestamp))
            return True
        else:
            return False