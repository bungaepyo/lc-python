'''
------------------
Difficulty: Hard
------------------

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string
and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''

'''
------------------------------------------------------------------------
Solution 1 - BFS
Time: O(n)
Space: O(n)

Runtime: 279 ms
Memory: 23.5 MB

This is a BFS style solution to serialize and deserialize the given binary tree.
In order to traverse the binary tree either in serialized form or not,
we need to use a queue data structure that can process data in FIFO fashion.

In the serialization scenario, we use a double ended queue to process
nodes level by level and append their values or "None" to a result list.

In the deserialization scenario, we also use a double ended queue, but this
time we need to use an extra index variable to keep track of potential node values.
Essentially, queue would only store actual nodes that's been created with values
in the input list. We will iterate through the input list using an index
variable to only create child nodes when the corresponding value is not "None."
------------------------------------------------------------------------
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("None")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ds = data.split(",")
        root = TreeNode(int(ds[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(ds):
            node = queue.popleft()
            if ds[i] != "None":
                left = TreeNode(int(ds[i]))
                node.left = left
                queue.append(left)
            i += 1
            if ds[i] != "None":
                right = TreeNode(int(ds[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

'''
------------------------------------------------------------------------
Solution 2 - DFS
Time: O(n)
Space: O(n)

Runtime: 505 ms
Memory: 24.8 MB

This is a recursive DFS style solution to serialize, deserialize a binary tree.
The way we serialize the binary tree is almost exactly same as the way we
traverse a binary tree in DFS fashion, except that we need to keep appending
node values and updating the serialized string variable.

The deserialization process unpacks the nodes in the same way it was serialized.
We simply pop the value from list and return None when we encounter "None."
We create a node, pop the value from list, and go forward with recursively adding
its left and right children when we encounter an valid value.
------------------------------------------------------------------------
'''
class Codec:

    def serialize(self, root):
        def rserialize(root, string):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, "")

    def deserialize(self, data):
        def rdeserialize(li):
            if li[0] == "None":
                li.popleft()
                return None
            
            root = TreeNode(li.popleft())
            root.left = rdeserialize(li)
            root.right = rdeserialize(li)
            return root
        
        data_list = deque(data.split(","))
        root = rdeserialize(data_list)
        return root
        