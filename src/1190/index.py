class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        n = len(s)
        wormhole = [0] * n

        for i in range(n):
            char = s[i]
            if char == '(':
                opened.append(i)
            elif char == ')':
                open_index = opened.pop()
                wormhole[open_index], wormhole[i] = i, open_index

        curr_index = 0
        direction = 1
        ans = []
        while curr_index < n:
            char = s[curr_index]
            if char == '(' or char == ')':
                curr_index = wormhole[curr_index]
                direction *= -1
            else:
                ans.append(s[curr_index])
            curr_index += direction

        return "".join(ans)