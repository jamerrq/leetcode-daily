class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(left, right, curr=""):

            if right == n:
                ans.append(curr)
                return

            if left < n:
                backtrack(left + 1, right, f"{curr}(")
            if right < left:
                backtrack(left, right + 1, f"{curr})")

        backtrack(0, 0, "")
        return ans