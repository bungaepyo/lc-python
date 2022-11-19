'''
------------------
Difficulty: Easy
------------------

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1]. 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
'''

'''
------------------------------------------------------------------------
Solution 1: Array & Sorting
Time: O(mn + mlogm) -> for loop with sum() AND the sort() function
Space: O(1) -> in-place and no extra memory

Runtime: 88 ms
Memory: 13.7 MB

This is a solution using in-place array updates and built-in sorting function.
In order to return the indices of the weakest rows at the end, we should be
able to compare two things:
  - (1) whether a row has more soldiers
  - (2) whether a row is weaker/stronger when with same number of soldiers

First comparison is easy to make since we can just compare the sum() of each row,
but it can get kinda tricky with the second comparison. The intuition I used
in this solution is: if you multiply sum(row) by number of rows and add the index,
every row will get a weighted number with which you can simply use to compare
both (1) and (2).

Thus, we update in-place using this intuition, sort it, and % by number of rows
again at the end, we will have indices of rows by weakest order. Simply return [:k] of this.
------------------------------------------------------------------------
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        ROWS = len(mat)
        for idx, row in enumerate(mat):
            mat[idx] = sum(row)*ROWS + idx
        
        mat.sort()
        mat = [val % ROWS for val in mat[:k]]
        
        return mat

'''
------------------------------------------------------------------------
Solution 2: Linear Search and Sorting
Time: O(mn + mlogm)
Space: O(m)

Runtime: 210 ms
Memory: 13.9 MB

This is a solution that utilizes the characteristics of the sort() function.
When told to sort tuples, python firstly sorts on the first element of the tuple
and then breaks any ties by sorting on the second element. Therefore,
if we are able to populate an array of tuples (number of soliders, index),
we would be able to simply sort them and return the index of first k elements.
------------------------------------------------------------------------
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        
        return [i for strengh, i in strengths[:k]]

'''
------------------------------------------------------------------------
Solution 3: Binary Search and Sorting/Map
Time: O(mlogmn) -> mlogn (binary search for m rows) + mlogm (sort function)
Space: O(m)

Runtime: 195 ms
Memory: 13.8 MB

This is a solution that uses the same intuition as solution 2, but uses
binary search to improve on time complexity. For both solution 1 and 2,
we used linear search to find and update the strength of each row. Instead
in this solution, we use binary search to improve time complexity from
O(mn) to O(mlogn).
------------------------------------------------------------------------
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        n = len(mat[0])
        
        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        row_strengths = []
        for i, row in enumerate(mat):
            row_strengths.append((binary_search(row), i))
        
        row_strengths.sort()
        
        return [i for strengh, i in row_strengths[:k]]

'''
------------------------------------------------------------------------
Solution 4: Binary Search and Priority Queue
Time: O(mlognk) -> mlogn (binary search) + mlogk (push m elements to heap size of k)
Space: O(k) -> heap size

Runtime: 122 ms
Memory: 13.8 MB

This solution further improves the space complexity by using a max-heap instead
of an array. When we used the array approach, we would fill in the entire
array and discard n-k amount to get the weakest k. If we use a heap, the size
of the data structre we would be filling in will never exceed k.
------------------------------------------------------------------------
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        #Calculate the strength of each row using binary search
        #Put the strength/index pairs into a priority queue
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)
        
        #Pull out and return the indices of the smallest k entries
        #Don't forget to convert them back to positive numbers
        indices = []
        while pq:
            strengh, i = heapq.heappop(pq)
            indices.append(-i)
            
        return indices[::-1]

'''
------------------------------------------------------------------------
Solution 5: Vertical Iteration
Time: O(mn)
Space: O(1)

Runtime: 91 ms
Memory: 13.7 MB

This is a really smart solution that totally switches the focus to columns
instead of rows. The intuition is: if we find a column element that is a 0
and has 1 left to it, it means we've found the first 0 of that row. If we aggregate
the row index everytime we find this way, we would be able to return the
row indices in order. There are two edge cases:
  - (1) first element is 0 -> we need to check this along with checking left is 1
  - (2) row is full of 1 -> we need to do another iteration filling in indices array
                            until its length reaches k
------------------------------------------------------------------------
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        indices = []
        for c, r in itertools.product(range(n), range(m)):
            if len(indices) == k:
                break
            if mat[r][c] == 0 and (c == 0 or mat[r][c-1] == 1):
                indices.append(r)
                
        #If there aren't enough, it's because some of the first k weakest rows
        #are entirely 1's. We need to include the ones with the lowest indexes
        #until we have at least k.
        i = 0
        while len(indices) < k:
            if mat[i][-1] == 1:
                indices.append(i)
            i += 1
        
        return indices