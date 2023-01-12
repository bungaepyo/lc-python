'''
------------------
Difficulty: Hard
------------------

Given an array of unique strings words, return all the word squares you can build from words.
The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string,
where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square
because each word reads the same both horizontally and vertically.

Example 1:

Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 4
All words[i] have the same length.
words[i] consists of only lowercase English letters.
All words[i] are unique.
'''

'''
------------------------------------------------------------------------
Solution 1: Backtracking + HashTable
Time: O(N*26^L) -> N is number of input words, L is length of a single word
Space: O(NL) -> in the HashTable, we store L times all words (this may be O(N^L*L))

Runtime: 650 ms
Memory: 37.2 MB

This is a solution using backtracking technique and HashTable data structure.
Once you understand the idea, the underlying intuition is not too hard:
  - In order to build a complete list of word squares, we need to start from each
    and every word since the order matters.
  - The most intuitive way to check if word square exists for every word is
    backtracking (DFS). If we find one (or more), just add to the result array.
  - During the backtracking recursion, we will have to search word candidates
    by prefix. Therefore, deciding which data structure to store the prefixes
    is important because long lookup times will cause TLE.

In this solution, we store all possible prefixes into a HashTable. Each prefix
is a key and the list of words that start with that prefix is the value.

During backtracking, we are going to add to result array and immediately return
if step == self.N since the last letter of last word can be anything (as well as
the first letter of first word). If false, we're going to joing all the word[step]
to create a prefix with which next candidates should start with.

Using a helper function, we will find those candidates from the hash table
and recursively look for word squares with those candidates.
------------------------------------------------------------------------
'''
class Solution(object):
    def wordSquares(self, words):
        self.words = words
        self.N = len(words[0])
        self.buildPrefixHashTable(self.words)
        
        results = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)

        return results
    
    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return
        
        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()
            
    def buildPrefixHashTable(self, words):
        self.prefixHashTable = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixHashTable.setdefault(prefix, set()).add(word)
                
    def getWordsWithPrefix(self, prefix):
        if prefix in self.prefixHashTable:
            return self.prefixHashTable[prefix]
        else:
            return []

'''
------------------------------------------------------------------------
Solution 2: Backtracking + Trie
Time: O(N*26^L*L) -> now we need O(L) for searching words with prefix instead of O(1)
Space: O(NL) -> in the Trie, we store L times the index for each word

Runtime: 708 ms
Memory: 37.1 MB

This is a solution with the same intuition, but implemented with the Trie data structure.
There are tradeoffs we make by using a Trie. Trie is better in terms of space complexity
since we don't have to store all the prefix variations now. However, we
cannot search for a prefix in constant time anymore, as we need to traverse
the TrieNodes. Nonetheless, Trie is pretty compact so the average case
time complexity shouldn't be that bad.

There are two caveat here:
  - when building the tree, saving the wordIndex (in words) instead of the
    actual word will can save us some space.
  - instead of labeling the word at the leaf node of the Trie, we label
    the word at each node so that we don't need to perform further traversal
    once we reach the last node in the prefix. This saves time.
------------------------------------------------------------------------
'''
class Solution(object):
    def wordSquares(self, words):
        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)
        
        results = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results
    
    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return
        
        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()
            
    def buildTrie(self, words):
        self.trie = {}
        
        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = node[char]
                node['#'].append(wordIndex)
                
    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]