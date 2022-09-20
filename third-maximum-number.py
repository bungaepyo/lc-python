'''
------------------
Difficulty: Easy
------------------

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number. 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1. 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Can you find an O(n) solution?
'''

'''
------------------------------------------------------------------------
Solution 1 - Use a Set and Delete Maximums
Time: O(n) -> set(nums) and max(nums) costs O(n)
Space: O(n) -> uses a set

Runtime: 63 ms
Memory: 14.3 MB

This is a simple but tricky solution using sets. Since the problem description
mentions that we shouuld ignore dupllicates, using a set is intuitively a good
idea since it automatically gets rid of the duplicates.
After making nums a set and figuring out the maximum element, return that element
if the length is less than 3. (if there isn't third max just return max)
Afterwards, remove the first two maximums and return the third.
------------------------------------------------------------------------
'''
class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        
        maximum = max(nums)
        
        if len(nums) < 3:
            return maximum
        
        nums.remove(maximum)
        maximum = max(nums)
        nums.remove(maximum)

        return max(nums)

'''
------------------------------------------------------------------------
Solution 2 - Seen-Maximums Set
Time: O(n)
Space: O(1)

Runtime: 66 ms
Memory: 13.9 MB

This seen-maximum solution improves the time complexity of the first solution
by using a set that only contains up to three maximum numbers (this, O(1)).
Using a helper function that returns the maximum number that has not been seen already,
we are able to determine 3 times which number is the current maximum and add it
to the seen-maximum set.
Whenever current maximum is None, it means there is no maximum that hasn't been
seen so we just return the maximum, not the third maximum.
min(seen_max) is equivalent to third maximum since we only do this three times.
------------------------------------------------------------------------
'''
class Solution(object):
    def thirdMax(self, nums):
        
        def helper(nums, seen_max):
            maximum = None
            for num in nums:
                if num in seen_max:
                    continue
                if maximum == None or num > maximum:
                    maximum = num
            return maximum
        
        seen_max = set()
        
        for _ in range(3):
            curr = helper(nums, seen_max)
            if curr == None:
                return max(seen_max)
            seen_max.add(curr)

        return min(seen_max)

'''
------------------------------------------------------------------------
Solution 3 - Keep Track of 3 Maximums Using a Set
Time: O(n)
Space: O(1)

Runtime: 44 ms
Memory: 14 MB

This is probably the most clean solution among the three. Using a single set,
we simply update the three maximum values on one pass.
Add first, see if it makes the set's length go over 3, and remove min if it does.
At the end of the day, if the length of the set is 3, you should return min.
Otherwise, return max.
------------------------------------------------------------------------
'''
class Solution(object):
    def thirdMax(self, nums):
        res = set()
        for num in nums:
            res.add(num)
            if len(res) > 3:
                res.remove(min(res))
        if len(res) == 3:
            return min(res)
        return max(res)