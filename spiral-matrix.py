'''
------------------
Difficulty: Medium
------------------

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: Set up boundaries - simulation
Time: O(MN) -> M is len(matrix), N is len(matrix[0])
Space: O(1) -> We don't use other data structures. We don't include the output array in the space complexity.

Runtime: 17 ms
Memory: 13.3 MB

This is a solution using a simulation technique, setting up boundaries of each iteration.
Essentially, in each iteration of the while loop using the helper function,
we add the outer most boundary of the matrix and restart with the inner matrix.
In the helper function, we do the following:
  - add the first row, unless there is less than 1 column.
  - add the last column, unless there are less than 2 rows.
  - add the last row, unless there are less than 1 row and less than 1 column.
    - 2x2 matrix is the minimum size we can run this operation.
  - add the first col, unless there are less than 2 rows and less than 1 column.
    - even 2x2 matrix does not have enough columns for this operation.
------------------------------------------------------------------------
'''
class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        if len(matrix) == 0:
            return res

        m = len(matrix)
        n = len(matrix[0])
        startRow = 0
        startCol = 0
        rowSize = m
        colSize = n
        
        def helper(startRow, startCol, rowSize, colSize):
            #add first row
            if colSize > 0:
                for i in range(colSize):
                    res.append(matrix[startRow][startCol+i])
            #add last col
            if rowSize > 1:
                for i in range(rowSize-1):
                    res.append(matrix[startRow+1+i][startCol+colSize-1])
            #add last row
            if rowSize > 1 and colSize > 1:
                for i in range(colSize-1):
                    res.append(matrix[startRow+rowSize-1][startCol+colSize-2-i])
            #add first col
            if rowSize > 2 and colSize > 1:
                for i in range(rowSize-2):  
                    res.append(matrix[startRow+rowSize-2-i][startCol])
            return
        
        while rowSize > 0 and colSize > 0:
            #helper function for adding outer-most boundary
            helper(startRow, startCol, rowSize, colSize)
            startRow += 1
            startCol += 1
            rowSize -= 2
            colSize -= 2
        
        return res

'''
------------------------------------------------------------------------
Solution 2: Set up boundaries - simulation (optimized)
Time: O(MN)
Space: O(1)

Runtime: 7 ms
Memory: 13.4 MB

This is an optimized solution for setting up the boundaries and doing a simulation.
The code below has a much more simpler constraint, therefore it allows
us to achieve the goal without having a helper function.
------------------------------------------------------------------------
'''
class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

'''
------------------------------------------------------------------------
Solution 3: Mark visited elements
Time: O(MN)
Space: O(1)

Runtime: 20 ms
Memory: 13.5 MB

This is a solution that does not use indices as boundaries, but uses visited
elements as boundaries to change direction of the spiral matrix.
While we change directions only once per each addition to the result array,
we check whether the next_row and next_col we will move to are not out of
bounds or already visited. If it's out of bounds or already visited, it
means that we should stop changing directions because we've reached the
last element of the matrix. In a spiral matrix, there would always be a
next element to move into if there are any.
------------------------------------------------------------------------
'''
class Solution(object):
    def spiralOrder(self, matrix):
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result

'''
------------------------------------------------------------------------
Solution 4: Simulation - mark visited elements #2
Time: O(MN)
Space: O(1)

Runtime: 27 ms
Memory: 13.6 MB

This is another version of a simulation solution where we mark visited cells.
It's really intuitive and concise, and we do the following:
  - iterate until length of result array is equal to R * C
  - calculate next cell
    - if valid cell, append to res and mark as visited
    - otherwise, revert the calculation and update direction
------------------------------------------------------------------------
'''
class Solution(object):
    def spiralOrder(self, matrix):
        # maximum pos int for m,n is 100
        VISITED = 101
        
        # directions array
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        current_direction = 0
        
        # column and row length
        C = len(matrix[0])
        R = len(matrix)
        
        # result array
        res = [matrix[0][0]]
        matrix[0][0] = VISITED
        next_row, next_col = 0, 0
        
        # iterate until we've visited all cells
        while len(res) < R*C:
            current_direction %= 4
            next_row += directions[current_direction][0]
            next_col += directions[current_direction][1]
            
            # if next cell exists and isn't visited, add to res and mark as visited
            if next_row < R and next_col < C and matrix[next_row][next_col] != VISITED:
                res.append(matrix[next_row][next_col])
                matrix[next_row][next_col] = VISITED
            # if next cell isn't valid, reverse change and change direction
            else:
                next_row -= directions[current_direction][0]
                next_col -= directions[current_direction][1]
                current_direction += 1

        return res