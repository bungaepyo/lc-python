'''
------------------
Difficulty: Hard
------------------

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells. 

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking
Time: O(9!^9)
Space: O(1)

Runtime: 590 ms
Memory: 13.5 MB

This is another good example of how to solve a backtracking problem.
If we want to solve the sudoku by filling in all the blank cells, we should
be able to return to the previous cell and revert its value if we find later
that the current solution is not valid. "Backtracking" is the perfect approach
for that because it essentially allows us to use recursion to travel back
and revert the changes we made, and try other options instead.

Here, the approach we're going to take is the following:
  - We are going to fill in the values column by column on the same row, and
    proceed to the next row
  - While doing so, we are going to check if the value we're trying to put
    (which is any number from 1 to 9) is valid.
    - Number is valid when it's not already in row, col, or sub-box
  - If the current number is valid, we assign that number and proceed to
    the next recursive call. If not, we try other options in within for loop.
  - If none of the current values are valid, it means that at least one of
    the previous cells should have used a different option. This is where
    (1) we backtrack by returning False (2) reset the current value (3) try
    other options (4) return False and backtrack again if none of them work as well.
------------------------------------------------------------------------
'''
class Solution(object):
    def solveSudoku(self, board):
        BOARD_SIZE = len(board)
        
        def is_valid (row, col, str_val):
            for i in range(9):
                if board[row][i] == str_val:
                    return False
                if board[i][col] == str_val:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == str_val:
                    return False
            return True
        
        def backtrack(row=0, col=0):
            if row == BOARD_SIZE:
                return True
            if col == BOARD_SIZE:
                return backtrack(row+1, 0)
            if board[row][col] != ".":
                return backtrack(row, col+1)
            
            for i in range(1, BOARD_SIZE+1):
                if is_valid(row, col, str(i)):
                    board[row][col] = str(i)
                    if backtrack(row, col+1):
                        return True
                    else:
                        board[row][col] = "."
            return False
        
        backtrack()