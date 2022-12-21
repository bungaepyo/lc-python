'''
------------------
Difficulty: Medium
------------------

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01

Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01 

Constraints:

1 <= n <= 30
1 <= k <= 2n - 1
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n)

Runtime: 24 ms
Memory: 13.5 MB

This is a really smart recursive solution that uses the characteristics of
the given data structure. As you can see, kth element of nth row is decided by
the element's parent in the n-1th row. Therefore, we would have to see what
its parent was in order to return the correct integer for kth element in nth row.

We need to know these two things when traversing the rows in reverse order:
  - K is odd: parent element is (k+1)//2th element in n-1th row
  - K is even: parent element is k//2th element in n-1th row

Therefore if the parent element is 0, even elements should return 1 and
odd elements should return 0. If the parent element is 1, it's vice versa.

Base case is the first row where we only have one number 0.
------------------------------------------------------------------------
'''
# think of the problem like this
#           0
#       /        \
#      0           1
#    /   \       /    \
#   0     1     1      0
#  / \   / \   / \    / \
# 0  1  1   0  1  0   0  1

class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n-1, k//2) == 0 else 0
        else:
            return 0 if self.kthGrammar(n-1, (k+1)//2) == 0 else 1