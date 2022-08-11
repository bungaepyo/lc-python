'''
------------------
Difficulty: Hard
------------------
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursion with Memoization
Time: O(S*P*(S+P))
Space: O(S*P) => this solution exceeds memory limit with python

Runtime: ? ms
Memory: ? MB

This solution is probably the most intuitive solution using recursion and memoization.
First, using remove_duplicate_stars function we truncate multiple juxtaposed stars into
just one star since * can represent any sequence of characters anyways.
Second, we go through the recursive calls in the helper function using our
memoization hashmap dp, which takes (s,p) pair and key and True/False boolean as value.
By using memoization, we are able to optimise the recursion by preventing duplciate
computations. Therefore, we need to check the hashmap everytime we run the helper function.
Otherwise, there are five scenarios:
  - p == s or p == '*' ===> memoize True
  - p == '' or s == '' ===> memoize False
  - p[0] == s[0] or p[0] == '?' ===> proceed recursive call helpers(s[1:], p[1:])
  - p[0] == '*' ===> proceed recursive call helpers(s[1:], p) or helpers(s, p[1:])
    - first one is when p matches one or more char
    - second one is when p matches no char
after the recursion reaches an end, return memoized dp[(s,p)]
------------------------------------------------------------------------
'''
class Solution(object):
    def isMatch(self, s, p):

        def remove_duplicate_stars(p):
            new_string = []
            for char in p:
                if not new_string or char != '*':
                    new_string.append(char)
                elif new_string[-1] != '*':
                    new_string.append(char)
            return ''.join(new_string)
        
        def helper(s, p):
            if(s, p) in dp:
                return dp[(s,p)]
            
            if p == s or p == '*':
                dp[(s,p)] = True
            elif p == '' or s == '':
                dp[(s,p)] = False
            elif p[0] == s[0] or p[0] == '?':
                dp[(s,p)] = helper(s[1:], p[1:])
            elif p[0] == '*':
                dp[(s,p)] = helper(s[1:], p) or helper(s, p[1:])
            else:
                dp[(s,p)] = False
            
            return dp[(s,p)]
        
        dp = {}
        p = remove_duplicate_stars(p)
        return helper(s,p)

'''
------------------------------------------------------------------------
Solution 2 - Dynamic Programming
Time: O(S*P) => nested for loop each length of S & P
Space: O(S*P) => store matrix

Runtime: 1733 ms
Memory: 22.1 MB

This is a solution using the dynamic programming approach. The runtime for
this solution is not the best, but it's way more readable than easier to
understand than the dp soltion in the article.
First, accounting for empty s or p, we create a matrix of size (len(p)+1)*(len(s)+1),
and set [0][0] to True, since if they both are empty it still matches.
Second, accounting for the case in which pattern begins with one or more *,
we assign True to the first row (s is empty) until non-star char is found.

One thing to note: dp[i][j] is whether dp[i-1][j-1] had a match.

Third, in a nested for loop iterating both s and p, we consider the following
two scenarios:
  - if p[j-1] is equal to s[i-1] or '?'
    - this means that there was a match in the index right before, thus just use
    the value of the previous one.
  - if p[j-1] is equal to '*'
    - this means that we could either increase the string or the pattern
    to see if there is a potential match. Thus, we use an 'or' operator to
    compute this.
    - this is just like dp[(s,p)] = helper(s[1:], p) or helper(s, p[1:])
    from solution one.

Return the last element of the matrix: dp[-1][-1]
------------------------------------------------------------------------
'''
class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]