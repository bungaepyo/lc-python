'''
------------------
Difficulty: Easy
------------------

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

'''
------------------------------------------------------------------------
Solution 1 - Vertical Scanning, enumerate()
Time: O(n)
Space: O(1)

Runtime: 16 ms
Memory: 13.6 MB

Best solution I've seen so far using vertical scanning method, but very pythonic.
First, get the shortest length string from the list as longest common prefix cannot be longer than that.
Second, use enumerate() and iterate through each index and char.
Third, within the index & char for loop, iterate through the list to see every string's ith index matches char.
Fourth, if any of the string's ith index doesn't match char, return shortest string sliced before i.
------------------------------------------------------------------------
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

'''
------------------------------------------------------------------------
Solution 2 - Vertical Scanning
Time: O(n)
Space: O(1)

Runtime: 28 ms
Memory: 14 MB

Another vertical scanning solution, but less pythonic.
Sets default to the first string in the list, and iterates through its indices.
In a nested for loop, compares the characters of the same index.
Checks (1) if any string is shorter than the first one OR (2) characters don't match => return strs[0][:i]
------------------------------------------------------------------------
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

'''
------------------------------------------------------------------------
Solution 3 - zip()
Time: O(n)
Space: O(1)

Runtime: 21 ms
Memory: 13.6 MB

Also a very pythonic solution using zip().
Compress and put each character of same index in a tuple using zip(*strs) => [('f','f'), ('l','l'),('o','e')]
Using set() only leave unique character, and add the character to the result string only if length of set is 1.
Return existing result string otherwise.
------------------------------------------------------------------------
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                res += char[0]
            else:
                return res
        return res