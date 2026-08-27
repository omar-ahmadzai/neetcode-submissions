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
                if not stack or stack.pop() != closing.get(bracket):
                    return False
            else:
                stack.append(bracket)
                
        return not stack
        