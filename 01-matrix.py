'''
------------------
Difficulty: Medium
------------------

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

'''
------------------------------------------------------------------------
Solution 1 - BFS
Time: O(mn) -> m is number of rows, n is number of columns
Space: O(mn) -> space for the queue

Runtime: 503 ms
Memory: 16 MB

The first intuition that comes into mind after reading this problem is that
we should use a BFS to update the cell values. The first thing I thought of
was to execute a BFS every time we encounter a non-zero element, while iterating the matrix.
However there was a problem with this approach:
  - we will only be able to update the distance of one 1 using one BFS (bad time complexity)

Therefore, we should start the BFS from zeros and thereby update the distances of all 1s in the path.
One thing to note here:
  - if we execute BFS every time we encounter a 0, updated cell values can be overriden in the future.

Thus, we need to first add all zeros to the queue and mark ones as unvisited
in one pass through the matrix.
This way we can make sure that the updated cell value has the distance to nearest
zero, since we're starting from zeros and proceeding to their neighbors.
If the cell has already been visited, it means that it was closer to one of
current cell's ancestors.
------------------------------------------------------------------------
'''
class Solution(object):
    def updateMatrix(self, mat):
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(mat)
        COLS = len(mat[0])
        queue = deque()
        
        for R in range(ROWS):
            for C in range(COLS):
                if mat[R][C] == 0:
                    queue.append((R,C))
                else:
                    mat[R][C] = -1
            
        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat

'''
------------------------------------------------------------------------
Solution 2 - DP
Time: O(mn) -> two pass for every matrix cell
Space: O(1) -> no extra space needed

Runtime: 414 ms
Memory: 15.9 MB

This is a pretty smart dynamic programming solution using the following intuition:
  - the distance of a cell from 0 can be calculated if we know the nearest
    distance for all neighbors, in which case the distance is the minimum
    distance of among neighbors + 1 (= use DP)

Note: DP can only proceed with pre-computed values.

Each cell has 4 neighbors in each direction, but it's impossible to compute
current cell's distance based on all 4 neighbors since we don't know if each cell's
distance has been computed or not.

Therefore, we shall do a 2 pass traversing from (1) top & left (2) bottom & right
Since zero cells have zero distance, we're only interested in non-zero cells.

In first pass, current cell's distance should be min(top, left) + 1
  - first pass is basically making sure that everything is computed
In second pass, current cell's distance should be min(curr, bottom+1, right+1)
  - second pass is covering any edge cases where cells have wrong value because
    it wasn't pre-computed for comparison
------------------------------------------------------------------------
'''
class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else float('inf')
                    left = mat[r][c - 1] if c > 0 else float('inf')
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else float('inf')
                    right = mat[r][c + 1] if c < n - 1 else float('inf')
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat