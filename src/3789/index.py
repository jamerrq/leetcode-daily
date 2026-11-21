class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        if cost1 + cost2 <= costBoth:
            return need1 * cost1 + need2 * cost2
        type3 = min(need1, need2)
        ans = costBoth * type3
        if need1 > type3:
            ans += (need1 - type3) * min(cost1, costBoth)
        if need2 > type3:
            ans += (need2 - type3) * min(cost2, costBoth)

        return ans
