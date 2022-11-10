'''
------------------
Difficulty: Medium
------------------

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
return true if you can visit all the rooms, or false otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room. 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
'''

'''
------------------------------------------------------------------------
Solution 1 - BFS
Time: O(n+k) -> n is number of rooms, k is number of keys
Space: O(n)

Runtime: 56 ms
Memory: 14 MB

This is a straightforward, standard BFS solution. We kick off the BFS by
initializing a double ended queue and putting the first room's keys in it.
For each key, we will mark the room it can open as visited, and get the keys in that room.
For any of the obtained keys that can open an unvisited room, we will put in the queue.

Once we're done with the BFS, meaning queue is empty, we should have a visited
array full of "True" if we've opened every room. If not, there will be at least
one "False" room because it hasn't been updated.
------------------------------------------------------------------------
'''
class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        queue = deque(rooms[0])
            
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            keys = rooms[curr]
            
            for key in keys:
                if not visited[key]:
                    queue.append(key)
        
        return all(visited)

'''
------------------------------------------------------------------------
Solution 2 - DFS
Time: O(n+k)
Space: O(n)

Runtime: 87 ms
Memory: 14.1 MB

This is a DFS solution, which makes small modifications to the BFS solution.
Instead of using a queue and popping from left so that we reach closer rooms first (FIFO),
we use a stack here and pop from right so (LIFO) that we dig deeper into the
chain of rooms that can be opened.
There is no big difference other than the two uses different data structures.
------------------------------------------------------------------------
'''
class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False]*n
        visited[0] = True
        stack = [0]
            
        while stack:
            curr = stack.pop()
            for nei in rooms[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
            
        return all(visited)