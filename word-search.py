'''
------------------
Difficulty: Medium
------------------

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

'''
------------------------------------------------------------------------
Solution 1: DFS + Backtracking
Time: O(N*3^L) => where N is the number of cells in the board and L is the length of the word to be matched.

For the backtracking function, initially we could have at most 4 directions to explore,
but further the choices are reduced into 3 (since we won't go back to where we come from).
As a result, the execution trace after the first step could be visualized as a 3-ary tree,
each of the branches represent a potential exploration in the corresponding direction.
Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree,
which is about 3^L.

Space: O(L)

The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. 

Runtime: 8531 ms (differs between python/java)
Memory: 13.4 MB

This is a recursive dfs solution using the backtracking technique.
First off, to simplify the problem, we will use a helper function that performs
a dfs on every element of the matrix. If anything returns true, word exists.
In the backtrack helper function, we recursively check on all four directions
if the next character of the word exists.
Base case:
  - there is no more suffix left to perform the recursion, return True
Constraints:
  - row/col index out of bounds or suffix[0] not the char we're looking for, return False

The place we use the backtracking is before/after the recursive calls to 4 directions.
We are using backtracking because:
  - when we're in the process of finding the word, we want to be able to mark
    which cells we've already visited.
  - when we are moving on to the next cell, we want to be able to use a
    clean matrix all over again.
------------------------------------------------------------------------
'''
class Solution(object):
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False
    

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        self.board[row][col] = '#'

        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False