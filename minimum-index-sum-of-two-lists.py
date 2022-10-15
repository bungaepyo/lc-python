'''
------------------
Difficulty: Easy
------------------

Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that
if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order.

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
 
Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the strings of list1 are unique.
All the strings of list2 are unique.
'''

'''
------------------------------------------------------------------------
Solution 1 - Hashmap, but naive
Time: O(nm*x) -> n, m are lengths of list1 and list2, x is average string length
Space: O(nm)

Runtime: 953 ms
Memory: 13.9 MB

This is a naive approach using a hashmap. We basically compare each and every
element from the two lists and add a indexSum -> string key value pair
to the hashmap. Once done, we calculate the minimum number of all the keys
in hashmap and return the values for that key.
------------------------------------------------------------------------
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        hashmap = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if not hashmap.get(i+j):
                        hashmap[i+j] = []
                    hashmap.get(i+j).append(list1[i])
        
        minSum = min(hashmap.keys())
        return hashmap.get(minSum)

'''
------------------------------------------------------------------------
Solution 2 - Hashmap, linear
Time: O(nm)
Space: O(n*x)

Runtime: 379 ms
Memory: 13.9 MB

This is a more advanced version of the hashmap approach. We first put in
all the values in list1 into a hashmap: list[i] -> i
Then, we iterate list2's elements and see if there is a key in hashmap
that matches the element. If there is, we calculate the index sum of two,
and try to update the min_sum and result array.
------------------------------------------------------------------------
'''
class Solution(object):
    def findRestaurant(self, list1, list2):
        hashmap = {}
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        res = []
        min_sum = float('inf')
        for j in range(len(list2)):
            if list2[j] in hashmap.keys():
                curr_sum = j + hashmap.get(list2[j])
                if curr_sum < min_sum:
                    res = [list2[j]]
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                    res.append(list2[j])
        return res