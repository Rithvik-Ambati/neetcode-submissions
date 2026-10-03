class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(int(b))
                stack.append(int(a))
                stack.append(int(c))
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                d = int(stack.pop())
                doub = d*2
                stack.append(d)
                stack.append(doub)
            else:
                stack.append(int(operations[i]))

        return sum(stack)
