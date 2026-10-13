class Solution:
    def minRotations(self, s: str) -> int:
        ans, pointer = 0, 0
        for char in s:
            num = int(char)
            dff = abs(pointer - num)
            ans += min(dff, 10 - dff)
            pointer = num
        return ans