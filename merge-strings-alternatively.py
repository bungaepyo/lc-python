'''
------------------
Difficulty: Easy
------------------

You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

'''
------------------------------------------------------------------------
Solution 1: One pointer
Time: O(min(m,n))
Space: O(1) -> we are only considering the space consumed by input strings

Runtime: 7 ms
Memory: 12.2 MB

After alternatively merging strings until the shorter one runs out, we just
append the rest of the longer string at the end. This means we don't even
need two pointers.

All we need to figure out is the length of the shorter string, so that we
can set that as the range of iteration to merge alternatively. After the
iteration, we just append rest of both strings to the result. One of them
should be empty anyways.
------------------------------------------------------------------------
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        shorterLen = len(word1) if len(word1) < len(word2) else len(word2)

        for i in range(shorterLen):
            res += word1[i]
            res += word2[i]

        res += word1[shorterLen:]
        res += word2[shorterLen:]

        return res
        
'''
------------------------------------------------------------------------
Solution 2: Two pointer
Time: O(m+n)
Space: O(1)

Runtime: 25 ms
Memory: 12.5 MB

This is a two pointer method that iterates the whole of word1 and word2.
Basically you set up a while loop with two independent conditions within.
Iterate throuth both words and return the joined result.
------------------------------------------------------------------------
'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = j = 0

        res = []

        while i < m or j < n:
            if i < m:
                res += word1[i]
                i += 1
            if j < n:
                res += word2[j]
                j += 1

        return "".join(res)