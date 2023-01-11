'''
------------------
Difficulty: Hard
------------------

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word. 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking + Trie
Time: O(M(4*3^(L-1))), M is number of board cells and L is max length of words
Space: O(N)

Note on time complexity
  - Algorithm loops around all the cells in the board -> M
  - In backtracking maximum number of steps we would need for each starting cell
    wouuld be its time complexity. 4 directions, 3 neighbors (excluding where it came from),
    L-1 is workd length left. -> 4*3^(L-1)

Runtime: 862 ms
Memory: 15.3 MB

This is a solution that combines backtracking technique and trie data structure.
The underlying intuition can be broken down into 3 parts:
  - (1) we build a trie of words, so that we can check prefixes fast
  - (2) starting from each cell, we check if the value is a valid prefix (potential starting point of a word)
  - (3) if valid, we start backtracking from the cell and add any words we discover on the way

(1) building a trie with words and (2) iterating through all the board cells
aren't hard. (3) backtracking function could be a little bit tricky.

We essentially drill down the board & trie simultaneously until we find
any matching words.
  - if we find a matching word, add to result array and remove word from
    the trie so that we don't have duplicates
  - if we don't find a matching word, continue searching for 4 directions

There are a couple things worth taking note of:
  - we need to set board[row][col] = "#" and reset it to letter in order
    to make sure that we don't use the same cell value twice
  - saving the actual words on the last TrieNode will improve performance,
    since we don't need to pass prefix as params or rebuild words
  - once you find a word, you would never need it again. Therefore,
    gradually pruning (removing) the nodes in Trie during backtracking
    will be helpful in terms of time complexity.
------------------------------------------------------------------------
'''
class Solution(object):
    def findWords(self, board, words):
        res = []
        KEY = "$"
        
        # 1. Build a trie with words
        root = {}
        
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr[KEY] = word
        
        # 2. Backtracking helper function
        def backtracking(row, col, parent):
            letter = board[row][col]
            curr = parent[letter]
            
            # Check if we found a word match
            word_match = curr.pop(KEY, False)
            if word_match:
                # Also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() for results
                res.append(word_match)
            
            # Before the exploration, mark the cell as visited 
            board[row][col] = '#'
            
            directions = {(1,0),(-1,0),(0,1),(0,-1)}
            for d in directions:
                new_r = row + d[0]
                new_c = col + d[1]
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if board[new_r][new_c] not in curr:
                    continue
                backtracking(new_r, new_c, curr)
            
            # End of exploration, we restore the cell
            board[row][col] = letter
            
            # Optimization: incrementally remove the matched leaf node in Trie
            if not curr:
                parent.pop(letter)
        
        # 3. Need to check all cell values
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val in root:
                    backtracking(r, c, root)

        return res