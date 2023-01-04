'''
------------------
Difficulty: Medium
------------------

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted
string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 
Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''

'''
------------------------------------------------------------------------
Solution 1 - Hashmap
Time: O(m) for all three functions, where m is the key length
Space: O(m) for insert, O(1) for search and startsWith

Runtime: 260 ms
Memory: 40.3 MB

This is a solution that implements the Trie (pronounced as "try") data structure
with hashmaps. I choose hashmap over array to implement a Trie because
it saves a lot more space and is more intuitive to access the children,
although it could be a little bit slower when accessing a child.

Each TrieNode has a character, a hashmap of children, and a boolean is_end.
"is_end" is only set to True for the last TrieNode of an inserted word.
Therefore, if we insert "app" and "apple", the second "p" and the "e" would
have "is_end" set to True.

Search checks each character of the given word, and checks if is_end == True
at the end to see if that character is just a prefix or if the target word
has actually been inserted before.
------------------------------------------------------------------------
'''
class TrieNode(object):
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode(char)
                curr = curr.children[char]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.is_end == True

    def startsWith(self, prefix):
        curr = self.root
        
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True