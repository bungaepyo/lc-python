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

'''
------------------------------------------------------------------------
Solution 2: Binary Search Tree
Time: O(h), both insertion and search
Space: O(n)

Runtime: ? ms
Memory: ? MB

This is a solution using the binary search tree data strcuture. The reason
we use a binary search tree is because both insertion and search can be
done in O(h) time. The underlying intuition is the following:
  - if we add all the elements into a binary search and keep track of
    how many nodes are in the subtree starting with itself, we're able
    to more efficiently get the kth largest element.
  - first, we're looking for a node whose right tree size + 1 == k.
    thus, this should be the base case of recursion.
  - if the right subtree size is bigger than k, it means the target
    node is further down the right subtree. do the recursion.
  - otherwise, you need to keep looking on the left subtree. however,
    note that you need to use "k - (right subtree size) - 1" for k as
    that is the remaining number of steps we should take further down the left side.
------------------------------------------------------------------------
'''
class TreeNode(object):
    def __init__(self, val, count):
        self.left = None
        self.right = None
        self.val = val
        self.count = count

class KthLargest(object):

    def __init__(self, k, nums):
        self.root = None
        for num in nums:
            root = self.addToBST(self.root, num)
        self.k = k

    def add(self, val):
        self.addToBST(self.root, val)
        return self.searchKth(self.root, self.k)
    
    def searchKth(self, root, k):
        rightSize = root.right.count if root.right else 0
        if k == rightSize+1:
            return root.val
        if k <= rightSize:
            return self.searchKth(root.right, k)
        else:
            return self.searchKth(root.left, k-m-1)
    
    def addToBST(self, root, val):
        if not root:
            return TreeNode(val, 1)
        
        if root.val < val:
            root.right = self.addToBST(root.right, val)
        else:
            root.left = self.addToBST(root.left, val)
        root.count += 1
        return root

