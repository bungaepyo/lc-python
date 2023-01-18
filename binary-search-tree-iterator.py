'''
------------------
Difficulty: Medium
------------------

Implement the BSTIterator class that represents an iterator
over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number
in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid.
That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 
Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
'''

'''
------------------------------------------------------------------------
Solution 1: Flattening the BST
Time: O(n) for constructor, O(1) for next(), O(1) for hasNext()
Space: O(n)

Runtime: 54 ms
Memory: 22.7 MB

This is a solution that satisfies the follow-up requirements, which is
running next() and hasNext() function in O(1) time. We do this by traversing
the TreeNodes in inorder and creating a TreeNode array with elements sorted
in inorder, while running the constructor.

After this, if we keep track of the current index with a global variable,
we are able to conveniently move the current node to next by simply updating
the current index. Implementing hasNext() is even easier because you only
need to compare current index and length of the inorder array.
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        self.inorder = []
        self.index = -1

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.inorder.append(root)
            root = root.right

    def next(self):
        self.index += 1
        curr = self.inorder[self.index]
        return curr.val

    def hasNext(self):
        return self.index < len(self.inorder)-1

'''
------------------------------------------------------------------------
Solution 2: Controlled Recursion
Time: O(1) for next(), O(1) for hasNext()
Space: O(n)

Runtime: 62 ms
Memory: 22.2 MB

This solution does basically the same thing as solution 1, immitating the
recursive stack with custom stack.
------------------------------------------------------------------------
'''
class BSTIterator:
    def __init__(self, root):
        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self):
        return len(self.stack) > 0