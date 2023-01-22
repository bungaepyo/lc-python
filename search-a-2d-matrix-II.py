'''
------------------
Difficulty: Medium
------------------

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
'''

'''
------------------------------------------------------------------------
Solution 1: Divide and Conquer
Time: O(nlogn) -> master theorem
Space: O(logn) -> recursion tree discards half of matrix every iteration

Runtime: 142 ms
Memory: 19.6 MB

This is a divide and conquer solution that decreases the problem space by half
in every recursive iteration. The underlying intuition is that, by choosing
a column in the middle and finding a rowIndex it satisfies the following condition,
  - matrix[row-1][pivotCol] < target < matrix[row][pivotCol]
it is basically possible to discard the top-left and bottom-right submatrix
every recursive iteration.
  - Base case: if row/col is out of bounds or target is not in scope anymore, return False
  - If we find the target on pivotCol, return True
  - Proceed with recursion on the top-right and bottom-left submatrix.
------------------------------------------------------------------------
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        def helper(rowStart, rowEnd, colStart, colEnd):
            # this submatrix has no height or no width
            if rowStart > rowEnd or colStart > colEnd:
                return False
            # target is already larger than the largest or smaller than the smallest of submatrix
            elif target < matrix[rowStart][colStart] or target > matrix[rowEnd][colEnd]:
                return False

            pivotCol = colStart+(colEnd-colStart)//2

            # locate row such that matrix[row-1][pivotCol] < target < matrix[row][pivotCol]
            row = rowStart
            while row <= rowEnd and matrix[row][pivotCol] <= target:
                if matrix[row][pivotCol] == target:
                    return True
                row += 1

            return helper(row, rowEnd, colStart, pivotCol-1) or helper(rowStart, row-1, pivotCol+1, colEnd)
        
        return helper(0, len(matrix)-1, 0, len(matrix[0])-1)

'''
------------------------------------------------------------------------
Solution 2: Search Space Reduction
Time: O(m+n)
Space: O(1)

Runtime: 137 ms
Memory: 19.6 MB

This is such a smart solution. The strategy of this solution is sweet and simple.
Start from bottom-left, if value is greater than target go up one row,
if value is smaller than target, go right one column.

Since the rows are sorted left to right, we know that all the values to
the right will be too large if current value is larger than target.
So, we move up one row in this case. Since the columns are sorted top to
bottom, it's guarenteed that value of matrix[row-1][col] will be smaller.

If the current value is smaller than target, we move one cell to the right (col += 1).
We continue this process until we find the target or current cell is out of range.
------------------------------------------------------------------------
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)-1
        col = 0
        
        while row >= 0 and col <= len(matrix[0])-1:
            val = matrix[row][col]
            if val < target:
                col += 1
            elif val > target:
                row -= 1
            else:
                return True
        return False