from ast import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        klist = []
        n = len(arr)
        while n > 1:
            k_val = max(arr[:n])
            k_idx = arr.index(k_val) + 1
            arr[:k_idx] = reversed(arr[:k_idx])
            klist.append(k_idx)
            arr[:n] = reversed(arr[:n])
            klist.append(n)
            n -= 1
        return klist
