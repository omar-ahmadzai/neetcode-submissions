class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ("+", "-", "*", "/")

        for token in tokens:
            if token in operator:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+": stack.append(num2 + num1)
                if token == "-": stack.append(num2 - num1)
                if token == "*": stack.append(num2 * num1)
                if token == "/": stack.append(int(num2 / num1))

            else:
                stack.append(int(token))
        
        return stack[-1]
