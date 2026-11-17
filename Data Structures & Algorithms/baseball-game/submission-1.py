class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #Stack 2 --> Use a running total instead of a stack and summing everything in the end
        # if its +, we add the number to our value, C; we subtract from our end value and D; double the top element then add  

        stack, res = [], 0

        for op in operations:
            if op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                res += stack[-1] * 2
                stack.append(stack[-1] *2)
            elif op == "C":
                res -= stack.pop()
            else: 
                res += int(op)
                stack.append(int(op))

        return res