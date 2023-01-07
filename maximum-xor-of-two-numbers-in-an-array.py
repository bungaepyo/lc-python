'''
------------------
Difficulty: Medium
------------------

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
'''

'''
------------------------------------------------------------------------
Solution 1: Brute Force (Time Limit Exceeded)
Time: O(n^2)
Space: O(1)

Runtime: ??? ms
Memory: ??? MB

This is a nested for loop brute force solution that exceeds time limit.
The requirement is to have O(n) time complexity.
------------------------------------------------------------------------
'''
class Solution(object):
    def findMaximumXOR(self, nums):
        maximum = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                maximum = max(maximum, nums[i]^nums[j])
        return maximum

'''
------------------------------------------------------------------------
Solution 2: Bitwise Prefixes in Trie
Time: O(n)
Space: O(1)

Runtime: 1993 ms
Memory: 117 MB

The underlying intuition of this solution is: to convert all numbers into
binary form and to construct the maximum XOR bit by bit, starting from
the leftmost one.

If you think about how the XOR operators work, it essentially yields a
1 whenever the two bits we're comparing are different. Therefore, given
a number, in order to maximize its XOR with another number, the other number
should be the complete opposite bitwise when converted into binary form.

This operation is can be very intuitively implemented the Trie data structure.
Given a number in binary form and a Trie, we simply need to select the TrieNode
that has a bit that's opposite from the binary number while iterating bit
by bit from the left.
------------------------------------------------------------------------
'''
class Solution:
    def findMaximumXOR(self, nums):
        # Compute length L of max number in a binary representation
        L = len(bin(max(nums))) - 2
        # zero left-padding to ensure L bits for each number
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        
        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                # insert new number in trie
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                
                # to compute max xor of that new number 
                # with all previously inserted
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]
                    
            max_xor = max(max_xor, curr_xor)

        return max_xor