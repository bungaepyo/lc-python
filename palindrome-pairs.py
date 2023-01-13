'''
------------------
Difficulty: Hard
------------------

You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"] 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.
'''

'''
------------------------------------------------------------------------
Solution 1: Hashing
Time: O(k^2 * n)
Space: O((k+n)^2)

Runtime: 3853 ms
Memory: 36 MB

This solution does use a hashtable, but the focus of solving this problem
should be on coming up with the idea of how to cover all the cases where
you can make a palindrome with two words.

To generalize things a bit, there are two big scenarios:
  - word 1 and word 2 has the same length
  - word 1 and word 2 does not have the same length

Within these two scenarios, we can further break things down.
  - word 1 and word 2 has the same length
    => In order to form a palindrome, word 1 needs to be the reverse of word 2

  - word 1 and word 2 does not have the same length
    => This means one of word 1 or word 2 is longer than the other.

    In order to form a palindrome,
    => word1 > word2: word1 has to start with the reverse of word2,
                      and the remaining part has to be a palindrome itself.
    => word2 > word1: word2 has to end with the reverse of word1,
                      and the remaining part has to be a palindrome itself.

If we are able to find all the index pairs for these three major cases,
we should be covering everything.
  - Case 1: we check if the reversed version is in our lookup table, and doesn't
            have the same index.
  - Case 2: find all prefixes (in word1, which is longer) whose remaining
            part of word1 is a palindrome itself. If the reverse of that
            prefix exists in the lookup table, it means we can build a palindrome.
  - Case 3: find all suffixes (in word2, which is longer) whose remaining
            part of word2 is a palindrome itself. If the reverse of that
            suffix exists in the lookup table, it means we can build a palindrome.
------------------------------------------------------------------------
'''
class Solution(object):
    def palindromePairs(self, words):

        def allValidPrefixes(word):
            validPrefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    validPrefixes.append(word[:i])
            return validPrefixes
        
        def allValidSuffixes(word):
            validSuffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    validSuffixes.append(word[i+1:])
            return validSuffixes
        
        word_lookup = {word:i for i, word in enumerate(words)}
        res = []
        
        for wordIndex, word in enumerate(words):
            reversedWord = word[::-1]
            
            #Case 1: word 1 and word 2 are same length
            if reversedWord in word_lookup and wordIndex != word_lookup[reversedWord]:
                res.append([wordIndex, word_lookup[reversedWord]])

            #Case 2: word 1 is longer than word 2
            for prefix in allValidPrefixes(word):
                reversedPrefix = prefix[::-1]
                if reversedPrefix in word_lookup:
                    res.append([wordIndex, word_lookup[reversedPrefix]])

            #Case 3: word 2 is longer than word 1
            for suffix in allValidSuffixes(word):
                reversedSuffix = suffix[::-1]
                if reversedSuffix in word_lookup:
                    res.append([word_lookup[reversedSuffix], wordIndex])

        return res

'''
------------------------------------------------------------------------
Solution 2: Trie
Time: O(k^2 * n)
Space: O((k+n)^2)

Runtime: 5456 ms
Memory: 609.6 MB

This is a solution that has the same intuition as solution 1, but uses
a Trie data structure to traverse through the words and do the prefix checks.

Couple important points:
  - while building the trie, we add the words in reverse order in order to
    facilitate the comparison later
  - while building the trie, whenever the remaining part of the word is
    a palindrome, we save the word index in an attribute (palindrome_suffixes)
------------------------------------------------------------------------
'''
class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []

class Solution(object):
    def palindromePairs(self, words):
        
        #Create the Trie and add the reverses of all the words
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1]
            curr = trie
            for idx, char in enumerate(word):
                #Check if remainder of word is palindrome
                if word[idx:] == word[idx:][::-1]:
                    curr.palindrome_suffixes.append(i)
                curr = curr.next[char]
            curr.ending_word = i
        
        #Look up each word in the Trie and find palindrome pairs
        res = []
        for i, word in enumerate(words):
            curr = trie
            for idx, char in enumerate(word):
                #Check for case 3
                if curr.ending_word != -1:
                    if word[idx:] == word[idx:][::-1]:
                        res.append([i, curr.ending_word])
                if char not in curr.next:
                    break
                curr = curr.next[char]
            #Case 1 and 2 only come up if whole word was iterated
            else:
                #Check for case 1
                if curr.ending_word != -1 and curr.ending_word != i:
                    res.append([i, curr.ending_word])
                #Check for case 2
                for j in curr.palindrome_suffixes:
                    res.append([i,j])
        return res
        