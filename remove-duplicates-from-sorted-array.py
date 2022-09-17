'''
------------------
Difficulty: Easy
------------------

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores). 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointers
Time: O(n)
Space: O(1)

Runtime: 108 ms
Memory: 14.7 MB

This is a solution using the two pointer method. Since the problem requires us
to return the number of unique integers (K) and not the array itself, it is up to us
with what we do to integers after K. First of all, we need to check if the
array is empty and return k, which is 0 at the moment, if true. We will increase
k by 1 if the array is not empty because we will be comparing two integers using
two pointers, and we will skip the integer when two numbers match. Increasing K by 1
accounts for the first element of the array where the two pointers always point to the same integer.
Afterwards, whenever we find a pair that don't match, we will
(1) move slow pointer to right (it will be pointing to the last unique integer at the moment)
(2) update slow pointer's value to fast pointer's value
(3) increase K by 1 - since we found a new unique integer
(4) move fast pointer to right
This loop continues until fast pointer reaches the end of the array.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        fast = 0
        slow = 0
        
        if len(nums) > 0:
            k += 1
        else:
            return k
        
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                k += 1
                fast += 1
        return k

'''
------------------------------------------------------------------------
Solution 2 - Two Pointers (simplified)
Time: O(n)
Space: O(1)

Runtime: 73 ms
Memory: 14.9 MB

This is a bit simplified version of the original two pointer solution.
Fast pointer is not initialized separately, and just runs in the loop starting from 1.
The first element of the array is taken account for via returning i+1.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1

'''
------------------------------------------------------------------------
Solution 3 - Two Pointers (also simple)
Time: O(n)
Space: O(1)

Runtime: 50 ms
Memory: 15 MB

For this two pointers solution, we simply bypass the duplicates. Whenever
we find a unique element, we assign it to the index where unique pointer is
located, and update that pointer.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeDuplicates(self, nums):
        unique = 0
        val = None

        for i in range(len(nums)):
            if nums[i] != val:
                val = nums[i]
                nums[unique] = nums[i]
                unique += 1
        
        return unique