'''
------------------
Difficulty: Easy
------------------

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1
 
Constraints:

1 <= bad <= n <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 7 ms
Memory: 13.3 MB

This is a simple binary search solution with a small tweak to the classic approach.
While shrinking the search space using left and right variables, there could
be two scenarios with the computed mid.
  - (1) isBadVersion(mid) == False -> we know that anything from mid to the left won't be first bad version.
        Thus, we need to update left = mid + 1
  - (2) isBadVersion(mid) == True -> we know that anything from mid to the right will be bad version.
        However, we still don't know whether mid is first bad version. 
        Therefore, we need to update right = mid so that mid is still included in search space.

If we take this approach, we need to keep the terminating condition to be left = right
until we have only one element left, which is guarenteed. This algorithm will
eventually shink the search space to 1 element -> test it with n = 2.
------------------------------------------------------------------------
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = left + (right-left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        
        return left

'''
------------------------------------------------------------------------
Solution 2 - Binary Search (alternate)
Time: O(logn)
Space: O(1)

Runtime: 18 ms
Memory: 13.3 MB

This is an alternate version of the binary search solution.
------------------------------------------------------------------------
'''
class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left <= right:
            mid = left + (right-left)/2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1