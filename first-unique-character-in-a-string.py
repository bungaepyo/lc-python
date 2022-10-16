'''
------------------
Difficulty: Easy
------------------

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1. 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(n)
Space: O(1) -> alphabet contains 26 letters

Runtime: 155 ms
Memory: 14.5 MB

This is a intuitive solution using a hashmap. In first pass, we update the
hashmap with how many times each character was seen in s. In second pass,
we see if any of the character was only seen once, and return the index.
------------------------------------------------------------------------
'''
class Solution(object):
    def firstUniqChar(self, s):
        hashmap = {}
        for i in range(len(s)):
            if hashmap.get(s[i]):
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        
        for i, c in enumerate(s):
            if hashmap.get(c) == 1:
                return i
        
        return -1