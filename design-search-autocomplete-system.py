'''
------------------
Difficulty: Hard
------------------

Design a search autocomplete system for a search engine.
Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n
where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times
the sentence was typed. For each input character except '#',
return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends,
and in this case, you need to return an empty list.

Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.
If there are fewer than 3 matches, return them all.
 
Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Constraints:

n == sentences.length
n == times.length
1 <= n <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
c is a lowercase English letter, a hash '#', or space ' '.
Each tested sentence will be a sequence of characters c that end with the character '#'.
Each tested sentence will have a length in the range [1, 200].
The words in each input sentence are separated by single spaces.
At most 5000 calls will be made to input.
'''

'''
------------------------------------------------------------------------
Solution 1: Trie
Time: O(?)
Space: O(?)

Runtime: 1351 ms
Memory: 21.5 MB

This question is a good simplified example of how a Trie data structure
could be applied in real life. Designing and implementing an autocomplete
system might sound intimidating, but it isn't hard to follow once you get
the idea.

The underlying intuition here is to utilize the Trie as much as we can.
  - We initialize the autocomplete system by creating a new Trie with
    the given sentences and their hot degrees. This could be done by using
    a helper function that adds a sentence to the Trie. Each TrieNode would
    have attributes such as children, isEnd, data, rank. Only the last node
    will have data (actual sentence), rank (cumulative hot degree), and isEnd=True.
  - Each time the user types a new character input, the input() function is called.
    We also created self.keyword upon system initialization in order to
    keep track of user's current complete sentence so we should be able
    to use the entire keyword if needed.
      (1) if the input is "#" it means the sentence ended, so we add that
          sentence with hot degree of 1 and reset the keyword.
      (2) if the input is not "#" it means we need to return max 3 hottest
          sentences that start with current keyword + latest input.
  - Given the current keyword, we need to first find every sentence stored
    in the Trie that starts with that keyword. For example, "i l" could
    return ["i love you", "i lie to you", "i love leetcode"], etc.
    Since we stored the sentence at the last TrieNode on self.data, we just
    need to find the last TrieNode that current keyword can take us, and
    start a dfs there in order to find all sentences and their hot degrees.
  - The base case of the dfs would be whe leaf nodes of Trie, starting from
    prefix. Since we have self.isEnd attributes, we would be able to identify
    the base case pretty easily.
      (1) if node.isEnd, we simply append (node.rank, node.data) to result
          array and return it
      (2) if node is not leaf, we "extend" (not append) the result array
          by recursively calling the dfs function on all its children.

          IMPORTANT: use node.children[child] because just "child" is unicode
  - Once we figured out the list of sentences that start with current keyword,
    we are going to sort it by rank and return the first three. Since we've
    been subtracting hot degrees from rank, hotter ones should be located
    in the front.
------------------------------------------------------------------------
'''
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addSentence(sentence, times[i])
            
    def addSentence(self, sentence, hot):
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True
        curr.data = sentence
        curr.rank -= hot
        
    def dfs(self, node):
        res = []
        if node:
            if node.isEnd:
                res.append((node.rank, node.data))
            for child in node.children:
                res.extend(self.dfs(node.children[child]))
        return res
    
    def search(self, keyword):
        curr = self.root
        for ch in keyword:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        return self.dfs(curr)

    def input(self, c):
        res = []
        if c == '#':
            self.addSentence(self.keyword, 1)
            self.keyword = ""
        else:
            self.keyword += c
            res = self.search(self.keyword)
        return [item[1] for item in sorted(res)[:3]]