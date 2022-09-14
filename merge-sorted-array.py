'''
------------------
Difficulty: Easy
------------------

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
'''

'''
------------------------------------------------------------------------
Solution 1: Three Pointers (Start from End)
Time: O(m+n)
Space: O(1)

Runtime: 19 ms
Memory: 13.5 MB

This is a m+n solution using the three pointer approach. Since we are updaing
nums1 array in-place to achieve the merge of two arrays, we cannot iterate
from the front since it will mess up with the indices. Hence, it is a better
approach to make:
  (1) first pointer at the very last index of nums1 to handle additions (m+n-1)
  (2) second pointer at the last index of non-zero element of nums1 (m-1)
  (3) third pointer at the last index of non-zero element of nums2 (n-1)

The base idea is to compare second & third pointer, update the first pointer
depending on which one is bigger, and decreasing pointers accordingly.

One thing to note:
  - since we are updating nums1 in place, we cannot end the iteration even
    if second pointer is lower than 0. We should continue updating nums1
    until either addPointer or nPointer is lower than 0 as well.
------------------------------------------------------------------------
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        mPointer = m-1
        nPointer = n-1
        addPointer = m+n-1

        while addPointer >= 0 and nPointer >= 0:
            if mPointer < 0:
                nums1[addPointer] = nums2[nPointer]
                nPointer -= 1
                addPointer -= 1
            elif nums2[nPointer] >= nums1[mPointer]:
                nums1[addPointer] = nums2[nPointer]
                nPointer -= 1
                addPointer -= 1
            else:
                nums1[addPointer] = nums1[mPointer]
                mPointer -= 1
                addPointer -= 1

'''
------------------------------------------------------------------------
Solution 2: Three Pointers (Start from Beginning)
Time: O(m+n)
Space: O(m)

Runtime: 21 ms
Memory: 13.5 MB

This is a solution using the three pointer approach, but starting from the
beginning. Therefore, its space complexity is slightly worse since it uses a
copy of nums1 for the comparison.
------------------------------------------------------------------------
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

'''
------------------------------------------------------------------------
Solution 3: Three Pointers (Start from End, Shorter)
Time: O(m+n)
Space: O(1)

Runtime: 24 ms
Memory: 13.5 MB

This is a three pointers solution just like solution #1,
but in a slightly shorter form. It also uses a for loop instead of a while loop.
------------------------------------------------------------------------
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
