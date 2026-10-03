class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        
        for token in tokens:
            if token not in '+-*/':
                s.append(int(token))
            else:
                b = s.pop()
                a = s.pop()
                if token == '+':
                    temp_res = a + b
                elif token == '-':
                    temp_res = a - b
                elif token == '*':
                    temp_res = a * b
                else:
                    temp_res = int(a / b)
                s.append(temp_res)

        return s[-1]