'''
------------------
Difficulty: Easy
------------------

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
'''

'''
------------------------------------------------------------------------
Solution 1: Heap
Time: O(nlogn + mlogk) -> n as len(nums), m as number of calls to add()
Space: O(n) -> even though we keep the heap size to k, it will initially be
               n right after we heapify and before reduce size to k

Note on time complexity:
  - heapify function can turn nums into a heap in O(n) time. Then, we need to remove
    from the heap until heap size is k, which means removing n-k elements.
    Since k can be a number like 1, each operation costs logn. Thus, nlogn for __init__
  - every call to add() can potentially remove an element from the heap,
    which costs O(logk) time. If we cann add() m times, time complexity is O(mlogk)

Runtime: 101 ms
Memory: 17.9 MB

Using the heap data structure, we are able to easily implement the KthLargest class.
The underlying intuition isn't complicated:
  - we create a min-heap by (1) heapifying nums (2) reducing size (aka popping) until size is k
  - every time we call add(), we heapq.heappush() and pop if length exceeds k.

The heappush operation should rearrange the nodes in the min-heap so that they
fulfill the heap conditions which are: (1) complete binary tree (2) val of each node must be
no greater than the value of its child nodes.
------------------------------------------------------------------------
'''
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]