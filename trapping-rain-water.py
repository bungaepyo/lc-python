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

'''
------------------------------------------------------------------------
Solution 2 - Stack
Time: O(n)
Space: O(n)

Runtime: 139 ms
Memory: 14.9 MB

Simplify problem: there has to be a bar bigger than previous bars in order to trap any water.

This is a solution using a stack data structure. While iterating the height
array one-pass, there are two things we need to keep in mind:
  (1) if current bar is lower or equal to the top bar of the stack,
      it means that current bar is bound by the top bar of the stack.
  (2) if current bar is greater than the top bar of the stack, it means
      that top bar is bounded by current bar and previous bars in the stack.
      Thus, it is safe to add trapped water to this point to the answer.
If you do not encounter (2), keep adding to the stack.
If you encounter (2), add trapped water one by one by 
  (1) popping the top element => you cannot trap water if bars are next to each other
  (2) calculating the distance between current and top bar after the pop
  (3) calculating the bound height by min(current, top after pop) * top before pop
  (4) add to answer
This process would lead to adding all trapped water up to current index, and starting fresh from there.
------------------------------------------------------------------------
'''
class Solution(object):
    def trap(self, height):
        ans = current = 0
        stack = []
        
        while (current < len(height)):
            while(not len(stack) == 0 and height[current] > height[stack[-1]]):
                top = stack.pop()
                if(len(stack) == 0):
                    break
                distance = current - stack[-1] - 1
                bound_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bound_height
            stack.append(current)
            current += 1
            
        return ans

'''
------------------------------------------------------------------------
Solution 3 - Two Pointer
Time: O(n)
Space: O(1)

Runtime: 108 ms
Memory: 14.9 MB

This solution uses the same concept as solution 1 (dp), but simplifies space complexity
by using the two pointer method. As you can see from solution 1:
  - as long as right_max[i] > left_max[i], the water trapped depends upon the left_max, and vice versa
Therefore, using the two pointer method from left and right, we are able to add trapped water simultaneously from
both directions by switching directions whenever left > right or right < left.
In any direction (say left for example), if height of current left is greater than or equal to left_max,
we should update left_max since the water cannot be trapped at the index if its height is bigger.
If the height of the current left is smaller than left_max, we should add trapped water by
adding the difference between left_max and height[left]. Distance is 1 since we are iterating by one index.
------------------------------------------------------------------------
'''
class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height)-1
        ans = 0
        left_max = right_max = 0
        
        while(left < right):
            if(height[left] < height[right]):
                if height[left] >= left_max:
                    left_max = height[left]    
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans