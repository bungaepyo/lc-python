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

'''
------------------------------------------------------------------------
Solution 1 - iteration to find perfect (i)
Time: O(log(min(m,n)))
Space: O(1)

Runtime: 76 ms
Memory: 13.7 MB

Nice solution from: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
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
------------------------------------------------------------------------
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
        
'''
------------------------------------------------------------------------
Solution 2 - Binary Search
Time: O(log(m+n))
Space: O(1)

Runtime: 91 ms
Memory: 13.8 MB

Solution from: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation

-------------------
#1 BACKGROUND
-------------------

(1) First of all, in order to understand this solution, we need to see the concept
"MEDIAN" in a slightly unconventional way:
  - If we cut the sorted array in two halves of equal length, then the median
    is the average of max(lower_half) and min(upper_half), which are
    the two numbers immediately next to the cut.
  - For example,
    - [2 3 5 7] -> [2 3 / 5 7] -> median is (3+5)/2 = 4
    - [2 3 4 5 6] -> [2 3 (4/4) 5 6] -> median is (4+4)/2 = 4

(2) Second of all, index of L (left of cut) and R (right of cut) has the
following relationship:
  - L = (N-1)/2, R = N/2
  - For example,
      N   L / R (Index)
      1   0 / 0
      2   0 / 1
      3   1 / 1  
      4   1 / 2      
      5   2 / 2
      6   2 / 3
      7   3 / 3
      8   3 / 4
  - Thus, we can conclude that the median is the following:
    - (L+R)/2 = (A[(N-1)/2] + A[N/2])/2

(3) Lastly, in a single array setting, we need to understand the concept of
"imaginary positions" between numbers in order to know where the cut should be located.
  - If we add possible cut "positions" represented as "#" between numbers:
    - (Example 1) [6 9 13 18]  ->   [# 6 # 9 # 13 # 18 #]    (N = 4)
                  position index     0 1 2 3 4 5  6 7  8     (N_Position = 9)
    - (Example 2) [6 9 11 13 18]->   [# 6 # 9 # 11 # 13 # 18 #]   (N = 5)
                  position index      0 1 2 3 4 5  6 7  8 9 10    (N_Position = 11)
  - We need to notice that there are always exactly 2N+1 positions regardless of N.
    - Thus, middle cut should always be located at Nth position (0-indexed)
    - Hence,
      - L = (N-1)/2 => (CutPosition-1)/2
      - R = N/2     => CurPosition/2

-------------------
#2 EXPLANATION
-------------------

The intuition for the two-array case is similar:
  - We need to find a cut that divides the two arrays so that any number in the
    left two halves <= any number in the right two halves

There are three observations here:
  - (1) There are 2N1+2N2+2 positions altogether. Therfore, there must be N1+N2
        positions on each side of the cut, and 2 positions directly on the cut.
  - (2) Thus, once we have a cut position on one array, the other array's cut position is auto-decided.
        Say C2 = k in A2, then the cut position on A1 should be N1+N2-k.
        For instance, C2 = 2, then C1 = 4+5-C2 = 7
          [# 1 # 2 # 3 # (4/4) # 5 #]
          [# 1 / 1 # 1 # 1 #]
  - (3) When the cuts are made, we would have two L's and two R's:
        L1 = A1[(C1-1)/2]
        R1 = A1[C1/2];
        L2 = A2[(C2-1)/2]
        R2 = A2[C2/2];

How do we decide if the cut is the cut we want?
  - According to the intuition, we only need to make sure that "any number in the
    left two halves <= any number in the right two halves"
  - L1 <= R1 && L1 <= R2 && L2 <= R1 && L2 <= R2
  - L1 <= R1 and L2 <= R2 is guarenteed, so L1 <= R2 && L2 <= R1

Using these conditions, we can perform a binary search where
  - If L1 > R2, it means that there are too many large numbers on the left half of A1.
    We need to move L1 to the left, which means L2 to the right.
  - If L2 > R1, it means that there are too many large numbers on the left half of A2.
    We need to move L2 to the left, with means L1 to the right.
  - If we find the right cut, return (max(L1, L2) + min(R1, R2)) / 2.0

Note: although the two cut positions are dependent on each other, it is more practical to
      move the shorter array's cut. This is because while shorter array's positions are
      all possible cut positions, some of the longer array's positions might not be eligible.
      (e.g.) [1] [2,3,4,5,6,7,8,9]

-------------------
#3 EDGE CASE
-------------------

The only edge case in this problem is when the cut falls on the first (0) or last (2N) position.
For example, if C2 = 2N, R2 = A[2*N2/2] = A[N2] => this is out of range since 0-indexed.
In order to cover this edge case, we're going to
  - assign INT_MIN when cut is 0
  - assign INT_MAX when cut is 2N

------------------------------------------------------------------------
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        
        # Make sure A2 is the shorter one.
        if n1 < n2: return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, 2 * n2
        
        while left <= right:
            mid2 = left + (right - left) # Try Cut 2 
            mid1 = n1 + n2 - mid2        # Calculate Cut 1 accordingly
            
            # Get L1, R1, L2, R2 respectively
            L1 = float('-inf') if mid1 == 0 else nums1[(mid1-1) // 2]
            L2 = float('-inf') if mid2 == 0 else nums2[(mid2-1) // 2]
            R1 = float('inf') if mid1 == n1*2 else nums1[mid1 // 2]
            R2 = float('inf') if mid2 == n2*2 else nums2[mid2 // 2]
            
            if L1 > R2:
                # A1's lower half is too big; need to move C1 left (C2 right)
                left = mid2 + 1
            elif L2 > R1:
                # A2's lower half too big; need to move C2 left.
                right = mid2 - 1
            else:
                # Otherwise, that's the right cut.
                return (max(L1, L2) + min(R1, R2)) / 2.0