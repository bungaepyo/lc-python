'''
------------------
Difficulty: Hard
------------------

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree.
An N-ary tree is a rooted tree in which each node has no more than N children.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string
and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

as [1 [3[5 6] 2 4]]. Note that this is just an example,
you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format,
where each group of children is separated by the null value.

For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above-suggested formats,
there are many more different formats that work so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Example 2:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

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
Solution 1: Preorder DFS
Time: O(N)
Space: O(N)

Runtime: 66 ms
Memory: 19.2 MB

If you're not used to serializing/deserializing trees, coming up with an
idea can be relatively hard for these types of design questions. However,
if you think about it very carefully, it is not as hard as it may look.

The underlying intuition is to recursively traverse the n-ary tree in preorder
fashion, and mark "no more children" as "#", meaning traversal is done for
a given subtree.

In the serialization scenario, we simply implement a preorder traversal
and add a "#" at the end of each recursive function call due to the reason
mentioned above. This will help use to deserialize much more easily.

In the deserialization scenario, we generate a token array with the data
that we get, and create a root node to be returned using the leftmost token.
And then we do the exact same thing as we did while serializing, but opposite.
We recursively traverse the tokens while popping from left:
  - while tokens[0] != '#' is equivalend to for child in node.children because
    '#' indicates that there is no more children.
  - for every child, we create a new node and add to the parent's children array
    and recursively process the new node's children. This recursion will
    help us get rid of the nested '#' tokens.
------------------------------------------------------------------------
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root):
        res = []
        
        def preorder(node):
            if not node:
                return
            
            res.append(str(node.val))
            
            for child in node.children:
                preorder(child)
            
            res.append('#')

        preorder(root)

        return " ".join(res)
    
    def deserialize(self, data):
        if not data:
            return None
        
        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])
        
        def helper(node):
            if not tokens:
                return
            
            while tokens[0] != '#':
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)
            
            tokens.popleft()
        
        helper(root)
        return root