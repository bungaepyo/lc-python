'''
------------------
Difficulty: Medium
------------------

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0] 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

'''
------------------------------------------------------------------------
Solution 1: Stack
Time: O(n)
Space: O(n)

Runtime: 1872 ms
Memory: 31 MB

This is a straightforward solution using a stack data structure. You basically
add (current temperature, index) pairs while iterating the original array.

While the top element's temperature is lower than the current temperature,
meaning that the current temperature is warmer, you update the result array
and pop the top element until the current temperature is not warmer anymore.
If the current temperature is not warmer anymore, you add it's pair to the stack.

This way you would be able to see how many days it takes each day to see a
temperature warmer than itself.
------------------------------------------------------------------------
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []
        stack.append((temperatures[0], 0))
        
        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            
            while stack and stack[-1][0] < curr:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((curr, i))
        
        return res

'''
------------------------------------------------------------------------
Solution 2: Brute Force (exceeds time limit)
Time: O(n^2)
Space: O(n)

Runtime: ? ms
Memory: ? MB

This is a brute force solution just using one array. It is a good starting
point to think about the solution even though it exceeds the required limits.
Basically, you compare each element in the temperatures array and compare it
with the future temperatures until you find a one that's warmer.
------------------------------------------------------------------------
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        for day in range(n):
            for future_day in range(day + 1, n):
                if temperatures[future_day] > temperatures[day]:
                    answer[day] = future_day - day
                    break      
                
        return answer

'''
------------------------------------------------------------------------
Solution 3: Monotonic Stack (optimized solution 1)
Time: O(n)
Space: O(n)

Note: at first, you might think that the time complexity should be O(n^2) because
      there is a nested while loop in the for loop. However, each element can be
      added to the stack at most once, meaning that the stack can only perform
      n amount of pops. Thus, it's actually O(2n) => O(n)

Runtime: 1151 ms
Memory: 25.2 MB

This is actually a simplified version of solution 1. It uses the sam intuition,
but only stores the index of each day that hasn't discovered a warmer temperature
yet in the stack.
------------------------------------------------------------------------
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                res[prev_day] = curr_day - prev_day
            
            stack.append(curr_day)
        
        return res

'''
------------------------------------------------------------------------
Solution 4: Array, Optimized Space
Time: O(n)
Space: O(1)

Runtime: 1109 ms
Memory: 27 MB

This is a solution that further improves on space complexity by utilizing
the answer array itself. The intuition is the following: if we iterate the
temperatures array backwards and keep updating how many days it takes to
see a warmer day, we would be able to skip the processing of a lot of elements.

Say there is an example array: [73, 74, 75, 71, 69, 72, 76, 73]
and its result array: [1,1,4,2,1,1,0,0]

Basically, we're doing it the opposite way from solution 1 & 3. At the point
we're looking at 75, we should be able to check the position at 71 and say that
no temperature will be greater than 71 for extra 2 days. Since 75 is larger than 71,
we can just add 2 and directly look at 72, and repeat (since 72 has 1, we add 1 again and see 76).

For elements that have no hotter temperatures in the future, this won't work.
Therefore, we need a "hottest" variable so that if a temperature is higher than
"hottest," we simply update hottest and move on. This will leave that day's value as
0 (default), and accounts for days like 76 and 73 in the example array.
------------------------------------------------------------------------
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        hottest = 0
        res = [0]*n
        
        for curr_day in range(n-1, -1, -1):
            curr_temp = temperatures[curr_day]
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= curr_temp:
                days += res[curr_day + days]
            res[curr_day] = days
        
        return res