'''
------------------
Difficulty: Medium
------------------

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order. 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
'''

'''
------------------------------------------------------------------------
Solution 1: HashMap, Hashing
Time: O(nk)
Space: O(nk)

Runtime: 16 ms
Memory: 13.8 MB

This is a solution using the hashmap data structure. The base concept of this
solution is the following:
  - in order to group shifted strings, we need to standardize them to make the comparison
  - we are able to standardize by making every string to start with "a," because
    strings in the same group will have the same sequqnce of characters
  - we use that standardized string as the key for the hashmap

We initialize an alphabet list along with the hashmap to get the characters in new positions.
For each string in strings,
  - (1) we calculate how many indices we need to move the first character to locate it at "a"
  - (2) we move the same amount with all the characters in the string and % 26
  - (3) since we have the standardized key, we add or update the hashmap
------------------------------------------------------------------------
'''
class Solution(object):
    def groupStrings(self, strings):
        hashmap = {}
        alphabet = map(chr, range(97,123))
        
        for i in range(len(strings)):
            first_char_index = ord(strings[i][0]) - 97
            index_to_move = 26 - first_char_index
            key = []
            for char in strings[i]:
                new_index = (ord(char)-97+index_to_move)%26
                key.append(alphabet[new_index])
            
            key = "".join(key)
            
            if key in hashmap:
                hashmap[key].append(strings[i])
            else:
                hashmap[key] = [strings[i]]
        
        return hashmap.values()

'''
------------------------------------------------------------------------
Solution 2: HashMap, Hashing
Time: O(nk)
Space: O(nk)

Runtime: 26 ms
Memory: 13.6 MB

This solution uses the same intuition, but divides the logic into 
multiple helper functions.
------------------------------------------------------------------------
'''
class Solution(object):
    def groupStrings(self, strings):
        hashmap = {}
        
        for string in strings:
            key = self.get_hash(string)
            
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        
        return hashmap.values()
    
    def get_hash(self, string):
        shift = ord(string[0])
        return ''.join(self.shift_letter(letter, shift) for letter in string)

    def shift_letter(self, letter, shift):
        return chr((ord(letter) - shift) % 26)