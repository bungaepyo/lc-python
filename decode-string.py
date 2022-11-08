'''
------------------
Difficulty: Medium
------------------

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

'''
------------------------------------------------------------------------
Solution 1: Stack
Time: O(n)
Space: O(n)

Runtime: 24 ms
Memory: 13.4 MB

This is a solution using the stack data structure. While iterating the input string
which contains the encoded version of the string we want to get,
we pose different action depending on which character we get for each iteration.
The final variable in which we will be storing the decoded string is curString.

Theses are the rules we follow during iteration:
  - if we encounter a number, add it to curNum*10 (to account for double digits)
  - if we encounter a regular character, add it to curString
  - if we encounter a opening bracket '[', we append the curString and curNum to the stack.
    This way, we are able to start fresh with the content in the brackets after
    clearing out whatever we were holding in our hands.
  - if we encounter a closing bracket ']', we pop twice to get the most
    recent number and string (this is reverse order of how we add to the stack).
    You simply curString = prevString + num*curString.
    Since we've accumulated previous strings in one stack element, multiplying currString
    by num and adding it after prevString would give us a decoded version.
------------------------------------------------------------------------
'''
class Solution(object):

    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

'''
------------------------------------------------------------------------
Solution 2: Stack - Optimized
Time: O((maxK^countK)*n) -> maxK is maximum value of k, countK is count of nested k, n is max length of encoded string
Space: O(sum(maxK^countK)*n))

Note:
  - Time Complexity: e.g. 10[ab10[cd]]10[ef] => time complexity would be (10*cd*10*ab) + (10*ef) = 10^2*2
                     maxK is 10, countK is 2, and n is 2.
  - Space Complexity: same example, max stack size would be equivalent to the sum of all decoded strings

Runtime: 19 ms
Memory: 13.7 MB

This stack solution takes a more intuitive approach to dissolve the encoded string.
The base intuition is the following:
  - add everything to the stack until you find a closing bracket (you wouldn't need to decode until you find one)
  - once you find a closing bracket,
    - (1) pop everything from the stack until you find an opening bracket -> save to decodedString
    - (2) pop and throw away the opening bracket
    - (3) calculate how many times to repeat decodedString -> find k and add decodedString k times to stack

After iterating the input string once, you should have a stack with decoded strings.
------------------------------------------------------------------------
'''
class Solution(object):
    def decodeString(self, s):
        stack = []
        
        for char in s:
            if char == ']':
                decodedString = []
                
                while stack[-1] != '[':
                    decodedString.append(stack.pop())
                    
                #pop opening bracket from stack
                stack.pop()
                
                base = 1
                k = 0
                
                #get number k
                while stack and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10
                
                #decode k[decodedString], by pushing decodedString k times to the stack
                while k > 0:
                    for i in range(len(decodedString)-1, -1, -1):
                        stack.append(decodedString[i])
                    k -= 1
            else:
                stack.append(char)
                
        return ''.join(stack)

'''
------------------------------------------------------------------------
Solution 3: 2 Stacks
Time: O(maxK*n) -> maxK is max value of k, n is length of input string
                   we traverse input string once, and iterate k times to decode each pattern.
Space: O(m+n) -> m is number of letters, n is number of digits (two stacks).

Runtime: 15 ms
Memory: 13.4 MB

This is an approach more similar to solution #1, but uses two stacks separately for numbers and string. 
Just like solution 1, this solution has different logic depending on which
character we encounter in each iteration.

Theses are the rules:
  - character => add to currString
  - integer => multiply k by 10 and add to it
  - opening bracket => add current count and string to each stack and reset variables
  - closing bracket => pop previous string (decoded) and add currentString k times. update k string

At the end of the iteration, the variable currentString will hold the decoded string
because we've been adding currentString k times each time we have a new k.
------------------------------------------------------------------------
'''
class Solution(object):
    def decodeString(self, s):
        countStack = []
        stringStack = []
        currentString = ''
        k = 0
        for char in s:
            if char.isdigit():
                k = k*10 + int(char)
            elif char == '[':
                countStack.append(k)
                stringStack.append(currentString)
                currentString = ''
                k = 0
            elif char == ']':
                decodedString = stringStack.pop()
                for _ in range(countStack.pop()):
                    decodedString += currentString
                currentString = decodedString
            else:
                currentString += char
        return currentString

'''
------------------------------------------------------------------------
Solution 4: Recursion
Time: O(maxK*n)
Space: O(n) -> internal call stack

Runtime: 27 ms
Memory: 13.4 MB

This solution simplifies the logic by recursively calling the function
whenever there is more nested content.

These are the rules:
  - whenever the character is not ] and not a digit, add to result string
  - whenever we find a digit, we build k.
  - (1) skip '[' (2) recursive call, which returns decoded string (3) skip ']'
  - add decodedString k times to the result

This recursive solution increases efficiecy by separating the concerns of
operation inside and outside the brackets.
------------------------------------------------------------------------
'''
class Solution(object):
    
    def __init__(self):
        self.index = 0

    def decodeString(self, s):
        result = ''
        
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                result += s[self.index]
                self.index += 1
            else:
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k*10 + int(s[self.index])
                    self.index += 1
                
                #ignore opening bracket
                self.index += 1
                
                decodedString = self.decodeString(s)
                
                #ignore closing bracket
                self.index += 1
                
                while k > 0:
                    result += decodedString
                    k -= 1
        return result