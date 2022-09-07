'''
------------------
Difficulty: Hard
------------------

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Optimized Brute Force (NOT A WORKING SOLUTION)
Time: O(n^2)
Space: O(1)

Runtime: ? ms
Memory: ? MB

This is the most basic & straightforward brute force solution, but slightly optimized.
Basically what we're doing here is calculating the area of all the minimum height
rectangles from i to j, while iterating j towards the end of the array.
If the area of the rectangle we found is larger than existing max_area, update it.
------------------------------------------------------------------------
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        max_area = 0
        for i in range(len(heights)):
            minHeight = float('inf')
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                max_area = max(max_area, minHeight*(j-i+1))
        return max_area

'''
------------------------------------------------------------------------
Solution 2: Divide and Conquer (NOT A WORKING SOLUTION)
Time: average O(nlogn), worst O(n^2) => when array is sorted ascending/decending
Space: O(n)

Runtime: ? ms
Memory: ? MB

This is a divide and conquer style solution using recursion.
This approach relies on the observation that the rectangle with maximum area will be the maximum of:
  - The widest possible rectangle with height equal to the height of the shortest bar.
  - The largest rectangle confined to the left of the shortest bar(subproblem).
  - The largest rectangle confined to the right of the shortest bar(subproblem).

If you think about it, once we found the minimum height of a given range,
rectangles to the left and right of the min height index will be bound by the
minimum height.
Thus, if we recursively compare the minimum height rectangle's area of
(1) minimum index, (2) left of minimum index, (3) right of minimum index,
we would be able to more effectively find the largest rectangle in histogram.
Basically, breaking down the big problem in to subproblems on left side and right side.
------------------------------------------------------------------------
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        def helper(heights, start, end):
            if start > end:
                return 0

            minIndex = start
            for i in range(start, end+1):
                if heights[i] < heights[minIndex]:
                    minIndex = i

            return max(
                helper(heights, start, minIndex-1),
                helper(heights, minIndex+1, end),
                heights[minIndex]*(end-start+1)
            )

        return helper(heights, 0, len(heights)-1)

'''
------------------------------------------------------------------------
Solution 3: Stack
Time: O(n)
Space: O(n)

Runtime: 1352 ms
Memory: 24.6 MB

This is the only accepted, trickiest, but most efficient solution using stacks.
Basically, ths idea is this:
  - There can be N candidates for largest rectangle, starting from the height of
    each index of the heights array.
  - In order to figure out the largest rectangle for each candidate, we need to
    know the smaller height to its left and right. e.g. [(4),5,6,(4)]

Start the stack with -1 to account for the first element of the heights array.
While adding indices to the stack, whenever we find an index with height that is
smaller than that of top of the stack, we pop the top element and try updating
the max_area. We use this logic to accomplish the second bullet above.

Once we're done appending everything, if stack is not empty, we pop each of
the remaining element in the stack and try updating the max_area.

Width calc:
  - during iteration: i - stack[-1] -1
    => R-L-1
    => R has to be i because we found a smaller height to the right
    => L as to be stack[-1] since we've been appending in ascending order
  - after iteration: len(heights) - stack[-1] -1
    => R-L-1
    => R has to be len(height) because that's the only thing remaining
    => L as to be stack[-1] since we've been appending in ascending order
------------------------------------------------------------------------
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area