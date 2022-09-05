'''
------------------
Difficulty: Hard
------------------

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string. 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

'''
------------------------------------------------------------------------
Solution 1 - Two Pointers, Sliding Window
Time: O(|S|+|T|)
Space: O(|S|+|T|)

Runtime: 155 ms
Memory: 16.8 MB

This is a sliding window solution using the two pointer method. The base idea
of the sliding window solution is the following:
  - extend the window until we see all the elements of the target string
  - contract the window until the window becomes invalid
  - repeat until the right pointer reaches the end of search_string

This might sound pretty simple, but things might get a little bit tricky because
the target string might contain duplicate characters.
Therefore, we need target_letter_counts and target_len.

While right pointer is increasing,
  - if we see a target letter, we decrease target_len by 1. This allows us to
    see if we need to continue extending the window.
  - regardless of we saw a target letter or not, we decrease target_letter_counts[search_string[end]] by 1.
    since target_letter_counts was initialized as the count of unique characters in target string,
    anything char that is not a unique char in target string will have a negative value.

If we found all target letters (a.k.a target_len == 0):
  - we update the min_window if (1) we haven't updated anything yet (2) our new window is smaller
  - try increasing target_letter_counts[search_string[start]] by 1. If this increase
    makes the count to be more than 10, it means char at our "start" was actually
    a target letter. If this is the case, we need to extend the window until 
    we find this target character again.
  - If this didn't make the count to be more than 0, it means char at "start"
    was not a target letter. Therefore, we continue with the while loop and
    contract the window further.
------------------------------------------------------------------------
'''
class Solution(object):
    def minWindow(self, search_string, target):
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
			      # If we see a target letter, decrease the total target letter count
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			      # If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[search_string[end]] -= 1
            
			      # If all letters in the target are found:
            while target_len == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					          # Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				        # Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window