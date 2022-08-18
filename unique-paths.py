'''
------------------
Difficulty: Medium
------------------

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of
possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
Constraints:

1 <= m, n <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: DFS, DP but not optimized
Time: O(mn)
Space: O(1)

Runtime: Exceeds time limit ms
Memory: ? MB

This is the initial dfs solution that I came up with. Essentially, using a
helper function that performs dfs, we calculate how many paths are available.
Since we only count it as a unique path if reached the last element [m-1][n-1],
we return 0 if out of bounds and return 1 if exactly at last element.
Otherwise, we continue the dfs recursion and add up the count of paths by
increasing i or increasing j by 1 (cannot decrease any since we only proceed
towards the last element).
------------------------------------------------------------------------
'''
class Solution(object):
    def uniquePaths(self, m, n):
        return self.helper(0, 0, m, n)
    
    def helper(self, i, j, m, n):
        #if out of bounds, don't count
        if i > m-1 or j > n-1:
            return 0

        #if reached last element, add to res
        if i == m-1 and j == n-1:
            return 1
            
        return self.helper(i+1, j, m, n) + self.helper(i, j+1, m, n)

'''
------------------------------------------------------------------------
Solution 1: DP, optimized
Time: O(mn)
Space: O(mn)

Runtime: 36 ms
Memory: 12.9 MB

This is an optimized DP solution that improves the time complexity drastically
by trading off the space complexity. The key here is to realize that you don't
actually have to recursively check how many unique paths each element has.
Since each cell provides +1 variation by going right or down, we we can calculate
the number of unique paths to the final element by adding up the number of
variations from the first element.
First, fill up a m by n matrix with 1s.
Second, Starting with matrix[1,1], we add up the numbers by doing:
  - matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
Then, the number should be populated for the last element, and we return it.
------------------------------------------------------------------------
'''
class Solution(object):
    def uniquePaths(self, m, n):
        matrix = m*[n*[1]]
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[m-1][n-1]