class Solution:
    def minCost(self, n: int) -> int:
        x = 0
        for i in range(1, n + 1):
            a = 1
            b = i - 1
            x += a * b
        return x