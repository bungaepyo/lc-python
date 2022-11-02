'''
------------------
Difficulty: Medium
------------------

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

'''
------------------------------------------------------------------------
Solution 1: DFS
Time: O(mn) -> number of rows * cols
Space: O(mn)

Runtime: 251 ms
Memory: 28.8 MB

This is a pretty intuitive depth-first-search solution. The base idea is the following:
  - an island is a series of connected "1" (land) surrounded by "0" (water)
  - if you mark all the connected "1"s as visited every time you encounter the first unvisited one,
    that means you've covered an entire island -> thus, increase count by 1
  - since you're updating the original matrix, you are safe to perform DFS on
    every unvisited "1" because all visited land are already marked as visited.
------------------------------------------------------------------------
'''
class Solution(object):
    def numIslands(self, grid):
        ROW = len(grid)
        COL = len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r<0 or r>=ROW or c<0 or c>=COL or grid[r][c] != "1":
                return
            grid[r][c] = "VISITED"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

'''
------------------------------------------------------------------------
Solution 2: BFS, Queue
Time: O(mn)
Space: O(mn)

Runtime: 256 ms
Memory: 28.6 MB

This is a breadth-first-search solution that uses the same intuition, but
uses a queue for processing the visited nodes.

Originally, I've marked the cells as visited after pop() from the queue.
This apparently causes a lot of duplicate cells to be added to the queue
since adjacent cells share a lot of neighbors. This slows down the execution
due to having to check the same cells multiple times even though it has been visited.

"if you put a node in the queue before marking it as seen,
then when you visit the neighbour of that node you will add it to the queue again;
leading to some duplications in your queue."

Thus, you will have to mark the cell as visited BEFORE adding it to the queue
so that future iterations do not double-process the same cell again by adding it to the queue.
------------------------------------------------------------------------
'''
class Solution(object):
    def numIslands(self, grid):
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        ROW = len(grid)
        COL = len(grid[0])
        count = 0
        
        def bfs(r, c):
            queue = []
            queue.append((r,c))

            while len(queue) > 0:
                x, y = queue.pop(0)
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<ROW and 0<=ny<COL and grid[nx][ny] == "1":
                        grid[nx][ny] = "VISITED"
                        queue.append((nx, ny))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] = "VISITED"
                    bfs(r, c)
        return count