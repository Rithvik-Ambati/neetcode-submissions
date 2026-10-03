class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                A = stack.pop()
                B = stack.pop()

                if token == "+":
                    stack.append(B + A)
                elif token == "-":
                    stack.append(B - A)
                elif token == "*":
                    stack.append(B * A)
                else:  # "/"
                    stack.append(int(B / A))  # truncates toward zero

        return stack[-1]