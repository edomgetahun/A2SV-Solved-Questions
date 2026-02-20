n, k = map(int, input().split())
nums = list(map(int, input().split()))
diff = []
for i in range(1, n):
    dif = nums[i] - nums[i-1]
    diff.append(dif)
diff.sort()
ans = 0
end = len(diff) - (k-1)
for j in range(end):
    ans += diff[j]
print(ans)
