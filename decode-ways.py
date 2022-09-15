'''
------------------
Difficulty: Medium
------------------

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters
using the reverse of the mapping above (there may be multiple ways).

For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer. 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion with Memoization
Time: O(n) -> Memoization helps in pruning the recursion tree and hence decoding for an index only once.
Space: O(n) -> The dictionary used for memoization would take the space equal to the length of the string.

Runtime: 41 ms
Memory: 14.7 MB

This is a solution using a recursion with the memoization technique.
Since this problem is about returning the number of ways we can decode a
string, we can recursively split the first or first two characters and
add up the resulting number of valid ways.
There are only a few constraints we need to keep for the recursion:
  - (1) string that is being split needs to be 1 <= s <= 26
  - (2) leftover string cannot have a leading zero
First, since we are passing substrings into recursive calls, base case would be
when the length of string is 0 => return 1
Second, due to constraint (2), return 0 if s[0] == "0"
Then, do the recursion for splitOne and conditionally for splitTwo

This is a normal recursive solution, and would not pass due to exceeding time limit.
Thus, we need to initialize a memoization map as global variable and use it whenever we can.
  - Add a memoization check in the very beginning
  - Add a memoization add in the very end
------------------------------------------------------------------------
'''
class Solution(object):
    memo = {}

    def numDecodings(self, s):
        #check if memoized
        if s in self.memo:
            return self.memo[s]

        #base case of recursion, reached the end
        if len(s) == 0:
            return 1
        
        #filter out leading zeros
        if s[0] == "0":
            return 0

        #split only 1 digit
        splitOne = self.numDecodings(s[1:])

        #split 2 digits (if lte 26)
        splitTwo = self.numDecodings(s[2:]) if len(s) >= 2 and int(s[:2]) <= 26 else 0
        
        self.memo[s] = splitOne + splitTwo

        return self.memo[s]

'''
------------------------------------------------------------------------
Solution 2: Iteration
Time: O(n) -> We iterate the length of dp array which is N+1.
Space: O(n) -> The length of the DP array.

Runtime: 24 ms
Memory: 13.3 MB

This is a dp style solution with an iterative approach, which is slightly
less intuitive but very smart.
Here, the core concept is to use a N+1 size dp array, in which dp[i] represents
the number of decode ways from s[0] to s[i-1]. And we initialize with the first two indices filled.

Think of this as a baton relay race:
  - indices passing values as batons

Starting from index 2 (ofc if there is), the current element dp[i] would be
getting passed the values from dp[i-1] and dp[i-2] if each of those can be decoded.

The decoding conditions are:
  - single decode is possible if previous element is not 0
    (as long as previous element is not 0, you would be only adding a single digit to the sequence)
  - double decode is possible if 10 <= s[i-2:i] <= 26
    (it cannot be anything greater than 26, or less than 10 like 06)

After filling out the dp array, we return the last element,
which contains the total number of decode ways.
------------------------------------------------------------------------
'''
class Solution(object):
    def numDecodings(self, s):
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
                
        return dp[len(s)]

'''
------------------------------------------------------------------------
Solution 3: Iterative, Constant Space
Time: O(n)
Space: O(1)

Runtime: 23 ms
Memory: 13.3 MB

This iterative solution with constant space basically optimizes the second
solution by only looking at previous two elements, and constantly updating them.
------------------------------------------------------------------------
'''
class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            return 0
    
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        
        return one_back