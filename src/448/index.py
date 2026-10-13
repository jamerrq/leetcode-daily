class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        n, curr, index, ans = len(nums), 1, 0, []
        while curr <= n:
            if index >= n:
                ans.append(curr)
                curr += 1
                continue
            num = nums[index]
            if num > curr:
                ans.append(curr)
                curr += 1
            elif num == curr:
                curr += 1
                index += 1
            else:
                index += 1

        return ans