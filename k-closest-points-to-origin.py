'''
------------------
Difficulty: Medium
------------------

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in). 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted. 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
'''

'''
------------------------------------------------------------------------
Solution 1 - Min-Heap
Time: O(nlogn)
Space: O(n)

Runtime: 701 ms
Memory: 19.9 MB

This is a straightforward solution using the min-heap data structure.
The key here is to realize that you need to put triplets (or embedded tuple) to
the min-heap. This is because, while pushing the points into the min heap,
there are two things that we want to achieve:
  - (1) sort the points by their distance
  - (2) retrieve their coorinates while popping them from heap

Thus, we push (distance, corrdinate) to the min heap so that they are
sorted by distance, and pop k times so we can get a list of k points
that are closest to the origin (least distance).
------------------------------------------------------------------------
'''
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        
        for point in points:
            dist = sqrt((point[0])**2+(point[1])**2)
            element = (dist, point)
            heapq.heappush(heap, element)
        
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res

'''
------------------------------------------------------------------------
Solution 2 - Max-Heap
Time: O(nlogn)
Space: O(n)

Runtime: 635 ms
Memory: 20.5 MB

This is a max-heap version of solution 1, which is more concise.
------------------------------------------------------------------------
'''
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

'''
------------------------------------------------------------------------
Solution 3 - Sort
Time: O(nlogn)
Space: O(n)

Runtime: 620 ms
Memory: 19.5 MB

This is a simple solution using a built in sort() function. The sort()
function allows custom sorting logic using lambda, so we are able to
sort the points by P[0]**2 + P[1]**2, which is the square of distance.
------------------------------------------------------------------------
'''
class Solution(object):
    def kClosest(self, points, k):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]

'''
------------------------------------------------------------------------
Solution 4 - Divide and Conquer (Quickselect)
Time: O(n) -> this is average case, worst case can be O(n^2)
Space: O(n)

Runtime: ? ms
Memory: ? MB

This is a solution using the quickselect algorithm. Basically, you choose
a random pivot and partition both sides of the pivot until you reach the
point k. After partitioning on k, anything left to the pivot will be
k closest points to origin.
------------------------------------------------------------------------
'''
class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]