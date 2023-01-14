'''
------------------
Difficulty: Easy
------------------

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples) 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 
Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

'''
------------------------------------------------------------------------
Solution 1: Recursion
Time: O(n)
Space: O(n)

Runtime: 36 ms
Memory: 16.6 MB

This is an intuitive recursive solution to traverse a n-ary tree in postorder.
Since postorder means visiting the root node after visiting all the child nodes
(opposite of preorder), we essentially have to recursively traverse all the
child nodes before actually adding root.val to the result array. Base case
is when root is None, where it simply returns root and marks an end to the
recursive stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def postorder(self, root):
        if not root:
            return root
        
        res = []
        for child in root.children:
            res += self.postorder(child)
        
        res.append(root.val)
        return res

'''
------------------------------------------------------------------------
Solution 2: Iteration - Fake way
Time: O(n)
Space: O(n)

Runtime: 34 ms
Memory: 16.3 MB

This is an iterative solution that returns the node values in the desired
postorder form. However, we aren't actually traversing the ndoes in postorder.
We're just traversing it the opposite way and returning the opposite of
the result array.
------------------------------------------------------------------------
'''
class Solution(object):
    def postorder(self, root):
        if not root:
            return root

        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        
        return res[::-1]

'''
------------------------------------------------------------------------
Solution 3: Iteration - True way
Time: O(n)
Space: O(n)

Runtime: 40 ms
Memory: 16.5 MB

If we keep adding nodes & its children in reverse order to the stack,
there are two scenarios in which you would add a node value to the result array:
  - (1) If a node is a leaf node
  - (2) If all the child nodes have already been added - can do this by "prev" variable

Therefore, we simply need to peek (check the rightmost element of stack)
and see if it's a leaf node or if all its children have been traversed.
If so, we add to the result array, and update the prev variable.
If not, it means there are still children to be traversed. Thus, add the
child nodes to the stack in reverse order.
------------------------------------------------------------------------
'''
class Solution(object):
    def postorder(self, root):
            if not root:
                return root

            ret = []
            stack = [root]
            prev = None

            while stack:
                peek = stack[len(stack)-1]

                isLeaf = len(peek.children) == 0
                isChildDone = not isLeaf and prev == peek.children[len(peek.children)-1]

                if isLeaf or isChildDone:
                    ret.append(stack.pop().val)
                    prev = peek
                else:
                    stack.extend(peek.children[::-1])

            return ret