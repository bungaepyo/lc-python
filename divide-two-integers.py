'''
------------------
Difficulty: Medium
------------------

Given two integers dividend and divisor, divide two integers
without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−231, 231 − 1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''

'''
------------------------------------------------------------------------
Solution 1 - Bit Shifting (exponential search)
Time: O((log a)^2) - left shift operation takes O(log a)
Space: O(1)

Runtime: 34 ms
Memory: 13.4 MB

This is a solution using the bit manipulation technique, specifically the bit
shifting method (<< or >>). First of all, since we're not allowed to use
division and multiplication (nor mod operator), it's important to understand
the meaning of division. The value returned after dividing a dividend with a divisor
tells us how many times the divisor can fit in the dividend.

Say a is the dividend and b is the divisor.

Mocking the division operation with bit manipulation essentially utilizes the same concept.
Two things to take note of:
  (1) b << i is equivalent to b * 2**i (bit shifting i times to the left means multiplying by 2**i)
  (2) b >> i is equivalent to b / 2**i
Therefore, if b << i is less than a, it means b can fit in a for at least 2**i times.
Hence, if we loop from 31 to 0 (in general, the size of an integer data type is 32 bits),
and do the comparison starting from larger powers to lower, we would be able to know
how many times b may fit in a. If a <= b << i
  (1) add 2**i to the answer 
  (2) subtract b << i from a (so that we can start again with the remaining portion)

Potential issue of using abs(): abs(-2**31) is 2**31 which is outside the allowed range by 1.
------------------------------------------------------------------------
'''
class Solution(object):
    def divide(self, dividend, divisor):
        ans = 0
        
        neg = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                ans += 2**i
                dividend -= divisor << i
        
        ans = ans if not neg else -1*ans
        return min(max(-2147483648, ans), 2147483647)



'''
------------------------------------------------------------------------
Solution 2 - Exponential Search
Time: O((log a)**2)
Space: O(1)

Runtime: 38 ms
Memory: 13.5 MB

This is an exponential search solution without using the bit shifting technique.
------------------------------------------------------------------------
'''
class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        # Once the divisor is bigger than the current dividend,
        # we can't fit any more copies of the divisor into it anymore */
        while divisor >= dividend:
            # We know it'll fit at least once as divivend >= divisor.
            # Note: We use a negative powerOfTwo as it's possible we might have
            # the case divide(INT_MIN, -1). */
            powerOfTwo = -1
            value = divisor
            # Check if double the current value is too big. If not, continue doubling.
            # If it is too big, stop doubling and continue with the next step */
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            # We have been able to subtract divisor another powerOfTwo times.
            quotient += powerOfTwo
            # Remove value so far so that we can continue the process with remainder.
            dividend -= value

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient
