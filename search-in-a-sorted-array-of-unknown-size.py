'''
------------------
Difficulty: Medium
------------------

This is an interactive problem.

You have a sorted array of unique elements and an unknown size.
You do not have an access to the array but you can use the ArrayReader interface to access it.
You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.

Example 2:

Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1. 

Constraints:

1 <= secret.length <= 104
-104 <= secret[i], target <= 104
secret is sorted in a strictly increasing order.
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logt) -> t is the index of target value
Space: O(1)

Runtime: 32 ms
Memory: 14.3 MB

This is a binary search solution that achieves the O(logn) time complexity goal.
The problem has a tweak to classic binary search problems in that we do not
know the size of the input array. Therefore, the key here is to realize
that there are two sub-problems we need to tackle:
  - (1) define search space
  - (2) perform binary search to look for target

The second sub-problem is a textbook binary search algorithm, so the first
sub-problem is the one we should focus on. Assuming we have left and right pointers,
the first thing that should come to mind is the fact that we should be increasing
the right pointer until its bigger than target (so target is included in search space).

Then, how should we increase the right pointer?
  - Since we are aiming for a O(logn) algorithm with log base of 2, we should be
    multiplying right by 2 every time we increase
  - Whenever the right pointer increases, this means that the previous value
    was smaller than target. Therefore, it is safe to update left to right's
    previous value in order to optimize search space. (line 83)
------------------------------------------------------------------------
'''
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
class Solution(object):
    def search(self, reader, target):
        #define search space: left and right
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
        
        #perform binary search within that search space
        while left <= right:
            mid = left + (right-left)/2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid-1
            else:
                left = mid+1

        return -1