class Solution:
    def isValid(self, s: str) -> bool:
        #Stack method --> Create a stack and when we see a closing bracket, check if it matches the opening item on the top of the stack

        stack = []
        closeToOpen = { 
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False