'''
------------------
Difficulty: Easy
------------------

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''

'''
------------------------------------------------------------------------
Solution 1: Sorting
Time: O(nlogn)
Space: O(1)

Runtime: 25 ms
Memory: 13.1 MB

Suboptimal solution is sorting the two arrays and comparing if they match
exactly. Not optimal because sorting function has time complexity of O(nlogn).
------------------------------------------------------------------------
'''
class Solution(object):
    def isAnagram(self, s, t):        
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))
        if sortedS == sortedT:
            return True
        return False

'''
------------------------------------------------------------------------
Solution 2: Hash Table
Time: O(n)
Space: O(1)

Runtime: 15 ms
Memory: 12.6 MB

Optimized solution is having a hashmap whose key is each character and
value is each character's count in the first string. If the two strings
are anagrams, they should have the same count for each character.
------------------------------------------------------------------------
'''
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hashmap = {}
        for charS in s:
            if charS in hashmap:
                hashmap[charS] += 1
                continue
            hashmap[charS] = 1
        
        for charT in t:
            if charT in hashmap:
                hashmap[charT] -= 1

        for _, value in hashmap.items():
            if value != 0:
                return False
        return True
