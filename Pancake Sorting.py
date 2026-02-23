class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_val = max(arr[: size])
            indx = arr.index(max_val)
            if indx != 0:
                arr[: indx+1] = reversed(arr[: indx + 1])
                res.append(indx + 1)
            arr[: size] = reversed(arr[:size])
            res.append(size)
        return res






       
