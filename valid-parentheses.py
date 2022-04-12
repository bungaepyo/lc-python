'''
------------------
Difficulty: Easy
------------------

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

'''
------------------------------------------------------------------------
Solution 1: two pointer method
Time: O(n)
Space: O(n)

Runtime: 34 ms
Memory: 13.8 MB

This is the most intuitive solution using the stack data structure.
Key thing to note while using this solution is that, in valid parentheses, sub-parentheses are also valid.
Therefore, if we create a stack and remove matching parentheses as soon as we find them,
we would be able to have an empty stack at the end of the algorithm.
After pre-populating the mapping dictionary, we would have to iterate the characters in the string
to see if it's an opening bracket or closing bracket.
If opening bracket, add to the stack, and if closing bracket, pop and save the top element of the stack.
If those two aren't pairs, return false.
Otherwise, if all element found their pairs, there will be nothing left in the stack since we popped
all the opening brackets that have been added to the stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack