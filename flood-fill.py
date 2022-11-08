'''
------------------
Difficulty: Easy
------------------

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image. 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
'''

'''
------------------------------------------------------------------------
Solution 1 - DFS
Time: O(n) -> number of pixels in image, might process every pixel
Space: O(n) -> size of implicit call stack

Runtime: 114 ms
Memory: 13.6 MB

This is a classic DFS solution that can be implemented in a matrix data structure (nested array).
Starting from a particular cell, there are two scenarios:
  - Cell is invalid: row or col index out of bounds, not the same value as starting cell, or already visited
  - Cell is valid: all other (within bounds, same val, not visited)

Only when the cell passes the if statement, we proceed with updating the value
to new color, mark as visited, and recursively stretch into 4 directions from that cell.
This way, we are able to flood-fill all eligible cells starting from a given cell.

We add a VISITED array in order to prevent stack overflow, and this is called memoization.
------------------------------------------------------------------------
'''
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(image)
        COLS = len(image[0])
        VISITED = []
        
        def dfs(r, c, val):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != val or (r,c) in VISITED:
                return
            image[r][c] = color
            VISITED.append((r,c))
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc, val)
        
        dfs(sr, sc, image[sr][sc])
        return image