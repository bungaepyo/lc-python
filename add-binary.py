'''
------------------
Difficulty: Easy
------------------

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101" 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

'''
------------------------------------------------------------------------
Solution 1 - String Conversion
Time: O(max(a,b))
Space: O(max(a,b))

Runtime: 28 ms
Memory: 13.7 MB

This problem is a binary version of the add the numbers problem, and this is
a non-bit-manipulation approach to solve it. Be aware that this heavily involves
type conversion using casting functions like str() and int().

First, we add a and b by making them into integers and make that sum into a string again
to allow index iteration.
While iterating the sum string from backwards, we use a carry to compute
overflowing numbers for the binary result.
Once we still have a non-zero carry after iteration is done, we simly add "1" in the beginning.
------------------------------------------------------------------------
'''
class Solution(object):
    def addBinary(self, a, b):
        plus = str(int(a) + int(b))
        carry = 0
        res = []
        
        for i in range(len(plus)-1, -1, -1):
            intPlus = int(plus[i]) + carry
            if intPlus > 1:
                intPlus -= 2
                res.insert(0, str(intPlus))
                carry = 1
            else:
                res.insert(0, str(intPlus))
                carry = 0

        if carry != 0:
            res.insert(0, '1')

        return ''.join(res)

'''
------------------------------------------------------------------------
Solution 2 - Bit-by-bit Computation
Time: O(max(a,b))
Space: O(max(a,b))

Runtime: 26 ms
Memory: 13.5 MB

This is the exact same approach as solution 1, but uses the bit concept
instead of converting types of a and b.
If a or b's index is 1, add that to carry. If carry % 2 == 1 add "1" to the answer
and add "0" otherwise. Update carry with // 2.
------------------------------------------------------------------------
'''
class Solution(object):
    def addBinary(self, a, b):
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)

'''
------------------------------------------------------------------------
Solution 3 - Bit Manipulation
Time: O(a+b)
Space: O(max(a,b))

Runtime: 33 ms
Memory: 13.6 MB

This is a bit manipulation solution using XOR.
------------------------------------------------------------------------
'''
class Solution(object):
    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]