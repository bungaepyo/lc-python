'''
------------------
Difficulty: Easy
------------------

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false 

Constraints:

1 <= num <= 2^31 - 1
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 20 ms
Memory: 13.3 MB

This problem can be solved using the binary search algorithm because,
given that the input num is a positive integer, it's essentially searching
for a target where target*target = num in a sorted integer array.

There is one intuition that will make your life easier:
  - for any number > 1 (since 1*1 = 1), the square root A is always less
    than num/2 and greate than 1. e.g. 4 -> 2, 9 -> 3, 16 -> 4, etc.

Thus, we can implement this down into a binary search algorithm where
initial search space is 2, num//2.
------------------------------------------------------------------------
'''
class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        
        left, right = 2, num//2
        
        while left <= right:
            mid = left + (right-left)//2
            square = mid*mid
            if square == num:
                return True
            elif square > num:
                right = mid-1
            else:
                left = mid+1
        
        return False

'''
------------------------------------------------------------------------
Solution 2 - Newton's Method
Time: O(logn)
Space: O(1)

Runtime: 32 ms
Memory: 13.1 MB

This is a solution that is based on Newton's mathematical proof that can
be seen at https://leetcode.com/problems/valid-perfect-square/solution/
------------------------------------------------------------------------
''' 
class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        
        x = num // 2
        while x*x > num:
            x = (x + num // x) // 2
        return x*x == num