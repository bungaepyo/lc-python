'''
------------------
Difficulty: Easy
------------------

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string?
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

'''
------------------------------------------------------------------------
Solution 1 - String Matching
Time: O(n)
Space: O(1)

Runtime: 23 ms
Memory: 13.6 MB

This is a solution using string matching method. In order to fulfill problem
requirements, we will check needle length and return 0 is empty, and return -1
if no match is found at the end.
Since a match cannot exist when the number of haystack characters left for comparison
is less than the length of needle, we will run a loop from 0 to len(haystack)-needleLength+1.
Whenever the first characters match, we will slice a substring with length equal to needle
starting that index and compare that substring with need. Return that index if they match.
------------------------------------------------------------------------
'''
class Solution(object):
    def strStr(self, haystack, needle):
        needleLength = len(needle)
        if needleLength < 1:
            return 0
        for i in range(len(haystack)-needleLength+1):
            if haystack[i] == needle[0]:
                substring = haystack[i:i+needleLength]
                if substring == needle:
                    return i
        return -1

'''
------------------------------------------------------------------------
Solution 2 - String Matching (simplified)
Time: O(n)
Space: O(1)

Runtime: 15 ms
Memory: 13.4 MB

This is a more concise version of solution #1. Line 80 is most important.
------------------------------------------------------------------------
'''
class Solution(object):
  def strStr(self, haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1