'''
------------------
Difficulty: Easy
------------------

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45
'''

'''
------------------------------------------------------------------------
Solution 1 - Recursion with Memoization
Time: O(n)
Space: O(n)

Runtime: 22 ms
Memory: 13.4 MB

This solution is a good example of using recursion with the memoization technique.
Coming up with the recursive solution is the first step for coming up with
this solution. Regardless of how many steps you have left, you have only
two choices: climb 1 step OR 2 steps.
Therefore, we can use recursion to add up the number of unique paths by
return fn(n-1) + fn(n-2).
Base case would be (1) if n == 0 return 1 (2) if n < 0 return 0, doesn't count as valid path.

However, just with recursion does not fulfill the time constraint of this problem.
Therefore, you need to use the memoization technique with a dictionary.
Every time you proceed with the recursive call, check if unique paths at
n-i has already been calculated, and return if so.
Otherwise, calculate it and memo it.
------------------------------------------------------------------------
'''
class Solution(object):    
    def climbStairs(self, n):
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if memo.get(n):
            return memo.get(n)

        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo.get(n)

'''
------------------------------------------------------------------------
Solution 2 - Dynamic Programming
Time: O(n)
Space: O(n)

Runtime: 11 ms
Memory: 13.3 MB

This solution takes a dynamic programming approach with a slightly tweaked
concept: only ways to reach fn(n) is 1 step from fn(n-1) AND 2 steps from fn(n-2).

Therefore, we can generalize this into:
  - number of unique paths to step n is equivalent to the sum of
    number of unique paths to step n-1 and n-2.

Since the big problem can be broken down into multiple sub-problems, it is
a perfect scenario to use DP. We will memoize throughout the dp process
using a dictionary, returning dp[n] in the end.
------------------------------------------------------------------------
'''
class Solution(object):    
    def climbStairs(self, n):
        dp = {}
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1, 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

'''
------------------------------------------------------------------------
Solution 3 - Fibonacci Number
Time: O(n)
Space: O(1)

Runtime: 28 ms
Memory: 13.3 MB

This is a Fibonacci version of the second solution, which utilizes the
notion that: Fib(n)=Fib(n−1)+Fib(n−2)
------------------------------------------------------------------------
'''
class Solution(object):    
    def climbStairs(self, n):
        
        if n == 1:
            return 1
        
        first = 1
        second = 2
        
        for i in range(3, n+1, 1):
            third = first + second
            first = second
            second = third
        
        return second