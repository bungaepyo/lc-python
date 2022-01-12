'''
------------------
Difficulty: Medium
------------------

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1: visit and store digits & check overflow at the end
Time: O(log(n)) - visit each digit
Space: O(log(n)) - store each digit

Runtime: 15 ms
Memory: 13.4 MB

This is my original solution. I visit each digit using a carry that is later /= 10.
I pick the last number of the carry by doing %= and add the number to a list.
Using list length & index of each number stored in the list, I decide the digit and append to the result integer.
Applying sign and checking for overflow is done right before returning the result.
------------------------------------------------------------------------
'''
class Solution(object):
    def reverse(self, x):
        digits = []
        carry = x if x >= 0 else -1*x
        sign = 1 if x >= 0 else -1
        
        while carry > 0:
            rem = carry % 10
            digits.append(rem)
            carry /= 10
            
        res = 0
        length = len(digits)
        for i in range(length):
            res += 10**(length-1-i)*digits[i]
        
        res *= sign
        return res if (res >= -1*2**31 and res < 2**31-1) else 0