'''
------------------
Difficulty: Easy
------------------

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]] 

Constraints:

1 <= numRows <= 30
'''

'''
------------------------------------------------------------------------
Solution 1 - Dynamic Programming
Time: O(numRows^2)
Space: O(1) -> result array does not count

Runtime: 35 ms
Memory: 13.4 MB

This is a straightforward DP solution. If numRows is 1 or 2, we return corresponding arrays.
While reducing numRows (after subtracting 2), we make a current array each time.
First and last element of current array should always be 1.
And for range i from 1 to last index of lastRow, we append the sum of element
at index i-1 and i to current array.
Then, append current array to res and decrease numRows.
------------------------------------------------------------------------
'''
class Solution(object):
    def generate(self, numRows):
        res = [[1],[1,1]]
        if numRows == 1:
            return [res[0]]
        if numRows == 2:
            return res
        
        numRows -= 2
        
        while numRows > 0:
            curr = [1]
            lastRow = res[-1]
            
            for i in range(1, len(lastRow)):
                prev = i-1
                post = i
                curr.append(lastRow[prev] + lastRow[post])
            
            curr.append(1)
            res.append(curr)
            numRows -= 1
        
        return res

'''
------------------------------------------------------------------------
Solution 2 - Dynamic Programming #2
Time: O(numRows^2)
Space: O(1)

Runtime: 23 ms
Memory: 13.5 MB

This is a different version of a DP solution. Each iteration of numRows,
we initialize an array full of None and make first and last element 1.
And then basically do the same thing: get previous row_num and add j-1 and j.
------------------------------------------------------------------------
'''
class Solution(object):
    def generate(self, numRows):
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle