'''
------------------
Difficulty: Medium
------------------

Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map.
If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 
Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
'''

'''
------------------------------------------------------------------------
Solution 1 - Trie
Time: O(k) for both insert and sum, where k is length of input key/prefix
Space: O(k) -> space used is linear in the size of the total input

Runtime: 21 ms
Memory: 13.7 MB

This is a solution using a Trie data structure implemented with a hashmap.
Two important things:
  - Since each prefix sum should return the sum of all keys' values that start with the prefix,
    it's easier if the prefix TrieNode already stores that sum. Therefore,
    each time we insert a new key, we are going to add its value to all TrieNode
    on its path.
  - In order to account for the overriding of values, we should use a hashmap
    to update the key's value and calculate the delta each time we insert a new key/value pair.
------------------------------------------------------------------------
'''
class TrieNode(object):
    
    def __init__(self):
        self.score = 0
        self.children = {}

class MapSum(object):

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        curr = self.root
        curr.score += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.score += delta

    def sum(self, prefix):
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.score
