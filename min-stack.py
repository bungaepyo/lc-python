'''
------------------
Difficulty: Medium
------------------

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

'''
------------------------------------------------------------------------
Solution 1: Stack of Value / Minimum Pairs
Time: O(1)
Space: O(n)

Runtime: 44 ms
Memory: 17.5 MB

This is a clever solution that pushes (value, minimum) pairs to the stack
in order to implement all operations in O(1) time complexity.

This solution uses the following intuition:
  - an important invariant of a Stack is that when a new number, which we'll call x, is placed on a Stack,
    the numbers below it will not change for as long as number x remains on the Stack.
    Numbers could come and go above x for the duration of x's presence, but never below.
  - So, whenever number x is the top of the Stack, the minimum will always be the same,
    as it's simply the minimum out of x and all the numbers below it.
------------------------------------------------------------------------
'''
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1]
        self.stack.append((val, min(val, current_min)))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

'''
------------------------------------------------------------------------
Solution 2: Two Stacks
Time: O(1)
Space: O(n)

Runtime: 108 ms
Memory: 16.9 MB

This is an even smarter solution using two stacks (stack and min_stack)
to let us avoid storing the same minimum value over and over again.
The main Stack should keep track of the order numbers arrived (a standard Stack),
and the second Stack should keep track of the current minimum.
------------------------------------------------------------------------
'''
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # If you set < self.min_stack[-1] you'll get an IndexError (list index out of range) for getMin().
        # It's because, if you only add one number for same values, you'll be getting rid of that one number
        # once you pop() one of those values. e.g. [2,1,0,0], [2,1,0] => pop() => [2,1,0], [2,1] => inaccurate
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        print(self.min_stack)
        
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

'''
------------------------------------------------------------------------
Solution 3: Improved Two Stacks
Time: O(1)
Space: O(n)

Runtime: 42 ms
Memory: 16.7 MB

This solution is an improvement to solution 2, fixing the pop() bug described
in the inline comment. It essentially solves by mixing solution 1 and 2,
by appending a (min_val, count) pair to min_stack instead of just min_val.
------------------------------------------------------------------------
'''
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1][0]:
            self.min_stack.append([val,1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1
        
    def pop(self):
        if self.stack[-1] == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1][0]