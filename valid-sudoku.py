'''
------------------
Difficulty: Medium
------------------

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

'''
------------------------------------------------------------------------
Solution 1 - Hash Set
Time: O(N^2)
Space: O(N^2)

(debatable if it's N^2 since we know the value of N)

Runtime: 79 ms
Memory: 13.4 MB

This is probably the most straightforward solution using hash sets.
The the first key to this solution is actually
  (1) realizing that you need to create a set for each row, column, and box. 
It is hard otherwise to check if there is a duplciate element in each 
row, col, and box. In a nested for loop, check each value if it already 
exists in the set (r or c). (skip, of course, it it's ".")
The second key to this solution is
  (2) checking each box by using this formula: (r//3)*3 + c//3
Each box would have assigned number (0-8) and it increases from left to right.
e.g. [[0,1,2],
      [3,4,5],
      [6,7,8]]
The weight for row is 3 times that of column in calculating box number because
- every 3 rows => there are 3 boxes
- every 3 columns => there is 1 box.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidSudoku(self, board):
        N = len(board)
        
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                
                if val == '.':
                    continue
                
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                idx = (r//3)*3+c//3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

'''
------------------------------------------------------------------------
Solution 2 - Bit Masking
Time: O(N^2)
Space: O(N)

(debatable if it's N^2 since we know the value of N)

Runtime: 62 ms
Memory:	13.7 MB

This solution basically has the same concept from the previous hashset solution,
creating a datastructure for checking each row, col, and box.
However, the difference is that this solution uses the bit masking technique in order
to reduce the space complexity from O(N^2) to O(N).
Instead of initializing a set or a fixed-length list for each row, col, or box,
this solution uses an integer (initally 0).
Using the bitwise operation & (AND), it checks whether the binary number location at
the position we want to check (0-8) is 1 or 0.
  e.g. e.g. 0001000 => this would mean that 4 already exists in a (row, col, box)
If the & (AND) operator returns 0, set it to 1 with the | (OR) operator.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValidSudoku(self, board):
        N = 9
        
        rows = [0]*N
        cols = [0]*N
        boxes = [0]*N
        
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                
                pos = int(board[r][c])-1
                
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)
                
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)
                
                idx = (r//3)*3 + (c//3)
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)
        
        return True