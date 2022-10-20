'''
------------------
Difficulty: Easy
------------------

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false. 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

Constraints:

-105 <= number <= 105
-231 <= value <= 231 - 1
At most 104 calls will be made to add and find.
'''

'''
------------------------------------------------------------------------
Solution 1 - HashMap
Time: O(1) for add, O(n) for find
Space: O(n)

Runtime: 627 ms
Memory: 18 MB

This is a solution using a hashmap. We design a hashmap to have number
as key and count as value, increasing the value by one when we see a number
already exists after running add().
Find function iterates through the hashmap keys and calculates complement for each number.
If current number and its complement aren't the same, we see if complement exists in hashmap.
If they are the same, we simply see if self.hashmap[num] > 1.
------------------------------------------------------------------------
'''
class TwoSum(object):

    def __init__(self):
        self.hashmap = {}

    def add(self, number):
        if number in self.hashmap:
            self.hashmap[number] += 1
        else:
            self.hashmap[number] = 1

    def find(self, value):
        for num in self.hashmap.keys():
            complement = value - num
            if num != complement:
                if complement in self.hashmap:
                    return True
            else:
                if self.hashmap[num] > 1:
                    return True
        return False

'''
------------------------------------------------------------------------
Solution 2 - Sorted List
Time: O(1) for add, O(nlogn) for find
Space: O(n)

Runtime: 776 ms
Memory: 17.9 MB

This is a solution using a sorted list, so that we can do a binary search
for the find() function. The find() function sorts the list and uses
the binary search technique to see if there is a pair whose sum is value.
Due to sorting, time complexity is O(nlogn).
The add() function just appends the number to the end of the array.
------------------------------------------------------------------------
'''
class TwoSum(object):

    def __init__(self):
        self.nums = []
        self.is_sorted = False


    def add(self, number):
        self.nums.append(number)
        self.is_sorted = False
    

    def find(self, value):
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        low, high = 0, len(self.nums)-1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else: # currSum == value
                return True
        
        return False
