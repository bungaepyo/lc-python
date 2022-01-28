'''
------------------
Difficulty: Medium
------------------

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

'''
------------------------------------------------------------------------
Solution 1 - Iterative
Time: O(n^3) -> not sure
Space: O(3^n)? O(4^n)? 

Runtime: 8 ms
Memory: 13.6 MB

This is the most elegant iterative python solution I've ever seen for this problem.
First create a result list and iterate through each digit in the digits string.
Using a nested for loop in list comprehension, append each incoming character to each existing string in the result list.
This code is so simple it's almost like cheating.
------------------------------------------------------------------------
'''
class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for i in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[i]]]
        return result

'''
------------------------------------------------------------------------
Solution 2 - Recursive
Time: O(n^4)
Space: O(n^4)

Runtime: 16 ms
Memory: 13.6 MB

This solution has a similar intuition as the iterative solution above, just folded out in a recursive way.
Edge case => digits length is 0
Base case => digits length is 1 => return list version of corresponding string
Using backtracking method, recursion travels from right to left until it reaches the first digit.
Line 82 builds a result list beginning from base case.
------------------------------------------------------------------------
'''
class Solution(object):
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]