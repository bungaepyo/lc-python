'''
------------------
Difficulty: Easy
------------------

You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0]. 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
'''

'''
------------------------------------------------------------------------
Solution 1 - Binary Search
Time: O(logn)
Space: O(1)

Runtime: 72 ms
Memory: 15.6 MB

This is a straightforward binary search solution. Although the solution
might look simple, there are a couple of important points:
  - since we're not directly looking for the target, we should set left < right
  - if letters[mid] > target, we don't know whether it's the smallest larget one.
    Therefore, only set right = mid (include mid so that it could be processed again later)

The loop will end when left == right, which should leave only one element in the
search space. If a character we were looking for didn't exist, it will
either be the first or the last character. Therefore, only return letters[left]
if letters[left] > target.
------------------------------------------------------------------------
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters)-1

        while left < right:
            mid = left + (right-left)/2
            if letters[mid] <= target:
                left = mid+1
            else:
                right = mid
        
        # post-processing is required as letters[left] is not necessarily larger than target
        return letters[left] if letters[left] > target else letters[0]