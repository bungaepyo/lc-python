'''
------------------
Difficulty: Medium
------------------

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointer
Time: O(n^2)
Space: O(1)

Runtime: 691 ms
Memory: 16.6 MB

In this 3 sum problem, the first thing you need to do is to fix a number and continue with a two sum sub-problem.
This solution is a relatively intuitive one using the two pointer method - the core is to use sort() in the beginning.
Assuming the numbers in nums are sorted before iteration, you fix a number at (i) and put the lowest bigger number as (l) and the biggest number as (r).
Using a while loop, you adjust the sum of numbers at (i) (l) (r) by increasing or decreasing (l) and (r).
Once a match is found, add it to the result arrary.
Two things to take note of:
  (1) check & skip duplicate integers using the if i>0 and nums[i] == nums[i-1] condition.
  (2) skip (l) and (r) to the next integer by using conditions at line 66 and 68.
------------------------------------------------------------------------
'''
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1; r-=1
        return res

'''
------------------------------------------------------------------------
Solution 2 - Step By Step
Time: O(n^2)
Space: O(1)

Runtime: 621 ms
Memory: 17.1 MB

#1. Split nums into three lists: negative numbers, positive numbers, and zeros
#2. Create a separate set for negatives and positives for O(1) look-up times
#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P. i.e. (-3, 0, 3) = 0
#4. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
#5. For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists in the positive number set
#6. For all pairs of positive numbers (1, 1), check to see if their complement (-2) exists in the negative number set
------------------------------------------------------------------------
'''
def threeSum(self, nums):
	res = set()
  #1
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)
  #2
	N, P = set(n), set(p)

	#3   
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#4
	if len(z) >= 3:
		res.add((0,0,0))

	#5
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#6
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res
