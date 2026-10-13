class Solution:
    def minInsertions(self, s: str) -> int:
        left, ans, index, n = 0, 0, 0, len(s)

        while index < n:
            char = s[index]

            if char == '(':
                left += 1
                index += 1
                continue

            if not left:
                ans += 1
            else:
                left -= 1

            next_char = s[index + 1] if index != n - 1 else ""
            if next_char == ')':
                index += 2
                continue

            ans += 1
            index += 1

        return ans + 2 * left