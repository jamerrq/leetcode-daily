class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        s = set()
        n = len(digits)
        for i in range(n):
            first = digits[i]
            if not first:
                continue
            #
            for j in range(n):
                if j == i:
                    continue
                second = digits[j]
                #
                for k in range(n):
                    if k == j or k == i:
                        continue
                    third = digits[k]
                    if third % 2:
                        continue
                    candidate = first * 100 + second * 10 + third
                    s.add(candidate)

        return len(s)

tests = [
    [1,2,3,4],
    [0,2,2],
    [6,6,6],
    [1,3,5]
]

expected = [
    12,
    2,
    1,
    0
]

s = Solution()
for i, test in enumerate(tests):
    res = s.totalNumbers(test)
    assert res == expected[i]
    print(f"test #{i + 1} ok ✅")