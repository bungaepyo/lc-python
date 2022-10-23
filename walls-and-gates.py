'''
------------------
Difficulty: Medium
------------------

You are given an m x n grid rooms initialized with these three possible values.
  - -1 A wall or an obstacle.
  - 0 A gate.
  - INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF
    as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 
Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
'''

'''
------------------------------------------------------------------------
Solution 1: Queue, BFS
Time: O(mn) -> m by n matrix, worst case every cell gets visited once
Space: O(mn)

Runtime: 593 ms
Memory: 17 MB

This is a BFS solution using a queue. It might look complicated when you first
look at it, but the intuition behind it is not too hard to understand.

In order to fill in all the empty rooms with its distance to the closest
gate, we need to start from the gates and perform a breadth-first-search.
Using a queue, we will advance level by level, first covering all the cells
that are 1 distance away from each gate. Because of this, if you discover an
empty room, it will have to be from the closest gate.

First, we add all the gate (val == 0) nodes to the queue so that we can
start with them. While the queue is not empty, we are going to repetitively do the following:
  - pop elements from the beginning (FIFO)
  - checkout neighboring cells in all 4 directions and see if any of them are empty rooms
  - if there is an empty room,
    - (1) we update its value with distance + 1
    - (2) we add it to the queue so that we can later start stretching out from it

Queue will be empty if we have checked & updated all eligible (reachable) cells.
------------------------------------------------------------------------
'''
class Solution(object):
    def wallsAndGates(self, rooms):
        ROW = len(rooms)
        COL = len(rooms[0])
        inf = 2147483647
        queue = []
        
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        while len(queue) > 0:
            x, y = queue.pop(0)
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<ROW and 0<=ny<COL and rooms[nx][ny] == inf:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))