class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # opening bracket
            if ch in '([{':
                stack.append(ch)

            # closing bracket
            else:
                if not stack:
                    return False

                top = stack.pop()
                if pairs[ch] != top:
                    return False

        return len(stack) == 0
        