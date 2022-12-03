'''
------------------
Difficulty: Medium
------------------

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4] 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''

'''
------------------------------------------------------------------------
Solution 1 - Sort With Custom Comparator
Time: O(nlogn + klogk) -> because of 2 sorted() functions
Space: O(n)

Runtime: 601 ms
Memory: 15.3 MB

This is the most intuitive, but least efficient solution we can come up with.
We first sort the input array based on the distance to x. This is not necessarily
sorted in ascending order, so we need to sort the subarray sorted_arr[:k] once again.

e.g. [-1,0,1,2,3], k = 3, x = 4
     array sorted by distance to x will be [3,2,1,0,-1]
------------------------------------------------------------------------
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        sorted_arr = sorted(arr, key = lambda num: abs(x-num))
        return sorted(sorted_arr[:k])

'''
------------------------------------------------------------------------
Solution 2 - Binary Search + Sliding Window
Time: O(logn + k)
Space: O(1)

Runtime: 323 ms
Memory: 14.9 MB

This is a solution using the combination of binary search and sliding window.
Since the input array is sorted, it gives us an advantage for finding an
element in the array by allowing binary search.
The element we need to find by using binary search is the target (x) or
where the target would have been if it was in the array (-1 of nearest greater element).

Once we find the index using binary search, we need to define the bounaries for
our sliding window. Remember these two things:
  - since x is not an element in arr, the initial size of the window needs to be 0
  - therefore, left and right should always be pointing at candidates

While the window size is less than k, we expand the boundaries either to
left and right while taking care of left and right going out of bounds.
------------------------------------------------------------------------
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = self.findIndex(arr, x) - 1
        # we can also use the bisect module
        # left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        # actual bounds are (L+1) and (H-1) => (H-1)-(L+1)+1
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]
    
    def findIndex(self, arr, x):
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = left + (right-left)/2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                right = mid-1
            else:
                left = mid+1

        return left

'''
------------------------------------------------------------------------
Solution 3 - Binary Search To Find The Left Bound
Time: O(log(n-k)+k) -> O(log(n-k)) from binary search, O(k) from building the result
Space: O(1)

Runtime: 554 ms
Memory: 15.2 MB

This is a pretty complicated binary search solution that tries to find what
the biggest index of left bound could be. If we find the biggest index of left bound,
we can simply return k elements starting from that index, since array is sorted.

Key intuition here are:
  - set right boundary to len(arr)-k as we are finding the leftmost index boundary
  - if midpoint of arr[mid] and arr[mid+k] is smaller than x, that basically means
    anything from arr[mid] to left of it will not be in the final solution.
    Vice versa with the opposite condition.
------------------------------------------------------------------------
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr)-k
        
        while left < right:
            mid = left+(right-left)/2
            if x > (arr[mid+k]+arr[mid])//2:
                left = mid+1
            else:
                right = mid
        
        return arr[left:left+k]