'''
------------------
Difficulty: Medium
------------------

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
  Input: n = 1
  Output: "1"
  Explanation: This is the base case.
  
Example 2:
  Input: n = 4
  Output: "1211"
  Explanation:
  countAndSay(1) = "1"
  countAndSay(2) = say "1" = one 1 = "11"
  countAndSay(3) = say "11" = two 1's = "21"
  countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
1 <= n <= 30
'''

'''
------------------------------------------------------------------------
Solution 1 - Iteration
Time: O(n^2)
Space: O(n)

Runtime: 36 ms
Memory: 13.1 MB

This solution uses simple iteration with a nested for loop to build the result string.
The first for loop is for iteration n-1 times (since "1" is already the base
case for countAndSay(1)). Each iteration uses res to count and say. The key
here is (1) res = temp after each iteration and (2) temp += str(count)+letter
right before - we still need to add the last count and letter to temp.
The second for loop is for either increasing count or switching to a different 
letter depending on which letter we're looking at.
------------------------------------------------------------------------
'''
class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for _ in range(n-1):
            letter = res[0]
            temp = ""
            count = 0
            for l in res:
                if l == letter:
                    count += 1
                else:
                    temp += str(count)+letter
                    letter = l
                    count = 1
            temp += str(count)+letter
            res = temp
        return res