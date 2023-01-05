'''
------------------
Difficulty: Medium
------------------

In English, we have a concept called root, which can be followed by some other word
to form another longer word - let's call this word successor.
For example, when the root "an" is followed by the successor word "other",
we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the successors in the sentence with the root forming it.
If a successor can be replaced by more than one root,
replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c" 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
'''

'''
------------------------------------------------------------------------
Solution 1: Trie
Time: O(n)
Space: O(n)

Runtime: 186 ms
Memory: 26.3 MB

This is a solution using the Trie data structure (implemented using hashmap)
to replace words in sentences with their shortest roots in dictionary.

Underlying intuition:
  - In order to replace each word with the shortest root, we first need to build
    a trie with all the roots in the dictionary. Then, we need to iterate each word.
    While iterating each word, we are going to use the trie we created to replace
    the word with the first root we encounter, which should be the shortest applicable root.

Explanation on the trie implementation:
  - Like we learned in the data structure design problems, a trie is basically
    a nested dictionary (nested hashmap). Trie having TrieNode objects
    that have different attributes including children dict is equivalent to
    a dictionary having different keys (children, char, score) and values
    (int, string, dict).
  - In the trie implementation below, we use a defaultdict so that it auto-creates
    a dict object if the current TrieNode doesn't already have that child.
    Therefore, at the end of the day, dictionary with only one word "cat"
    could have generated a trie like this: { "c":{ "a": { "t":{ END: "cat" } } } }
  - For a short-term implementation of a trie, we can use a lambda function
    like below.
------------------------------------------------------------------------
'''
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        def _trie():
            return collections.defaultdict(_trie)

        #Short version:
        #_trie = lambda: collections.defaultdict(_trie)

        trie = _trie()

        #This is a constant used as a key to mark the end of a root.
        #This could also be a string, but should be kept a boolean.
        END = True

        for root in dictionary:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        res = []
        word_list = sentence.split(" ")
        for word in word_list:
            res.append(replace(word))
        return " ".join(res)

        #Short version:
        #return " ".join(map(replace, sentence.split()))