'''
------------------
Difficulty: Easy
------------------

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false 

Constraints:

1 <= n <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1 - Detect Cycles with a HashSet
Time: O(logn) -> finding next value for given number is O(logn), number of digits in a number is given by logn
Space: O(logn) -> related to time complexity, measure of what numbers we're putting in hashset

Runtime: 37 ms
Memory: 13.4 MB

This is a solution using a hashset to track numbers that have been seen before.
It is important to detect numbers that were seen because if the result cannot be
true, it will inevitably be in a cycle as described in the description.
Two things:
  - we must take into consideration that numbers can be 1,2,3 digits.
  - we must note that, if once a number is below 243, it cannot go over it.
------------------------------------------------------------------------
'''
class Solution(object):
    def isHappy(self, n):
        def get_next(n):
            total_sum = 0
            while n > 0:
                remainder = n % 10
                total_sum += remainder**2
                n = n // 10
            return total_sum
        
        seen = set()
        while n != 0 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

'''
------------------------------------------------------------------------
Solution 2 - Floyd's Cycle-Finding Algorithm
Time: O(logn)
Space: O(1)

Runtime: 20 ms
Memory: 13.6 MB

This solution takes a similar approach in terms of calculating the next number,
but optimizes space complexity by not using a hashset. It instead takes a
a two-pointer style approach where there are two runners that can be used
to detect a cycle. Essentially, the fast pointer will reach 1 before meeting
the slow pointer if 1 exists.
------------------------------------------------------------------------
'''
class Solution(object):
    def isHappy(self, n):
        def get_next(n):
            total_sum = 0
            while n > 0:
                remainder = n % 10
                total_sum += remainder**2
                n = n // 10
            return total_sum
        
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1