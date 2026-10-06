class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)

        for i, elem in enumerate(seq):
            if elem == '(' and i % 2 or elem == ')' and not i % 2:
                ans[i] = 1

        return ans