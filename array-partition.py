'''
------------------
Difficulty: Easy
------------------

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9. 

Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
'''

'''
------------------------------------------------------------------------
Solution 1 - Sort Function
Time: O(nlogn)
Space: O(n)

Note on space complexity:
  The only variable we need is maxSum, which takes O(1)O(1) space.
  However, some space will be used for sorting the list nums.
  The space complexity of the sorting algorithm depends on the implementation of each programming language.
  Java: O(logn)
  C++: O(logn)
  Python: O(n)

Runtime: 533 ms
Memory: 15.4 MB

This is a solution using the built in sort() function. It is easy to understand,
but has a poor time complexity due to the sort() function having O(nlogn).
In order to maximize the sum of min(ai, bi), you will need to sort the array
in ascending order. That is because, since we're using the min() function to
see which value to get from the pair, if you put smaller values with bigger values,
the bigger values will be sacrificed. Therefore, it is optimal to link up pairs
starting from smaller values and getting to bigger values.
------------------------------------------------------------------------
'''
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        return res

'''
------------------------------------------------------------------------
Solution 1 - Counting Sort
Time: O(n+k) -> first pass iterate n in nums, second pass iterate numbers in k range
Space: O(k) -> elements_to_count holds O(k) values

Runtime: 395 ms
Memory: 15.5 MB

This is a solution that improves on time complexity by using the counting sort technique.
It sacrifices the space complexity a bit due to having to store O(k) elements in an array,
because counting sort array needs to be initialized with all possible elements.
In first pass, we add +1 the indices+K (negative numbers can't be indices) of all numbers in nums,
to note the frequency of each number.
In second pass, we iterate through the frequency array's elements and only add even index elements to the sum.
------------------------------------------------------------------------
'''
class Solution(object):
    def arrayPairSum(self, nums):
        K = 10000
        elements_to_count = [0]*(2*K+1)
        for num in nums:
            elements_to_count[num+K] += 1
        
        maxSum = 0
        is_even_index = True
        for element in range(2*K+1):
            while elements_to_count[element] > 0:
                if is_even_index:
                    maxSum += element - K
                is_even_index = not is_even_index
                elements_to_count[element] -= 1
        return maxSum