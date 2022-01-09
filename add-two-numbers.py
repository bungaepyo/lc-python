'''
------------------
Difficulty: Medium
------------------

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

#ListNode
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
------------------------------------------------------------------------
Solution 1 - Math using while loop, no recursion
Time: O(max(m,n))
Space: O(max(m,n)) - length of returned list is at most max(m,n)+1

Runtime: 139ms

This is a very readable solution, but relies on the divmod function.
If divmod is replaced by % and /, exceeds time complexity.
------------------------------------------------------------------------
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        dummy = result
        carry = 0
        out = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1+val2+carry, 10)
            
            dummy.next = ListNode(out)
            dummy = dummy.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return result.next
'''
------------------------------------------------------------------------
Solution 2 - Math using while loop, no recursion (simplified)
Time: O(max(m,n))
Space: O(max(m,n)) - length of returned list is at most max(m,n)+1

Runtime: 57ms

This is an alternative solution to solution 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, out = divmod(val1+val2+carry, 10)
            dummy.next = ListNode(out)
            dummy = dummy.next
        return result.next

'''
------------------------------------------------------------------------
Solution 3 - Math using while loop, no recursion, no divmod
Time: O(max(m,n))
Space: O(max(m,n)) - length of returned list is at most max(m,n)+1

Runtime: 82ms

This is an alternative solution, not relying on the divmod function.
This solution introduces the floor division operator // and gets rid of "out" variable in solution 1 & 2.
------------------------------------------------------------------------
'''
class Solution(object):
  def addTwoNumbers(self, l1, l2):
        result = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            dummy.next = ListNode(carry%10)
            dummy = dummy.next
            carry //= 10
        return result.next

'''
------------------------------------------------------------------------
Solution 4 - Recursion
Time: O(max(m,n))
Space: O(max(m,n)) - length of returned list is at most max(m,n)+1

Runtime: 64ms

This is a recursive solution.
------------------------------------------------------------------------
'''
def printList(nodeStart):
    print(nodeStart.val)
    if nodeStart.next == None:
        return
    else:
        printList(nodeStart.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
            
        if l1 == None:
            return l2
            
        if l2 == None:
            return l1
            
        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            rval = l1.val + l2.val-10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode