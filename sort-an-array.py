'''
------------------
Difficulty: Medium
------------------

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed
(for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique. 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''

'''
------------------------------------------------------------------------
Solution 1: Merge Sort
Time: O(nlogn)
Space: O(n)

Runtime: 2483 ms
Memory: 23.5 MB

This is an implementation of the merge sort algorithm, where you continuously
break down the array until they have single elements, and start merging them
in sorted order. Therefore, it's basically a top -> down -> top procedure.

When we merge the sublists, we essentially compare the head of each sublists
and take pop whichever is smaller and append in the result array. And then,
we extend the result array with whatever subarray is left. Essentially, if
you start doing this from the single-elemented sublists, it is guarenteed
that the sublists that bubble up will already be sorted.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        if n > 1:
            list1 = self.sortArray(nums[:n/2])
            list2 = self.sortArray(nums[n/2:])
            nums = self.merge(list1, list2)
        return nums
    
    def merge(self, list1, list2):
        sorted_list = []
        while list1 and list2:
            if list1[0] <= list2[0]:
                sorted_list.append(list1.pop(0))
            else:
                sorted_list.append(list2.pop(0))
        if not list1:
            sorted_list.extend(list2)
        if not list2:
            sorted_list.extend(list1)
        return sorted_list

'''
------------------------------------------------------------------------
Solution 2: Merge Sort - Classic Template
Time: O(nlogn)
Space: O(n)

Runtime: 2942 ms
Memory: 22.1 MB

This is a more generalized version of the merge sort solution. This basically
does the same thing as solution 1, but elaborates more on the process.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortArray(self, nums):
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.sortArray(L)
            self.sortArray(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1

        return nums

'''
------------------------------------------------------------------------
Solution 2: Quick Sort (TLE)
Time: O(nlogn) -> average case, worst case O(n^2)
Space: O(n)

Note on time complexity: average case is O(nlogn) because, if the pivot
happens to be the mdeian of the list, the list would be divided into two
sublists of equal size. This would be a balanced binary search tree. With
height of logn, each level will be scanned once O(n) due to partitioning.
Worst case is when pivot is an extreme value on the far left or right side.

Runtime: ??? ms
Memory: ??? MB

This is a classic quicksort algorithm implementation. Quicksort basically
uses a pivot to divide the array into two partitions:
  - left side should only have smaller elements
  - right side should only have larger elements

(1) we choose a pivot and get it out of the way by swapping with last element
(2) with two pointers, we swap when we find smaller (than pivot) elements located at
    the right of larger (than pivot) elements.
(3) we swap back the pivot to its correct position, which is saved by the
    slower pointer

This results in a partitioned array that has a pivot with smaller elements
on its left, and larger elements on its right. Since we return the pivot
index, we can recursively call quicksort(low, pivot-1) and quicksort(pivot+1, high)
so that the sublists are also sorted in the end result.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortArray(self, nums):
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, low, high):
        if low < high:
            partition = self.partition(nums, low, high)
            self.quicksort(nums, low, partition-1)
            self.quicksort(nums, partition+1, high)
    
    def partition(self, nums, low, high):
        mid = low+(high-low)//2
        nums[mid], nums[high] = nums[high], nums[mid]
        pivot = nums[high]
        
        i = low
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[high] = nums[high], nums[i]
        return i