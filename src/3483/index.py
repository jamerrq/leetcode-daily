class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
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
