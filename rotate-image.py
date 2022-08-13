'''
------------------
Difficulty: Medium
------------------

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1: Rotate Groups of Four Cells
Time: O(M) -> M is number of cells in matrix
Space: O(1)

Runtime: 35 ms
Memory: 13.4 MB

This is a solution that mathematically calculates four indices in the matrix
that should swap out each other's positions clockwise.
Key is to use range(n//2 + n%2) and range(n//2).
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

'''
------------------------------------------------------------------------
Solution 2: Reverse on Diagonal and then Reverse Left to Right
Time: O(M) -> M is number of cells in matrix
Space: O(1)

Runtime: 19 ms
Memory: 13.5 MB

This solution uses the transpose and reflect technique to rotate the matrix.
Firstly reverse the matrix around the main diagonal, and then reverse it from left to right.
Key is range(i+1, n) for transpose, range(n//2) for reflect.
------------------------------------------------------------------------
'''
class Solution(object):
    def rotate(self, matrix):
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]