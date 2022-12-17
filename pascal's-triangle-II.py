'''
------------------
Difficulty: Easy
------------------

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1] 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''

'''
------------------------------------------------------------------------
Solution 1 - Dynamic Programming
Time: O(n^2)
Space: O(n)

Runtime: 7 ms
Memory: 13.4 MB

This is a dp style solution that makes a little tweak to the pascal triangle I solution.
We save up on the memory by using prev and curr arrays for each rowIndex reduction in
the while loop. Each time we advance a rowIndex, curr becomes prev and we
iterate prev to populate the numbers in curr.
Once we're done filling out our array at last rowIndex, we simply return it.
------------------------------------------------------------------------
'''
class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        rowIndex -= 2
        prev = [1,1]
        while rowIndex >= 0:
            curr = [1]
            for i in range(1, len(prev)):
                num = prev[i-1]+prev[i]
                curr.append(num)

            curr.append(1)
            prev = curr
            rowIndex -= 1

        return prev

'''
------------------------------------------------------------------------
Solution 2 - Brute Force Recursion (Exceeds Time Limit)
Time: O(2^n)
Space: O(n)

Runtime: Exceeds Time Limit ms
Memory: ? MB

This is a brute force recursive solution that I think is pretty smart too.
The recursive function returns the number for a given row and column index
so that it could be just added to the result array.

Simple base case of the recursion is returning 1 when either row or col is 0
or row == col.
------------------------------------------------------------------------
'''
class Solution(object):
    def getRow(self, rowIndex):
        res = []
        for i in range(rowIndex+1):
            res.append(self.getNum(rowIndex, i))
        return res
    
    def getNum(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        return self.getNum(row-1, col-1) + self.getNum(row-1, col)