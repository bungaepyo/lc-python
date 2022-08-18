'''
------------------
Difficulty: Medium
------------------

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input. 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping. 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Sorting and Iteration
Time: O(nlogn) => sorting function has nlogn time complexity
Space: O(n)

Runtime: 126 ms
Memory: 18.1 MB

This is the first solution that I came up with, using sorting and one-pass
iteration. Two key things to take note of:
  - you will have to sort the intervals array first in order to line the
    intervals up in increasing order of interval start index
  - there are three scenarios: (1) no overlap at all (2) overlap (3) subset.
Since interval is guaranteed to have at least one element, add the first element
and return if length of intervals is only 1.
Starting with the second element, see if the first index of current element
is lower than or equal to the last index of res[-1] => this is scenario (2)(3)
If last index of current element is smaller than or equal to res[-1][1],
this is scenario (3) and simply ignore the current element.
Otherwise, there is an overlap (2) so replace res[-1][1] with current element's
last index.
If there is no overlap at all, just add the current element to res array.
------------------------------------------------------------------------
'''
class Solution(object):
    def merge(self, intervals):
        res = []
        
        #sort all the
        intervals.sort()

        #add first element of intervals to res
        res.append(intervals[0])
        
        #if length is only 1, return it
        if len(intervals) == 1:
            return res
        
        #iterate through intervals
        for interval in intervals[1:]:
            #if there is a possible overlap, don't append to res yet
            if interval[0] <= res[-1][1]:
                #if current interval is subset of last element of res,
                #simply ignore it
                if interval[1] <= res[-1][1]:
                    continue
                #if there is an overlap, swap last idx of res[-1]
                else:
                    res[-1][1] = interval[1]
            #else add current el to res
            else:
                res.append(interval)

        return res

'''
------------------------------------------------------------------------
Solution 2: Sorting and Iteration (Shorter)
Time: O(nlogn)
Space: O(n)

Runtime: 170 ms
Memory: 18.1 MB

This is a sorting solution that uses the exact same idea introduced in
the first solution, but a bit simplified.
------------------------------------------------------------------------
'''
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged