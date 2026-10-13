class Solution:
    def minSwaps(self, s: str) -> int:
        n, depth, ans = len(s), 0, 0
        for i in range(n):
            if s[i] == '[':
                depth += 1
            else:
                if not depth:
                    ans += 1
                    depth += 1
                    continue
                depth -= 1

        return ans