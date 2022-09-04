'''
------------------
Difficulty: Medium
------------------

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

'''
------------------------------------------------------------------------
Solution 1: Three Pointers, Dutch National Flag Problem
Time: O(n)
Space: O(1)

Runtime: 14 ms
Memory: 13.3 MB

This problem is commonly known as the dutch national flag problem, and can
be relatively intuitively solved using the three pointer approach in one-pass.
The strategy here is the following:
  - move all 2s to the end by swapping curr and p2
  - move all 0s to the start by swapping curr and p0

We initialize p0 and curr to the beginning of the nums array, and p2 to the end.
p0 should always point to the rightmost boundary of zeros, and p2 should always
point to the leftmost boundary of twos.

While curr is less than or equal to (equal to because of this test case: [1,0,2]) p2,
  - if the element at curr is 0, swap p0 and curr, increase p0 and curr by 1
    - it is safe to increase both p0 and curr after the swap because
      (1) if p0 and curr are in same index, both need to increase
      (2) if p0 was behind curr, number swapped in from p0 can only be 1s because
          we've already pushed all 2s to the end without touching p0 or curr.

  - if the element at curr is 1, increase curr by 1
    - only increase 1 because ones are not involved in any swapping

  - if the element at curr is 2, swap p2 and curr, decrease p2 by 1
    - with this condition, we simply push all 2s to the end
    - we do not increase curr here because the element swapped in by p2 can
      either be 0 or 1 or 2, and these should be re-evaluated in this case.
------------------------------------------------------------------------
'''
class Solution(object):
    def sortColors(self, nums):
        p0 = curr = 0
        p2 = len(nums)-1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1

'''
------------------------------------------------------------------------
Solution 2: Three Pointers
Time: O(n)
Space: O(1)

Runtime: 35 ms
Memory: 13.4 MB

This is a quite interesting solution using the three pointers method.
First, you initialize pointers for each 0, 1, 2 as -1 (idx right before looping).
Then, follow this logic:
  - save current element nums[i] in a variable, c
  - regardless of the value of c, increase p2 by 1 and update p2 to 2
  - if value of c is less than or equal to 1, increase p2 by 1 and update p2 to 1
  - if value of c is equal to 0, increase p0 by 1 and update p0 to 0

This way:
  (1) we first make everything 2s
  (2) make things 1s if they're less than or equal to 1
  (3) make things 0s if they're equal to 0

This logic automatically handles the sorting and successfully updates all elements
because you're basically
  (1) checking every element and counting how many 0s and 1s there are
  (2) updating elements based on that number
------------------------------------------------------------------------
'''
class Solution(object):
    def sortColors(self, nums):
        p0 = p1 = p2 = -1
        
        for i in range(len(nums)):
            c = nums[i]
            p2 += 1
            nums[p2] = 2
            if c <= 1:
                p1 += 1
                nums[p1] = 1
            if c == 0:
                p0 += 1
                nums[p0] = 0