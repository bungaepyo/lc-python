'''
------------------
Difficulty: Easy
------------------
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''

'''
------------------------------------------------------------------------
Solution 1 - Reverse Iteration
Time: O(n)
Space: O(1)

Question: can the space complexity be O(n)?

Although we perform the operation in-place (i.e. on the input list itself),
in the worst scenario, we would need to allocate an intermediate space to hold the result,
which contains the N+1N+1 elements. Hence the overall space complexity of the algorithm is O(N).


Runtime: 28 ms
Memory: 13.3 MB

This is a solution using reverse iteration. Before starting, it is important
to realize that we don't need to include any list (digits) whose last element
is less than 9 since we only have to add 1 and return. Only dealing with
9s, we iterate the list from backwards. The logic is pretty intuitive
(1) always add 1 and see if element < 10 (2) if less than 10, this means
we can stop our loop since there is no overflow (3) if element is 10,
we make the element 0 and continue with the loop since we already have
the logic to add 1 in the beginning for every iteration.

Note: only edge cases are when digits[i] == 10 and i == 0, which is when
we have to add the integer 1 to the beginning of the list. e.g. [9,9]
------------------------------------------------------------------------
'''
class Solution(object):
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        
        return digits

'''
------------------------------------------------------------------------
Solution 2 - Reverse Iteration (more simple, but worse)
Time: O(n)
Space: O(1)

Question: can the space complexity be O(n)?

Although we perform the operation in-place (i.e. on the input list itself),
in the worst scenario, we would need to allocate an intermediate space to hold the result,
which contains the N+1N+1 elements. Hence the overall space complexity of the algorithm is O(N).

Runtime: 34 ms
Memory: 13.3 MB

This is also a solution using reverse iteration, but this solution iterates
all lists (digits) regardless of what their last element is. Therefore,
we do not skip any of the lists with 0-8 as last element. During iteration,
all 9s will be replaced with 0s, and we will return after +1 as soon as we
see an element that is not a 9. e.g. [1,2,9,9] => return after making 2 -> 3.
This soltion handles the [9,9] edge case with `return [1]+digits` at the end
which will only run if all elements were 9s.
------------------------------------------------------------------------
'''
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits