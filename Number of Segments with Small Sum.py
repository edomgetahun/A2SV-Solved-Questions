n, s = map(int, input().split())
a = list(map(int, input().split()))
l = 0
curr = 0
res = 0
for r in range(n):
    curr += a[r]
    while curr > s:
        curr -= a[l]
        l += 1
    res += r - l + 1 
print(res)


    


