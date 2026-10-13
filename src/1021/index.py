class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth, start = 0, 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
                if depth == 1:
                    start = i + 1
            else:
                depth -= 1
                if not depth:
                    ans.append(s[start:i])

        return "".join(ans)
