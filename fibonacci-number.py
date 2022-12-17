'''
------------------
Difficulty: Easy
------------------

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3. 

Constraints:

0 <= n <= 30
'''

'''
------------------------------------------------------------------------
Solution 1 - Plain Recursion
Time: O(2^n)
Space: O(n) -> there is a potential for stack overflow error

Runtime: 1381 ms
Memory: 13.3 MB

This is a plain recursive solution to calculate the fibonacci number.
The base case is when n == 1 or n == 0, because these are the building blocks
of the fibonacci number and all numbers boil down to the sum of these two numbers.

Plain recursion is the slowest way to solve the fibonacci sequence because
it takes exponential time. Every time we make a recursive call, we multiply
the function call by 2 -> O(2^n).
------------------------------------------------------------------------
'''
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

'''
------------------------------------------------------------------------
Solution 2 - Bottom-Up Approach using Tabulation
Time: O(n)
Space: O(n)

Runtime: 31 ms
Memory: 13.2 MB

This is an approach using the tabluation method, where you pre-allocate
space until the given n's value and calculate bottom-up using values at
array indices.

When F(6), this means we need to calculate from F(0) to F(6) so we allocate
7 slots which is n+1 and prepopulated F(0) and F(1). Starting F(2), we
use the fibonacci rule to populate the numbers until we reach F(n). This way,
we can avoid exponential time, and reduce the complexity to linear time.
------------------------------------------------------------------------
'''
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        
        cache = [0]*(n+1)
        cache[1] = 1
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]

'''
------------------------------------------------------------------------
Solution 3 - Top-Down Approach using Memoization
Time: O(n)
Space: O(n)

Runtime: 23 ms
Memory: 13.6 MB

This approach demonstrates a technique commonly known as memoization.
Memoization is used in recursive functions where it saves results in a
dedicated space (mostly hashmap) in order to avoid duplicate calculations.
This can dramatically reduce the time complexity from O(2^n) to O(n) since
you only need to calculate once for each unique input.
------------------------------------------------------------------------
'''
class Solution(object):
    def fib(self, n):
        cache = {0:0, 1:1}
        
        def calculate(n):
            if n in cache:
                return cache[n]
            
            cache[n] = calculate(n-1) + calculate(n-2)
            return cache[n]
        
        return calculate(n)

'''
------------------------------------------------------------------------
Solution 4 - Bottom-Up Iteration
Time: O(n)
Space: O(1)

Runtime: 18 ms
Memory: 13.8 MB

You'll realize that you don't even have to use O(n) space in order to calculate
the fibonacci number, since the fibonacci number only looks at the past two
numbers F(n-1) and F(n-2).

Thus, if we iteratively save the past two numbers, we're able to calculate
the fibonacci number in O(1) space.
------------------------------------------------------------------------
'''
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        
        current = 0
        prev1 = 0
        prev2 = 1
        
        for i in range(2, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        
        return current