'''
------------------
Difficulty: Medium
------------------

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Note: notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# ------------------------
# Solution 1 - Hash Table, Sliding Window
# Time: O(n) - one pass
# Space: O(n) - worst case Hash Table holds all characters in s
# ------------------------
'''
This is my initial solution using hash table and sliding window.
Check repeating characters using a hash table, keep track of longest substring a sliding window (end-start+1).
If you find a string that already exists in the hash table, delete everything before and update index.

Runtime: 423 ms
Memory: 14.5 MB
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maximum = start = end = 0
        hashtable = {}
        
        for i in range(len(s)):
            if s[i] in hashtable:
                start = hashtable[s[i]]+1
                end = i
                hashtable = {k: v for k, v in hashtable.items() if v >= hashtable[s[i]]}
                hashtable[s[i]] = i
            else:
                hashtable[s[i]] = i
                end = i
                maximum = max(maximum, (end-start)+1)
            
        return maximum


# ------------------------
# Solution 2 - Hash Table, Sliding Window, Optimized
# Time: O(n) - one pass
# Space: O(n) - worst case Hash Table holds all characters in s
# ------------------------
'''
This is an optimized soltution using hash table and sliding window.
The way this solution dramatically reduces runtime is by keeping track of each character's next index in mp, and updating i.
i is equivalent to the start, j is equivalent to the end of the sliding window.
Everytime a repeating character is found, i is updated to the mp's character's value (next index) so that current substring only holds unique characters.

Runtime: 45 ms
Memory: 14.2 MB
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        mp = {}
        i = 0

        for j in range(n):
            if s[j] in mp:
                #updating i is most important
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans