class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = list()

        for bracket in s:
            if bracket in closing:
                if len(stack) == 0:
                    return False
                if stack.pop() != closing.get(bracket):
                    return False
            else:
                stack.append(bracket)
        
        if len(stack) > 0:
            return False
        
        return True