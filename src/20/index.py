class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_d = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or open_d.get(stack.pop()) != char:
                    return False

        return not stack
