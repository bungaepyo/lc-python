'''
------------------
Difficulty: Medium
------------------

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements
(it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashSet -> accepted, but time complexity is not O(1)
Time: O(n)
Space: O(n)

Runtime: 628 ms
Memory: 59.8 MB

This is a pretty intuitive solution using a hashset. However, due to the
function list() trying to transform a set into an array, this implementation
has a time complexity of O(n).
------------------------------------------------------------------------
'''
import random

class RandomizedSet(object):

    def __init__(self):
        self.hashset = set()

    def insert(self, val):
        if val in self.hashset:
            return False
        else:
            self.hashset.add(val)
            return True

    def remove(self, val):
        if val in self.hashset:
            self.hashset.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        length = len(self.hashset)
        idx = random.randint(0,length-1)
        return list(self.hashset)[idx]

'''
------------------------------------------------------------------------
Solution 2 - HashMap + Array
Time: O(1)
Space: O(n)

Runtime: 455 ms
Memory: 60.1 MB

This is a solution that uses a combination of hashmap and array to achieve
O(1) time complexity. We need the list along with the hashmap because
hashmaps key value pairs are not stored in order. In order to achieve O(1)
time complexity for removal, we should be able to remove an element directly by
it's index.

Thus, when we insert a number, we add its value & index to the hashmap and add
its value to the list. When removing a number, we use a little trick of using
the last element of the array.

As long as we know what value we want to remove, we are able to get its
index by looking it up in the hashmap. Once we have the index, we also need
the last element of the array.

We simply put the last element in val's position and update last element's
index to val's index. Then, we pop() from list and delete map[val].
------------------------------------------------------------------------
'''
import random

class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val):
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val in self.map:
            last_element, idx = self.list[-1], self.map[val]
            self.list[idx], self.map[last_element] = last_element, idx
            self.list.pop()
            del self.map[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.list)