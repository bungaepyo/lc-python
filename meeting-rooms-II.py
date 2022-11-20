'''
------------------
Difficulty: Medium
------------------

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.
 
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1 

Constraints:

1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
'''

'''
------------------------------------------------------------------------
Solution 1: Min-Heap
Time: O(nlogn) -> sorting is O(nlogn), for loop & heap operation is O(nlogn)
Space: O(n)

Runtime: 52 ms
Memory: 17.1 MB

This is a really smart solution utilizing the characteristics of the min-heap
data structure. The intuition is the following:
  - if we sort the intervals array by start time, we will always be looking at
    a meeting that starts earliest
  - if we use a min heap of end times, the top element will always be the
    meeting that ends earliest
  - we just need to compare the meeting that starts earliest and the meeting
    that ends earliest. if these two overlap, we need a new room. if they don't
    simply update the end time (namely, extend).
------------------------------------------------------------------------
'''
class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i[0] >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
        return len(heap)

'''
------------------------------------------------------------------------
Solution 2: Min-Heap
Time: O(nlogn)
Space: O(n)

Runtime: 69 ms
Memory: 17 MB

This is the exact same min-heap solution as solution 1, but implemented slighly
differently e.g. push first, no else statement.
------------------------------------------------------------------------
'''
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key= lambda x:x[0])
        heapq.heappush(free_rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)

'''
------------------------------------------------------------------------
Solution 3: Chronological Ordering - Two Pointers
Time: O(nlogn)
Space: O(n)

Runtime: 91 ms
Memory: 16.8 MB

This is a two pointers solution that separates start times and end times.
Using separated arrays for start and end times, we iterate through the start_times
array and see how many rooms we need to afford the meetings in intervals array.

The two pointer approach has a similar intuition to the min-heap approach in that
they both are trying to compare the meeting that starts earliest and the meeting
that ends earliest. The two pointer approach achieves this by updating and
advancing the start_pointer and end_pointer.

Only when you find out that the earliest ending meeting ends before the
start time of the earliest starting meeting, you increase the end_pointer by 1.
  - subtracting used_rooms by 1 is to nullify the effect of used_rooms += 1
  - start_pointer is += 1 regardless since we either update end_pointer or
    add a new room.
------------------------------------------------------------------------
'''
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        used_rooms = 0
        
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        start_pointer = 0
        end_pointer = 0
        
        while start_pointer < len(intervals):
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            
            used_rooms += 1
            start_pointer += 1
        
        return used_rooms