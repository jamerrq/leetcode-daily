class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)

        while n > k:
            # slice in blocks
            blocks: list[str] = [s[i:i+k] for i in range(0, n, k)]
            # process all blocks
            digits_sums: list[str] = []
            for block in blocks:
                digit_sum = sum(int(d) for d in block)
                digits_sums.append(str(digit_sum))
            # create new string
            s = "".join(digits_sums)
            # update n
            n = len(s)

        return s