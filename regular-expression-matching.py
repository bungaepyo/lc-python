'''
------------------
Difficulty: Hard
------------------

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: See solution
Space: See solution

Runtime: 1856 ms
Memory: 13.4 MB

Excellent explanation: https://levelup.gitconnected.com/solving-for-recursive-complexity-736439987cb0

-------------------
#1 PSEUDO-CODE
-------------------
def recurse(text, pattern):
    ### recursion rock bottom
    if reached end of pattern:
        return whether reached end of text
    
    ### check if the current character matches the pattern
    character_match = pattern[0] is either text[0] or "."

    if pattern[1] exists and pattern[1] is "*":
        ### checking if we can move on from the asterisk
        skip_asterisk_matched = recurse(text, pattern[2:])

        ### checking if the asterisk is still used
        keep_asterisk_matched = character_match and recurse(text[1:], pattern)
    
    else:
      ### no asterisk? this is easy just continue recursing
      return character_match and recurse(text[1:], pattern[1:])

-------------------
#2 Explanation
-------------------
We are essentially doing checking two things:
  1. checking if the current character of the text matches the pattern
  2. asking if the pattern will match the text if we modify the text a bit or the pattern a bit or both for the remaining characters

"skip_asteris_match" is true if the text matches the pattern without the asterisk (pattern[2:]) 
i.e if we match 0 of the preceding element. In (text="aab" pattern="c*a*b) where c* didn’t have to match anything,
and this is also how we jump out of the keep_asteris_match trap that we made for ourselves earlier.

"keep_asteris_match" is true if we don’t change the pattern but move along the length of the text (text[1:]).
This is how * is dealt with in recursion, we simply move on to the next character of the text like the current one
never existed and keep the asterisk in the pattern.

e.g. (text="aabb" pattern="a*b*") => (text="abb" pattern="a*b*") => (text="bb" pattern="a*b*") => passed down to "skip_asteris_match" (text="bb" pattern="b*")
=> passed down to "keep_asteris_match" (text="b" pattern="b*") => (text="" pattern="b*") => passed down to "skip_asteris_match" (text="" pattern="") => TRUE

If we don’t see an asterisk we check if that first character matched the pattern with character_match 
and we keep recusing by reducing the input text and pattern by that first matched character (text[1:], pattern[1:]) 
and recursively check if the rest of the string matches.

The final part of recursion which ironically is usually defined at the top of the function, is our recursion rock bottom. 
If we have an empty pattern and an empty string as our inputs, we have the divine knowledge that the pattern will match 
the string because empty matches empty for sure. If only one of them is empty we know that there’s no match.
------------------------------------------------------------------------
'''
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])