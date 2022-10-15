'''
------------------
Difficulty: Easy
------------------

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

'''
------------------------------------------------------------------------
Solution 1 - Character Mapping with Dictionary (two hashmaps)
Time: O(n)
Space: O(1) -> since the size of the ASCII character set is fixed and the keys in our dictionary are all valid ASCII characters.

Runtime: 82 ms
Memory: 14.6 MB

This is a solution using two hashmaps to track the mapping of each characters.
Either we initialize one or two hashmaps, it is important to make sure that
a character is mapped to one character and one character only.
Therefore, there could be three scenarios:
  - Mapping does not exist
  - Mapping from either direction exists, and they don't match
  - Mapping from either direction exists, and they do match
Only problematic case is the second one, in which case we return False.
------------------------------------------------------------------------
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        mapST = {}
        mapTS = {}
        
        for i in range(len(s)):
            if s[i] not in mapST and t[i] not in mapTS:
                mapST[s[i]] = t[i]
                mapTS[t[i]] = s[i]
            elif mapST.get(s[i]) != t[i] or mapTS.get(t[i]) != s[i]:
                return False
        
        return True

'''
------------------------------------------------------------------------
Solution 2 - Character Mapping with Dictionary (one hashmap)
Time: O(n)
Space: O(1)

Runtime: 31 ms
Memory: 14.9 MB

Same logic as solution 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap and t[i] not in hashmap.values():
                hashmap[s[i]] = t[i]
            elif hashmap.get(s[i]) != t[i]:
                return False
        
        return True

'''
------------------------------------------------------------------------
Solution 3 - First Occurrence Transformation
Time: O(n)
Space: O(n)

Runtime: 49 ms
Memory: 15.5 MB

This is a pretty clever solution using a hashmap that maps each character to
its first occurence index. Essentially, if two strings are isomorphic,
they should match if you turn every character to it's first occurence index.
e.g. title => 01034 AND paper => 01034, thus they're isomorphic.
One thing to be careful here is when indices are two digit numbers.
There could be scenarios where we think 11 0 and 1 10 are the same if we don't
separate them with spaces (line 129).
------------------------------------------------------------------------
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        return self.transformString(s) == self.transformString(t)
    
    def transformString(self, string):
        index_map = {}
        res = []
        
        for i, c in enumerate(string):
            if c not in index_map:
                index_map[c] = i
            res.append(str(index_map[c]))
        
        return " ".join(res)