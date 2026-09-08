class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxil = [[0] for _ in range(len(nums))]
        maxi = 0
        for i in range(len(nums)):
            maxi = max(maxi, nums[i])
            maxil[i][0] = maxi

        mini = float("inf")
        idx = float("inf")

        for i in range(len(nums) - 1, -1, -1):
            mini = min(mini, nums[i])
            if maxil[i][0] - mini <= k:
                idx = min(idx, i)

        return -1 if idx == float("inf") else idx
