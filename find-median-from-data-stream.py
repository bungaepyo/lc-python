'''
------------------
Difficulty: Hard
------------------

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''

'''
------------------------------------------------------------------------
Solution 1 - Simple Sorting
Time: O(nlogn)
Space: O(n)

Runtime: 9394 ms
Memory: 38 MB

This is a sorting solution that does exactly what the problem says.
Since the findMedian() function sorts the array every time it's called,
the time complexity is not the best you can get.
------------------------------------------------------------------------
'''
class MedianFinder(object):

    def __init__(self):
        self.store = []

    def addNum(self, num):
        self.store.append(num)

    def findMedian(self):
        self.store.sort()
        n = len(self.store)
        return self.store[n/2] if n % 2 == 1 else float((self.store[(n/2)-1] + self.store[n/2])*0.5)

'''
------------------------------------------------------------------------
Solution 2 - Two Heaps
Time: O(logn) -> addNum, O(1) -> findMedian
Space: O(n) -> we store all numbers in two heaps

Runtime: 718 ms
Memory: 38.8 MB

This is a solution using two types of heap data structure to find the median.
The intuition is that if we have the following two data structures, we would
be able to easily find median at all times:
  - a data structure that holds smaller half of numbers, and provides easy access to largest
    => this is max-heap

  - a data structure that holds larger half of numbers, and provides easy access to smallest
    => this is min-heap
  
When adding a number,
  - if two heaps have same sizes, we first push it to the max-heap
    and pop the largest one to add it to the min-heap.
  - if two heaps have different sizes, we first push it to the min-heap
    and pop the smallest one to add it to the max-heap.

This way, we can ensure that the numbers are well sorted into halves.

When returning the median,
  - if two heaps have same sizes, we simply subtract top elements from both heaps and divide by 2
    => this is even scenario e.g. [1,2] => 1.5

  - if two heaps have different sizes, we return largest element's top element
    => this is odd scenario e.g. [1,2,3] => 2
    => we do this because we always increase min-heap's size first, guarenteeing
       that min-heap will always have 1 more element when there are odd numbers
------------------------------------------------------------------------
'''
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])