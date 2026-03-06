class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)

        temp = []
        for start, end in requests:
            temp.append((start, 1))
            if end + 1 < n:
                temp.append((end + 1, -1))

        temp.sort()

        diff = [0] * n
        for idx, val in temp:
            diff[idx] += val

        curr = 0
        prefix = [0] * n
        for i in range(n):
            curr += diff[i]
            prefix[i] = curr

        list2 = []
        for i, val in enumerate(prefix):
            list2.append([i, val])

        list2.sort(key=lambda x: x[1], reverse=True)
        nums.sort(reverse=True)

        last = [0] * n
        l = 0
        for r in range(len(list2)):
            index = list2[r][0]
            last[index] = nums[l]
            l += 1

        total = 0
        lastprefix = [0] * n
        for i in range(n):
            total += last[i]
            lastprefix[i] = total

        ans = 0
        for i, j in requests:
            if i != 0:
                ans += lastprefix[j] - lastprefix[i-1]
            else:
                ans += lastprefix[j]
        return ans % (10**9 + 7)






