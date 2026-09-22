class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        P = [0] * k
        ans = [x for x in P]
        #
        for i in range(n):
            T = [0] * k
            if nums[i] % k == 0:
                T[0] = i + 1
                ans[0] += i + 1
            else:
                for ki in range(k):
                    if not P[ki]:
                        continue
                    remainder = (ki * nums[i]) % k
                    T[remainder] += P[ki]
                    ans[remainder] += P[ki]
                T[nums[i] % k] += 1
                ans[nums[i] % k] += 1
            P = [x for x in T]

        return ans