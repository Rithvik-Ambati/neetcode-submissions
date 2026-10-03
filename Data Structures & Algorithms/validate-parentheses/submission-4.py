class Solution:
    def isValid(self, s: str) -> bool:
        """
        logic: lets say i get ({{ then i push them into the stack and if i find corresponding }}), then i pop the stack
        """
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else: 
                if not stack:
                    return False
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False