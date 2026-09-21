class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            index = -ord(s[i]) + 123
            ans += (i + 1) * index
        return ans