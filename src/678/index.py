class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack, stars_stack = [], []
        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                stars_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif stars_stack:
                    stars_stack.pop()
                else:
                    return False

        while open_stack and stars_stack:
            if open_stack.pop() > stars_stack.pop():
                return False

        return not open_stack
