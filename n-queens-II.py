'''
------------------
Difficulty: Hard
------------------

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]] 

Constraints:

1 <= n <= 9
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking
Time: O(n!)
Space: O(n) -> 3 sets & recursion stack, all linear with number of queens

Note on time complexity: available options for placing a queen on the board
                         decreses from n -> (n-2) -> (n-4) ... -> 0. The reason
                         the options decrease by 2 is because, whenever a
                         new queen is placed, it can potentially attack
                         1 col and 1 diagonal on our current row.

Runtime: 35 ms
Memory: 13.4 MB

This is a classic example of the backtracking technique, so it will be
helpful to understand what's going on in this solution. First, we have to
clarify our constraints for putting a new queen on the board. Queens cannot
be placed on the same row, column, diagonal, and anti-diagonal.
  - Track attacked row & col by their indices
  - Track attacked diagonal & anti-diagonal by (row - col) and (row + col)
    - all diagonal cells have the same (row - col) value
    - all anti-diagonal cells have the same (row + col) value

Therefore, we're going to iterate through the rows, and check if each cell (col)
of that row is an eligible spot for placing a new queen. If so, we are going
to mark the current cell's col, diagonal, anti-diagonal values as visited
and proceed to the next row. If not, we're going to skip the column.
After we're done with the recursion, we need to remove the current col, 
diagonal, anti-diagonal from the sets in order to backtrack one level higher
and try out other paths to find other solutions.
------------------------------------------------------------------------
'''
class Solution(object):
    def totalNQueens(self, n):
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                return 1
            
            res = 0
            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                
                if (col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals):
                    continue
                    
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                
                res += backtrack(row+1, cols, diagonals, anti_diagonals)
                
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
                
            return res
                
        
        return backtrack(0, set(), set(), set())