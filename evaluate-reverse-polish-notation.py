'''
------------------
Difficulty: Medium
------------------

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

'''
------------------------------------------------------------------------
Solution 1: Stack & Lookup Table
Time: O(n)
Space: O(n)

Runtime: 102 ms
Memory: 15.5 MB

This is a straightforward solution using a stack and a lookup table.
The intuition is the following: while iterationg a reverse polish notation array,
you would only perform an operation with the latest two integers when you encounter
an operator. This is pretty much guarenteed if you use a stack data structure.

Basically, you would keep adding the integer representation of the elements to
the stack until you encounter an operator. When you find an operator is when you should
perform the corresponding operation with the two elements on the top of the stack.

In order to do that, we use a lookup table where key = string rep of operator, value = operator.operator.
The popping order does matter because division is one of the operations.
Since divisions should truncate towards zero, we cast the divident to a float and later
return the integer representation of the result.

Line 97, 99 shows how operator lookup table could work.

Since it is guarenteed that the given RPN is always valid, the only edge case
to cover here is when the length of input array is less than 3. This means
that there is only one element in the table. Thus, return it.
------------------------------------------------------------------------
'''
class Solution(object):
    def evalRPN(self, tokens):
        n = len(tokens)
        stack = []
        
        if n < 3:
            return tokens[0]
        stack.append(int(tokens[0]))
        stack.append(int(tokens[1]))
        
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.div
        }
        
        for token in tokens[2:]:
            if token in ops:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '/':
                    new_val = int(ops[token](float(val1), val2))
                else:
                    new_val = ops[token](val1, val2)
                stack.append(new_val)
            else:
                stack.append(int(token))
        
        return stack[0]

'''
------------------------------------------------------------------------
Solution 2: Reducing the list in-place
Time: O(n^2)
Space: O(1)

Runtime: 130 ms
Memory: 14.7 MB

This is an alternative solution not using a stack. If you reduce the array
in-place, you could improve space complexity a bit, but will end up with
a much larger time complexity of O(n^2).

The intuition is the following: following the rules of RPN, you perform the
operation once you encounter an operator after keep increasing current position.
Once you have the operation result (taking care of division of course),
you would assign that result to the current position and simply remove
the latest two numbers in the array by popping. You need to decrease current_position
by 1 as well.

This process will result in the input array having only length of 1.
You return that one element at the end.
------------------------------------------------------------------------
'''
class Solution(object):
    def evalRPN(self, tokens):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(float(a) / b),
            "*": lambda a, b: a * b
        }
        
        current_position = 0
        
        while len(tokens) > 1:
            
            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-*/":
                current_position += 1
        
            # Extract the operator and numbers from the list.
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])
            
            # Calculate the result to overwrite the operator with.
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)
            
            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1
        
        return tokens[0]

'''
------------------------------------------------------------------------
Solution 3: Stack (simplified)
Time: O(n)
Space: O(n)

Runtime: 139 ms
Memory: 15.7 MB

This is a slightly simplified version of solution 1. It turns out that
you wouldn't have to worry about the edge case where length of input array
is less than 3 because we eventually just return the stack.pop().

Also, using lambda functions, which allows a bit of customization, lets us
to get rid of if/else statement to control the division truncating to zero.
------------------------------------------------------------------------
'''
class Solution(object):
    def evalRPN(self, tokens):
        operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(float(a) / b),
        "*": lambda a, b: a * b
        }

        stack = []
        for token in tokens:
            if token in operations:
                number_2 = stack.pop()
                number_1 = stack.pop()
                operation = operations[token]
                stack.append(operation(number_1, number_2))
            else:
                stack.append(int(token))
        return stack.pop()