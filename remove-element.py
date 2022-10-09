'''
------------------
Difficulty: Easy
------------------

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

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
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: One Pass - Pointer
Time: O(n)
Space: O(1)

Runtime: 16 ms
Memory: 13.4 MB

This is a one pass solution using a pointer. While iterating the nums array,
whenever we find something that is not val, we fill up the nums array from
the beginning and add 1 to the pointer.
That way, we are able to both fill up nums with non-val elements and have
k (addPointer) ready to be returned.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeElement(self, nums, val):
        addPointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[addPointer] = nums[i]
                addPointer += 1
        return addPointer

'''
------------------------------------------------------------------------
Solution 2: One Pass - Pointer (when removal is rare)
Time: O(n)
Space: O(1)

Runtime: 25 ms
Memory: 13.6 MB

"The relative order of the elements may be changed."
It is really important to keep in mind the above statement in the problem description,
because we can simply swap out the val element with the last element and
decrease the length by 1. This would allow us to save up the unnecessary
operation of copying over all non-val elements.
Even if the unknown last element is swapped in, we are able to check that
on the next iteration since we do not increase i when we found val.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n

'''
------------------------------------------------------------------------
Solution 3: Two Pointers
Time: O(n)
Space: O(1)

Runtime: 39 ms
Memory: 13 MB

This is a straightforward two pointers solution. While left pointer is smaller than
or equal to right pointer, if left pointer points to the val, we swap with
right pointer's value and decreases right pointer & increase k.
Otherwise, we increase left pointer and proceed.
At the end, we return len(nums)-k since that's the nubmer of non-value
numbers in the rearranged array.
------------------------------------------------------------------------
'''
class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)-1
        k = 0
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                k += 1
            else:
                left += 1

        return len(nums)-k