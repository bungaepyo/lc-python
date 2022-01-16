'''
------------------
Difficulty: Medium
------------------

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1: Two Pointer
Time: O(n) - one pass
Space: O(1)

Runtime: 723 ms
Memory: 24.2 MB

This is my original solution using two pointer & greedy algorithm.
The area of the container is bound by two factors (1) height of the shorter line (2) width between the two lines.
Therefore, in order to cover the entire width range, it is best to start calculating with the largest width using the two pointer method.
With maximum width guaranteed, we need to choose which line to shift inwards.
In this situation, the decision needs to be based on the height of the lines because we need to minimize the loss caused by 
the reduction of width (inward shift).
Since the area of the container is limited by the height of the shorter line, there could be two scenarios:
  (1) inward shift of longer line: 
      we simply cannot increase the height used by the area no matter how tall the next line is 
      because area is always limited by the shorter line.

  (2) inward shift of shorter line: 
      we could come across an even shorter line (which would also decrease height) but there exists a chance 
      that we come across a line longer than the shorter line, which could increase the maximum area despite the width reduction by 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def maxArea(self, height):
        res = 0
        start = 0
        end = len(height)-1
        
        while start < end:
            w = end-start
            h = min(height[start], height[end])
            res = max(res, w*h)
            
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        
        return res