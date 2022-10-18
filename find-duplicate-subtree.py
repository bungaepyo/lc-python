'''
------------------
Difficulty: Medium
------------------

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
'''

'''
------------------------------------------------------------------------
Solution 1: HashMap, preorder serialization

Time: O(n^2) -> O(n) string copy and paste time at each node
Space: O(n^2) -> similar reason

Runtime: 26 ms
Memory: 21.8 MB

This is a solution using hashmap, which uses serialized path strings as keys.
Essentially, we serialize a path from our current node using recursion,
check if that serialized path exists in the hashmap. If value (frequency) is 2,
we know it's a duplicate subtree so add it to res.
An example of a path is: 1,2,#,#,3,#,# OR 2,#,# (leaf node)
------------------------------------------------------------------------
'''
class Solution(object):
    def findDuplicateSubtrees(self, root):
        res = []     
        hmap = {}
        
        def recurse(node):
            if node is None:
                return '#'
            
            path = ','.join([str(node.val), recurse(node.left), recurse(node.right)])
            
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
            
            return path
        
        recurse(root)
        return res