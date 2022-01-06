'''
------------------
Difficulty: Hard
------------------

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

# ------------------------
# Solution 1 - iteration to find perfect (i)
# Time: O(log(min(m,n)))
# Space: O(1)
# ------------------------
'''
Nice solution from: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation

Runtime: 76 ms
Memory: 13.7 MB
-------------------
#1 BACKGROUND
-------------------
The reason this problem's difficulty is hard is because the time complexity is limited to O(log(m+n)), meaning you shouldn't use sort function.
The first and most important thing to clarify here is the definition of a median: "dividing a set into two equal length subsets, where one subset is always greater (numerically) than the other."

Assuming:
  - Two sorted arrays A and B
  - A has m elements => i = 0 ~ m
  - B has n elements => j = 0 ~ n
  - Divide the two arrays into left_part and right_part such that:

          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

-------------------
#2 EXPLANATION
-------------------
This definition of a median can be transformed into meeting these two conditions:
  1) len(left_part) == len(right_part)
  2) max(left_part) <= min(right_part)

  => Thus: median = (max(left_part) + min(right_part))/2.

To ensure the two conditions, we need to ensure:
  (1) i + j == m - i + n - j (or: m - i + n - j + 1)
      if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
      
       --------------------------------------------------------------------
      | Why n >= m? Because I have to make sure j is non-nagative          |
      | since 0 <= i <= m and j = (m + n + 1)/2 - i.                       |
      | If n < m , then j may be nagative, that will lead to wrong result. |
       --------------------------------------------------------------------

  (2) B[j-1] <= A[i] and A[i-1] <= B[j]

Thus, as of now, all we need to do is:
  Searching i in [0, m], to find an object `i` that:
    B[j-1] <= A[i] and A[i-1] <= B[j], where j = (m + n + 1)/2 - i

Thus, median would be
  (1) when m+n is odd => max(A[i-1], B[j-1])
  (2) when m+n is even => (max(A[i-1], B[j-1]) + min(A[i], B[j]))/2

-------------------
#3 EDGE CASE
-------------------
The edge cases that this problem has are: i=0, i=m, j=0, j=n where A[i-1], B[j-1], A[i], B[j] may not exist.
In these cases, just know that we just need to ensure max(left_part) <= min(right_part). 
If some of A[i-1], B[j-1], A[i], B[j] don't exist, then we just don't need to check one(or both) of these two conditions in (2). 
For example, if i=0, then A[i-1] doesn't exist, then we don't need to check A[i-1] <= B[j]. So, what we need to do is:

Thus, the solution would change to:
  Searching i in [0, m], to find an object `i` that:
    (j == 0 or i == m or B[j-1] <= A[i]) and
    (i == 0 or j == n or A[i-1] <= B[j])
    where j = (m + n + 1)/2 - i

Where we would encounter 3 scenarios:
  <a> (j == 0 or i == m or B[j-1] <= A[i]) and
      (i == 0 or j = n or A[i-1] <= B[j])
      Means i is perfect, we can stop searching.

  <b> j > 0 and i < m and B[j - 1] > A[i]
      Means i is too small, we must increase it.

  <c> i > 0 and j < n and A[i - 1] > B[j]
      Means i is too big, we must decrease it.

We don't need to check whether j > 0 and whether j < n because i < m ==> j > 0 and i > 0 ==> j < n.

-------------------
#4 BOILERPLATE CODE
-------------------
<1> Set imin = 0, imax = m, then start searching in [imin, imax]

<2> Set i = (imin + imax)/2, j = (m + n + 1)/2 - i

<3> Now we have len(left_part)==len(right_part). And there are only 3 situations
     that we may encounter:
    <a> B[j-1] <= A[i] and A[i-1] <= B[j]
        Means we have found the object `i`, so stop searching.
    <b> B[j-1] > A[i]
        Means A[i] is too small. We must `ajust` i to get `B[j-1] <= A[i]`.
        Can we `increase` i?
            Yes. Because when i is increased, j will be decreased.
            So B[j-1] is decreased and A[i] is increased, and `B[j-1] <= A[i]` may
            be satisfied.
        Can we `decrease` i?
            `No!` Because when i is decreased, j will be increased.
            So B[j-1] is increased and A[i] is decreased, and B[j-1] <= A[i] will
            be never satisfied.
        So we must `increase` i. That is, we must ajust the searching range to
        [i+1, imax]. So, set imin = i+1, and goto <2>.
    <c> A[i-1] > B[j]
        Means A[i-1] is too big. And we must `decrease` i to get `A[i-1]<=B[j]`.
        That is, we must ajust the searching range to [imin, i-1].
        So, set imax = i-1, and goto <2>.
'''
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
        