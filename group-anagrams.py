'''
------------------
Difficulty: Medium
------------------

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

'''
------------------------------------------------------------------------
Solution 1: Hashmap & sorted function
Time: O(N)
Space: O(N)

Runtime: 100 ms
Memory: 17.5 MB

This is a straightforward solution using hashmap and the sorted function.
First, initialize res (result list), hashmap (map that contains sorted string as key
and index in res as value), and idx (index that separates diff anagram groups in res).
Then, in a one-pass iteration of the strs list, we first sort each string
and see if it's already in the hashmap.
  - if it's already in there, simply get the index from hashmap and add
    to that index (which will be a list) of res.
  - if it's not already there, use the current idx to insert to that index of res
    and increase by 1. Also you need to add the sorted string to the hashmap
    since this should be the first encounter of the anagram set.
------------------------------------------------------------------------
'''
class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        hashmap = {}
        idx = 0
        
        for string in strs:
            sortedString = ''.join(sorted(string))
            if hashmap.get(sortedString) is not None:
                index = hashmap.get(sortedString)
                res[index].append(string)
            else:
                res.insert(idx, [string])
                hashmap[sortedString] = idx
                idx += 1
        
        return res

'''
------------------------------------------------------------------------
Solution 2: Hashmap - categorize by sorted string
Time: O(NK*logK) -> outer loop is O(N) and we sort each string in O(KlogK) time.
Space: O(NK)

N is length of strs, K is max length of strings in strs

Runtime: 68 ms
Memory: 18.3 MB

This solution uses a similar hashmap-based logic as solution 1, but is a bit
more optimized because we're using collections.defaultdict(list).

Note: defaultdict means that if a key is not found in the dictionary,
then instead of a KeyError being thrown, a new entry is created.
The type of this new entry is given by the argument of defaultdict.

By using defaultdict(list), we do not have to implement extra logic for
if and if not the sorted string exists in the dictionary.
In a one-pass for loop, we simply need to append s in ans[tuple(sorted(s))].
If it does not exist, it will create a new entry since it was initialized using
defaultdict. We use tuples as keys because it is immutable.
Also, should remember to return ans.values().
------------------------------------------------------------------------
'''
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

'''
------------------------------------------------------------------------
Solution 3: Categorize by count
Time: O(NK) -> Counting each string is linear in the size of the string, and we count every string.
Space: O(NK)

Runtime: 150 ms
Memory: 19.7 MB

This is a soltion that implements almost the exact same logic as solution 2,
but categorizes by character count, not sorted string. Strings should be anagrams
if they have exactly same amount of each characters.
Therefore, for each string in strs, we initialize a "count" array which is
essentially a representation of the letters of the alphabet and how many of
each letter has been found. We do this calculation with ord(c)-ord('a') and
adding 1 to it.
------------------------------------------------------------------------
'''
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()