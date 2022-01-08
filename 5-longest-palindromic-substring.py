'''
------------------
Difficulty: Medium
------------------

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

'''
------------------------------------------------------------------------
Solution 1 - Dynamic Programming
Time: O(n^2) - worst case for + while loop "aaa....aaa"
Space: O(1) - only stores res

Runtime: 872 ms
Memory: 13.7 MB

This solution is a classic one using dynamic programming.
Defining, palindrome function P(i, j) as:
  - P(i, j) => true if the substring from S[i] to S[j] is a palindrome
  - P(i, j) => false otherwise

P(i, j) needs to meet two conditions:
  (1) P(i+1, j-1) => substring inside (1 length shorter from both start and end) needs to be a palindrome as well
  (2) S[i] == S[j] => characters surrounding should be the same.

  e.g. "cabac" (i = 1, j = 3) => (1) "aba" is a palindrome as well (2) s[0] and s[4] is both "c"

Base cases are:
  - Odd: P(i, i) such as "aba"
  - Even: P(i, i+1) => S[i] == S[i+1] such as "abba"
------------------------------------------------------------------------
'''
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
       
    def helper(self,s,l,r): 
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]

'''
------------------------------------------------------------------------
Solution 2 - Dynamic Programming, Matrix
Time: O(n^2)
Space: O(n^2) - stores 2D matrix (n by n)

Runtime: 7149 ms
Memory: 21.2 MB

This solution also uses dynamic programming, and a n by n true/false matrix labelled by index.
Definition, condition, base case of a palindrome are all the same.
First step is to create a n by n matrix dp and and fill it with False or 0.
Second step is to fill dp[i][i] with True, since single character strings are always palindrome.
Third step is to only iterate through one side of the matrix (upper or lower triangle) and upate to True if palindrome is found.
We should update the longest_palindrom whenever we find one in order to keep it the longest palindromic substring.
------------------------------------------------------------------------
'''
class Solution(object):
    def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
        # fill the dp table by iterating through upper triangle
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                # second condition of palindrome
                if s[i] == s[j]:
                    # even case OR first condition of palindrome
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # update longest palindrome
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]

        return longest_palindrom