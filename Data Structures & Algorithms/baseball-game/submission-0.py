class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #Stack 1 Solution --> create a new stack, append and do operations on last or second last value in stack, then sum them all

        stack = []

        for operation in operations:
            if operation == "+":
                #Add the last and second last value in the stack 
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            else:
                #Convert each value to int before adding
                stack.append(int(operation))

        #return the sum of all the values in the stack
        return sum(stack) 
