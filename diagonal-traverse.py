'''
------------------
Difficulty: Medium
------------------

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order. 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4] 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1: Diagonal Iteration and Reversal
Time: O(nm)
Space: O(nm)

Runtime: 158 ms
Memory: 16.5 MB

In this solution, we iterate all possible diagonals that go from right to left,
and add them while reversing the even numbered diagonals.

After initializing the result array and the intermediate array (temp array for each diagonal),
we iterate possible heads throughout the first row and the last column.
We do that because first row and last column contain the heads for diagonals
going from right to left => range(R + C - 1)

For each diagonal, we figure out the starting row and colum index by looking at d.
  - if d is smaller than C, which means the diagonal head is on the first row,
    we assign r = 0 and c = d
  - if d is greater than or equal to C, it means that the diagonal head is now on the last column,
    so we assign r = d-C+1 and c = C-1

And until one of (r, c) goes out of bounds (since matrix doesn't have to be square),
we append to mat[r][c] to intermediate array and increase r and decrease c.

After we finish iterating all the diagonal elements, we reverse it if it's even numbered diagonal.
Reversing can be done by intermediate[::-1] => from start to end by 1 in reverse order
------------------------------------------------------------------------
'''
class Solution(object):
    def findDiagonalOrder(self, mat):
        # check for empty matrices
        if not mat or not mat[0]:
            return []
        
        # variables to track the size of matrix
        R, C = len(mat), len(mat[0])
        
        # two arrays
        result, intermediate = [], []
        
        # go over all the elements in the first row and
        # the last column in order to cover all possible diagonals
        for d in range(R + C - 1):
            
            # clear intermediate array
            intermediate = []
            
            # figure out the head of diagonal
            r = 0 if d < C else d-C+1
            c = d if d < C else C-1
            
            # iterate the diagonal elements
            while r < R and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # reverse even numbered diagonals
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result

'''
------------------------------------------------------------------------
Solution 2: Simulation
Time: O(nm)
Space: O(1)

Runtime: 434 ms
Memory: 16.3 MB

This is honestly overly complicated solution. Check out:
https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING

This is a solution that exactly simulates the diagonal traversal the problem is
asking to perform. There are two things to consider while iterating through
the elements that are in bound:
  - direction
    - 1 if going up
    - 0 if going down
  - next head
    - going up: [i, j] -> [i-1, j+1]
    - going down: [i, j] -> [i+1, j-1]
------------------------------------------------------------------------
'''
class Solution(object):
    def findDiagonalOrder(self, mat):
        # check for empty matrices
        if not mat or not mat[0]:
            return []
        
        # variables to track the size of matrix
        R, C = len(mat), len(mat[0])
        
        row, col = 0, 0
        direction = 1
        result = []
        
        while row < R and col < C:
            
            # first, add the current element to result array
            result.append(mat[row][col])
            
            # move along current diagonal depending on direction
            # going up: [i, j] -> [i-1, j+1]
            # going down: [i, j] -> [i+1, j-1]
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)
            
            # check if next element is within bounds
            # if not in bounds, we find the next diagonal head
            if new_row < 0 or new_row == R or new_col < 0 or new_col == C:
                
                if direction:
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (col == C-1)
                    col += (col < C-1)
                
                else:
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    col += (row == R - 1)
                    row += (row < R - 1)
                
                # flip direction
                direction = 1 - direction
            else:
                row = new_row
                col = new_col

        return result