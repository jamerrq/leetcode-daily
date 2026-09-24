class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)
        mem = {0: -1}
        csi = 0
        ans = -1
        for i in range(n):
            csi += nums[i]
            mem[csi] = i
            index = mem.get(csi - (s - x))
            if index is not None:
                ans = max(ans, i - index)

        return n - ans if ans != -1 else ans