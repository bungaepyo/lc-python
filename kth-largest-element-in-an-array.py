'''
------------------
Difficulty: Medium
------------------

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity. 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''

'''
------------------------------------------------------------------------
Solution 1: Heap
Time: O(nlogk)
Space: O(k)

Runtime: 1386 ms
Memory: 28.8 MB

The kth largest number problem could be easily solved by using a heap data structure.
Note: it is generally allowed to use built-in data structure libraries as long as you
are able to explain how they work and how they're implemented.

Using a max-heap data structure of size k, healpq.nlargest function iterates through
the input array and keeps "k" largest element in the heap. It constantly
updates the elements in the max-heap to keep elements the largest ones,
therefore doing O(logk) operation n times.
------------------------------------------------------------------------
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

'''
------------------------------------------------------------------------
Solution 2: Quickselect
Time: O(n) -> this is average case, worst case can be O(n^2)
Space: O(1)

Runtime: 782 ms
Memory: 30.2 MB

If you know how the quicksort algorithm works, understanding this quickselect
solution should be intuitive as well. Quicksort is a sorting algorithm
using a random pivot index so that we can achieve average time complexity of O(nlogn).

Basically, quicksort does the following (shown in the partition function below):
  - select a random pivot integer and send it to the end of the array
  - using pointer such as store_index, fill the left side of the array with
    elements strictly smaller than pivot
  - place pivot right after the leftside so that the pivot has only smaller elements
    to the left and greater than or equal to elements to the right.
  - repeat this

In quickselect, we only care about one side of the quicksorted array since we're
only looking for kth largest element in the array. This makes the algorithm's time
complexity to converge to average case of O(n) since we're only looking at one side.

One important intuition we can also use is that kth largest is also (n-k)th smallest.
Thus, we can perform regular quicksort each time we pick a new random pivot,
and do the same thing again for only one side (just like binary search) depending
on whether the element on pivot_index is larget than, smaller than, or equal to (n-k) smallest.
------------------------------------------------------------------------
'''
class Solution:
    def findKthLargest(self, nums, k):
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)