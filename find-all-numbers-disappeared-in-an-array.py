'''
------------------
Difficulty: Easy
------------------

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2] 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
'''

'''
------------------------------------------------------------------------
Solution 1 - Use a set, One Pass
Time: O(n)
Space: O(n)

Runtime: 298 ms
Memory: 23.1 MB

This is a one pass solution using a set, thus has a space complexity of O(n).
We make nums a set of its elements, and iterate through the integers from
1 to len(num). If a number is not in set(nums), it means that the number
is missing from the sequence. Therefore, add it to the result array.
------------------------------------------------------------------------
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        N = len(nums)
        nums = set(nums)
        res = []
        
        for i in range(N):
            if i+1 not in nums:
                res.append(i+1)
        
        return res

'''
------------------------------------------------------------------------
Solution 2 - Use a hashmap, One Pass
Time: O(n)
Space: O(n)

Runtime: 660 ms
Memory: 24.5 MB

This solution uses the exact same logic as solution 1, but uses a hashmap.
It takes longer than using a set because of the duplicates.
------------------------------------------------------------------------
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        hashtable = {}
        res = []
        
        for num in nums:
            hashtable[num] = True
        
        for i in range(len(nums)):
            if i+1 not in hashtable:
                res.append(i+1)
                
        return res

'''
------------------------------------------------------------------------
Solution 3 - Negation, O(1) In-Place
Time: O(n)
Space: O(1) -> space of the output array doesn't count toward the space complexity

Runtime: 318 ms
Memory: 20.8 MB

This is a very clever solution using the negation technique to solve it in O(1) space.
While all elements are integers between 1 and len(nums), no one is stopping
us from manipulating the magnitude of the elements. Therefore, we are able
to mark the visited integers by making the indices negative integers.
For example, while iterating we visited 3, we will multiply nums[3] with -1.

Later on our second paas (0,len(nums)-1), we will see which indices were not marked negative
and add i+1 to the output array. 
------------------------------------------------------------------------
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            num = abs(nums[i])-1
            if nums[num] > 0:
                nums[num] = -nums[num]
        
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res