'''
------------------
Difficulty: Hard
------------------

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''

'''
------------------------------------------------------------------------
Solution 1 - Brute Force
Time: O(nlogn)
Space: O(n)

Runtime: 83 ms
Memory: 22.2 MB

This is a brute force solution for the problem. Iterates through all the values
of each list of k lists, put them in a new list (nodes), sort them via sorted() function,
and connects sorted nodes with a pointer.
If implementing this solution, doesn't really matter whether the initial
k number of lists are sorted or not.
------------------------------------------------------------------------
'''
class Solution(object):
    def mergeKLists(self, lists):
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

'''
------------------------------------------------------------------------
Solution 2 - Compare one by one + Priority Queue optimization
Time: O(nlogk)
Space: O(n)

Runtime: 136 ms
Memory: 23.3 MB

This solution cleverly compares the lowest value nodes of each list using
the characteristics of a PriorityQueue.
PriorityQueue is basically a heap that has values associated with priorities.
In this solution, we iterate through all the lists and put them in a PriorityQueue (q).
Since LinkedLists are represented by their head node, we are able to easily
compare the lowest valued nodes out of the k lists when using q.get() method,
which gets the node with the highest priority (lowest val).
Since we initialized a pointer (point), we point the next node to be a ListNode
with the currently lowest value. Then, (1) update point to next (2) node to next
If node still exists (list is not empty), we put it in the PriorityQueue again
so that it can be sorted through more rounds.
------------------------------------------------------------------------
'''
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next