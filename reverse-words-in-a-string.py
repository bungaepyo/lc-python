'''
------------------
Difficulty: Medium
------------------

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces. 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string. 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
'''

'''
------------------------------------------------------------------------
Solution 1: Simulation
Time: O(n)
Space: O(n)

Runtime: 32 ms
Memory: 14.1 MB


------------------------------------------------------------------------
'''
class Solution(object):
    def reverseWords(self, s):
        res = []
        word = []

        for i in range(len(s)):
            if s[i] == " " and len(word) > 0:
                res.insert(0, "".join(word))
                word = []
            elif s[i] != " ":
                word.append(s[i])
                if i == len(s)-1:
                    res.insert(0, "".join(word))

        return " ".join(res)

'''
------------------------------------------------------------------------
Solution 2: Python Built-in Method
Time: O(n)
Space: O(n)

Runtime: 20 ms
Memory: 13.9 MB

This is a solution using python built-in methods.
  - split() creates a list of words in s
  - reversed() will reverse it
  - " ".join will create a string with words in input list separated by a space.
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))

'''
------------------------------------------------------------------------
Solution 3: Reverse the whole string and then reverse each word
Time: O(n)
Space: O(n)

Runtime: 31 ms
Memory: 13.9 MB

This solution does the following:
  - (1) gets rid of leading and trailing spaces
  - (2) reverses the whole string
  - (3) finds the start and end of each word and reverse it
------------------------------------------------------------------------
'''
class Solution:
    def trim_spaces(self, s):
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        
        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
                
    def reverseWords(self, s):
        # converst string to char array 
        # and trim spaces at the same time
        l = self.trim_spaces(s)
        
        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)
        
        # reverse each word
        self.reverse_each_word(l)
        
        return ''.join(l)