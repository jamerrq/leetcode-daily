class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mem = dict(knowledge)
        n = len(s)
        ans = []
        curr = ""
        for i in range(n):
            if s[i] == '(':
               ans.append(curr)
               curr = ""
            elif s[i] == ')':
                ans.append(mem.get(curr, '?'))
                curr = ""
            else:
                curr += s[i]
        ans.append(curr)
        return ''.join(ans)