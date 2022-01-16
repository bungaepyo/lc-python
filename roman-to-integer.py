'''
------------------
Difficulty: Easy
------------------

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

'''
------------------------------------------------------------------------
Solution 1 - Hashmap
Time: O(n)
Space: O(1)

Runtime: 36 ms
Memory: 13.5 MB

This is my solution using hashmap. There are only couple key points to take not of:
  (1) store roman-integer pairs in a map
  (2) iterate string backwards and add each integer matching to the result
  (3) be aware that the only exception is when the previous integer is greater than the current one
    - this is due to the way roman numbers are written, and you need to subtract from the result in this case
    - e.g. IV => 4, IX => 9, XC => 90, CM => 900
------------------------------------------------------------------------
'''
class Solution(object):
    def romanToInt(self, s):
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        temp = 0
        
        for i in range(len(s)):
            integer = hashmap[s[len(s)-1-i]]
            if integer < temp:
                res -= integer
            else:
                res += integer
            temp = integer
        
        return res
            