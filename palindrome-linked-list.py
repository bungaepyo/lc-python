'''
------------------
Difficulty: Easy
------------------

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
'''

'''
------------------------------------------------------------------------
Solution 1 - Copy into array and use Two Pointer
Time: O(n)
Space: O(n)

Runtime: 2060 ms
Memory: 85.4 MB

This is probably one of the first approaches that comes to mind when thinking
of verifying whether a linked list is has a palindrome structure.
We simply append all the linked list node values to an array and compare the array
with its reversed version.

Accepted solution, but has poor space complexity.
------------------------------------------------------------------------
'''
class Solution(object):
    def isPalindrome(self, head):
        res = []
        
        while head is not None:
            res.append(head.val)
            head = head.next
        
        return res == res[::-1]

'''
------------------------------------------------------------------------
Solution 2 - Recursion
Time: O(n)
Space: O(n) -> recursion has n stack frames (runtime stack)

Runtime: 2512 ms
Memory: 178.7 MB -> worse than solution 1 because stack frames are large in general

This is a recursive solution that basically uses the same intuition we did for
the reverse a linked list problem. Recursion provides us with an elegant
way to iterate linked lists backwards. Along with the recursive function, we
need a variable outside of recursive calls in order to check palindrome.

Base case is when curr (initially head) is None, which means we've reached the
end of the linked list. While curr is not None:
  - return False if anything before returned False
  - return False if curr's val does not match the variable's value
  - update the variable to it's next node as we proceed with to the next recursive call.

Essentially, we are iterating forward and backward at the same time.
But, this still has a bad space complexity since recursive stack frames are big and requires O(n).
------------------------------------------------------------------------
'''
class Solution(object):
    def isPalindrome(self, head):
        self.globalHead = head
        
        def helper(curr = head):
            if curr is not None:
                if not helper(curr.next):
                    return False
                if self.globalHead.val != curr.val:
                    return False
                self.globalHead = self.globalHead.next
            return True
        
        return helper()

'''
------------------------------------------------------------------------
Solution 3 - Reverse Second Half In-Place
Time: O(n)
Space: O(1)

Runtime: 1076 ms
Memory: 84.8 MB

This is a constant space complexity solution that uses the characteristics of a palindrome.
Basically, what we're trying to do here is:
  - find where the second half begins, and reverse it
  - compare the first half and the reversed second half's values to check palindrome.

In order to do that, we need two helper functions:
  - (1) one that finds where the second half begins -> slow & fast pointers
  - (2) one that reverses a linked list -> reverse a linked list problem

Once we find out where the second half begins and reversed it,
initialize two pointers and move them forward within a while loop until we
fine an unmatching value or p2 reaches the end.

Two things to note here:
  - (1) we need to check if p2 is None as a while loop condition
        since the list can have odd number of nodes, and even if it had even
        numbers we would have to check at least one of the two pointers
  - (2) we need to reverse the second half again before returning in order to
        put it back the way it was initially
------------------------------------------------------------------------
'''
class Solution:

    def isPalindrome(self, head):
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        p1 = head
        p2 = second_half_start
        while result and p2 is not None:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result   

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    #what we've done for the reverse linked list problem
    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous