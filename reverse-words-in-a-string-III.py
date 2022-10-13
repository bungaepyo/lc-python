'''
------------------
Difficulty: Medium
------------------

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD" 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''

'''
------------------------------------------------------------------------
Solution 1: Simulation
Time: O(n)
Space: O(n)

Runtime: 140 ms
Memory: 15.7 MB

This is a recycled version of Reverse Words in a String problem solution #1
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseWords(self, s):
        res = []
        word = []

        for i in range(len(s)):
            if s[i] == " " and len(word) > 0:
                res.append("".join(word))
                word = []
            elif s[i] != " ":
                word.insert(0, s[i])
                if i == len(s)-1:
                    res.append("".join(word))

        return " ".join(res)