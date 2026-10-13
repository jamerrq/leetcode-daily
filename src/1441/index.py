class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans = []
        for i in range(1, target[-1] + 1):
            ans.append("Push")
            if i not in target:
                ans.append("Pop")

        return ans