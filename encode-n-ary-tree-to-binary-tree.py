'''
------------------
Difficulty: Hard
------------------

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree.
An N-ary tree is a rooted tree in which each node has no more than N children.
Similarly, a binary tree is a rooted tree in which each node has no more than 2 children.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that an N-ary tree can be encoded to a binary tree
and this binary tree can be decoded to the original N-nary tree structure.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See following example).

For example, you may encode the following 3-ary tree to a binary tree in this way:

Input: root = [1,null,3,2,4,null,5,6]
Note that the above is just an example which might or might not work.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Example 3:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states.
Your encode and decode algorithms should be stateless.
'''

'''
------------------------------------------------------------------------
Solution 1: BFS
Time: O(N)
Space: O(L) -> L is maximum number of nodes that reside at the same level
            -> L could be equal to N so, we can also generalize this to O(n)
            -> at any given moment, queue contains node that are at most spread into 2 levels (2L)

Runtime: 46 ms
Memory: 21.4 MB

This is a really tricky question, because if you've never serialized or deserialized
a n-ary tree it would be hard to come up with the intuition. The underlying
intuition is using the binary tree node's left and right pointers for different
purposese:
  - left: would be pointing its leftmost child, if any
  - right: would be pointing its sibling on the right

If we simply (1) connect all the siblings with right pointer and (2) connect
parent with leftmost child, we would automatically get a functional binary tree.
The key here is to keep track of the parent node, head node (leftmost child), and
the previous node in order to connect siblings and parent-child.

For decoding, we do the complete opposite. Using a double ended queue as well,
we pop the parent and do the following:
  - identify the first child with the parent's left pointer
  - for all siblings, add to the parent's children array
  - for all siblings, add to queue
------------------------------------------------------------------------
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def encode(self, root):
        if not root:
            return root
        
        rootNode = TreeNode(root.val)
        queue = deque([(rootNode, root)])
        
        while queue:
            parent, curr = queue.popleft()
            headNode = None
            prevNode = None
            
            # traverse each child one by one
            for child in curr.children:
                newNode = TreeNode(child.val)
                if prevNode:
                    prevNode.right = newNode
                else:
                    headNode = newNode
                prevNode = newNode
                queue.append((newNode, child))
            
            # use the first child in the left node of parent
            parent.left = headNode
        
        return rootNode
	
    def decode(self, data):
        if not data:
            return data
        
        rootNode = Node(data.val, [])
        queue = deque([(rootNode, data)])
        
        while queue:
            parent, curr = queue.popleft()
            firstChild = curr.left
            sibling = firstChild
            
            while sibling:
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right
        
        return rootNode


'''
------------------------------------------------------------------------
Solution 2: DFS
Time: O(N)
Space: O(L)

Runtime: 59 ms
Memory: 20.9 MB

This is the DFS version where it recursively connects the first child with
left and rest of the children with right pointer.
------------------------------------------------------------------------
'''
class Codec:

    def encode(self, root):
        if not root:
            return None

        rootNode = TreeNode(root.val)
        if len(root.children) > 0:
            firstChild = root.children[0]
            rootNode.left = self.encode(firstChild)

        # the parent for the rest of the children
        curr = rootNode.left

        # encode the rest of the children
        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return rootNode


    def decode(self, data):
        if not data:
            return None

        rootNode = Node(data.val, [])

        curr = data.left
        while curr:
            rootNode.children.append(self.decode(curr))
            curr = curr.right

        return rootNode