'''
------------------
Difficulty: Easy
------------------

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet.
If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
'''

'''
------------------------------------------------------------------------
Solution 1 - Linked List as Bucket
Time: O(n/k) -> n is number of all possible values, k is number of predefined buckets (e.g. 769)
Space: O(k+m) -> k is number of predefined buckets, m is number of unique values that must be inserted into HashSet

As to the design of a "bucket," there are several options. One could simply use another
"Array" as bucket to store all the values. However, one drawback with the
array data structure is that it would take O(n) time complexity for operations like
remove or insert, rather than desired O(1).
Thus, the better choice for implementation would be a "Linked List", which
has constant time complexity for insertion and deletion once we locate the position to update.

Runtime: 436 ms
Memory: 21.1 MB
------------------------------------------------------------------------
'''
class MyHashSet(object):

    def __init__(self):
        self.keyRange = 769 #prime number
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange
        
    def add(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        #pseudo heads
        self.head = Node(0)
    
    def insert(self, newValue):
        #if not already exists, add the new element to the head
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            #set the new head
            self.head.next = newNode
    
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                #remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                #value exists already, do nothing
                return True
            curr = curr.next
        return False

'''
------------------------------------------------------------------------
Solution 2 - Binary Search Tree (BST) as Bucket
Time: O()
Space: O()

In the Linked List approach, one drawback is that we need to scan the entire list
to verify if a value exists in the bucket (lookup operation is linear time).
To optimize this, we can use a sorted list instead.
  - Using a sorted array would achieve O(logn) time complexity, but insertion and deletion will still be O(n).
  - Using a BST, we are able to make insertion and deletion in O(logn) time.

Runtime: 471 ms
Memory: 20.9 MB
------------------------------------------------------------------------
'''
class MyHashSet(object):

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Bucket:
    def __init__(self):
        self.tree = BSTree()
    
    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)
    
    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self):
        self.root = None

    def searchBST(self, root, val):
        if root is None or val == root.val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val == root.val:
            return root
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def successor(self, root):
        # one step right and then always left
        root = root.right
        while root.left:
            root = root.left
        return root.val
        
    def predecessor(self, root):
        # one step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        if not root:
            return None
        
        #delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        #delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #delete current node
        else:
            #node is a leaf
            if not (root.left or root.right):
                root = None
            #node is not a leaf, and has right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            #node is not a leaf, has no right child, thus has left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root