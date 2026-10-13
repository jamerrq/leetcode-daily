class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # alternative: shunting yard
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                op = token
                B, A = stack.pop(), stack.pop()
                C = A + B
                match op:
                    case '-':
                        C = A - B
                    case '*':
                        C = A * B
                    case '/':
                        C = int(A / B)
                stack.append(C)

        return stack[0]


if __name__ == "__main__":
    cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]
    sol = Solution()
    for tokens, expected in cases:
        got = sol.evalRPN(tokens)
        assert got == expected, f"evalRPN({tokens}) = {got}, expected {expected}"
        print(f"evalRPN({tokens}) = {got}")