'''
------------------
Difficulty: Medium
------------------

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

Input: matrix = [[-5]], k = 1
Output: -5 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity?
The solution may be too advanced for an interview but you may find reading this paper fun.
'''

'''
------------------------------------------------------------------------
Solution 1: Min-heap
Time: O(x + klogx) -> x = min(n, k), heap construction O(x), k times operation O(logx)
Space: O(x)

Runtime: 203 ms
Memory: 17.6 MB

This is a min-heap approach that essentially uses the nodes in the heap as
pointers. First, we consider min(n,k) rows and add all its first cells to the heap
in order to use them as pointers. By pointers, I mean using them to note until which
cell in each row we've advanced.

This is important because:
  - (1) we need to know row & col index in order to return kth smallest element
  - (2) we should be able to compare the largest of each row to smallest of next row

This this is a min-heap, every element popped from it will be the smallest
element in the heap, accomplishing (2). If we keep popping from heap k times,
kth element popped will be kth smallest element no matter what we added to the heap,
since every time an element is added it will be allocated a space where it belongs.
------------------------------------------------------------------------
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        N = len(matrix)
        
        minHeap = []
        for r in range(min(k, N)):
            #add triplets of information for each first cell of row
            #we're going to use these as pointers
            minHeap.append((matrix[r][0], r, 0))
        
        heapq.heapify(minHeap)
        
        while k:
            element, r, c = heapq.heappop(minHeap)
            
            #if we have any new elements in the current row, add them
            if c < N-1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            
            k -= 1
        
        return element

'''
------------------------------------------------------------------------
Solution 2: Binary Search
Time: O(nlog(max-min))
Space: O(1)

Runtime: 139 ms
Memory: 17.4 MB

This is a complex way of using binary search in a (row, col) sorted matrix.
The way we use binary search in a sorted matrix is the following:
  - we knoe top left corner has smallest element, bottom right corner has biggest element
  - using this number range (note this is not index range), we calculate temporary mid number
  - using this mid number, we try to figure out how many elements in the matrix are
    smaller than the mid number (since problem asked kth smallest)
  - if number of elements left to mid number is equal to k, we've found our value.
    - if larger/smaller, update the boundaries until left side size is equal to k
------------------------------------------------------------------------
'''
class Solution:    
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1
        return count, smaller, larger
    
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower
        return start