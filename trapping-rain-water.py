'''
------------------
Difficulty: Hard
------------------
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1 - Dynamic Programming
Time: O(n)
Space: O(n)

Runtime: 160 ms
Memory: 15.1 MB

This is a solution using dynamic programming, but I feel like coming up
with this kind of idea requires more than just being used to DP solutions.
The core of this solution are the two max lists: leftMax and rightMax.
Each of these lists contains elements that are maximum values up until the index
from the left side and from the right side. e.g. [1,1,2,2,2,3,3,3,3]
You create such list by copying the first element from the height array, and
filling the rest by doing max(height, leftMax) or max(height, rightMax).
The way we make use of these lists is the gist of the problem, and it's hard to realize:
  - min(leftMax[i], rightMax[i]) - height[i]
  - above bulletpoint subtracts height[i] from the small of the two max values,
    which means you want to subtract the floor from the second highest ceiling.
    ** if the water isn't trapped at index i: min(leftMax[i], rightMax[i]) = height[i]
    ** if the water is trapped at index i: min(leftMax[i], rightMax[i]) > height[i]

  - if we add this up for all indices, we get total area of trapped water
------------------------------------------------------------------------
'''
class Solution(object):
    def trap(self, height):
        if len(height) < 1:
            return 0

        ans = 0
        size = len(height)
        leftMax = [0]*size
        rightMax = [0]*size

        leftMax[0] = height[0]
        for i in range(1, size):
            leftMax[i] = max(height[i], leftMax[i-1])

        rightMax[size-1] = height[size-1]
        for i in range(size-2, 0, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        for i in range(1, size-1):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans