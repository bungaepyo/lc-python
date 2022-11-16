'''
------------------
Difficulty: Easy
------------------

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:

Input: stones = [1]
Output: 1 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1: Heap
Time: O(nlogn) -> removal costs O(logn), we might perform up to (n-1) times
Space: O(1) -> just in python because modifies array in-place. Java costs O(n)
               because it needs to create PriorityQueue

Runtime: 29 ms
Memory: 13.5 MB

This is an intuitive solution using the max-heap data structure. Since we're
playing the stone game with the heaviest two every iteration, we need a
max-heap and will pop twice in each iteration from the max-heap. Depending
on the two stones' weight, we might continue with loop or add subtraction back to the heap.

If the heap has only one stone left, return it's weight. Otherwise, return 0.

Creating a max heap is possible in python by creating a min-heap and multiplying
-1 to all values being added to the heap.
------------------------------------------------------------------------
'''
class Solution(object):
    def lastStoneWeight(self, stones):
        # make a max-heap
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        # while heap size is larger than 1, keep playing the game
        while len(stones) > 1:
            first_stone = -1*heapq.heappop(stones)
            second_stone = -1*heapq.heappop(stones)
            if first_stone == second_stone:
                continue
            else:
                heapq.heappush(stones, -1*(first_stone - second_stone))
        
        # if heap size is 0, return 0. else, return last stone weight
        return -1*stones[0] if stones else 0

'''
------------------------------------------------------------------------
Solution 2: Array (brute-force)
Time: O(n^2) -> index() and max() has O(n) time complexity
Space: O(1)

Runtime: 35 ms
Memory: 13.4 MB

This is a naive array-based brute force solution where it simulates the
problem. While array length is larger than 1, it pops two largest stones
and compares them. Each pop to the largest stone costs O(n).
------------------------------------------------------------------------
'''
class Solution(object):
    def lastStoneWeight(self, stones):
        def remove_largest():
            index_of_largest = stones.index(max(stones))
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()
        
        while len(stones) > 1:
            first_stone = remove_largest()
            second_stone = remove_largest()
            if first_stone != second_stone:
                stones.append(first_stone - second_stone)
        
        return stones[0] if stones else 0

'''
------------------------------------------------------------------------
Solution 3: Counting Sort
Time: O(n + w) -> putting n stones in buckets, worst case iterates through all w (max_weight) indices of buckets
Space: O(w) -> buckets size is max_weight + 1

Runtime: 43 ms
Memory: 13.5 MB

This is a counting sort version of solving this problem.
------------------------------------------------------------------------
'''
class Solution(object):
    def lastStoneWeight(self, stones):
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)
        
        for weight in stones:
            buckets[weight] += 1
        
        biggest_weight = 0
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight