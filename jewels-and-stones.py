'''
------------------
Difficulty: Easy
------------------

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashSet
Time: O(n+m) -> n, m are lengths of jewels and stones
Space: O(n) -> n is length of jewels

Runtime: 29 ms
Memory: 13.4 MB

This is a simple solution using a hashset. We add all the characters in jewels
to the hashset, and it will only store unique characters. While iterating
stones, if you see a character that exists in the hashset, increase count.
------------------------------------------------------------------------
'''
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hashset = set()
        
        for jewel in jewels:
            hashset.add(jewel)
        
        res = 0
        for stone in stones:
            if stone in hashset:
                res += 1
            
        return res

'''
------------------------------------------------------------------------
Solution 1.5 - HashSet (simplified)
Time: O(n+m)
Space: O(n)

Runtime: 11 ms
Memory: 13.6 MB

This solution uses the same idea as solution 1, but is much more simplified.
------------------------------------------------------------------------
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)