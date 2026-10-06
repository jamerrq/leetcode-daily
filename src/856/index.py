# https://leetcode.com/problems/score-of-parentheses/description
"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        max_depth, depth = len(s) // 2, 0
        stack = [0] * (max_depth + 1)

        for char in s:
            if char == '(':
                depth += 1
                stack[depth] = 0
            else:
                depth -= 1
                prev = stack[depth + 1]
                stack[depth] += 2 * prev if prev else 1

        return stack[0]


# O(1) memory approach
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth, ans = 0, 0

        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    ans += 1 << depth

        return ans
"""


tests = [
    "()",
    "(())",
    "()()",
    "(()(()))",
    "((()))",
    "(()(())())",
    f"{'(' * 25 + ')' * 25}",
    '()' * 25
]

expected = [
    1, 2, 2, 6, 4, 8, 2 ** 24, 25
]

import time

s = Solution()
total_time = 0

for i, test in enumerate(tests):
    start_time = time.perf_counter()
    res = s.scoreOfParentheses(test)
    end_time = time.perf_counter()

    total_time += end_time - start_time

    if res == expected[i]:
        print(f"test #{i + 1} ok ✅")
    else:
        print(f"test #{i + 1} failed. result={res}, expected={expected[i]}")

print()

# Calculate and print execution time
print(f"Execution time: {total_time:.6f} seconds")