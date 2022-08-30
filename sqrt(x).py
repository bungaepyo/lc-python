'''
------------------
Difficulty: Easy
------------------
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:

0 <= x <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1 - Pocket Calculator Algorithm (NOT A REAL SOLUTION)
Time: O(1)
Space: O(1)

Runtime: 28 ms
Memory: 13.3 MB

This is not a real solution, but a math concept exercise that shows
how real world pocket calculators do the calculations for square roots.
  - Algorithm: sqrt(x) = e**(0.5 * log(x))
So, return left if right^2 is bigger than x.
Otherwise, return right because this means right^2 is exactly x.
------------------------------------------------------------------------
'''
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

'''
------------------------------------------------------------------------
Solution 2 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 27 ms
Memory: 13.3 MB

This is a solution that uses the fundamental concepts of binary search.
Before we start, note that 0 and 1 are exceptions. We return x in this case.
First thing we need to realize in this binary search solution is that the sqrt
is always going to be greater than 0 and less than x//2.
Therefore, we set left as 2 and right as x // 2. (floor division)
While left <= right, we update left and right according to a set of conditions.
Take the first mid guess as left + (right - left) // 2, which is the
non-overflowing mid.
  - If pivot squared is larger than x, it means that pivot is too big.
    Thus, we set right = pivot - 1
  - If pivot squared is smaller than x, it means that pivot is too small.
    Thus, we set left = pivot + 1
  - If pivot squared is equal to x, we found the perfect sqrt of x.
    Thus, just return pivot.

IMPORTANT!
If the loop ended without returning anything, we want to return the
smaller integer between right and left. Since the while loop condition is
left <= right, we return right.
------------------------------------------------------------------------
'''
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left)//2
            num = pivot * pivot
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot
        
        return right
