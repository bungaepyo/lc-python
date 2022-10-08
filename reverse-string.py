'''
------------------
Difficulty: Easy
------------------

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"] 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pointers
Time: O(n)
Space: O(1)

Runtime: 21.3 ms
Memory: 157 MB

This is a very straightforward two pointers solution that reverses the list.
Start the two pointers from the very beginning and end, swap the two, and continue
by increasing start pointer and decreasing end pointer by 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseString(self, s):
        start = 0
        end = len(s)-1
        while start <= end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return s

'''
------------------------------------------------------------------------
Solution 2: Recursion
Time: O(n)
Space: O(n)

Runtime: 43.5 ms
Memory: 147 MB

You can even achieve the goal with recursion using a helper function.
However, this has larger space complexity due to the recursive stack being O(n).
------------------------------------------------------------------------
'''
class Solution(object):
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)

        helper(0, len(s)-1)