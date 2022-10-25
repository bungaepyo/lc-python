'''
------------------
Difficulty: Medium
------------------

You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible. 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck. 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
'''

'''
------------------------------------------------------------------------
Solution 1: BFS
Time: O(n^2 * a^n + D) -> a is number of digits, n is number of digits in lock, d is deadends
Space: O(a^n + D)

Runtime: 1456 ms
Memory: 14.5 MB

This is a pretty complicated solution using the BFS method, with a lot of optimizations necessary.
The base idea is the following:
  - node represents the string representation of a lock combination
  - for the leftmost (node, depth) pair in the queue,
    - we return depth if it matches with target
    - we skip if it's a deadend (so if everything skips on first try, we can return -1)
  - add unseen neighbors (8 different variations we can go forward with) to the queue
  - how we determine neighbors is basically doing +1 and -1 for each index of the node

Optimizations:
  - not really an optimization, but (x+dx) % 10 handles both 0 -> 9 and 9 -> 0
    (reference: https://stackoverflow.com/questions/3883004/the-modulo-operation-on-negative-numbers-in-python)
  - you need to make deadends a set to remove duplicates
  - you need to use a deque for the queue because pop(0) will take O(n) while popleft() will take O(1)
  - you need to make "seen" a set because add() takes O(1)
------------------------------------------------------------------------
'''
class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            res = []
            for i in range(4):
                x = int(node[i])
                for dx in (-1, 1):
                    nx = (x+dx) % 10
                    res.append(node[:i]+str(nx)+node[i+1:])
            return res
        
        dead = set(deadends)
        queue = collections.deque([('0000',0)])
        seen = {'0000'}
        while len(queue) > 0:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1