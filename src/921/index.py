class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth, ans = 0, 0
        for char in s:
            if char == ')':
                if not depth:
                    ans += 1
                    continue
                depth -= 1
            else:
                depth += 1

        return ans + depth