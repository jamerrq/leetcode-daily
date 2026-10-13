from itertools import pairwise

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        pairs = {}
        pairs_count = 0
        most_frequent_pair_count = 0
        for prev, num in pairwise(nums):
            pair = (prev, num)
            if num < prev:
                pair = (num, prev)

            if num != prev:
                pairs[pair] = pairs.get(pair, 0) + 1
                most_frequent_pair_count = max(
                    most_frequent_pair_count, pairs[pair]
                )
            else:
                pairs_count += 1

        return most_frequent_pair_count + pairs_count