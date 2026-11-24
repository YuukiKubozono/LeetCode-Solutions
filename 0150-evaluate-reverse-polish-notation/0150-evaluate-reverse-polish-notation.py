class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+" or x == "-" or x == "*" or x == "/":
                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    stack.append(a + b)
                elif x == "-":
                    stack.append(a - b)
                elif x == "*":
                    stack.append(a * b)
                elif x == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(x))
        return stack[-1]