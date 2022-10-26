'''
------------------
Difficulty: Medium
------------------

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
t is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9. 

Constraints:

1 <= n <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Brute Force Enumeration - Exceeds Time Limit
Time: O(?)
Space: O(?)

Runtime: ? ms
Memory: ? MB

This is a brute force solution that computes all possible combinations of
square numbers that add up to n, and returns the least number of steps.

Base idea: numSquares(n) = min(numSquares(n-k)+1), where k is a perfect square number

The way we compute all the square numbers <= n is [i**2 for i in range(1, int(math.sqrt(n))+1)].
N itself is the boundary for the square numbers <= n in case itself is a perfect square number.

Base case is when n is in square_nums, which means there is no further
iteration needed since we're trying to get the minimum number of steps.

Then, for all the perfect square numbers that are smaller than n, we compute
the minimum number of steps of (n - square). If we add 1 to it, it's the
minimum steps required at the current level in the recursive stack.
We update the min_num if this value is lower than that.
------------------------------------------------------------------------
'''
class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        
        def minNumSquares(n):
            # bottom cases: find a square number
            if n in square_nums:
                return 1
            min_num = float('inf')
            
            # find the minimal value among all possible solutions
            for square in square_nums:
                if n < square:
                    break
                new_num = minNumSquares(n-square) + 1
                min_num = min(min_num, new_num)
            return min_num
        
        return minNumSquares(n)

'''
------------------------------------------------------------------------
Solution 2: Dynamic Programming
Time: O(n*sqrt(n)) -> outer loop is n, inner loop is sqrt(n)
Space: O(n) -> keep all intermediate subsolutions in dp[]

Runtime: 2696 ms
Memory: 13.7 MB

This is a dynamic programming solution, which has a similar structure to the
fibonacci problem.

The reason the brute force recursive solution was causing a stack overflow issue
was because we were re-calculating the sub-solutions over and over again.
Therefore, we can use a dynamic programming approach to optimize this.

The most important thing to realize here is that, given the problem conditions,
n's minimum number of steps is actually (min number of steps of n - k) + 1 where
k is a square number smaller than n.
For example, 13's min number of steps is:
  - (min number of steps of 13 - 9) + 1
  - (min number of steps of 4) + 1 => 2, since 4 is a perfect square number.

Thus, if we create a dp array of length n+1 and pre-populate dp[0] = 0,
we would be able to fill in all the blanks in dp array.
Then, we simply return last element.
------------------------------------------------------------------------
'''
class Solution(object):
    def numSquares(self, n):
        square_nums = [i*i for i in range(0,int(math.sqrt(n))+1)]
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        
        return dp[-1]

'''
------------------------------------------------------------------------
Solution 3: Greedy Enumeration
Time: O(n^(h/2)) -> h is the max number of recursion that could happen
Space: O(sqrt(n)) -> square_nums size is sqrt(n)

Note on time complexity:
  - As one might notice, the above formula actually resembles the formula to
    calculate the number of nodes in a complete N-ary tree.
    Indeed, the trace of recursive calls in the algorithm form a N-ary tree,
    where N is the number of squares in square_nums, i.e. sqrt(n).
    In the worst case, we might have to traverse the entire tree to find the solution.

Runtime: 131 ms
Memory: 13.9 MB

This is a greedy recursive solution that uses this intuition:
  - starting from the combination of one single number to multiple numbers,
    once we find a combination that can sum up to the given number n,
    then we can say that we must have found the smallest combination,
    since we enumerate the combinations greedily from small to large.

Basically, since we're starting with the smallest count of numbers (1) that
may sum up to n, if we find a count that returns True, it is guaranteed that
it will be the smallest count.
------------------------------------------------------------------------
'''
class Solution(object):
    def numSquares(self, n):
        square_nums = [i*i for i in range(1, int(math.sqrt(n))+1)]
        
        def is_divided_by(n, count):
            """
            return true if "n" can be decomposed into "count" number of perfect square numbers.
            e.g. n=12, count=3:  true.
                 n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n-k, count-1):
                    return True
            return False
        
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count

'''
------------------------------------------------------------------------
Solution 4: Greedy + BFS
Time: O(n^(h/2)) -> h is height of n-ary tree
Space: O(sqrt(n)^h) -> max number of nodes that can appear at level h (next_queue)

Runtime: 317 ms
Memory: 14.5 MB

For each level (equivalent to count in solution 3), we are going to
check all the elements in the queue (remainders, namely n-k) and see if they
are square numbers.

If an element is a square number, it means that we do not have to proceed
any further with the BFS because our goal was to find the min number of
perfect square numbers that add up to n.
Otherwise (as long as sq num is lower than element), we add element - num
to the queue so that we can process it in the next level.
------------------------------------------------------------------------
'''
class Solution(object):
    def numSquares(self, n):
        square_nums = [i*i for i in range(1, int(math.sqrt(n))+1)]
        
        level = 0
        queue = {n}
        #! Important: use set() instead of list() to eliminate the redundancy,
        # which would even provide a 5-times speedup, 200ms vs. 1000ms.
        while queue:
            level += 1
            #construct the queue for next level
            next_queue = set()
            
            for remainder in queue:
                for num in square_nums:
                    if remainder == num:
                        return level
                    elif remainder < num:
                        break
                    else:
                        next_queue.add(remainder - num)
            queue = next_queue
        return level