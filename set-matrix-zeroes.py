'''
------------------
Difficulty: Medium
------------------

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place. 

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]] 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

'''
------------------------------------------------------------------------
Solution 1: O(1) Space, Nested Loop
Time: O(mn)
Space: O(1)

Runtime: 717 ms
Memory: 14.5 MB

This is the first O(1) solution that I came up with, but not fully efficient.
Since we need to achieve a O(1) time complexity, there is no way we can
mark the cells that have the value 0, and set col & row to zeroes later.
Therefore, we need to use a helper function that can do the job for us.
As soon as we encounter a cell with value 0, we set it to a non-integer (None)
and run the helper function that iterates through the matrix again and sets
the row & col to a non-integer as well.
The reason we make them non-integer is because:
  - we cannot set it to zero because there could be other zeroes
  - we cannot set it to another integer because there could be other instances
    of that another integer.
In the end, we loop through the matrix again and set the non-integers to zeroes.
------------------------------------------------------------------------
'''
class Solution(object):
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    self.helper('row', i, matrix)
                    self.helper('col', j, matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return matrix

    def helper(self, direction, idx, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rowOrCol = i if direction is 'row' else j
                if rowOrCol == idx and matrix[i][j] != 0:
                    matrix[i][j] = None

'''
------------------------------------------------------------------------
Solution 2: Additional Memory (NOT A REAL SOLUTION)
Time: O(mn)
Space: O(m+n)

Runtime: 173 ms
Memory: 14.3 MB

This solution is pretty straighforward, but cannot be accepted because
it uses extra memory to achieve the goal.
Using rows and cols sets, we first identify and mark which rows and columns
should be having all zeroes.
Afterwards, we iterate through the matrix once again and set all cells that
have row in rows & col in cols to zeroes.
------------------------------------------------------------------------
'''
class Solution(object):
    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

'''
------------------------------------------------------------------------
Solution 3: O(1) Space, Efficient Solution
Time: O(mn)
Space: O(1)

Runtime: 99 ms
Memory: 14.5 MB

IMPORTANT!

If you don't handle the first row separately, then if there is a zero in the row,
we would mark matrix[0][0] as zero (based on our core logic),
which means the first column would be set all to 0s later on when in fact it may not be required.
Vice versa, if we don't treat the first column separately, 
if there is a zero in the column, we would also mark matrix[0][0] as zero,
which means the first row would be set all to 0s later on when in fact it may not be required.

This is a more efficient O(1) solution that uses matrix[0][0] as a marker for zeroing out
the first row, and is_col as a marker for zeroing out the first col.
First, we iterate through the matrix (0,R)(1,C) and zero out first element of row and col
whenever we find a cell with value 0.
Later, while iterating (1,R)(1,C) we zero out all cells that have either
first element of row or col as zero.
At last, we check matrix[0][0] to see if we need first row zeroed out,
and check is_col to see if we need first col zeroed out.

We are treating matrix[0][0] and first column as special cases here because
the first element of cow and col overlap, possibly causing the col to be
zeroed out because a cell with 0 on the first row can zero out matrix[0][0].
------------------------------------------------------------------------
'''
class Solution(object):
    def setZeroes(self, matrix):
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
