'''
------------------
Difficulty: Medium
------------------

Design a data structure that supports adding new words and
finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.'
where dots can be matched with any letter.
 
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

'''
------------------------------------------------------------------------
Solution 1: Trie
Time: O(M) for well-defined words, O(26^M) for totally undefined word
Space: O(1) for well-defined word, O(M) for undefined word (recursion stack)

Runtime: 11420 ms
Memory: 116.8 MB

This problem could be a bit tricky to come up with a working solution because
we need to consider "." while searching.
  - The addWord function follows the typical insertion to a Trie method.
  - The search function is a bit different, and it needs to use a dfs
    because if we encounter a "." we need to search all available children
    since it could be any letter.
    (1) base case would be when current node is last TrieNode, and there
        is no more characters left to find in word. We've found a match.
    (2) If word[0] == "." we need to iterate through all the children
        nodes and recursively check if there is a match.
    (3) If word[0] != "." we need to check if word[0] is a valid key
        in node.children, and if it is, keep recursively checking with
        the corresponding child node.

Due to TLE errors, I had to reference other solutions and implement a trick
to avoid getting TLE. The trick is to keep track of the maximum word length
so that we don't even start a search and return False if the given word's
length is larger than historic maximum word length.
------------------------------------------------------------------------
'''
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        #this is a trick to avoid TLE
        self.max_word_length = 0

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True
        #this is a trick to avoid TLE
        self.max_word_length = max(self.max_word_length, len(word))
        
    def dfs(self, node, word):
        if not word:
            if node.isEnd:
                self.res = True
            return
        if word[0] == ".":
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

    def search(self, word):
        #this is a trick to avoid TLE
        if len(word) > self.max_word_length:
            return False
        curr = self.root
        self.res = False
        self.dfs(curr, word)
        return self.res