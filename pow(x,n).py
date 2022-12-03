'''
------------------
Difficulty: Medium
------------------

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Simple recursion (Time Limit Exceeded)
Time: O(N)
Space: O(1)

Runtime: Exceeded ms
Memory: ? MB

This is a simple recursive solution that exceeds time limit, but is worth
starting with. This solution will pass for cases where it has lower depths.
Key math concept to note is:
  - pow(2,0) => 1
  - pow(2,1) => 2
  - pow(2,2) => 2*2
  - pow(2,-1) => 1/2
  - pow(2,-2) => (1/2)*(1/2)
First, adjust the negative powers to the positive integer logic by x = 1/x
and n = -1*n. This will only run once in the recursion.
Second, account for the edge case in which it's always 1 when n is 0.
Then, figure out what the base case for the recursion is. In this case, it's
when n == 1 since we're going to be multiplying additional x until n shrinks to 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -1*n
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x*self.myPow(x, n-1)

'''
------------------------------------------------------------------------
Solution 2: Brute Force (Time Limit Exceeded)
Time: O(N)
Space: O(1)

Runtime: Exeeded ms
Memory: ? MB

This is an iterative brute force approach with similar logic to solution 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -1*n
        res = 1
        for _ in range(n):
            res *= x
        return res

'''
------------------------------------------------------------------------
Solution 3: Fast Power Algorithm Recursive
Time: O(logN) -> each time we apply the formula (x^n)^2 => (x^2)^n, n is reduced by half.
Space: O(logN) -> for each computation, we need to store result of x^(n/2). we do this logN times.

Runtime: 28 ms
Memory: 13.3 MB

This solution is commonly referred to as the "Fast Power", and we use it to get logN time complexity.
The core of this fast power solution is using this exponential formula:
  - (x^n)^2 => x^(2*n)
The strength of this formula is that, assuming we get x^(n/2), we can get x^n with only one computation.
We only need to take care of the cases where the computation varies slightly
depending on n being odd or even.
Since we are passing (n//2) to a recursive call to calculate the half,
we should return half*half*x when n % 2 is not 0.
Otherwise, just return half*half, and base case is n == 0, return 1.0.
------------------------------------------------------------------------
'''
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -1*n

        return self.fastPow(x, n)
    
    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fastPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half*half*x

'''
------------------------------------------------------------------------
Solution 4: Fast Power Algorithm Iterative
Time: O(logN) -> For each bit of n's binary representation, we will at most multiply once.
Space: O(1) -> we only need ans and curr_product

Runtime: 28 ms
Memory: 13.5 MB

This is the iterative version of solution 3, with improved space complexity.
Using essentially the same concept, this solution makes curr_product as twice as big
until it reaches a scenario where i%2 == 1, and multiplies ans with curr_product.
Since the step of while loop is i // 2, both even and odd integers will have to
eventually face i%2 == 1.
  - Even: 2 // 2 = 1
  - Odd: 3 // 2 = 1 OR 5 // 2 = 3, 2 // 2 = 1

We can also come up with a binary interpretation of this solution.
Assuming (i, i2, i3, i4 ... ) is the binary representation of n, for the Nth bit (iN),
it needs to be multiplied by x^(2^N).
------------------------------------------------------------------------
'''
class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -1*n
        
        ans = 1
        curr_product = x
        i = n
        while i > 0:
            if(i%2 == 1):
                ans *= curr_product
            curr_product *= curr_product
            i = i // 2
        return ans