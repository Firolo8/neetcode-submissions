class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        for char in s:
            if char in bracketMap:
                # if stack is empty and end of stack(stack[-1]) =               opening braket
                if stack and stack[-1] == bracketMap[char]:
                    stack.pop()
                else : return False
            else : stack.append(char)

        return True if not stack else False