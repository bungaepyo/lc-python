'''
------------------
Difficulty: Medium
------------------

Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3] 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
'''

'''
------------------------------------------------------------------------
Solution 1: One Pass (insert & pop)
Time: O(n)
Space: O(1)

Runtime: 77 ms
Memory: 13.5 MB

This is a one-pass solution mostly using python's insert and pop array functions.
Simply put, we start iterating from the end of the array (reduce complexities in index calc),
and insert an extra 0 whenever we encounter a 0. After that, we pop() from
the array so that len(arr) is kept same.
------------------------------------------------------------------------
'''
class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()

'''
------------------------------------------------------------------------
Solution 1: Two Pass
Time: O(n)
Space: O(1)

Runtime: 90 ms
Memory: 13.7 MB

This is a slightly more complicated solution using a two pass method.
Since we should amend the existing array in place, we are using the first
pass to count how many possible duplicates (a.k.a how many zeros) there are.
One edge case we need to consider is when the last element of the result
array is zero, and it does not have space for duplication. In this case (left == length-possible_dups),
we simply copy the zero to the last index of the array (w/o duplicating) 
and simply shrink length by 1 so that it's not included in the second pass.

In the second pass, we start from length-possibe_dups and iterate the arr backwards.
Whenever we find a zero, we copy twice, filling in from the back (i+possible_dups).
------------------------------------------------------------------------
'''
class Solution(object):
    def duplicateZeros(self, arr):
        possible_dups = 0
        length = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length - possible_dups:
                    arr[length] = 0 # For this zero we just copy it without duplication.
                    length -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]