'''
------------------
Difficulty: Medium
------------------

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1] 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap, Counting Sort
Time: O(n)
Space: O(n)

Runtime: 109 ms
Memory: 17.1 MB

This is a pretty intuitive solution using hashmap and counting sort.
The steps are the following:
  - (1) for each num in nums, update hashmap so that key -> number, value -> count
  - (2) initialize a counting sort array (index = count) and update so that numbers are
        allocated to its count's position
  - (3) iterate counting sort array backwards and add everything to result array
  - (4) return res[:k] since we only want top k frequent elements
------------------------------------------------------------------------
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        #put number -> count in hashmap
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        #make a count sort array with k, v enumerate()
        frequency = [0]*(len(nums)+1)
        for num, count in hashmap.items():
            if frequency[count] == 0:
                frequency[count] = [num]
            else:
                frequency[count].append(num)

        #iterate count sort array from the right and add k elements
        res = []
        for i in range(len(frequency)-1, -1, -1):
            if frequency[i] != 0:
                res += frequency[i]
        
        return res[:k]

'''
------------------------------------------------------------------------
Solution 2 - Heap
Time: O(nlogk) -> if k < n and O(n) if k = n
Space: O(n+k) -> hashmap n, heap k

Runtime: 215 ms
Memory: 16.7 MB

This is a solution using a heap data structure. The intuition behind this
solution is the following:
  - build a hashmap that has number -> frequency key value pair
  - build a heap out of the hashmap that can represent k most frequent elements
  - build an output array from the heap
------------------------------------------------------------------------
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        #O(1) time
        if k == len(nums):
            return nums
        
        #build hashmap: char and its frequency
        #O(n) time
        count = Counter(nums)
        
        #build heap of top k frequency elements
        #and convert it into an output array
        # O(nlogk) time
        return heapq.nlargest(k, count.keys(), key=count.get)

'''
------------------------------------------------------------------------
Solution 3 - Quickselect
Time: O(n)
Space: O(n)

Runtime: 77 ms
Memory: 16.5 MB

Core concept of the quickselect algorithm is same as quicksort: one chooses
a pivot and defines its position in a sorted array in a linear time using
a "partition algorithm."
  - (1) choose a pivot, and swap it with the last element
  - (2) store_index = left = 0, and start iterating elements on left.
  - (3) whenever the frequency of left is lower than pivot's frequency, swap
        the element on left with elemen on store_index
  - (4) end the end of this process, swap element on store_index with
        last element, which is the pivot
  - (5) we now have an array where left to pivot are elements that have
        lower frequency than pivot, and right to pivot are those that have
        frequencies greater than or equal to piovot.
If pivot == n - k, nums[pivot:] is the subarray with top k frequent elements.
------------------------------------------------------------------------
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        unique = list(count.keys())
    
        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  

            return store_index

        def quickselect(left, right, k_smallest):
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)     

            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]