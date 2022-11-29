'''
------------------
Difficulty: Easy
------------------

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 29 ms
Memory: 13.2 MB

This problem can be solved by this really basic binary search solution.
Since the integers are already sorted, and it's guaranteed that a number
will be chosen between 1 and n, we can go ahead and implement a classic
binary search algorithm.

While left <= right, we use the given guess(int num) API function to compare
the mid with the target.
------------------------------------------------------------------------
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n
        
        while left <= right:
            mid = left + (right-left)/2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        return right