'''
------------------
Difficulty: Easy
------------------

A school is trying to take an annual photo of all the students.
The students are asked to stand in a single file line in non-decreasing order by height.
Let this ordering be represented by the integer array expected
where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in.
Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.

Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match. 

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: Sort
Time: O(nlogn)
Space: O(1)

Runtime: 38 ms
Memory: 13.3 MB

This is a really simple solution using the sort() function. This won't be accepted
in most other cases.
------------------------------------------------------------------------
'''
class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        expected.sort()
        unmatch = 0 
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                unmatch += 1
        return unmatch

'''
------------------------------------------------------------------------
Solution 2: Counting Sort
Time: O(n)
Space: O(n)

Runtime: 33 ms
Memory: 13.5 MB

This is a solution using the counting sort method to compare these two:
  - height frequency list iterated in ascending order
  - heights array
Since height frequency list iterated in ascending order (heightToFreq) is
equivalent to the "expected" array of heights, comparing currHeight and heights[i]
is valid.
Each time we do a comparison:
  - (1) we find the next currHeight that is not zero
  - (2) decrease frequency of currHeight by 1 (since we've done the comparison)
  - (3) proceed with the for loop (compare the next element in heights)
------------------------------------------------------------------------
'''
class Solution(object):
    def heightChecker(self, heights):
        heightToFreq = [0]*101
        
        for height in heights:
            heightToFreq[height] += 1
            
        result = 0
        currHeight = 0
        
        for i in range(len(heights)):
            while heightToFreq[currHeight] == 0:
                currHeight += 1
            
            if currHeight != heights[i]:
                result += 1
            
            heightToFreq[currHeight] -= 1

        return result