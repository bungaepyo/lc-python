'''
------------------
Difficulty: Easy
------------------

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree. 

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion, Binary Search Style
Time: O(n)
Space: O(logn) -> recursion stack requires O(logn) because the tree is height-balanced.
                  Note that the O(n) space used to store the output does not count as
                  auxiliary space, so it is not included in the space complexity.

Runtime:  ms
Memory:  MB

This is a recursive solution that builds up a height-balanced BST in a
binary search style. The reason we try to implement this like a binary search
is because the resulting BST should be height balanced.

By height balanced it means that we have to distribute around the same number
of nodes to the left and to the right. In BST context it means that the
middle node should be the root. Since we have a sorted array, it is easy
to find the midpoint -> low+(high-low)//2. We set it as root, process the
right and left side with reduced boundaries, and return root.
------------------------------------------------------------------------
'''
class Solution(object):
    def helper(self, nums, left, right):
        if left > right:
            return None
        
        mid = left + (right-left)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid-1)
        node.right = self.helper(nums, mid+1, right)
        return node
    
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums)-1)